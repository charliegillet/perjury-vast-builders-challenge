"""PERJURY web app (FINAL-IDEA-v3 §9, BUILD-CONTRACT "App").

Every route is relative to `/` because the Ingress strips `/app`; the UI in app/static/ uses relative URLs only.
The same app runs on the VM (`python -m app.main`, http://localhost:8080) and in the team pod (`python main.py`).

Pipeline modules (perjury.pipeline, perjury.clients, ...) are imported lazily so this module always imports,
even while they are being built. With PERJURY_DEV_STUB=1 and no pipeline, app/dev_stub.py replays a scripted run
so the UI can be checked; the UI then shows a DEV STUB banner.
"""
from __future__ import annotations

import asyncio
import io
import json
import logging
import os
import re
import time
import uuid
from collections import OrderedDict
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path
from typing import Any, Literal, Optional

from fastapi import FastAPI, File, HTTPException, Query, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator

from perjury import obs
from perjury.config import CACHE, settings
from perjury.events import EventBus, load_recording, sse_format

log = logging.getLogger("perjury.app")

STATIC = Path(__file__).resolve().parent / "static"
MAX_TEXT = 500
MAX_AUDIO_BYTES = 12 * 1024 * 1024      # ~6 min of 16 kHz mono WAV; wav.js output is far smaller
MAX_RUNS = 50
RUN_TIMEOUT_S = float(os.getenv("PERJURY_RUN_TIMEOUT_S", "60"))   # app-level guard over the pipeline's 20 s atom cap
KEEPALIVE_S = 10.0
CAMERA_RE = re.compile(r"^p[1-3]c[1-6]$")
NAME_RE = re.compile(r"^[\w.-]{1,160}$")
SLOTS = [f"p{p}c{c}" for c in range(1, 7) for p in range(1, 4)]   # 6 camera rows x 3 pole columns


def runs_dir() -> Path:
    return Path(os.getenv("PERJURY_RUNS_DIR", str(CACHE / "runs")))


def replay_dirs() -> list[Path]:
    # cache/runs: every live run; cache/replays: curated hero recordings shipped in the perjury-cache ConfigMap
    return [runs_dir(), CACHE / "replays"]


# ---------------------------------------------------------------- state

class State:
    def __init__(self) -> None:
        self.ctx: Any = None
        self.ctx_error: Optional[str] = None
        self.ctx_tried_at = 0.0
        self.stub = None                         # app.dev_stub module when PERJURY_DEV_STUB=1 and no pipeline
        self.runs: OrderedDict[str, dict] = OrderedDict()
        self.transcripts: OrderedDict[str, dict] = OrderedDict()
        self.tiles: dict[tuple[int, str], bytes] = {}
        self.exhibit_jpgs: OrderedDict[tuple, bytes] = OrderedDict()
        self.index_raw: Optional[dict] = None
        self.index_mtime = 0.0
        self.probes_raw: Optional[dict] = None
        self.probes_mtime = 0.0
        self.witness_job: dict = {"state": "idle"}
        self.warm_task: Optional[asyncio.Task] = None


STATE = State()


def _remember(store: OrderedDict, key: Any, value: Any, cap: int) -> None:
    store[key] = value
    store.move_to_end(key)
    while len(store) > cap:
        store.popitem(last=False)


async def _ensure_ctx(force: bool = False) -> Any:
    """Load the pipeline Context once; retry at most every 5 s while the pipeline modules are missing or broken."""
    if STATE.ctx is not None:
        return STATE.ctx
    if not force and time.monotonic() - STATE.ctx_tried_at < 5:
        return None
    STATE.ctx_tried_at = time.monotonic()
    try:
        from perjury import pipeline  # noqa: WPS433 (lazy: written concurrently)
        STATE.ctx = await asyncio.to_thread(pipeline.load_context, settings())
        STATE.ctx_error = None
        STATE.stub = None
    except Exception as e:  # keep serving the UI, /health says why
        STATE.ctx_error = f"{type(e).__name__}: {str(obs.redact(str(e)))[:300]}"
        log.warning("pipeline context unavailable: %s", STATE.ctx_error)
        if os.getenv("PERJURY_DEV_STUB") == "1":
            from app import dev_stub  # noqa: WPS433
            STATE.stub = dev_stub
            STATE.ctx = dev_stub.load_context(settings())
    return STATE.ctx


