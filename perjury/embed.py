"""Cosmos-Embed1 (256-d): text query embedding + segment visual vectors for T2 retrieval (§5a #6).

visual_vectors() reads cache/embed_visual.json ({source: [256 floats]}) or cache/embed_visual.npy + embed_visual_index.json
(row i <-> source i). When VastDB vectors_visual can't be selected, build them offline:
    python -m perjury.embed --segments [--limit N]     # embeds every index segment as a 640 px clip (data URI)
"""
from __future__ import annotations

import argparse
import asyncio
import base64
import json
import math
import sys
from typing import Optional

from perjury.clients import HttpBase, ServiceError, ribbon
from perjury.config import CACHE, Settings
from perjury.obs import op

DIM = 256
VISUAL_JSON = CACHE / "embed_visual.json"
VISUAL_NPY = CACHE / "embed_visual.npy"
VISUAL_IDX = CACHE / "embed_visual_index.json"


def cosine(a: list[float], b: list[float]) -> float:
    num = sum(x * y for x, y in zip(a, b))
    da, db = math.sqrt(sum(x * x for x in a)), math.sqrt(sum(y * y for y in b))
    return num / (da * db) if da and db else 0.0


def load_visual_vectors() -> Optional[dict[str, list[float]]]:
    try:
        if VISUAL_JSON.exists():
            d = json.loads(VISUAL_JSON.read_text())
            return {k: list(map(float, v)) for k, v in d.items()} or None
        if VISUAL_NPY.exists() and VISUAL_IDX.exists():
            import numpy as np
            arr = np.load(VISUAL_NPY)
            idx = json.loads(VISUAL_IDX.read_text())
            return {src: arr[i].astype(float).tolist() for i, src in enumerate(idx)} or None
    except (OSError, ValueError):
        return None
    return None


class Embed(HttpBase):
    service = "embed1"

    def __init__(self, s: Settings):
        super().__init__(s, timeout=30.0)
        self.model = s.embed_model
        self._visual: Optional[dict[str, list[float]]] = None
        self._visual_loaded = False

    async def _model(self) -> str:
        if not self.model:
            r = await self.http().get(f"{self.s.embed_url}/v1/models", headers=self.gpu_headers())
            r.raise_for_status()
            self.model = r.json()["data"][0]["id"]
        return self.model

    async def _embed(self, inp: str, bus, what: str) -> list[float]:
        if not self.s.embed_url:
            raise ServiceError(self.service, "COSMOS_EMBED1_URL not set")
        with ribbon(bus, self.service, gpu=True, request={"input": inp[:200], "request_type": "query"}) as call:
            try:
                body = {"input": inp, "model": await self._model(), "request_type": "query", "encoding_format": "float"}
                r = await self.http().post(f"{self.s.embed_url}/v1/embeddings", json=body, headers=self.gpu_headers())
                r.raise_for_status()
                vec = [float(x) for x in r.json()["data"][0]["embedding"]]
            except ServiceError:
                raise
            except Exception as e:
                raise self.http_error(e) from e
            call.note = f"{what} dim={len(vec)}" + ("" if len(vec) == DIM else " (expected 256)")
            call.response = {"dim": len(vec)}
            return vec

    @op("embed_text")
    async def embed_text(self, text: str, *, bus=None) -> list[float]:
        return await self._embed(text, bus, "text")

    @op("embed_video")
    async def embed_video(self, mp4: bytes, *, bus=None) -> list[float]:
        return await self._embed("data:video/mp4;base64," + base64.b64encode(mp4).decode(), bus, "video")

    def visual_vectors(self) -> dict[str, list[float]] | None:
        if not self._visual_loaded:
            self._visual, self._visual_loaded = load_visual_vectors(), True
        return self._visual


async def embed_segments(limit: int | None = None, concurrency: int = 4) -> int:
    """Offline: embed every index segment directly (640 px clip via data URI) -> embed_visual.npy + index."""
    import numpy as np

    from perjury.clients import build_clients
    from perjury.config import settings
    s = settings()
    c = build_clients(s)
    segs = json.loads(s.index_path.read_text())["segments"][: limit or None]
    sem = asyncio.Semaphore(concurrency)
    out: dict[str, list[float]] = {}

    async def one(seg):
        async with sem:
            try:
                clip = await c.media.small_clip(seg["source"])
                out[seg["source"]] = await c.embed.embed_video(clip)
            except Exception as e:
                print(f"[embed] skip {seg['source'].rsplit('/', 2)[-2:]}: {type(e).__name__}", file=sys.stderr)

    await asyncio.gather(*(one(x) for x in segs))
    srcs = [x["source"] for x in segs if x["source"] in out]
    if srcs:
        np.save(VISUAL_NPY, np.array([out[k] for k in srcs], dtype=np.float32))
        VISUAL_IDX.write_text(json.dumps(srcs))
    print(f"embedded {len(srcs)}/{len(segs)} segments -> {VISUAL_NPY.name}")
    return len(srcs)


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description="Cosmos-Embed1 helpers")
    ap.add_argument("--segments", action="store_true", help="embed all index segments (writes cache/embed_visual.npy)")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--text", help="embed one text query and print its dimension")
    a = ap.parse_args(argv)
    if a.segments:
        asyncio.run(embed_segments(a.limit))
    elif a.text:
        from perjury.clients import build_clients
        v = asyncio.run(build_clients().embed.embed_text(a.text))
        print(f"dim={len(v)}")
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
