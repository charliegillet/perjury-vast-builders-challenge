"""Evidence tiers (FINAL-IDEA-v3 §4, §5, §7): T0 RECORDS, T1 CAPTIONS, T2 JURY, and per-rule atom evaluation.

T0  index pushdown over EVERY segment of the scene: COCO classes, peak counts, persistence, pack metadata. 0 GPU.
T1  synonym preselect (<= 24 snippets + 4 calibration) -> LLM labels, contradiction-first; quotes code-checked.
T2  retrieval (Embed1 cosine x YOLO truck rank) -> top-1 moment per camera, best `jury_size` cameras -> 2x2 grid
    -> Cosmos neutral probe (jurors never see the claim) -> yes panels: P-GROUND -> 4K crop -> YOLO zoom-check.
    Scene-wide atoms use the PRE-RUN P-COND / P-COUNT jurors (cache/scene_probes.json): zero live GPU.
Verdicts are computed by perjury/quorum.py; reasons by perjury/verdict.py. Events: t0, t1, summon, juror, ground, zoom.
"""
from __future__ import annotations

import asyncio
import hashlib
import random
import re
import time
from collections import Counter
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Optional

import numpy as np

from perjury import quorum, verdict
from perjury.atomize import canonical
from perjury.obs import op
from perjury.probes import (P_GROUND, P_LEAD, P_TOW, T1_SYSTEM, Parsed, bbox_to_px, count_vote,
                            cond_vote, ground_box, lead_prompt, lead_vote, semis_vote, t1_user, tow_panel_times,
                            tow_vote)
from perjury.router import Route
from perjury.types import Atom, AtomType, AtomVerdict, Juror, Segment, Vote

if TYPE_CHECKING:  # pragma: no cover
    from perjury.pipeline import Context

T1_MAX_SNIPPETS = 24
T1_CALIBRATION = 4
DEFAULT_SHAPE = (2160, 3840)


@dataclass
class RunOpts:
    """Per-run knobs. probe_overrides (bench): {"lead": True} -> P-LEAD instead of P-TOW (sycophancy row);
    {"cameras": [...]} -> restrict the jury pool; {"ignore_promotion": True} -> evaluate demoted types too."""
    run_id: str
    claim: str
    jury_size: int = 6
    juror_timeout_s: float = 8.0
    probe_overrides: dict = field(default_factory=dict)


def _g(obj: Any, name: str, default: Any = None) -> Any:
    """Attribute-or-key access: clients may return pydantic models or dicts."""
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _av(atom: Atom, rule: quorum.Rule, tiers: list, votes: list[Vote] = (), extra: dict | None = None,
        fallback: str = "") -> AtomVerdict:
    stats = {**rule.stats, **(extra or {})}
    av = AtomVerdict(atom_id=atom.id, verdict=rule.verdict, reason=verdict.reason(atom, rule.reason_code, stats, fallback),
                     reason_code=rule.reason_code, tiers=tiers, votes=list(votes), stats=stats)
    av.stats["pill"] = verdict.pill(atom, av)
    return av


def unverifiable(atom: Atom, reason: str, code: str, stats: dict | None = None) -> AtomVerdict:
    av = AtomVerdict(atom_id=atom.id, verdict="UNVERIFIABLE", reason=reason, reason_code=code, stats=stats or {})
    av.stats["pill"] = verdict.pill(atom, av)
    return av


