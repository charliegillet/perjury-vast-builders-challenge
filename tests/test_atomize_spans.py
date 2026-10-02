"""§6 atomizer: spans are exact substrings (code-validated), closed type set, COCO mapping, rules fallback."""
import asyncio

import pytest

from perjury.atomize import atomize, canonical, rules_parse, validate_llm_atoms
from perjury.types import AtomType as T


def by(atoms, t):
    return [a for a in atoms if a.type == t]


def one(atoms, t):
    xs = by(atoms, t)
    assert len(xs) == 1, (t, atoms)
    return xs[0]


def ids(atoms):
    return {a.id: a for a in atoms}


# (text, expected atoms as (type, span, extra fields))
GOLDEN = [
    ("A pickup is towing a trailer", [(T.towing, "A pickup is towing a trailer", {"towing_vehicle": "pickup"})]),
    ("an SUV pulling a camper", [(T.towing, "an SUV pulling a camper", {"towing_vehicle": "suv"})]),
    ("a vehicle towing a trailer", [(T.towing, "a vehicle towing a trailer", {"towing_vehicle": "any"})]),
    ("The road is covered in snow", [(T.road_surface, "covered in snow", {"value": "snow"})]),
    ("There is snow beside the road", [(T.road_surface, "snow beside the road", {"value": "snow"})]),
    ("Traffic is at a standstill", [(T.traffic_state, "at a standstill", {"value": "stop_and_go"})]),
    ("stop-and-go traffic", [(T.traffic_state, "stop-and-go", {"value": "stop_and_go"})]),
    ("Traffic is flowing freely at speed", [(T.traffic_state, "flowing freely at speed", {"value": "free_flow"})]),
    ("Traffic flows freely", [(T.traffic_state, "flows freely", {"value": "free_flow"})]),
    ("It is nighttime", [(T.lighting, "nighttime", {"value": "night"})]),
    ("It is daytime", [(T.lighting, "daytime", {"value": "day"})]),
    ("There are trucks on the highway", [(T.coco_presence, "trucks", {"cls": "truck"}),
                                         (T.scene_identity, "highway", {})]),
    ("Cars travel in both directions", [(T.coco_presence, "Cars", {"cls": "car"}),
                                        (T.lane_position, "in both directions", {})]),
    ("The white truck braked hard", [(T.attribute, "white", {"value": "color"}), (T.coco_presence, "truck", {"cls": "truck"}),
                                     (T.action, "braked hard", {"value": "braking"})]),
    ("A car changed into the left lane", [(T.coco_presence, "car", {"cls": "car"}),
                                          (T.action, "changed into", {"value": "lane_change"}),
                                          (T.lane_position, "the left lane", {})]),
    ("The pickup's driver was texting", [(T.coco_presence, "pickup", {"cls": "truck"}),
                                         (T.identity_intent, "driver was texting", {})]),
    ("The SUV was doing 90 mph", [(T.coco_presence, "SUV", {"cls": "car"}), (T.action, "doing 90 mph", {"value": "speed"})]),
    ("The same truck appears on five cameras", [(T.cross_camera, "The same truck appears on five cameras", {})]),
    ("The plate reads ABC123", [(T.attribute, "The plate reads ABC123", {"value": "plate"})]),
    ("It's a FedEx truck", [(T.attribute, "FedEx", {"value": "brand"}), (T.coco_presence, "truck", {"cls": "truck"})]),
    ("Exactly 23 cars are visible", [(T.count, "Exactly 23", {"count": 23, "count_op": "exact", "cls": "car"}),
                                     (T.coco_presence, "cars", {"cls": "car"})]),
    ("Two cars collided", [(T.count, "Two", {"count": 2, "cls": "car"}), (T.coco_presence, "cars", {"cls": "car"}),
                           (T.action, "collided", {"value": "collision"})]),
    ("A cyclist is riding on the shoulder", [(T.coco_presence, "cyclist", {"cls": "bicycle"}),
                                             (T.action, "riding", {}), (T.lane_position, "on the shoulder", {})]),
    ("There are at least two trucks", [(T.count, "at least two", {"count": 2, "count_op": "at_least"}),
                                       (T.coco_presence, "trucks", {"cls": "truck"})]),
    ("It is nighttime and raining", [(T.lighting, "nighttime", {}), (T.weather, "raining", {"value": "rain"})]),
    ("A cyclist on a snowy highway", [(T.coco_presence, "cyclist", {"cls": "bicycle"}),
                                      (T.road_surface, "snowy", {"value": "snow"}), (T.scene_identity, "highway", {})]),
    ("The camera is in Toronto", [(T.scene_identity, "Toronto", {"value": "toronto"})]),
    ("A semi-truck passes", [(T.heavy_vehicle_kind, "semi-truck", {"value": "semi"}), (T.action, "passes", {})]),
]


