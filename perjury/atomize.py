"""Atomizer (FINAL-IDEA-v3 §6): one statement -> closed-set atoms whose spans are exact substrings of the transcript.

LLM path: Nemotron via ctx.clients.llm.complete_json(ATOMIZER_SYSTEM, ...), then code validates every atom
(span substring, closed type set, COCO class mapping, counts split out, dependencies). Rules path: a regex parser
for the golden phrasings, used when the LLM errors, 429s, returns nothing or nothing valid (and always in fixture
mode, where the fake LLM declines). The trace labels which one ran ("llm" | "rules").
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Optional

import yaml

from perjury.obs import op
from perjury.probes import ATOMIZER_SYSTEM, atomizer_user
from perjury.types import COCO_CLASSES, Atom, AtomType

TYPES_PATH = Path(__file__).with_name("claim_types.yaml")
SUBJECT_TYPES = {AtomType.coco_presence, AtomType.towing, AtomType.heavy_vehicle_kind}
DEPENDENT_TYPES = {AtomType.action, AtomType.attribute, AtomType.identity_intent, AtomType.lane_position}

# ---- lexicon ----
NUMBER_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
                "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "a dozen": 12, "a couple of": 2,
                "a pair of": 2, "a few": 3, "several": 3, "dozens of": 24}
CLASS_WORDS: dict[str, str] = {
    # person
    "pedestrians": "person", "pedestrian": "person", "people": "person", "persons": "person", "person": "person",
    "men": "person", "man": "person", "women": "person", "woman": "person", "kids": "person", "kid": "person",
    "children": "person", "child": "person", "walkers": "person", "walker": "person", "joggers": "person",
    "jogger": "person", "workers": "person", "worker": "person", "hitchhiker": "person", "someone": "person",
    "somebody": "person", "boy": "person", "girl": "person",
    # bicycle
    "cyclists": "bicycle", "cyclist": "bicycle", "bicyclists": "bicycle", "bicyclist": "bicycle",
    "bicycles": "bicycle", "bicycle": "bicycle", "bikes": "bicycle", "bike": "bicycle",
    # motorcycle
    "motorcyclists": "motorcycle", "motorcyclist": "motorcycle", "motorcycles": "motorcycle",
    "motorcycle": "motorcycle", "motorbikes": "motorcycle", "motorbike": "motorcycle", "scooters": "motorcycle",
    "scooter": "motorcycle",
    # car (COCO "car" covers sedans, SUVs, vans)
    "cars": "car", "car": "car", "sedans": "car", "sedan": "car", "suvs": "car", "suv": "car", "minivans": "car",
    "minivan": "car", "vans": "car", "van": "car", "jeeps": "car", "jeep": "car", "vehicles": "car", "vehicle": "car",
    "hatchback": "car", "coupe": "car",
    # truck (COCO "truck" covers pickups)
    "pickup trucks": "truck", "pickup truck": "truck", "pickups": "truck", "pickup": "truck", "trucks": "truck",
    "truck": "truck", "lorries": "truck", "lorry": "truck",
    # bus
    "buses": "bus", "busses": "bus", "bus": "bus", "coaches": "bus", "coach": "bus",
}
NEGATED_PERSON = ("nobody", "no one", "no-one")
_TOW_VEHICLE = {"pickup": "pickup", "pickups": "pickup", "pickup truck": "pickup", "suv": "suv", "jeep": "suv",
                "van": "van", "minivan": "van", "car": "car", "sedan": "car"}


def _alt(words) -> str:
    return "|".join(re.escape(w) for w in sorted(words, key=len, reverse=True))


_CLASS_RE = re.compile(rf"\b(?P<w>{_alt(CLASS_WORDS)})(?:'s|’s)?\b", re.I)
_NUM_ALT = rf"\d+|{_alt(NUMBER_WORDS)}"
_COUNT_BEFORE_RE = re.compile(
    rf"(?P<q>(?:(?P<op>at least|no fewer than|no less than|more than|over|exactly|precisely|just|only|at most|"
    rf"no more than|fewer than|less than|up to)\s+)?(?P<num>{_NUM_ALT}))\s+(?:(?!(?:are|is|were|was)\b)[\w-]+\s+){{0,2}}$",
    re.I)
_NEG_BEFORE_RE = re.compile(r"\b(?:no|zero|not any|not a single|without any|without)\s+(?:[\w-]+\s+)?$", re.I)


@dataclass
class _M:
    start: int
    end: int
    type: AtomType
    fields: dict[str, Any] = field(default_factory=dict)
    subject_pref: str = "before"     # dependent atoms: look for the subject before or after the span first
    tag: Optional[str] = None         # links a count to its presence atom


def _table() -> dict:
    return _load_table(str(TYPES_PATH))


@lru_cache(maxsize=4)
def _load_table(path: str) -> dict:
    return yaml.safe_load(Path(path).read_text())


# ---- pattern tables (rules parser + value normaliser). Order inside a list = priority. ----
ROAD = [
    ("snow", r"(?:covered|blanketed|caked) (?:in|with) snow|snow[- ]covered|snow (?:on|beside|along|by|next to|at the side of) "
             r"(?:the )?(?:road|roadway|highway|shoulders?|median|edges?)|in the snow|snowy|snowbanks?|slush(?:y)?|"
             r"\bicy\b|ice[- ]covered|\bsnow\b"),
    ("dry", r"dry (?:road|roadway|pavement|asphalt|conditions)|(?:road|roadway|pavement) is dry|\bdry\b"),
    ("wet", r"wet (?:road|roadway|pavement|asphalt|conditions)|(?:road|roadway|pavement) is wet|\bwet\b|puddles?"),
]
WEATHER = [
    ("snow", r"\bsnowing\b|\bsnowfall\b|\bblizzard\b|\bsnowstorm\b|\bflurries\b|\bit snows\b"),
    ("rain", r"\braining\b|\brainy\b|in the rain|\brain\b|\bdrizzl\w*|\bdownpour\b|\bpouring\b"),
    ("fog", r"\bfog(?:gy)?\b|\bmisty?\b|\bhaz[ey]\b"),
    ("clear", r"\bsunny\b|\bclear skies?\b|\bsunshine\b"),
]
TRAFFIC = [
    ("stop_and_go", r"stop[- ]and[- ]go|at a standstill|\bstandstill\b|gridlock(?:ed)?|bumper[- ]to[- ]bumper|"
                    r"traffic jam|\bjammed\b|\bcongested\b|\bcongestion\b|\bqueued\b|backed up|barely moving|crawling"),
    ("free_flow", r"(?:flowing|flows|flow|moving|moves|travel+ing|travels) freely(?: at (?:highway )?speed)?|"
                  r"free[- ]flowing(?: traffic)?|flowing smoothly|moving smoothly|at highway speed|light traffic"),
    ("slow", r"slow[- ]moving|moving slowly|moves slowly|slow traffic|traffic is slow|heavy but moving"),
]
LIGHT = [
    ("night", r"\bnight[- ]?time\b|\bat night\b|\bnight\b|after dark|in the dark|\bit(?:'s| is) dark\b"),
    ("day", r"\bday[- ]?time\b|\bbroad daylight\b|\bdaylight\b|during the day|\bdaytime\b"),
    ("dusk", r"\bdusk\b|\bdawn\b|\bsunset\b|\bsunrise\b|\btwilight\b"),
]
HEAVY = [
    ("semi", r"semi[- ]?trucks?|tractor[- ]trailers?|\bsemis?\b|18[- ]wheelers?|big rigs?"),
    ("box_truck", r"box trucks?"),
    ("dump_truck", r"dump trucks?"),
    ("tanker", r"\btankers?\b"),
    ("flatbed", r"\bflatbeds?\b"),
    ("car_carrier", r"car carriers?|car haulers?"),
]
ACTIONS = [
    ("lane_change", r"\bchang(?:ing|ed|es|e) (?:lanes?|into)\b|\bswitch(?:ing|ed|es)? lanes?\b"),
    ("speed", r"\b(?:doing|going|driving at|travel+ing at|moving at)\s+\d+\s*(?:mph|km/?h|kph|miles per hour)|"
              r"\bspeed(?:ing|s)\b|\bsped(?: up)?\b|\baccelerat\w+"),
    ("braking", r"\bbrak(?:ing|ed|es|e)\b(?: (?:hard|suddenly|abruptly|sharply)\b)?|"
                r"\bslam(?:med|s)? on (?:the|its|his|her) brakes\b"),
    ("collision", r"\bcollid(?:ing|ed|es|e)\b|\bcrash(?:ing|ed|es)?\b(?: into\b)?|\brear[- ]ended\b|\bsideswiped\b|\bhit\b"),
    ("crossing", r"\bcross(?:ing|ed|es)?\b"),
    ("walking", r"\bwalk(?:ing|ed|s)?\b|\brunning\b|\bran\b"),
    ("riding", r"\brid(?:ing|es|e)\b|\brode\b"),
    ("merging", r"\bmerg(?:ing|ed|es|e)\b"),
    ("slowing", r"\bslow(?:ing|ed|s)? down\b|\bdecelerat\w+"),
    ("stopping", r"\bstop(?:ping|ped|s)?\b|\bhalt(?:ing|ed|s)?\b"),
    ("cut_off", r"\bcut(?:ting|s)? (?:\w+ )?off\b"),
    ("turning", r"\bswerv(?:ing|ed|es|e)\b|\bturn(?:ing|ed|s)\b|\bu[- ]turn\b|\brevers(?:ing|ed|es|e)\b|\bbacking up\b"),
    ("passing", r"\bovert(?:aking|akes|ake|ook)\b|\bpass(?:ing|ed|es)?\b|\btailgat\w+"),
]
LANE = r"(?:the |a )?(?:far[- ]left|far[- ]right|left|right|middle|center|centre|inside|outside|fast|slow|passing|hov|exit)" \
       r" lanes?|on the shoulder|the shoulder|(?:in |into )?(?:both|opposite|the opposite|oncoming) directions?|" \
       r"\b(?:north|south|east|west)bound\b|wrong way"
CROSS_CAMERA = r"\b(?:the )?same (?:[\w-]+ ){0,2}(?:appears?|appeared|shows? up|showed up|is seen|was seen|is visible|passes)" \
               r"\b[^.;]*?\bcameras?\b|\bacross (?:\w+ )?cameras\b|from camera to camera"
PLATE = r"\b(?:the |its |his |her )?(?:licen[cs]e )?plate(?: number)? (?:reads|says|is|shows|was)\s*:?\s*['\"]?[A-Z0-9][A-Z0-9 -]{1,9}[A-Z0-9]['\"]?"
IDENTITY = r"\bdrivers? (?:was|is|were|seemed|appeared|looked) [\w-]+(?: (?:on|at|the|a|his|her|their|phone|wheel))*|" \
           r"\b(?:drunk|intoxicated|impaired)(?: driv(?:er|ing))?\b|\bon purpose\b|\bdeliberately\b|\bintentionally\b|" \
           r"\bat fault\b|\broad rage\b|\brecklessly\b|\breckless\b|\btexting\b|\bfell asleep\b"
TOWING = rf"(?P<veh>{_alt(list(_TOW_VEHICLE) + ['vehicle', 'truck', 'car'])})(?:'s|s)?\b(?:\s+(?!and\b)[\w-]+){{0,3}}?\s+" \
         r"(?:is |was |are |were )?(?:towing|tows|towed|pulling|pulls|pulled|hauling|hauls|dragging|with)\s+" \
         r"(?:an? |the |its |their )?(?:[\w-]+ ){0,2}?(?:trailers?|campers?|caravans?|boats?|car haulers?)\b"
COLORS = ("white", "black", "red", "blue", "green", "silver", "grey", "gray", "yellow", "orange", "brown", "gold",
          "beige", "tan", "maroon", "purple")
BRANDS = ("fedex", "ups", "usps", "dhl", "amazon", "walmart", "tesla", "ford", "toyota", "honda", "chevy", "chevrolet",
          "dodge", "gmc", "nissan", "bmw", "mercedes", "kenworth", "peterbilt", "freightliner", "volvo", "u-haul",
          "uhaul", "budget", "penske", "ryder", "coca-cola", "pepsi")
_CLASS_AHEAD = rf"(?=\s+(?:[\w-]+\s+)?(?:{_alt(CLASS_WORDS)}|semi|tractor|box truck)\b)"
ATTRIBUTE = rf"\b(?P<color>{_alt(COLORS)}){_CLASS_AHEAD}|\b(?P<brand>{_alt(BRANDS)})\b"
_GENERIC_ROAD = {"road", "the road", "multi-lane road", "multilane road"}


def _scene_terms() -> list[str]:
    terms: set[str] = set()
    for pack in _table()["types"]["scene_identity"]["packs"].values():
        terms |= set(pack.get("match", [])) | set(pack.get("mismatch", []))
    return sorted(terms - _GENERIC_ROAD, key=len, reverse=True)


def _scene_re() -> re.Pattern:
    return re.compile(rf"\b(?:{_alt(_scene_terms())})\b", re.I)


# ---- value normalisation (shared by both paths) ----
_VALUE_TABLES = {AtomType.road_surface: ROAD, AtomType.weather: WEATHER, AtomType.traffic_state: TRAFFIC,
                 AtomType.lighting: LIGHT, AtomType.heavy_vehicle_kind: HEAVY, AtomType.action: ACTIONS}


def normalize_value(t: AtomType, value: Optional[str], span: str) -> Optional[str]:
    """Map a free-text value/span to the canonical value keys used in claim_types.yaml."""
    table = _VALUE_TABLES.get(t)
    if table is None:
        return value.lower().strip() if isinstance(value, str) and value.strip() else value
    keys = {k for k, _ in table}
    if isinstance(value, str) and value.lower().replace("-", "_").replace(" ", "_") in keys:
        return value.lower().replace("-", "_").replace(" ", "_")
    for text in (value or "", span):
        for key, pat in table:
            if text and re.search(pat, text, re.I):
                return key
    return value.lower() if isinstance(value, str) else value


def map_class(word: Optional[str]) -> Optional[str]:
    if not word:
        return None
    w = re.sub(r"(?:'s|’s)$", "", word.lower().strip())
    if w in COCO_CLASSES:
        return w
    return CLASS_WORDS.get(w) or CLASS_WORDS.get(w + "s") or (CLASS_WORDS.get(w[:-1]) if w.endswith("s") else None)


def parse_number(s: str) -> Optional[int]:
    s = s.lower().strip()
    if s.isdigit():
        return int(s)
    return NUMBER_WORDS.get(s)


def count_op(quantifier: str) -> str:
    q = quantifier.lower()
    if re.search(r"at least|no fewer than|no less than|more than|\bover\b", q):
        return "at_least"
    if re.search(r"at most|no more than|fewer than|less than|up to", q):
        return "at_most"
    return "exact"


def _negated_before(text: str, start: int) -> bool:
    return bool(_NEG_BEFORE_RE.search(text[:start]))


# ---- rules parser ----
def _free(taken: list[tuple[int, int]], s: int, e: int) -> bool:
    return all(e <= a or s >= b for a, b in taken)


def _scan(text: str, pattern: str, taken: list, flags=re.I):
    for m in re.finditer(pattern, text, flags):
        if m.end() > m.start() and _free(taken, m.start(), m.end()):
            taken.append((m.start(), m.end()))
            yield m


def rules_parse(text: str) -> list[Atom]:
    """Deterministic parser for the golden phrasings (§8 bench). Every span is a slice of `text`."""
    taken: list[tuple[int, int]] = []
    ms: list[_M] = []
    for m in _scan(text, CROSS_CAMERA, taken):
        ms.append(_M(m.start(), m.end(), AtomType.cross_camera, {"value": "same_vehicle"}, "none"))
    for m in _scan(text, PLATE, taken):
        ms.append(_M(m.start(), m.end(), AtomType.attribute, {"value": "plate"}, "none"))
    for m in _scan(text, TOWING, taken):
        veh = _TOW_VEHICLE.get(m.group("veh").lower(), "any")
        s = m.start()
        art = re.search(r"\b(?:an?|the)\s+$", text[:s], re.I)       # include a leading article in the span
        ms.append(_M(art.start() if art else s, m.end(), AtomType.towing, {"towing_vehicle": veh}))
    for key, pat in HEAVY:
        for m in _scan(text, pat, taken):
            ms.append(_M(m.start(), m.end(), AtomType.heavy_vehicle_kind, {"value": key}))
    for typ, table in ((AtomType.weather, WEATHER), (AtomType.road_surface, ROAD), (AtomType.traffic_state, TRAFFIC),
                       (AtomType.lighting, LIGHT)):
        for key, pat in table:
            for m in _scan(text, pat, taken):
                ms.append(_M(m.start(), m.end(), typ, {"value": key}))
    for m in _scan(text, _scene_re().pattern, taken):
        ms.append(_M(m.start(), m.end(), AtomType.scene_identity, {"value": m.group(0).lower()}))
    for m in _scan(text, LANE, taken):
        ms.append(_M(m.start(), m.end(), AtomType.lane_position, {"value": m.group(0).lower()}))
    for m in _scan(text, IDENTITY, taken):
        ms.append(_M(m.start(), m.end(), AtomType.identity_intent, {"value": m.group(0).lower()}))
    for key, pat in ACTIONS:
        for m in _scan(text, pat, taken):
            ms.append(_M(m.start(), m.end(), AtomType.action, {"value": key}))
    for m in _scan(text, ATTRIBUTE, taken):
        kind = "color" if m.group("color") else "brand"
        ms.append(_M(m.start(), m.end(), AtomType.attribute, {"value": kind}, "after"))
    for m in _scan(text, rf"\b(?:{_alt(NEGATED_PERSON)})\b", taken):
        ms.append(_M(m.start(), m.end(), AtomType.coco_presence, {"cls": "person", "negated": True}))
    n_cls = 0
    for m in _CLASS_RE.finditer(text):
        s, e = m.start("w"), m.end("w")
        if not _free(taken, s, e):
            continue
        taken.append((s, e))
        n_cls += 1
        tag = f"c{n_cls}"
        cls = CLASS_WORDS[m.group("w").lower()]
        ms.append(_M(s, e, AtomType.coco_presence, {"cls": cls, "negated": _negated_before(text, s)}, tag=tag))
        c = _COUNT_BEFORE_RE.search(text[:s])
        if c and _free(taken, c.start("q"), c.end("q")):
            n = parse_number(c.group("num"))
            if n is not None:
                op_ = count_op(c.group("op") or "")
                if (c.group("op") or "").lower() in ("more than", "over"):
                    n += 1
                taken.append((c.start("q"), c.end("q")))
                ms.append(_M(c.start("q"), c.end("q"), AtomType.count,
                             {"cls": cls, "count": n, "count_op": op_}, tag=tag))
    if not ms:
        stripped = text.strip()
        if not stripped:
            return []
        s = text.index(stripped)
        ms.append(_M(s, s + len(stripped), AtomType.other, {}, "none"))
    return _finalize(text, ms)


def _finalize(text: str, ms: list[_M]) -> list[Atom]:
    ms.sort(key=lambda m: (m.start, m.end))
    ids = {id(m): f"a{i + 1}" for i, m in enumerate(ms)}
    subjects = [m for m in ms if m.type in SUBJECT_TYPES]
    presence_by_tag = {m.tag: m for m in ms if m.type == AtomType.coco_presence and m.tag}
    atoms = []
    for m in ms:
        dep = None
        if m.type == AtomType.count and m.tag in presence_by_tag:
            dep = ids[id(presence_by_tag[m.tag])]
        elif m.type in DEPENDENT_TYPES and m.subject_pref != "none":
            subj = _nearest_subject(m, subjects)
            dep = ids[id(subj)] if subj else None
        atoms.append(Atom(id=ids[id(m)], span=text[m.start:m.end], type=m.type, depends_on=dep, **m.fields))
    return atoms


def _nearest_subject(m: _M, subjects: list[_M]) -> Optional[_M]:
    before = [s for s in subjects if s.end <= m.start]
    after = [s for s in subjects if s.start >= m.end]
    b = max(before, key=lambda s: s.end) if before else None
    a = min(after, key=lambda s: s.start) if after else None
    return (a or b) if m.subject_pref == "after" else (b or a)


# ---- LLM path ----
def validate_llm_atoms(text: str, raw: Any) -> list[Atom]:
    """Code-side validation of the atomizer's JSON (§6). Drops any atom whose span is not an exact substring."""
    items = raw.get("atoms") if isinstance(raw, dict) else raw if isinstance(raw, list) else None
    if not isinstance(items, list):
        return []
    valid_types = {t.value for t in AtomType}
    ms: list[_M] = []
    old_ids: dict[str, _M] = {}
    deps: dict[int, str] = {}
    for i, it in enumerate(items):
        if not isinstance(it, dict):
            continue
        span = it.get("span")
        if not isinstance(span, str) or not span.strip() or span not in text:
            continue                                                   # hallucinated span: dropped
        start = _span_start(text, span, ms)
        t = AtomType(it["type"]) if it.get("type") in valid_types else AtomType.other
        f: dict[str, Any] = {}
        cls = it.get("class", it.get("cls"))
        if t in (AtomType.coco_presence, AtomType.count):
            f["cls"] = map_class(cls) or map_class(_class_in(span))
            if f["cls"] is None:
                t, f = AtomType.other, {}
        if t == AtomType.count:
            n = it.get("count")
            n = n if isinstance(n, int) else parse_number(str(n or "")) or _number_in(span)
            if n is None:
                t, f = AtomType.other, {}
            else:
                f.update(count=n, count_op=count_op(span))
        if t == AtomType.towing:
            tv = str(it.get("towing_vehicle") or "any").lower()
            f["towing_vehicle"] = tv if tv in ("pickup", "suv", "van", "car", "any") else "any"
        if t in _VALUE_TABLES or t in (AtomType.scene_identity, AtomType.attribute, AtomType.lane_position,
                                       AtomType.identity_intent):
            f["value"] = normalize_value(t, it.get("value"), span)
            if t == AtomType.attribute and re.search(r"\bplate\b", span, re.I):
                f["value"] = "plate"
            if t == AtomType.scene_identity and not f["value"]:
                f["value"] = span.lower()
        if t == AtomType.coco_presence:
            f["negated"] = _negated_before(text, start) or bool(re.match(r"\s*(?:no|zero)\b", span, re.I))
        m = _M(start, start + len(span), t, f)
        ms.append(m)
        if it.get("id"):
            old_ids[str(it["id"])] = m
        if it.get("depends_on"):
            deps[id(m)] = str(it["depends_on"])
        # rule 5: a presence atom carrying a count becomes presence + its own count atom
        if t == AtomType.coco_presence and isinstance(it.get("count"), int) and it["count"] > 0:
            c = _COUNT_BEFORE_RE.search(text[:start])
            cs, ce = (c.start("q"), c.end("q")) if c else (start, start + len(span))
            cm = _M(cs, ce, AtomType.count, {"cls": f["cls"], "count": it["count"],
                                            "count_op": count_op(c.group("op") or "") if c else "exact"})
            ms.append(cm)
            deps[id(cm)] = f"__obj{id(m)}"
    by_obj = {f"__obj{id(m)}": m for m in ms}
    # rule 7: ONE towing atom - drop presence/heavy atoms inside a towing span; dedupe identical atoms
    tows = [m for m in ms if m.type == AtomType.towing]
    seen, keep = set(), []
    for m in ms:
        if m.type in (AtomType.coco_presence, AtomType.heavy_vehicle_kind) and any(
                t.start <= m.start and m.end <= t.end for t in tows):
            continue
        key = (m.type, m.start, m.end, m.fields.get("cls"), m.fields.get("value"))
        if key in seen:
            continue
        seen.add(key)
        keep.append(m)
    keep_ids = {id(m) for m in keep}
    # counts without a presence parent get one synthesized from the class word in their span
    for m in list(keep):
        if m.type != AtomType.count:
            continue
        parent = old_ids.get(deps.get(id(m), "")) or by_obj.get(deps.get(id(m), ""))
        if parent is None or id(parent) not in keep_ids or parent.type != AtomType.coco_presence:
            parent = next((p for p in keep if p.type == AtomType.coco_presence and p.fields.get("cls") == m.fields["cls"]),
                          None)
            if parent is None:
                w = _CLASS_RE.search(text, m.start, m.end + 40)
                if w:
                    parent = _M(w.start("w"), w.end("w"), AtomType.coco_presence,
                                {"cls": m.fields["cls"], "negated": False})
                    keep.append(parent)
                    keep_ids.add(id(parent))
        if parent is not None:
            m.tag = f"__p{id(parent)}"
            parent.tag = m.tag
    return _finalize_llm(text, keep, deps, old_ids, by_obj)


