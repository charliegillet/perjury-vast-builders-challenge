"""§4 routing table + promotion state (claim_types.yaml, cache/promotion.json)."""
import json

import pytest

from perjury.router import DEMOTED_REASON, Router
from perjury.types import Atom, AtomType


@pytest.fixture
def router(tmp_path):
    return Router(promotion_path=tmp_path / "absent.json")


def A(t, **kw):
    return Atom(id="a1", span="x", type=t, **kw)


def test_every_atom_type_is_in_the_table(router):
    assert set(router.types) == {t.value for t in AtomType}


@pytest.mark.parametrize("t,rule,tiers,hard", [
    (AtomType.scene_identity, "metadata_match", ["RECORDS"], True),
    (AtomType.road_surface, "scene_majority", ["CAPTIONS", "JURY"], True),
    (AtomType.weather, "scene_majority", ["CAPTIONS", "JURY"], True),
    (AtomType.traffic_state, "scene_majority", ["CAPTIONS", "JURY"], True),
    (AtomType.lighting, "scene_majority", ["JURY"], True),
    (AtomType.coco_presence, "coco_presence", ["RECORDS", "JURY"], True),
    (AtomType.count, "count_lower_bound", ["RECORDS"], True),
    (AtomType.towing, "presence_jury", ["CAPTIONS", "JURY"], True),
    (AtomType.heavy_vehicle_kind, "heavy_vehicle_jury", ["JURY"], False),   # demoted until the bench promotes it
])
def test_routes(router, t, rule, tiers, hard):
    r = router.route(A(t))
    assert (r.rule, r.tiers, r.hard) == (rule, tiers, hard)


@pytest.mark.parametrize("t,code", [
    (AtomType.action, "temporal"), (AtomType.attribute, "attribute"), (AtomType.identity_intent, "not_observable"),
    (AtomType.cross_camera, "cross_camera"), (AtomType.lane_position, "lane_position"), (AtomType.other, "other"),
])
def test_unverifiable_types(router, t, code):
    r = router.route(A(t))
    assert r.rule == "unverifiable" and not r.hard and r.reason_code == code and r.reason_if_unverifiable


def test_plates_are_never(router):
    r = router.route(A(AtomType.attribute, value="plate"))
    assert r.reason_code == "never" and "never" in r.reason_if_unverifiable.lower()


def test_unknown_type_is_unverifiable(tmp_path):
    p = tmp_path / "types.yaml"
    p.write_text("types:\n  towing: {tiers: [JURY], hard: true, rule: presence_jury, promoted: true}\n")
    r = Router(types_path=p, promotion_path=None).route(A(AtomType.weather))
    assert r.rule == "unverifiable" and r.reason_code == "unrouted"


def test_heavy_vehicle_demoted_by_default(router):
    r = router.route(A(AtomType.heavy_vehicle_kind, value="semi"))
    assert r.demoted and r.reason_if_unverifiable == DEMOTED_REASON and r.reason_code == "demoted_by_bench"


def test_frozen_promotion_overrides_defaults(tmp_path):
    p = tmp_path / "promotion.json"
    p.write_text(json.dumps({"frozen_at": "2026-10-02T14:00:00", "types": {
        "towing": {"promoted": False, "catch": 0.6, "false_accusation": 0.2, "n": 7},
        "heavy_vehicle_kind": {"promoted": True, "catch": 0.9, "false_accusation": 0.0, "n": 6}},
        "alpha": {"towing": 0.1}, "m": {"towing": 3}}))
    r = Router(promotion_path=p)
    tow = r.route(A(AtomType.towing))
    assert tow.demoted and not tow.hard and tow.reason_if_unverifiable == DEMOTED_REASON
    assert tow.alpha == 0.1 and tow.m == 3
    assert r.route(A(AtomType.heavy_vehicle_kind)).hard
    assert r.state()["towing"]["catch"] == 0.6
    assert Router(promotion_path=p, ignore_promotion=True).route(A(AtomType.towing)).hard


def test_m_from_alpha_prior(router):
    assert router.alpha("towing") == 0.27
    assert router.m("towing", 6) == 4
    assert router.route(A(AtomType.towing)).m == 4


def test_value_config(router):
    snow = router.value_cfg(A(AtomType.road_surface, value="snow"))
    assert snow["option"] == "C" and "slush" in snow["synonyms"]
    assert router.value_cfg(A(AtomType.traffic_state, value="stop_and_go"))["option"] == "C"
    assert router.value_cfg(A(AtomType.lighting, value="night"))["option"] == "C"