def _clients() -> Any:
    return getattr(STATE.ctx, "clients", None)


# ---------------------------------------------------------------- index / probes (raw JSON, cached by mtime)

def _load_json_cached(path: Path, attr: str) -> Optional[dict]:
    try:
        mtime = path.stat().st_mtime
    except OSError:
        return None
    if getattr(STATE, attr) is None or getattr(STATE, attr.replace("raw", "mtime")) != mtime:
        setattr(STATE, attr, json.loads(path.read_text()))
        setattr(STATE, attr.replace("raw", "mtime"), mtime)
    return getattr(STATE, attr)


def index_raw() -> Optional[dict]:
    return _load_json_cached(settings().index_path, "index_raw")


def probes_raw() -> Optional[dict]:
    return _load_json_cached(settings().probes_path, "probes_raw")


def scene_cameras(scene: int) -> list[str]:
    idx = index_raw() or {}
    return list(((idx.get("scenes") or {}).get(str(scene)) or {}).get("cameras") or [])


def _check_scene(scene: int) -> int:
    if scene not in (1, 2, 3):
        raise HTTPException(422, "scene must be 1, 2 or 3")
    return scene


def _check_camera(camera: str) -> str:
    if not CAMERA_RE.match(camera or ""):
        raise HTTPException(422, "camera must look like p1c1…p3c6")
    return camera


# ---------------------------------------------------------------- lifespan

async def _warm_tiles() -> None:
    """Warm the 49 wall thumbnails in the background (§9: ~30 s at boot)."""
    await _ensure_ctx(force=True)
    media = getattr(_clients(), "media", None)
    if media is None:
        return
    sem = asyncio.Semaphore(4)

    async def one(scene: int, cam: str) -> None:
        async with sem:
            try:
                STATE.tiles[(scene, cam)] = await media.tile(scene, cam)
            except Exception as e:
                log.info("tile warm failed scene%s %s: %s", scene, cam, type(e).__name__)

    await asyncio.gather(*[one(s, c) for s in (1, 2, 3) for c in scene_cameras(s)])


@asynccontextmanager
async def lifespan(app: FastAPI):
    STATE.ctx = None
    STATE.ctx_tried_at = 0.0
    obs.init(settings().wandb_project)
    await _ensure_ctx(force=True)
    if os.getenv("PERJURY_WARM_TILES", "1") != "0":
        STATE.warm_task = asyncio.create_task(_warm_tiles())
    try:
        yield
    finally:
        if STATE.warm_task:
            STATE.warm_task.cancel()


app = FastAPI(title="PERJURY", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])  # contract: CORS on
app.mount("/static", StaticFiles(directory=str(STATIC)), name="static")


# ---------------------------------------------------------------- UI + health

@app.get("/", include_in_schema=False)
async def index() -> FileResponse:
    return FileResponse(STATIC / "index.html", headers={"Cache-Control": "no-cache"})


@app.get("/health")
async def health() -> dict:
    s = settings()
    idx = index_raw()
    return {
        "ok": True,
        "mode": s.mode,
        "pod": s.pod_name,
        "index_segments": len((idx or {}).get("segments") or []),
        "coverage": (idx or {}).get("coverage"),
        "probes": settings().probes_path.exists(),
        "pipeline": STATE.ctx is not None and STATE.stub is None,
        "pipeline_error": STATE.ctx_error,
        "dev_stub": STATE.stub is not None,
        "weave": obs.enabled(),
        "tiles_warm": len(STATE.tiles),
        "tiles_total": sum(len(scene_cameras(n)) for n in (1, 2, 3)),
    }


# ---------------------------------------------------------------- scene + tiles

def _t0_camera_summary(segs: list[dict]) -> dict:
    classes: dict[str, int] = {}
    peak: dict[str, int] = {}
    persist: dict[str, int] = {}
    for g in segs:
        for c in g.get("object_classes") or []:
            classes[c] = classes.get(c, 0) + 1
        for c, n in (g.get("object_counts") or {}).items():
            peak[c] = max(peak.get(c, 0), int(n or 0))
        for c, n in (g.get("persist") or {}).items():
            persist[c] = max(persist.get(c, 0), int(n or 0))
    return {"segments": len(segs), "segments_with": classes, "peak": peak, "persist": persist}


