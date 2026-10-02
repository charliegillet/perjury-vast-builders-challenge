"""Cosmos3-Reason jurors (§6): neutral probe on one 2x2 grid JPEG (image_url data URI) or a clip (video_url).

Refactored from src/verifier_backends.py CosmosNIMBackend: OpenAI-style chat body, <think> strip + JSON repair,
xyxy_to_box2d / box2d_to_pixels, COSMOS_BBOX_SCALE. Its build_prompt() is NOT reused (planted-assertion sycophancy
hazard): prompts come only from perjury/probes.py. temperature 0, max_tokens 512; enable_thinking=false behind
PERJURY_COSMOS_NO_THINK=1 (G5). Disk cache cache/cosmos/<image_sha>_<probe_version>_<prompt_sha>.json.
"""
from __future__ import annotations

import base64
import hashlib
import json
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

import httpx

from perjury.clients import HttpBase, ProbeResult, parse_model_json, ribbon
from perjury.config import CACHE, Settings
from perjury.obs import op

PROBE_TIMEOUT_S = 20.0


# ---- bbox helpers (verbatim semantics from src/verifier_backends.py) ----
def _clamp(v: float) -> int:
    return int(max(0, min(1000, round(v))))


def xyxy_to_box2d(b: list, scale: float = 1000.0) -> Optional[list[int]]:
    """Cosmos/Qwen3-VL bbox_2d [x1,y1,x2,y2] (0-scale) -> canonical [ymin,xmin,ymax,xmax] 0-1000."""
    if not b or len(b) != 4:
        return None
    x1, y1, x2, y2 = (float(v) * 1000.0 / scale for v in b)
    return [_clamp(min(y1, y2)), _clamp(min(x1, x2)), _clamp(max(y1, y2)), _clamp(max(x1, x2))]


def box2d_to_pixels(box: list[int], width: int, height: int) -> tuple[int, int, int, int]:
    """Canonical box_2d [ymin,xmin,ymax,xmax] 0-1000 -> pixel (x1, y1, x2, y2)."""
    ymin, xmin, ymax, xmax = box
    return (int(xmin / 1000 * width), int(ymin / 1000 * height), int(xmax / 1000 * width), int(ymax / 1000 * height))


def normalize_xyxy(b, scale: float = 1000.0) -> Optional[list[int]]:
    """Model bbox_2d [x1,y1,x2,y2] at `scale` -> ordered xyxy 0-1000 (the Vote.grounded convention)."""
    if not isinstance(b, (list, tuple)) or len(b) != 4:
        return None
    try:
        x1, y1, x2, y2 = (float(v) * 1000.0 / scale for v in b)
    except (TypeError, ValueError):
        return None
    out = [_clamp(min(x1, x2)), _clamp(min(y1, y2)), _clamp(max(x1, x2)), _clamp(max(y1, y2))]
    return out if out[2] > out[0] and out[3] > out[1] else None


def xyxy1000_to_pixels(b: list[int], width: int, height: int) -> tuple[int, int, int, int]:
    x1, y1, x2, y2 = b
    return (int(x1 / 1000 * width), int(y1 / 1000 * height), int(x2 / 1000 * width), int(y2 / 1000 * height))


def sha(b: bytes | str) -> str:
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode()).hexdigest()


def _hhmm(iso: str) -> Optional[str]:
    try:
        return datetime.fromisoformat(iso).strftime("%H:%M")
    except (TypeError, ValueError):
        return None


class ProbeCache:
    """(image_sha, probe_version, prompt_sha) -> {parsed, raw_text, latency_ms, ts, model}. Only successful parses are kept."""

    def __init__(self, root: Path | None = None):
        self.root = root or CACHE / "cosmos"

    def path(self, image_sha: str, probe_version: str, prompt_sha: str) -> Path:
        pv = re.sub(r"[^A-Za-z0-9._-]+", "-", probe_version)
        return self.root / f"{image_sha[:24]}_{pv}_{prompt_sha[:12]}.json"

    def get(self, image_sha: str, probe_version: str, prompt_sha: str) -> Optional[dict]:
        p = self.path(image_sha, probe_version, prompt_sha)
        try:
            return json.loads(p.read_text())
        except (OSError, ValueError):
            return None

    def put(self, image_sha: str, probe_version: str, prompt_sha: str, rec: dict) -> None:
        p = self.path(image_sha, probe_version, prompt_sha)
        try:
            p.parent.mkdir(parents=True, exist_ok=True)
            tmp = p.with_suffix(".tmp")
            tmp.write_text(json.dumps(rec))
            tmp.replace(p)
        except OSError:
            pass


