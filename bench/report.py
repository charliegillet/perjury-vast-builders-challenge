"""Build cache/bench_report.json (served at GET /api/bench, rendered by the UI Bench tab) from stored bench runs.

    python -m bench.report [--out cache/bench_report.json] [--subsets 50] [--seed 0]

Inputs (all optional; missing inputs give null sections, never invented numbers):
  cache/bench_runs/<split>_<ts>.json        neutral runs (bench/run_bench.py); live runs beat fixture runs
  cache/bench_runs/<split>_lead_<ts>.json   P-LEAD runs (sycophancy)
  cache/stock_ab.json                       bench/stock_ab.py
  cache/witness.json                        perjury/witness.py
  cache/promotion.json | fixture_promotion.json   run_bench --freeze

SCHEMA (keys are stable; the UI may rely on them). Every "metric" is {"k": int, "n": int, "rate": float|null,
"ci": [lo, hi]|null} with Wilson 95% CIs (k = numerator, n = denominator).
{
  "version": 1,
  "generated_at": "<iso>",
  "mode": "live" | "fixture" | "empty", # "fixture" if ANY input came from fixture/offline runs; "empty" = no inputs
  "fixture": bool,                      # UI shows a FIXTURE banner; bench/fill_numbers.py refuses to fill slides
  "splits": {
    "dev" | "test": null | {
      "run": {"path", "started_at", "finished_at", "mode", "jury_size", "variant", "weave_url", "n_claims", "errors"},
      "catch":             metric,      # lies -> FALSE / lies
      "false_accusation":  metric,      # truths -> FALSE / truths
      "support":           metric,      # truths -> TRUE / truths   (anti-hover number)
      "decline":           metric,      # UNPROVEN / all claims
      "correct_decline":   metric,      # unverifiable-by-design -> UNPROVEN / those claims
      "overreach":         metric,      # unverifiable-by-design -> TRUE|FALSE / those claims
      "compound_correct":  metric,      # compound claims whose verdict == expected
      "claim_accuracy":    metric,      # all claims whose verdict == expected
      "by_kind": {"lie"|"truth"|"unverifiable"|"compound": {"TRUE": int, "FALSE": int, "UNPROVEN": int, "ERROR": int}},
      "atoms": {"<type>": {"n", "correct", "accuracy": metric, "catch": metric, "false_accusation": metric,
                           "support": metric}},
      "latency_ms": {"p50", "p90", "max"}, "gpu_s": {"mean", "total"},
      "claims": [{"id", "scene", "text", "kind", "expected", "verdict", "correct", "elapsed_ms", "gpu_s",
                  "atoms": [{"span", "type", "expected", "got", "correct"}]}]
    }
  },
  "jury_curve": [{"k", "catch", "false_accusation", "support", "atom_catch", "atom_false_accusation", "m", "alpha",
                  "n_lie_claims", "n_true_claims", "subsets", "splits": [..]}],   # [] when no T2 votes stored
  "jury_curve_note": str,
  "sycophancy": {"neutral": {"yes": j, "yes_after_zoom": int, "n": int} | null,
                 "lead": {"yes": k, "n": int} | null, "claim_id", "scene", "text"},
  "stock": null | {"path", "mode", "splits": {"dev"|"test": {"catch", "false_accusation", "support", "decline",
                   "unclassified": int, "hits_median"}}, "g2": {...}|null},
  "promotion": null | {"frozen_at", "mode", "types": {...}, "alpha": {...}, "m": {...}},
  "witness": null | {"available": bool, "sentences", "contradicted", "unverifiable", "supported",
                     "agreement": metric|null, "sources": [..]},
  "numbers": {"N","L","X","T","Y","S","U","Z","A","A_n","j","k","syco_n","c","u","p", ... see numbers()},
  "weave_url": str | null
}
"""
from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from pathlib import Path
from typing import Any, Optional

from bench.common import (KINDS, PRESENCE_JURY_TYPES, RUNS_DIR, DEFAULT_ALPHA_PRIOR, _choose_m_local, claim_verdict,
                          latest_run, now_iso, promotion_path, rate)