def _probe_summary(p: Optional[dict]) -> Optional[dict]:
    if not p:
        return None
    out: dict[str, Any] = {}
    cond = (p.get("P-COND") or {}).get("parsed")
    if cond:
        out["cond"] = cond
    panels = ((p.get("P-COUNT") or {}).get("parsed") or {}).get("panels")
    if panels:
        out["people_on_foot"] = max(int(x.get("people_on_foot") or 0) for x in panels)
    return out or None


@app.get("/api/scene/{n}")
async def scene(n: int) -> dict:
    _check_scene(n)
    idx = index_raw()
    if idx is None:
        raise HTTPException(503, f"index not built yet ({settings().index_path.name})")
    meta = (idx.get("scenes") or {}).get(str(n)) or {}
    cams = list(meta.get("cameras") or [])
    segs = [g for g in idx.get("segments") or [] if g.get("scene") == n]
    by_cam: dict[str, list[dict]] = {}
    for g in segs:
        by_cam.setdefault(g.get("camera"), []).append(g)
    probes = ((probes_raw() or {}).get("scenes") or {}).get(str(n)) or {}
    totals = _t0_camera_summary(segs)
    return {
        "scene": n,
        "label": meta.get("label", ""),
        "duration": meta.get("duration"),
        "cameras": cams,
        "slots": [{"camera": c, "present": c in cams} for c in SLOTS],
        "segments": len(segs),
        "location": next((g.get("location") for g in segs if g.get("location")), None),
        "t0": {"totals": totals,
               "cameras": {c: {**_t0_camera_summary(by_cam.get(c, [])), "probes": _probe_summary(probes.get(c))}
                           for c in cams}},
        "source": idx.get("source"),
    }


def _placeholder_jpeg(text: str, w: int = 480, h: int = 270) -> bytes:
    from PIL import Image, ImageDraw  # noqa: WPS433
    im = Image.new("RGB", (w, h), (11, 16, 32))
    d = ImageDraw.Draw(im)
    for x in range(-h, w, 18):
        d.line([(x, h), (x + h, 0)], fill=(20, 28, 49), width=6)
    d.text((12, h - 24), text, fill=(147, 160, 192))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=80)
    return buf.getvalue()


@app.get("/api/tile")
async def tile(scene: int = Query(...), camera: str = Query(...)) -> Response:
    _check_scene(scene)
    _check_camera(camera)
    key = (scene, camera)
    data = STATE.tiles.get(key)
    if data is None:
        await _ensure_ctx()
        media = getattr(_clients(), "media", None)
        if media is not None and camera in scene_cameras(scene):
            try:
                data = await media.tile(scene, camera)
                STATE.tiles[key] = data
            except Exception as e:
                log.info("tile failed: %s", type(e).__name__)
    if data is None:
        return Response(_placeholder_jpeg(f"scene {scene} · {camera} · no tile"), media_type="image/jpeg",
                        headers={"Cache-Control": "no-store"})
    return Response(data, media_type="image/jpeg", headers={"Cache-Control": "public, max-age=3600"})


# ---------------------------------------------------------------- testify (SSE)

class TestifyIn(BaseModel):
    text: str = Field(..., min_length=1, max_length=MAX_TEXT)
    scene: int
    stock_ab: bool = False
    transcript_source: Literal["typed", "canary"] = "typed"
    transcript_id: Optional[str] = None
    jury_size: Optional[int] = Field(None, ge=1, le=16)

    @field_validator("text")
    @classmethod
    def _text(cls, v: str) -> str:
        v = " ".join(v.split())
        if not v:
            raise ValueError("text is empty")
        return v

    @field_validator("scene")
    @classmethod
    def _scene(cls, v: int) -> int:
        if v not in (1, 2, 3):
            raise ValueError("scene must be 1, 2 or 3")
        return v


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:40] or "claim"


def _new_run_id(text: str) -> str:
    return f"{datetime.now():%Y%m%d-%H%M%S}_{_slug(text)}_{uuid.uuid4().hex[:4]}"


