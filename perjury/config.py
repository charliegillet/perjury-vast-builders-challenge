"""Settings. Reads env, plus (optionally) exactly one team config file named by PERJURY_TEAM_CONFIG.

Never print values from here: they include GPU_BEARER_TOKEN, VSS password, S3 keys and WANDB_API_KEY.
PERJURY_MODE: "live" (event VM / pod) or "fixture" (offline; fake clients over cache/fixture_*.json, UI shows a FIXTURE banner).
"""
from __future__ import annotations

import os
import shlex
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(os.getenv("PERJURY_CACHE_DIR", ROOT / "cache"))


def _load_team_config(path: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if line.startswith("export "):
            line = line[7:]
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        toks = shlex.split(v, comments=True)
        out[k.strip()] = toks[0] if len(toks) == 1 else v.strip()
    return out


class Settings:
    def __init__(self, env: dict[str, str] | None = None):
        e = dict(os.environ) if env is None else dict(env)
        if e.get("PERJURY_TEAM_CONFIG"):
            for k, v in _load_team_config(e["PERJURY_TEAM_CONFIG"]).items():
                e.setdefault(k, v)
        self.env = e
        self.mode = e.get("PERJURY_MODE", "fixture" if not e.get("INGRESS_URL") and not e.get("VSS_URL") else "live")
        # VSS (deploy-app-no-registry injects VSS_URL / VSS_USERNAME / VSS_PASSWORD)
        self.vss_url = (e.get("INGRESS_URL") or e.get("VSS_URL") or "").rstrip("/")
        self.vss_user = e.get("USERNAME") or e.get("VSS_USERNAME") or ""
        self.vss_password = e.get("PASSWORD") or e.get("VSS_PASSWORD") or ""
        # GPU host (shared CoreWeave endpoints). config.example: "No auth token is needed"; the bearer is sent only if set
        self.gpu_token = e.get("GPU_BEARER_TOKEN", "")
        self.cosmos_url = e.get("COSMOS3_REASON_URL", "").rstrip("/")
        self.cosmos_model = e.get("COSMOS3_REASON_MODEL", "nvidia/cosmos3-reason")
        self.cosmos_bbox_scale = float(e.get("COSMOS_BBOX_SCALE", "1000"))
        self.yolo_url = e.get("YOLO_URL", "").rstrip("/")
        self.embed_url = e.get("COSMOS_EMBED1_URL", "").rstrip("/")
        self.embed_model = e.get("COSMOS_EMBED1_MODEL", "nvidia/cosmos-embed1")
        self.canary_url = e.get("CANARY_1B_URL", "").rstrip("/")
        self.canary_model = e.get("CANARY_1B_MODEL", "")  # config.example leaves it unset on purpose
        # W&B
        self.wandb_key = e.get("WANDB_API_KEY", "")
        self.wandb_project = (f"{e['WANDB_TEAM']}/{e.get('WANDB_PROJECT', 'perjury')}"
                              if e.get("WANDB_TEAM") else e.get("WANDB_PROJECT", "perjury"))
        self.wandb_base = e.get("WANDB_BASE_URL", "https://api.inference.wandb.ai/v1").rstrip("/")
        self.atomizer_model = e.get("PERJURY_ATOMIZER_MODEL", "nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B")
        # S3 / VastDB
        self.s3_endpoint = e.get("S3_ENDPOINT", "")
        self.s3_access = e.get("ACCESS_KEY", "")
        self.s3_secret = e.get("SECRET_KEY", "")
        self.s3_segments_bucket = e.get("S3_SEGMENTS_BUCKET", "")
        self.vdb_endpoint = e.get("VDB_ENDPOINT") or self.s3_endpoint
        self.vdb_bucket = e.get("VASTDB_BUCKET", "vss-db")
        self.vdb_schema = e.get("VDB_SCHEMA", "vss-schema")
        self.vdb_collection = e.get("VDB_COLLECTION", "vss-collection")
        self.camera_id = e.get("PERJURY_CAMERA_ID", "i24_cam-1")
        # Runtime knobs (§7 timeouts, §8 GPU budget)
        self.juror_timeout_s = float(e.get("PERJURY_JUROR_TIMEOUT_S", "8"))
        self.atom_timeout_s = float(e.get("PERJURY_ATOM_TIMEOUT_S", "20"))
        self.jury_size = int(e.get("PERJURY_JURY_SIZE", "6"))
        self.cosmos_concurrency = int(e.get("PERJURY_COSMOS_CONCURRENCY", "6"))
        self.fixture_latency = float(e.get("PERJURY_FIXTURE_LATENCY", "1.0"))  # 0 = instant fakes (tests)
        self.pod_name = e.get("HOSTNAME", "") if e.get("KUBERNETES_SERVICE_HOST") else ""
        self.weave_enabled = bool(self.wandb_key) and e.get("PERJURY_WEAVE", "1") != "0"

    @property
    def index_path(self) -> Path:
        name = "fixture_i24_index.json" if self.mode == "fixture" else "i24_index.json"
        return CACHE / name

    @property
    def probes_path(self) -> Path:
        name = "fixture_scene_probes.json" if self.mode == "fixture" else "scene_probes.json"
        return CACHE / name


@lru_cache(maxsize=1)
def settings() -> Settings:
    return Settings()
