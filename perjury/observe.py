"""Per-video observations: any location, any number of videos (Exhibits for every scope).

When an atom's verdict carries no per-camera juror votes (a VAST catalog location, or a claim type the I-24 jury
doesn't cover), every video (parent clip) in the scope gets an observation: yes / no / abstain with a real keyframe.
They are emitted as `summon` + `juror` events and attached to AtomVerdict.votes, so the Exhibits panel, the exhibit
drawer and playback work unchanged.

Observations are evidence to inspect, not a jury: clips from one camera are correlated, so they never change the
verdict rule. What decides each video's vote:
  objects (coco_presence, count)        the pipeline's YOLO sidecars for that video (no GPU; every video)
  place (scene_identity, named place)   that video's location metadata (no GPU; every video)
  road / traffic / light                P-COND on one segment of the video (live Cosmos; capped)
  towing / heavy vehicle                P-TOW live juror (live Cosmos; capped)
Jurors still never see the claim. Live probes are capped at PERJURY_OBSERVE_VIDEOS (default 6) spread across the scope.
"""
from __future__ import annotations

import asyncio
import os
import re
import time
from collections import defaultdict
from typing import TYPE_CHECKING, Callable, Optional

from perjury.probes import P_COND, cond_vote, tow_panel_times
from perjury.types import Atom, AtomType, AtomVerdict, Juror, Segment, Vote

if TYPE_CHECKING:  # pragma: no cover
    from perjury.pipeline import Context
    from perjury.router import Route
    from perjury.tiers import RunOpts

PLACES = {"toronto": "toronto", "san francisco": "san_francisco", "nashville": "nashville",
          "neighborhood": "neighborhood", "indoor": "indoor", "warehouse": "warehouse3"}
COCO_YOLO = {"person", "bicycle", "motorcycle", "car", "bus", "truck"}


def live_cap() -> int:
    try:
        return max(1, int(os.getenv("PERJURY_OBSERVE_VIDEOS", "6")))
    except ValueError:
        return 6


def videos(ctx: "Context", scene: int) -> list[tuple[str, list[Segment]]]:
    """(key, segments) per parent video, ordered by camera then time. key = '<camera>.vNN' (a valid exhibit id)."""
    by_cam: dict[str, dict[str, list[Segment]]] = defaultdict(lambda: defaultdict(list))
    for s in ctx.index.segments(scene):
        by_cam[s.camera][s.original_video].append(s)
    out = []
    for cam in sorted(by_cam):
        parents = sorted(by_cam[cam].values(), key=lambda segs: min(x.start for x in segs))
        for i, segs in enumerate(parents, 1):
            out.append((f"{cam}.v{i:02d}", sorted(segs, key=lambda x: x.start)))
    return out


def scene_value(atom: Atom, route: "Route") -> Optional[str]:
    """The atom's scene-wide value; when the LLM left it blank, the first claim_types.yaml value whose name or
    synonym appears in the span ("The road is wet." -> wet)."""
    values = route.cfg.get("values", {}) or {}
    if atom.value in values:
        return atom.value
    span = (atom.span or "").lower()
    for name, cfg in values.items():
        for term in [name.replace("_", " ")] + list(cfg.get("synonyms") or []):
            if re.search(rf"\b{re.escape(term.lower())}\b", span):
                return name
    return None


def _spread(items: list, n: int) -> list:
    if len(items) <= n:
        return items
    step = len(items) / n
    return [items[int(i * step + step / 2)] for i in range(n)]


def _juror(key: str, seg: Segment, times: Optional[list[float]] = None) -> Juror:
    dur = max(0.1, (seg.end - seg.start) if seg.end and seg.start is not None else 5.0)
    return Juror(camera=key, source=seg.source, seg=seg.seg, times=times or [round(dur / 2, 2)])