# ======================================================================================================
# T0 RECORDS
# ======================================================================================================
def t0_class(ctx: "Context", scene: int, cls: str, floor: int = quorum.NOISE_FLOOR_FRAMES) -> dict:
    """Per-camera YOLO evidence for one COCO class over every segment of the scene.
    wall: camera -> segments where the class persisted >= floor frames (what the jury wall paints; noise stays 0)."""
    segs = ctx.index.segments(scene)
    cams = ctx.index.cameras(scene)
    persist = {c: 0 for c in cams}
    peak = {c: 0 for c in cams}
    seg_hits: dict[str, int] = {c: 0 for c in cams}
    wall: dict[str, int] = {c: 0 for c in cams}
    for s in segs:
        if cls in s.object_classes or s.object_counts.get(cls, 0) > 0:
            run = int(s.persist.get(cls, 1 if cls in s.object_classes else 0))
            seg_hits[s.camera] = seg_hits.get(s.camera, 0) + 1
            wall[s.camera] = wall.get(s.camera, 0) + (run >= floor)
            persist[s.camera] = max(persist.get(s.camera, 0), run)
            peak[s.camera] = max(peak.get(s.camera, 0), int(s.object_counts.get(cls, 0)))
    return {"cls": cls, "segments_total": len(segs), "segments_with": sum(seg_hits.values()), "cameras": len(cams),
            "per_camera": {c: {"segments": seg_hits.get(c, 0), "persist": persist.get(c, 0), "peak": peak.get(c, 0)}
                           for c in cams},
            "persist": persist, "peak": peak, "wall": wall}


@op("perjury.t0.scene_identity")
async def eval_scene_identity(atom: Atom, route: Route, scene: int, ctx: "Context", bus, opts: RunOpts) -> AtomVerdict:
    term = f" {(atom.value or atom.span).lower()} "
    locs, cam_ids = ctx.index.locations(scene), ctx.index.camera_ids(scene)
    for name, pack in route.cfg.get("packs", {}).items():
        if not any(c.lower().startswith(pack.get("camera_id_prefix", "~")) for c in cam_ids):
            continue
        if pack.get("location") and locs and pack["location"] not in locs:
            continue
        desc = f"{', '.join(sorted(cam_ids))} · {', '.join(sorted(locs)) or 'no location'}"
        hit = lambda terms: next((t for t in terms if re.search(rf"\b{re.escape(t)}\b", term)), None)  # noqa: E731
        bad, good = hit(pack.get("mismatch", [])), hit(pack.get("match", []))
        data = {"pack": name, "camera_ids": sorted(cam_ids), "locations": sorted(locs), "term": term.strip(),
                "matched": good, "mismatched": bad}
        bus.emit("t0", {"atom_id": atom.id, "summary": f"metadata: {desc}", "data": data})
        stats = {"pack_desc": desc, **data}
        if bad:
            return _av(atom, quorum.Rule("CONTRADICTED", "metadata_mismatch", stats), ["RECORDS"])
        if good:
            return _av(atom, quorum.Rule("SUPPORTED", "metadata_match", stats), ["RECORDS"])
        return unverifiable(atom, route.reason_if_unverifiable, route.reason_code, stats)
    bus.emit("t0", {"atom_id": atom.id, "summary": "no pack metadata for this scene", "data": {}})
    return unverifiable(atom, route.reason_if_unverifiable, route.reason_code)


@op("perjury.t0.count")
async def eval_count(atom: Atom, route: Route, scene: int, ctx: "Context", bus, opts: RunOpts) -> AtomVerdict:
    t0 = t0_class(ctx, scene, atom.cls or "")
    bus.emit("t0", {"atom_id": atom.id,
                    "summary": f"YOLO peak {atom.cls}: max {max(t0['peak'].values(), default=0)} per frame",
                    "data": {"per_camera": t0["peak"], "peak": t0["peak"], "n": atom.count, "op": atom.count_op,
                             "hits": sum(1 for v in t0["peak"].values() if v >= (atom.count or 0)),
                             "total": len(t0["peak"]), "segments_with": t0["segments_with"],
                             "segments_total": t0["segments_total"]}})
    rule = quorum.count_lower_bound_verdict(t0["peak"], atom.count or 0, atom.count_op)
    if rule.verdict != "SUPPORTED":
        return unverifiable(atom, verdict.reason(atom, rule.reason_code, rule.stats, route.reason_if_unverifiable)
                            if rule.reason_code != "count_not_testable" else route.reason_if_unverifiable,
                            rule.reason_code, rule.stats)
    return _av(atom, rule, ["RECORDS"])


