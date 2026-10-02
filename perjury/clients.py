"""Service client bundle (BUILD-CONTRACT "Client interfaces"). build_clients() returns live clients or fixture fakes.

Live modules import their shared helpers from here (ServiceError, parse_model_json, ribbon, HttpBase), so this module
must not import them at top level: build_clients() imports lazily.
"""
from __future__ import annotations

import asyncio
import json
import re
import time
import weakref
from contextlib import contextmanager
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Optional

import httpx
from pydantic import BaseModel

from perjury.config import Settings
from perjury.obs import redact

if TYPE_CHECKING:  # pragma: no cover
    from perjury.canary import Canary
    from perjury.cosmos import Cosmos
    from perjury.embed import Embed
    from perjury.llm import LLM
    from perjury.media import Media
    from perjury.vss import VSSClient
    from perjury.yolo import Yolo


class ProbeResult(BaseModel):
    """One Cosmos juror answer. parsed=None means invalid JSON or an error: the juror abstains."""
    parsed: Optional[dict] = None
    raw_text: str = ""
    latency_ms: int = 0
    cached: bool = False
    cached_at: Optional[str] = None   # "11:32" (local time the cached answer was produced)
    image_sha: str = ""
    error: Optional[str] = None


class ZoomResult(BaseModel):
    """YOLO zoom-check on a 4K crop (§7): ok iff a car/truck box covers >= min_cover of the crop on >= 2 frames."""
    ok: bool = False
    label: Optional[str] = None
    conf: Optional[float] = None
    cover: Optional[float] = None
    frames_ok: int = 0
    error: Optional[str] = None


class ServiceError(Exception):
    def __init__(self, service: str, msg: str, status: Optional[int] = None, timeout: bool = False):
        super().__init__(f"{service}: {msg}")
        self.service, self.status, self.timeout = service, status, timeout


# ---- model output parsing (Cosmos, Nemotron) ----
_THINK = re.compile(r"<think>.*?</think>", re.S)
_FENCE = re.compile(r"```(?:json|JSON)?\s*(.*?)```", re.S)


def strip_think(text: str) -> str:
    """Drop <think>...</think>; also a dangling '...</think>' prefix (template opened the tag) or an unclosed <think> tail."""
    text = _THINK.sub("", text or "")
    if "</think>" in text:
        text = text.split("</think>", 1)[1]
    if "<think>" in text:
        text = text.split("<think>", 1)[0]
    return text.strip()


def parse_model_json(text: str) -> dict:
    """<think> strip, ```fence strip, outermost {...}, light repair (trailing commas, Python literals). Raises ValueError."""
    t = strip_think(text)
    m = _FENCE.search(t)
    if m:
        t = m.group(1)
    start = t.find("{")
    if start < 0:
        raise ValueError("no JSON object in model output")
    body = t[start:]
    end = body.rfind("}")
    candidates = [body[:end + 1]] if end >= 0 else []
    candidates.append(body)
    for c in candidates:
        for fix in (lambda s: s,
                    lambda s: re.sub(r",\s*([}\]])", r"\1", s),
                    lambda s: re.sub(r",\s*([}\]])", r"\1", re.sub(r"\bTrue\b", "true", re.sub(
                        r"\bFalse\b", "false", re.sub(r"\bNone\b", "null", s))))):
            try:
                v, _ = json.JSONDecoder().raw_decode(fix(c))
            except json.JSONDecodeError:
                continue
            if isinstance(v, dict):
                return v
    raise ValueError("invalid JSON in model output")


# ---- ribbon reporting ----
class _Call:
    def __init__(self):
        self.response: Any = None
        self.note = ""
        self.ms = 0


@contextmanager
def ribbon(bus, service: str, *, gpu: bool = False, request: Any = None):
    """bus.service(firing) -> body -> done (ms, redacted request/response) or error. bus=None is a no-op."""
    call, t0 = _Call(), time.monotonic()
    req = redact(request)
    if bus is not None:
        bus.service(service, "firing", request=req)
    try:
        yield call
    except BaseException as e:
        call.ms = int((time.monotonic() - t0) * 1000)
        if bus is not None:
            bus.service(service, "error", ms=call.ms, note=(call.note or f"{type(e).__name__}: {e}")[:300], request=req)
        raise
    call.ms = int((time.monotonic() - t0) * 1000)
    if bus is not None:
        bus.service(service, "done", ms=call.ms, gpu=gpu, note=call.note, request=req,
                    response=redact(call.response))


# ---- httpx client per event loop (tests and offline jobs open several loops) ----
class HttpBase:
    service = "http"

    def __init__(self, s: Settings, timeout: float = 30.0):
        self.s = s
        self.timeout = timeout
        self._clients: "weakref.WeakKeyDictionary[asyncio.AbstractEventLoop, httpx.AsyncClient]" = weakref.WeakKeyDictionary()
        self._sems: "weakref.WeakKeyDictionary[asyncio.AbstractEventLoop, asyncio.Semaphore]" = weakref.WeakKeyDictionary()

    def http(self) -> httpx.AsyncClient:
        loop = asyncio.get_running_loop()
        c = self._clients.get(loop)
        if c is None or c.is_closed:
            c = httpx.AsyncClient(timeout=self.timeout, follow_redirects=True)
            self._clients[loop] = c
        return c

    def sem(self, n: int) -> asyncio.Semaphore:
        loop = asyncio.get_running_loop()
        if loop not in self._sems:
            self._sems[loop] = asyncio.Semaphore(max(1, n))
        return self._sems[loop]

    def gpu_headers(self) -> dict:
        return {"Authorization": f"Bearer {self.s.gpu_token}"} if self.s.gpu_token else {}

    def http_error(self, e: Exception) -> ServiceError:
        if isinstance(e, httpx.HTTPStatusError):
            return ServiceError(self.service, f"HTTP {e.response.status_code}: {e.response.text[:200]}",
                                status=e.response.status_code)
        if isinstance(e, httpx.TimeoutException):
            return ServiceError(self.service, "timeout", timeout=True)
        if isinstance(e, httpx.HTTPError):
            return ServiceError(self.service, f"{type(e).__name__}: {e}"[:300], status=503)
        return ServiceError(self.service, f"{type(e).__name__}: {e}"[:300])


@dataclass
class Clients:
    llm: "LLM"
    cosmos: "Cosmos"
    embed: "Embed"
    yolo: "Yolo"
    canary: "Canary"
    vss: "VSSClient"
    media: "Media"
    mode: str = "live"


def build_clients(s: Settings | None = None) -> Clients:
    """Live clients when s.mode == 'live'; otherwise the deterministic fixture fakes (zero network, zero credentials)."""
    from perjury.config import settings as _settings
    s = s or _settings()
    if s.mode != "live":
        from perjury import fakes
        return fakes.build_fakes(s)
    from perjury.canary import Canary
    from perjury.cosmos import Cosmos
    from perjury.embed import Embed
    from perjury.llm import LLM
    from perjury.media import Media
    from perjury.vss import VSSClient
    from perjury.yolo import Yolo
    vss = VSSClient(s)
    return Clients(llm=LLM(s), cosmos=Cosmos(s), embed=Embed(s), yolo=Yolo(s), canary=Canary(s), vss=vss,
                   media=Media(s, vss=vss), mode="live")
