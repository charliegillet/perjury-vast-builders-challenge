"""Shared data shapes for PERJURY (FINAL-IDEA-v3 §4, §7). Every module imports from here; nothing here does I/O."""
from __future__ import annotations

from enum import Enum
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field


class AtomType(str, Enum):
    scene_identity = "scene_identity"
    road_surface = "road_surface"
    weather = "weather"
    traffic_state = "traffic_state"
    lighting = "lighting"
    coco_presence = "coco_presence"
    count = "count"
    towing = "towing"
    heavy_vehicle_kind = "heavy_vehicle_kind"
    action = "action"
    attribute = "attribute"
    identity_intent = "identity_intent"
    cross_camera = "cross_camera"
    lane_position = "lane_position"
    other = "other"


COCO_CLASSES = ("person", "bicycle", "motorcycle", "car", "bus", "truck")
TowingVehicle = Literal["pickup", "suv", "van", "car", "any"]


class Atom(BaseModel):
    """One atomic claim. `span` is an exact substring of the transcript (validated by code, §6)."""
    id: str
    span: str
    type: AtomType
    cls: Optional[str] = Field(None, description="coco_presence / count: one of COCO_CLASSES")
    value: Optional[str] = Field(None, description="road_surface/weather/traffic_state/lighting/action/... normalized value")
    count: Optional[int] = None
    count_op: Optional[Literal["exact", "at_least", "at_most"]] = None
    towing_vehicle: Optional[TowingVehicle] = None
    depends_on: Optional[str] = None
    negated: bool = False  # "there are no pedestrians" -> coco_presence person, negated=True


AtomVerdictLabel = Literal["SUPPORTED", "CONTRADICTED", "UNVERIFIABLE", "MOOT"]
ClaimVerdictLabel = Literal["TRUE", "FALSE", "UNPROVEN"]
VoteLabel = Literal["yes", "no", "abstain"]
Tier = Literal["RECORDS", "CAPTIONS", "JURY"]


class Juror(BaseModel):
    """One summoned juror = one camera looking at one moment (or a pre-run scene-wide grid)."""
    camera: str                      # e.g. "p1c3"
    source: Optional[str] = None     # segment s3 URI the panels came from
    seg: Optional[int] = None
    times: list[float] = []          # panel timestamps (s, relative to segment start)
    rank: Optional[int] = None       # retrieval rank within the scene (0 = most claim-like)
    retrieval_score: Optional[float] = None


class Vote(BaseModel):
    camera: str
    vote: VoteLabel
    tier: Tier = "JURY"
    probe: str = ""                   # "P-TOW", "P-COND", "P-COUNT", "P-LEAD"
    probe_version: str = ""
    raw: Optional[dict[str, Any]] = None   # parsed juror JSON (shown in the exhibit drawer)
    yes_panels: list[int] = []        # 1-based panel numbers the juror said yes on
    visibility: Optional[str] = None
    zoom_ok: Optional[bool] = None    # None = no zoom-check ran
    grounded: Optional[list[int]] = None  # bbox_2d 0-1000 xyxy from P-GROUND
    abstain_reason: Optional[str] = None  # cannot_tell | poor_visibility | invalid_json | timeout | error
    latency_ms: int = 0
    cached: bool = False
    cached_at: Optional[str] = None
    image_sha: Optional[str] = None
    juror: Optional[Juror] = None


class AtomVerdict(BaseModel):
    atom_id: str
    verdict: AtomVerdictLabel
    reason: str                       # template text (never LLM-written)
    reason_code: str = ""             # e.g. "temporal", "not_observable", "demoted_by_bench", "jury_timeout"
    tiers: list[Tier] = []            # tiers that decided it
    votes: list[Vote] = []
    stats: dict[str, Any] = {}        # e.g. {"Y":3,"N":2,"k":6,"k_valid":5,"m":4,"alpha":0.27,"t1":{"supports":0,...}}


class ClaimVerdict(BaseModel):
    run_id: str
    text: str
    scene: int
    verdict: ClaimVerdictLabel
    explanation: str
    atoms: list[Atom]
    atom_verdicts: list[AtomVerdict]
    parser: Literal["llm", "rules"] = "llm"
    elapsed_ms: int = 0
    gpu_s: float = 0.0
    services_fired: list[str] = []
    calls: int = 0
    mode: Literal["live", "fixture", "replay"] = "live"


# ---- index (cache/i24_index.json, cache/fixture_i24_index.json) ----
class Segment(BaseModel):
    source: str
    original_video: str
    scene: int
    camera: str
    seg: int
    start: float
    end: float
    object_classes: list[str] = []
    object_counts: dict[str, int] = {}   # peak concurrent per class (pipeline YOLO)
    persist: dict[str, int] = {}         # max consecutive sidecar frames per class (noise-floor rule, §7)
    caption: str = ""
    processing_time: Optional[float] = None
    video_shape: Optional[list[int]] = None  # [h, w] or [h, w, c]
    location: Optional[str] = None
    camera_id: str = "i24_cam-1"