# ======================================================================================================
# Pre-run scene-wide jurors (P-COND, P-COUNT)
# ======================================================================================================
def _prerun(ctx: "Context", scene: int) -> dict:
    return (ctx.probes or {}).get("scenes", {}).get(str(scene), {}) or {}


def _prerun_version(ctx: "Context", name: str) -> str:
    v = (ctx.probes or {}).get("probe_versions", {}).get(name, "v1")
    return f"{name} {v}"


def _prerun_votes(atom: Atom, ctx: "Context", scene: int, bus, name: str, parse) -> list[tuple[Vote, Parsed]]:
    """Emit summon + one juror event per pre-run camera; returns (Vote, Parsed) per camera."""
    rows = _prerun(ctx, scene)
    cams = [c for c in ctx.index.cameras(scene) if c in rows] or sorted(rows)
    ran_at = (ctx.probes or {}).get("ran_at")
    version = _prerun_version(ctx, name)
    jurors = [Juror(camera=c, source=ctx.index.scene_parent(scene, c), times=rows[c].get("grid_times", []))
              for c in cams]
    bus.emit("summon", {"atom_id": atom.id, "probe": name, "probe_version": version, "jurors": jurors,
                        "source": "pre-run", "cached": True, "ran_at": ran_at, "retrieval": "all cameras"})
    out = []
    for j in jurors:
        entry = (rows[j.camera] or {}).get(name) or {}
        p = parse(entry.get("parsed"))
        v = Vote(camera=j.camera, vote=p.vote, tier="JURY", probe=name, probe_version=version, raw=entry.get("parsed"),
                 yes_panels=p.yes_panels, visibility=p.visibility, abstain_reason=p.abstain_reason,
                 latency_ms=int(entry.get("latency_ms", 0)), cached=True, cached_at=ran_at, juror=j)
        bus.emit("juror", {"atom_id": atom.id, "vote": v, "value": p.value, "badge": "COSMOS"})
        out.append((v, p))
    return out


# ======================================================================================================
# T1 CAPTIONS
# ======================================================================================================
def _terms_hit(text: str, terms: list[str]) -> bool:
    low = text.lower()
    return any(re.search(rf"(?<![\w-]){re.escape(t.lower())}(?![\w-])", low) for t in terms)


def _spread(snips: list[dict], n: int) -> list[dict]:
    """Up to n snippets, round-robin across cameras so one camera can't fill the window."""
    by_cam: dict[str, list[dict]] = {}
    for s in snips:
        by_cam.setdefault(s["cam"], []).append(s)
    out: list[dict] = []
    while len(out) < n and any(by_cam.values()):
        for cam in sorted(by_cam):
            if by_cam[cam] and len(out) < n:
                out.append(by_cam[cam].pop(0))
    return out


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