async def _sse_from(agen) -> Any:
    """Yield SSE frames from an async iterator of events, with keepalive comments while idle."""
    yield ": perjury\n\n"
    pending = asyncio.ensure_future(agen.__anext__())
    try:
        while True:
            done, _ = await asyncio.wait({pending}, timeout=KEEPALIVE_S)
            if not done:
                yield ": ping\n\n"
                continue
            try:
                ev = pending.result()
            except StopAsyncIteration:
                return
            yield sse_format(ev)
            if ev["event"] == "done":
                return
            pending = asyncio.ensure_future(agen.__anext__())
    finally:
        if not pending.done():
            pending.cancel()


SSE_HEADERS = {"Cache-Control": "no-cache", "X-Accel-Buffering": "no", "Connection": "keep-alive"}


async def _run_pipeline(entry: dict, body: TestifyIn, source: str) -> None:
    bus: EventBus = entry["bus"]
    try:
        ctx = await _ensure_ctx()
        if ctx is None:
            raise RuntimeError(f"pipeline unavailable ({STATE.ctx_error})")
        if STATE.stub is not None:
            testify = STATE.stub.testify
        else:
            from perjury.pipeline import testify  # noqa: WPS433
        kwargs: dict[str, Any] = {"transcript_source": source, "stock_ab": body.stock_ab}
        if entry.get("canary_ms"):
            kwargs["transcript_latency_ms"] = entry["canary_ms"]
        if body.jury_size:
            kwargs["jury_size"] = body.jury_size
        entry["verdict"] = await asyncio.wait_for(testify(body.text, body.scene, ctx, bus, **kwargs),
                                                  timeout=RUN_TIMEOUT_S)
    except asyncio.TimeoutError:
        bus.emit("error", {"message": f"run exceeded the {RUN_TIMEOUT_S:.0f} s hard cap"})
    except Exception as e:
        log.exception("testify failed")
        if not any(ev["event"] == "run" for ev in bus.events):
            bus.emit("run", {"run_id": bus.run_id, "text": body.text, "scene": body.scene, "mode": settings().mode})
        bus.emit("error", {"message": obs.redact(f"{type(e).__name__}: {e}")[:400]})
    finally:
        if not bus.closed:
            bus.emit("done", {})


@app.post("/api/testify")
async def testify(body: TestifyIn) -> StreamingResponse:
    run_id = _new_run_id(body.text)
    bus = EventBus(run_id, record_to=runs_dir() / f"{run_id}.jsonl")
    source = "typed"
    # Voice testimony: the Canary call already happened in /api/transcribe; report it on this run's ribbon,
    # but only if the text is exactly what Canary heard (edited text counts as typed, §10 honesty rules).
    tr = STATE.transcripts.get(body.transcript_id or "") if body.transcript_source == "canary" else None
    if tr and " ".join(tr["text"].split()) == body.text:
        source = "canary"
        bus.service("canary", "done", ms=tr["latency_ms"], gpu=True, note=tr.get("model_id") or "",
                    request=tr["request"], response=tr["response"])
    entry = {"run_id": run_id, "bus": bus, "events": bus.events, "verdict": None, "text": body.text,
             "scene": body.scene, "started_at": time.time(), "replay": False,
             "canary_ms": tr["latency_ms"] if source == "canary" else 0}
    _remember(STATE.runs, run_id, entry, MAX_RUNS)
    entry["task"] = asyncio.create_task(_run_pipeline(entry, body, source))
    return StreamingResponse(_sse_from(bus.stream()), media_type="text/event-stream", headers=SSE_HEADERS)


# ---------------------------------------------------------------- transcribe (Canary)

