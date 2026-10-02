"""Quorum math and verdict rules (FINAL-IDEA-v3 §7). Pure functions: no I/O, no clients, no randomness.

Each rule returns a `Rule` (verdict label + reason_code + stats). Template text lives in perjury/verdict.py.
Notation (§7): Y = yes votes that passed P-GROUND + YOLO zoom-check, N = no votes, k = jurors summoned,
k' = Y + N valid jurors, alpha = a juror's false-yes rate after the zoom-check.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Iterable, Optional, Sequence

from perjury.types import Atom, AtomVerdict, ClaimVerdictLabel

MAX_M = 4                 # §7: m >= 5 => the type is demoted
NOISE_FLOOR_FRAMES = 3    # §7: a camera "has" a COCO class only with >= 3 consecutive sidecar frames
SCENE_MIN_VALID = 8       # §7: scene-wide majority needs k' >= 8
ABSENCE_ZERO_FRACTION = 14 / 16   # §7: >= 14 of 16 P-COUNT jurors report 0


@dataclass
class Rule:
    verdict: str                       # SUPPORTED | CONTRADICTED | UNVERIFIABLE
    reason_code: str
    stats: dict[str, Any] = field(default_factory=dict)


# ---- binomial quorum (§7 "Choosing m from the measured alpha") ----
def p_at_least(m: int, k: int, alpha: float) -> float:
    """P(Y >= m | absent) for k independent jurors with false-yes rate alpha."""
    if m <= 0:
        return 1.0
    if m > k:
        return 0.0
    return 1.0 - sum(math.comb(k, i) * alpha ** i * (1 - alpha) ** (k - i) for i in range(m))


def choose_m(alpha: float, k: int = 6, target: float = 0.05, max_m: int = MAX_M) -> Optional[int]:
    """Smallest m with P(Y >= m | absent) <= target. None when m would exceed max_m (=> demote the type)."""
    for m in range(1, k + 2):
        if p_at_least(m, k, alpha) <= target:
            return m if m <= max_m else None
    return None


def wilson_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson 95% interval for k successes out of n (§8 metrics). (0, 1) when n == 0."""
    if n <= 0:
        return (0.0, 1.0)
    p = k / n
    den = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0.0, centre - half), min(1.0, centre + half))


# ---- presence (towing, heavy_vehicle_kind) ----
def min_valid_for_absence(k: int) -> int:
    """§7 "k' >= 5 of 6", scaled for other jury sizes (k=16 -> 14). Never below 1."""
    return max(1, math.ceil(5 * k / 6))


def presence_verdict(Y: int, N: int, k: int, m: Optional[int], *, retrieved_top: bool,
                     t1_supports: int, t1_complete: bool = True) -> Rule:
    """§7 presence rule. Y counts only yes votes that passed P-GROUND and the zoom-check.

    SUPPORTED    Y >= m.
    CONTRADICTED Y = 0, k' >= 5 of 6, jurors saw the most claim-like moments, and T1 has 0 supporting captions
                 (t1_complete: every synonym-matching caption was labelled; otherwise T1 silence is unproven).
    UNVERIFIABLE otherwise (also when m is None: the type would need m >= 5).
    """
    kv = Y + N
    need = min_valid_for_absence(k)
    stats = {"Y": Y, "N": N, "k": k, "k_valid": kv, "m": m, "min_valid": need,
             "retrieved_top": retrieved_top, "t1_supports": t1_supports}
    if m is not None and Y >= m:
        return Rule("SUPPORTED", "quorum", stats)
    if Y == 0 and kv >= need and retrieved_top and t1_supports == 0 and t1_complete:
        return Rule("CONTRADICTED", "absent_everywhere", stats)
    if m is None:
        return Rule("UNVERIFIABLE", "m_too_high", stats)
    if kv < need and Y == 0:
        return Rule("UNVERIFIABLE", "too_few_valid", stats)
    if Y == 0 and t1_supports > 0:
        return Rule("UNVERIFIABLE", "captions_disagree", stats)
    return Rule("UNVERIFIABLE", "no_quorum", stats)


