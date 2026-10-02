"""VSS backend client (async port of lastframe/vss.py: login, 401 retry, rows(), normalize(); plus the endpoints PERJURY
needs). Credentials never leave this module; stream_url() carries the JWT in ?token= for <video>/ffmpeg only.
Service chips: "vss" (reads, agent) and "dataengine" (upload, suggestions).
"""
from __future__ import annotations

import asyncio
import math
import re
import time
import urllib.parse
from typing import Any, Optional

import httpx

from perjury.clients import HttpBase, ServiceError, ribbon
from perjury.config import Settings
from perjury.obs import op

STOCK_PROMPT = ("Is this statement about the footage true: '{claim}'? "
                "Start your answer with TRUE, FALSE or CANNOT TELL, then one sentence.")
_STOCK_RE = re.compile(r"^\W*(TRUE|FALSE|CANNOT\s+TELL|CAN'?T\s+TELL)\b", re.I)


def classify_stock(answer: str) -> str:
    """First token of the stock agent's answer -> TRUE | FALSE | CANNOT TELL | UNCLASSIFIED (hand-checked, §6).
    Same labels as perjury.probes.classify_stock."""
    # The stock agent wraps its answer in an Answer section even when asked to
    # start with the decision. Remove only that known heading, not later text.
    answer = re.sub(r"^\s*(?:\*\*Answer\*\*|#{1,6}\s+Answer)\s*\n+", "", answer or "", flags=re.I)
    m = _STOCK_RE.search(answer)
    if not m:
        return "UNCLASSIFIED"
    return re.sub(r"\s+", " ", m.group(1).upper()).replace("CAN'T", "CANNOT").replace("CANT", "CANNOT")


def rows(response) -> list:
    if isinstance(response, list):
        return response
    if isinstance(response, dict):
        for key in ("segments", "results", "videos", "items", "data", "suggestions", "chunks"):
            if isinstance(response.get(key), list):
                return response[key]
    raise ServiceError("vss", "unfamiliar list shape")


def _number(row: dict, *keys) -> Optional[float]:
    for key in keys:
        v = row.get(key)
        if isinstance(v, bool):
            continue
        try:
            n = float(v)
            if math.isfinite(n):
                return n
        except (TypeError, ValueError):
            pass
    return None


def normalize(row: dict, parent: str | None = None) -> dict:
    """Raw VSS segment row + the canonical keys (source, original_video, start, end, caption, camera_id, location)."""
    return {**row, "source": row.get("source"), "original_video": row.get("original_video") or parent,
            "start": _number(row, "start_sec", "start_time_sec", "segment_start_sec", "start_time", "start"),
            "end": _number(row, "end_sec", "end_time_sec", "segment_end_sec", "end_time", "end"),
            "caption": row.get("reasoning_content") or row.get("caption") or "",
            "camera_id": row.get("camera_id") or "unknown", "location": row.get("location") or "unknown"}