from perjury.config import CACHE

JURY_KS = (1, 3, 6, 16)
LEAD_PROBE = "P-LEAD"


# ---------------------------------------------------------------- per-split metrics
def _verdict(r: dict) -> str:
    return r.get("verdict") or "ERROR"


def split_metrics(run: dict) -> dict:
    res = run.get("results", [])
    by_kind = {k: {"TRUE": 0, "FALSE": 0, "UNPROVEN": 0, "ERROR": 0} for k in KINDS}
    for r in res:
        by_kind.setdefault(r["kind"], {"TRUE": 0, "FALSE": 0, "UNPROVEN": 0, "ERROR": 0})
        v = _verdict(r)
        by_kind[r["kind"]][v if v in ("TRUE", "FALSE", "UNPROVEN") else "ERROR"] += 1

    def n(kind: str) -> int:
        return sum(by_kind[kind].values())

    unv = by_kind["unverifiable"]
    comp = [r for r in res if r["kind"] == "compound"]
    lat = sorted(int(r.get("elapsed_ms") or 0) for r in res if r.get("verdict"))
    gpu = [float(r.get("gpu_s") or 0.0) for r in res if r.get("verdict")]

    def pct(xs: list, q: float) -> Optional[int]:
        return xs[min(len(xs) - 1, int(math.ceil(q * len(xs))) - 1)] if xs else None

    return {
        "run": {"path": run.get("_path"), "started_at": run.get("started_at"), "finished_at": run.get("finished_at"),
                "mode": run.get("mode"), "jury_size": run.get("jury_size"), "variant": run.get("variant", "neutral"),
                "weave_url": run.get("weave_url"), "n_claims": len(res),
                "errors": sum(1 for r in res if not r.get("verdict")),
                "evaluation_scope": run.get("evaluation_scope"), "exclusions": run.get("exclusions", []),
                "ground_truth_basis": run.get("ground_truth_basis"), "coverage": run.get("coverage")},
        "catch": rate(by_kind["lie"]["FALSE"], n("lie")),
        "false_accusation": rate(by_kind["truth"]["FALSE"], n("truth")),
        "support": rate(by_kind["truth"]["TRUE"], n("truth")),
        "decline": rate(sum(1 for r in res if _verdict(r) == "UNPROVEN"), len(res)),
        "correct_decline": rate(unv["UNPROVEN"], n("unverifiable")),
        "overreach": rate(unv["TRUE"] + unv["FALSE"], n("unverifiable")),
        "compound_correct": rate(sum(1 for r in comp if _verdict(r) == r["expected_claim"]), len(comp)),
        "claim_accuracy": rate(sum(1 for r in res if _verdict(r) == r["expected_claim"]), len(res)),
        "by_kind": by_kind,
        "atoms": atom_type_stats(res),
        "latency_ms": {"p50": pct(lat, 0.5), "p90": pct(lat, 0.9), "max": lat[-1] if lat else None},
        "gpu_s": {"mean": round(statistics.mean(gpu), 2) if gpu else None, "total": round(sum(gpu), 2)},
        "claims": [{"id": r["id"], "scene": r["scene"], "text": r["text"], "kind": r["kind"],
                    "expected": r["expected_claim"], "verdict": _verdict(r),
                    "correct": _verdict(r) == r["expected_claim"], "elapsed_ms": r.get("elapsed_ms"),
                    "gpu_s": r.get("gpu_s"),
                    "atoms": [{k: m.get(k) for k in ("span", "type", "expected", "got", "correct")}
                              for m in r.get("atom_matches", [])]} for r in res],
    }


