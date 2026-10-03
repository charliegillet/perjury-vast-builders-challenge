"""Build the K8s manifests for PERJURY at /app (deploy-app-no-registry, adapted for a multi-directory app).

`kubectl create configmap --from-file=<dir>` does not recurse and a ConfigMap holds ~1 MiB, so files are
bin-packed into several ConfigMaps (`<app>-code-N`, `<app>-cache-N`) with flat keys (`perjury__pipeline.py`).
One projected volume maps every key back to its repo path under /seed; the container copies /seed into a
writable /code (emptyDir) so cache/ can take runs, tiles and the Cosmos disk cache.

Writes <out>/configmaps.yaml and <out>/app.yaml, prints a size table, exits 1 if a ConfigMap is over the limit.
Never reads secrets; the Secret is created by deploy.sh.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIMIT = 1_000_000          # bytes per ConfigMap (API cap is 1 MiB incl. metadata; base64 counted for binary)
CODE_GLOBS = ["perjury/*.py", "perjury/*.yaml", "app/*.py", "app/static/*", "requirements.txt"]
CACHE_GLOBS = ["cache/*.json", "cache/*.npy", "cache/replays/*.jsonl"]
FIXTURE_ONLY = "fixture_"  # cache/fixture_*.json ship only with --mode fixture (fakes need them, live never does)
SKIP_NAMES = {"feedback.jsonl"}


def collect(mode: str) -> tuple[list[tuple[str, Path]], list[tuple[str, Path]], list[str]]:
    code = [(str(p.relative_to(ROOT)), p) for g in CODE_GLOBS for p in sorted(ROOT.glob(g)) if p.is_file()]
    code.append(("main.py", ROOT / "deploy" / "pod_main.py"))
    cache, notes = [], []
    for g in CACHE_GLOBS:
        for p in sorted(ROOT.glob(g)):
            rel = str(p.relative_to(ROOT))
            if not p.is_file() or p.name in SKIP_NAMES:
                continue
            if p.name.startswith(FIXTURE_ONLY) and mode != "fixture":
                continue
            cache.append((rel, p))
    if mode == "live":
        for need in ("cache/i24_index.json", "cache/scene_probes.json"):
            if not (ROOT / need).exists():
                notes.append(f"WARNING: {need} missing: the live pod will show 'index not built' / no pre-run walls")
    return code, cache, notes


def entry(rel: str, p: Path) -> dict:
    raw = p.read_bytes()
    if rel == "app/static/index.html":
        # Each deploy gets URLs derived from the actual asset bytes, so an open
        # browser cannot retain stale scripts after a code ConfigMap changes.
        text = raw.decode("utf-8")
        for name in ("app.js", "wav.js", "style.css", "trucks.js"):
            asset = ROOT / "app" / "static" / name
            version = hashlib.sha256(asset.read_bytes()).hexdigest()[:12]
            text = re.sub(r"static/" + re.escape(name) + r"(?:\?v=[^\"']*)?", f"static/{name}?v={version}", text)
        raw = text.encode("utf-8")
    key = rel.replace("/", "__")
    try:
        text = raw.decode("utf-8")
        return {"key": key, "path": rel, "text": text, "size": len(raw) + len(key)}
    except UnicodeDecodeError:
        b64 = base64.b64encode(raw).decode()
        return {"key": key, "path": rel, "b64": b64, "size": len(b64) + len(key)}


def pack(entries: list[dict], prefix: str) -> list[dict]:
    bins: list[dict] = []
    for e in sorted(entries, key=lambda x: -x["size"]):
        if e["size"] > LIMIT:
            raise SystemExit(f"ERROR: {e['path']} is {e['size']:,} bytes, over the {LIMIT:,}-byte ConfigMap limit")
        b = next((b for b in bins if b["size"] + e["size"] <= LIMIT), None)
        if b is None:
            b = {"name": f"{prefix}-{len(bins)}", "size": 0, "entries": []}
            bins.append(b)
        b["entries"].append(e)
        b["size"] += e["size"]
    return bins


def cm_doc(b: dict, app: str) -> dict:
    doc: dict = {"apiVersion": "v1", "kind": "ConfigMap",
                 "metadata": {"name": b["name"], "labels": {"app": app, "perjury/part": "files"}}}
    data = {e["key"]: e["text"] for e in b["entries"] if "text" in e}
    binary = {e["key"]: e["b64"] for e in b["entries"] if "b64" in e}
    if data:
        doc["data"] = data
    if binary:
        doc["binaryData"] = binary
    return doc


def app_docs(app: str, host: str, mode: str, bins: list[dict], digest: str, port: int) -> list[dict]:
    labels = {"app": app}
    sources = [{"configMap": {"name": b["name"], "items": [{"key": e["key"], "path": e["path"]} for e in b["entries"]]}}
               for b in bins]
    start = "\n".join([
        "set -euo pipefail",
        "for f in /seed/*; do cp -rL \"$f\" /code/; done",   # glob skips the projected volume's ..data dirs
        "mkdir -p /code/cache/runs",
        "apt-get update -qq && apt-get install -y -qq --no-install-recommends ffmpeg && rm -rf /var/lib/apt/lists/*",
        "pip install --no-cache-dir -q --disable-pip-version-check -r requirements.txt",
        "exec python main.py",
    ])
    deployment = {
        "apiVersion": "apps/v1", "kind": "Deployment", "metadata": {"name": app, "labels": labels},
        "spec": {
            "replicas": 1,
            "strategy": {"type": "Recreate"},
            "selector": {"matchLabels": labels},
            "template": {
                "metadata": {"labels": labels, "annotations": {"perjury/files-sha": digest}},
                "spec": {
                    "containers": [{
                        "name": "app", "image": "python:3.12-slim", "imagePullPolicy": "IfNotPresent",
                        "workingDir": "/code", "command": ["bash", "-c"], "args": [start],
                        "ports": [{"containerPort": port}],
                        "env": [{"name": "PORT", "value": str(port)},
                                {"name": "PERJURY_MODE", "value": mode},
                                {"name": "IMAGEIO_FFMPEG_EXE", "value": "/usr/bin/ffmpeg"},
                                {"name": "PYTHONUNBUFFERED", "value": "1"}],
                        "envFrom": [{"secretRef": {"name": f"{app}-secrets", "optional": mode == "fixture"}}],
                        "volumeMounts": [{"name": "seed", "mountPath": "/seed", "readOnly": True},
                                         {"name": "code", "mountPath": "/code"}],
                        "startupProbe": {"httpGet": {"path": "/health", "port": port},
                                         "periodSeconds": 5, "failureThreshold": 72},   # pip install: up to 6 min
                        "readinessProbe": {"httpGet": {"path": "/health", "port": port}, "periodSeconds": 10},
                        "livenessProbe": {"httpGet": {"path": "/health", "port": port}, "periodSeconds": 20,
                                          "failureThreshold": 6},
                        "resources": {"requests": {"cpu": "500m", "memory": "1Gi"}, "limits": {"memory": "3Gi"}},
                    }],
                    "volumes": [{"name": "seed", "projected": {"sources": sources}},
                                {"name": "code", "emptyDir": {}}],
                },
            },
        },
    }
    service = {"apiVersion": "v1", "kind": "Service", "metadata": {"name": app, "labels": labels},
               "spec": {"selector": labels, "type": "ClusterIP",
                        "ports": [{"name": "http", "port": 80, "targetPort": port}]}}
    ingress = {
        "apiVersion": "networking.k8s.io/v1", "kind": "Ingress",
        "metadata": {"name": app, "labels": labels, "annotations": {
            "nginx.ingress.kubernetes.io/rewrite-target": "/$2",
            "nginx.ingress.kubernetes.io/proxy-buffering": "off",       # SSE verdict stream
            "nginx.ingress.kubernetes.io/proxy-read-timeout": "120",
            "nginx.ingress.kubernetes.io/proxy-body-size": "16m",       # recorded testimony upload
        }},
        "spec": {"ingressClassName": "nginx", "rules": [{"host": host, "http": {"paths": [{
            "path": "/app(/|$)(.*)", "pathType": "ImplementationSpecific",
            "backend": {"service": {"name": app, "port": {"number": 80}}}}]}}]},
    }
    return [deployment, service, ingress]


def dump(docs: list[dict]) -> str:
    # JSON is valid YAML; one document per `---`
    return "\n---\n".join(json.dumps(d, indent=1) for d in docs) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", default="perjury")
    ap.add_argument("--host", required=True, help="team host from INGRESS_URL, e.g. video-lab-team-17.cosmos.vastdata.com")
    ap.add_argument("--mode", choices=("live", "fixture"), default="live")
    ap.add_argument("--port", type=int, default=8080)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    code, cache, notes = collect(a.mode)
    bins = pack([entry(r, p) for r, p in code], f"{a.app}-code") + pack([entry(r, p) for r, p in cache], f"{a.app}-cache")
    digest = hashlib.sha256(json.dumps([[e["key"], e.get("text") or e.get("b64")] for b in bins
                                        for e in b["entries"]], sort_keys=True).encode()).hexdigest()[:16]
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "configmaps.yaml").write_text(dump([cm_doc(b, a.app) for b in bins]))
    (out / "app.yaml").write_text(dump(app_docs(a.app, a.host, a.mode, bins, digest, a.port)))
    (out / "configmaps.txt").write_text("\n".join(b["name"] for b in bins) + "\n")
    print(f"{'ConfigMap':<22}{'files':>6}{'bytes':>12}  (limit {LIMIT:,})")
    for b in bins:
        print(f"{b['name']:<22}{len(b['entries']):>6}{b['size']:>12,}")
    print(f"{'total':<22}{sum(len(b['entries']) for b in bins):>6}{sum(b['size'] for b in bins):>12,}  files-sha {digest}")
    for n in notes:
        print(n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
