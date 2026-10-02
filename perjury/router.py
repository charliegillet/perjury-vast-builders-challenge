"""Claim router (FINAL-IDEA-v3 §4): atom type -> tiers + verdict rule, with the frozen bench's promotion state.

claim_types.yaml holds the §4 table; cache/promotion.json (bench/run_bench.py --freeze) overrides `promoted`,
alpha and m per type. Types missing from the table are UNVERIFIABLE; demoted types render UNVERIFIABLE with
"demoted by bench".
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

import yaml

from perjury.config import CACHE
from perjury.quorum import choose_m
from perjury.types import Atom, AtomType, Tier

TYPES_PATH = Path(__file__).with_name("claim_types.yaml")
PROMOTION_PATH = CACHE / "promotion.json"
DEMOTED_REASON = "demoted by bench"


@dataclass
class Route:
    tiers: list[Tier]
    rule: str                                  # rule name; "unverifiable" when nothing may decide the atom
    hard: bool                                 # may issue SUPPORTED/CONTRADICTED right now
    reason_if_unverifiable: str
    reason_code: str = ""
    promoted: bool = True
    alpha: Optional[float] = None
    m: Optional[int] = None                    # quorum size for k = jury size (presence rules only)
    cfg: dict[str, Any] = field(default_factory=dict)   # the type's yaml block (values, synonyms, probe, ...)

    @property
    def demoted(self) -> bool:
        return not self.promoted and self.rule != "unverifiable"


class Router:
    def __init__(self, types_path: Path = TYPES_PATH, promotion_path: Optional[Path] = PROMOTION_PATH,
                 ignore_promotion: bool = False):
        self.table: dict[str, Any] = yaml.safe_load(Path(types_path).read_text())
        self.types: dict[str, dict] = self.table.get("types", {})
        self.alpha_prior: float = float(self.table.get("alpha_prior", 0.27))
        self.target: float = float(self.table.get("quorum_target", 0.05))
        self.noise_floor: int = int(self.table.get("noise_floor_frames", 3))
        self.promotion: dict[str, Any] = {}
        if promotion_path and Path(promotion_path).exists():
            self.promotion = json.loads(Path(promotion_path).read_text())
        self.ignore_promotion = ignore_promotion

    # ---- promotion state (§4 promotion rule) ----
    def promoted(self, type_name: str) -> bool:
        if self.ignore_promotion:
            return True
        frozen = self.promotion.get("types", {}).get(type_name)
        if frozen is not None and "promoted" in frozen:
            return bool(frozen["promoted"])
        return bool(self.types.get(type_name, {}).get("promoted", False))

    def alpha(self, type_name: str) -> float:
        return float(self.promotion.get("alpha", {}).get(type_name, self.alpha_prior))

    def m(self, type_name: str, k: int = 6) -> Optional[int]:
        """Frozen m (bench) when k is the stage jury size 6, else recomputed from alpha for this k."""
        frozen = self.promotion.get("m", {}).get(type_name)
        if frozen is not None and k == 6:
            return int(frozen)
        return choose_m(self.alpha(type_name), k, self.target)

    def state(self) -> dict[str, dict]:
        """Promotion state per type, for the Bench tab and /api/bench."""
        out = {}
        for t, cfg in self.types.items():
            frozen = self.promotion.get("types", {}).get(t, {})
            out[t] = {"promoted": self.promoted(t), "rule": cfg.get("rule"), "hard": bool(cfg.get("hard")),
                      "alpha": self.alpha(t) if cfg.get("rule") in ("presence_jury", "heavy_vehicle_jury") else None,
                      "m": self.m(t) if cfg.get("rule") in ("presence_jury", "heavy_vehicle_jury") else None,
                      **{k: frozen[k] for k in ("catch", "false_accusation", "n") if k in frozen}}
        return out

    # ---- routing ----
    def route(self, atom: Atom, k: int = 6) -> Route:
        t = atom.type.value if isinstance(atom.type, AtomType) else str(atom.type)
        cfg = self.types.get(t)
        if cfg is None:
            return Route([], "unverifiable", False, "This kind of statement is not in the routing table.",
                         "unrouted", promoted=False)
        rule = cfg.get("rule", "unverifiable")
        reason, code = cfg.get("reason", ""), cfg.get("reason_code", t)
        if t == "attribute" and (atom.value or "").lower() in cfg.get("never", []):
            return Route([], "unverifiable", False, cfg.get("never_reason", reason), "never", False, cfg=cfg)
        promoted = self.promoted(t)
        hard = bool(cfg.get("hard")) and promoted and rule != "unverifiable"
        r = Route(list(cfg.get("tiers", [])), rule, hard, reason, code, promoted, cfg=cfg)
        if rule in ("presence_jury", "heavy_vehicle_jury"):
            r.alpha, r.m = self.alpha(t), self.m(t, k)
        if r.demoted:
            r.reason_if_unverifiable, r.reason_code = DEMOTED_REASON, "demoted_by_bench"
        return r

    def value_cfg(self, atom: Atom) -> dict:
        """The yaml block for the atom's normalized value (scene-wide types), or {}."""
        return self.types.get(atom.type.value, {}).get("values", {}).get(atom.value or "", {})
