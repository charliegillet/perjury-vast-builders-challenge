"""Canary-1B testimony ASR (§10): multipart POST /v1/audio/transcriptions. Health is /v1/health/ready only
(/v1/models is 404 on this NIM). Model id is ambiguous: try nvidia/canary-1b -> no model field -> canary-1b, keep the
first variant that returns text. PERJURY_CANARY_LANGUAGE=en adds a language field ([A] at G4).
"""
from __future__ import annotations

import time

from perjury.clients import HttpBase, ServiceError, ribbon
from perjury.config import Settings
from perjury.obs import op

MODEL_VARIANTS: tuple[str | None, ...] = ("nvidia/canary-1b", None, "canary-1b")


class Canary(HttpBase):
    service = "canary"

    def __init__(self, s: Settings):
        super().__init__(s, timeout=30.0)
        self.variant: str | None | bool = False   # False = not yet found; None = "send no model field"
        self.language = s.env.get("PERJURY_CANARY_LANGUAGE", "")

    async def health(self) -> bool:
        if not self.s.canary_url:
            return False
        try:
            r = await self.http().get(f"{self.s.canary_url}/v1/health/ready", headers=self.gpu_headers(), timeout=10)
            return r.status_code == 200
        except Exception:
            return False

    async def _post(self, wav: bytes, model: str | None) -> dict:
        data = {}
        if model:
            data["model"] = model
        if self.language:
            data["language"] = self.language
        r = await self.http().post(f"{self.s.canary_url}/v1/audio/transcriptions", headers=self.gpu_headers(),
                                   files={"file": ("claim.wav", wav, "audio/wav")}, data=data)
        r.raise_for_status()
        try:
            out = r.json()
        except ValueError:
            return {"text": r.text.strip()}
        return out if isinstance(out, dict) else {"text": str(out)}

    @op("canary_transcribe")
    async def transcribe(self, wav: bytes, *, bus=None) -> dict:
        """{"text", "model_id", "latency_ms"}. Raises ServiceError when no variant returns text."""
        if not self.s.canary_url:
            raise ServiceError(self.service, "CANARY_1B_URL not set")
        variants = [self.variant] if self.variant is not False else list(MODEL_VARIANTS)
        errors = []
        with ribbon(bus, self.service, gpu=True, request={"file": wav, "language": self.language or None}) as call:
            t0 = time.monotonic()
            for v in variants:
                try:
                    out = await self._post(wav, v)  # type: ignore[arg-type]
                except Exception as e:
                    errors.append(f"{v or 'no-model'}: {self.http_error(e)}")
                    continue
                text = (out.get("text") or out.get("transcript") or "").strip()
                if text:
                    self.variant = v
                    res = {"text": text, "model_id": v or "(default)", "latency_ms": int((time.monotonic() - t0) * 1000)}
                    call.note, call.response = f"model={res['model_id']}", res
                    return res
                errors.append(f"{v or 'no-model'}: empty text")
            self.variant = False   # re-probe all variants next time
            raise ServiceError(self.service, "; ".join(errors)[:300])
