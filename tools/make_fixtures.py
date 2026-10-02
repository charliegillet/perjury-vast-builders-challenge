#!/usr/bin/env python3
"""Generate deterministic offline fixtures that mimic the real Pack A shapes (FINAL-IDEA-v3 §13).

Writes:
  cache/fixture_i24_index.json   the same schema index_i24.py writes for the real VastDB pull (690 segments)
  cache/fixture_scene_probes.json  pre-run P-COND / P-COUNT juror answers per scene x camera (prerun_scene_probes.py schema)
  cache/fixture_truth.json       hidden ground truth that ONLY perjury/fakes.py may read (never live code)

Scenes follow I24-3D Table 1: S1 free-flow 90 s x 17 cams, S2 snow 60 s x 16, S3 stop-and-go 60 s x 16; 5 s segments.
Trailers in S1 and S3, none in S2; no pedestrians anywhere (YOLO calls a sign 'person' for a frame or two: noise floor).
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache"
ALL_CAMS = [f"p{p}c{c}" for p in (1, 2, 3) for c in range(1, 7)]
SCENES = {
    1: {"label": "free-flow", "duration": 90, "drop": ["p2c4"]},
    2: {"label": "snow", "duration": 60, "drop": ["p1c2", "p3c5"]},
    3: {"label": "stop-and-go", "duration": 60, "drop": ["p1c6", "p2c3"]},
}
SEG = 5.0


def h(*parts) -> float:
    """Deterministic pseudo-random in [0, 1)."""
    d = hashlib.sha256("|".join(map(str, parts)).encode()).digest()
    return int.from_bytes(d[:8], "big") / 2**64


CAPTIONS = {
    1: ["Multi-lane highway viewed from a high fixed camera; traffic moves freely at speed in both directions. "
        "Several cars and a semi-truck travel in the right lanes on a dry road in daylight.",
        "Dry highway in daylight with free-flowing traffic; sedans, SUVs and a box truck pass the camera.",
        "Overhead view of a busy interstate; vehicles travel at highway speed with steady spacing on dry pavement."],
    2: ["Highway in winter conditions with snow on the shoulders and median; traffic moves slowly in daylight.",
        "Snow and slush beside the roadway; cars and trucks proceed slowly with headlights on, overcast daylight.",
        "Wet road with snow banks along the edges; slow traffic in both directions under grey skies."],
    3: ["Dense stop-and-go traffic on a multi-lane highway; vehicles are queued and barely moving in daylight.",
        "Congested interstate with long queues; a semi-truck occludes cars in the far lanes, dry road.",
        "Heavy traffic creeping forward bumper to bumper; brake lights visible, daylight, dry pavement."],
}
TOW_PHRASES = {1: " A pickup truck towing a small utility trailer is visible in the middle lanes.",
               3: " An SUV pulling an enclosed trailer is caught in the queue."}


def build():
    segments, truth = [], {"towing": {}, "people": 0, "scene_conditions": {}}
    for scene, meta in SCENES.items():
        cams = [c for c in ALL_CAMS if c not in meta["drop"]]
        nseg = int(meta["duration"] // SEG)
        truth["scene_conditions"][str(scene)] = {
            1: {"road": "A", "traffic": "A", "light": "A"},
            2: {"road": "C", "traffic": "B", "light": "A"},
            3: {"road": "A", "traffic": "C", "light": "A"},
        }[scene]
        for cam in cams:
            parent = f"s3://vss-chunks/i24/scene{scene}_{cam}.mp4"
            for i in range(nseg):
                src = f"s3://vss-chunks-segments/i24/scene{scene}_{cam}/seg_{i:03d}.mp4"
                base = {1: (14, 3), 2: (8, 2), 3: (22, 4)}[scene]
                cars = base[0] + int(h(src, "car") * 8)
                trucks = base[1] + int(h(src, "truck") * 3)
                counts = {"car": cars, "truck": trucks}
                classes = ["car", "truck"]
                persist = {"car": 120, "truck": 90}
                if h(src, "bus") < 0.04:
                    counts["bus"] = 1; classes.append("bus"); persist["bus"] = 20
                # YOLO noise: a sign/pole called 'person' for 1-2 frames in ~1.5% of S1/S3 segments, never S2.
                if scene != 2 and h(src, "person") < 0.015:
                    counts["person"] = 1; classes.append("person"); persist["person"] = 1 + int(h(src, "pp") * 2)
                # Towing truth: S1 and S3 have trailers on some cameras/segments; S2 has none.
                tow = scene in (1, 3) and h(src, "tow") < (0.16 if scene == 1 else 0.10)
                if tow:
                    truth["towing"][src] = {"towing_vehicle": "pickup" if scene == 1 else "suv",
                                            "trailer": "utility" if scene == 1 else "enclosed",
                                            "panels": sorted({1 + int(h(src, "pan", k) * 4) for k in range(3)})}
                cap = CAPTIONS[scene][int(h(src, "cap") * 3)]
                if tow and h(src, "capmention") < 0.5:
                    cap += TOW_PHRASES[scene]
                segments.append({
                    "source": src, "original_video": parent, "scene": scene, "camera": cam, "seg": i,
                    "start": i * SEG, "end": (i + 1) * SEG, "object_classes": classes, "object_counts": counts,
                    "persist": persist, "caption": cap, "processing_time": round(6 + h(src, "pt") * 4, 2),
                    "video_shape": [2160, 3840, 3], "location": "nashville", "camera_id": "i24_cam-1"})
    index = {"version": 1, "source": "fixture", "camera_id": "i24_cam-1",
             "scenes": {str(s): {"label": m["label"], "duration": m["duration"],
                                 "cameras": [c for c in ALL_CAMS if c not in m["drop"]]} for s, m in SCENES.items()},
             "segments": segments}

    # Pre-run scene-wide jurors (P-COND, P-COUNT), as prerun_scene_probes.py would write them.
    probes = {"version": 1, "source": "fixture", "probe_versions": {"P-COND": "v1", "P-COUNT": "v1"},
              "ran_at": "2026-10-02T11:32:00-07:00", "scenes": {}}
    for scene, meta in SCENES.items():
        cams = [c for c in ALL_CAMS if c not in meta["drop"]]
        cond = truth["scene_conditions"][str(scene)]
        out = {}
        for cam in cams:
            r = h(scene, cam, "cond")
            ans = dict(cond)
            if r < 0.08:
                ans["road"] = "D"            # occasional "cannot tell"
            elif r < 0.12 and scene == 2:
                ans["road"] = "B"            # wet vs snow confusion
            if h(scene, cam, "traffic") < 0.1:
                ans["traffic"] = "B" if cond["traffic"] != "B" else "C"
            count_panels = [{"panel": p, "people_on_foot": 0, "bicycles": 0, "motorcycles": 0,
                             "visibility": "poor" if (scene == 2 and h(scene, cam, p) < 0.1) else "clear"}
                            for p in (1, 2, 3, 4)]
            out[cam] = {
                "P-COND": {"parsed": ans, "latency_ms": int(3000 + h(scene, cam, "lc") * 4000)},
                "P-COUNT": {"parsed": {"panels": count_panels}, "latency_ms": int(3000 + h(scene, cam, "lp") * 4000)},
                "grid_times": [round(meta["duration"] * f, 2) for f in (0.10, 0.35, 0.60, 0.85)],
            }
        probes["scenes"][str(scene)] = out

    CACHE.mkdir(exist_ok=True)
    (CACHE / "fixture_i24_index.json").write_text(json.dumps(index, indent=1))
    (CACHE / "fixture_scene_probes.json").write_text(json.dumps(probes, indent=1))
    (CACHE / "fixture_truth.json").write_text(json.dumps(truth, indent=1))
    n_tow = len(truth["towing"])
    print(f"segments={len(segments)} towing_segments={n_tow} "
          f"(S1={sum('scene1' in k for k in truth['towing'])}, S3={sum('scene3' in k for k in truth['towing'])})")


if __name__ == "__main__":
    build()
