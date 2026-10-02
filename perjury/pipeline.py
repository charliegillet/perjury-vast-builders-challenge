"""testify(): one statement -> atoms -> tiers -> quorum -> claim verdict, streamed as SSE events (FINAL-IDEA-v3 §5, §9).

Event order: run, transcript, atoms, then per atom any of t0/t1/summon/juror/ground/zoom and atom_verdict (atoms run
concurrently; 20 s cap per atom, 8 s per juror), then verdict, (stock), receipt, done. `done` is always emitted,
after `error` if something broke. The verdict is computed by code (perjury/quorum.py); no LLM writes it.
"""
from __future__ import annotations

import asyncio
import json
import time
import uuid
from dataclasses import dataclass
from typing import Any, Optional

from perjury import obs
from perjury.atomize import atomize
from perjury.config import Settings, settings as get_settings
from perjury.events import BADGES, SERVICES, EventBus
from perjury.index import SceneIndex
from perjury.probes import stock_query
from perjury.vss import classify_stock
from perjury.quorum import claim_verdict
from perjury.router import FIXTURE_PROMOTION_PATH, PROMOTION_PATH, Router
from perjury.tiers import RunOpts, evaluate, unverifiable
from perjury.types import Atom, AtomVerdict, ClaimVerdict
from perjury.verdict import explain_claim

STOCK_TIMEOUT_S = 30.0


@dataclass
class Context:
    settings: Settings
    clients: Any            # perjury.clients.Clients
    index: SceneIndex
    probes: dict
    router: Router


def _load_json(path) -> dict:
    try:
        return json.loads(path.read_text()) if path.exists() else {}
    except (OSError, ValueError):
        return {}


def load_context(s: Settings | None = None) -> Context:
    from perjury.clients import build_clients   # imported lazily: clients pull in httpx/ffmpeg
    s = s or get_settings()
    return Context(settings=s, clients=build_clients(s), index=SceneIndex.load(s.index_path),
                   probes=_load_json(s.probes_path),
                   router=Router(promotion_path=PROMOTION_PATH if s.mode == "live" else FIXTURE_PROMOTION_PATH))


def new_run_id() -> str:
    return f"r{time.strftime('%H%M%S')}-{uuid.uuid4().hex[:6]}"


def _mode(ctx: Context) -> str:
    return ctx.settings.mode if ctx.settings.mode in ("live", "fixture", "replay") else "live"


# ---- per-atom processing ----
def _acyclic_parents(atoms: list[Atom]) -> dict[str, Optional[str]]:
    """depends_on, with unknown ids and cycles removed (a cycle would deadlock the parent wait)."""
    ids = {a.id for a in atoms}
    parent = {a.id: (a.depends_on if a.depends_on in ids and a.depends_on != a.id else None) for a in atoms}
    for a in atoms:
        seen, p = {a.id}, parent[a.id]
        while p is not None:
            if p in seen:
                parent[a.id] = None
                break
            seen.add(p)
            p = parent[p]
    return parent


def _moot(atom: Atom, parent: Atom) -> AtomVerdict:
    return AtomVerdict(atom_id=atom.id, verdict="MOOT", reason=f"Moot: “{parent.span}” was contradicted.",
                       reason_code="moot", stats={"parent": parent.id, "pill": "moot"})


async def _run_atoms(atoms: list[Atom], scene: int, ctx: Context, bus: EventBus, opts: RunOpts) -> list[AtomVerdict]:
    parents = _acyclic_parents(atoms)
    by_id = {a.id: a for a in atoms}
    tasks: dict[str, asyncio.Task] = {}

    async def one(atom: Atom) -> AtomVerdict:
        pid = parents[atom.id]
        if pid is not None:
            pv = await tasks[pid]
            if pv.verdict in ("CONTRADICTED", "MOOT"):
                av = _moot(atom, by_id[pid])
                bus.emit("atom_verdict", {"atom_verdict": av})
                return av
        route = ctx.router.route(atom, k=opts.jury_size)
        try:
            av = await asyncio.wait_for(evaluate(atom, route, scene, ctx, bus, opts), timeout=ctx.settings.atom_timeout_s)
        except asyncio.TimeoutError:
            av = unverifiable(atom, "The jury timed out; no verdict is guessed.", "jury_timeout")
        except Exception as e:  # one broken atom must not sink the claim; it is UNVERIFIABLE with the reason
            av = unverifiable(atom, f"Internal error while testing this atom ({type(e).__name__}).", "error")
        av.stats.setdefault("route", {"rule": route.rule, "tiers": route.tiers, "hard": route.hard,
                                      "promoted": route.promoted})
        bus.emit("atom_verdict", {"atom_verdict": av})
        return av

    for a in atoms:
        tasks[a.id] = asyncio.create_task(one(a))
    return list(await asyncio.gather(*tasks.values()))


# ---- stock VSS agent A/B (§6) ----
async def _stock(text: str, ctx: Context, bus: EventBus) -> dict:
    t = time.monotonic()
    try:
        r = await asyncio.wait_for(ctx.clients.vss.search_and_answer(text, ctx.settings.camera_id, bus=bus),
                                   timeout=STOCK_TIMEOUT_S)
        r = r if isinstance(r, dict) else {"answer": str(r)}
        answer = r.get("answer") or r.get("response") or r.get("text") or ""
        hits = r.get("hits")
        if hits is None:
            hits = len(r.get("results") or r.get("clips") or r.get("sources") or [])
        return {"answer": answer, "classification": classify_stock(answer), "hits": hits,
                "latency_ms": int((time.monotonic() - t) * 1000), "query": stock_query(text)}
    except Exception as e:
        return {"answer": None, "classification": "ERROR", "hits": 0, "error": obs.redact(str(e))[:400],
                "latency_ms": int((time.monotonic() - t) * 1000), "query": stock_query(text)}


