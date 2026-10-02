"""PERJURY bench (FINAL-IDEA-v3 §8): Weave Evaluation `perjury-bench` over bench/claims.yaml.

    python -m bench.run_bench --split dev [--k 16] [--concurrency 6]      # dev pass (tune on this only)
    python -m bench.run_bench --split dev --lead [--n 10]                 # P-LEAD sycophancy pass (bench only)
    python -m bench.run_bench --freeze                                    # dev run -> cache/promotion.json
    python -m bench.run_bench --split test                                # ONCE, after --freeze (14:00)
    PERJURY_MODE=fixture PERJURY_FIXTURE_LATENCY=0 python -m bench.run_bench --split dev --offline

Every run saves the raw per-claim results, including ALL juror votes, to cache/bench_runs/<split>[_lead]_<ts>.json,
so the jury-size curve (bench/report.py) costs no extra GPU. --offline forces fixture mode and skips Weave.
Test-split guard: refuses without a frozen promotion file, and refuses a second test run of the same variant unless
--i-know (the lock file cache/test_run.lock records each run; Weave timestamps prove the order).
"""
from __future__ import annotations

import argparse
import asyncio
import inspect
import json
import os
import sys
import time
import uuid
from typing import Any, Optional

from bench.common import (choose_m, latest_run, load_claims, match_atoms, now_iso, promotion_path, save_run,
                          test_lock_path)

LEAD_TYPES = ("towing", "heavy_vehicle_kind")   # the presence-jury types whose P-TOW probe P-LEAD replaces


def probe_overrides(split: str, variant: str) -> dict:
    """tiers.RunOpts.probe_overrides. Dev measures every type (ignore_promotion), or a demoted type could never earn
    promotion; test runs with the frozen router exactly as on stage. P-LEAD is bench-only."""
    o: dict = {"ignore_promotion": True} if split == "dev" else {}
    if variant == "lead":
        o["lead"] = True
    return o
_RESULTS: dict[str, dict] = {}   # claim_id -> raw result (weave.Model fields must stay serializable)
_CTX: dict[str, Any] = {}


class GuardError(SystemExit):
    pass


# ---------------------------------------------------------------- pipeline call (lazy; core owns perjury.pipeline)
def _pipeline():
    try:
        from perjury import pipeline  # noqa: WPS433
    except ImportError as e:
        raise RuntimeError(f"perjury.pipeline is not importable yet ({e}); the bench needs testify()/verify()") from e
    return pipeline


def _kwargs_for(fn, **kw) -> dict:
    params = inspect.signature(fn).parameters
    if any(p.kind == p.VAR_KEYWORD for p in params.values()):
        return kw
    return {k: v for k, v in kw.items() if k in params}


async def call_pipeline(text: str, scene: int, *, jury_size: int, probe_overrides: Optional[dict]) -> dict:
    """verify(claim, scene, ...) if core exposes it, else testify(text, scene, ctx, bus, ...). Returns a plain dict."""
    pl = _pipeline()
    if "ctx" not in _CTX:
        _CTX["ctx"] = pl.load_context()
    ctx = _CTX["ctx"]
    extra = {"jury_size": jury_size, "probe_overrides": probe_overrides}
    if hasattr(pl, "verify"):
        fn = pl.verify
        cv = await fn(text, scene, **_kwargs_for(fn, ctx=ctx, **extra))
    else:
        from perjury.events import EventBus
        fn = pl.testify
        bus = EventBus(f"bench-{uuid.uuid4().hex[:8]}")
        cv = await fn(text, scene, ctx, bus, **_kwargs_for(fn, transcript_source="typed", **extra))
    d = cv.model_dump(mode="json") if hasattr(cv, "model_dump") else dict(cv)
    return d