# ---- scene-wide majority (road_surface, weather, traffic_state, lighting) ----
def two_thirds(k_valid: int) -> int:
    return math.ceil(2 * k_valid / 3)


def scene_majority_verdict(answers: Sequence[Optional[str]], target: str, *, t1_supports: int = 0,
                           t1_contradicts: int = 0, min_valid: int = SCENE_MIN_VALID) -> Rule:
    """§7 majority quorum over the pre-run P-COND jurors.

    answers: one option letter per juror; "D" (cannot tell) or None (invalid/missing) abstain.
    SUPPORTED    >= ceil(2/3 k') pick `target`, k' >= 8, and T1 CONTRADICTS do not outnumber SUPPORTS.
    CONTRADICTED >= ceil(2/3 k') pick a different option, k' >= 8, and T1 is not net-supporting.
    """
    valid = [a for a in answers if a and a != "D"]
    kv = len(valid)
    match = sum(1 for a in valid if a == target)
    other = kv - match
    need = two_thirds(kv)
    stats = {"k": len(answers), "k_valid": kv, "match": match, "other": other, "need": need,
             "target": target, "t1_supports": t1_supports, "t1_contradicts": t1_contradicts}
    if kv < min_valid:
        return Rule("UNVERIFIABLE", "too_few_valid", stats)
    if match >= need and t1_contradicts <= t1_supports:
        return Rule("SUPPORTED", "majority", stats)
    if other >= need and t1_supports <= t1_contradicts:
        return Rule("CONTRADICTED", "majority_other", stats)
    if match >= need or other >= need:
        return Rule("UNVERIFIABLE", "captions_disagree", stats)
    return Rule("UNVERIFIABLE", "no_majority", stats)


# ---- COCO classes (person, bicycle, motorcycle, car, bus, truck) ----
def yolo_cameras_over_floor(persist_by_camera: dict[str, int], floor: int = NOISE_FLOOR_FRAMES) -> list[str]:
    """Cameras whose longest run of consecutive sidecar frames with the class reaches the noise floor."""
    return sorted(c for c, p in persist_by_camera.items() if p >= floor)


def coco_absence_verdict(persist_by_camera: dict[str, int], jury_counts: Optional[Sequence[Optional[int]]],
                         *, floor: int = NOISE_FLOOR_FRAMES) -> Rule:
    """§7 COCO absence: CONTRADICTED (the class is absent) needs BOTH
    YOLO: no camera has the class in >= `floor` consecutive sidecar frames, and
    jury: >= 14/16 of P-COUNT jurors report 0 with the rest abstaining (None = abstain).
    jury_counts None => this class has no jury leg => never CONTRADICTED.
    """
    over = yolo_cameras_over_floor(persist_by_camera, floor)
    stats: dict[str, Any] = {"yolo_cameras": len(over), "floor": floor}
    if jury_counts is None:
        stats["jury"] = None
        return Rule("UNVERIFIABLE", "no_jury_leg", stats)
    k = len(jury_counts)
    zeros = sum(1 for c in jury_counts if c == 0)
    seen = sum(1 for c in jury_counts if c is not None and c > 0)
    need = max(1, math.ceil(ABSENCE_ZERO_FRACTION * k))
    stats.update({"k": k, "zeros": zeros, "seen": seen, "abstain": k - zeros - seen, "need_zeros": need})
    if not over and seen == 0 and zeros >= need:
        return Rule("CONTRADICTED", "absent_everywhere", stats)
    return Rule("UNVERIFIABLE", "absence_unproven", stats)


def coco_presence_verdict(persist_by_camera: dict[str, int], jury_counts: Optional[Sequence[Optional[int]]],
                          *, floor: int = NOISE_FLOOR_FRAMES, min_cameras: int = 2) -> Rule:
    """§7 COCO presence: SUPPORTED needs YOLO in >= 2 cameras (over the noise floor) AND >= 2 P-COUNT jurors.
    Classes without a P-COUNT field (car, bus, truck) are decided by YOLO alone (jury_counts None)."""
    over = yolo_cameras_over_floor(persist_by_camera, floor)
    stats: dict[str, Any] = {"yolo_cameras": len(over), "floor": floor}
    yolo_ok = len(over) >= min_cameras
    if jury_counts is None:
        stats["jury"] = None
        return Rule("SUPPORTED" if yolo_ok else "UNVERIFIABLE", "yolo_only" if yolo_ok else "presence_unproven", stats)
    seen = sum(1 for c in jury_counts if c is not None and c > 0)
    stats.update({"k": len(jury_counts), "seen": seen})
    if yolo_ok and seen >= min_cameras:
        return Rule("SUPPORTED", "yolo_and_jury", stats)
    return Rule("UNVERIFIABLE", "presence_unproven", stats)


