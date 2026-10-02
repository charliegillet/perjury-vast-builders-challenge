"""nw-verifier backends: Cosmos-Reason2 NIM (primary) + Gemini (drop-in fallback) behind a circuit breaker.

verify(clip_bytes, camera_ctx) -> Verdict. Canonical box_2d = [ymin, xmin, ymax, xmax], 0-1000 (Gemini order).
Env: COSMOS3_REASON_URL + COSMOS3_REASON_MODEL + GPU_BEARER_TOKEN (event VM; or override with COSMOS_NIM_URL / COSMOS_MODEL / COSMOS_API_KEY), GEMINI_API_KEY,
GEMINI_MODEL, GEMINI_FPS, GEMINI_THINKING, GEMINI_API_MODE, COSMOS_TIMEOUT_S, GEMINI_TIMEOUT_S, CB_FAILS, CB_COOLDOWN_MIN. No secrets in code.
"""
from __future__ import annotations
import base64, json, os, re, shutil, subprocess, tempfile, threading, time
from typing import Literal, Optional
from pydantic import BaseModel, Field, ValidationError

try:
    import weave
except ImportError:  # keep the function importable without weave
    class _NoWeave:
        def op(self, fn=None, **_):
            return fn if fn else (lambda f: f)
        def attributes(self, _):
            import contextlib; return contextlib.nullcontext()
    weave = _NoWeave()

def _redact(inputs: dict) -> dict:  # never ship raw video bytes into Weave traces
    return {k: (f"<{len(v)} bytes>" if isinstance(v, (bytes, bytearray)) else v) for k, v in inputs.items()}


SEV_TO_INT = {"low": 2, "med": 3, "high": 4}  # maps onto FINAL-IDEA's 1-5 scale; pusher fires on >= 4


class VerdictOut(BaseModel):
    """Exactly what the model must emit (also the Gemini response schema)."""
    escalate: bool
    event: str = Field(description="Short event label, e.g. equipment_removed, person_passing, lighting_change")
    severity: Literal["low", "med", "high"]
    reason: str = Field(description="<= 20 words, plain English")
    box_2d: Optional[list[int]] = Field(None, min_length=4, max_length=4,
                                        description="[ymin, xmin, ymax, xmax] normalized 0-1000, or null")


class Verdict(VerdictOut):
    backend: str = ""
    model: str = ""
    latency_ms: int = 0


class BackendError(Exception):
    def __init__(self, msg: str, status: Optional[int] = None, timeout: bool = False):
        super().__init__(msg); self.status, self.timeout = status, timeout

    @property
    def hard(self) -> bool:  # trips the breaker immediately: timeout, 404, any 5xx
        return self.timeout or self.status == 404 or (self.status or 0) >= 500


# ---------- bbox helpers ----------
def _clamp(v: float) -> int:
    return int(max(0, min(1000, round(v))))

def xyxy_to_box2d(b: list, scale: float = 1000.0) -> Optional[list[int]]:
    """Cosmos/Qwen3-VL bbox_2d [x1,y1,x2,y2] (0-scale) -> canonical [ymin,xmin,ymax,xmax] 0-1000."""
    if not b or len(b) != 4:
        return None
    x1, y1, x2, y2 = (float(v) * 1000.0 / scale for v in b)
    return [_clamp(min(y1, y2)), _clamp(min(x1, x2)), _clamp(max(y1, y2)), _clamp(max(x1, x2))]

def box2d_to_pixels(box: list[int], width: int, height: int) -> tuple[int, int, int, int]:
    """Canonical box_2d -> pixel (x1, y1, x2, y2) for drawing on the Slack keyframe."""
    ymin, xmin, ymax, xmax = box
    return (int(xmin / 1000 * width), int(ymin / 1000 * height), int(xmax / 1000 * width), int(ymax / 1000 * height))