def _finalize_llm(text: str, ms: list[_M], deps: dict[int, str], old_ids: dict[str, _M],
                  by_obj: dict[str, _M]) -> list[Atom]:
    ms.sort(key=lambda m: (m.start, m.end))
    ids = {id(m): f"a{i + 1}" for i, m in enumerate(ms)}
    subjects = [m for m in ms if m.type in SUBJECT_TYPES]
    parent_of: dict[int, Optional[_M]] = {}
    for m in ms:
        p = None
        if m.type == AtomType.count:
            p = next((x for x in ms if x.type == AtomType.coco_presence and x.tag and x.tag == m.tag), None)
        elif m.type in DEPENDENT_TYPES:
            p = old_ids.get(deps.get(id(m), "")) or by_obj.get(deps.get(id(m), ""))
            if p is None or id(p) not in ids or p.type not in SUBJECT_TYPES:
                p = _nearest_subject(m, subjects) if not (m.type == AtomType.attribute and
                                                          m.fields.get("value") == "plate") else None
        parent_of[id(m)] = p if p is not None and p is not m else None
    # break cycles: a parent may not (transitively) depend on its child
    for m in ms:
        seen, p = {id(m)}, parent_of[id(m)]
        while p is not None:
            if id(p) in seen:
                parent_of[id(m)] = None
                break
            seen.add(id(p))
            p = parent_of.get(id(p))
    return [Atom(id=ids[id(m)], span=text[m.start:m.end], type=m.type,
                 depends_on=ids[id(parent_of[id(m)])] if parent_of[id(m)] is not None else None, **m.fields)
            for m in ms]


