"""Per-video observations (perjury/observe.py): every scope gets exhibits, without changing verdict labels."""
from __future__ import annotations

import asyncio
import os

import pytest

from perjury.events import EventBus
from perjury.observe import attach, observe, videos
from perjury.types import Atom, AtomType, AtomVerdict

os.environ.setdefault("PERJURY_MODE", "fixture")
os.environ.setdefault("PERJURY_FIXTURE_LATENCY", "0")


@pytest.fixture(scope="module")
def ctx():
    from perjury.config import Settings
    from perjury.pipeline import load_context
    return load_context(Settings({"PERJURY_MODE": "fixture", "PERJURY_FIXTURE_LATENCY": "0", "PERJURY_WEAVE": "0"}))


def run(coro):
    return asyncio.run(coro)


def opts():
    from perjury.tiers import RunOpts
    return RunOpts(run_id="t", claim="x", juror_timeout_s=5)


def test_videos_one_key_per_parent(ctx):
    vids = videos(ctx, 2)
    parents = {s.original_video for s in ctx.index.segments(2)}
    assert len(vids) == len(parents)
    assert all(k.count(".v") == 1 for k, _ in vids)


def test_object_claim_votes_on_every_video_without_a_model(ctx):
    atom = Atom(id="a1", span="cars", type=AtomType.coco_presence, cls="car")
    route = ctx.router.route(atom)
    bus = EventBus("t")
    votes = run(observe(atom, route, 2, ctx, bus, opts()))
    assert len(votes) == len(videos(ctx, 2)) and votes
    assert {v.vote for v in votes} <= {"yes", "no", "abstain"} and all(v.tier == "RECORDS" for v in votes)
    assert all(v.juror and v.juror.source for v in votes)          # every vote has a frame to show
    names = [e["event"] for e in bus.events]
    assert "summon" not in names and names.count("juror") == len(votes)


def test_place_claim_uses_location_metadata(ctx):
    atom = Atom(id="a1", span="in Toronto", type=AtomType.scene_identity, value="toronto")
    votes = run(observe(atom, ctx.router.route(atom), 1, ctx, EventBus("t"), opts()))
    assert votes and all(v.vote == "no" and v.probe == "metadata" for v in votes)   # fixture footage is Nashville


def test_scene_wide_claim_is_capped_live_cosmos(ctx, monkeypatch):
    monkeypatch.setenv("PERJURY_OBSERVE_VIDEOS", "3")
    atom = Atom(id="a1", span="snow", type=AtomType.road_surface, value="snow")
    route = ctx.router.route(atom)
    bus = EventBus("t")
    votes = run(observe(atom, route, 2, ctx, bus, opts()))
    assert len(votes) == 3 and all(v.probe == "P-COND" for v in votes)
    assert "summon" in [e["event"] for e in bus.events]


def test_attach_keeps_the_verdict_label(ctx):
    atom = Atom(id="a1", span="cars", type=AtomType.coco_presence, cls="car")
    av = AtomVerdict(atom_id="a1", verdict="UNVERIFIABLE", reason="No calibrated jury.", reason_code="x")
    out = run(attach(av, atom, ctx.router.route(atom), 2, ctx, EventBus("t"), opts(), budget_s=5))
    assert out.verdict == "UNVERIFIABLE" and out.votes and out.stats["observations"]["videos"] == len(out.votes)
    assert "Per-video observations" in out.reason


def test_attach_leaves_juror_verdicts_alone(ctx):
    from perjury.types import Vote
    atom = Atom(id="a1", span="cars", type=AtomType.coco_presence, cls="car")
    av = AtomVerdict(atom_id="a1", verdict="SUPPORTED", reason="r", votes=[Vote(camera="p1c1", vote="yes")])
    assert run(attach(av, atom, ctx.router.route(atom), 2, ctx, EventBus("t"), opts(), budget_s=5)) is av


def test_scene_value_inferred_when_llm_leaves_it_blank(ctx):
    from perjury.observe import scene_value
    atom = Atom(id="a1", span="The road is wet.", type=AtomType.weather)       # what the live LLM returned
    assert scene_value(atom, ctx.router.route(atom)) == "rain"
    atom = Atom(id="a1", span="The road is wet.", type=AtomType.road_surface)
    assert scene_value(atom, ctx.router.route(atom)) == "wet"
