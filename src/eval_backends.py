"""Weave Evaluation: Cosmos-Reason2 NIM vs Gemini on the hand-labeled candidate clips.

Usage:  WANDB_API_KEY=... GEMINI_API_KEY=... COSMOS_NIM_URL=http://host:8001/v1 \
        python src/eval_backends.py --labels clips/labels.jsonl [--project team/unwatched] [--only gemini]

labels.jsonl, one row per clip (paths relative to the labels file):
  {"clip": "cam-05/seg-0412.mp4", "camera_ctx": {"camera_id": "cam-05-live", "camera_context": "stool w/ boxed DGX Spark",
   "baseline_summary": "...", "dist": 0.41, "p99": 0.22, "class_deltas": {"person": 1}},
   "expected_escalate": true, "expected_event": "equipment_removed", "expected_box_2d": [380, 410, 620, 590]}
Both runs land in one Weave project, so the Evaluations tab shows them side by side (accuracy, precision, recall,
JSON validity, latency, bbox IoU). Pick the rows and click Compare.
"""
from __future__ import annotations
import argparse, asyncio, json, os, pathlib, sys
from typing import Optional

import weave

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from verifier_backends import BackendError, CosmosNIMBackend, GeminiBackend  # noqa: E402

_BACKENDS = {"cosmos": CosmosNIMBackend, "gemini": GeminiBackend}
_LIVE: dict = {}  # backend instances live outside the weave.Model (clients aren't serializable)


class VerifierModel(weave.Model):
    backend: str
    model_id: str
    labels_dir: str

    @weave.op()
    def predict(self, clip: str, camera_ctx: dict) -> dict:
        data = (pathlib.Path(self.labels_dir) / clip).read_bytes()
        try:
            v = _LIVE[self.backend].verify(data, camera_ctx)
            return {**v.model_dump(), "ok": True}
        except BackendError as e:  # count failures against the backend, don't crash the eval
            return {"ok": False, "error": str(e), "escalate": None, "latency_ms": None, "box_2d": None}


def _iou(a: Optional[list], b: Optional[list]) -> Optional[float]:
    if not a or not b:
        return None
    y1, x1, y2, x2 = max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, y2 - y1) * max(0, x2 - x1)
    area = lambda r: max(0, r[2] - r[0]) * max(0, r[3] - r[1])  # noqa: E731
    union = area(a) + area(b) - inter
    return inter / union if union else 0.0


@weave.op()
def verdict_scorer(expected_escalate: bool, output: dict) -> dict:
    pred = output.get("escalate")
    return {
        "valid_json": bool(output.get("ok")),
        "correct": pred == expected_escalate,
        "tp": bool(pred) and expected_escalate,           # precision = tp / (tp + fp)
        "fp": bool(pred) and not expected_escalate,       # a false page: the thing we promise not to do
        "fn": (pred is False) and expected_escalate,      # a missed real event
    }


@weave.op()
def latency_scorer(output: dict) -> dict:
    return {"latency_ms": output.get("latency_ms") or 0, "under_10s": (output.get("latency_ms") or 1e9) < 10_000}


@weave.op()
def bbox_scorer(output: dict, expected_box_2d: Optional[list] = None) -> dict:
    if not expected_box_2d:  # only clips with a hand-drawn box count toward IoU
        return {"has_box": output.get("box_2d") is not None}
    iou = _iou(output.get("box_2d"), expected_box_2d) or 0.0
    return {"has_box": output.get("box_2d") is not None, "iou": iou, "iou_ge_0_3": iou >= 0.3}


def load_rows(path: pathlib.Path) -> list[dict]:
    rows = []
    for line in path.read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            r.setdefault("expected_box_2d", None)
            r.setdefault("camera_ctx", {})
            rows.append(r)
    return rows


def summarize(name: str, res: dict) -> str:
    v = res.get("verdict_scorer", {})
    get = lambda k: (v.get(k) or {}).get("true_count", 0)  # noqa: E731
    tp, fp, fn = get("tp"), get("fp"), get("fn")
    prec = tp / (tp + fp) if tp + fp else float("nan")
    rec = tp / (tp + fn) if tp + fn else float("nan")
    acc = (v.get("correct") or {}).get("true_fraction", float("nan"))
    lat = (res.get("latency_scorer", {}).get("latency_ms") or {}).get("mean", float("nan"))
    return f"{name:<8} acc={acc:.2f} precision={prec:.2f} recall={rec:.2f} false_pages={fp} mean_latency_ms={lat:.0f}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", default="clips/labels.jsonl")
    ap.add_argument("--project", default=os.getenv("WEAVE_PROJECT", "unwatched"))
    ap.add_argument("--only", choices=list(_BACKENDS), action="append")
    ap.add_argument("--trials", type=int, default=1)
    a = ap.parse_args()

    labels = pathlib.Path(a.labels).resolve()
    rows = load_rows(labels)
    weave.init(a.project)  # WANDB_API_KEY from env; autopatches openai + google-genai clients
    dataset = weave.Dataset(name="nw-candidates", rows=rows)
    ev = weave.Evaluation(name="nw-verifier-backends", dataset=dataset, trials=a.trials,
                          scorers=[verdict_scorer, latency_scorer, bbox_scorer])

    lines = []
    for name in a.only or list(_BACKENDS):
        try:
            _LIVE[name] = _BACKENDS[name]()
        except KeyError as e:
            print(f"skip {name}: missing env {e}"); continue
        m = VerifierModel(backend=name, model_id=_LIVE[name].model, labels_dir=str(labels.parent))
        res = asyncio.run(ev.evaluate(m, __weave={"display_name": f"{name}:{m.model_id}"}))
        lines.append(summarize(name, res))
    print(f"\n{len(rows)} labeled clips")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
