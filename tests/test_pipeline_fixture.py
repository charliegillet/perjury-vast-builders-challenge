"""testify() end to end (§5, §7, §9).

Part 1 uses tiny in-test stub clients over cache/fixture_i24_index.json + cache/fixture_scene_probes.json (no fakes).
Part 2 runs the §14 demo through perjury.fakes (PERJURY_MODE=fixture, PERJURY_FIXTURE_LATENCY=0).
"""
import asyncio
import json
from types import SimpleNamespace

import pytest

from perjury.config import Settings
from perjury.events import EventBus
from perjury.index import SceneIndex
from perjury import pipeline
from perjury.pipeline import Context
from perjury.probes import P_GROUND, P_TOW
from perjury.router import Router

ENV = {"PERJURY_MODE": "fixture", "PERJURY_FIXTURE_LATENCY": "0"}
TOW_WORDS = ("trailer", "pulling")


# ---------------------------------------------------------------------------------------------------- stubs
class StubLLM:
    async def complete_json(self, system, user, *, temperature=0.0, max_tokens=1200, bus=None, purpose=""):
        if purpose == "atomize":
            raise RuntimeError("429")                  # forces the rules parser
        return {"labels": []}                          # T1: everything SILENT


class StubMedia:
    async def keyframes(self, source, times, width=1920):
        return [f"{source}|{t}".encode() for t in times]

    def grid2x2(self, frames, labels=None):
        return b"GRID\n" + b"\n".join(frames)

    async def crop_clip(self, source, t, box_px, dur=0.5):
        return b"CROP"


class StubCosmos:
    def __init__(self, tow_sources, delay=0.0):
        self.tow, self.delay, self.prompts = tow_sources, delay, []

    async def probe(self, image_jpeg, prompt, probe_version, *, timeout_s, bus=None):
        self.prompts.append((probe_version, prompt))
        await asyncio.sleep(self.delay)
        if probe_version.startswith("P-GROUND"):
            parsed = {"bbox_2d": [400, 400, 600, 600]}
        else:
            src = image_jpeg.split(b"\n")[1].split(b"|")[0].decode()
            tows = [{"towing_vehicle": "pickup", "trailer": "utility"}] if src in self.tow else []
            parsed = {"panels": [{"panel": p, "towing": tows if p == 2 else [], "semis": 0, "visibility": "clear"}
                                 for p in (1, 2, 3, 4)]}
        return SimpleNamespace(parsed=parsed, raw_text="", latency_ms=5, cached=False, cached_at=None,
                               image_sha="x", error=None)


class StubEmbed:
    def __init__(self, tow_sources, vectors=True):
        self.tow, self.vectors = tow_sources, vectors

    async def embed_text(self, text, *, bus=None):
        return [1.0, 0.0]

    def visual_vectors(self):
        if not self.vectors:
            return None
        return {s: ([1.0, 0.0] if s in self.tow else [0.0, 1.0]) for s in ALL_SOURCES}


class StubYolo:
    def __init__(self, ok=True):
        self.ok = ok

    async def zoom_check(self, crop_mp4, crop_url, *, min_cover=0.30, bus=None):
        return SimpleNamespace(ok=self.ok, label="truck", conf=0.8, cover=0.5, frames_ok=2, error=None)


class StubVSS:
    async def search_and_answer(self, claim, camera_id, *, bus=None):
        return {"answer": "TRUE. Looks consistent.", "hits": 15}


S = Settings(env=ENV)
INDEX = SceneIndex.load(S.index_path)
PROBES = json.loads(S.probes_path.read_text())
ALL_SOURCES = [s.source for sc in INDEX.scenes() for s in INDEX.segments(sc)]
# stub "truth": segments whose caption mentions a trailer (S1/S3 only)
TOW = {s.source for sc in INDEX.scenes() for s in INDEX.segments(sc) if any(w in s.caption for w in TOW_WORDS)}


def stub_ctx(*, cosmos_delay=0.0, vectors=True, zoom_ok=True, env=None):
    s = Settings(env={**ENV, **(env or {})})
    cosmos = StubCosmos(TOW, cosmos_delay)
    clients = SimpleNamespace(llm=StubLLM(), media=StubMedia(), cosmos=cosmos, embed=StubEmbed(TOW, vectors),
                              yolo=StubYolo(zoom_ok), vss=StubVSS(), canary=None)
    return Context(settings=s, clients=clients, index=INDEX, probes=PROBES, router=Router(promotion_path=None))