def atom_type_stats(results: list[dict]) -> dict:
    """Per expected atom type: accuracy over all scored atoms, plus the promotion numbers on hard expectations.
    catch = expected CONTRADICTED that got CONTRADICTED; false_accusation = expected SUPPORTED that got CONTRADICTED."""
    acc: dict[str, dict] = {}
    for r in results:
        for m in r.get("atom_matches", []):
            a = acc.setdefault(m["type"], {"n": 0, "correct": 0, "lies": 0, "caught": 0, "truths": 0,
                                           "accused": 0, "supported": 0})
            a["n"] += 1
            a["correct"] += bool(m.get("correct"))
            if m["expected"] == "CONTRADICTED":
                a["lies"] += 1
                a["caught"] += m.get("got") == "CONTRADICTED"
            elif m["expected"] == "SUPPORTED":
                a["truths"] += 1
                a["accused"] += m.get("got") == "CONTRADICTED"
                a["supported"] += m.get("got") == "SUPPORTED"
    return {t: {"n": a["n"], "correct": a["correct"], "n_hard": a["lies"] + a["truths"],
                "accuracy": rate(a["correct"], a["n"]), "catch": rate(a["caught"], a["lies"]),
                "false_accusation": rate(a["accused"], a["truths"]), "support": rate(a["supported"], a["truths"])}
            for t, a in sorted(acc.items())}


# ---------------------------------------------------------------- promotion (§4 rule, used by run_bench --freeze)
def measured_alpha(results: list[dict]) -> dict[str, dict]:
    """alpha per type = juror false-yes rate after the zoom-check, on atoms expected CONTRADICTED (object absent).
    Only neutral jury votes count (P-LEAD is never a verdict probe)."""
    out: dict[str, dict] = {}
    for r in results:
        avs = {v.get("atom_id"): v for v in r.get("atom_verdicts", [])}
        for m in r.get("atom_matches", []):
            if m["expected"] != "CONTRADICTED" or not m.get("atom_id"):
                continue
            votes = [v for v in (avs.get(m["atom_id"]) or {}).get("votes", [])
                     if v.get("tier", "JURY") == "JURY" and v.get("probe") != LEAD_PROBE]
            if not votes:
                continue
            a = out.setdefault(m["type"], {"false_yes": 0, "valid": 0})
            zr = _zoom_required(avs.get(m["atom_id"]) or {})
            for v in votes:
                if v.get("vote") in ("yes", "no"):
                    a["valid"] += 1
                    a["false_yes"] += _counted_yes(v, zr)
    for a in out.values():
        a["alpha"] = round(a["false_yes"] / a["valid"], 4) if a["valid"] else None
    return out


def promotion_from_run(run: dict, *, jury_size: int = 6, min_catch: float = 0.80, max_fa: float = 0.10,
                       min_n: int = 5, aliases: Optional[dict] = None) -> dict:
    """§4 promotion rule on a DEV run -> the cache/promotion.json document (BUILD-CONTRACT shape + extras)."""
    from bench.common import TYPE_ALIASES
    aliases = TYPE_ALIASES if aliases is None else aliases
    stats = atom_type_stats(run.get("results", []))
    alphas = measured_alpha(run.get("results", []))
    types, alpha, m_by = {}, {}, {}
    for t, s in stats.items():
        if s["n_hard"] == 0:
            continue   # unverifiable-by-design types: nothing to promote
        catch, fa = s["catch"]["rate"], s["false_accusation"]["rate"]
        reasons = []
        if s["n_hard"] < min_n:
            reasons.append(f"n={s['n_hard']} < {min_n}")
        if catch is None:
            reasons.append("no planted lies of this type in dev (catch undefined)")
        elif catch < min_catch:
            reasons.append(f"catch {catch:.0%} < {min_catch:.0%}")
        if fa is not None and fa > max_fa:
            reasons.append(f"false accusation {fa:.0%} > {max_fa:.0%}")
        entry = {"promoted": not reasons, "catch": catch, "false_accusation": fa, "n": s["n_hard"],
                 "n_lies": s["catch"]["n"], "n_truths": s["false_accusation"]["n"],
                 "reason": "; ".join(reasons) or "meets rule"}
        if t in PRESENCE_JURY_TYPES:
            a = (alphas.get(t) or {}).get("alpha")
            entry["alpha_source"] = "measured" if a is not None else "prior"
            a = DEFAULT_ALPHA_PRIOR if a is None else a
            m = _choose_m_from_quorum(a, jury_size)
            alpha[t], m_by[t] = a, m
            if m is None and entry["promoted"]:
                entry["promoted"], entry["reason"] = False, f"m would be >= 5 at alpha={a:.2f}"
        types[t] = entry
        for al in aliases.get(t, ()):
            if al not in stats:
                types[al] = {**entry, "reason": entry["reason"] + f" (shares the {t} rule)"}
    return {"frozen_at": now_iso(), "mode": run.get("mode"), "source_run": run.get("_path"),
            "rule": {"min_catch": min_catch, "max_false_accusation": max_fa, "min_n": min_n, "split": "dev",
                     "jury_size": jury_size},
            "types": types, "alpha": alpha, "m": m_by, "alpha_detail": alphas}


