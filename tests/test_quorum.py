"""§7 quorum math and verdict rules (perjury/quorum.py is pure: no clients, no I/O)."""
import pytest

from perjury import quorum as q
from perjury.types import Atom, AtomType, AtomVerdict

# §7 table: alpha (k = 6) -> P(Y>=2), P(Y>=3), P(Y>=4), m chosen
TABLE = [
    (0.05, 0.033, 0.002, None, 2),
    (0.10, 0.114, 0.016, None, 3),
    (0.20, 0.345, 0.099, 0.017, 4),
    (0.27, None, 0.202, 0.049, 4),
]


@pytest.mark.parametrize("alpha,p2,p3,p4,m", TABLE)
def test_alpha_to_m_table(alpha, p2, p3, p4, m):
    assert q.choose_m(alpha, k=6) == m
    for mm, p in ((2, p2), (3, p3), (4, p4)):
        if p is not None:
            assert q.p_at_least(mm, 6, alpha) == pytest.approx(p, abs=0.001)


def test_choose_m_demotes_when_m_would_be_5_or_more():
    assert q.choose_m(0.40, k=6) is None
    assert q.choose_m(0.27, k=16) is None          # 16 jurors at alpha 0.27 need m > 4


def test_p_at_least_edges():
    assert q.p_at_least(0, 6, 0.3) == 1.0
    assert q.p_at_least(7, 6, 0.3) == 0.0
    assert q.p_at_least(1, 6, 0.0) == 0.0


def test_wilson_ci():
    lo, hi = q.wilson_ci(9, 10)
    assert lo == pytest.approx(0.596, abs=0.002) and hi == pytest.approx(0.982, abs=0.002)
    assert q.wilson_ci(0, 0) == (0.0, 1.0)
    lo, hi = q.wilson_ci(0, 10)
    assert lo == 0.0 and hi == pytest.approx(0.278, abs=0.002)


# ---- presence (§7: SUPPORTED Y>=m; CONTRADICTED needs all four conditions) ----
def test_presence_supported_at_quorum():
    assert q.presence_verdict(4, 2, 6, 4, retrieved_top=True, t1_supports=0).verdict == "SUPPORTED"
    assert q.presence_verdict(3, 3, 6, 4, retrieved_top=True, t1_supports=5).verdict == "UNVERIFIABLE"


def test_presence_contradicted_needs_all_four():
    ok = dict(retrieved_top=True, t1_supports=0)
    assert q.presence_verdict(0, 6, 6, 4, **ok).verdict == "CONTRADICTED"
    assert q.presence_verdict(0, 5, 6, 4, **ok).verdict == "CONTRADICTED"                  # k' = 5 of 6
    assert q.presence_verdict(1, 5, 6, 4, **ok).verdict == "UNVERIFIABLE"                  # Y != 0
    assert q.presence_verdict(0, 4, 6, 4, **ok).verdict == "UNVERIFIABLE"                  # k' = 4 < 5
    assert q.presence_verdict(0, 6, 6, 4, retrieved_top=False, t1_supports=0).verdict == "UNVERIFIABLE"
    assert q.presence_verdict(0, 6, 6, 4, retrieved_top=True, t1_supports=1).verdict == "UNVERIFIABLE"
    assert q.presence_verdict(0, 6, 6, 4, retrieved_top=True, t1_supports=0,
                              t1_complete=False).verdict == "UNVERIFIABLE"               # T1 silence unproven


def test_presence_scales_min_valid_with_jury_size():
    assert q.min_valid_for_absence(6) == 5
    assert q.min_valid_for_absence(16) == 14
    assert q.presence_verdict(0, 13, 16, None, retrieved_top=True, t1_supports=0).verdict == "UNVERIFIABLE"
    assert q.presence_verdict(0, 14, 16, None, retrieved_top=True, t1_supports=0).verdict == "CONTRADICTED"


# ---- scene-wide majority (§7: ceil(2/3 k'), k' >= 8, T1 guard) ----
def test_scene_majority():
    sixteen_c = ["C"] * 14 + ["B", "D"]
    r = q.scene_majority_verdict(sixteen_c, "C", t1_supports=10, t1_contradicts=0)
    assert r.verdict == "SUPPORTED" and r.stats["k_valid"] == 15 and r.stats["need"] == 10
    assert q.scene_majority_verdict(sixteen_c, "A").verdict == "CONTRADICTED"
    # captions net-supporting the claim block a contradiction
    assert q.scene_majority_verdict(sixteen_c, "A", t1_supports=3, t1_contradicts=1).verdict == "UNVERIFIABLE"
    # captions contradicting more than supporting block support
    assert q.scene_majority_verdict(sixteen_c, "C", t1_supports=1, t1_contradicts=4).verdict == "UNVERIFIABLE"