def run(text, scene, ctx, **kw):
    bus = EventBus("t-run")
    cv = asyncio.run(pipeline.testify(text, scene, ctx, bus, **kw))
    return cv, bus.events


def verdicts(cv):
    return {a.span: v.verdict for a, v in zip(cv.atoms, cv.atom_verdicts)}


def names(events):
    """Event names without the ribbon's `service` chips (they interleave anywhere)."""
    return [e["event"] for e in events if e["event"] != "service"]


# ---------------------------------------------------------------------------------------------------- part 1
def test_event_order_and_receipt():
    cv, evs = run("Three pedestrians are crossing the highway in the snow", 2, stub_ctx(), stock_ab=True)
    n = names(evs)
    assert n[:3] == ["run", "transcript", "atoms"]
    assert n[-1] == "done" and n.count("done") == 1
    assert n.index("verdict") < n.index("stock") < n.index("receipt") < n.index("done")
    assert all(n.index("atoms") < i < n.index("verdict") for i, x in enumerate(n) if x == "atom_verdict")
    assert n.count("atom_verdict") == len(cv.atoms) == 5
    rc = next(e["data"] for e in evs if e["event"] == "receipt")
    assert rc["verdict"] == "FALSE" and rc["total"] == 13 and rc["mode"] == "fixture"
    stock = next(e["data"] for e in evs if e["event"] == "stock")
    assert stock["classification"] == "TRUE" and "Start your answer with TRUE" in stock["query"]
    assert next(e["data"] for e in evs if e["event"] == "atoms")["parser"] == "rules"


def test_pedestrians_snow_compound_is_false_with_moots():
    cv, evs = run("Three pedestrians are crossing the highway in the snow", 2, stub_ctx())
    assert cv.verdict == "FALSE"
    assert verdicts(cv) == {"Three": "MOOT", "pedestrians": "CONTRADICTED", "crossing": "MOOT",
                            "highway": "SUPPORTED", "in the snow": "SUPPORTED"}
    ped = next(v for a, v in zip(cv.atoms, cv.atom_verdicts) if a.span == "pedestrians")
    assert ped.stats["pill"] == "YOLO: person in 0 of 192 segments · jury: 0 people seen by 16/16"
    assert ped.reason == "No person was detected in any of 192 segments; 16/16 cameras count 0."
    juror_evs = [e["data"] for e in evs if e["event"] == "juror"]
    assert all(e["vote"]["cached"] for e in juror_evs)              # scene-wide jurors are pre-run: 0 live GPU


def test_towing_true_and_false_and_jurors_never_see_the_claim():
    ctx = stub_ctx()
    claim = "A pickup is towing a trailer"
    cv1, evs1 = run(claim, 1, ctx)
    assert cv1.verdict == "TRUE"
    av = cv1.atom_verdicts[0]
    assert av.stats["Y"] >= av.stats["m"] == 4 and av.tiers == ["JURY"]
    assert {"summon", "juror", "ground", "zoom"} <= set(names(evs1))
    summon = next(e["data"] for e in evs1 if e["event"] == "summon")
    assert summon["retrieval"] == "embed1+yolo" and len(summon["jurors"]) == 6
    assert len({j["camera"] for j in summon["jurors"]}) == 6        # one moment per camera
    cv2, _ = run(claim, 2, ctx)
    assert cv2.verdict == "FALSE" and cv2.atom_verdicts[0].reason_code == "absent_everywhere"
    # jurors never see the claim: every Cosmos prompt is a fixed, pre-written probe
    assert ctx.clients.cosmos.prompts
    for version, prompt in ctx.clients.cosmos.prompts:
        assert prompt in (P_TOW.prompt, P_GROUND.prompt) and version in (P_TOW.version, P_GROUND.version)
        assert claim.lower() not in prompt.lower()


def test_failed_zoom_check_votes_do_not_count():
    cv, _ = run("A pickup is towing a trailer", 1, stub_ctx(zoom_ok=False))
    av = cv.atom_verdicts[0]
    assert cv.verdict == "UNPROVEN" and av.stats["Y"] == 0 and av.stats["yes_raw"] >= 4


def test_yolo_rank_fallback_without_vectors():
    cv, evs = run("A pickup is towing a trailer", 2, stub_ctx(vectors=False))
    summon = next(e["data"] for e in evs if e["event"] == "summon")
    assert summon["retrieval"] == "yolo" and "YOLO truck-count rank alone" in summon["note"]
    assert cv.atom_verdicts[0].stats["retrieval"] == "yolo"


