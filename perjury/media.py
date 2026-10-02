"""Pixels for the jury: presigned S3 GETs (dependency-free SigV4), ffmpeg keyframes / 4K crop clips (imageio-ffmpeg's bundled
binary; -ss before -i), the 2x2 juror grid with burned-in panel numbers, and 480 px wall tiles (cache/tiles/).
Without S3 keys, sources are read through VSS playback-url / stream?token= (safety-board ensure_poster pattern).
"""
from __future__ import annotations

import asyncio
import hashlib
import hmac
import io
import json
import os
import tempfile
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from PIL import Image, ImageDraw, ImageFont

from perjury.clients import ServiceError, ribbon
from perjury.config import CACHE, Settings

GRID_W, GRID_H = 1920, 1080
TILES = CACHE / "tiles"


class MediaError(ServiceError):
    def __init__(self, msg: str):
        super().__init__("s3", msg)


def ffmpeg_exe() -> str:
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


# ---- SigV4 query-string presign (AWS "Authenticating Requests: Using Query Parameters") ----
def _q(s: str, safe: str = "-_.~") -> str:
    return urllib.parse.quote(s, safe=safe)


def presign_s3(endpoint: str, bucket: str, key: str, access: str, secret: str, *, expires: int = 3600,
               region: str = "us-east-1", method: str = "GET", now: Optional[datetime] = None,
               virtual_host: bool = False) -> str:
    ep = endpoint if "://" in endpoint else f"http://{endpoint}"
    u = urllib.parse.urlsplit(ep)
    host = f"{bucket}.{u.netloc}" if virtual_host else u.netloc
    path = "/" + _q(key, safe="/-_.~") if virtual_host else f"/{_q(bucket)}/" + _q(key, safe="/-_.~")
    t = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    amz_date, day = t.strftime("%Y%m%dT%H%M%SZ"), t.strftime("%Y%m%d")
    scope = f"{day}/{region}/s3/aws4_request"
    params = {"X-Amz-Algorithm": "AWS4-HMAC-SHA256", "X-Amz-Credential": f"{access}/{scope}", "X-Amz-Date": amz_date,
              "X-Amz-Expires": str(int(expires)), "X-Amz-SignedHeaders": "host"}
    qs = "&".join(f"{_q(k)}={_q(v)}" for k, v in sorted(params.items()))
    canonical = "\n".join([method, path, qs, f"host:{host}", "", "host", "UNSIGNED-PAYLOAD"])
    to_sign = "\n".join(["AWS4-HMAC-SHA256", amz_date, scope, hashlib.sha256(canonical.encode()).hexdigest()])
    k = ("AWS4" + secret).encode()
    for part in (day, region, "s3", "aws4_request"):
        k = hmac.new(k, part.encode(), hashlib.sha256).digest()
    sig = hmac.new(k, to_sign.encode(), hashlib.sha256).hexdigest()
    return f"{u.scheme}://{host}{path}?{qs}&X-Amz-Signature={sig}"


def split_s3(uri: str) -> tuple[str, str]:
    if not uri.startswith("s3://"):
        raise MediaError(f"not an s3:// uri: {uri[:80]}")
    bucket, _, key = uri[5:].partition("/")
    return bucket, key


# ---- Pillow helpers ----
def font(size: int):
    try:
        return ImageFont.load_default(size=size)
    except TypeError:  # Pillow < 10.1
        return ImageFont.load_default()


def to_jpeg(im: Image.Image, quality: int = 88, comment: bytes | None = None) -> bytes:
    buf = io.BytesIO()
    kw = {"comment": comment} if comment else {}
    im.convert("RGB").save(buf, "JPEG", quality=quality, **kw)
    return buf.getvalue()