@app.post("/api/transcribe")
async def transcribe(request: Request, file: UploadFile = File(...)) -> dict:
    wav = await file.read(MAX_AUDIO_BYTES + 1)
    if len(wav) > MAX_AUDIO_BYTES:
        raise HTTPException(413, "recording too large (max 12 MB); keep testimony under a minute")
    if len(wav) < 44 or wav[:4] != b"RIFF" or wav[8:12] != b"WAVE":
        raise HTTPException(415, "expected a 16 kHz mono WAV (the browser encodes it with wav.js)")
    ctx = await _ensure_ctx()
    canary = getattr(_clients(), "canary", None)
    if ctx is None or canary is None:
        raise HTTPException(503, f"Canary client unavailable ({STATE.ctx_error})")
    hint = request.headers.get("X-Fixture-Transcript")
    if hint and settings().mode == "fixture":
        # FakeCanary reads the transcript after this marker inside the upload (tests and offline demos only)
        wav = wav + b"\nX-Fixture-Transcript: " + hint[:MAX_TEXT].encode("utf-8", "replace") + b"\n"
    t = time.monotonic()
    try:
        out = await canary.transcribe(wav)
    except Exception as e:
        raise HTTPException(502, obs.redact(f"Canary failed: {type(e).__name__}: {e}")[:300])
    ms = int(out.get("latency_ms") or (time.monotonic() - t) * 1000)
    text = " ".join(str(out.get("text") or "").split())[:MAX_TEXT]
    tid = uuid.uuid4().hex[:12]
    _remember(STATE.transcripts, tid, {
        "text": text, "latency_ms": ms, "model_id": out.get("model_id"),
        "request": {"endpoint": "/v1/audio/transcriptions", "file": f"<{len(wav)} bytes wav>",
                    "model": out.get("model_id")},
        "response": obs.redact({k: v for k, v in out.items()}),
    }, 50)
    return {"text": text, "model_id": out.get("model_id"), "latency_ms": ms, "transcript_id": tid}


# ---------------------------------------------------------------- exhibits

def _events_for(run_id: str) -> Optional[list[dict]]:
    entry = STATE.runs.get(run_id)
    if entry is not None:
        return entry["events"]
    if NAME_RE.match(run_id):
        for d in replay_dirs():
            p = d / f"{run_id}.jsonl"
            if p.exists():
                return load_recording(p)
    return None


def _exhibit(run_id: str, atom_id: str, camera: str) -> dict:
    events = _events_for(run_id)
    if events is None:
        raise HTTPException(404, "unknown run (the app keeps the last 50 runs plus recordings)")
    run = next((e["data"] for e in events if e["event"] == "run"), {})
    atom = None
    juror = None
    vote = None
    probe = {}
    ground = None
    zoom = None
    for e in events:
        d, name = e["data"], e["event"]
        if name == "atoms":
            atom = next((a for a in d.get("atoms") or [] if a.get("id") == atom_id), atom)
        if d.get("atom_id") != atom_id and name != "atom_verdict":
            continue
        if name == "summon":
            probe = {"probe": d.get("probe"), "probe_version": d.get("probe_version")}
            juror = next((j for j in d.get("jurors") or [] if j.get("camera") == camera), juror)
        elif name == "juror" and (d.get("vote") or {}).get("camera") == camera:
            vote = d["vote"]
        elif name == "ground" and d.get("camera") == camera:
            ground = d
        elif name == "zoom" and d.get("camera") == camera:
            zoom = d
        elif name == "atom_verdict":
            av = d.get("atom_verdict") or {}
            if av.get("atom_id") == atom_id:
                vote = next((v for v in av.get("votes") or [] if v.get("camera") == camera), vote)
    if vote is None and juror is None:
        raise HTTPException(404, f"no juror {camera} on atom {atom_id}")
    juror = (vote or {}).get("juror") or juror or {}
    panel = (ground or {}).get("panel") or next(iter((vote or {}).get("yes_panels") or []), None) or 1
    q = f"run_id={run_id}&atom_id={atom_id}&camera={camera}"
    return {
        "run_id": run_id, "atom_id": atom_id, "camera": camera, "scene": run.get("scene"),
        "atom": atom, "vote": vote, "juror": juror, "ground": ground, "zoom": zoom, "panel": panel,
        "probe": (vote or {}).get("probe") or probe.get("probe"),
        "probe_version": (vote or {}).get("probe_version") or probe.get("probe_version"),
        "latency_ms": (vote or {}).get("latency_ms"),
        "cached": (vote or {}).get("cached"), "cached_at": (vote or {}).get("cached_at"),
        "image": f"api/exhibit.jpg?{q}&panel={panel}",
        "stream": f"api/stream?{q}" if juror.get("source") else None,
        "replay": (STATE.runs.get(run_id) or {}).get("replay", True),
    }