def _choose_m_from_quorum(alpha: float, k: int) -> Optional[int]:
    from bench.common import choose_m
    return choose_m(alpha, k)


# ---------------------------------------------------------------- jury-size curve (§8; no extra GPU)
def _zoom_required(av: dict) -> bool:
    """quorum.presence_verdict counts Y = yes votes with zoom_ok True when the atom required the zoom-check
    (normal P-TOW); P-LEAD / semis runs set stats.zoom_required False and every yes counts."""
    return bool((av.get("stats") or {}).get("zoom_required", True))


def _counted_yes(v: dict, zoom_required: bool) -> bool:
    return v.get("vote") == "yes" and (v.get("zoom_ok") is True or not zoom_required)


def _presence(votes: list[dict], k: int, m: Optional[int], t1_supports: int, *, zoom_required: bool = True,
              t1_complete: bool = True) -> str:
    Y = sum(1 for v in votes if _counted_yes(v, zoom_required))
    N = sum(1 for v in votes if v.get("vote") == "no")
    try:
        from perjury.quorum import presence_verdict
        return presence_verdict(Y, N, k, m, retrieved_top=True, t1_supports=t1_supports,
                                t1_complete=t1_complete).verdict
    except ImportError:
        if m is not None and Y >= m:
            return "SUPPORTED"
        if Y == 0 and Y + N >= max(1, math.ceil(5 * k / 6)) and t1_supports == 0 and t1_complete:
            return "CONTRADICTED"
        return "UNVERIFIABLE"


def _t1(av: dict) -> tuple[int, bool]:
    st = av.get("stats") or {}
    t1 = st.get("t1")
    if isinstance(t1, dict):
        return int(t1.get("supports") or 0), bool(t1.get("complete", True))
    return int(st.get("t1_supports") or 0), True