def test_juror_timeout_abstains_and_atom_is_unverifiable():
    ctx = stub_ctx(cosmos_delay=0.3, env={"PERJURY_JUROR_TIMEOUT_S": "0.05"})
    cv, evs = run("A pickup is towing a trailer", 1, ctx)
    av = cv.atom_verdicts[0]
    assert av.verdict == "UNVERIFIABLE" and av.reason_code == "jury_timeout"
    assert all(v.abstain_reason == "timeout" for v in av.votes)
    assert cv.verdict == "UNPROVEN"


def test_atom_cap_timeout():
    ctx = stub_ctx(cosmos_delay=0.5, env={"PERJURY_ATOM_TIMEOUT_S": "0.1", "PERJURY_JUROR_TIMEOUT_S": "5"})
    cv, _ = run("A pickup is towing a trailer", 1, ctx)
    assert cv.atom_verdicts[0].reason_code == "jury_timeout" and cv.verdict == "UNPROVEN"


def test_unverifiable_types_never_touch_a_model():
    ctx = stub_ctx()
    cv, evs = run("The pickup's driver was texting", 1, ctx)
    assert cv.verdict == "UNPROVEN"
    assert verdicts(cv)["driver was texting"] == "UNVERIFIABLE"
    assert not ctx.clients.cosmos.prompts and "summon" not in names(evs)


def test_errors_still_emit_done():
    ctx = stub_ctx()
    ctx.router = None                                   # breaks routing inside testify
    cv, evs = run("A pickup is towing a trailer", 1, ctx)
    n = names(evs)
    assert "error" in n and n[-1] == "done" and n.index("error") < n.index("done")
    assert cv.verdict == "UNPROVEN"


def test_lead_probe_override_sees_the_claim_bench_only():
    ctx = stub_ctx()
    run("A pickup is towing a trailer", 2, ctx, probe_overrides={"lead": True})
    prompts = [p for v, p in ctx.clients.cosmos.prompts if v.startswith("P-LEAD")]
    assert prompts and all("A pickup is towing a trailer" in p for p in prompts)


def test_jury_size_and_camera_subset():
    cv, evs = run("A pickup is towing a trailer", 1, stub_ctx(), jury_size=16)
    summon = next(e["data"] for e in evs if e["event"] == "summon")
    assert len(summon["jurors"]) == 16 and cv.atom_verdicts[0].stats["k"] == 16
    cv, evs = run("A pickup is towing a trailer", 1, stub_ctx(), probe_overrides={"cameras": ["p1c1", "p1c2"]})
    summon = next(e["data"] for e in evs if e["event"] == "summon")
    assert {j["camera"] for j in summon["jurors"]} <= {"p1c1", "p1c2"}


# ---------------------------------------------------------------------------------------------------- part 2
@pytest.fixture(scope="module")
def fake_ctx():
    pytest.importorskip("perjury.fakes")
    from perjury.clients import build_clients
    s = Settings(env=ENV)
    return Context(settings=s, clients=build_clients(s), index=SceneIndex.load(s.index_path),
                   probes=json.loads(s.probes_path.read_text()), router=Router(promotion_path=None))


DEMO = [
    (2, "Three pedestrians are crossing the highway in the snow", "FALSE"),
    (2, "A pickup is towing a trailer", "FALSE"),
    (1, "A pickup is towing a trailer", "TRUE"),
    (1, "The road is covered in snow", "FALSE"),
    (2, "The road is covered in snow", "TRUE"),
    (2, "The white truck braked hard", "UNPROVEN"),
    (3, "stop-and-go traffic", "TRUE"),
]


@pytest.mark.parametrize("scene,text,expected", DEMO, ids=[f"S{s}-{t}" for s, t, _ in DEMO])
def test_fixture_demo(fake_ctx, scene, text, expected):
    cv, evs = run(text, scene, fake_ctx)
    assert cv.verdict == expected, cv.explanation
    assert names(evs)[-1] == "done" and "error" not in names(evs)
    assert cv.mode == "fixture"


def test_fixture_hero_atoms(fake_ctx):
    cv, _ = run("Three pedestrians are crossing the highway in the snow", 2, fake_ctx)
    assert verdicts(cv) == {"Three": "MOOT", "pedestrians": "CONTRADICTED", "crossing": "MOOT",
                            "highway": "SUPPORTED", "in the snow": "SUPPORTED"}
