"""Weave observability, optional. `op(name)` is weave.op when weave is importable and enabled, else a no-op.

Every PERJURY step is decorated with @op(...) so traces land in Weave on the VM/pod (§5a #10);
offline/tests run without weave or a key.
"""
from __future__ import annotations

import os
import re
from typing import Any, Callable

_B64 = re.compile(r"data:[\w/+.-]+;base64,[A-Za-z0-9+/=]{64,}")
_SECRET_KEYS = {"authorization", "api_key", "password", "token", "secret", "secret_key", "access_key", "gpu_bearer_token"}

_weave = None
_inited = False


def redact(v: Any) -> Any:
    """Strip bytes, base64 data URIs and secret-looking keys before anything leaves the process (Weave, UI ribbon)."""
    if isinstance(v, (bytes, bytearray)):
        return f"<{len(v)} bytes>"
    if isinstance(v, str):
        v = _B64.sub(lambda m: m.group(0)[:30] + f"…<{len(m.group(0))} chars>", v)
        return v if len(v) <= 4000 else v[:4000] + f"…<{len(v)} chars>"
    if isinstance(v, dict):
        return {k: ("<redacted>" if str(k).lower() in _SECRET_KEYS else redact(x)) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [redact(x) for x in v[:200]]
    return v


def _redact_inputs(inputs: dict) -> dict:
    return {k: redact(v) for k, v in inputs.items() if k not in ("self", "bus", "ctx")}


def init(project: str | None = None) -> bool:
    """Call once at app/bench start. Returns True when Weave tracing is live."""
    global _weave, _inited
    if _inited:
        return _weave is not None
    _inited = True
    if os.getenv("PERJURY_WEAVE", "1") == "0" or not os.getenv("WANDB_API_KEY"):
        return False
    try:
        import weave  # noqa: WPS433
        weave.init(project or os.getenv("WANDB_PROJECT", "perjury"))
        _weave = weave
        return True
    except Exception as e:  # never let tracing break a verdict
        print(f"[perjury] weave disabled: {type(e).__name__}")
        return False


def op(name: str | None = None) -> Callable:
    """Decorator usable before init(): binds to weave lazily if available at import time."""
    def deco(fn):
        try:
            import weave  # noqa: WPS433
            if os.getenv("PERJURY_WEAVE", "1") == "0":
                return fn
            return weave.op(name=name or fn.__name__, postprocess_inputs=_redact_inputs)(fn)
        except Exception:
            return fn
    return deco


def enabled() -> bool:
    return _weave is not None


def current_call_url() -> str | None:
    """Best-effort link to the current Weave trace for the receipt."""
    if _weave is None:
        return None
    try:
        call = _weave.require_current_call()
        return getattr(call, "ui_url", None)
    except Exception:
        return None