async def _stream_url(source: Optional[str]) -> Optional[str]:
    await _ensure_ctx()
    vss = getattr(_clients(), "vss", None)
    if vss is None or not source:
        return None
    try:
        url = await asyncio.to_thread(vss.stream_url, source)   # may log in synchronously
    except Exception:
        return None
    return url if url and str(url).startswith(("http://", "https://")) else None


@app.get("/api/exhibit")
async def exhibit(run_id: str, atom_id: str, camera: str) -> dict:
    _check_camera(camera)
    ex = _exhibit(run_id, atom_id, camera)
    if ex["stream"] and not await _stream_url((ex["juror"] or {}).get("source")):
        ex["stream"] = None   # e.g. fixture mode: no playback, the drawer shows the keyframe only
    return ex


@app.get("/api/exhibit.jpg")
async def exhibit_jpg(run_id: str, atom_id: str, camera: str, panel: int = Query(1, ge=1, le=4)) -> Response:
    _check_camera(camera)
    key = (run_id, atom_id, camera, panel)
    if key in STATE.exhibit_jpgs:
        return Response(STATE.exhibit_jpgs[key], media_type="image/jpeg")
    ex = _exhibit(run_id, atom_id, camera)
    await _ensure_ctx()
    media = getattr(_clients(), "media", None)
    juror = ex["juror"] or {}
    data = None
    scene = ex.get("scene")
    source, times = juror.get("source"), juror.get("times") or []
    scene_probes = ((probes_raw() or {}).get("scenes") or {}).get(str(scene)) or {}
    panel_sources = (scene_probes.get(camera) or {}).get("panel_sources") or []
    if ex.get("cached") and len(panel_sources) >= panel:
        source, offset = panel_sources[panel - 1]
        times = [float(offset)] * panel
    if not source and scene:
        # scene-wide pre-run juror: the P-COND/P-COUNT grid came from the scene parent at grid_times
        idx = getattr(STATE.ctx, "index", None)
        try:
            source = idx.scene_parent(int(scene), camera) if idx is not None else None
        except Exception:
            source = None
        times = ((((probes_raw() or {}).get("scenes") or {}).get(str(scene)) or {}).get(camera) or {}).get(
            "grid_times") or []
    if media is not None and source:
        t = times[panel - 1] if len(times) >= panel else (times[0] if times else 0.0)
        try:
            frames = await media.keyframes(source, [float(t)], width=1920)
            data = frames[0] if frames else None
        except Exception as e:
            log.info("exhibit keyframe failed: %s", type(e).__name__)
    if data is None and scene and (int(scene), camera) in STATE.tiles:
        data = STATE.tiles[(int(scene), camera)]
    if data is None:
        data = _placeholder_jpeg(f"{camera} · exhibit frame unavailable", 960, 540)
    else:
        _remember(STATE.exhibit_jpgs, key, data, 40)
    return Response(data, media_type="image/jpeg")


@app.get("/api/stream")
async def stream(request: Request, run_id: str, atom_id: str, camera: str) -> Response:
    """Range-capable proxy to VSS videos/stream for the juror's segment; the VSS token stays server-side."""
    _check_camera(camera)
    ex = _exhibit(run_id, atom_id, camera)
    url = await _stream_url((ex["juror"] or {}).get("source"))
    if not url:
        raise HTTPException(404, "no playable stream for this segment")
    import httpx  # noqa: WPS433
    headers = {k: v for k, v in request.headers.items() if k.lower() in ("range", "if-range")}
    client = httpx.AsyncClient(timeout=httpx.Timeout(30.0, read=60.0))
    upstream = await client.send(client.build_request("GET", url, headers=headers), stream=True)

    async def body():
        try:
            async for chunk in upstream.aiter_bytes(65536):
                yield chunk
        finally:
            await upstream.aclose()
            await client.aclose()

    passthru = {k: v for k, v in upstream.headers.items()
                if k.lower() in ("content-type", "content-length", "content-range", "accept-ranges")}
    return StreamingResponse(body(), status_code=upstream.status_code, headers=passthru)