@op("perjury.t1.captions")
async def t1_captions(atom: Atom, terms: list[str], contra_terms: list[str], scene: int, ctx: "Context", bus,
                      opts: RunOpts) -> dict:
    """Label <= 24 synonym-matched captions (+4 calibration) against canonical(atom). Returns the T1 summary.
    complete=True means every synonym-matched caption was labelled (needed before T1 silence can count)."""
    caps = ctx.index.captions(scene)
    hit_terms = list(terms) + list(contra_terms)
    matched = [c for c in caps if _terms_hit(c["text"], hit_terms)]
    pre = _spread(matched, T1_MAX_SNIPPETS)
    rest = [c for c in caps if c not in matched]
    seed = int(hashlib.sha256(f"{atom.span}|{atom.type.value}|{scene}".encode()).hexdigest()[:8], 16)
    calib = random.Random(seed).sample(rest, min(T1_CALIBRATION, len(rest)))
    calib_ids = {c["id"] for c in calib}
    snippets = pre + calib
    summary = {"supports": 0, "contradicts": 0, "silent": len(caps), "total": len(caps), "matched": len(matched),
               "labelled": 0, "calibration_flags": 0, "complete": True, "error": None}
    labels: dict[str, dict] = {}
    if pre:
        t = time.monotonic()
        try:
            raw = await ctx.clients.llm.complete_json(T1_SYSTEM, t1_user(canonical(atom), snippets), temperature=0.0,
                                                      max_tokens=1200, bus=bus, purpose="t1")
            labels = _validate_labels(raw, {s["id"]: s for s in snippets})
            summary["labelled"] = len(pre)
            summary["complete"] = len(matched) <= T1_MAX_SNIPPETS
        except Exception as e:  # T1 failed: synonym hits stay unlabelled, so T1 silence is not established
            summary.update(complete=False, error=type(e).__name__)
        summary["latency_ms"] = int((time.monotonic() - t) * 1000)
    out_snips = []
    for s in snippets:
        lab = labels.get(s["id"], {"label": "SILENT", "quote": None})
        is_cal = s["id"] in calib_ids
        if is_cal and lab["label"] != "SILENT":
            summary["calibration_flags"] += 1          # a non-silent label on a no-synonym caption: not counted
        elif lab["label"] == "SUPPORTS":
            summary["supports"] += 1
        elif lab["label"] == "CONTRADICTS":
            summary["contradicts"] += 1
        out_snips.append({"id": s["id"], "cam": s["cam"], "seg": s["seg"], "text": s["text"], "label": lab["label"],
                          "quote": lab["quote"], "calibration": is_cal})
    summary["silent"] = len(caps) - summary["supports"] - summary["contradicts"]
    bus.emit("t1", {"atom_id": atom.id, **{k: summary[k] for k in ("supports", "contradicts", "silent")},
                    "total": summary["total"], "matched": summary["matched"], "complete": summary["complete"],
                    "error": summary["error"], "snippets": out_snips})
    return summary


def _validate_labels(raw: Any, by_id: dict[str, dict]) -> dict[str, dict]:
    """Code check (§6): label in the closed set, id known, quote a substring of its snippet; else SILENT."""
    out: dict[str, dict] = {}
    items = raw.get("labels") if isinstance(raw, dict) else raw
    for it in items if isinstance(items, list) else []:
        if not isinstance(it, dict) or it.get("id") not in by_id:
            continue
        label = str(it.get("label", "")).upper()
        quote = it.get("quote")
        ok = (label in ("SUPPORTS", "CONTRADICTS") and isinstance(quote, str) and quote.strip()
              and _norm(quote) in _norm(by_id[it["id"]]["text"]))
        out[it["id"]] = {"label": label if ok else "SILENT", "quote": quote if ok else None}
    return out


# ======================================================================================================
# Scene-wide majority (road_surface, weather, traffic_state, lighting)
# ======================================================================================================
@op("perjury.scene_wide")
async def eval_scene_wide(atom: Atom, route: Route, scene: int, ctx: "Context", bus, opts: RunOpts) -> AtomVerdict:
    vcfg = route.cfg.get("values", {}).get(atom.value or "", {})
    option, question = vcfg.get("option"), route.cfg.get("question", "road")
    if not option:
        return unverifiable(atom, f"No juror question covers “{atom.value or atom.span}”.", "no_probe")
    t1_task = None
    if "CAPTIONS" in route.tiers:
        t1_task = asyncio.create_task(t1_captions(atom, vcfg.get("synonyms", []), vcfg.get("contradicts", []), scene,
                                                  ctx, bus, opts))
    if not _prerun(ctx, scene):
        if t1_task:
            await t1_task
        return unverifiable(atom, "No pre-run scene jury for this scene.", "no_prerun")
    pairs = _prerun_votes(atom, ctx, scene, bus, "P-COND", lambda parsed: cond_vote(parsed, question, option))
    t1 = await t1_task if t1_task else None
    answers = [p.value if v.vote != "abstain" else None for v, p in pairs]
    rule = quorum.scene_majority_verdict(answers, option, t1_supports=(t1 or {}).get("supports", 0),
                                         t1_contradicts=(t1 or {}).get("contradicts", 0))
    others = Counter(a for a in answers if a and a not in (option, "D"))
    extra = {"question": question, "top_other": others.most_common(1)[0][0] if others else None, "t1": t1,
             "answers": {v.camera: a for (v, _), a in zip(pairs, answers)}}
    tiers = ["JURY"] + (["CAPTIONS"] if t1 and (t1["supports"] or t1["contradicts"]) else [])
    return _av(atom, rule, tiers, [v for v, _ in pairs], extra)