def grid2x2(frames: list[bytes], labels: list[str] | None = None) -> bytes:
    """1920x1080 JPEG: panels 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right, numbers burned in."""
    pw, ph = GRID_W // 2, GRID_H // 2
    canvas = Image.new("RGB", (GRID_W, GRID_H), (8, 10, 14))
    d = ImageDraw.Draw(canvas)
    big, small = font(64), font(26)
    for i in range(4):
        x0, y0 = (i % 2) * pw, (i // 2) * ph
        if i < len(frames) and frames[i]:
            im = Image.open(io.BytesIO(frames[i]))
            im.draft("RGB", (pw, ph))   # JPEG DCT-domain downscale: 4K/1080p frames decode at panel size
            im = im.convert("RGB")
            im.thumbnail((pw, ph))
            canvas.paste(im, (x0 + (pw - im.width) // 2, y0 + (ph - im.height) // 2))
        d.rectangle([x0 + 14, y0 + 14, x0 + 94, y0 + 104], fill=(0, 0, 0))
        d.text((x0 + 54, y0 + 59), str(i + 1), fill=(255, 255, 255), font=big, anchor="mm")
        if labels and i < len(labels) and labels[i]:
            d.rectangle([x0 + 14, y0 + ph - 50, x0 + 30 + int(d.textlength(labels[i], font=small)), y0 + ph - 14],
                        fill=(0, 0, 0))
            d.text((x0 + 22, y0 + ph - 32), labels[i], fill=(230, 230, 230), font=small, anchor="lm")
    d.line([(pw, 0), (pw, GRID_H)], fill=(255, 255, 255), width=3)
    d.line([(0, ph), (GRID_W, ph)], fill=(255, 255, 255), width=3)
    return to_jpeg(canvas)


def draw_boxes(jpeg: bytes, boxes: list[dict], caption: str = "") -> bytes:
    """boxes: [{"xyxy1000":[x1,y1,x2,y2] | "px":[...], "label": str, "color": (r,g,b)}] -> JPEG (exhibit frames)."""
    im = Image.open(io.BytesIO(jpeg)).convert("RGB")
    d = ImageDraw.Draw(im)
    f = font(max(16, im.width // 60))
    for b in boxes:
        if b.get("px"):
            x1, y1, x2, y2 = b["px"]
        else:
            x1, y1, x2, y2 = (v / 1000 * (im.width if i % 2 == 0 else im.height) for i, v in enumerate(b["xyxy1000"]))
        color = tuple(b.get("color") or (255, 196, 0))
        d.rectangle([x1, y1, x2, y2], outline=color, width=max(3, im.width // 400))
        if b.get("label"):
            d.text((x1 + 4, max(0, y1 - f.size - 6)), b["label"], fill=color, font=f)
    if caption:
        d.rectangle([0, im.height - f.size - 20, im.width, im.height], fill=(0, 0, 0))
        d.text((12, im.height - f.size - 10), caption, fill=(255, 255, 255), font=f)
    return to_jpeg(im)


async def run_ffmpeg(args: list[str], timeout: float = 60.0) -> bytes:
    proc = await asyncio.create_subprocess_exec(ffmpeg_exe(), "-hide_banner", "-loglevel", "error", *args,
                                                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    try:
        out, err = await asyncio.wait_for(proc.communicate(), timeout)
    except asyncio.TimeoutError:
        proc.kill()
        raise MediaError("ffmpeg timeout")
    if proc.returncode != 0:
        raise MediaError(f"ffmpeg rc={proc.returncode}: {err.decode(errors='replace')[-300:]}")
    return out


_X264 = ["-an", "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p", "-movflags", "+faststart"]


async def ffmpeg_to_mp4(args: list[str], timeout: float = 90.0) -> bytes:
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "out.mp4")
        await run_ffmpeg([*args, *_X264, "-y", out], timeout)
        return Path(out).read_bytes()


async def stills_to_mp4(jpegs: list[bytes], seconds_each: float = 1.5, width: int = 1280) -> bytes:
    """Slideshow mp4 (exhibit reel): each still held seconds_each."""
    with tempfile.TemporaryDirectory() as d:
        lst = []
        for i, j in enumerate(jpegs):
            p = os.path.join(d, f"f{i:03d}.jpg")
            Path(p).write_bytes(j)
            lst += [f"file '{p}'", f"duration {seconds_each}"]
        if jpegs:
            lst.append(f"file '{os.path.join(d, f'f{len(jpegs) - 1:03d}.jpg')}'")
        Path(d, "list.txt").write_text("\n".join(lst))
        return await ffmpeg_to_mp4(["-f", "concat", "-safe", "0", "-i", os.path.join(d, "list.txt"),
                                    "-vf", f"scale={width}:-2,fps=10"])


class Media:
    service = "s3"

    def __init__(self, s: Settings, vss=None):
        self.s = s
        self.vss = vss
        self.region = s.env.get("S3_REGION", "us-east-1")
        self._index: Optional[dict] = None
        self._sems: dict = {}

    def _sem(self) -> asyncio.Semaphore:
        loop = asyncio.get_running_loop()
        if loop not in self._sems:
            self._sems = {loop: asyncio.Semaphore(int(self.s.env.get("PERJURY_FFMPEG_CONCURRENCY", "6")))}
        return self._sems[loop]

    # ---- URLs ----
    def presign(self, source: str, expires=3600) -> str:
        """Presigned S3 GET (SigV4, path-style) when S3 keys are set; else the VSS stream?token= URL."""
        if source.startswith(("http://", "https://")) or "://" not in source:   # URL or local file
            return source
        if self.s.s3_endpoint and self.s.s3_access and self.s.s3_secret:
            bucket, key = split_s3(source)
            return presign_s3(self.s.s3_endpoint, bucket, key, self.s.s3_access, self.s.s3_secret,
                              expires=expires, region=self.region)
        if self.vss is not None:
            return self.vss.stream_url(source)
        raise MediaError("no S3 keys and no VSS client to read media")

    async def _fallback_url(self, source: str) -> Optional[str]:
        if self.vss is None:
            return None
        try:
            return await self.vss.playback_url(source)
        except Exception:
            try:
                await self.vss.login()
                return self.vss.stream_url(source)
            except Exception:
                return None

    async def _with_url(self, source: str, fn):
        """fn(url) with the presigned URL, then once more through VSS if the first read fails."""
        try:
            return await fn(self.presign(source))
        except MediaError as first:
            alt = await self._fallback_url(source)
            if not alt:
                raise first
            return await fn(alt)

    # ---- frames / clips ----
    async def keyframe(self, source: str, t: float, width: int = 1920) -> bytes:
        async def grab(url: str) -> bytes:
            async with self._sem():
                out = await run_ffmpeg(["-ss", f"{max(0.0, t):.3f}", "-i", url, "-frames:v", "1",
                                        "-vf", f"scale={width}:-2", "-q:v", "3", "-f", "image2pipe",
                                        "-vcodec", "mjpeg", "pipe:1"], timeout=45)
            if len(out) < 200:
                raise MediaError(f"empty frame at t={t:.2f}")
            return out
        return await self._with_url(source, grab)

    async def keyframes(self, source: str, times: list[float], width: int = 1920, *, bus=None) -> list[bytes]:
        with ribbon(bus, self.service, request={"source": source, "times": times, "op": "presigned GET + ffmpeg"}) as c:
            frames = await asyncio.gather(*(self.keyframe(source, t, width) for t in times))
            c.response = {"frames": len(frames), "bytes": sum(map(len, frames))}
            return list(frames)

    def grid2x2(self, frames: list[bytes], labels: list[str] | None = None) -> bytes:
        return grid2x2(frames, labels)

    async def crop_clip(self, source: str, t: float, box_px: tuple[int, int, int, int], dur: float = 0.5, *,
                        bus=None, pad: float = 0.10) -> bytes:
        """dur-second mp4 of the 4K crop around box_px (padded), longer side scaled to 640 for YOLO."""
        x1, y1, x2, y2 = box_px
        w, h = max(8, x2 - x1), max(8, y2 - y1)
        x, y = max(0, int(x1 - w * pad)), max(0, int(y1 - h * pad))
        w, h = int(w * (1 + 2 * pad)) // 2 * 2, int(h * (1 + 2 * pad)) // 2 * 2
        vf = (f"crop='min({w},iw-{x})':'min({h},ih-{y})':{x}:{y},"
              "scale='if(gt(iw,ih),640,-2)':'if(gt(iw,ih),-2,640)'")

        async def cut(url: str) -> bytes:
            async with self._sem():
                return await ffmpeg_to_mp4(["-ss", f"{max(0.0, t):.3f}", "-i", url, "-t", f"{dur:.2f}", "-vf", vf])
        with ribbon(bus, self.service, request={"source": source, "t": t, "box_px": list(box_px), "op": "4K crop"}) as c:
            out = await self._with_url(source, cut)
            c.response = {"bytes": len(out)}
            return out

    async def small_clip(self, source: str, width: int = 640, dur: float = 5.0) -> bytes:
        async def cut(url: str) -> bytes:
            async with self._sem():
                return await ffmpeg_to_mp4(["-i", url, "-t", f"{dur:.2f}", "-vf", f"scale={width}:-2"])
        return await self._with_url(source, cut)

    # ---- wall tiles ----
    def _segments(self) -> list[dict]:
        if self._index is None:
            try:
                self._index = json.loads(self.s.index_path.read_text())
            except (OSError, ValueError):
                self._index = {"segments": []}
        return self._index.get("segments", [])

    def tile_source(self, scene: int, camera: str) -> Optional[str]:
        segs = sorted((x for x in self._segments() if x.get("scene") == scene and x.get("camera") == camera),
                      key=lambda x: x.get("seg", 0))
        return segs[len(segs) // 3]["source"] if segs else None

    async def tile(self, scene: int, camera: str) -> bytes:
        path = TILES / f"scene{scene}_{camera}.jpg"
        if path.exists() and path.stat().st_size > 200:
            return path.read_bytes()
        src = self.tile_source(scene, camera)
        if not src:
            raise MediaError(f"no segment for scene {scene} {camera}")
        jpg = await self.keyframe(src, 1.0, width=480)
        try:
            TILES.mkdir(parents=True, exist_ok=True)
            path.write_bytes(jpg)
        except OSError:
            pass
        return jpg

    async def warm_tiles(self, concurrency: int = 6) -> int:
        """Boot-time warm of every (scene, camera) tile; returns how many are ready."""
        pairs = sorted({(x["scene"], x["camera"]) for x in self._segments()})
        sem = asyncio.Semaphore(concurrency)

        async def one(p):
            async with sem:
                try:
                    await self.tile(*p)
                    return 1
                except Exception:
                    return 0
        return sum(await asyncio.gather(*(one(p) for p in pairs)))