async def predict_one(row: dict, *, jury_size: int, variant: str, timeout_s: float) -> dict:
    t0 = time.monotonic()
    out: dict[str, Any] = {k: row[k] for k in ("id", "scene", "text", "kind", "split", "expected_claim",
                                                 "expected_atoms", "truth_source", "hero", "sycophancy")}
    try:
        cv = await asyncio.wait_for(
            call_pipeline(row["text"], int(row["scene"]), jury_size=jury_size,
                          probe_overrides=probe_overrides(row["split"], variant) or None), timeout_s)
        out.update(verdict=cv.get("verdict"), explanation=cv.get("explanation"), atoms=cv.get("atoms", []),
                   atom_verdicts=cv.get("atom_verdicts", []), parser=cv.get("parser"), run_id=cv.get("run_id"),
                   elapsed_ms=cv.get("elapsed_ms") or int((time.monotonic() - t0) * 1000),
                   gpu_s=float(cv.get("gpu_s") or 0.0), calls=cv.get("calls"),
                   services_fired=cv.get("services_fired", []), mode=cv.get("mode"), error=None)
    except Exception as e:  # count failures against the system, don't crash the bench
        out.update(verdict=None, explanation=None, atoms=[], atom_verdicts=[], elapsed_ms=int((time.monotonic() - t0) * 1000),
                   gpu_s=0.0, error=f"{type(e).__name__}: {e}"[:500])
    out["wall_ms"] = int((time.monotonic() - t0) * 1000)
    out["atom_matches"] = match_atoms(row["expected_atoms"], out["atoms"], out["atom_verdicts"])
    return out


# ---------------------------------------------------------------- scorers (plain functions; wrapped by weave.op lazily)
def verdict_score(kind: str, expected_claim: str, output: dict) -> dict:
    v = output.get("verdict")
    return {"ok": v is not None, "correct": v == expected_claim,
            "caught": kind == "lie" and v == "FALSE",                 # catch = caught / lies
            "false_accusation": kind == "truth" and v == "FALSE",     # / truths
            "supported": kind == "truth" and v == "TRUE",             # / truths (anti-hover)
            "declined": v == "UNPROVEN",
            "correct_decline": kind == "unverifiable" and v == "UNPROVEN",
            "overreach": kind == "unverifiable" and v in ("TRUE", "FALSE")}


def atom_score(output: dict) -> dict:
    ms = output.get("atom_matches") or []
    correct = sum(1 for m in ms if m.get("correct"))
    return {"n": len(ms), "correct": correct, "accuracy": correct / len(ms) if ms else None,
            "missing": sum(1 for m in ms if m.get("got") == "MISSING")}


def latency_score(output: dict) -> dict:
    ms = output.get("elapsed_ms") or 0
    return {"elapsed_ms": ms, "under_20s": ms < 20_000}


def gpu_s_score(output: dict) -> dict:
    return {"gpu_s": float(output.get("gpu_s") or 0.0)}


# ---------------------------------------------------------------- guards
def check_test_guard(split: str, variant: str, mode: str, i_know: bool) -> None:
    if split != "test":
        return
    if not promotion_path(mode).exists():
        raise GuardError(f"REFUSED: test split needs a frozen promotion state ({promotion_path(mode).name}). "
                         "Run `python -m bench.run_bench --freeze` on the dev run first.")
    lock = test_lock_path(mode)
    entries = json.loads(lock.read_text()) if lock.exists() else []
    prior = [e for e in entries if e.get("variant") == variant]
    if prior and not i_know:
        raise GuardError(f"REFUSED: the test split ({variant}) already ran at {prior[0].get('started_at')} "
                         f"({lock.name}). Test runs ONCE. Pass --i-know only if that run was void, and say so.")


def write_test_lock(variant: str, mode: str, info: dict) -> None:
    lock = test_lock_path(mode)
    entries = json.loads(lock.read_text()) if lock.exists() else []
    entries.append({"variant": variant, **info})
    lock.parent.mkdir(parents=True, exist_ok=True)
    lock.write_text(json.dumps(entries, indent=1))


# ---------------------------------------------------------------- runners
def select_rows(rows: list[dict], variant: str, n: Optional[int]) -> list[dict]:
    if variant == "lead":   # P-LEAD only changes towing-type probes: put those first (S2 sycophancy row first of all)
        tow = [r for r in rows if any(a["type"] in LEAD_TYPES for a in r["expected_atoms"])]
        tow.sort(key=lambda r: (not r.get("sycophancy"), r["id"]))
        rest = [r for r in rows if r not in tow and r["kind"] == "lie"]
        rows = tow + rest
        return rows[: n or 10]
    return rows[:n] if n else rows


