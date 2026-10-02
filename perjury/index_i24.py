"""G1: build cache/i24_index.json (BUILD-CONTRACT index schema) from Pack A.

    python -m perjury.index_i24 [--source vastdb|vss|auto] [--sidecars] [--out cache/i24_index.json]

1. VastDB pushdown camera_id == PERJURY_CAMERA_ID on vss-collection, vector columns excluded (vastdb SDK; VM only).
2. Fallback: VSS videos/explore -> tools/segments per parent.
scene/camera come from source/original_video by three regex variants; if none match, parents are clustered by
duration (90 s => scene 1) and caption "snow" (scene 2 vs 3). --sidecars fills Segment.persist / video_shape from
videos/detections. Prints one G1 PASS/FAIL line.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from collections import defaultdict
from typing import Iterable, Optional

from perjury.config import CACHE, Settings, settings
from perjury.types import Segment
from perjury.yolo import parse_counts, peak_counts, persistence

SCENE_RES = (re.compile(r"scene(\d)_p(\d)c(\d)", re.I),
             re.compile(r"Scene(\d)[_/-]p(\d)c(\d)", re.I),
             re.compile(r"scene(\d).*?p(\d+)c(\d+)", re.I))
CAM_RE = re.compile(r"p(\d+)c(\d+)", re.I)
CHUNK_RE = re.compile(r"chunk[_-](\d+)", re.I)
SEG_RE = re.compile(r"seg(?:ment)?[_-]?(\d+)", re.I)
VECTOR_COLS = {"vectors", "vectors_visual"}
G1_MIN_ROWS, G1_MIN_CAMS = 600, 14
SCENE_LABELS = {1: "free-flow", 2: "snow", 3: "stop-and-go"}


def parse_scene_cam(*texts: Optional[str]) -> tuple[Optional[int], Optional[str]]:
    for rx in SCENE_RES:
        for t in texts:
            m = rx.search(t or "")
            if m:
                return int(m.group(1)), f"p{int(m.group(2))}c{int(m.group(3))}"
    for t in texts:
        m = CAM_RE.search(t or "")
        if m:
            return None, f"p{int(m.group(1))}c{int(m.group(2))}"
    return None, None


def _num(row: dict, *keys) -> Optional[float]:
    for k in keys:
        v = row.get(k)
        try:
            if v is not None and not isinstance(v, bool):
                return float(v)
        except (TypeError, ValueError):
            pass
    return None


def _classes(v) -> list[str]:
    if isinstance(v, (list, tuple)):
        return [str(x) for x in v]
    if isinstance(v, str) and v.strip():
        try:
            j = json.loads(v)
            if isinstance(j, list):
                return [str(x) for x in j]
            if isinstance(j, dict):
                return list(j)
        except ValueError:
            return [x.strip() for x in v.split(",") if x.strip()]
    return []


def _shape(v) -> Optional[list[int]]:
    if isinstance(v, str):
        try:
            v = json.loads(v)
        except ValueError:
            return None
    return [int(x) for x in v] if isinstance(v, (list, tuple)) and len(v) >= 2 else None


def cluster_scenes(parents: dict[str, list[dict]]) -> dict[str, int]:
    """Fallback when filenames don't name the scene: 90 s parents => scene 1; else majority 'snow' captions => 2, else 3."""
    out = {}
    for p, rows in parents.items():
        dur = max((r.get("end") or 0) for r in rows) - min((r.get("start") or 0) for r in rows)
        snow = sum("snow" in (r.get("caption") or "").lower() for r in rows)
        out[p] = 1 if dur >= 80 else (2 if snow * 2 >= len(rows) else 3)
    return out