# ======================================================================================================
# COCO presence / absence (T0 YOLO over every segment + pre-run P-COUNT jury)
# ======================================================================================================
@op("perjury.coco")
async def eval_coco(atom: Atom, route: Route, scene: int, ctx: "Context", bus, opts: RunOpts) -> AtomVerdict:
    cls = atom.cls or ""
    floor = ctx.router.noise_floor
    t0 = t0_class(ctx, scene, cls, floor)
    over = quorum.yolo_cameras_over_floor(t0["persist"], floor)
    bus.emit("t0", {"atom_id": atom.id,
                    "summary": f"YOLO: {cls} in {t0['segments_with']} of {t0['segments_total']} segments; "
                               f"{len(over)} cameras over the {floor}-frame noise floor",
                    "data": {"per_camera": t0["wall"], "hits": t0["segments_with"], "total": t0["segments_total"],
                             "segments_with": t0["segments_with"], "segments_total": t0["segments_total"],
                             "floor": floor, "cameras_over_floor": over, "detail": t0["per_camera"]}})
    fld = route.cfg.get("jury_field", {}).get(cls)
    votes: list[Vote] = []
    counts: Optional[list[Optional[int]]] = None
    if fld and _prerun(ctx, scene):
        pairs = _prerun_votes(atom, ctx, scene, bus, "P-COUNT", lambda parsed: count_vote(parsed, fld))
        votes = [v for v, _ in pairs]
        counts = [p.value if v.vote != "abstain" else None for v, p in pairs]
    rule = quorum.coco_verdict(t0["persist"], counts, negated=atom.negated, floor=floor)
    extra = {"segments_with": t0["segments_with"], "segments_total": t0["segments_total"], "cameras": t0["cameras"],
             "floor": floor, "jury_field": fld}
    tiers = ["RECORDS"] + (["JURY"] if counts is not None else [])
    if rule.verdict == "UNVERIFIABLE":
        return _av(atom, rule, [], votes, extra, route.reason_if_unverifiable)
    return _av(atom, rule, tiers, votes, extra)


# ======================================================================================================
# T2 live jury (towing; heavy_vehicle_kind when promoted)
# ======================================================================================================
def _pct_rank(values: dict[str, float]) -> dict[str, float]:
    """Percentile rank in [0, 1] (ties share the mean rank)."""
    if not values:
        return {}
    keys = list(values)
    arr = np.array([values[k] for k in keys], dtype=float)
    order = arr.argsort(kind="stable")
    ranks = np.empty(len(arr))
    ranks[order] = np.arange(len(arr))
    for v in np.unique(arr):
        idx = arr == v
        ranks[idx] = ranks[idx].mean()
    denom = max(1, len(arr) - 1)
    return {k: float(r / denom) for k, r in zip(keys, ranks)}