async def run_offline(rows: list[dict], *, jury_size: int, variant: str, concurrency: int, timeout_s: float) -> list[dict]:
    sem = asyncio.Semaphore(max(1, concurrency))

    async def one(r):
        async with sem:
            res = await predict_one(r, jury_size=jury_size, variant=variant, timeout_s=timeout_s)
            print(f"  {r['id']} S{r['scene']} {r['kind']:<12} expect {r['expected_claim']:<8} got {res['verdict'] or 'ERROR':<8}"
                  f" {res['elapsed_ms']:>6} ms" + (f"  {res['error']}" if res["error"] else ""), flush=True)
            return res
    return list(await asyncio.gather(*(one(r) for r in rows)))


def run_weave(rows: list[dict], *, project: str, jury_size: int, variant: str, concurrency: int,
              timeout_s: float, mode: str) -> tuple[list[dict], Optional[str], Optional[dict]]:
    import weave  # noqa: WPS433

    os.environ.setdefault("WEAVE_PARALLELISM", str(max(1, concurrency)))
    client = weave.init(project)

    class PerjuryModel(weave.Model):
        jury_size: int
        probe_variant: str   # "neutral" | "lead"
        mode: str

        @weave.op()
        async def predict(self, claim_id: str, text: str, scene: int) -> dict:
            row = by_id[claim_id]
            res = await predict_one(row, jury_size=self.jury_size, variant=self.probe_variant, timeout_s=timeout_s)
            _RESULTS[claim_id] = res
            return {k: res[k] for k in ("verdict", "explanation", "atom_matches", "elapsed_ms", "gpu_s", "error",
                                        "atom_verdicts")}

    @weave.op(name="verdict")
    def verdict(kind: str, expected_claim: str, output: dict) -> dict:
        return verdict_score(kind, expected_claim, output)

    @weave.op(name="atom")
    def atom(output: dict) -> dict:
        return atom_score(output)

    @weave.op(name="latency")
    def latency(output: dict) -> dict:
        return latency_score(output)

    @weave.op(name="gpu_s")
    def gpu_s(output: dict) -> dict:
        return gpu_s_score(output)

    by_id = {r["id"]: r for r in rows}
    ds_rows = [{"claim_id": r["id"], "text": r["text"], "scene": int(r["scene"]), "kind": r["kind"],
                "split": r["split"], "expected_claim": r["expected_claim"], "expected_atoms": r["expected_atoms"]}
               for r in rows]
    split = rows[0]["split"] if rows else "dev"
    ds = weave.Dataset(name=f"perjury-claims-{split}", rows=ds_rows)
    ev = weave.Evaluation(name="perjury-bench", dataset=ds, scorers=[verdict, atom, latency, gpu_s])
    model = PerjuryModel(jury_size=jury_size, probe_variant=variant, mode=mode)
    label = f"perjury k={jury_size}" + (" P-LEAD" if variant == "lead" else "") + f" · {split}"
    summary = asyncio.run(ev.evaluate(model, __weave={"display_name": label}))
    url = None
    try:
        url = f"https://wandb.ai/{client.entity}/{client.project}/weave/evaluations"
    except Exception:
        pass
    return [_RESULTS[r["id"]] for r in rows if r["id"] in _RESULTS], url, summary


def freeze(mode: str, jury_size: int) -> int:
    from bench.report import promotion_from_run
    run = latest_run("dev", "neutral", mode=mode)
    if not run:
        print(f"[bench] no {mode} dev run in cache/bench_runs/; run `--split dev` first", file=sys.stderr)
        return 2
    doc = promotion_from_run(run, jury_size=jury_size)
    path = promotion_path(mode)
    path.write_text(json.dumps(doc, indent=1))
    print(f"[bench] froze promotion state from {run['_path']} -> {path}")
    for t, e in doc["types"].items():
        extra = f" alpha={doc['alpha'][t]} m={doc['m'][t]}" if t in doc["alpha"] else ""
        print(f"  {t:<16} {'PROMOTED' if e['promoted'] else 'demoted ':<8} catch={e['catch']} "
              f"false_acc={e['false_accusation']} n={e['n']}{extra}  ({e['reason']})")
    return 0