def test_scene_majority_needs_8_valid_and_two_thirds():
    assert q.scene_majority_verdict(["C"] * 7 + ["D"] * 9, "C").verdict == "UNVERIFIABLE"
    assert q.two_thirds(9) == 6
    assert q.scene_majority_verdict(["C"] * 6 + ["A"] * 3, "C").verdict == "SUPPORTED"
    assert q.scene_majority_verdict(["C"] * 5 + ["A"] * 4, "C").verdict == "UNVERIFIABLE"
    assert q.scene_majority_verdict([None] * 4 + ["C"] * 8, "C").verdict == "SUPPORTED"


# ---- COCO (§7: noise floor >= 3 consecutive frames; >= 14/16 jury zeros) ----
def test_coco_absence_noise_floor_and_jury():
    sign_noise = {"p1c1": 2, "p1c2": 1, "p2c1": 0}
    zeros16 = [0] * 16
    assert q.coco_absence_verdict(sign_noise, zeros16).verdict == "CONTRADICTED"
    assert q.coco_absence_verdict({"p1c1": 3}, zeros16).verdict == "UNVERIFIABLE"        # at the floor
    assert q.coco_absence_verdict({}, [0] * 14 + [None] * 2).verdict == "CONTRADICTED"   # rest abstain
    assert q.coco_absence_verdict({}, [0] * 13 + [None] * 3).verdict == "UNVERIFIABLE"
    assert q.coco_absence_verdict({}, [0] * 15 + [1]).verdict == "UNVERIFIABLE"          # one juror saw it
    assert q.coco_absence_verdict({}, None).verdict == "UNVERIFIABLE"                    # no jury leg


def test_coco_presence():
    assert q.coco_presence_verdict({"a": 5, "b": 9}, [1, 2, 0]).verdict == "SUPPORTED"
    assert q.coco_presence_verdict({"a": 5}, [1, 2, 0]).verdict == "UNVERIFIABLE"        # 1 camera
    assert q.coco_presence_verdict({"a": 5, "b": 9}, [1, 0, 0]).verdict == "UNVERIFIABLE"
    assert q.coco_presence_verdict({"a": 90, "b": 90}, None).verdict == "SUPPORTED"      # car/truck/bus: YOLO only


def test_coco_verdict_negation():
    assert q.coco_verdict({}, [0] * 16).verdict == "CONTRADICTED"
    assert q.coco_verdict({}, [0] * 16, negated=True).verdict == "SUPPORTED"
    assert q.coco_verdict({"a": 9, "b": 9}, [2, 1], negated=True).verdict == "CONTRADICTED"


def test_count_lower_bound_never_contradicts():
    peaks = {"a": 3, "b": 4, "c": 1}
    assert q.count_lower_bound_verdict(peaks, 2, "at_least").verdict == "SUPPORTED"
    assert q.count_lower_bound_verdict(peaks, 4, "at_least").verdict == "UNVERIFIABLE"
    assert q.count_lower_bound_verdict(peaks, 3, "exact").verdict == "UNVERIFIABLE"
    assert q.count_lower_bound_verdict(peaks, 99, "at_most").verdict == "UNVERIFIABLE"


# ---- claim level + MOOT ----
def _av(i, v):
    return AtomVerdict(atom_id=i, verdict=v, reason="")


def test_claim_verdict_rules():
    assert q.claim_verdict([_av("a1", "SUPPORTED"), _av("a2", "CONTRADICTED")]) == "FALSE"
    assert q.claim_verdict([_av("a1", "SUPPORTED"), _av("a2", "MOOT")]) == "TRUE"
    assert q.claim_verdict([_av("a1", "SUPPORTED"), _av("a2", "UNVERIFIABLE")]) == "UNPROVEN"
    assert q.claim_verdict([]) == "UNPROVEN"
    assert q.claim_verdict([_av("a1", "MOOT")]) == "UNPROVEN"


def test_moot_propagates_through_dependencies():
    atoms = [Atom(id="a1", span="Three", type=AtomType.count, cls="person", count=3, depends_on="a2"),
             Atom(id="a2", span="pedestrians", type=AtomType.coco_presence, cls="person"),
             Atom(id="a3", span="crossing", type=AtomType.action, depends_on="a2"),
             Atom(id="a4", span="snow", type=AtomType.road_surface, value="snow")]
    labels = {"a1": "UNVERIFIABLE", "a2": "CONTRADICTED", "a3": "UNVERIFIABLE", "a4": "SUPPORTED"}
    assert q.moot_ids(atoms, labels) == {"a1", "a3"}
    avs = [_av(k, v) for k, v in labels.items()]
    assert q.claim_verdict(avs, atoms) == "FALSE"
    # a cycle must not recurse forever
    cyc = [Atom(id="x", span="x", type=AtomType.action, depends_on="y"),
           Atom(id="y", span="y", type=AtomType.action, depends_on="x")]
    assert q.moot_ids(cyc, {"x": "UNVERIFIABLE", "y": "UNVERIFIABLE"}) == set()