def jury_curve(runs: list[dict], alpha: float, ks=JURY_KS, subsets: int = 50, seed: int = 0) -> list[dict]:
    """For every stored presence-jury atom (towing / heavy_vehicle_kind) with neutral votes: draw `subsets` random
    camera subsets of size k, recompute the atom verdict with the §7 presence rule (m chosen for that k from alpha,
    with no demotion cap: this is the curve, not the stage router), recompute the claim verdict with the other atoms
    held fixed, and average. Retrieval rank is assumed satisfied (every stored juror was a top-1-per-camera moment)."""
    rng = random.Random(seed)
    items = []
    for run in runs:
        for r in run.get("results", []):
            if r.get("expected_claim") not in ("TRUE", "FALSE") or not r.get("verdict"):
                continue
            avs = r.get("atom_verdicts", [])
            types = {m.get("atom_id"): m for m in r.get("atom_matches", []) if m.get("atom_id")}
            pred_types = {a.get("id"): str(a.get("type")) for a in r.get("atoms", [])}
            for i, av in enumerate(avs):
                t = pred_types.get(av.get("atom_id")) or (types.get(av.get("atom_id")) or {}).get("type")
                if t not in PRESENCE_JURY_TYPES:
                    continue
                votes = [v for v in av.get("votes", []) if v.get("tier", "JURY") == "JURY"
                         and v.get("probe") != LEAD_PROBE]
                if votes:
                    sup, complete = _t1(av)
                    items.append({"r": r, "i": i, "votes": votes, "t1": sup, "t1_complete": complete,
                                  "zoom_required": _zoom_required(av),
                                  "expected_atom": (types.get(av.get("atom_id")) or {}).get("expected"),
                                  "split": run.get("split")})
    out = []
    for k in ks:
        m = _choose_m_local(alpha, k, max_m=k)
        tallies = {"lie": [0, 0], "true_fa": [0, 0], "true_sup": [0, 0], "atom_c": [0, 0], "atom_fa": [0, 0]}
        used = 0
        for it in items:
            if len(it["votes"]) < k:
                continue
            used += 1
            r, labels = it["r"], [a.get("verdict") for a in it["r"]["atom_verdicts"]]
            for _ in range(subsets):
                sub = rng.sample(it["votes"], k)
                v = _presence(sub, k, m, it["t1"], zoom_required=it["zoom_required"], t1_complete=it["t1_complete"])
                labels2 = list(labels)
                labels2[it["i"]] = v
                cv = claim_verdict(labels2)
                if r["expected_claim"] == "FALSE":
                    tallies["lie"][0] += cv == "FALSE"; tallies["lie"][1] += 1
                else:
                    tallies["true_fa"][0] += cv == "FALSE"; tallies["true_fa"][1] += 1
                    tallies["true_sup"][0] += cv == "TRUE"; tallies["true_sup"][1] += 1
                if it["expected_atom"] == "CONTRADICTED":
                    tallies["atom_c"][0] += v == "CONTRADICTED"; tallies["atom_c"][1] += 1
                elif it["expected_atom"] == "SUPPORTED":
                    tallies["atom_fa"][0] += v == "CONTRADICTED"; tallies["atom_fa"][1] += 1
        if not used:
            continue
        f = lambda t: round(t[0] / t[1], 4) if t[1] else None  # noqa: E731
        out.append({"k": k, "catch": f(tallies["lie"]), "false_accusation": f(tallies["true_fa"]),
                    "support": f(tallies["true_sup"]), "atom_catch": f(tallies["atom_c"]),
                    "atom_false_accusation": f(tallies["atom_fa"]), "m": m, "alpha": alpha,
                    "n_lie_claims": tallies["lie"][1] // subsets, "n_true_claims": tallies["true_fa"][1] // subsets,
                    "subsets": subsets, "splits": sorted({it["split"] for it in items if len(it["votes"]) >= k})})
    return out


# ---------------------------------------------------------------- sycophancy (§8)
def _syco_claim(runs: list[dict]) -> Optional[dict]:
    for run in runs:
        for r in run.get("results", []):
            if r.get("sycophancy"):
                return r
    return None


def _towing_votes(r: dict) -> list[dict]:
    pred_types = {a.get("id"): str(a.get("type")) for a in r.get("atoms", [])}
    for av in r.get("atom_verdicts", []):
        if pred_types.get(av.get("atom_id")) in PRESENCE_JURY_TYPES:
            return [v for v in av.get("votes", []) if v.get("tier", "JURY") == "JURY"]
    return []


def sycophancy(neutral_runs: list[dict], lead_runs: list[dict]) -> dict:
    """P(yes | absent) on the S2 trailer lie: neutral P-TOW vs leading P-LEAD, same cameras."""
    n_r, l_r = _syco_claim(neutral_runs), _syco_claim(lead_runs)
    out: dict[str, Any] = {"neutral": None, "lead": None, "claim_id": None, "scene": None, "text": None}
    if n_r:
        votes = [v for v in _towing_votes(n_r) if v.get("probe") != LEAD_PROBE]
        out.update(claim_id=n_r["id"], scene=n_r["scene"], text=n_r["text"])
        if votes:
            out["neutral"] = {"yes": sum(v.get("vote") == "yes" for v in votes),
                              "yes_after_zoom": sum(v.get("vote") == "yes" and v.get("zoom_ok") is True for v in votes),
                              "n": len(votes)}
    if l_r:
        votes = _towing_votes(l_r)
        out.update(claim_id=l_r["id"], scene=l_r["scene"], text=l_r["text"])
        if votes:
            out["lead"] = {"yes": sum(v.get("vote") == "yes" for v in votes), "n": len(votes)}
    return out


