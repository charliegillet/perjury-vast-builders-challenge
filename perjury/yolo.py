"""YOLO11 /v1/infer (zoom-check, §7) plus parsers for the pipeline's detection sidecars (T0 noise floor).

Sidecar shape (VSS videos/detections): {"video_shape":[h,w,(c)], "fps", "object_counts", "frames":[{"time_sec",
"detections":[{"label","bbox":[x1,y1,x2,y2],"conf"}]}]}. /v1/infer returns the same frames when include_frames=true.
"""
from __future__ import annotations

import base64
import json
import struct
from typing import Optional

from perjury.clients import HttpBase, ServiceError, ZoomResult, ribbon
from perjury.config import Settings
from perjury.obs import op

ZOOM_CLASSES = ("car", "truck")


def parse_counts(raw) -> dict[str, int]:
    if isinstance(raw, dict):
        return {str(k): int(v) for k, v in raw.items() if isinstance(v, (int, float))}
    if isinstance(raw, str) and raw.strip():
        try:
            return parse_counts(json.loads(raw))
        except json.JSONDecodeError:
            return {}
    return {}


def frames_of(sidecar: dict | None) -> list[dict]:
    return [f for f in ((sidecar or {}).get("frames") or []) if isinstance(f, dict)]


def labels_in(frame: dict, min_conf: float = 0.0) -> set[str]:
    return {d.get("label") for d in frame.get("detections") or []
            if d.get("label") and float(d.get("conf") or d.get("confidence") or 1.0) >= min_conf}


def persistence(sidecar: dict | None, min_conf: float = 0.0) -> dict[str, int]:
    """Max consecutive sidecar frames per class (Segment.persist; the noise floor is persist < 3)."""
    best: dict[str, int] = {}
    run: dict[str, int] = {}
    frames = sorted(frames_of(sidecar), key=lambda f: float(f.get("time_sec") or f.get("frame") or 0))
    for f in frames:
        here = labels_in(f, min_conf)
        for lab in here:
            run[lab] = run.get(lab, 0) + 1
            best[lab] = max(best.get(lab, 0), run[lab])
        for lab in list(run):
            if lab not in here:
                run[lab] = 0
    return best


def peak_counts(sidecar: dict | None) -> dict[str, int]:
    """Peak concurrent detections per class over the frames (pipeline object_counts semantics)."""
    peak: dict[str, int] = {}
    for f in frames_of(sidecar):
        n: dict[str, int] = {}
        for d in f.get("detections") or []:
            if d.get("label"):
                n[d["label"]] = n.get(d["label"], 0) + 1
        for k, v in n.items():
            peak[k] = max(peak.get(k, 0), v)
    return peak or parse_counts((sidecar or {}).get("object_counts"))


def mp4_dims(mp4: bytes | None) -> Optional[tuple[int, int]]:
    """(width, height) from the first video tkhd box (16.16 fixed point). None if not found."""
    if not mp4:
        return None
    i = 0
    while (i := mp4.find(b"tkhd", i)) >= 0:
        p = i + 4
        version = mp4[p] if p < len(mp4) else 0
        off = p + 4 + (32 if version == 1 else 20) + 8 + 8 + 36   # times/track/duration, reserved, layer..volume, matrix
        if off + 8 <= len(mp4):
            w, h = struct.unpack(">II", mp4[off:off + 8])
            if w >> 16 and h >> 16:
                return w >> 16, h >> 16
        i += 4
    return None


def frame_wh(resp: dict, hint: Optional[tuple[int, int]]) -> Optional[tuple[float, float]]:
    shape = resp.get("video_shape") or resp.get("shape")
    if isinstance(shape, (list, tuple)) and len(shape) >= 2 and shape[0] and shape[1]:
        return float(shape[1]), float(shape[0])
    if resp.get("width") and resp.get("height"):
        return float(resp["width"]), float(resp["height"])
    return (float(hint[0]), float(hint[1])) if hint else None


def box_cover(bbox, wh: Optional[tuple[float, float]]) -> float:
    if not isinstance(bbox, (list, tuple)) or len(bbox) < 4:
        return 0.0
    x1, y1, x2, y2 = map(float, bbox[:4])
    area = abs(x2 - x1) * abs(y2 - y1)
    if max(x1, y1, x2, y2) <= 1.5:   # already normalized
        return area
    return area / (wh[0] * wh[1]) if wh and wh[0] * wh[1] else 0.0


def zoom_from_response(resp: dict, *, min_cover: float = 0.30, min_frames: int = 2,
                       dims: Optional[tuple[int, int]] = None) -> ZoomResult:
    """ok iff a car/truck box covers >= min_cover of the crop on >= min(min_frames, n_frames) frames."""
    frames = frames_of(resp)
    if not frames:
        return ZoomResult(ok=False, error="no frames in YOLO response")
    wh = frame_wh(resp, dims)
    best: tuple[float, Optional[str], Optional[float]] = (0.0, None, None)
    frames_ok = 0
    for f in frames:
        hit = False
        for d in f.get("detections") or []:
            if d.get("label") not in ZOOM_CLASSES:
                continue
            cov = box_cover(d.get("bbox") or d.get("box") or d.get("xyxy"), wh)
            conf = d.get("conf", d.get("confidence"))
            if cov > best[0]:
                best = (cov, d.get("label"), float(conf) if conf is not None else None)
            hit = hit or cov >= min_cover
        frames_ok += hit
    need = min(min_frames, len(frames))
    return ZoomResult(ok=frames_ok >= need, label=best[1], conf=best[2], cover=round(best[0], 3), frames_ok=frames_ok)


class Yolo(HttpBase):
    service = "yolo"

    def __init__(self, s: Settings):
        super().__init__(s, timeout=60.0)

    @op("yolo_infer")
    async def infer(self, *, url: str | None = None, video_b64: str | None = None, bus=None) -> dict:
        """Raw /v1/infer response. With both set, tries `url` first, then `video_base64`."""
        if not self.s.yolo_url:
            raise ServiceError(self.service, "YOLO_URL not set")
        attempts = ([{"url": url}] if url else []) + ([{"video_base64": video_b64}] if video_b64 else [])
        if not attempts:
            raise ServiceError(self.service, "infer needs url or video_b64")
        last: Exception | None = None
        for a in attempts:
            field = next(iter(a))
            with_req = {field: a[field], "filename": "clip.mp4", "include_frames": True}
            try:
                with ribbon(bus, self.service, gpu=True, request=with_req) as call:
                    call.note = f"infer via {field}"
                    try:
                        r = await self.http().post(f"{self.s.yolo_url}/v1/infer", json=with_req,
                                                   headers=self.gpu_headers())
                        r.raise_for_status()
                        out = r.json()
                    except Exception as e:
                        raise self.http_error(e) from e
                    call.response = {k: out.get(k) for k in ("perception_ok", "object_classes", "object_counts",
                                                             "video_shape")} | {"frames": len(frames_of(out))}
                    return out
            except ServiceError as e:
                last = e
        raise last  # type: ignore[misc]

    @op("yolo_zoom_check")
    async def zoom_check(self, crop_mp4: bytes | None, crop_url: str | None, *, min_cover=0.30, bus=None) -> ZoomResult:
        b64 = base64.b64encode(crop_mp4).decode() if crop_mp4 else None
        try:
            resp = await self.infer(url=crop_url, video_b64=b64, bus=bus)
        except ServiceError as e:
            return ZoomResult(ok=False, error=str(e)[:300])
        return zoom_from_response(resp, min_cover=min_cover, dims=mp4_dims(crop_mp4))