@op("perjury.t2.retrieve")
async def retrieve(atom: Atom, phrase: str, scene: int, ctx: "Context", bus, k: int,
                   cameras: Optional[list[str]] = None) -> tuple[list[tuple[Juror, Segment]], str, str]:
    """Top-1 most claim-like moment per camera, best k cameras. Score = 0.85 * Embed1 cosine percentile +
    0.15 * YOLO truck-count percentile; YOLO rank alone when visual vectors (or the text embedding) are missing."""
    segs = [s for s in ctx.index.segments(scene) if not cameras or s.camera in cameras]
    vectors, note, method = None, "", "embed1+yolo"
    try:
        vectors = ctx.clients.embed.visual_vectors()
    except Exception as e:
        note = f"visual vectors unavailable ({type(e).__name__})"
    cos: dict[str, float] = {}
    if vectors:
        try:
            q = np.asarray(await ctx.clients.embed.embed_text(phrase, bus=bus), dtype=float)
            qn = q / (np.linalg.norm(q) or 1.0)
            for s in segs:
                v = vectors.get(s.source)
                if v is not None:
                    v = np.asarray(v, dtype=float)
                    cos[s.source] = float(qn @ v / (np.linalg.norm(v) or 1.0))
        except Exception as e:
            note = f"Embed1 text embedding failed ({type(e).__name__})"
            cos = {}
    elif not note:
        note = "no visual vectors"
    if not cos:
        method = "yolo"
        note = (note + "; " if note else "") + "retrieval by YOLO truck-count rank alone"
    truck = _pct_rank({s.source: float(s.object_counts.get("truck", 0)) for s in segs})
    cosp = _pct_rank(cos)
    score = {s.source: (0.85 * cosp.get(s.source, 0.0) + 0.15 * truck.get(s.source, 0.0)) if cos
             else truck.get(s.source, 0.0) for s in segs}
    best: dict[str, Segment] = {}
    for s in segs:
        if s.camera not in best or score[s.source] > score[best[s.camera].source]:
            best[s.camera] = s
    ranked = sorted(best.values(), key=lambda s: (-score[s.source], s.camera))[:k]
    out = [(Juror(camera=s.camera, source=s.source, seg=s.seg, times=tow_panel_times(s.end - s.start), rank=i,
                  retrieval_score=round(score[s.source], 4)), s) for i, s in enumerate(ranked)]
    return out, method, note


def _vote_from(j: Juror, p: Parsed, probe_name: str, version: str, res: Any, ms: int) -> Vote:
    return Vote(camera=j.camera, vote=p.vote, tier="JURY", probe=probe_name, probe_version=version,
                raw=_g(res, "parsed"), yes_panels=p.yes_panels, visibility=p.visibility, abstain_reason=p.abstain_reason,
                latency_ms=int(_g(res, "latency_ms", ms) or ms), cached=bool(_g(res, "cached", False)),
                cached_at=_g(res, "cached_at"), image_sha=_g(res, "image_sha"), juror=j)