class VSSClient(HttpBase):
    service = "vss"

    def __init__(self, s: Settings):
        super().__init__(s, timeout=60.0)
        self.base = s.vss_url
        self.token: Optional[str] = s.env.get("VSS_TOKEN") or None

    @property
    def configured(self) -> bool:
        return bool(self.base and (self.token or (self.s.vss_user and self.s.vss_password)))

    def _login_body(self) -> dict:
        return {"username": self.s.vss_user, "password": self.s.vss_password}

    async def login(self) -> None:
        if not (self.base and self.s.vss_user and self.s.vss_password):
            raise ServiceError(self.service, "VSS not configured (INGRESS_URL/VSS_URL + credentials)")
        try:
            r = await self.http().post(self.base + "/api/v1/auth/login", json=self._login_body(), timeout=30)
            r.raise_for_status()
            self.token = r.json()["access_token"]
        except Exception as e:
            raise ServiceError(self.service, f"login failed ({type(e).__name__})") from e

    def login_sync(self) -> None:
        if not (self.base and self.s.vss_user and self.s.vss_password):
            raise ServiceError(self.service, "VSS not configured")
        try:
            r = httpx.post(self.base + "/api/v1/auth/login", json=self._login_body(), timeout=30)
            r.raise_for_status()
            self.token = r.json()["access_token"]
        except Exception as e:
            raise ServiceError(self.service, f"login failed ({type(e).__name__})") from e

    async def request(self, method: str, path: str, *, json: Any = None, params: dict | None = None,
                      files: dict | None = None, data: dict | None = None, timeout: float | None = None,
                      allow_404: bool = False) -> Any:
        if not self.configured:
            raise ServiceError(self.service, "VSS not configured")
        if not self.token:
            async with self.sem(1):   # one login per loop
                if not self.token:
                    await self.login()
        relogged = False
        for attempt in range(4):
            try:
                r = await self.http().request(method, self.base + path, json=json, params=params, files=files,
                                              data=data, headers={"Authorization": f"Bearer {self.token}"},
                                              timeout=timeout or self.timeout)
            except httpx.TimeoutException as e:
                raise ServiceError(self.service, f"{path} timeout", timeout=True) from e
            except httpx.HTTPError as e:
                if attempt < 2:
                    await asyncio.sleep(1.0 * (attempt + 1))
                    continue
                raise ServiceError(self.service, f"{path} unreachable ({type(e).__name__})", status=503) from e
            if r.status_code == 401 and not relogged and self.s.vss_user:
                relogged = True
                await self.login()
                continue
            if r.status_code in (502, 503) and attempt < 3:
                await asyncio.sleep(2.0 * (attempt + 1))
                continue
            if r.status_code == 404 and allow_404:
                return None
            if r.status_code >= 400:
                raise ServiceError(self.service, f"{path} HTTP {r.status_code}: {r.text[:200]}", status=r.status_code)
            return r.json() if r.content else {}
        raise ServiceError(self.service, f"{path} failed after retries", status=503)

    # ---- segments / playback ----
    async def detections(self, source) -> dict | None:
        """YOLO bbox sidecar for one segment, or None (404 = no sidecar)."""
        return await self.request("GET", "/api/v1/videos/detections", params={"source": source}, allow_404=True)

    def stream_url(self, source) -> str:
        if not self.token:
            self.login_sync()
        return f"{self.base}/api/v1/videos/stream?" + urllib.parse.urlencode({"source": source, "token": self.token})

    async def playback_url(self, source: str, expires: int = 3600) -> str:
        if not self.token:
            await self.login()
        d = await self.request("GET", "/api/v1/videos/playback-url",
                               params={"source": source, "token": self.token, "expires_in": expires})
        url = d.get("url") or d.get("playback_url") or d.get("presigned_url") if isinstance(d, dict) else d
        if not isinstance(url, str) or not url:
            raise ServiceError(self.service, "playback-url returned no url")
        return url

    async def segments(self, original_video) -> list[dict]:
        resp = await self.request("GET", "/api/v1/tools/segments", params={"original_video": original_video})
        out = [normalize(r, original_video) for r in rows(resp) if isinstance(r, dict)]
        return sorted([r for r in out if r["source"] and r["start"] is not None], key=lambda r: r["start"])

    async def explore(self, limit=48, offset=0) -> dict:
        return await self.request("GET", "/api/v1/videos/explore",
                                  params={"scope": "all", "limit": limit, "offset": offset})

    # ---- agent / synthesis ----
    @op("vss_search_and_answer")
    async def search_and_answer(self, claim: str, camera_id: str, *, bus=None) -> dict:
        """Stock A/B (§6, exact text). Returns {answer, classification, hits, latency_ms, query, evidence}."""
        body = {"query": STOCK_PROMPT.format(claim=claim), "metadata_filters": {"camera_id": camera_id},
                "top_k": 10, "min_similarity": 0.1}
        with ribbon(bus, self.service, request=body) as call:
            call.note = "stock search-and-answer"
            t0 = time.monotonic()
            d = await self.request("POST", "/api/v1/agent/search-and-answer", json=body, timeout=120)
            answer = (d.get("answer") or d.get("llm_synthesis") or "") if isinstance(d, dict) else str(d)
            ev = (d.get("evidence") or {}) if isinstance(d, dict) else {}
            chunks = ev.get("chunks") if isinstance(ev, dict) else ev if isinstance(ev, list) else []
            out = {"answer": answer, "classification": classify_stock(answer), "hits": len(chunks or []),
                   "latency_ms": int((time.monotonic() - t0) * 1000), "query": body["query"],
                   "evidence": [{k: c.get(k) for k in ("original_video", "similarity_score", "best_match_start_sec",
                                                       "best_match_end_sec", "preview_source")}
                                for c in (chunks or [])[:10] if isinstance(c, dict)]}
            call.response = {k: out[k] for k in ("answer", "classification", "hits")}
            return out

    @op("vss_ask")
    async def ask(self, question, original_video=None, *, bus=None) -> dict:
        body = {"question": question, "top_k": 10}
        if original_video:
            body["original_video"] = original_video
        with ribbon(bus, self.service, request=body) as call:
            d = await self.request("POST", "/api/v1/agent/ask", json=body, timeout=120)
            call.response = {"answer": (d or {}).get("answer"), "tool_used": (d or {}).get("tool_used")}
            return d

    @op("vss_synthesize")
    async def synthesize(self, original_video, question="Summarize what happens in this video", max_segments=20, *,
                         bus=None) -> dict:
        body = {"original_video": original_video, "question": question, "max_segments": max_segments}
        with ribbon(bus, self.service, request=body) as call:
            d = await self.request("POST", "/api/v1/videos/synthesize", json=body, timeout=180)
            call.response = {"answer": (d or {}).get("answer"), "segment_count": (d or {}).get("segment_count")}
            return d

    async def suggestions(self, *, bus=None) -> list[dict]:
        with ribbon(bus, "dataengine", request={"path": "suggestions"}) as call:
            d = await self.request("GET", "/api/v1/suggestions")
            if isinstance(d, list):
                out = [x if isinstance(x, dict) else {"text": x} for x in d]
            else:
                out = []
                for k, v in (d or {}).items():
                    if isinstance(v, list):
                        out += [{**x, "kind": k} if isinstance(x, dict) else {"text": x, "kind": k} for x in v]
            call.response, call.note = {"n": len(out)}, "prompt-suggester"
            return out

    async def dashboard_stats(self, *, bus=None) -> dict:
        with ribbon(bus, self.service, request={"path": "dashboard/stats"}) as call:
            d = await self.request("GET", "/api/v1/dashboard/stats", params={"scope": "all"})
            call.response = (d or {}).get("overview")
            return d

    @op("vss_upload")
    async def upload(self, mp4: bytes, filename: str, metadata: dict, *, bus=None) -> dict:
        """videos/upload (multipart) -> DataEngine ingest. The only way PERJURY puts an mp4 into the pipeline."""
        form = {k: (str(v).lower() if isinstance(v, bool) else ",".join(map(str, v)) if isinstance(v, (list, tuple))
                    else str(v)) for k, v in (metadata or {}).items() if v is not None and v != ""}
        with ribbon(bus, "dataengine", request={"filename": filename, "bytes": len(mp4), **form}) as call:
            d = await self.request("POST", "/api/v1/videos/upload", files={"file": (filename, mp4, "video/mp4")},
                                   data=form, timeout=180)
            call.response, call.note = d, "upload -> DataEngine"
            return d