# ---------------------------------------------------------------- stock A/B + witness
def stock_summary(stock: Optional[dict]) -> Optional[dict]:
    if not stock:
        return None
    splits = {}
    for sp in ("dev", "test"):
        rows = [r for r in stock.get("results", []) if r.get("split") == sp]
        if not rows:
            splits[sp] = None
            continue
        v = lambda r: r.get("verdict")  # noqa: E731  (TRUE/FALSE/UNPROVEN after hand labels; None = unclassified)
        lies = [r for r in rows if r["kind"] == "lie"]
        truths = [r for r in rows if r["kind"] == "truth"]
        unv = [r for r in rows if r["kind"] == "unverifiable"]
        hits = [r["hits"] for r in rows if isinstance(r.get("hits"), int)]
        splits[sp] = {"catch": rate(sum(v(r) == "FALSE" for r in lies), len(lies)),
                      "false_accusation": rate(sum(v(r) == "FALSE" for r in truths), len(truths)),
                      "support": rate(sum(v(r) == "TRUE" for r in truths), len(truths)),
                      "decline": rate(sum(v(r) == "UNPROVEN" for r in rows), len(rows)),
                      "correct_decline": rate(sum(v(r) == "UNPROVEN" for r in unv), len(unv)),
                      "unclassified": sum(1 for r in rows if v(r) is None),
                      "errors": sum(1 for r in rows if r.get("error")),
                      "hits_median": statistics.median(hits) if hits else None}
    return {"path": stock.get("_path"), "mode": stock.get("mode"), "generated_at": stock.get("generated_at"),
            "prompt_template": stock.get("prompt_template"), "splits": splits, "g2": stock.get("g2")}


def _walk(x: Any):
    if isinstance(x, dict):
        yield x
        for v in x.values():
            yield from _walk(v)
    elif isinstance(x, list):
        for v in x:
            yield from _walk(v)


def witness_summary(w: Optional[dict]) -> Optional[dict]:
    """Shape-tolerant: counts every dict carrying a claim verdict (TRUE/FALSE/UNPROVEN), and agreement with a human
    label when one is present (`human_label` / `label` / `expected`)."""
    if not w:
        return None
    rows = [d for d in _walk(w) if d.get("verdict") in ("TRUE", "FALSE", "UNPROVEN")]
    labelled = [d for d in rows if any(d.get(k) in ("TRUE", "FALSE", "UNPROVEN")
                                       for k in ("human_label", "label", "expected"))]
    agree = sum(1 for d in labelled
                if d["verdict"] == next(d[k] for k in ("human_label", "label", "expected")
                                        if d.get(k) in ("TRUE", "FALSE", "UNPROVEN")))
    sources = sorted({str(d.get("witness") or d.get("source") or d.get("who")) for d in rows
                      if d.get("witness") or d.get("source") or d.get("who")})
    return {"available": bool(rows), "sentences": len(rows),
            "contradicted": sum(d["verdict"] == "FALSE" for d in rows),
            "unverifiable": sum(d["verdict"] == "UNPROVEN" for d in rows),
            "supported": sum(d["verdict"] == "TRUE" for d in rows),
            "agreement": rate(agree, len(labelled)) if labelled else None,
            "sources": sources[:20], "mode": w.get("mode")}


# ---------------------------------------------------------------- pitch numbers
def _fmt_ci(m: Optional[dict]) -> Optional[str]:
    if not m or not m.get("ci"):
        return None
    return f"{m['ci'][0] * 100:.0f}–{m['ci'][1] * 100:.0f}%"


def _pct(m: Optional[dict]) -> Optional[str]:
    return None if not m or m.get("rate") is None else f"{m['rate'] * 100:.0f}%"


def _claim(run: Optional[dict], cid: str) -> Optional[dict]:
    return next((r for r in (run or {}).get("results", []) if r["id"] == cid), None)