def _span_start(text: str, span: str, ms: list[_M]) -> int:
    """First occurrence of span not already used by an atom of the same span."""
    pos = text.find(span)
    used = {m.start for m in ms if text[m.start:m.end] == span}
    while pos in used:
        nxt = text.find(span, pos + 1)
        if nxt < 0:
            break
        pos = nxt
    return pos


def _class_in(span: str) -> Optional[str]:
    m = _CLASS_RE.search(span)
    return m.group("w") if m else None


def _number_in(span: str) -> Optional[int]:
    m = re.search(rf"\b({_NUM_ALT})\b", span, re.I)
    return parse_number(m.group(1)) if m else None


@op("perjury.atomize")
async def atomize(text: str, llm: Any = None, *, bus: Any = None) -> tuple[list[Atom], str]:
    """Return (atoms, parser). parser = "llm" when the LLM produced >= 1 valid atom, else "rules"."""
    if llm is not None and text.strip():
        try:
            raw = await llm.complete_json(ATOMIZER_SYSTEM, atomizer_user(text), temperature=0.0, max_tokens=1200,
                                          bus=bus, purpose="atomize")
            atoms = validate_llm_atoms(text, raw)
            if atoms:
                # Preserve explicit pack/place claims even when the model folds
                # them into a traffic or road-condition atom. These are exact
                # transcript spans from the same routing lexicon as the rules
                # parser; they do not replace any other valid model atoms.
                for match in _scene_re().finditer(text):
                    span = match.group(0)
                    if not any(a.type == AtomType.scene_identity and
                               re.search(rf"\b{re.escape(span)}\b", a.value or a.span, re.I)
                               for a in atoms):
                        atoms.append(Atom(id=f"a{len(atoms) + 1}", span=span,
                                          type=AtomType.scene_identity, value=span.lower()))
                from perjury.trucks import split_coloured_truck
                return split_coloured_truck(text, atoms), "llm"
        except Exception as e:  # 429, timeout, bad JSON: the rules parser takes over (§17)
            if bus is not None:
                bus.service("wandb_inference", "fallback", note=f"atomizer: rules parser ({type(e).__name__})")
    from perjury.trucks import split_coloured_truck
    return split_coloured_truck(text, rules_parse(text)), "rules"


