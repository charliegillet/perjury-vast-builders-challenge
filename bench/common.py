"""Shared bench helpers: claims loading, Wilson CI, choose_m, atom matching, run files. No network, no weave.

`perjury.quorum` is preferred for `wilson_ci` / `choose_m` / `claim_verdict` when importable with the expected
signatures; the local versions below are the reference (§7, §8) and what tests/test_bench.py pins.
"""
from __future__ import annotations

import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

import yaml

from perjury.config import CACHE, ROOT

CLAIMS_PATH = ROOT / "bench" / "claims.yaml"
RUNS_DIR = CACHE / "bench_runs"
KINDS = ("lie", "truth", "unverifiable", "compound")
HARD = ("SUPPORTED", "CONTRADICTED")
# atom types that share a verdict rule; promotion for the key is copied to the aliases (§4)
TYPE_ALIASES = {"road_surface": ("weather",)}
PRESENCE_JURY_TYPES = ("towing", "heavy_vehicle_kind")   # T2 presence rule; the jury-size curve runs on these
DEFAULT_ALPHA_PRIOR = 0.27                              # §7: Cosmos3-Super VANTAGE non-event acceptance


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def ts_slug() -> str:
    return time.strftime("%Y%m%dT%H%M%S", time.gmtime())


# ---------------------------------------------------------------- claims
def load_claims(path: Path = CLAIMS_PATH, split: Optional[str] = None) -> list[dict]:
    rows = yaml.safe_load(Path(path).read_text())["claims"]
    for r in rows:
        r.setdefault("notes", "")
        r.setdefault("hero", False)
        r.setdefault("sycophancy", False)
        r["expected_claim"] = str(r["expected_claim"])  # YAML would read bare TRUE/FALSE as bools
    return [r for r in rows if split is None or r["split"] == split]


# ---------------------------------------------------------------- stats
def _wilson_local(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n <= 0:
        return (0.0, 1.0)
    p = k / n
    den = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0.0, centre - half), min(1.0, centre + half))


def wilson_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    try:
        from perjury.quorum import wilson_ci as q  # noqa: WPS433
        lo, hi = q(k, n)
        if 0.0 <= float(lo) <= float(hi) <= 1.0:
            return (float(lo), float(hi))
    except Exception:
        pass
    return _wilson_local(k, n, z)


def rate(k: int, n: int) -> dict:
    """{"k","n","rate","ci"}: the shape of every metric in bench_report.json."""
    if n == 0:
        return {"k": k, "n": 0, "rate": None, "ci": None}
    lo, hi = wilson_ci(k, n)
    return {"k": k, "n": n, "rate": round(k / n, 4), "ci": [round(lo, 4), round(hi, 4)]}


def p_at_least(m: int, k: int, alpha: float) -> float:
    """P(Y >= m | absent) for k independent jurors with false-yes rate alpha."""
    return 1.0 - sum(math.comb(k, i) * alpha ** i * (1 - alpha) ** (k - i) for i in range(m))


def _choose_m_local(alpha: float, k: int, target: float = 0.05, max_m: int = 4) -> Optional[int]:
    for m in range(1, k + 1):
        if p_at_least(m, k, alpha) <= target:
            return m if m <= max_m else None
    return None


def choose_m(alpha: float, k: int, target: float = 0.05, max_m: int = 4) -> Optional[int]:
    """Smallest m with P(Y>=m | absent) <= target (§7); None = demote (m would be >= 5)."""
    try:
        from perjury.quorum import choose_m as q  # noqa: WPS433
        m = q(alpha, k)
        return None if m is None or m > max_m else int(m)
    except Exception:
        return _choose_m_local(alpha, k, target, max_m)


def claim_verdict(atom_labels: Iterable[str]) -> str:
    """§4: FALSE if any CONTRADICTED; TRUE if every non-MOOT atom is SUPPORTED; else UNPROVEN."""
    labels = list(atom_labels)
    if any(v == "CONTRADICTED" for v in labels):
        return "FALSE"
    live = [v for v in labels if v != "MOOT"]
    return "TRUE" if live and all(v == "SUPPORTED" for v in live) else "UNPROVEN"


# ---------------------------------------------------------------- atom matching
def _norm(s: str) -> str:
    return " ".join(s.lower().strip(" .,!?").split())


def match_atoms(expected: list[dict], atoms: list[dict], atom_verdicts: list[dict]) -> list[dict]:
    """Pair each expected atom with at most one predicted atom by span (exact > containment), preferring same type.

    Returns one row per expected atom: {span, type, expected, got, atom_id, pred_type, correct}.
    `got` is "MISSING" when the atomizer produced no overlapping span (counts as wrong).
    """
    by_id = {v.get("atom_id"): v for v in atom_verdicts}
    used: set[str] = set()
    out = []
    for e in expected:
        es = _norm(e["span"])
        best, best_score = None, -1
        for a in atoms:
            if a.get("id") in used:
                continue
            ps = _norm(a.get("span", ""))
            if not ps:
                continue
            if ps == es:
                score = 3
            elif es in ps or ps in es:
                score = 2
            else:
                continue
            if str(a.get("type")) == e["type"]:
                score += 1
            if score > best_score:
                best, best_score = a, score
        if best is None:
            out.append({**e, "got": "MISSING", "atom_id": None, "pred_type": None, "correct": False})
            continue
        used.add(best["id"])
        got = (by_id.get(best["id"]) or {}).get("verdict", "MISSING")
        out.append({**e, "got": got, "atom_id": best["id"], "pred_type": str(best.get("type")),
                    "correct": got == e["expected"]})
    return out


# ---------------------------------------------------------------- run files
def run_path(split: str, variant: str = "neutral") -> Path:
    tag = split if variant == "neutral" else f"{split}_{variant}"
    return RUNS_DIR / f"{tag}_{ts_slug()}.json"


def save_run(run: dict, path: Optional[Path] = None) -> Path:
    path = path or run_path(run["split"], run.get("variant", "neutral"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(run, indent=1, default=str))
    return path


def list_runs(runs_dir: Path = RUNS_DIR) -> list[dict]:
    out = []
    for p in sorted(runs_dir.glob("*.json")):
        try:
            r = json.loads(p.read_text())
        except Exception:
            continue
        r["_path"] = str(p)
        out.append(r)
    return out


def latest_run(split: str, variant: str = "neutral", runs_dir: Path = RUNS_DIR,
               mode: Optional[str] = None) -> Optional[dict]:
    """Newest run for (split, variant). Live runs beat fixture runs regardless of age, unless `mode` is given."""
    runs = [r for r in list_runs(runs_dir) if r.get("split") == split and r.get("variant", "neutral") == variant]
    if mode:
        runs = [r for r in runs if r.get("mode") == mode]
    if not runs:
        return None
    live = [r for r in runs if r.get("mode") == "live"]
    pool = live or runs
    return max(pool, key=lambda r: r.get("finished_at") or r.get("started_at") or "")


def promotion_path(mode: str) -> Path:
    """Live runs freeze to cache/promotion.json (read by the router); fixture runs never touch it."""
    return CACHE / ("promotion.json" if mode == "live" else "fixture_promotion.json")


def test_lock_path(mode: str) -> Path:
    return CACHE / ("test_run.lock" if mode == "live" else "fixture_test_run.lock")
