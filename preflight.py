#!/usr/bin/env python3
"""PERJURY preflight: gates G0-G6 (FINAL-IDEA-v3 §11) as timeboxed async checks -> PASS / FAIL / SKIP table.

    python preflight.py [--only G3,G5] [--json] [--wav claim.wav --wav-text "a pickup is towing a trailer"]

Thresholds are hard-coded from §11. Never prints env values (no URLs, tokens or keys). In fixture mode the gates run
against the fakes and say so; G0 and G4 (pure reachability) are SKIP there.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import statistics
import sys
import time
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Awaitable, Callable

from perjury.config import CACHE, Settings, settings

# ---- §11 thresholds ----
G1_MIN_ROWS, G1_MIN_CAMS = 600, 14
G3_MAX_FPR, G3_MIN_S1 = 0.25, 2
G4_MAX_MS = 1500
G5_MIN_VALID, G5_MAX_P50_MS, G5_CALLS = 0.95, 10_000, 6
G6_PERSON_NOISE = 0.10
TIMEBOX = {"G0": 45, "G1": 240, "G2": 300, "G3": 420, "G4": 90, "G5": 150, "G6": 150}

# §8 planted lies (stock A/B baseline); the stock agent has no scene filter, so the scene is informational only.
G2_LIES = [
    ("Three pedestrians are crossing the highway", 1),
    ("A cyclist is riding on the shoulder", 1),
    ("A pickup is towing a trailer", 2),
    ("An SUV is pulling a camper", 2),
    ("The road is covered in snow", 1),
    ("Traffic is at a standstill", 1),
    ("Traffic is flowing freely at speed", 3),
    ("It is nighttime", 2),
    ("Three pedestrians are crossing the highway in the snow", 2),
    ("A cyclist on a snowy highway", 2),
]
TOW_QUERY = "a pickup truck towing a trailer on the highway"


@dataclass
class Result:
    gate: str
    status: str = "SKIP"
    note: str = ""
    ms: int = 0
    data: dict = field(default_factory=dict)
    steps: list[str] = field(default_factory=list)


class Ctx:
    def __init__(self, s: Settings, args):
        from perjury.clients import build_clients
        self.s, self.args = s, args
        self.c = build_clients(s)
        self.fixture = s.mode != "live"
        self._index: dict | None = None

    def index(self) -> dict | None:
        if self._index is None and self.s.index_path.exists():
            self._index = json.loads(self.s.index_path.read_text())
        return self._index

    def probe(self, name: str):
        from perjury.probes import PROBES
        return PROBES[name]


# ---- G0 reachability ----
async def _http_ok(url: str, headers: dict | None = None, any_status: bool = False) -> tuple[bool, str]:
    import httpx
    try:
        async with httpx.AsyncClient(timeout=8, follow_redirects=True) as h:
            r = await h.get(url, headers=headers or {})
        return (True if any_status else r.status_code < 400), f"HTTP {r.status_code}"
    except Exception as e:
        return False, type(e).__name__


async def _tcp_ok(endpoint: str) -> tuple[bool, str]:
    u = urllib.parse.urlsplit(endpoint if "://" in endpoint else f"http://{endpoint}")
    try:
        _, w = await asyncio.wait_for(asyncio.open_connection(u.hostname, u.port or 80), 6)
        w.close()
        return True, "tcp ok"
    except Exception as e:
        return False, type(e).__name__


async def g0(ctx: Ctx) -> Result:
    r = Result("G0")
    r.steps = ["Laptop Chrome: chrome://flags/#unsafely-treat-insecure-origin-as-secure -> add the /app origin, relaunch, "
               "record 2 s on /app (docs/CHROME-FLAG-CARD.md)",
               "From the pod: kubectl exec <pod> -- python preflight.py --only G0",
               "DataEngine UI: confirm the trigger filters by suffix/prefix before writing anything under perjury/"]
    if ctx.fixture:
        r.note = "fixture mode: reachability not testable"
        return r
    s = ctx.s
    auth = {"Authorization": f"Bearer {s.gpu_token}"} if s.gpu_token else {}
    checks: dict[str, Awaitable] = {}
    if s.cosmos_url:
        checks["cosmos3"] = _http_ok(f"{s.cosmos_url}/v1/health/ready", auth)
    if s.yolo_url:
        checks["yolo"] = _http_ok(f"{s.yolo_url}/healthz", auth)
    if s.embed_url:
        checks["embed1"] = _http_ok(f"{s.embed_url}/v1/health/ready", auth)
    if s.canary_url:
        checks["canary"] = _http_ok(f"{s.canary_url}/v1/health/ready", auth)
    if s.wandb_key:
        checks["wandb_inference"] = _http_ok(f"{s.wandb_base}/models", {"Authorization": f"Bearer {s.wandb_key}"})
    checks["pypi"] = _http_ok("https://pypi.org/simple/imageio-ffmpeg/")
    if s.s3_endpoint:
        checks["s3"] = _http_ok(s.s3_endpoint if "://" in s.s3_endpoint else f"http://{s.s3_endpoint}", any_status=True)
    if s.vdb_endpoint:
        checks["vastdb"] = _tcp_ok(s.vdb_endpoint)
    if s.vss_url:
        checks["vss"] = _http_ok(s.vss_url, any_status=True)
    if s.env.get("PERJURY_APP_URL"):
        checks["app"] = _http_ok(s.env["PERJURY_APP_URL"].rstrip("/") + "/health")
    names = list(checks)
    res = await asyncio.gather(*checks.values())
    r.data = {n: {"ok": ok, "detail": d} for n, (ok, d) in zip(names, res)}
    missing = [n for n in ("cosmos3", "yolo", "embed1", "canary", "wandb_inference", "s3", "vastdb", "vss")
               if n not in checks]
    bad = [n for n in names if not r.data[n]["ok"]]
    r.status = "PASS" if not bad and not missing else "FAIL"
    r.note = (f"reachable {len(names) - len(bad)}/{len(names)}" + (f"; down: {', '.join(bad)}" if bad else "")
              + (f"; unset: {', '.join(missing)}" if missing else ""))
    if bad:
        r.steps.append("Pod -> GPU fails: run live T2 from the VM app (localhost:8080); /app serves T0/T1 + replay")
    return r


# ---- G1 index ----
async def g1(ctx: Ctx) -> Result:
    from perjury.index_i24 import g1_check, run as build
    r = Result("G1")
    idx = ctx.index()
    if idx is None and not ctx.fixture:
        idx = await build("auto", False, ctx.s.index_path, ctx.s)
        ctx._index = idx
    if idx is None:
        r.status, r.note = "FAIL", "no index file"
        return r
    ok, msg = g1_check(idx)
    r.status, r.note, r.data = ("PASS" if ok else "FAIL"), f"source={idx.get('source')} {msg}", {"ok": ok}
    if not ok:
        r.steps = ["Regex failed? python -m perjury.index_i24 --source vss (duration/caption clustering fallback)",
                   "Fewer than 2 scenes recoverable -> decision tree (§11)"]
    return r


# ---- G2 stock baseline ----
async def g2(ctx: Ctx) -> Result:
    r = Result("G2")
    sem = asyncio.Semaphore(3)

    async def one(claim, scene):
        async with sem:
            try:
                d = await ctx.c.vss.search_and_answer(claim, ctx.s.camera_id)
                return {"claim": claim, "scene": scene, "classification": d["classification"], "hits": d["hits"],
                        "answer": (d.get("answer") or "")[:160]}
            except Exception as e:
                return {"claim": claim, "scene": scene, "error": f"{type(e).__name__}: {str(e)[:80]}"}
    rows = await asyncio.gather(*(one(c, sc) for c, sc in G2_LIES))
    answered = [x for x in rows if "classification" in x]
    false_n = sum(x["classification"] == "FALSE" for x in answered)
    r.data = {"rows": rows, "false": false_n, "answered": len(answered)}
    r.status = "PASS" if len(answered) >= 8 else "FAIL"
    r.note = (f"stock said FALSE to {false_n}/{len(answered)} planted lies "
              f"(hits {[x.get('hits') for x in answered]}); "
              + ("pitch = 'evidence audit' (stock rejects >= 8/10)" if false_n >= 8 else "pitch = 'stock believes the lie'"))
    r.steps = ["Hand-check every UNCLASSIFIED answer (two people)"]
    return r


# ---- G3 hero integrity ----
def _video_wh(seg: dict) -> tuple[int, int]:
    shape = seg.get("video_shape") or [2160, 3840]
    return int(shape[1]), int(shape[0])


async def tow_juror(ctx: Ctx, seg: dict) -> dict:
    """P-TOW on one segment; for the first yes panel: P-GROUND -> 4K crop -> YOLO zoom-check."""
    from perjury.cosmos import normalize_xyxy, xyxy1000_to_pixels
    from perjury.probes import tow_panel_times
    m = ctx.c.media
    times = tow_panel_times(seg["end"] - seg["start"])
    grid = m.grid2x2(await m.keyframes(seg["source"], times))
    p_tow = ctx.probe("P-TOW")
    pr = await ctx.c.cosmos.probe(grid, p_tow.prompt, p_tow.version, timeout_s=30)
    out = {"camera": seg["camera"], "source": seg["source"], "yes": False, "zoom_ok": None, "kinds": [],
           "latency_ms": pr.latency_ms, "error": pr.error}
    panels = [p for p in ((pr.parsed or {}).get("panels") or []) if isinstance(p, dict) and p.get("towing")]
    if not panels:
        return out
    out["yes"] = True
    out["kinds"] = [t.get("towing_vehicle") for p in panels for t in p["towing"] if isinstance(t, dict)]
    panel = int(panels[0].get("panel") or 1)
    t = times[min(max(panel, 1), 4) - 1]
    frame = (await m.keyframes(seg["source"], [t]))[0]
    p_g = ctx.probe("P-GROUND")
    gr = await ctx.c.cosmos.probe(frame, p_g.prompt, p_g.version, timeout_s=30)
    box = normalize_xyxy((gr.parsed or {}).get("bbox_2d"))
    if not box:
        out["zoom_ok"] = False
        return out
    w, h = _video_wh(seg)
    crop = await m.crop_clip(seg["source"], t, xyxy1000_to_pixels(box, w, h), pad=0.15)   # as tiers.py pads
    z = await ctx.c.yolo.zoom_check(crop, None)
    out.update(zoom_ok=z.ok, zoom=z.model_dump(), grounded=box)
    return out


def _s1_moments(ctx: Ctx, idx: dict, qvec: list[float] | None, k: int = 6) -> tuple[list[dict], str]:
    from perjury.embed import cosine
    segs = [x for x in idx["segments"] if x["scene"] == 1]
    vis = ctx.c.embed.visual_vectors() if qvec else None
    if vis:
        score, how = (lambda x: cosine(qvec, vis[x["source"]]) if x["source"] in vis else -1.0), "embed1"
    else:
        score, how = (lambda x: (x.get("object_counts") or {}).get("truck", 0)), "yolo-truck-rank"
    best: dict[str, dict] = {}
    for x in sorted(segs, key=score, reverse=True):
        best.setdefault(x["camera"], x)
    return list(best.values())[:k], how


async def g3(ctx: Ctx) -> Result:
    r = Result("G3")
    idx = ctx.index()
    if not idx:
        r.status, r.note = "FAIL", "needs the scene index (G1)"
        return r
    r.steps = ["P4 eyeballs: scrub the 16 Scene 2 cameras x 4 moments for any trailer (G3 sheet)",
               "Note which vehicle kinds tow in Scene 1; if mostly SUVs, hero wording = 'A vehicle is towing a trailer'"]
    s2 = {}
    for x in idx["segments"]:
        if x["scene"] == 2:
            s2.setdefault(x["camera"], []).append(x)
    s2_moments = [sorted(v, key=lambda x: x["start"])[len(v) // 2] for v in s2.values()]
    try:
        qvec = await ctx.c.embed.embed_text(TOW_QUERY)
    except Exception:
        qvec = None
    s1_moments, how = _s1_moments(ctx, idx, qvec)
    sem = asyncio.Semaphore(ctx.s.cosmos_concurrency)

    async def guarded(seg):
        async with sem:
            try:
                return await tow_juror(ctx, seg)
            except Exception as e:
                return {"camera": seg["camera"], "source": seg["source"], "yes": False, "error": str(e)[:120]}
    s2_res, s1_res = await asyncio.gather(asyncio.gather(*(guarded(x) for x in s2_moments)),
                                          asyncio.gather(*(guarded(x) for x in s1_moments)))
    n2 = max(1, len(s2_res))
    fpr_before = sum(x["yes"] for x in s2_res) / n2
    fpr_after = sum(bool(x["yes"] and x.get("zoom_ok")) for x in s2_res) / n2
    s1_pass = sum(bool(x["yes"] and x.get("zoom_ok")) for x in s1_res)
    kinds: dict[str, int] = {}
    for x in s1_res:
        for k in x.get("kinds") or []:
            kinds[k] = kinds.get(k, 0) + 1
    r.data = {"s2": s2_res, "s1": s1_res, "fpr_before": fpr_before, "fpr_after": fpr_after, "s1_pass": s1_pass,
              "s1_retrieval": how, "s1_kinds": kinds}
    r.status = "PASS" if fpr_after < G3_MAX_FPR and s1_pass >= G3_MIN_S1 else "FAIL"
    r.note = (f"S2 FPR {fpr_before:.0%} -> {fpr_after:.0%} after zoom (n={len(s2_res)}); "
              f"S1 {s1_pass}/{len(s1_res)} jurors pass zoom ({how}); kinds={kinds}")
    if r.status == "FAIL":
        r.steps.append("FAIL -> hero = snow flip ('The road is covered in snow': S1 FALSE vs S2 TRUE)")
    return r


# ---- G4 Canary ----
async def g4(ctx: Ctx) -> Result:
    r = Result("G4")
    r.steps = ["Fallbacks: (d) recorded file upload -> wav.js -> Canary, then (e) typed"]
    if ctx.fixture:
        r.note = "fixture mode: Canary not testable"
        return r
    ready = await ctx.c.canary.health()
    wav_path = ctx.args.wav or ctx.s.env.get("PERJURY_G4_WAV") or str(CACHE / "g4.wav")
    if not Path(wav_path).exists():
        r.status = "SKIP" if ready else "FAIL"
        r.note = f"health ready={ready}; no reference WAV (pass --wav, 16 kHz mono)"
        return r
    expected = ctx.args.wav_text
    txt = Path(wav_path).with_suffix(".txt")
    if not expected and txt.exists():
        expected = txt.read_text().strip()
    try:
        out = await ctx.c.canary.transcribe(Path(wav_path).read_bytes())
    except Exception as e:
        r.status, r.note = "FAIL", f"health ready={ready}; transcribe failed: {str(e)[:160]}"
        return r
    words = lambda t: re.findall(r"[a-z0-9]+", (t or "").lower())  # noqa: E731
    match = 1.0
    if expected:
        exp, got = words(expected), set(words(out["text"]))
        match = sum(w in got for w in exp) / max(1, len(exp))
    r.data = {**out, "match": match, "ready": ready}
    r.status = "PASS" if out["latency_ms"] <= G4_MAX_MS and match >= 0.8 else "FAIL"
    r.note = f"ready={ready} model={out['model_id']} {out['latency_ms']} ms match={match:.0%} text={out['text'][:60]!r}"
    return r


# ---- G5 Cosmos throughput / format ----
async def g5(ctx: Ctx) -> Result:
    r = Result("G5")
    idx = ctx.index()
    if not idx:
        r.status, r.note = "FAIL", "needs the scene index (G1)"
        return r
    from perjury.prerun_scene_probes import plan
    jobs = plan(idx)
    jobs = (jobs[::max(1, len(jobs) // G5_CALLS)])[:G5_CALLS]
    p = ctx.probe("P-COND")

    async def one(job):
        from perjury.prerun_scene_probes import grid_for
        grid = await grid_for(job, ctx.c.media)
        return await ctx.c.cosmos.probe(grid, p.prompt, p.version, timeout_s=30, use_cache=False)
    t0 = time.monotonic()
    res = await asyncio.gather(*(one(j) for j in jobs), return_exceptions=True)
    wall = int((time.monotonic() - t0) * 1000)
    ok = [x for x in res if not isinstance(x, BaseException) and x.parsed is not None]
    errs = [str(x) if isinstance(x, BaseException) else (x.error or "") for x in res]
    lat = [x.latency_ms for x in res if not isinstance(x, BaseException) and x.latency_ms]
    p50 = int(statistics.median(lat)) if lat else 0
    n429 = sum("429" in e for e in errs)
    think = sum("<think>" in (x.raw_text or "") for x in res if not isinstance(x, BaseException))
    empty = sum(1 for x in res if not isinstance(x, BaseException) and not x.error and not x.raw_text)
    valid = len(ok) / max(1, len(res))
    r.data = {"valid": valid, "p50_ms": p50, "wall_ms": wall, "n429": n429, "think": think, "empty": empty,
              "errors": [e[:120] for e in errs if e]}
    r.status = "PASS" if valid >= G5_MIN_VALID and p50 < G5_MAX_P50_MS and n429 == 0 else "FAIL"
    r.note = (f"{len(ok)}/{len(res)} valid JSON, p50 {p50} ms, wall {wall} ms (x{len(res)} concurrent), "
              f"429s={n429}, <think> in {think}, empty={empty}")
    r.steps = ["Panel numbering: open one grid + answer and check the model's panel order",
               "Bbox scale: hand-box one vehicle, run P-GROUND, compare -> set COSMOS_BBOX_SCALE (1000 vs 1024)"]
    if r.status == "FAIL":
        r.steps += ["Empty outputs: PERJURY_COSMOS_NO_THINK=1 (enable_thinking false), re-run --only G5",
                    "p50 >= 10 s: jury of 3 (PERJURY_JURY_SIZE=3) and pre-run more; unusable -> PERJURY-LITE"]
    return r


# ---- G6 YOLO noise and scale ----
async def g6(ctx: Ctx) -> Result:
    r = Result("G6")
    idx = ctx.index()
    if not idx:
        r.status, r.note = "FAIL", "needs the scene index (G1)"
        return r
    segs = idx["segments"]
    person = [x for x in segs if "person" in (x.get("object_classes") or [])]
    rate = len(person) / max(1, len(segs))
    top = sorted(person, key=lambda x: -(x.get("persist") or {}).get("person", 0))[:5]
    shapes = {tuple((x.get("video_shape") or [0, 0])[:2]) for x in segs if x.get("video_shape")}
    is4k = bool(shapes) and all(h >= 2160 for h, _ in shapes)
    # zoom-check on a real vehicle: busiest-truck segment, a sidecar box (or the frame centre if no sidecar)
    seg = max(segs, key=lambda x: (x.get("object_counts") or {}).get("truck", 0))
    w, h = _video_wh(seg)
    box, t = (w // 2 - 300, h // 2 - 200, w // 2 + 300, h // 2 + 200), 1.0
    url_ok = None
    try:
        sc = await ctx.c.vss.detections(seg["source"])
        for f in (sc or {}).get("frames") or []:
            d = next((d for d in f.get("detections") or [] if d.get("label") in ("truck", "car")), None)
            if d and d.get("bbox"):
                x1, y1, x2, y2 = map(int, d["bbox"][:4])
                box, t = (x1, y1, x2, y2), float(f.get("time_sec") or 1.0)
                break
    except Exception:
        pass
    zoom = None
    try:
        try:
            await ctx.c.yolo.infer(url=ctx.c.media.presign(seg["source"]))
            url_ok = True
        except Exception:
            url_ok = False
        crop = await ctx.c.media.crop_clip(seg["source"], t, box)
        zoom = (await ctx.c.yolo.zoom_check(crop, None)).model_dump()
    except Exception as e:
        zoom = {"ok": False, "error": f"{type(e).__name__}: {str(e)[:120]}"}
    boxes = bool(zoom and zoom.get("label"))
    r.data = {"person_rate": rate, "person_segments": len(person), "top5": [
        {"source": x["source"], "persist": (x.get("persist") or {}).get("person")} for x in top],
        "video_shapes": sorted(shapes), "is4k": is4k, "zoom": zoom, "url_field_ok": url_ok}
    r.status = "PASS" if boxes else "FAIL"
    r.note = (f"person in {len(person)}/{len(segs)} segments ({rate:.1%}); 4K={is4k}; "
              f"infer url-field={'ok' if url_ok else 'failed (video_base64 used)'}; "
              f"zoom label={zoom.get('label') if zoom else None} cover={zoom.get('cover') if zoom else None}")
    r.steps = [f"Eyeball the top-5 'person' segments: {[x['source'].rsplit('/', 2)[-2] for x in top]}"]
    if rate > G6_PERSON_NOISE:
        r.steps.append("person > 10%: absence rule leans on the jury (>= 14/16) + persistence >= 3 frames; report noise")
    if not boxes:
        r.steps.append("zoom-check failed: SUPPORTED needs m+1 jurors with no zoom")
    return r


GATES: dict[str, Callable[[Ctx], Awaitable[Result]]] = {"G0": g0, "G1": g1, "G2": g2, "G3": g3, "G4": g4,
                                                          "G5": g5, "G6": g6}


async def run_gate(name: str, ctx: Ctx) -> Result:
    t0 = time.monotonic()
    try:
        r = await asyncio.wait_for(GATES[name](ctx), TIMEBOX[name])
    except asyncio.TimeoutError:
        r = Result(name, "FAIL", f"timebox {TIMEBOX[name]} s exceeded")
    except Exception as e:
        r = Result(name, "FAIL", f"{type(e).__name__}: {str(e)[:200]}")
    r.ms = int((time.monotonic() - t0) * 1000)
    if ctx.fixture and r.status != "SKIP":
        r.note = f"[FIXTURE] {r.note}"
    return r


async def main_async(args) -> list[Result]:
    s = settings()
    ctx = Ctx(s, args)
    names = [g.strip().upper() for g in args.only.split(",")] if args.only else list(GATES)
    out = []
    for n in names:   # sequential: G1 feeds G3/G5/G6, and the GPU host is shared
        out.append(await run_gate(n, ctx))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="PERJURY gates G0-G6 (§11)")
    ap.add_argument("--only", help="comma list, e.g. G4 or G3,G5")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--wav", help="G4 reference WAV (16 kHz mono)")
    ap.add_argument("--wav-text", help="G4 expected transcript")
    args = ap.parse_args(argv)
    s = settings()
    res = asyncio.run(main_async(args))
    if args.json:
        print(json.dumps([r.__dict__ for r in res], indent=1, default=str))
    else:
        print(f"PERJURY preflight · mode={s.mode}" +
              (" (results exercise the fixture fakes, not live endpoints)" if s.mode != "live" else ""))
        print(f"{'gate':<5} {'status':<6} {'time':>7}  note")
        for r in res:
            print(f"{r.gate:<5} {r.status:<6} {r.ms / 1000:>6.1f}s  {r.note}")
        steps = [(r.gate, st) for r in res for st in r.steps]
        if steps:
            print("\nHuman steps:")
            for g, st in steps:
                print(f"  [{g}] {st}")
    return 1 if any(r.status == "FAIL" for r in res) else 0


if __name__ == "__main__":
    sys.exit(main())