class Cosmos(HttpBase):
    service = "cosmos3"

    def __init__(self, s: Settings, cache: ProbeCache | None = None):
        super().__init__(s, timeout=PROBE_TIMEOUT_S)
        self.model = s.cosmos_model
        self.bbox_scale = s.cosmos_bbox_scale
        self.no_think = s.env.get("PERJURY_COSMOS_NO_THINK", "0") == "1"
        self.cache = cache or ProbeCache()

    def body(self, media_part: dict, prompt: str) -> dict:
        b = {"model": self.model, "temperature": 0, "max_tokens": 512,
             "messages": [{"role": "user", "content": [media_part, {"type": "text", "text": prompt}]}]}
        if self.no_think:
            b["chat_template_kwargs"] = {"enable_thinking": False}
        return b

    @op("cosmos_probe")
    async def probe(self, image_jpeg: bytes, prompt: str, probe_version: str, *, timeout_s: float = PROBE_TIMEOUT_S,
                    bus=None, use_cache: bool = True) -> ProbeResult:
        """Never raises for service errors: ProbeResult.error is set and parsed is None (the juror abstains)."""
        part = {"type": "image_url",
                "image_url": {"url": "data:image/jpeg;base64," + base64.b64encode(image_jpeg).decode()}}
        return await self._run(sha(image_jpeg), part, prompt, probe_version, timeout_s, bus, use_cache)

    @op("cosmos_probe_video")
    async def probe_video(self, mp4: bytes, prompt: str, probe_version: str, *, timeout_s: float = PROBE_TIMEOUT_S,
                          bus=None, use_cache: bool = True) -> ProbeResult:
        part = {"type": "video_url", "video_url": {"url": "data:video/mp4;base64," + base64.b64encode(mp4).decode()}}
        return await self._run(sha(mp4), part, prompt, probe_version, timeout_s, bus, use_cache)

    async def _run(self, image_sha: str, part: dict, prompt: str, probe_version: str, timeout_s: float, bus,
                   use_cache: bool) -> ProbeResult:
        prompt_sha = sha(prompt)
        if use_cache and (hit := self.cache.get(image_sha, probe_version, prompt_sha)):
            if bus is not None:
                bus.service(self.service, "fallback", note=f"cached {probe_version} @{_hhmm(hit.get('ts')) or '?'}")
            return ProbeResult(parsed=hit.get("parsed"), raw_text=hit.get("raw_text", ""),
                               latency_ms=int(hit.get("latency_ms", 0)), cached=True, cached_at=_hhmm(hit.get("ts")),
                               image_sha=image_sha)
        if not self.s.cosmos_url:
            return ProbeResult(image_sha=image_sha, error="COSMOS3_REASON_URL not set")
        body = self.body(part, prompt)
        try:
            async with self.sem(self.s.cosmos_concurrency):
                with ribbon(bus, self.service, gpu=True,
                            request={"probe_version": probe_version, "model": self.model, "image_sha": image_sha[:12],
                                     "prompt": prompt[:300]}) as call:
                    call.note = probe_version
                    t0 = time.monotonic()
                    try:
                        r = await self.http().post(f"{self.s.cosmos_url}/v1/chat/completions", json=body,
                                                   headers=self.gpu_headers(), timeout=httpx.Timeout(timeout_s))
                        r.raise_for_status()
                    except Exception as e:
                        raise self.http_error(e) from e
                    latency = int((time.monotonic() - t0) * 1000)
                    raw = (r.json().get("choices") or [{}])[0].get("message", {}).get("content") or ""
                    call.response = {"raw_text": raw[:1500]}
        except Exception as e:
            return ProbeResult(image_sha=image_sha, error="timeout" if getattr(e, "timeout", False) else str(e)[:300])
        try:
            parsed = parse_model_json(raw)
        except ValueError as e:
            return ProbeResult(raw_text=raw, latency_ms=latency, image_sha=image_sha, error=f"invalid_json: {e}")
        if "bbox_2d" in parsed and self.bbox_scale != 1000:
            parsed["bbox_2d"] = normalize_xyxy(parsed.get("bbox_2d"), self.bbox_scale)
        ts = datetime.now().astimezone().isoformat(timespec="seconds")
        self.cache.put(image_sha, probe_version, prompt_sha, {"parsed": parsed, "raw_text": raw, "latency_ms": latency,
                                                              "ts": ts, "model": self.model,
                                                              "probe_version": probe_version})
        return ProbeResult(parsed=parsed, raw_text=raw, latency_ms=latency, image_sha=image_sha)