async def _juror(atom: Atom, j: Juror, seg: Segment, ctx: "Context", bus, opts: RunOpts, mode: str) -> Vote:
    """One live juror: keyframes -> 2x2 grid -> neutral probe -> (yes) P-GROUND -> 4K crop -> YOLO zoom-check."""
    lead = mode == "lead"
    probe = P_LEAD if lead else P_TOW
    prompt = lead_prompt(opts.claim) if lead else probe.prompt
    t = time.monotonic()
    frames: list[bytes] = []
    try:
        async def look():
            fr = await ctx.clients.media.keyframes(j.source, j.times, width=1920, bus=bus)
            grid = ctx.clients.media.grid2x2(fr, None)
            return fr, await ctx.clients.cosmos.probe(grid, prompt, probe.version, timeout_s=opts.juror_timeout_s,
                                                      bus=bus)
        frames, res = await asyncio.wait_for(look(), timeout=opts.juror_timeout_s)
        ms = int((time.monotonic() - t) * 1000)
        err = _g(res, "error")
        if err and _g(res, "parsed") is None and "invalid_json" not in str(err):
            p = Parsed("abstain", [], abstain_reason="timeout" if "timeout" in str(err).lower() else "error")
        elif lead:
            p = lead_vote(_g(res, "parsed"))
        elif mode == "semis":
            p = semis_vote(_g(res, "parsed"))
        else:
            p = tow_vote(_g(res, "parsed"), atom.towing_vehicle)
        vote = _vote_from(j, p, probe.name, probe.version, res, ms)
    except asyncio.TimeoutError:
        vote = Vote(camera=j.camera, vote="abstain", probe=probe.name, probe_version=probe.version,
                    abstain_reason="timeout", latency_ms=int((time.monotonic() - t) * 1000), juror=j)
    except Exception as e:
        vote = Vote(camera=j.camera, vote="abstain", probe=probe.name, probe_version=probe.version,
                    abstain_reason="error", raw={"error": type(e).__name__}, latency_ms=int((time.monotonic() - t) * 1000),
                    juror=j)
    bus.emit("juror", {"atom_id": atom.id, "vote": vote, "badge": "COSMOS"})
    if vote.vote == "yes" and mode == "tow" and frames:
        try:
            await asyncio.wait_for(_ground_and_zoom(atom, vote, frames, j, seg, ctx, bus, opts),
                                   timeout=opts.juror_timeout_s * 1.5)
        except Exception as e:  # timeout or failure: the yes vote is not counted (zoom_ok False)
            vote.zoom_ok = False
            bus.emit("zoom", {"atom_id": atom.id, "camera": j.camera, "ok": False, "label": None, "conf": None,
                              "crop_box": None, "error": type(e).__name__})
    return vote


async def _ground_and_zoom(atom: Atom, vote: Vote, frames: list[bytes], j: Juror, seg: Segment, ctx: "Context", bus,
                           opts: RunOpts) -> None:
    panel = vote.yes_panels[0]
    if panel < 1 or panel > len(frames):
        vote.zoom_ok = False
        return
    res = await ctx.clients.cosmos.probe(frames[panel - 1], P_GROUND.prompt, P_GROUND.version,
                                         timeout_s=opts.juror_timeout_s, bus=bus)
    scale = ctx.settings.cosmos_bbox_scale
    box = ground_box(_g(res, "parsed"), scale)
    vote.grounded = box
    bus.emit("ground", {"atom_id": atom.id, "camera": j.camera, "panel": panel, "bbox_2d": box,
                        "t": j.times[panel - 1] if panel <= len(j.times) else None,
                        "latency_ms": _g(res, "latency_ms", 0), "cached": bool(_g(res, "cached", False))})
    if box is None:
        vote.zoom_ok = False
        return
    shape = seg.video_shape or DEFAULT_SHAPE
    h, w = int(shape[0]), int(shape[1])
    px = bbox_to_px(box, w, h, scale)
    crop = await ctx.clients.media.crop_clip(j.source, j.times[panel - 1], px, bus=bus)
    z = await ctx.clients.yolo.zoom_check(crop, None, min_cover=0.30, bus=bus)
    vote.zoom_ok = bool(_g(z, "ok", False))
    bus.emit("zoom", {"atom_id": atom.id, "camera": j.camera, "panel": panel, "ok": vote.zoom_ok,
                      "label": _g(z, "label"), "conf": _g(z, "conf"), "cover": _g(z, "cover"),
                      "frames_ok": _g(z, "frames_ok"), "crop_box": list(px), "error": _g(z, "error")})


