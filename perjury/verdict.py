"""Template explanations and pill text (FINAL-IDEA-v3 §7, §9). No LLM writes a verdict or its reason.

reason(...)       one sentence per atom verdict, from the rule's reason_code + stats
pill(...)         the atom pill's evidence line, e.g. "YOLO: person in 0 of 192 segments · jury: 0 people seen by 16/16"
explain_claim()   the claim-level "Why" under the verdict stamp
"""
from __future__ import annotations

from typing import Any, Optional, Sequence

from perjury.types import Atom, AtomType, AtomVerdict

OPTION_TEXT = {
    "road": {"A": "dry", "B": "wet", "C": "snow or slush on or beside the road", "D": "cannot tell"},
    "traffic": {"A": "moving freely at speed", "B": "slow but moving", "C": "stop-and-go or queued", "D": "cannot tell"},
    "light": {"A": "daylight", "B": "dusk or dawn", "C": "night", "D": "cannot tell"},
}
_SING = {"person": "person", "bicycle": "bicycle", "motorcycle": "motorcycle", "car": "car", "bus": "bus", "truck": "truck"}
_PLUR = {"person": "people", "bicycle": "bicycles", "motorcycle": "motorcycles", "car": "cars", "bus": "buses",
         "truck": "trucks"}


def noun(cls: Optional[str], plural: bool = False) -> str:
    return (_PLUR if plural else _SING).get(cls or "", cls or "object")


def _t1_phrase(s: dict) -> str:
    t1 = s.get("t1")
    if not t1:
        return ""
    return (f"; captions: {t1.get('supports', 0)} support, {t1.get('contradicts', 0)} contradict "
            f"of {t1.get('total', 0)}")


# ---- per-atom reasons ----
def reason(atom: Atom, code: str, s: dict[str, Any], fallback: str = "") -> str:
    """Template sentence for one atom verdict. `s` is the AtomVerdict.stats dict."""
    cls = atom.cls
    if code == "absent_everywhere" and atom.type == AtomType.coco_presence:
        segs, total = s.get("segments_with", 0), s.get("segments_total", 0)
        yolo = (f"No {noun(cls)} was detected in any of {total} segments" if segs == 0 else
                f"YOLO flagged a {noun(cls)} in {segs} of {total} segments but never for "
                f"{s.get('floor', 3)}+ consecutive frames")
        return f"{yolo}; {s.get('zeros', 0)}/{s.get('k', 0)} cameras count 0."
    if code in ("yolo_and_jury", "yolo_only"):
        jury = f" and {s.get('seen', 0)}/{s.get('k', 0)} jurors count at least one" if code == "yolo_and_jury" else ""
        return (f"YOLO sees a {noun(cls)} for {s.get('floor', 3)}+ consecutive frames on "
                f"{s.get('yolo_cameras', 0)} of {s.get('cameras', 0)} cameras{jury}.")
    if code == "no_agreement":
        return (f"YOLO and the jury did not agree on {noun(cls, True)}: YOLO on {s.get('yolo_cameras', 0)} cameras, "
                f"jurors on {s.get('seen', 0)}/{s.get('k', 0) or '-'}.")
    if code in ("majority", "majority_other", "captions_disagree", "no_majority", "too_few_valid") and "target" in s:
        q = s.get("question", "road")
        opt = OPTION_TEXT.get(q, {}).get(s.get("target", ""), s.get("target", ""))
        if code == "majority":
            return f"{s['match']}/{s['k_valid']} cameras answered “{opt}”{_t1_phrase(s)}."
        if code == "majority_other":
            top = OPTION_TEXT.get(q, {}).get(s.get("top_other", ""), s.get("top_other", "something else"))
            return f"{s['other']}/{s['k_valid']} cameras answered otherwise (mostly “{top}”){_t1_phrase(s)}."
        if code == "too_few_valid":
            return f"Only {s['k_valid']} of {s['k']} cameras gave a usable answer (need 8)."
        if code == "captions_disagree":
            return f"Cameras {s['match']}/{s['k_valid']} for “{opt}”, but captions disagree{_t1_phrase(s)}."
        return f"No 2/3 majority: {s['match']}/{s['k_valid']} cameras answered “{opt}”{_t1_phrase(s)}."
    if code == "quorum":
        zoom = ", each confirmed by a Cosmos box and a YOLO zoom-check" if s.get("zoom_required", True) else ""
        return f"{s['Y']}/{s['k']} jurors saw it{zoom} (quorum m={s['m']})."
    if code == "absent_everywhere":
        caps = (s.get("t1") or {}).get("total", 0)
        return (f"0/{s['k']} jurors saw it in the {s['k']} most claim-like moments of the scene "
                f"({s['k_valid']} answered), and 0 of {caps} captions mention it.")
    if code == "no_quorum":
        return f"Only {s.get('Y', 0)}/{s.get('k', 0)} confirmed yes votes (quorum m={s.get('m')}); not enough either way."
    if code == "too_few_valid" and "Y" in s:
        return f"Only {s['k_valid']}/{s['k']} jurors gave a usable answer (need {s['min_valid']})."
    if code == "captions_disagree" and "Y" in s:
        return f"No juror confirmed it, but {s.get('t1_supports', 0)} captions mention it."
    if code == "m_too_high":
        return f"At alpha={s.get('alpha')} a jury of {s.get('k')} cannot reach a 5% false-yes quorum."
    if code == "lower_bound":
        return f"YOLO's peak count reaches {s['n']} {noun(cls, True)} on {s['cameras_at_or_above']} cameras."
    if code == "lower_bound_unproven":
        return (f"YOLO's peak count reaches {s['n']} {noun(cls, True)} on only {s['cameras_at_or_above']} camera(s); "
                f"counts are never contradicted (YOLO undercounts far lanes).")
    if code == "metadata_match":
        return f"Pack metadata ({s.get('pack_desc', '')}) matches “{atom.span}”."
    if code == "metadata_mismatch":
        return f"Pack metadata ({s.get('pack_desc', '')}) contradicts “{atom.span}”."
    if code == "jury_timeout":
        return "The jury timed out; no verdict is guessed."
    if code == "moot":
        return "Moot: the thing it depends on was contradicted."
    return fallback or "Not testable here."


