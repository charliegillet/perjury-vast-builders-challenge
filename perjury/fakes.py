"""Fixture-mode fakes (BUILD-CONTRACT "Fake behaviour"): zero network, zero credentials, deterministic.

This is the ONLY module allowed to read cache/fixture_truth.json. FakeMedia renders Pillow highway frames and embeds a
JSON tag (source, t, scene, camera, what was drawn) in the JPEG COM segment; FakeCosmos / FakeYolo read the tag back to
answer from the truth file. Every call sleeps fixture_latency x a realistic latency (0 => instant) and reports to the
ribbon with note "FIXTURE".
"""
from __future__ import annotations

import asyncio
import base64
import hashlib
import io
import json
import math
import random
import re
import time
from datetime import datetime
from functools import lru_cache
from typing import Any, Optional

from PIL import Image, ImageDraw

from perjury.clients import Clients, ProbeResult, ServiceError, ZoomResult, ribbon
from perjury.config import CACHE, Settings
from perjury.media import Media, font, grid2x2, to_jpeg

FIXTURE = "FIXTURE"
CROP_MAGIC = b"PERJURY-FIXTURE-CLIP\n"
TOW_TIMES = (0.6, 1.8, 3.0, 4.2)   # P-TOW panel times within a 5 s segment (perjury.probes.TOW_PANEL_TIMES)
_SRC_RE = re.compile(r"scene(\d)[_/-]?(p\d+c\d+)", re.I)


def h(*parts) -> float:
    """Deterministic pseudo-random in [0, 1) (same construction as tools/make_fixtures.py)."""
    d = hashlib.sha256("|".join(map(str, parts)).encode()).digest()
    return int.from_bytes(d[:8], "big") / 2**64


@lru_cache(maxsize=1)
def load_truth() -> dict:
    return json.loads((CACHE / "fixture_truth.json").read_text())


@lru_cache(maxsize=1)
def load_index() -> dict:
    return json.loads((CACHE / "fixture_i24_index.json").read_text())


@lru_cache(maxsize=1)
def _by_source() -> dict[str, dict]:
    return {s["source"]: s for s in load_index()["segments"]}


def scene_cam(source: str) -> tuple[int, str]:
    m = _SRC_RE.search(source or "")
    return (int(m.group(1)), m.group(2).lower()) if m else (0, "")


def tow_truth(source: str) -> Optional[dict]:
    return load_truth()["towing"].get(source)


def false_yes_panel(source: str) -> Optional[int]:
    """Cosmos hallucination on a non-towing grid: p=0.05 per juror (deterministic)."""
    if tow_truth(source) or h(source, "falseyes") >= 0.05:
        return None
    return 1 + int(h(source, "fyp") * 4)


def zoom_passes(source: str) -> bool:
    if tow_truth(source):
        return True
    return false_yes_panel(source) is not None and h(source, "zoom") < 0.5


def panel_of(t: float) -> int:
    return 1 + min(range(4), key=lambda i: abs(TOW_TIMES[i] - t))


# ---- JPEG COM tag ----
def read_tag(jpeg: bytes | None) -> Optional[dict]:
    if not jpeg:
        return None
    try:
        c = Image.open(io.BytesIO(jpeg)).info.get("comment")
        return json.loads(c) if c else None
    except Exception:
        return None


def read_clip(blob: bytes | None) -> Optional[dict]:
    if blob and blob.startswith(CROP_MAGIC):
        try:
            return json.loads(blob[len(CROP_MAGIC):])
        except ValueError:
            return None
    return None


async def _nap(s: Settings, ms: float) -> int:
    if s.fixture_latency > 0:
        await asyncio.sleep(s.fixture_latency * ms / 1000)
    return int(ms)


# ---- frame renderer ----
def _lane_x(f: float, y: float, W: int, H: int, hy: float) -> float:
    d = (y - hy) / (H - hy)
    left, right = W * (0.44 - 0.50 * d), W * (0.56 + 0.50 * d)
    return left + f * (right - left)


