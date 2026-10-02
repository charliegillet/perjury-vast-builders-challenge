"""Pre-run the scene-wide jurors (§6 P-COND, P-COUNT) on every camera of every scene -> cache/scene_probes.json.

    python -m perjury.prerun_scene_probes [--concurrency 4] [--scenes 1,2,3] [--out PATH]

Panels sit at 10/35/60/85 % of the scene window on the camera's parent video (falls back to the segment holding each
time). Prompt text and versions come from perjury.probes. Cosmos answers are disk-cached, so a re-run is cheap.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

from perjury.config import CACHE, settings

FRACTIONS = (0.10, 0.35, 0.60, 0.85)


def _probes():
    from perjury import probes  # core-owned; imported lazily
    return probes.PROBES["P-COND"], probes.PROBES["P-COUNT"]


def plan(index: dict, scenes: list[int] | None = None) -> list[dict]:
    """One job per (scene, camera): parent video + grid times, plus per-time (segment, offset) fallbacks."""
    jobs = []
    for sc, meta in sorted(index["scenes"].items(), key=lambda kv: int(kv[0])):
        if scenes and int(sc) not in scenes:
            continue
        for cam in meta["cameras"]:
            segs = sorted((s for s in index["segments"] if s["scene"] == int(sc) and s["camera"] == cam),
                          key=lambda s: s["start"])
            if not segs:
                continue
            t0, t1 = segs[0]["start"], segs[-1]["end"]
            times = [round(t0 + (t1 - t0) * f, 2) for f in FRACTIONS]
            fallback = []
            for t in times:
                seg = next((s for s in segs if s["start"] <= t < s["end"]), segs[-1])
                fallback.append((seg["source"], round(t - seg["start"], 2)))
            jobs.append({"scene": int(sc), "camera": cam, "parent": segs[0]["original_video"], "times": times,
                         "fallback": fallback})
    return jobs


async def grid_for(job: dict, media) -> bytes:
    try:
        frames = await media.keyframes(job["parent"], job["times"])
    except Exception:
        frames = [(await media.keyframes(src, [t]))[0] for src, t in job["fallback"]]
    return media.grid2x2(frames, [f"t={t:.0f}s" for t in job["times"]])


async def run(concurrency: int = 4, scenes: list[int] | None = None, out: Path | None = None) -> dict:
    from perjury.clients import build_clients
    s = settings()
    c = build_clients(s)
    p_cond, p_count = _probes()
    index = json.loads(s.index_path.read_text())
    jobs = plan(index, scenes)
    sem = asyncio.Semaphore(concurrency)
    result: dict = {"version": 1, "source": "fixture" if s.mode != "live" else "live",
                    "probe_versions": {p.name: p.version.split()[-1] for p in (p_cond, p_count)},
                    "ran_at": datetime.now().astimezone().isoformat(timespec="seconds"), "scenes": {}}
    stats = {"ok": 0, "null": 0, "fail": 0}

    async def one(job):
        async with sem:
            try:
                grid = await grid_for(job, c.media)
            except Exception as e:
                stats["fail"] += 1
                print(f"[prerun] scene{job['scene']} {job['camera']} keyframes failed: {type(e).__name__}",
                      file=sys.stderr)
                return
            rec = {"grid_times": job["times"]}
            for p in (p_cond, p_count):
                r = await c.cosmos.probe(grid, p.prompt, p.version, timeout_s=30.0)
                rec[p.name] = {"parsed": r.parsed, "latency_ms": r.latency_ms, "cached": r.cached,
                               "image_sha": r.image_sha[:16], **({"error": r.error} if r.error else {})}
                stats["ok" if r.parsed is not None else "null"] += 1
            result["scenes"].setdefault(str(job["scene"]), {})[job["camera"]] = rec

    await asyncio.gather(*(one(j) for j in jobs))
    out = out or CACHE / ("scene_probes.json" if s.mode == "live" else "scene_probes.fixture-run.json")
    out.write_text(json.dumps(result, indent=1))
    print(f"prerun: cameras={len(jobs)} answers ok={stats['ok']} null={stats['null']} grid_fail={stats['fail']} -> {out}")
    return result


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description="Pre-run P-COND / P-COUNT on all cameras")
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--scenes", help="comma list, e.g. 2,3")
    ap.add_argument("--out", type=Path)
    a = ap.parse_args(argv)
    asyncio.run(run(a.concurrency, [int(x) for x in a.scenes.split(",")] if a.scenes else None, a.out))


if __name__ == "__main__":
    main()