# ---- pill text ----
def pill(atom: Atom, av: AtomVerdict) -> str:
    s = av.stats
    parts: list[str] = []
    if atom.type == AtomType.coco_presence and "segments_total" in s:
        parts.append(f"YOLO: {noun(atom.cls)} in {s.get('segments_with', 0)} of {s['segments_total']} segments")
        if s.get("k"):
            if s.get("seen", 0) == 0:
                parts.append(f"jury: 0 {noun(atom.cls, True)} seen by {s.get('zeros', 0)}/{s['k']}")
            else:
                parts.append(f"jury: {noun(atom.cls, True)} seen by {s['seen']}/{s['k']}")
    elif "target" in s and "k_valid" in s:
        against = av.verdict == "CONTRADICTED"
        parts.append(f"JURY {s['other']}/{s['k_valid']} against" if against else f"JURY {s['match']}/{s['k_valid']}")
        t1 = s.get("t1")
        if t1:
            parts.append(f"CAPTIONS {t1.get('contradicts', 0)}/{t1.get('total', 0)} against" if against
                         else f"CAPTIONS {t1.get('supports', 0)}/{t1.get('total', 0)}")
    elif "Y" in s:
        parts.append(f"JURY {s['Y']}/{s['k']}" + (f" · m={s['m']}" if s.get("m") else ""))
        if s.get("t1"):
            parts.append(f"CAPTIONS {s['t1'].get('supports', 0)}/{s['t1'].get('total', 0)}")
    elif "cameras_at_or_above" in s:
        parts.append(f"RECORDS peak≥{s['n']} on {s['cameras_at_or_above']} cams")
    elif "pack_desc" in s:
        parts.append(f"RECORDS {s['pack_desc']}")
    if av.verdict == "MOOT":
        return "moot"
    if av.verdict == "UNVERIFIABLE" and not parts:
        return av.reason_code.replace("_", " ") or "unverifiable"
    return " · ".join(parts)


# ---- claim level ----
def explain_claim(verdict: str, atoms: Sequence[Atom], avs: Sequence[AtomVerdict]) -> str:
    by_id = {a.id: a for a in atoms}
    span = lambda v: by_id[v.atom_id].span if v.atom_id in by_id else v.atom_id  # noqa: E731
    live = [v for v in avs if v.verdict != "MOOT"]
    moot = [v for v in avs if v.verdict == "MOOT"]
    if verdict == "FALSE":
        bad = [v for v in avs if v.verdict == "CONTRADICTED"]
        text = " ".join(f"“{span(v)}”: {v.reason}" for v in bad)
        if moot:
            text += f" ({len(moot)} dependent atom{'s' if len(moot) > 1 else ''} moot.)"
        return text
    if verdict == "TRUE":
        return f"All {len(live)} testable atoms supported. " + " ".join(f"“{span(v)}”: {v.reason}" for v in live)
    sup = sum(1 for v in live if v.verdict == "SUPPORTED")
    unv = [v for v in live if v.verdict == "UNVERIFIABLE"]
    text = f"Supported as far as the pixels go: {sup} of {len(live)} atoms."
    if unv:
        text += " Not testable: " + "; ".join(f"“{span(v)}” ({v.reason_code.replace('_', ' ')})" for v in unv) + "."
    return text