def build_index(raw_rows: Iterable[dict], camera_id: str, source_label: str) -> dict:
    """Raw VastDB / VSS rows -> contract index dict. Pure (tested offline)."""
    rows = []
    for r in raw_rows:
        src = r.get("source")
        if not src:
            continue
        rows.append({**r, "start": _num(r, "start_sec", "start_time_sec", "segment_start_sec", "start_time", "start"),
                     "end": _num(r, "end_sec", "end_time_sec", "segment_end_sec", "end_time", "end"),
                     "caption": r.get("reasoning_content") or r.get("caption") or ""})
    parents: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        parents[r.get("original_video") or r["source"].rsplit("/", 1)[0]].append(r)
    clustered: Optional[dict[str, int]] = None
    segs: list[Segment] = []
    cam_fallback: dict[str, str] = {}
    for parent, prs in parents.items():
        prs.sort(key=lambda r: (r["start"] if r["start"] is not None else 1e9, r["source"]))
        for i, r in enumerate(prs):
            scene, cam = parse_scene_cam(r["source"], parent)
            if scene is None:
                clustered = clustered or cluster_scenes(parents)
                scene = clustered[parent]
            if cam is None:
                cam = cam_fallback.setdefault(parent, f"cam{len(cam_fallback) + 1}")
            m = SEG_RE.search(r["source"].rsplit("/", 1)[-1])
            start = r["start"] if r["start"] is not None else i * 5.0
            counts = parse_counts(r.get("object_counts"))
            segs.append(Segment(source=r["source"], original_video=parent, scene=scene, camera=cam,
                                seg=int(m.group(1)) if m else i, start=start,
                                end=r["end"] if r["end"] is not None else start + 5.0,
                                object_classes=_classes(r.get("object_classes")) or sorted(counts),
                                object_counts=counts, persist=r.get("persist") or {}, caption=r["caption"],
                                processing_time=_num(r, "processing_time"), video_shape=_shape(r.get("video_shape")),
                                location=r.get("location"), camera_id=r.get("camera_id") or camera_id))
    # Pipeline parents are 30-second upload chunks, each with local segment times.
    # Reconstruct the camera timeline from the explicit chunk sequence rather than
    # confusing upload wall-clock timestamps with capture times.
    chunked: dict[tuple[int, str], dict[str, list[Segment]]] = defaultdict(lambda: defaultdict(list))
    for seg in segs:
        if CHUNK_RE.search(seg.original_video):
            chunked[(seg.scene, seg.camera)][seg.original_video].append(seg)
    for group in chunked.values():
        spans = [max(s.end for s in ss) for ss in group.values()]
        span = max(spans)  # the final chunk can be shorter
        for parent, ss in group.items():
            chunk = int(CHUNK_RE.search(parent).group(1))
            for seg in ss:
                seg.start += chunk * span
                seg.end += chunk * span
        for number, seg in enumerate(sorted((s for ss in group.values() for s in ss), key=lambda s: s.start)):
            seg.seg = number
    segs.sort(key=lambda s: (s.scene, s.camera, s.start))
    scenes: dict[str, dict] = {}
    for sc in sorted({s.scene for s in segs}):
        ss = [s for s in segs if s.scene == sc]
        scenes[str(sc)] = {"label": SCENE_LABELS.get(sc, f"scene {sc}"),
                           "duration": round(max(s.end for s in ss) - min(s.start for s in ss)),
                           "cameras": sorted({s.camera for s in ss})}
    missing_scenes = sorted({1, 2, 3} - {int(sc) for sc in scenes})
    camera_counts = {sc: len(meta["cameras"]) for sc, meta in scenes.items()}
    complete = (len(segs) >= G1_MIN_ROWS and not missing_scenes
                and all(count >= G1_MIN_CAMS for count in camera_counts.values()))
    reasons = []
    if len(segs) < G1_MIN_ROWS:
        reasons.append(f"Only {len(segs)} indexed segments available; full-pack target is {G1_MIN_ROWS}.")
    if missing_scenes:
        reasons.append("Scenes " + ", ".join(map(str, missing_scenes)) + " are absent from the index.")
    for sc, count in camera_counts.items():
        if count < G1_MIN_CAMS:
            reasons.append(f"Scene {sc} has {count} cameras; full-pack target is {G1_MIN_CAMS}.")
    return {"version": 1, "source": source_label, "camera_id": camera_id, "scenes": scenes,
            "coverage": {"complete": complete, "source": source_label,
                         "expected": {"minimum_segments": G1_MIN_ROWS, "scenes": [1, 2, 3],
                                      "minimum_cameras_per_scene": G1_MIN_CAMS},
                         "actual": {"segments": len(segs), "scenes": sorted(map(int, scenes)),
                                    "cameras_per_scene": camera_counts},
                         "missing_scenes": missing_scenes, "reasons": reasons},
            "segments": [s.model_dump(mode="json") for s in segs]}


def g1_check(index: dict) -> tuple[bool, str]:
    """§11 G1: >= 600 rows, 3 scenes, >= 14 cameras each, segments ordered."""
    segs = index.get("segments") or []
    scenes = index.get("scenes") or {}
    cams = {k: len(v.get("cameras") or []) for k, v in scenes.items()}
    by_cam: dict[tuple, list[float]] = defaultdict(list)
    for s in segs:
        by_cam[(s["scene"], s["camera"])].append(s["start"])
    ordered = all(v == sorted(v) for v in by_cam.values())
    pts = [s.get("processing_time") for s in segs if s.get("processing_time") is not None]
    shapes = {tuple(s["video_shape"][:2]) for s in segs if s.get("video_shape")}
    ok = len(segs) >= G1_MIN_ROWS and len(scenes) >= 3 and all(n >= G1_MIN_CAMS for n in cams.values()) and ordered
    msg = (f"rows={len(segs)} scenes={len(scenes)} cams={cams} ordered={ordered} "
           f"avg_processing_time={f'{sum(pts) / len(pts):.2f}s' if pts else 'n/a'} video_shape={sorted(shapes)[:2]}")
    return ok, msg


