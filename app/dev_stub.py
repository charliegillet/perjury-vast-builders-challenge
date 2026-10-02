"""DEV ONLY: a scripted stand-in for perjury.pipeline so the UI can be checked before the pipeline exists.

Active only with PERJURY_DEV_STUB=1 *and* when `perjury.pipeline.load_context` fails; /health then reports
`dev_stub: true` and the UI shows a DEV STUB banner. It never runs in live mode by accident and never reads
cache/fixture_truth.json: verdicts below are hand-written for the §14 demo sentences, over fixture_i24_index.json.
"""
from __future__ import annotations

import asyncio
import io
import json
import random
import re
from types import SimpleNamespace
from typing import Any

from perjury.config import Settings

LAT = 1.0


def _render(scene: int, camera: str, w: int, label: str) -> bytes:
    from PIL import Image, ImageDraw  # noqa: WPS433
    h = w * 9 // 16
    rnd = random.Random(f"{scene}{camera}{label}")
    sky = {1: (54, 62, 74), 2: (150, 156, 166), 3: (60, 64, 70)}[scene]
    im = Image.new("RGB", (w, h), sky)
    d = ImageDraw.Draw(im)
    road = (40, 42, 48) if scene != 2 else (92, 96, 104)
    d.polygon([(0, h), (w, h), (w * 0.62, h * 0.22), (w * 0.38, h * 0.22)], fill=road)
    for i in range(1, 6):
        x0 = w * (i / 6)
        d.line([(x0, h), (w * 0.38 + (w * 0.24) * i / 6, h * 0.22)], fill=(200, 200, 160), width=max(1, w // 400))
    for _ in range(18 if scene != 3 else 40):
        y = rnd.uniform(h * 0.3, h * 0.95)
        s = (y / h) * w * 0.05
        x = rnd.uniform(w * 0.5 - (y / h) * w * 0.45, w * 0.5 + (y / h) * w * 0.4)
        col = rnd.choice([(220, 220, 225), (180, 30, 40), (30, 60, 140), (20, 20, 20), (230, 200, 60)])
        d.rectangle([x, y, x + s, y + s * 0.6], fill=col)
    if scene == 2:
        for _ in range(w * 2):
            x, y = rnd.uniform(0, w), rnd.uniform(0, h)
            d.point((x, y), fill=(240, 240, 245))
    d.text((8, 6), f"DEV STUB · scene{scene} {camera} {label}", fill=(255, 255, 255))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=82)
    return buf.getvalue()


class _Media:
    def __init__(self, index: dict):
        self.index = index

    async def tile(self, scene: int, camera: str) -> bytes:
        await asyncio.sleep(0.01)
        return _render(scene, camera, 480, "")

    async def keyframes(self, source: str, times: list[float], width: int = 1920) -> list[bytes]:
        m = re.search(r"scene(\d)_(p\dc\d)", source or "")
        scene, cam = (int(m.group(1)), m.group(2)) if m else (1, "p1c1")
        return [_render(scene, cam, width, f"t={t:.1f}s") for t in times]


class _Canary:
    fixture_transcript = None

    async def transcribe(self, wav: bytes, *, bus=None) -> dict:
        await asyncio.sleep(0.8 * LAT)
        text, self.fixture_transcript = self.fixture_transcript or "A pickup is towing a trailer.", None
        return {"text": text, "model_id": "dev-stub", "latency_ms": 800}


class _VSS:
    def stream_url(self, source: str) -> str:
        return ""


class _Index:
    def __init__(self, raw: dict):
        self.raw = raw

    def scene_parent(self, scene: int, camera: str) -> str | None:
        return next((g["original_video"] for g in self.raw["segments"]
                     if g["scene"] == scene and g["camera"] == camera), None)


def load_context(s: Settings) -> Any:
    global LAT
    LAT = s.fixture_latency
    raw = json.loads(s.index_path.read_text()) if s.index_path.exists() else {"scenes": {}, "segments": []}
    probes = json.loads(s.probes_path.read_text()) if s.probes_path.exists() else {"scenes": {}}
    clients = SimpleNamespace(media=_Media(raw), canary=_Canary(), vss=_VSS())
    return SimpleNamespace(settings=s, clients=clients, index=_Index(raw), probes=probes, raw=raw)


# ------------------------------------------------------------------ scripted run

def _atoms(text: str) -> list[dict]:
    atoms: list[dict] = []
    low = text.lower()

    def add(pattern: str, **kw) -> dict | None:
        m = re.search(pattern, low)
        if not m:
            return None
        a = {"id": f"a{len(atoms) + 1}", "span": text[m.start():m.end()], "negated": False, **kw}
        atoms.append(a)
        return a

    tow = add(r"(a |an )?(pickup|suv|van|car|vehicle)[\w\s]{0,12}(towing|pulling) a (trailer|camper)",
              type="towing", towing_vehicle="pickup")
    person = add(r"pedestrians?|people|cyclists?", type="coco_presence", cls="person")
    if person:
        add(r"\b(three|two|four|five)\b", type="count", count=3, count_op="exact", cls="person",
            depends_on=person["id"])
        add(r"crossing|walking", type="action", value="crossing", depends_on=person["id"])
    add(r"highway", type="scene_identity", value="highway")
    add(r"snow\w*", type="road_surface", value="snow")
    add(r"stop-and-go|standstill|flowing freely", type="traffic_state", value="stop_and_go")
    if not tow:
        add(r"braked hard|changed lanes?|sped up", type="action", value="braking")
    if not atoms:
        atoms.append({"id": "a1", "span": text.rstrip("."), "type": "other", "negated": False})
    return atoms


def _juror(cam: str, scene: int, seg: int, rank: int) -> dict:
    return {"camera": cam, "source": f"s3://vss-chunks-segments/i24/scene{scene}_{cam}/seg_{seg:03d}.mp4",
            "seg": seg, "times": [0.6, 1.8, 3.0, 4.2], "rank": rank, "retrieval_score": round(0.41 - rank * 0.03, 3)}


async def testify(text: str, scene: int, ctx: Any, bus: Any, *, transcript_source: str = "typed",
                  stock_ab: bool = False, jury_size: int | None = None, probe_overrides: dict | None = None):
    sl = lambda s: asyncio.sleep(s * LAT)  # noqa: E731
    cams = ctx.raw["scenes"].get(str(scene), {}).get("cameras", [])
    nseg = sum(1 for g in ctx.raw["segments"] if g["scene"] == scene)
    bus.emit("run", {"run_id": bus.run_id, "text": text, "scene": scene, "mode": "fixture"})
    bus.emit("transcript", {"text": text, "source": transcript_source, "latency_ms": 0})
    bus.service("wandb_inference", "firing", note="atomize")
    await sl(0.9)
    atoms = _atoms(text)
    bus.service("wandb_inference", "done", ms=900, note="atomize",
                request={"model": "nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B", "statement": text},
                response={"atoms": atoms})
    bus.emit("atoms", {"atoms": atoms, "parser": "rules"})
    bus.service("vastdb", "firing", note="T0 pushdown")
    await sl(0.3)
    bus.service("vastdb", "done", ms=280, note="T0 pushdown camera_id='i24_cam-1'",
                request={"table": "vss-collection", "filter": "camera_id = 'i24_cam-1'",
                         "columns": ["object_classes", "object_counts", "location"]},
                response={"rows": nseg})
    bus.service("yolo", "done", ms=0, note="pipeline output: object_classes", response={"segments": nseg})
    verdicts: dict[str, dict] = {}
    av = lambda a, v, reason, code, tiers, votes=(), stats=None: {  # noqa: E731
        "atom_id": a["id"], "verdict": v, "reason": reason, "reason_code": code, "tiers": tiers,
        "votes": list(votes), "stats": stats or {}}

    async def jury_cond(a: dict, want: str) -> dict:
        jurors = [{"camera": c} for c in cams]
        bus.emit("summon", {"atom_id": a["id"], "probe": "P-COND", "probe_version": "P-COND v1 (pre-run)",
                            "jurors": jurors})
        votes = []
        for c in cams:
            await sl(0.05)
            p = ctx.probes["scenes"].get(str(scene), {}).get(c, {}).get("P-COND", {}).get("parsed") or {}
            ok = p.get("road") == want
            v = {"camera": c, "vote": "yes" if ok else "no", "tier": "JURY", "probe": "P-COND",
                 "probe_version": "P-COND v1", "raw": p, "latency_ms": 4100, "cached": True,
                 "cached_at": "2026-10-02T11:32:00", "juror": {"camera": c}}
            votes.append(v)
            bus.emit("juror", {"atom_id": a["id"], "vote": v})
        y = sum(v["vote"] == "yes" for v in votes)
        return {"votes": votes, "Y": y, "N": len(votes) - y, "k": len(votes), "k_valid": len(votes)}

    for a in atoms:
        t = a["type"]
        if t == "coco_presence":
            bus.emit("t0", {"atom_id": a["id"], "summary": f"YOLO: person in 0 of {nseg} segments",
                            "data": {"hits": 0, "total": nseg, "per_camera": {c: 0 for c in cams}}})
            await sl(0.4)
            bus.emit("t1", {"atom_id": a["id"], "supports": 0, "contradicts": 3, "silent": 21, "snippets": []})
            bus.emit("summon", {"atom_id": a["id"], "probe": "P-COUNT", "probe_version": "P-COUNT v1 (pre-run)",
                                "jurors": [{"camera": c} for c in cams]})
            votes = []
            for c in cams:
                await sl(0.06)
                v = {"camera": c, "vote": "no", "tier": "JURY", "probe": "P-COUNT", "probe_version": "P-COUNT v1",
                     "raw": {"panels": [{"panel": i, "people_on_foot": 0, "visibility": "clear"} for i in (1, 2, 3, 4)]},
                     "latency_ms": 3900, "cached": True, "cached_at": "2026-10-02T11:32:00", "juror": {"camera": c}}
                votes.append(v)
                bus.emit("juror", {"atom_id": a["id"], "vote": v})
            verdicts[a["id"]] = av(a, "CONTRADICTED", f"No person was detected in any of {nseg} segments; "
                                   f"{len(cams)}/{len(cams)} cameras count 0", "absence", ["RECORDS", "JURY"], votes,
                                   {"Y": 0, "N": len(cams), "k": len(cams), "k_valid": len(cams)})
        elif t == "scene_identity":
            bus.emit("t0", {"atom_id": a["id"], "summary": "metadata: I-24 MOTION, Nashville interstate",
                            "data": {"location": "nashville"}})
            verdicts[a["id"]] = av(a, "SUPPORTED", "Camera metadata: interstate I-24 (Nashville)", "metadata",
                                   ["RECORDS"])
        elif t in ("road_surface", "traffic_state"):
            bus.emit("t1", {"atom_id": a["id"], "supports": 14 if scene == 2 else 0,
                            "contradicts": 0 if scene == 2 else 9, "silent": 6, "snippets": []})
            st = await jury_cond(a, "C")
            ok = st["Y"] * 3 >= 2 * st["k"]
            verdicts[a["id"]] = av(a, "SUPPORTED" if ok else "CONTRADICTED",
                                   f"{st['Y'] if ok else st['N']}/{st['k']} cameras agree", "majority",
                                   ["CAPTIONS", "JURY"], st.pop("votes"), st)
        elif t == "towing":
            bus.emit("t1", {"atom_id": a["id"], "supports": 0, "contradicts": 0, "silent": 24, "snippets": []})
            bus.service("embed1", "firing", note="query embedding")
            await sl(0.15)
            bus.service("embed1", "done", ms=150, gpu=True, note="query embedding",
                        request={"input": "a vehicle pulling a trailer", "request_type": "query"},
                        response={"dims": 256})
            jur = [_juror(c, scene, 3 + i, i) for i, c in enumerate(cams[: (jury_size or 6)])]
            bus.emit("summon", {"atom_id": a["id"], "probe": "P-TOW", "probe_version": "P-TOW v1", "jurors": jur})
            bus.service("s3", "done", ms=40, note="presigned GET ×6")
            for _ in jur:
                bus.service("cosmos3", "firing", note="P-TOW v1")
            votes = []

            async def one(j: dict, i: int) -> None:
                ms = 2500 + (i * 731) % 3000
                await sl(ms / 1000)
                yes = scene != 2 and i in (0, 2, 3)
                v = {"camera": j["camera"], "vote": "yes" if yes else "no", "tier": "JURY", "probe": "P-TOW",
                     "probe_version": "P-TOW v1", "yes_panels": [2, 3] if yes else [], "latency_ms": ms,
                     "raw": {"panels": [{"panel": p, "towing": ([{"towing_vehicle": "pickup", "trailer": "utility"}]
                                                                if yes and p in (2, 3) else []),
                                         "semis": 1, "visibility": "clear"} for p in (1, 2, 3, 4)]},
                     "image_sha": f"{i:04x}deadbeef", "juror": j}
                bus.service("cosmos3", "done", ms=ms, gpu=True, note=f"P-TOW {j['camera']}",
                            request={"model": "nvidia/cosmos3-reason", "image_url": "data:image/jpeg;base64,…",
                                     "probe_version": "P-TOW v1"}, response=v["raw"])
                bus.emit("juror", {"atom_id": a["id"], "vote": v})
                if yes:
                    bus.service("cosmos3", "firing", note="P-GROUND")
                    await sl(1.2)
                    box = [380 + i * 20, 420, 560 + i * 20, 560]
                    bus.service("cosmos3", "done", ms=1200, gpu=True, note=f"P-GROUND {j['camera']}",
                                response={"bbox_2d": box})
                    bus.emit("ground", {"atom_id": a["id"], "camera": j["camera"], "panel": 2, "bbox_2d": box})
                    bus.service("yolo", "firing", note="zoom-check")
                    await sl(0.4)
                    bus.service("yolo", "done", ms=400, gpu=True, note=f"zoom-check {j['camera']}",
                                response={"label": "truck", "conf": 0.87})
                    bus.emit("zoom", {"atom_id": a["id"], "camera": j["camera"], "ok": True, "label": "truck",
                                      "conf": 0.87, "crop_box": [box[0] - 40, box[1] - 40, box[2] + 40, box[3] + 40]})
                    v["zoom_ok"], v["grounded"] = True, box
                votes.append(v)

            await asyncio.gather(*[one(j, i) for i, j in enumerate(jur)])
            y = sum(v["vote"] == "yes" for v in votes)
            ok = y >= 3
            verdicts[a["id"]] = av(
                a, "SUPPORTED" if ok else "CONTRADICTED",
                f"{y}/{len(votes)} jurors saw it, each boxed and zoom-checked" if ok else
                f"0/{len(votes)} of the most trailer-like moments show one; 0 of {nseg} captions mention one",
                "presence" if ok else "hardest_exhibit_absence", ["JURY"], votes,
                {"Y": y, "N": len(votes) - y, "k": len(votes), "k_valid": len(votes), "m": 3, "alpha": 0.1})
    for a in atoms:
        if a["id"] in verdicts:
            continue
        parent = verdicts.get(a.get("depends_on") or "")
        if parent and parent["verdict"] == "CONTRADICTED":
            verdicts[a["id"]] = av(a, "MOOT", "depends on a contradicted claim", "moot", [])
        elif a["type"] == "action":
            verdicts[a["id"]] = av(a, "UNVERIFIABLE", "temporal claims are not graded: localization tops out near "
                                   "52 mIoU on fixed cameras", "temporal", [])
        else:
            verdicts[a["id"]] = av(a, "UNVERIFIABLE", "not observable from these pixels", "not_observable", [])
    for a in atoms:
        await sl(0.15)
        bus.emit("atom_verdict", {"atom_verdict": verdicts[a["id"]]})
    labels = [v["verdict"] for v in verdicts.values()]
    if "CONTRADICTED" in labels:
        verdict = "FALSE"
        bad = next(v for v in verdicts.values() if v["verdict"] == "CONTRADICTED")
        expl = bad["reason"]
    elif all(x in ("SUPPORTED", "MOOT") for x in labels):
        verdict, expl = "TRUE", "; ".join(v["reason"] for v in verdicts.values())
    else:
        k = labels.count("SUPPORTED")
        verdict, expl = "UNPROVEN", f"supported as far as the pixels go: {k} of {len(labels)} atoms"
    bus.emit("verdict", {"verdict": verdict, "explanation": expl})
    if stock_ab:
        bus.service("vss", "firing", note="agent/search-and-answer")
        await sl(2.0)
        bus.service("vss", "done", ms=2000, note="agent/search-and-answer",
                    request={"query": f"Is this statement about the footage true: '{text}'? ..."},
                    response={"answer": "TRUE. Several clips show vehicles on the highway consistent with the description."})
        bus.emit("stock", {"answer": "TRUE. Several clips show vehicles on the highway consistent with the "
                                     "description.", "classification": "TRUE", "hits": 15, "latency_ms": 2000})
    elapsed = int(bus.events[-1]["t_ms"])
    bus.emit("receipt", {"verdict": verdict, "atoms": len(atoms), "fired": bus.fired_live(),
                         "fired_count": len(bus.fired_live()), "total": 13, "calls": bus.calls,
                         "elapsed_ms": elapsed, "gpu_s": round(bus.gpu_ms / 1000, 1), "weave_url": None,
                         "mode": "fixture"})
    bus.emit("done", {})
    return None
