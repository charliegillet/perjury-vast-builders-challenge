"""SSE event bus for one testimony run (FINAL-IDEA-v3 §9), plus the JSONL recorder that replay mode re-emits.

Event names (data is a JSON object):
  run          {run_id, text, scene, mode}
  transcript   {text, source: "canary"|"typed", latency_ms}
  atoms        {atoms: [Atom], parser: "llm"|"rules"}
  t0           {atom_id, summary, data}                 RECORDS tier result for one atom
  t1           {atom_id, supports, contradicts, silent, snippets: [{id,cam,seg,text,label,quote}]}
  summon       {atom_id, probe, probe_version, jurors: [Juror]}
  juror        {atom_id, vote: Vote}                    one per juror as it lands
  ground       {atom_id, camera, panel, bbox_2d}
  zoom         {atom_id, camera, ok, label, conf, crop_box}
  atom_verdict {atom_verdict: AtomVerdict}
  verdict      {verdict, explanation}
  stock        {answer, classification, hits, latency_ms}
  service      {service, state: "firing"|"done"|"fallback"|"error", ms, n, note, request, response}
  receipt      {verdict, atoms, fired: [service], fired_count, total: 13, calls, elapsed_ms, gpu_s, weave_url, mode}
  error        {message}
  done         {}
"""
from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel

SERVICES = ("s3", "dataengine", "vastdb", "vss", "cosmos3", "embed1", "yolo", "canary",
            "wandb_inference", "weave", "coreweave", "cursor", "k8s")
BADGES = ("coreweave", "cursor")  # never count toward "fired" (§5a receipt rule)


def _plain(v: Any) -> Any:
    if isinstance(v, BaseModel):
        return v.model_dump(mode="json")
    if isinstance(v, dict):
        return {k: _plain(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_plain(x) for x in v]
    return v


class EventBus:
    """emit() is sync and never blocks; consumers iterate stream(). Every event is timestamped relative to t0."""

    def __init__(self, run_id: str, record_to: Optional[Path] = None):
        self.run_id = run_id
        self.t0 = time.monotonic()
        self.queue: asyncio.Queue = asyncio.Queue()
        self.events: list[dict] = []
        self.fired: dict[str, dict] = {}   # service -> {"n": calls, "ms": total_ms}
        self.calls = 0
        self.gpu_ms = 0
        self.record_to = record_to
        self.closed = False

    def emit(self, name: str, data: Optional[dict] = None) -> None:
        if self.closed:
            return
        ev = {"event": name, "t_ms": int((time.monotonic() - self.t0) * 1000), "data": _plain(data or {})}
        self.events.append(ev)
        self.queue.put_nowait(ev)
        if name == "done":
            self.closed = True
            if self.record_to:
                self.record_to.parent.mkdir(parents=True, exist_ok=True)
                with self.record_to.open("w") as f:
                    for e in self.events:
                        f.write(json.dumps(e) + "\n")

    def service(self, service: str, state: str, ms: int = 0, note: str = "", gpu: bool = False,
                request: Any = None, response: Any = None) -> None:
        """Ribbon chip update. Call with state='done' once per completed live call (counts toward the receipt)."""
        if state == "done":
            f = self.fired.setdefault(service, {"n": 0, "ms": 0})
            f["n"] += 1
            f["ms"] += ms
            self.calls += 1
            if gpu:
                self.gpu_ms += ms
        self.emit("service", {"service": service, "state": state, "ms": ms, "note": note,
                              "n": self.fired.get(service, {}).get("n", 0),
                              "request": request, "response": response})

    def fired_live(self) -> list[str]:
        return [s for s in self.fired if s not in BADGES]

    async def stream(self):
        while True:
            ev = await self.queue.get()
            yield ev
            if ev["event"] == "done":
                return


def sse_format(ev: dict) -> str:
    return f"event: {ev['event']}\ndata: {json.dumps({**ev['data'], '_t_ms': ev['t_ms']})}\n\n"


def load_recording(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
