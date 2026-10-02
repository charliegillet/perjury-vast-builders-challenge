"""Exhibit A reel (§5): juror keyframes with the grounded boxes drawn on, ~6 s mp4, published via VSS videos/upload so
DataEngine indexes the verdict as searchable video. Never written to the pipeline buckets directly.

    python -m perjury.exhibit --events cache/replays/<run>.jsonl [--atom a1] [--dry-run]
"""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
from typing import Optional

from perjury.config import CACHE, settings
from perjury.events import load_recording
from perjury.media import draw_boxes, stills_to_mp4

REEL_SECONDS = 6.0
MAX_STILLS = 4


def exhibit_stills(events: list[dict], atom_id: Optional[str] = None) -> list[dict]:
    """Yes-votes with a grounded box (from `juror` + `ground` events) -> [{source, t, camera, panel, bbox_2d, atom_id}]."""
    grounds = {}
    for ev in events:
        if ev["event"] == "ground":
            d = ev["data"]
            grounds[(d.get("atom_id"), d.get("camera"), d.get("panel"))] = d.get("bbox_2d")
    out = []
    for ev in events:
        if ev["event"] != "juror":
            continue
        d = ev["data"]
        v = d.get("vote") or {}
        if v.get("vote") != "yes" or (atom_id and d.get("atom_id") != atom_id):
            continue
        j = v.get("juror") or {}
        times = j.get("times") or []
        for p in v.get("yes_panels") or []:
            box = v.get("grounded") or grounds.get((d.get("atom_id"), v.get("camera"), p))
            if j.get("source") and box and 1 <= p <= len(times):
                out.append({"source": j["source"], "t": times[p - 1], "camera": v.get("camera"), "panel": p,
                            "bbox_2d": box, "atom_id": d.get("atom_id"), "zoom_ok": v.get("zoom_ok")})
                break
    return out[:MAX_STILLS]


async def build_reel(stills: list[dict], media, verdict_line: str = "") -> bytes:
    jpegs = []
    for st in stills:
        frame = (await media.keyframes(st["source"], [st["t"]], width=1280))[0]
        label = f"juror {st['camera']} · panel {st['panel']}" + (" · zoom ✓" if st.get("zoom_ok") else "")
        jpegs.append(draw_boxes(frame, [{"xyxy1000": st["bbox_2d"], "label": label}],
                                caption=f"PERJURY Exhibit A · {verdict_line}"[:120]))
    if not jpegs:
        raise ValueError("no grounded yes-votes to build an exhibit from")
    return await stills_to_mp4(jpegs, seconds_each=REEL_SECONDS / len(jpegs))


async def publish(mp4: bytes, clients, run_id: str, *, bus=None) -> dict:
    meta = {"is_public": True, "camera_id": "perjury-exhibit", "location": "nashville",
            "tags": ["perjury", "exhibit", run_id], "capture_type": "traffic"}
    return await clients.vss.upload(mp4, f"perjury_exhibit_{run_id}.mp4", meta, bus=bus)


async def run(events_path: Path, atom_id: Optional[str] = None, dry_run: bool = False) -> dict:
    from perjury.clients import build_clients
    c = build_clients(settings())
    events = load_recording(events_path)
    run_id = next((e["data"].get("run_id") for e in events if e["event"] == "run"), events_path.stem)
    verdict = next((e["data"].get("verdict") for e in events if e["event"] == "verdict"), "")
    stills = exhibit_stills(events, atom_id)
    if not stills:
        raise SystemExit(f"no grounded yes-votes in {events_path.name}{' for ' + atom_id if atom_id else ''}")
    mp4 = await build_reel(stills, c.media, f"verdict {verdict}")   # FakeMedia renders the stills in fixture mode
    out = CACHE / "exhibits" / f"{run_id}.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(mp4)
    res = {"run_id": run_id, "stills": len(stills), "bytes": len(mp4), "path": str(out)}
    if not dry_run:
        res["upload"] = await publish(mp4, c, run_id)
    print(json.dumps(res))
    return res


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description="Build and upload the Exhibit A reel")
    ap.add_argument("--events", type=Path, required=True, help="recorded run JSONL (EventBus record_to)")
    ap.add_argument("--atom")
    ap.add_argument("--dry-run", action="store_true", help="write cache/exhibits/<run>.mp4 only")
    a = ap.parse_args(argv)
    asyncio.run(run(a.events, a.atom, a.dry_run))


if __name__ == "__main__":
    main()