def _pipeline_chips(atoms: list[AtomVerdict], ctx: Context, bus: EventBus) -> None:
    """Outlined chips (§9 ribbon): we READ the pipeline's YOLO/VastDB output via the index snapshot. State
    'pipeline' never counts toward 'fired'. Weave and K8s count only when they really served this run."""
    if any(t == "RECORDS" for av in atoms for t in av.tiers):
        bus.service("vastdb", "pipeline", note=f"T0 over index snapshot ({ctx.index.source}, {len(ctx.index)} segments)")
        bus.service("yolo", "pipeline", note="pipeline YOLO classes / counts / persistence")
    if obs.enabled():
        bus.service("weave", "done", note="trace")
    if ctx.settings.pod_name:
        bus.service("k8s", "done", note=ctx.settings.pod_name)


def _receipt(cv: ClaimVerdict, bus: EventBus, ctx: Context, elapsed_ms: int) -> dict:
    fired = bus.fired_live()
    return {"run_id": cv.run_id, "verdict": cv.verdict, "atoms": len(cv.atoms), "fired": fired,
            "fired_count": len(fired), "total": len(SERVICES), "badges": list(BADGES), "calls": bus.calls,
            "elapsed_ms": elapsed_ms, "gpu_s": round(bus.gpu_ms / 1000, 1), "weave_url": obs.current_call_url(),
            "mode": cv.mode, "parser": cv.parser}


# ---- entry points ----
@obs.op("perjury.testify")
async def testify(text: str, scene: int, ctx: Context, bus: EventBus, *, transcript_source: str = "typed",
                  stock_ab: bool = False, jury_size: int | None = None, probe_overrides: dict | None = None,
                  transcript_latency_ms: int = 0) -> ClaimVerdict:
    """Run one testimony end to end. probe_overrides (bench): see tiers.RunOpts."""
    t0 = time.monotonic()
    mode = _mode(ctx)
    opts = RunOpts(run_id=bus.run_id, claim=text, jury_size=jury_size or ctx.settings.jury_size,
                   juror_timeout_s=ctx.settings.juror_timeout_s, probe_overrides=dict(probe_overrides or {}))
    atoms: list[Atom] = []
    parser = "rules"
    cv: Optional[ClaimVerdict] = None
    try:
        bus.emit("run", {"run_id": bus.run_id, "text": text, "scene": scene, "mode": mode,
                         "jury_size": opts.jury_size})
        bus.emit("transcript", {"text": text, "source": transcript_source, "latency_ms": transcript_latency_ms})
        atoms, parser = await atomize(text, ctx.clients.llm, bus=bus)
        routes = {a.id: (lambda r: {"rule": r.rule, "tiers": r.tiers, "hard": r.hard, "promoted": r.promoted})(
            ctx.router.route(a, k=opts.jury_size)) for a in atoms}
        bus.emit("atoms", {"atoms": atoms, "parser": parser, "routes": routes})
        stock_task = asyncio.create_task(_stock(text, ctx, bus)) if stock_ab else None
        avs = await _run_atoms(atoms, scene, ctx, bus, opts)
        label = claim_verdict(avs, atoms)
        explanation = explain_claim(label, atoms, avs)
        bus.emit("verdict", {"verdict": label, "explanation": explanation, "run_id": bus.run_id})
        if stock_task:
            bus.emit("stock", await stock_task)
        _pipeline_chips(avs, ctx, bus)
        elapsed = int((time.monotonic() - t0) * 1000)
        cv = ClaimVerdict(run_id=bus.run_id, text=text, scene=scene, verdict=label, explanation=explanation,
                          atoms=atoms, atom_verdicts=avs, parser=parser, elapsed_ms=elapsed,
                          gpu_s=round(bus.gpu_ms / 1000, 1), services_fired=bus.fired_live(), calls=bus.calls,
                          mode=mode)
        bus.emit("receipt", _receipt(cv, bus, ctx, elapsed))
    except Exception as e:
        bus.emit("error", {"message": f"{type(e).__name__}: {str(e)[:300]}"})
        if cv is None:
            cv = ClaimVerdict(run_id=bus.run_id, text=text, scene=scene, verdict="UNPROVEN",
                              explanation=f"Internal error ({type(e).__name__}); no verdict is guessed.", atoms=atoms,
                              atom_verdicts=[], parser=parser, elapsed_ms=int((time.monotonic() - t0) * 1000),
                              gpu_s=round(bus.gpu_ms / 1000, 1), services_fired=bus.fired_live(), calls=bus.calls,
                              mode=mode)
    finally:
        bus.emit("done", {})
    return cv


_CTX: Optional[Context] = None


def get_context() -> Context:
    """Process-wide context (agent tool, bench)."""
    global _CTX
    if _CTX is None:
        _CTX = load_context()
    return _CTX


async def verify(claim: str, scene: int, ctx: Context | None = None, *, stock_ab: bool = False,
                 jury_size: int | None = None, probe_overrides: dict | None = None,
                 bus: EventBus | None = None) -> ClaimVerdict:
    """No-UI convenience for the agent tool and bench: a throwaway bus unless one is given."""
    return await testify(claim, scene, ctx or get_context(), bus or EventBus(new_run_id()), stock_ab=stock_ab,
                         jury_size=jury_size, probe_overrides=probe_overrides)