def pull_vastdb(s: Settings) -> list[dict]:
    """VM only (requirements-vm.txt). Vector columns are never selected."""
    import vastdb  # noqa: WPS433
    ep = s.vdb_endpoint if "://" in s.vdb_endpoint else f"http://{s.vdb_endpoint}"
    session = vastdb.connect(endpoint=ep, access=s.s3_access, secret=s.s3_secret, ssl_verify=False)
    with session.transaction() as tx:
        table = tx.bucket(s.vdb_bucket).schema(s.vdb_schema).table(s.vdb_collection)
        cols = [c.name for c in table.columns() if c.name not in VECTOR_COLS]
        try:
            from ibis import _  # noqa: WPS433
            reader = table.select(columns=cols, predicate=(_.camera_id == s.camera_id))
        except Exception:
            reader = table.select(columns=cols)
        rows = reader.read_all().to_pylist()
    return [r for r in rows if (r.get("camera_id") or s.camera_id) == s.camera_id]


async def pull_vss(clients, camera_id: str) -> list[dict]:
    parents, off = [], 0
    while True:
        d = await clients.vss.explore(limit=48, offset=off)
        batch = [x for x in (d.get("videos") or d.get("results") or d.get("items") or []) if isinstance(x, dict)]
        parents += [x for x in batch if (x.get("camera_id") or camera_id) == camera_id]
        if len(batch) < 48 or off > 2000:
            break
        off += 48
    rows = []
    for p in parents:
        pv = p.get("original_video") or p.get("source")
        if pv:
            rows += await clients.vss.segments(pv)
    return rows


async def fill_sidecars(index: dict, clients, concurrency: int = 8, limit: int | None = None) -> int:
    sem, n = asyncio.Semaphore(concurrency), 0

    async def one(seg):
        nonlocal n
        async with sem:
            try:
                sc = await clients.vss.detections(seg["source"])
            except Exception:
                return
            if sc:
                seg["persist"] = persistence(sc)
                seg["video_shape"] = seg.get("video_shape") or sc.get("video_shape")
                seg["object_counts"] = seg.get("object_counts") or peak_counts(sc)
                n += 1
    await asyncio.gather(*(one(x) for x in index["segments"][: limit or None]))
    return n


async def run(source: str = "auto", sidecars: bool = False, out=None, s: Settings | None = None) -> dict:
    from perjury.clients import build_clients
    s = s or settings()
    clients = build_clients(s)
    index, errors = None, []
    if source in ("auto", "vastdb") and s.mode == "live":
        try:
            index = build_index(pull_vastdb(s), s.camera_id, "vastdb")
        except Exception as e:
            errors.append(f"vastdb: {type(e).__name__}: {str(e)[:120]}")
    if (index is None or not index["segments"]) and source in ("auto", "vss"):
        try:
            index = build_index(await pull_vss(clients, s.camera_id), s.camera_id,
                                "vss-tools" if s.mode == "live" else "fixture")
        except Exception as e:
            errors.append(f"vss: {type(e).__name__}: {str(e)[:120]}")
    if index is None:
        raise SystemExit("G1 FAIL no rows (" + "; ".join(errors) + ")")
    if sidecars:
        print(f"sidecars filled: {await fill_sidecars(index, clients)}")
    out = out or CACHE / ("i24_index.json" if s.mode == "live" else "i24_index.fixture-run.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(index, indent=1))
    ok, msg = g1_check(index)
    for e in errors:
        print(f"note: {e}", file=sys.stderr)
    print(f"G1 {'PASS' if ok else 'FAIL'} source={index['source']} {msg} -> {out}")
    return index


def main(argv=None) -> None:
    from pathlib import Path
    ap = argparse.ArgumentParser(description="Build cache/i24_index.json (G1)")
    ap.add_argument("--source", choices=("auto", "vastdb", "vss"), default="auto")
    ap.add_argument("--sidecars", action="store_true", help="fetch videos/detections to fill persist/video_shape")
    ap.add_argument("--out", type=Path)
    a = ap.parse_args(argv)
    asyncio.run(run(a.source, a.sidecars, a.out))


if __name__ == "__main__":
    main()