# ---------- prompt ----------
def build_prompt(ctx: dict, box_hint: str) -> str:
    return (
        f"You are a night-shift video verifier for camera {ctx.get('camera_id', '?')} ({ctx.get('camera_context', '')}).\n"
        "A statistical baseline flagged this 5-second clip as unusual for this camera.\n"
        f"What is normal here: {ctx.get('baseline_summary', 'unknown')}\n"
        f"Why it was flagged: embed_dist={ctx.get('dist')} (p99={ctx.get('p99')}); class deltas={ctx.get('class_deltas', {})}.\n"
        "Escalate only if a person interacts with, removes, or damages property, or someone is at risk. "
        "Passing through is not an event. Lighting changes and camera noise are not events.\n"
        f"Output JSON with keys escalate (bool), event (short snake_case label), severity (low|med|high), "
        f"reason (<=20 words), {box_hint}"
    )

def _parse_json(text: str) -> dict:
    text = re.sub(r"<think>.*?</think>", "", text or "", flags=re.S)
    m = re.search(r"\{.*\}", text, flags=re.S)  # outermost object; tolerate ```json fences / chatter
    if not m:
        raise BackendError("no JSON in model output")
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError as e:
        raise BackendError(f"bad JSON: {e}") from e


# ---------- backends ----------
class CosmosNIMBackend:
    name = "cosmos"

    def __init__(self):
        from openai import OpenAI  # NIM is OpenAI-compatible; weave autopatches this client
        # Event VM (/config/<team>.config) provides COSMOS3_REASON_URL / COSMOS3_REASON_MODEL / GPU_BEARER_TOKEN;
        # COSMOS_NIM_URL / COSMOS_MODEL / COSMOS_API_KEY override them.
        self.model = os.getenv("COSMOS_MODEL") or os.getenv("COSMOS3_REASON_MODEL", "nvidia/cosmos3-reason")
        self.timeout = float(os.getenv("COSMOS_TIMEOUT_S", "20"))
        self.scale = float(os.getenv("COSMOS_BBOX_SCALE", "1000"))  # Qwen-family sometimes 1024; verify on-site
        self.fps = os.getenv("COSMOS_FPS")  # unset = NIM default (4 fps)
        base_url = os.getenv("COSMOS_NIM_URL") or os.environ["COSMOS3_REASON_URL"].rstrip("/") + "/v1"
        api_key = os.getenv("COSMOS_API_KEY") or os.getenv("GPU_BEARER_TOKEN", "not-used")
        self.client = OpenAI(base_url=base_url, api_key=api_key,
                             timeout=self.timeout, max_retries=0)

    @weave.op(name="cosmos_verify", postprocess_inputs=_redact)
    def verify(self, clip_bytes: bytes, camera_ctx: dict) -> Verdict:
        import openai
        prompt = build_prompt(camera_ctx, 'bbox_2d ([x1,y1,x2,y2] 0-1000 around the key object/person, or null).') + (
            "\nAnswer in the format: <think>\nyour reasoning\n</think>\n\nthen ONLY the JSON object.")
        b64 = base64.b64encode(clip_bytes).decode()
        extra = {"media_io_kwargs": {"video": {"fps": float(self.fps)}}} if self.fps else None
        t0 = time.monotonic()
        try:
            r = self.client.chat.completions.create(
                model=self.model, max_tokens=1024, temperature=0.2, extra_body=extra,
                messages=[{"role": "user", "content": [
                    {"type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{b64}"}},
                    {"type": "text", "text": prompt}]}])
        except openai.APITimeoutError as e:
            raise BackendError("cosmos timeout", timeout=True) from e
        except openai.APIStatusError as e:
            raise BackendError(f"cosmos HTTP {e.status_code}", status=e.status_code) from e
        except openai.APIConnectionError as e:
            raise BackendError(f"cosmos connection: {e}", status=503) from e
        d = _parse_json(r.choices[0].message.content)
        d["box_2d"] = xyxy_to_box2d(d.pop("bbox_2d", None) or d.pop("evidence_bbox", None), self.scale)
        try:
            out = VerdictOut(**d)
        except ValidationError as e:
            raise BackendError(f"cosmos schema mismatch: {e.errors()[:2]}") from e
        return Verdict(**out.model_dump(), backend=self.name, model=self.model,
                       latency_ms=int((time.monotonic() - t0) * 1000))