@pytest.mark.parametrize("text,expected", GOLDEN, ids=[g[0] for g in GOLDEN])
def test_rules_golden(text, expected):
    atoms = rules_parse(text)
    got = sorted((a.type, a.span) for a in atoms)
    assert got == sorted((t, s) for t, s, _ in expected)
    for t, s, extra in expected:
        a = next(a for a in atoms if a.type == t and a.span == s)
        for k, v in extra.items():
            assert getattr(a, k) == v, (text, k)
    for a in atoms:
        assert a.span in text


def test_hero_compound_claim():
    text = "Three pedestrians are crossing the highway in the snow"
    atoms = rules_parse(text)
    person = one(atoms, T.coco_presence)
    assert (person.span, person.cls, person.negated) == ("pedestrians", "person", False)
    count = one(atoms, T.count)
    assert (count.span, count.count, count.count_op, count.depends_on) == ("Three", 3, "exact", person.id)
    crossing = one(atoms, T.action)
    assert crossing.span == "crossing" and crossing.depends_on == person.id
    assert one(atoms, T.road_surface).value == "snow"
    assert one(atoms, T.scene_identity).span == "highway"
    assert len(atoms) == 5


def test_dependents_point_at_their_subject():
    atoms = rules_parse("The white truck braked hard")
    truck = one(atoms, T.coco_presence)
    assert one(atoms, T.attribute).depends_on == truck.id
    assert one(atoms, T.action).depends_on == truck.id
    assert one(rules_parse("The plate reads ABC123"), T.attribute).depends_on is None


def test_negation():
    a = one(rules_parse("There are no pedestrians"), T.coco_presence)
    assert a.cls == "person" and a.negated
    a = one(rules_parse("Nobody is on the road"), T.coco_presence)
    assert a.cls == "person" and a.negated


def test_more_than_is_lower_bound_plus_one():
    c = one(rules_parse("more than 5 cars"), T.count)
    assert (c.count, c.count_op) == (6, "at_least")


def test_unparseable_is_other_and_empty_is_empty():
    atoms = rules_parse("  blah blah  ")
    assert [(a.type, a.span) for a in atoms] == [(T.other, "blah blah")]
    assert rules_parse("   ") == []


def test_canonical_statements():
    atoms = {a.type: a for a in rules_parse("Three pedestrians are crossing the highway in the snow")}
    assert canonical(atoms[T.road_surface]) == "There is snow or slush on or beside the road."
    assert canonical(atoms[T.coco_presence]) == "There is at least one person visible."
    assert canonical(atoms[T.count]) == "There are exactly 3 people visible."
    assert canonical(one(rules_parse("an SUV pulling a camper"), T.towing)) == "An SUV is towing a separate trailer."


# ---- LLM path (mocked) ----
class StubLLM:
    def __init__(self, reply=None, exc=None):
        self.reply, self.exc, self.calls = reply, exc, []

    async def complete_json(self, system, user, *, temperature=0.0, max_tokens=1200, bus=None, purpose=""):
        self.calls.append((system, user, purpose))
        if self.exc:
            raise self.exc
        return self.reply


def run(text, llm):
    return asyncio.run(atomize(text, llm))