# ---- canonical statements (T1 input, templates) ----
def canonical(atom: Atom) -> str:
    """Plain one-sentence statement of the atom (no claim context leaks beyond the atom itself)."""
    t = atom.type
    vcfg = _table()["types"].get(t.value, {}).get("values", {}).get(atom.value or "", {})
    if vcfg.get("statement"):
        return vcfg["statement"]
    if t == AtomType.scene_identity:
        return f"The footage is from: {atom.span}."
    if t == AtomType.coco_presence:
        noun = _noun(atom.cls, 1)
        return f"There is no {noun} visible." if atom.negated else f"There is at least one {noun} visible."
    if t == AtomType.count:
        q = {"at_least": "at least ", "at_most": "at most ", "exact": "exactly "}.get(atom.count_op or "exact", "")
        return f"There are {q}{atom.count} {_noun(atom.cls, atom.count or 2)} visible."
    if t == AtomType.towing:
        veh = {"any": "A vehicle", "suv": "An SUV", "van": "A van", "car": "A car", "pickup": "A pickup"}.get(
            atom.towing_vehicle or "any", "A vehicle")
        return f"{veh} is towing a separate trailer."
    if t == AtomType.heavy_vehicle_kind:
        return f"There is a {(atom.value or atom.span).replace('_', ' ')} visible."
    return f"{atom.span[:1].upper()}{atom.span[1:]}."


def _noun(cls: Optional[str], n: int) -> str:
    sing = {"person": "person", "bicycle": "bicycle", "motorcycle": "motorcycle", "car": "car", "bus": "bus",
            "truck": "truck"}.get(cls or "", cls or "object")
    plur = {"person": "people", "bus": "buses"}.get(cls or "", sing + "s")
    return sing if n == 1 else plur