@op("perjury.t2.presence")
async def eval_presence(atom: Atom, route: Route, scene: int, ctx: "Context", bus, opts: RunOpts) -> AtomVerdict:
    """Towing (and promoted heavy_vehicle_kind): T1 support statistic + live T2 jury, §7 presence rule."""
    heavy = route.rule == "heavy_vehicle_jury"
    if heavy and atom.value != "semi":
        return unverifiable(atom, route.cfg.get("reason", "No probe for this kind."), "no_probe")
    lead = bool(opts.probe_overrides.get("lead")) or opts.probe_overrides.get(atom.type.value) == "P-LEAD"
    mode = "lead" if lead else ("semis" if heavy else "tow")
    vehicle = {"any": "vehicle", None: "vehicle", "suv": "SUV"}.get(atom.towing_vehicle, atom.towing_vehicle) \
        if not heavy else (atom.value or "truck").replace("_", " ")
    phrase = route.cfg.get("visual_phrase", "{vehicle}").format(vehicle=vehicle)

    t1_task = None
    if "CAPTIONS" in route.tiers:
        t1_task = asyncio.create_task(t1_captions(atom, route.cfg.get("synonyms", []), route.cfg.get("contradicts", []),
                                                  scene, ctx, bus, opts))
    picked, method, note = await retrieve(atom, phrase, scene, ctx, bus, opts.jury_size,
                                          opts.probe_overrides.get("cameras"))
    probe = P_LEAD if lead else P_TOW
    bus.emit("summon", {"atom_id": atom.id, "probe": probe.name, "probe_version": probe.version,
                        "jurors": [j for j, _ in picked], "source": "live", "cached": False, "retrieval": method,
                        "note": note, "phrase": phrase, "sees_claim": probe.sees_claim})
    votes = list(await asyncio.gather(*[_juror(atom, j, s, ctx, bus, opts, mode) for j, s in picked]))
    t1 = await t1_task if t1_task else {"supports": 0, "total": 0, "complete": True}

    k = len(votes)
    zoom_required = mode == "tow"
    Y = sum(1 for v in votes if v.vote == "yes" and (v.zoom_ok or not zoom_required))
    N = sum(1 for v in votes if v.vote == "no")
    m = ctx.router.m(atom.type.value, k) if k else None
    rule = quorum.presence_verdict(Y, N, k, m, retrieved_top=bool(picked), t1_supports=t1.get("supports", 0),
                                   t1_complete=bool(t1.get("complete", True)))
    extra = {"alpha": ctx.router.alpha(atom.type.value), "t1": t1 if t1_task else None, "retrieval": method,
             "retrieval_note": note, "zoom_required": zoom_required, "probe": probe.name,
             "yes_raw": sum(1 for v in votes if v.vote == "yes"),
             "abstain": sum(1 for v in votes if v.vote == "abstain")}
    if rule.verdict == "CONTRADICTED":
        tiers = ["JURY"] + (["CAPTIONS"] if t1_task else [])
    elif rule.verdict == "SUPPORTED":
        tiers = ["JURY"]
    else:
        tiers = []
    if rule.verdict == "UNVERIFIABLE" and k == 0:
        return unverifiable(atom, "No camera moments to summon for this scene.", "no_jurors", {**rule.stats, **extra})
    if rule.verdict == "UNVERIFIABLE" and k and all(v.abstain_reason == "timeout" for v in votes):
        rule = quorum.Rule("UNVERIFIABLE", "jury_timeout", rule.stats)
    return _av(atom, rule, tiers, votes, extra, route.reason_if_unverifiable)


# ======================================================================================================
# dispatch
# ======================================================================================================
RULES = {
    "metadata_match": eval_scene_identity,
    "scene_majority": eval_scene_wide,
    "coco_presence": eval_coco,
    "count_lower_bound": eval_count,
    "presence_jury": eval_presence,
    "heavy_vehicle_jury": eval_presence,
}


async def evaluate(atom: Atom, route: Route, scene: int, ctx: "Context", bus, opts: RunOpts) -> AtomVerdict:
    """Route -> rule -> AtomVerdict. Unrouted, never-testable and bench-demoted types never touch a model."""
    fn = RULES.get(route.rule)
    if fn is None:
        return unverifiable(atom, route.reason_if_unverifiable, route.reason_code)
    if route.demoted and not opts.probe_overrides.get("ignore_promotion"):
        return unverifiable(atom, route.reason_if_unverifiable, route.reason_code, {"promoted": False})
    return await fn(atom, route, scene, ctx, bus, opts)