def _has_audio_track(mp4: bytes) -> bool:
    return re.search(rb"hdlr.{8}soun", mp4, flags=re.S) is not None  # 'hdlr' box, handler_type 'soun'

def _add_silent_audio(mp4: bytes) -> Optional[bytes]:
    """Gemini 3 has returned 404/500 on video with no audio stream; remux with a silent track (video copied)."""
    if not shutil.which("ffmpeg"):
        return None
    with tempfile.TemporaryDirectory() as d:
        src, dst = os.path.join(d, "in.mp4"), os.path.join(d, "out.mp4")
        open(src, "wb").write(mp4)
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-f", "lavfi", "-i", "anullsrc=r=16000:cl=mono",
               "-c:v", "copy", "-c:a", "aac", "-shortest", dst]
        ok = subprocess.run(cmd, timeout=10).returncode == 0
        return open(dst, "rb").read() if ok else None


class GeminiBackend:
    """Interactions API (GA Jun 2026, recommended) when the SDK has it; legacy generateContent otherwise.
    Weave autopatches only generate_content, so the @weave.op below is what traces the interactions path."""
    name = "gemini"

    def __init__(self):
        from google import genai
        from google.genai import types
        self.types = types
        self.model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
        self.fps = float(os.getenv("GEMINI_FPS", "2"))  # static mode only; (0, 24]
        lvl = os.getenv("GEMINI_THINKING", "minimal")
        self.thinking = "low" if (lvl == "minimal" and "3.8" in self.model) else lvl  # 3.8 Flash rejects minimal
        self.timeout_s = float(os.getenv("GEMINI_TIMEOUT_S", "15"))
        retry = types.HttpRetryOptions(attempts=2, initial_delay=0.5, max_delay=2.0,
                                       http_status_codes=[408, 429, 500, 502, 503, 504])  # gc default = no retry
        self.client = genai.Client(api_key=os.environ["GEMINI_API_KEY"], http_options=types.HttpOptions(
            timeout=int(self.timeout_s * 1000), retry_options=retry))
        mode = os.getenv("GEMINI_API_MODE", "interactions")
        self.mode = mode if (mode != "interactions" or hasattr(self.client, "interactions")) else "generate_content"

    def _interactions(self, clip: bytes, prompt: str, high_res: bool) -> str:
        r = self.client.interactions.create(
            model=self.model, store=False, timeout=self.timeout_s,  # store=False: no server-side retention
            input=[{"type": "video", "data": base64.b64encode(clip).decode(), "mime_type": "video/mp4",
                    "processing": {"type": "static", "fps": self.fps}, "resolution": "high" if high_res else "low"},
                   {"type": "text", "text": prompt}],  # text after the video
            response_format={"type": "text", "mime_type": "application/json", "schema": VerdictOut.model_json_schema()},
            generation_config={"thinking_level": self.thinking})
        return r.output_text or ""

    def _generate_content(self, clip: bytes, prompt: str, high_res: bool) -> str:
        t = self.types
        cfg = t.GenerateContentConfig(
            response_mime_type="application/json", response_json_schema=VerdictOut.model_json_schema(),
            thinking_config=t.ThinkingConfig(thinking_level=self.thinking),
            media_resolution=t.MediaResolution.MEDIA_RESOLUTION_HIGH if high_res else t.MediaResolution.MEDIA_RESOLUTION_LOW)
        parts = [t.Part(inline_data=t.Blob(data=clip, mime_type="video/mp4"), video_metadata=t.VideoMetadata(fps=self.fps)),
                 t.Part(text=prompt)]
        return self.client.models.generate_content(model=self.model, contents=[t.Content(role="user", parts=parts)],
                                                   config=cfg).text or ""

    @weave.op(name="gemini_verify", postprocess_inputs=_redact)
    def verify(self, clip_bytes: bytes, camera_ctx: dict) -> Verdict:
        high_res = False  # Gemini 3 404s/500s on video with no audio stream unless resolution=high
        if not _has_audio_track(clip_bytes):
            fixed = _add_silent_audio(clip_bytes)
            clip_bytes, high_res = (fixed, False) if fixed else (clip_bytes, True)
        if len(clip_bytes) > 19_000_000:
            raise BackendError("clip too large for inline (20 MB request cap)", status=413)
        prompt = build_prompt(camera_ctx, "box_2d ([ymin,xmin,ymax,xmax] normalized 0-1000 around the key object/person, or null).")
        t0 = time.monotonic()
        try:
            call = self._interactions if self.mode == "interactions" else self._generate_content
            text = call(clip_bytes, prompt, high_res)
        except Exception as e:  # google.genai.errors.APIError (.code) | interactions APIStatusError (.status_code) | httpx
            status = getattr(e, "code", None) or getattr(e, "status_code", None)
            is_timeout = "timeout" in type(e).__name__.lower() or "timed out" in str(e).lower()
            raise BackendError(f"gemini {self.mode} {status or type(e).__name__}: {str(e)[:200]}",
                               status=status if isinstance(status, int) else 503, timeout=is_timeout) from e
        try:
            out = VerdictOut.model_validate_json(text)
        except ValidationError as e:  # empty text = safety block / truncation
            raise BackendError(f"gemini bad output: {text[:120]!r}") from e
        return Verdict(**out.model_dump(), backend=self.name, model=f"{self.model}/{self.mode}",
                       latency_ms=int((time.monotonic() - t0) * 1000))