def _records_vote(key: str, segs: list[Segment], cls: str, floor: int, need: int) -> Vote:
    """YOLO sidecars for one video: yes if `cls` persists >= floor frames with >= need at once in any segment."""
    known = [s for s in segs if s.persist or s.object_counts or s.object_classes]
    best = max(segs, key=lambda s: int(s.object_counts.get(cls, 0)))
    hit = [s for s in known if int(s.persist.get(cls, 0)) >= floor and int(s.object_counts.get(cls, 0)) >= need]
    peak = int(best.object_counts.get(cls, 0))
    if hit:
        state, reason = "yes", None
    elif known:
        state, reason = "no", None
    else:
        state, reason = "abstain", "no_detections"
    seg = hit[0] if hit else (best if peak else segs[len(segs) // 2])
    return Vote(camera=key, vote=state, tier="RECORDS", probe="YOLO", probe_version="pipeline sidecars",
                raw={"class": cls, "peak": peak, "segments_with": len(hit), "segments": len(segs),
                     "noise_floor_frames": floor}, abstain_reason=reason, juror=_juror(key, seg))


def _place_vote(key: str, segs: list[Segment], named: set[str]) -> Vote:
    loc = (segs[0].location or "").lower()
    state = "abstain" if not loc else ("yes" if loc in named else "no")
    return Vote(camera=key, vote=state, tier="RECORDS", probe="metadata", probe_version="VAST upload metadata",
                raw={"location": loc or None, "claimed": sorted(named)},
                abstain_reason=None if loc else "no_metadata", juror=_juror(key, segs[len(segs) // 2]))


async def _cosmos_vote(atom: Atom, key: str, seg: Segment, ctx: "Context", bus, opts: "RunOpts",
                       question: str, option: str) -> Vote:
    """P-COND on 4 frames of one segment of this video (claim-blind, same probe as the pre-run jury)."""
    dur = max(0.1, (seg.end - seg.start) if seg.end else 5.0)
    j = _juror(key, seg, tow_panel_times(dur))
    t = time.monotonic()
    try:
        async def look():
            frames = await ctx.clients.media.keyframes(j.source, j.times, width=1920, bus=bus)
            grid = ctx.clients.media.grid2x2(frames, None)
            return await ctx.clients.cosmos.probe(grid, P_COND.prompt, P_COND.version,
                                                  timeout_s=opts.juror_timeout_s, bus=bus)
        res = await asyncio.wait_for(look(), timeout=opts.juror_timeout_s)
        parsed = res.get("parsed") if isinstance(res, dict) else getattr(res, "parsed", None)
        p = cond_vote(parsed, question, option)
        return Vote(camera=key, vote=p.vote, tier="JURY", probe=P_COND.name, probe_version=P_COND.version, raw=parsed,
                    abstain_reason=p.abstain_reason, latency_ms=int((time.monotonic() - t) * 1000),
                    cached=bool(getattr(res, "cached", False) if not isinstance(res, dict) else res.get("cached")),
                    juror=j)
    except Exception as e:
        reason = "timeout" if isinstance(e, asyncio.TimeoutError) else "error"
        return Vote(camera=key, vote="abstain", tier="JURY", probe=P_COND.name, probe_version=P_COND.version,
                    abstain_reason=reason, latency_ms=int((time.monotonic() - t) * 1000), juror=j)


def _summary(votes: list[Vote]) -> dict:
    return {"videos": len(votes), "yes": sum(v.vote == "yes" for v in votes),
            "no": sum(v.vote == "no" for v in votes), "abstain": sum(v.vote == "abstain" for v in votes)}


async def observe(atom: Atom, route: "Route", scene: int, ctx: "Context", bus, opts: "RunOpts") -> list[Vote]:
    """Per-video votes for one atom (possibly empty when no video-level evidence applies)."""
    vids = videos(ctx, scene)
    if not vids:
        return []
    t = atom.type
    probe, live = "", False
    mk: Optional[Callable[[str, list[Segment]], Vote]] = None
    if t in (AtomType.coco_presence, AtomType.count) and (atom.cls or "") in COCO_YOLO:
        need = atom.count if (t == AtomType.count and atom.count_op in (None, "at_least", "exact") and atom.count) else 1
        floor = ctx.router.noise_floor
        mk = lambda key, segs: _records_vote(key, segs, atom.cls or "", floor, need)  # noqa: E731
        probe = "YOLO"
    elif t == AtomType.scene_identity:
        term = (atom.value or atom.span or "").lower()
        named = {v for name, v in PLACES.items() if re.search(rf"\b{re.escape(name)}\b", term)}
        if not named:
            return []
        mk = lambda key, segs: _place_vote(key, segs, named)  # noqa: E731
        probe = "metadata"
    elif route.rule == "scene_majority":
        value = scene_value(atom, route)
        option = route.cfg.get("values", {}).get(value or "", {}).get("option")
        if not option:
            return []
        live, probe = True, P_COND.name
    elif route.rule in ("presence_jury", "heavy_vehicle_jury"):
        live, probe = True, "P-TOW"
    else:
        return []

    if not live:
        chosen = vids
        jurors = [_juror(key, segs[len(segs) // 2]) for key, segs in chosen]
    else:
        chosen = _spread(vids, live_cap())
        if probe == "P-TOW":   # the most truck-like segment of each video (YOLO rank), like the jury's retrieval
            chosen = [(key, [max(segs, key=lambda s: int(s.object_counts.get("truck", 0)))]) for key, segs in chosen]
        else:
            chosen = [(key, [segs[len(segs) // 2]]) for key, segs in chosen]
        jurors = [_juror(key, segs[0], tow_panel_times(max(0.1, segs[0].end - segs[0].start))) for key, segs in chosen]
    if live:   # records observations need no summon: nothing is asked of a model
        bus.emit("summon", {"atom_id": atom.id, "probe": probe, "probe_version": probe, "jurors": jurors,
                            "source": "per-video observations", "retrieval": f"{len(chosen)} of {len(vids)} videos",
                            "note": "Observations to inspect, not a calibrated jury"})
    else:
        votes = [mk(key, segs) for key, segs in chosen]
        for v in votes:
            bus.emit("juror", {"atom_id": atom.id, "vote": v, "badge": "YOLO" if probe == "YOLO" else "RECORDS"})
        return votes

    if probe == "P-TOW":
        from perjury.tiers import _juror as tier_juror   # live P-TOW juror (ground + YOLO zoom on yes)
        votes = await asyncio.gather(*(tier_juror(atom, j, segs[0], ctx, bus, opts, "tow")
                                       for j, (_, segs) in zip(jurors, chosen)))
        return list(votes)
    question = route.cfg.get("question", "road")
    option = route.cfg.get("values", {}).get(scene_value(atom, route) or "", {}).get("option")
    votes = await asyncio.gather(*(_cosmos_vote(atom, key, segs[0], ctx, bus, opts, question, option)
                                   for key, segs in chosen))
    for v in votes:
        bus.emit("juror", {"atom_id": atom.id, "vote": v, "badge": "COSMOS"})
    return list(votes)


async def attach(av: AtomVerdict, atom: Atom, route: "Route", scene: int, ctx: "Context", bus, opts: "RunOpts",
                 budget_s: float) -> AtomVerdict:
    """Add per-video observations to a verdict that has no juror votes. Never changes the verdict label."""
    if av.votes or av.verdict == "MOOT":
        return av
    try:
        votes = await asyncio.wait_for(observe(atom, route, scene, ctx, bus, opts), timeout=max(1.0, budget_s))
    except Exception:
        return av
    if not votes:
        return av
    s = _summary(votes)
    stats = {**av.stats, "observations": s}
    reason = av.reason
    if ctx.index.coverage.get("catalog_scope") or av.verdict == "UNVERIFIABLE":
        reason = (f"{reason} Per-video observations: {s['yes']} yes, {s['no']} no, {s['abstain']} abstain "
                  f"across {s['videos']} videos (evidence to inspect, not a calibrated jury).").strip()
    return av.model_copy(update={"votes": votes, "stats": stats, "reason": reason})