def test_llm_atoms_validated_and_hallucinated_span_dropped():
    text = "Three pedestrians are crossing the highway in the snow"
    reply = {"atoms": [
        {"id": "a1", "span": "pedestrians", "type": "coco_presence", "class": "pedestrian", "count": 3},
        {"id": "a2", "span": "crossing", "type": "action", "value": "crossing", "depends_on": "a1"},
        {"id": "a3", "span": "in the snow", "type": "road_surface", "value": "snowy"},
        {"id": "a4", "span": "highway", "type": "scene_identity"},
        {"id": "a5", "span": "a red pickup truck", "type": "coco_presence", "class": "truck"},   # not in the text
        {"id": "a6", "span": "Pedestrians", "type": "coco_presence", "class": "person"},       # case differs: dropped
    ]}
    llm = StubLLM(reply)
    atoms, parser = run(text, llm)
    assert parser == "llm" and llm.calls[0][2] == "atomize"
    assert "untrusted data" in llm.calls[0][0]
    assert all(a.span in text for a in atoms)
    assert not any(a.span in ("a red pickup truck", "Pedestrians") for a in atoms)
    person = one(atoms, T.coco_presence)
    assert person.cls == "person"
    count = one(atoms, T.count)                       # rule 5: the count is split out with depends_on
    assert (count.span, count.count, count.depends_on) == ("Three", 3, person.id)
    assert one(atoms, T.action).depends_on == person.id
    assert one(atoms, T.road_surface).value == "snow"   # normalized
    assert len(ids(atoms)) == len(atoms)


def test_llm_closed_type_set_and_class_mapping():
    text = "A cyclist and a dragon are here"
    reply = {"atoms": [{"id": "a1", "span": "cyclist", "type": "coco_presence", "class": "cyclist"},
                       {"id": "a2", "span": "dragon", "type": "coco_presence", "class": "dragon"},
                       {"id": "a3", "span": "here", "type": "vibes"}]}
    atoms, _ = run(text, StubLLM(reply))
    assert one(atoms, T.coco_presence).cls == "bicycle"
    assert sorted(a.span for a in by(atoms, T.other)) == ["dragon", "here"]


def test_llm_one_towing_atom():
    text = "A pickup is towing a trailer"
    reply = {"atoms": [{"id": "a1", "span": "A pickup is towing a trailer", "type": "towing", "towing_vehicle": "pickup"},
                       {"id": "a2", "span": "pickup", "type": "coco_presence", "class": "truck"},
                       {"id": "a3", "span": "trailer", "type": "coco_presence", "class": "truck"}]}
    atoms, _ = run(text, StubLLM(reply))
    assert [(a.type, a.towing_vehicle) for a in atoms] == [(T.towing, "pickup")]


def test_llm_count_without_parent_gets_one():
    text = "Exactly 23 cars are visible"
    atoms, _ = run(text, StubLLM({"atoms": [{"id": "a1", "span": "Exactly 23 cars", "type": "count", "class": "car",
                                             "count": 23}]}))
    c = one(atoms, T.count)
    p = one(atoms, T.coco_presence)
    assert c.depends_on == p.id and c.count_op == "exact" and p.span == "cars"


def test_llm_cycle_is_broken():
    text = "The truck braked hard"
    reply = {"atoms": [{"id": "a1", "span": "truck", "type": "coco_presence", "class": "truck", "depends_on": "a2"},
                       {"id": "a2", "span": "braked hard", "type": "action", "depends_on": "a1"}]}
    atoms, _ = run(text, StubLLM(reply))
    assert one(atoms, T.coco_presence).depends_on is None
    assert one(atoms, T.action).depends_on == one(atoms, T.coco_presence).id


@pytest.mark.parametrize("llm", [StubLLM(exc=RuntimeError("429 Too Many Requests")), StubLLM(reply=None),
                                 StubLLM(reply={"atoms": []}), StubLLM(reply={"atoms": [{"span": "nope", "type": "x"}]}),
                                 StubLLM(reply="not json"), None])
def test_rules_fallback(llm):
    atoms, parser = run("A pickup is towing a trailer", llm)
    assert parser == "rules"
    assert [(a.type, a.span) for a in atoms] == [(T.towing, "A pickup is towing a trailer")]


def test_validate_handles_garbage():
    assert validate_llm_atoms("x", None) == []
    assert validate_llm_atoms("x", {"atoms": "nope"}) == []
    assert validate_llm_atoms("x", [{"span": 3}]) == []