def numbers(splits: dict, stock: Optional[dict], syco: dict, witness: Optional[dict],
            dev_run: Optional[dict], test_run: Optional[dict]) -> dict:
    """Every {X} placeholder the pitch uses. None = not measured; bench/fill_numbers.py leaves those unfilled."""
    t, d = splits.get("test") or {}, splits.get("dev") or {}
    g = lambda s, key, f: (s.get(key) or {}).get(f)  # noqa: E731
    n: dict[str, Any] = {
        "N": (t.get("run") or {}).get("n_claims"),
        "L": g(t, "catch", "n"), "X": g(t, "catch", "k"), "X_pct": _pct(t.get("catch")), "X_ci": _fmt_ci(t.get("catch")),
        "T": g(t, "false_accusation", "n"), "Y": g(t, "false_accusation", "k"),
        "Y_pct": _pct(t.get("false_accusation")), "Y_ci": _fmt_ci(t.get("false_accusation")),
        "S": g(t, "support", "k"), "S_pct": _pct(t.get("support")), "S_ci": _fmt_ci(t.get("support")),
        "U": g(t, "correct_decline", "n"), "Z": g(t, "correct_decline", "k"),
        "Z_pct": _pct(t.get("correct_decline")), "Z_ci": _fmt_ci(t.get("correct_decline")),
        "decline_pct": _pct(t.get("decline")), "overreach": g(t, "overreach", "k"),
        "compound_ok": g(t, "compound_correct", "k"), "compound_n": g(t, "compound_correct", "n"),
        "dev_X": g(d, "catch", "k"), "dev_L": g(d, "catch", "n"), "dev_Y": g(d, "false_accusation", "k"),
        "dev_T": g(d, "false_accusation", "n"), "dev_S": g(d, "support", "k"),
        "dev_Z": g(d, "correct_decline", "k"), "dev_U": g(d, "correct_decline", "n"),
        "latency_p50_s": None if not t.get("latency_ms", {}).get("p50") else round(t["latency_ms"]["p50"] / 1000, 1),
    }
    st = ((stock or {}).get("splits") or {}).get("test") or {}
    n.update({"A": g(st, "catch", "k"), "A_n": g(st, "catch", "n"),
              "A_false_acc": g(st, "false_accusation", "k"), "A_declined": g(st, "decline", "k"),
              "stock_hits": st.get("hits_median"),
              "g2_false": ((stock or {}).get("g2") or {}).get("false"),
              "g2_n": ((stock or {}).get("g2") or {}).get("n")})
    n.update({"j": (syco.get("neutral") or {}).get("yes"), "j_zoom": (syco.get("neutral") or {}).get("yes_after_zoom"),
              "k": (syco.get("lead") or {}).get("yes"),
              "syco_n": (syco.get("neutral") or syco.get("lead") or {}).get("n")})
    n.update({"c": (witness or {}).get("contradicted") if (witness or {}).get("available") else None,
              "u": (witness or {}).get("unverifiable") if (witness or {}).get("available") else None,
              "w_n": (witness or {}).get("sentences") if (witness or {}).get("available") else None})
    # p: % of test atoms settled (hard verdict) by RECORDS alone, i.e. zero GPU
    atoms = [av for r in (test_run or {}).get("results", []) for av in r.get("atom_verdicts", [])]
    t0 = [av for av in atoms if av.get("verdict") in ("SUPPORTED", "CONTRADICTED")
          and av.get("tiers") and set(av["tiers"]) <= {"RECORDS"}]
    n["p"] = round(100 * len(t0) / len(atoms)) if atoms else None
    # hero rows (dev): S1 jury yes count and the S2 receipt
    s1 = _claim(dev_run, "d08")
    if s1:
        st1 = next((av.get("stats") or {} for av in s1.get("atom_verdicts", []) if (av.get("stats") or {}).get("k")), {})
        n["hero_s1_yes"], n["hero_s1_k"] = st1.get("Y"), st1.get("k")
    s2 = _claim(dev_run, "d01")
    if s2 and s2.get("verdict"):
        n["receipt_calls"], n["receipt_s"] = s2.get("calls"), round((s2.get("elapsed_ms") or 0) / 1000, 1)
        n["receipt_gpu_s"] = round(float(s2.get("gpu_s") or 0), 1)
    return n


# ---------------------------------------------------------------- assemble
def _load(path: Path) -> Optional[dict]:
    if not path.exists():
        return None
    try:
        d = json.loads(path.read_text())
        d["_path"] = str(path)
        return d
    except Exception:
        return None