def render_frame(source: str, t: float, width: int = 1920, towing: bool = False) -> tuple[bytes, dict]:
    scene, cam = scene_cam(source)
    W, H = width, width * 9 // 16
    hy = 0.14 * H
    rnd = random.Random(f"{source}|{round(t, 2)}")
    im = Image.new("RGB", (W, H), (18, 22, 30))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, hy], fill=(34, 40, 52) if scene != 2 else (70, 74, 82))
    road = [(_lane_x(0, hy, W, H, hy), hy), (_lane_x(1, hy, W, H, hy), hy), (_lane_x(1, H, W, H, hy), H),
            (_lane_x(0, H, W, H, hy), H)]
    if scene == 2:   # snow-white shoulders and median
        d.rectangle([0, hy, W, H], fill=(196, 200, 206))
    d.polygon(road, fill=(46, 48, 54) if scene != 2 else (66, 68, 74))
    if scene == 2:
        d.polygon([(_lane_x(0.48, hy, W, H, hy), hy), (_lane_x(0.52, hy, W, H, hy), hy),
                   (_lane_x(0.52, H, W, H, hy), H), (_lane_x(0.48, H, W, H, hy), H)], fill=(205, 208, 214))
    for k in range(1, 8):  # lane markings
        dash = k != 4
        for y0 in range(int(hy), H, 40 if dash else 4):
            y1 = min(H, y0 + (22 if dash else 4))
            d.line([(_lane_x(k / 8, y0, W, H, hy), y0), (_lane_x(k / 8, y1, W, H, hy), y1)],
                   fill=(150, 150, 120) if dash else (200, 170, 60), width=max(1, W // 900))
    n = {1: 14, 2: 9, 3: 30}.get(scene, 12)
    speed = {1: 0.093, 2: 0.0377, 3: 0.0113}.get(scene, 0.071)
    vehicles = []
    for i in range(n):
        lane = int(h(source, "lane", i) * 8)
        toward = lane < 4
        d0 = h(source, "d0", i) if scene != 3 else (i % 8) / 8 + 0.02 * h(source, "j", i)
        dd = (d0 + (speed if toward else -speed) * t) % 1.0
        y = hy + (0.06 + 0.92 * dd) * (H - hy)
        s = 0.25 + 0.75 * dd
        lw = (_lane_x(1, y, W, H, hy) - _lane_x(0, y, W, H, hy)) / 8
        truck = h(source, "truck", i) < 0.18
        vw, vh = lw * 0.62, lw * (2.6 if truck else 1.1) * (0.6 + 0.4 * s)
        cx = _lane_x((lane + 0.5) / 8, y, W, H, hy)
        box = (cx - vw / 2, y - vh / 2, cx + vw / 2, y + vh / 2)
        col = (230, 230, 235) if truck else tuple(int(60 + 160 * h(source, "c", i, k)) for k in range(3))
        d.rectangle(box, fill=col, outline=(10, 10, 10))
        vehicles.append(box)
    rig = None
    if towing:
        lane = 1 + int(h(source, "riglane") * 3)
        dd = 0.35 + 0.35 * h(source, "rigd") + 0.02 * t
        y = hy + dd * (H - hy)
        lw = (_lane_x(1, y, W, H, hy) - _lane_x(0, y, W, H, hy)) / 8
        cx = _lane_x((lane + 0.5) / 8, y, W, H, hy)
        pw, ph = lw * 0.66, lw * 1.5
        tw, th = lw * 0.6, lw * 1.25
        pickup = (cx - pw / 2, y, cx + pw / 2, y + ph)
        trailer = (cx - tw / 2, y - th - lw * 0.18, cx + tw / 2, y - lw * 0.18)
        d.rectangle(pickup, fill=(170, 40, 36), outline=(10, 10, 10))
        d.rectangle([pickup[0] + pw * 0.1, y + ph * 0.45, pickup[2] - pw * 0.1, y + ph * 0.95], fill=(120, 26, 24))
        d.line([(cx, trailer[3]), (cx, pickup[1])], fill=(20, 20, 20), width=max(2, W // 640))
        d.rectangle(trailer, fill=(150, 150, 140), outline=(10, 10, 10))
        rig = (trailer[0], trailer[1], pickup[2], pickup[3])
    if scene == 2:  # snow speckle
        for _ in range(W * H // 1400):
            x, y = rnd.random() * W, rnd.random() * H
            d.point((x, y), fill=(235, 235, 240))
    f = font(max(14, W // 48))
    label = f"{FIXTURE} · scene{scene} {cam} t={t:.1f}s"
    d.rectangle([W - d.textlength(label, font=f) - 24, H - f.size - 20, W, H], fill=(0, 0, 0))
    d.text((W - d.textlength(label, font=f) - 12, H - f.size - 12), label, fill=(255, 196, 0), font=f)

    def norm(b):
        return [int(max(0, min(1000, b[0] / W * 1000))), int(max(0, min(1000, b[1] / H * 1000))),
                int(max(0, min(1000, b[2] / W * 1000))), int(max(0, min(1000, b[3] / H * 1000)))]
    veh = vehicles[int(h(source, "veh") * len(vehicles))] if vehicles else None
    tag = {"fx": 1, "source": source, "t": round(t, 3), "scene": scene, "camera": cam, "towing": bool(towing),
           "rig_box": norm(rig) if rig else None, "veh_box": norm(veh) if veh else None}
    return to_jpeg(im, quality=82, comment=json.dumps(tag).encode()), tag


class FakeMedia(Media):
    def __init__(self, s: Settings):
        super().__init__(s, vss=None)
        self._tiles: dict[tuple[int, str], bytes] = {}

    def presign(self, source: str, expires=3600) -> str:
        return f"fixture://{source}"

    def frame_has_rig(self, source: str, t: float) -> bool:
        tow = tow_truth(source)
        return bool(tow) and panel_of(t) in tow.get("panels", [])

    async def keyframe(self, source: str, t: float, width: int = 1920) -> bytes:
        return (await asyncio.to_thread(render_frame, source, t, width, self.frame_has_rig(source, t)))[0]

    async def keyframes(self, source: str, times: list[float], width: int = 1920, *, bus=None) -> list[bytes]:
        with ribbon(bus, self.service, request={"source": source, "times": times, "op": "fixture render"}) as c:
            await _nap(self.s, 60)
            frames = list(await asyncio.gather(*(self.keyframe(source, t, width) for t in times)))
            c.note, c.response = FIXTURE, {"frames": len(frames)}
            return frames

    def grid2x2(self, frames: list[bytes], labels: list[str] | None = None) -> bytes:
        tags = [read_tag(f) or {} for f in frames]
        first = next((t for t in tags if t.get("source")), {})
        tag = {"fx": 1, "grid": True, "source": first.get("source"), "scene": first.get("scene"),
               "camera": first.get("camera"), "times": [t.get("t") for t in tags],
               "panels": [{"panel": i + 1, "t": t.get("t"), "towing": bool(t.get("towing")),
                           "source": t.get("source")} for i, t in enumerate(tags)]}
        jpg = grid2x2(frames, labels)
        im = Image.open(io.BytesIO(jpg))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=88, comment=json.dumps(tag).encode())
        return buf.getvalue()

    async def crop_clip(self, source: str, t: float, box_px: tuple[int, int, int, int], dur: float = 0.5, *,
                        bus=None, pad: float = 0.10) -> bytes:
        with ribbon(bus, self.service, request={"source": source, "t": t, "box_px": list(box_px)}) as c:
            await _nap(self.s, 120)
            c.note = FIXTURE
            return CROP_MAGIC + json.dumps({"source": source, "t": t, "box_px": list(box_px), "dur": dur}).encode()

    async def small_clip(self, source: str, width: int = 640, dur: float = 5.0) -> bytes:
        return CROP_MAGIC + json.dumps({"source": source, "t": 0, "dur": dur}).encode()

    async def tile(self, scene: int, camera: str) -> bytes:
        key = (scene, camera)
        if key not in self._tiles:
            src = self.tile_source(scene, camera) or f"s3://fixture/scene{scene}_{camera}/seg_000.mp4"
            self._tiles[key] = render_frame(src, 1.0, 480)[0]
        return self._tiles[key]

    def _segments(self) -> list[dict]:
        return load_index()["segments"]


class FakeCosmos:
    service = "cosmos3"

    def __init__(self, s: Settings):
        self.s = s
        self.model = "fixture/cosmos3-reason"

    @staticmethod
    def _kind(probe_version: str, prompt: str) -> str:
        pv = (probe_version or "").upper()
        for k in ("P-TOW", "P-GROUND", "P-COND", "P-COUNT", "P-LEAD"):
            if pv.startswith(k):
                return k
        p = prompt or ""
        if "witness" in p.lower():
            return "P-LEAD"
        if "bbox_2d" in p:
            return "P-GROUND"
        if "trailer" in p.lower():
            return "P-TOW"
        if "people_on_foot" in p:
            return "P-COUNT"
        if '"road"' in p:
            return "P-COND"
        return "?"

    def answer(self, kind: str, tag: dict, prompt: str) -> Optional[dict]:
        src = tag.get("source") or ""
        scene = int(tag.get("scene") or scene_cam(src)[0] or 0)
        panels = tag.get("panels") or [{"panel": 1, "t": tag.get("t"), "towing": tag.get("towing"), "source": src}]
        if kind == "P-TOW":
            tow, fy = tow_truth(src), false_yes_panel(src)
            out = []
            for p in panels:
                towing = []
                if p.get("towing") and tow:
                    towing = [{"towing_vehicle": tow["towing_vehicle"], "trailer": tow["trailer"]}]
                elif fy == p["panel"]:
                    towing = [{"towing_vehicle": "pickup", "trailer": "unclear"}]
                vis = "partial" if scene == 2 and h(src, p["panel"], "vis") < 0.15 else "clear"
                out.append({"panel": p["panel"], "towing": towing, "semis": int(h(src, p["panel"], "semi") * 3),
                            "visibility": vis})
            return {"panels": out}
        if kind == "P-GROUND":
            if tag.get("rig_box"):
                return {"bbox_2d": tag["rig_box"]}
            return {"bbox_2d": tag.get("veh_box")}   # a plausible box (the hallucinated yes still gets one)
        if kind == "P-COND":
            cond = dict(load_truth()["scene_conditions"].get(str(scene)) or {"road": "D", "traffic": "D", "light": "D"})
            key = f"{src}|{tag.get('times')}"
            if h(key, "cond") < 0.06:
                cond["road"] = "D"
            if h(key, "traffic") < 0.06:
                cond["traffic"] = "D"
            return cond
        if kind == "P-COUNT":
            return {"panels": [{"panel": p["panel"], "people_on_foot": 0, "bicycles": 0, "motorcycles": 0,
                                "visibility": "partial" if scene == 2 and h(src, p["panel"], "cv") < 0.1 else "clear"}
                               for p in panels]}
        if kind == "P-LEAD":   # sycophancy: agrees with the witness 60% of the time regardless of the pixels
            return {"witness_correct": h(src, tag.get("times"), prompt, "lead") < 0.6}
        return None

    async def probe(self, image_jpeg: bytes, prompt: str, probe_version: str, *, timeout_s: float = 20.0,
                    bus=None, use_cache: bool = True) -> ProbeResult:
        image_sha = hashlib.sha256(image_jpeg).hexdigest()
        tag = read_tag(image_jpeg)
        kind = self._kind(probe_version, prompt)
        with ribbon(bus, self.service, gpu=True, request={"probe_version": probe_version, "image_sha": image_sha[:12],
                                                          "prompt": prompt[:300]}) as c:
            c.note = f"{probe_version} · {FIXTURE}"
            ms = 2500 + 3500 * h(image_sha, probe_version)
            if ms / 1000 * self.s.fixture_latency > timeout_s:
                await asyncio.sleep(timeout_s)
                return ProbeResult(image_sha=image_sha, error="timeout")
            ms = await _nap(self.s, ms)
            parsed = self.answer(kind, tag, prompt) if tag else None
            c.response = parsed
        if parsed is None:
            return ProbeResult(image_sha=image_sha, latency_ms=ms, raw_text="",
                               error="fixture: untagged image" if not tag else f"fixture: unknown probe {probe_version}")
        return ProbeResult(parsed=parsed, raw_text=json.dumps(parsed), latency_ms=ms, image_sha=image_sha)

    async def probe_video(self, mp4: bytes, prompt: str, probe_version: str, **kw) -> ProbeResult:
        return ProbeResult(image_sha=hashlib.sha256(mp4).hexdigest(), error="fixture: video probes not faked")


class FakeYolo:
    service = "yolo"

    def __init__(self, s: Settings):
        self.s = s

    def _clip(self, url: str | None, video_b64: str | None) -> Optional[dict]:
        if video_b64:
            try:
                return read_clip(base64.b64decode(video_b64))
            except ValueError:
                return None
        if url and url.startswith("fixture://"):
            return {"source": url[len("fixture://"):], "t": 0}
        return None

    def response(self, clip: Optional[dict]) -> dict:
        src = (clip or {}).get("source") or ""
        ok = zoom_passes(src) if clip and clip.get("box_px") else False
        frames = []
        for i in range(5):
            dets = []
            if ok:
                dets.append({"label": "truck", "bbox": [90, 70, 560, 610], "conf": round(0.62 + 0.05 * h(src, i), 2)})
            else:
                dets.append({"label": "car", "bbox": [260, 300, 380, 390], "conf": round(0.4 + 0.2 * h(src, i), 2)})
            frames.append({"time_sec": round(i * 0.1, 2), "detections": dets})
        return {"perception_ok": True, "object_classes": sorted({d["label"] for f in frames for d in f["detections"]}),
                "object_counts": {frames[0]["detections"][0]["label"]: 1}, "video_shape": [640, 640, 3],
                "frames": frames, "fixture": True}

    async def infer(self, *, url: str | None = None, video_b64: str | None = None, bus=None) -> dict:
        with ribbon(bus, self.service, gpu=True, request={"url": url, "video_base64": video_b64}) as c:
            await _nap(self.s, 400)
            out = self.response(self._clip(url, video_b64))
            c.note, c.response = FIXTURE, {"object_classes": out["object_classes"]}
            return out

    async def zoom_check(self, crop_mp4: bytes | None, crop_url: str | None, *, min_cover=0.30, bus=None) -> ZoomResult:
        clip = read_clip(crop_mp4) or self._clip(crop_url, None)
        if not clip:
            return ZoomResult(ok=False, error="fixture: unrecognised crop")
        with ribbon(bus, self.service, gpu=True, request={"crop": clip}) as c:
            await _nap(self.s, 400)
            ok = zoom_passes(clip.get("source") or "")
            res = ZoomResult(ok=ok, label="truck" if ok else "car", conf=0.66 if ok else 0.48,
                             cover=0.47 if ok else 0.06, frames_ok=4 if ok else 0)
            c.note, c.response = FIXTURE, res.model_dump()
            return res


# ---- text tiers ----
_T1_RULES = [  # (statement trigger, supports, contradicts); first matching trigger wins
    (r"snow|slush|wint", r"snow|slush|winter", r"\bdry\b|clear roadway"),
    (r"\bdry\b", r"\bdry\b", r"snow|slush|\bwet\b"),
    (r"\bwet\b|rain", r"\bwet\b|rain", r"\bdry\b"),
    (r"stop[- ]and[- ]go|standstill|queue|congest|jam|bumper",
     r"stop-and-go|queue|congest|bumper to bumper|barely moving|standstill|creeping",
     r"mov\w* freely|free-flowing|freely|at (?:highway )?speed"),
    (r"free|flow|speed", r"mov\w* freely|free-flowing|freely|at (?:highway )?speed",
     r"stop-and-go|queue|congest|bumper to bumper|barely moving|standstill|creeping"),
    (r"slow", r"\bslow", r"at (?:highway )?speed|freely"),
    (r"night|dark", r"\bnight|\bdark", r"daylight|daytime"),
    (r"\bday", r"daylight|daytime", r"\bnight"),
    (r"tow|trailer|pull|hitch", r"tow\w*|trailer|pulling", None),
    (r"pedestrian|person|people|walk", r"pedestrian|people|person|walking", None),
    (r"cycl|bicycl|bike", r"cyclist|bicycle", None),
    (r"motorcycl", r"motorcycl\w*", None),
    (r"\bbus", r"\bbus\b", None),
    (r"truck|semi", r"trucks?|semi", None),
    (r"\bcars?\b|sedan|vehicle", r"\bcars?\b|sedans?|vehicles", None),
]


def quote_around(text: str, m: re.Match, max_words: int = 12) -> str:
    """Exact substring of text: the clause holding the match, trimmed to <= max_words words around it."""
    a = max(text.rfind(c, 0, m.start()) for c in ".;,") + 1
    ends = [i for i in (text.find(c, m.end()) for c in ".;,") if i >= 0]
    b = min(ends) if ends else len(text)
    words = list(re.finditer(r"\S+", text[a:b]))
    if not words:
        return m.group(0)
    k = next((i for i, w in enumerate(words) if a + w.end() > m.start()), 0)
    lo = max(0, min(k - max_words // 2, len(words) - max_words))
    sel = words[lo:lo + max_words]
    return text[a + sel[0].start():a + sel[-1].end()]


def label_snippets(statement: str, snippets: list[dict]) -> list[dict]:
    rule = next((r for r in _T1_RULES if re.search(r[0], statement, re.I)), None)
    out = []
    for sn in snippets:
        text, lab, quote = str(sn.get("text") or ""), "SILENT", ""
        if rule:
            con = re.search(rule[2], text, re.I) if rule[2] else None
            sup = re.search(rule[1], text, re.I)
            if con:   # contradictions first
                lab, quote = "CONTRADICTS", quote_around(text, con)
            elif sup:
                lab, quote = "SUPPORTS", quote_around(text, sup)
        out.append({"id": sn.get("id"), "label": lab, "quote": quote})
    return out


def _json_array_after(text: str, marker: str) -> Optional[list]:
    i = text.find(marker)
    j = text.find("[", i if i >= 0 else 0)
    while j >= 0:
        try:
            v, _ = json.JSONDecoder().raw_decode(text[j:])
            if isinstance(v, list):
                return v
        except ValueError:
            pass
        j = text.find("[", j + 1)
    return None


class FakeLLM:
    service = "wandb_inference"

    def __init__(self, s: Settings):
        self.s = s
        self.model = "fixture/rules"

    async def complete_json(self, system: str, user: str, *, temperature=0.0, max_tokens=1200, bus=None,
                            purpose="") -> dict:
        both = f"{system}\n{user}"
        if "atom" in (purpose or "").lower() or "split ONE statement" in both:
            # The rules parser is the fixture atomizer: raising is the same path as a live 429 / bad JSON.
            raise ServiceError(self.service, "fixture: atomizer uses the rules parser")
        snippets = _json_array_after(both, "Snippets:")
        if snippets is None:
            return {}
        m = re.search(r'Statement:\s*"([^"]*)"', both)
        with ribbon(bus, self.service, request={"purpose": purpose or "t1", "user": user[:600]}) as c:
            await _nap(self.s, 600 + 600 * h(both))
            out = {"labels": label_snippets(m.group(1) if m else "", [x for x in snippets if isinstance(x, dict)])}
            c.note, c.response = f"{purpose or 't1'} · {FIXTURE}", out
            return out


class FakeEmbed:
    service = "embed1"
    _TOW = re.compile(r"trailer|tow", re.I)

    def __init__(self, s: Settings):
        self.s = s
        self._visual: Optional[dict[str, list[float]]] = None

    @staticmethod
    def _rand(seed: str) -> list[float]:
        r = random.Random(seed)
        return [r.gauss(0, 1) for _ in range(256)]

    @staticmethod
    def _unit(v: list[float]) -> list[float]:
        n = math.sqrt(sum(x * x for x in v)) or 1.0
        return [x / n for x in v]

    @classmethod
    def _mix(cls, a: list[float], wa: float, b: list[float], wb: float) -> list[float]:
        a, b = cls._unit(a), cls._unit(b)
        return cls._unit([wa * x + wb * y for x, y in zip(a, b)])

    async def embed_text(self, text: str, *, bus=None) -> list[float]:
        with ribbon(bus, self.service, gpu=True, request={"input": text, "request_type": "query"}) as c:
            await _nap(self.s, 150)
            noise = self._rand(f"text|{text}")
            v = self._mix(self._rand("concept|towing"), 0.85, noise, 0.15) if self._TOW.search(text) else self._unit(noise)
            c.note, c.response = FIXTURE, {"dim": len(v)}
            return v

    def visual_vectors(self) -> dict[str, list[float]] | None:
        if self._visual is None:
            tow = self._rand("concept|towing")
            out = {}
            for seg in load_index()["segments"]:
                src = seg["source"]
                w = 0.8 if tow_truth(src) else 0.08 * h(src, "vis")
                out[src] = self._mix(tow, w, self._rand(f"vis|{src}"), 1 - w)
            self._visual = out
        return self._visual


class FakeCanary:
    service = "canary"
    DEFAULT = "A pickup is towing a trailer."
    MARK = b"X-Fixture-Transcript:"

    def __init__(self, s: Settings):
        self.s = s

    async def health(self) -> bool:
        return True

    async def transcribe(self, wav: bytes, *, bus=None) -> dict:
        """Text after an 'X-Fixture-Transcript:' marker inside the upload (e.g. a WAV LIST chunk), else DEFAULT."""
        with ribbon(bus, self.service, gpu=True, request={"file": wav}) as c:
            ms = await _nap(self.s, 800)
            text = self.s.env.get("PERJURY_FIXTURE_TRANSCRIPT") or self.DEFAULT
            i = wav.find(self.MARK) if wav else -1
            if i >= 0:
                raw = wav[i + len(self.MARK):].split(b"\n", 1)[0].split(b"\x00", 1)[0]
                text = raw.decode("utf-8", "replace").strip() or text
            out = {"text": text, "model_id": "fixture/canary-1b", "latency_ms": ms}
            c.note, c.response = FIXTURE, out
            return out


_SYNTH = {
    1: ["The video shows a multi-lane highway from a high fixed camera.",
        "Traffic moves freely at highway speed on a dry road in daylight.",
        "Cars and trucks pass in both directions."],
    2: ["Snow lines the shoulders and median of the highway.",
        "Traffic moves slowly in overcast daylight.",
        "Cars and a few trucks proceed with headlights on."],
    3: ["Dense stop-and-go traffic fills the highway.",
        "Vehicles queue bumper to bumper in daylight on dry pavement.",
        "A semi-truck occludes cars in the far lanes."],
}
_HALLUCINATIONS = {
    1: ["A pedestrian walks along the right shoulder.", "Traffic comes to a standstill near the end of the clip.",
        "The road is covered in snow."],
    2: ["A cyclist rides along the snowy shoulder.", "A pickup truck is towing a trailer through the snow.",
        "It is nighttime and the road is dark."],
    3: ["Traffic flows freely at speed.", "Two pedestrians cross between the stopped cars.",
        "The road is covered in snow."],
}


class FakeVSS:
    service = "vss"

    def __init__(self, s: Settings):
        self.s = s
        self.token = None

    def _segs(self, original_video: str) -> list[dict]:
        return sorted((x for x in load_index()["segments"] if x["original_video"] == original_video),
                      key=lambda x: x["seg"])

    async def detections(self, source) -> dict | None:
        seg = _by_source().get(source)
        if not seg:
            return None
        H, W = (seg.get("video_shape") or [2160, 3840])[:2]
        frames = []
        counts = seg.get("object_counts") or {}
        persist = seg.get("persist") or {}
        for i in range(50):
            dets = []
            for lab, n in counts.items():
                if lab == "person" and i >= persist.get("person", 0):
                    continue
                for k in range(min(int(n), 6)):
                    x, y = h(source, lab, k, "x") * (W - 200), h(source, lab, k, "y") * (H - 200) + i * 4 % 100
                    dets.append({"label": lab, "bbox": [round(x), round(y), round(x + 160), round(y + 120)],
                                 "conf": round(0.5 + 0.4 * h(source, lab, k, i), 2)})
            frames.append({"time_sec": round(i * 0.1, 2), "detections": dets})
        return {"segment_source": source, "video_shape": seg.get("video_shape"), "fps": 10,
                "object_counts": counts, "frames": frames, "fixture": True}

    def stream_url(self, source) -> str:
        return ""   # no playback in fixture mode; the UI shows the rendered tile instead

    async def playback_url(self, source: str, expires: int = 3600) -> str:
        return ""

    async def search_and_answer(self, claim: str, camera_id: str, *, bus=None) -> dict:
        from perjury.vss import STOCK_PROMPT, classify_stock
        body = {"query": STOCK_PROMPT.format(claim=claim), "metadata_filters": {"camera_id": camera_id},
                "top_k": 10, "min_similarity": 0.1}
        with ribbon(bus, self.service, request=body) as c:
            ms = await _nap(self.s, 2200 + 1500 * h(claim, "stock"))
            r = h(claim, "stock-verdict")
            if r < 0.78:
                answer = "TRUE. The retrieved highway segments are consistent with the statement."
            elif r < 0.9:
                answer = "CANNOT TELL. The retrieved captions do not mention this."
            else:
                answer = "FALSE. The retrieved captions describe something different."
            out = {"answer": answer, "classification": classify_stock(answer), "hits": 10, "latency_ms": ms,
                   "query": body["query"], "evidence": [], "fixture": True}
            c.note, c.response = f"stock A/B · {FIXTURE}", {"answer": answer, "classification": out["classification"]}
            return out

    async def ask(self, question, original_video=None, *, bus=None) -> dict:
        with ribbon(bus, self.service, request={"question": question, "original_video": original_video}) as c:
            await _nap(self.s, 1800)
            scene = scene_cam(original_video or "")[0] or 1
            out = {"answer": " ".join(_SYNTH[scene][:2]), "tool_used": "video_segments" if original_video else
                   "search_hybrid", "evidence": [], "fixture": True}
            c.note, c.response = FIXTURE, {"answer": out["answer"]}
            return out

    async def synthesize(self, original_video, question="Summarize what happens in this video", max_segments=20, *,
                         bus=None) -> dict:
        with ribbon(bus, self.service, request={"original_video": original_video, "question": question}) as c:
            await _nap(self.s, 3000)
            segs = self._segs(original_video)
            scene = scene_cam(original_video)[0] or 1
            lines = list(_SYNTH[scene])
            if any(tow_truth(x["source"]) for x in segs):
                lines.append("A pickup truck towing a small trailer travels in the middle lanes." if scene == 1 else
                             "An SUV pulling an enclosed trailer waits in the queue.")
            hall = _HALLUCINATIONS[scene]
            lines.append(hall[int(h(original_video, "hall") * len(hall))])
            answer = ("## Overview\n" + " ".join(lines[:2]) + "\n\n## Timeline\n" +
                      "\n".join(f"- 0:{5 * i:02d}–0:{5 * i + 5:02d}: {ln}" for i, ln in enumerate(lines[2:])))
            out = {"answer": answer, "llm_synthesis": answer, "segment_count": len(segs),
                   "segments_used": min(len(segs), max_segments), "generated_at": datetime.now().isoformat(),
                   "fixture": True}
            c.note, c.response = FIXTURE, {"segment_count": len(segs)}
            return out

    async def suggestions(self, *, bus=None) -> list[dict]:
        return [{"kind": "prompts", "text": "trucks in the right lane"},
                {"kind": "prompts", "text": "snow on the shoulder"},
                {"kind": "key_events", "text": "Stop-and-go queue forms on the westbound lanes", "fixture": True}]

    async def dashboard_stats(self, *, bus=None) -> dict:
        segs = load_index()["segments"]
        return {"overview": {"total_rows": len(segs), "segment_rows": len(segs),
                             "unique_videos": len({x["original_video"] for x in segs}),
                             "indexed_clips": len(segs)}, "fixture": True}

    async def upload(self, mp4: bytes, filename: str, metadata: dict, *, bus=None) -> dict:
        with ribbon(bus, "dataengine", request={"filename": filename, "bytes": len(mp4), **(metadata or {})}) as c:
            await _nap(self.s, 500)
            out = {"success": True, "object_key": f"fixture/{int(time.time())}_{filename}",
                   "message": "FIXTURE: not uploaded", "fixture": True}
            c.note, c.response = FIXTURE, out
            return out

    async def segments(self, original_video) -> list[dict]:
        from perjury.vss import normalize
        return [normalize({"source": x["source"], "start_sec": x["start"], "end_sec": x["end"],
                           "reasoning_content": x["caption"], "camera_id": x["camera_id"], "location": x["location"],
                           "object_classes": x["object_classes"], "object_counts": x["object_counts"],
                           "processing_time": x["processing_time"]},
                          original_video) for x in self._segs(original_video)]

    async def explore(self, limit=48, offset=0) -> dict:
        parents: dict[str, dict] = {}
        for x in load_index()["segments"]:
            p = parents.setdefault(x["original_video"], {"original_video": x["original_video"],
                                                         "camera_id": x["camera_id"], "location": x["location"],
                                                         "segment_count": 0})
            p["segment_count"] += 1
        rows = sorted(parents.values(), key=lambda r: r["original_video"])
        return {"videos": rows[offset:offset + limit], "total": len(rows), "fixture": True}


def build_fakes(s: Settings) -> Clients:
    return Clients(llm=FakeLLM(s), cosmos=FakeCosmos(s), embed=FakeEmbed(s), yolo=FakeYolo(s),  # type: ignore[arg-type]
                   canary=FakeCanary(s), vss=FakeVSS(s), media=FakeMedia(s), mode="fixture")  # type: ignore[arg-type]