@app.get("/api/camera-stream")
async def camera_stream(request: Request, scene: int, camera: str) -> Response:
    """Actual recorded camera video, independent of a claim or exhibit."""
    if settings().mode != "live":
        raise HTTPException(409, "Real recorded video requires live service mode")
    _check_camera(camera)
    ctx = await _ensure_ctx()
    try:
        source = ctx.index.scene_parent(scene, camera) if ctx is not None else None
    except (KeyError, ValueError):
        source = None
    if not source:
        raise HTTPException(404, "No recorded camera source for this scene")
    url = await _stream_url(source)
    if not url:
        raise HTTPException(503, "Recorded playback service unavailable")
    import httpx
    client = httpx.AsyncClient(timeout=httpx.Timeout(30.0, read=60.0))
    headers = {k: v for k, v in request.headers.items() if k.lower() in ("range", "if-range")}
    try:
        upstream = await client.send(client.build_request("GET", url, headers=headers), stream=True)
        if upstream.status_code >= 400:
            await upstream.aclose()
            await client.aclose()
            raise HTTPException(upstream.status_code, "Recorded camera playback unavailable")
    except httpx.HTTPError:
        await client.aclose()
        raise HTTPException(502, "Recorded playback connection failed")
    async def body():
        try:
            async for chunk in upstream.aiter_bytes(65536):
                yield chunk
        finally:
            await upstream.aclose()
            await client.aclose()
    passthru = {k: v for k, v in upstream.headers.items()
                if k.lower() in ("content-type", "content-length", "content-range", "accept-ranges")}
    return StreamingResponse(body(), status_code=upstream.status_code, headers=passthru)


# ---------------------------------------------------------------- bench + witness

def _json_file(name: str) -> Any:
    p = CACHE / name
    if not p.exists():
        return {"status": "not_run", "file": name}
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError as e:
        return {"status": "unreadable", "file": name, "error": str(e)[:200]}


@app.get("/api/bench")
async def bench() -> Any:
    rep = _json_file("bench_report.json")
    if isinstance(rep, dict) and "promotion" not in rep and (CACHE / "promotion.json").exists():
        rep = {**rep, "promotion": _json_file("promotion.json")}
    return rep


@app.get("/api/witness")
async def witness() -> Any:
    out = _json_file("witness.json")
    if isinstance(out, dict):
        out = {**out, "job": STATE.witness_job}
    return out


async def _witness_job() -> None:
    STATE.witness_job = {"state": "running", "started_at": time.time()}
    try:
        ctx = await _ensure_ctx()
        if ctx is None:
            raise RuntimeError(f"pipeline unavailable ({STATE.ctx_error})")
        from perjury import witness as wmod  # noqa: WPS433
        await wmod.run(n=9, per_scene=3, out=None, ctx=ctx)   # writes cache/witness.json
        STATE.witness_job = {"state": "done", "finished_at": time.time()}
    except Exception as e:
        STATE.witness_job = {"state": "error", "error": obs.redact(f"{type(e).__name__}: {e}")[:300]}


@app.post("/api/witness/run", status_code=202)
async def witness_run() -> dict:
    if STATE.witness_job.get("state") != "running":
        asyncio.create_task(_witness_job())
    return {"ok": True, "job": STATE.witness_job}


# ---------------------------------------------------------------- replay

def _recording_info(p: Path) -> dict:
    info: dict[str, Any] = {"name": p.stem, "curated": p.parent.name == "replays",
                            "recorded_at": datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec="seconds")}
    try:
        for line in p.read_text().splitlines():
            if '"event": "run"' in line or '"event": "verdict"' in line or '"event": "receipt"' in line:
                ev = json.loads(line)
                d = ev["data"]
                if ev["event"] == "run":
                    info.update(text=d.get("text"), scene=d.get("scene"), mode=d.get("mode"), run_id=d.get("run_id"))
                elif ev["event"] == "verdict":
                    info["verdict"] = d.get("verdict")
                else:
                    info["elapsed_ms"] = d.get("elapsed_ms")
    except Exception:
        info["broken"] = True
    m = re.match(r"^(\d{8})-(\d{6})_", p.stem)
    if m:
        info["recorded_at"] = datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M%S").isoformat()
    return info