def build_report(runs_dir: Path = RUNS_DIR, cache: Path = CACHE, subsets: int = 50, seed: int = 0) -> dict:
    dev, test = latest_run("dev", runs_dir=runs_dir), latest_run("test", runs_dir=runs_dir)
    dev_lead, test_lead = latest_run("dev", "lead", runs_dir), latest_run("test", "lead", runs_dir)
    stock = _load(cache / "stock_ab.json")
    witness_raw = _load(cache / "witness.json")
    inputs = [x for x in (dev, test, dev_lead, test_lead, stock, witness_raw) if x]
    fixture = any(x.get("mode") not in (None, "live") for x in inputs)
    mode = "empty" if not inputs else "fixture" if fixture else "live"
    prom = _load(promotion_path("live")) if not fixture else (_load(promotion_path("fixture"))
                                                              or _load(promotion_path("live")))
    splits = {"dev": split_metrics(dev) if dev else None, "test": split_metrics(test) if test else None}
    neutral = [r for r in (test, dev) if r]
    alpha = ((prom or {}).get("alpha") or {}).get("towing")
    if alpha is None:
        ma = measured_alpha([x for r in neutral for x in r.get("results", [])]).get("towing") or {}
        alpha = ma.get("alpha") if ma.get("alpha") is not None else DEFAULT_ALPHA_PRIOR
    curve = jury_curve(neutral, alpha, subsets=subsets, seed=seed)
    syco = sycophancy([r for r in (dev, test) if r], [r for r in (dev_lead, test_lead) if r])
    stock_s, wit = stock_summary(stock), witness_summary(witness_raw)
    weave_url = next((r.get("weave_url") for r in (test, dev, dev_lead) if r and r.get("weave_url")), None)
    note = ("Recomputed from stored juror votes (no extra GPU): 50 random camera subsets per T2 atom, §7 presence rule, "
            "m chosen per k from alpha. If catch does not improve from k=1 to 16, the jurors' errors are correlated.")
    if curve and len({c["catch"] for c in curve}) == 1:
        note += " Catch is flat across k here: errors look correlated (or every subset already agrees)."
    return {"version": 1, "generated_at": now_iso(), "mode": mode, "fixture": fixture, "splits": splits,
            "jury_curve": curve, "jury_curve_note": note, "sycophancy": syco, "stock": stock_s,
            "promotion": prom, "witness": wit,
            "numbers": numbers(splits, stock_s, syco, wit, dev, test), "weave_url": weave_url}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=str(CACHE / "bench_report.json"))
    ap.add_argument("--subsets", type=int, default=50)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    rep = build_report(subsets=a.subsets, seed=a.seed)
    Path(a.out).write_text(json.dumps(rep, indent=1, default=str))
    tag = "FIXTURE (not pitch numbers)" if rep["fixture"] else "LIVE"
    print(f"[bench.report] wrote {a.out} · {tag}")
    for sp in ("dev", "test"):
        s = rep["splits"][sp]
        if not s:
            print(f"  {sp:<4} no run")
            continue
        f = lambda m: "—" if m["rate"] is None else f"{m['k']}/{m['n']} [{m['ci'][0]:.2f},{m['ci'][1]:.2f}]"  # noqa: E731
        print(f"  {sp:<4} catch {f(s['catch'])}  false-acc {f(s['false_accusation'])}  support {f(s['support'])}  "
              f"correct-decline {f(s['correct_decline'])}  overreach {f(s['overreach'])}  errors {s['run']['errors']}")
    for c in rep["jury_curve"]:
        print(f"  jury k={c['k']:<2} m={c['m']} catch={c['catch']} false_acc={c['false_accusation']} "
              f"support={c['support']}")
    sy = rep["sycophancy"]
    print(f"  sycophancy neutral={sy['neutral']} lead={sy['lead']}")
    missing = sorted(k for k, v in rep["numbers"].items() if v is None)
    print(f"  numbers missing: {', '.join(missing) or 'none'}")


if __name__ == "__main__":
    main()