def summarize(results: list[dict]) -> str:
    def frac(kind: str, verdict: str) -> str:
        xs = [r for r in results if r["kind"] == kind]
        return f"{sum(r['verdict'] == verdict for r in xs)}/{len(xs)}"
    errs = sum(1 for r in results if not r["verdict"])
    return (f"catch {frac('lie', 'FALSE')} · false-accusation {frac('truth', 'FALSE')} · support {frac('truth', 'TRUE')}"
            f" · correct-decline {frac('unverifiable', 'UNPROVEN')} · compound-FALSE {frac('compound', 'FALSE')}"
            f" · errors {errs}")


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="PERJURY bench (Weave Evaluation perjury-bench)")
    ap.add_argument("--split", choices=("dev", "test"), default="dev")
    ap.add_argument("--k", type=int, default=16, help="jurors per T2 atom (16 = every camera; the curve subsamples)")
    ap.add_argument("--lead", action="store_true", help="P-LEAD pass (sycophancy; bench only)")
    ap.add_argument("--n", type=int, default=None, help="limit claims (default: all; 10 for --lead)")
    ap.add_argument("--freeze", action="store_true", help="write the promotion state from the latest dev run; no new run")
    ap.add_argument("--offline", action="store_true", help="fixture mode, no Weave")
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--timeout", type=float, default=120.0, help="per-claim cap in seconds")
    ap.add_argument("--project", default=None)
    ap.add_argument("--i-know", dest="i_know", action="store_true", help="allow a second test run (say why on stage)")
    a = ap.parse_args(argv)

    if a.offline:
        os.environ["PERJURY_MODE"] = "fixture"
        os.environ["PERJURY_WEAVE"] = "0"
    from perjury.config import Settings
    s = Settings()
    mode = s.mode

    if a.freeze:
        return freeze(mode, s.jury_size)

    variant = "lead" if a.lead else "neutral"
    try:
        check_test_guard(a.split, variant, mode, a.i_know)
    except GuardError as e:
        print(str(e), file=sys.stderr)
        return 3
    rows = select_rows(load_claims(split=a.split), variant, a.n)
    started = now_iso()
    if a.split == "test":
        write_test_lock(variant, mode, {"started_at": started, "jury_size": a.k, "n": len(rows),
                                        "promotion": str(promotion_path(mode))})
    print(f"[bench] {a.split} · {variant} · k={a.k} · {len(rows)} claims · mode={mode}"
          + (" · FIXTURE numbers are not pitch numbers" if mode != "live" else ""))

    weave_url, summary = None, None
    use_weave = not a.offline and bool(os.getenv("WANDB_API_KEY")) and os.getenv("PERJURY_WEAVE", "1") != "0"
    if use_weave:
        results, weave_url, summary = run_weave(rows, project=a.project or s.wandb_project, jury_size=a.k,
                                                variant=variant, concurrency=a.concurrency, timeout_s=a.timeout,
                                                mode=mode)
    else:
        if not a.offline:
            print("[bench] WANDB_API_KEY unset or PERJURY_WEAVE=0: running without Weave", file=sys.stderr)
        results = asyncio.run(run_offline(rows, jury_size=a.k, variant=variant, concurrency=a.concurrency,
                                          timeout_s=a.timeout))
    run = {"version": 1, "split": a.split, "variant": variant, "jury_size": a.k, "mode": mode,
           "offline": a.offline, "started_at": started, "finished_at": now_iso(), "weave_url": weave_url,
           "promotion_frozen_at": (json.loads(promotion_path(mode).read_text()).get("frozen_at")
                                   if promotion_path(mode).exists() else None),
           "weave_summary": summary, "results": results}
    path = save_run(run)
    print(f"[bench] {summarize(results)}")
    print(f"[bench] saved {path}" + (f" · Weave {weave_url}" if weave_url else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