@app.get("/api/replays")
async def replays() -> dict:
    files = [p for d in replay_dirs() if d.exists() for p in d.glob("*.jsonl")]
    files.sort(key=lambda p: (p.parent.name != "replays", -p.stat().st_mtime))
    return {"replays": [_recording_info(p) for p in files[:100]]}


def _replay_path(name: str) -> Path:
    name = name[:-6] if name.endswith(".jsonl") else name
    if not NAME_RE.match(name):
        raise HTTPException(422, "bad replay name")
    for d in replay_dirs():
        p = d / f"{name}.jsonl"
        if p.exists():
            return p
    raise HTTPException(404, "no such recording")


@app.get("/api/replay/{name}")
async def replay(name: str, speed: float = Query(1.0, ge=0, le=20)) -> StreamingResponse:
    path = _replay_path(name)
    events = load_recording(path)
    recorded_at = _recording_info(path)["recorded_at"]
    run = next((e["data"] for e in events if e["event"] == "run"), {})
    run_id = run.get("run_id") or path.stem
    _remember(STATE.runs, run_id, {"run_id": run_id, "bus": None, "events": events, "verdict": None,
                                   "text": run.get("text"), "scene": run.get("scene"),
                                   "started_at": time.time(), "replay": True}, MAX_RUNS)

    async def gen():
        prev = 0
        for ev in events:
            if speed > 0:
                gap = max(0, ev.get("t_ms", 0) - prev) / 1000 / speed
                if gap:
                    await asyncio.sleep(min(gap, 15.0))
            prev = ev.get("t_ms", prev)
            yield {"event": ev["event"], "t_ms": ev.get("t_ms", 0),
                   "data": {**ev.get("data", {}), "replay": True, "recorded_at": recorded_at}}
        if not events or events[-1]["event"] != "done":
            yield {"event": "done", "t_ms": prev, "data": {"replay": True, "recorded_at": recorded_at}}

    return StreamingResponse(_sse_from(gen()), media_type="text/event-stream", headers=SSE_HEADERS)


# ---------------------------------------------------------------- feedback

class FeedbackIn(BaseModel):
    run_id: str = Field(..., min_length=1, max_length=200)
    thumbs: Literal["up", "down"]
    note: str = Field("", max_length=1000)


def _weave_feedback(events: list[dict], thumbs: str, note: str) -> bool:
    """Attach 👍/👎 to the run's Weave call when the receipt carries a Weave call URL."""
    if not obs.enabled():
        return False
    url = next((e["data"].get("weave_url") for e in events if e["event"] == "receipt"), None)
    m = re.search(r"/calls?/([0-9a-fA-F-]{8,})", url or "")
    if not m:
        return False
    try:
        import weave  # noqa: WPS433
        call = weave.get_client().get_call(m.group(1))
        call.feedback.add_reaction("👍" if thumbs == "up" else "👎")
        if note:
            call.feedback.add_note(note)
        return True
    except Exception as e:
        log.info("weave feedback failed: %s", type(e).__name__)
        return False


@app.post("/api/feedback")
async def feedback(body: FeedbackIn) -> dict:
    events = _events_for(body.run_id) or []
    run = next((e["data"] for e in events if e["event"] == "run"), {})
    verdict = next((e["data"].get("verdict") for e in events if e["event"] == "verdict"), None)
    sent = await asyncio.to_thread(_weave_feedback, events, body.thumbs, body.note)
    row = {"at": datetime.now().isoformat(timespec="seconds"), "run_id": body.run_id, "thumbs": body.thumbs,
           "note": body.note, "text": run.get("text"), "scene": run.get("scene"), "verdict": verdict,
           "weave": sent}
    p = CACHE / "feedback.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a") as f:
        f.write(json.dumps(row) + "\n")
    return {"ok": True, "weave": sent}


from app.live import router as live_router
app.include_router(live_router)


def main() -> None:
    import uvicorn  # noqa: WPS433
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    # Playback URLs contain authentication tokens; do not log request URLs.
    logging.getLogger("httpx").setLevel(logging.WARNING)
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")), log_level="info", proxy_headers=True)


if __name__ == "__main__":
    main()