# ---------- circuit-breaker router ----------
class VerifierRouter:
    """Closed: Cosmos. Hard error (timeout/404/5xx) or CB_FAILS consecutive soft errors -> open for
    CB_COOLDOWN_MIN minutes (all traffic to Gemini). After cooldown, one half-open probe goes to Cosmos."""

    def __init__(self, primary=None, fallback=None):
        self.primary, self.fallback = primary or CosmosNIMBackend(), fallback or GeminiBackend()
        self.max_fails = int(os.getenv("CB_FAILS", "3"))
        self.cooldown_s = float(os.getenv("CB_COOLDOWN_MIN", "5")) * 60
        self.fails, self.open_until, self.lock = 0, 0.0, threading.Lock()

    @property
    def state(self) -> str:
        return "open" if time.time() < self.open_until else ("half_open" if self.open_until else "closed")

    def _trip(self, why: str):
        with self.lock:
            self.open_until, self.fails = time.time() + self.cooldown_s, 0
        print(f"[nw-verifier] breaker OPEN for {self.cooldown_s:.0f}s: {why}")

    def _call(self, backend, clip: bytes, ctx: dict, state: str) -> Verdict:
        with weave.attributes({"backend": backend.name, "breaker_state": state, "camera_id": ctx.get("camera_id")}):
            return backend.verify(clip, ctx)

    @weave.op(name="nw_verify", postprocess_inputs=_redact)
    def verify(self, clip_bytes: bytes, camera_ctx: dict) -> Verdict:
        state = self.state
        if state != "open":
            try:
                v = self._call(self.primary, clip_bytes, camera_ctx, state)
                with self.lock:
                    self.fails, self.open_until = 0, 0.0  # success closes (incl. half-open probe)
                return v
            except BackendError as e:
                with self.lock:
                    self.fails += 1
                    trip = e.hard or self.fails >= self.max_fails or state == "half_open"
                if trip:
                    self._trip(str(e))
                print(f"[nw-verifier] cosmos failed ({e}); this clip -> gemini")
        return self._call(self.fallback, clip_bytes, camera_ctx, self.state)  # raises if Gemini also fails


_router: Optional[VerifierRouter] = None

def verify(clip_bytes: bytes, camera_ctx: dict) -> Verdict:
    """Module-level entry point used by the nw-verifier DataEngine handler (router built once per pod)."""
    global _router
    if _router is None:
        _router = VerifierRouter()
    return _router.verify(clip_bytes, camera_ctx)