def coco_verdict(persist_by_camera: dict[str, int], jury_counts: Optional[Sequence[Optional[int]]],
                 *, negated: bool = False, floor: int = NOISE_FLOOR_FRAMES) -> Rule:
    """Atom-level COCO verdict: presence claim ("there are pedestrians") or negated ("there are no pedestrians")."""
    absent = coco_absence_verdict(persist_by_camera, jury_counts, floor=floor)
    present = coco_presence_verdict(persist_by_camera, jury_counts, floor=floor)
    stats = {**absent.stats, **present.stats}
    if absent.verdict == "CONTRADICTED":
        return Rule("SUPPORTED" if negated else "CONTRADICTED", "absent_everywhere", stats)
    if present.verdict == "SUPPORTED":
        return Rule("CONTRADICTED" if negated else "SUPPORTED", present.reason_code, stats)
    return Rule("UNVERIFIABLE", "no_agreement", stats)


# ---- counts (§4: lower bounds SUPPORTED only; never CONTRADICTED) ----
def count_lower_bound_verdict(peak_by_camera: dict[str, int], n: int, op: Optional[str],
                              *, min_cameras: int = 2) -> Rule:
    """at_least n: peak concurrent count >= n in >= 2 cameras -> SUPPORTED, else UNVERIFIABLE.
    exact / at_most / unknown op: UNVERIFIABLE (peak-concurrent counts miss far lanes)."""
    cams = sorted(c for c, p in peak_by_camera.items() if p >= n)
    stats = {"n": n, "op": op, "cameras_at_or_above": len(cams), "max_peak": max(peak_by_camera.values(), default=0)}
    if op != "at_least":
        return Rule("UNVERIFIABLE", "count_not_testable", stats)
    if len(cams) >= min_cameras:
        return Rule("SUPPORTED", "lower_bound", stats)
    return Rule("UNVERIFIABLE", "lower_bound_unproven", stats)


# ---- claim level (§4 "Claim-level verdict (code)") ----
def moot_ids(atoms: Iterable[Atom], verdicts: dict[str, str]) -> set[str]:
    """Atoms whose depends_on parent (transitively) is CONTRADICTED or MOOT."""
    by_id = {a.id: a for a in atoms}
    out: set[str] = set()

    def is_moot(aid: str, seen: frozenset) -> bool:
        a = by_id.get(aid)
        if a is None or not a.depends_on or a.depends_on in seen or a.depends_on not in by_id:
            return False
        p = a.depends_on
        return verdicts.get(p) in ("CONTRADICTED", "MOOT") or is_moot(p, seen | {aid})

    for aid in by_id:
        if is_moot(aid, frozenset()):
            out.add(aid)
    return out


def claim_verdict(atom_verdicts: Sequence[AtomVerdict], atoms: Sequence[Atom] = ()) -> ClaimVerdictLabel:
    """FALSE if any atom is CONTRADICTED; TRUE if every non-MOOT atom is SUPPORTED; else UNPROVEN.
    `atoms` (optional) lets dependency MOOTs be derived here too."""
    labels = {v.atom_id: v.verdict for v in atom_verdicts}
    moot = moot_ids(atoms, labels) if atoms else set()
    live = [v for v in atom_verdicts if v.verdict != "MOOT" and v.atom_id not in moot]
    if any(v.verdict == "CONTRADICTED" for v in live):
        return "FALSE"
    if live and all(v.verdict == "SUPPORTED" for v in live):
        return "TRUE"
    return "UNPROVEN"
