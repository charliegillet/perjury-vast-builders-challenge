#!/usr/bin/env bash
# Deploy PERJURY to the team namespace at http://<team host>/app (deploy-app-no-registry, adapted).
#   deploy/deploy.sh             live mode (real endpoints; needs cache/i24_index.json + scene_probes.json)
#   deploy/deploy.sh fixture     offline fakes (the 10:00 "prove the deploy path" skeleton)
#   deploy/deploy.sh --dry-run   build manifests + size table only, apply nothing
# Run on the event VM from the repo root or anywhere. Never prints secret values; never use `set -x` here.
set -euo pipefail

MODE=live
DRY=0
for arg in "$@"; do
  case "$arg" in
    live|fixture) MODE="$arg" ;;
    --dry-run) DRY=1 ;;
    *) echo "usage: $0 [live|fixture] [--dry-run]" >&2; exit 2 ;;
  esac
done

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
APP_NAME="${APP_NAME:-perjury}"
# kubeconfig: canonical /config/kubeconfig first, then the team-prefixed alias /config/<team>-k8s.yaml
if [[ -z "${KUBECONFIG:-}" ]]; then
  if [[ -e /config/kubeconfig ]]; then
    KUBECONFIG=/config/kubeconfig
  else
    KUBECONFIG="$(find /config -maxdepth 1 \( -type f -o -type l \) -name '*-k8s.yaml' 2>/dev/null | sort | head -n 1 || true)"
  fi
fi
export KUBECONFIG
PY="$(command -v python3 || command -v python)"

# --- this team's config only (exactly one /config/*.config, possibly team-prefixed; files or symlinks).
# Values stay in this process's env; WANDB_* etc. already exported in your shell are kept as a fallback.
TEAM_CONFIGS=()
while IFS= read -r f; do TEAM_CONFIGS+=("$f"); done < <(find /config -maxdepth 1 \( -type f -o -type l \) -name '*.config' 2>/dev/null | sort)
if (( ${#TEAM_CONFIGS[@]} == 1 )); then
  set -a
  # shellcheck disable=SC1090
  source "${TEAM_CONFIGS[0]}"
  set +a
elif (( DRY == 0 )); then
  echo "expected exactly one /config/*.config, found ${#TEAM_CONFIGS[@]}" >&2
  exit 1
fi

NS="${NS:-${USERNAME:-}}"
APP_HOST="${INGRESS_URL:-http://video-lab-team-N.cosmos.vastdata.com}"
APP_HOST="${APP_HOST#http://}"; APP_HOST="${APP_HOST#https://}"; APP_HOST="${APP_HOST%%/*}"
if (( DRY == 0 )) && [[ -z "$NS" || -z "${INGRESS_URL:-}" ]]; then
  echo "USERNAME (namespace) or INGRESS_URL missing from the team config" >&2
  exit 1
fi

OUT="$(mktemp -d)"
chmod 700 "$OUT"
trap 'rm -rf "$OUT"' EXIT

echo "== PERJURY deploy · mode=$MODE · ns=${NS:-?} · host=$APP_HOST"
echo "== 1/5 manifests (ConfigMaps bin-packed under the 1 MiB limit)"
"$PY" "$REPO/deploy/build_manifests.py" --app "$APP_NAME" --host "$APP_HOST" --mode "$MODE" --out "$OUT"

if (( DRY == 1 )); then
  mkdir -p "$REPO/deploy/out"
  cp "$OUT/configmaps.yaml" "$OUT/app.yaml" "$REPO/deploy/out/"
  echo "dry run: manifests copied to deploy/out/ (no Secret built, nothing applied)"
  exit 0
fi

command -v kubectl >/dev/null || { echo "kubectl not found" >&2; exit 1; }
[[ -n "$KUBECONFIG" && -e "$KUBECONFIG" ]] || { echo "no kubeconfig: tried /config/kubeconfig and /config/*-k8s.yaml" >&2; exit 1; }
kubectl -n "$NS" get deployments >/dev/null

echo "== 2/5 Secret ${APP_NAME}-secrets (keys only listed, values never printed)"
# The env file is written 0600 inside the 0700 temp dir and deleted on exit.
"$PY" - "$OUT/secret.env" <<'PYEOF'
import os, sys
e = os.environ
alias = {"VSS_URL": e.get("INGRESS_URL") or e.get("VSS_URL"),
         "VSS_USERNAME": e.get("USERNAME") or e.get("VSS_USERNAME"),
         "VSS_PASSWORD": e.get("PASSWORD") or e.get("VSS_PASSWORD")}
# GPU endpoints need no token per config.example; GPU_BEARER_TOKEN ships only if it happens to be set.
keys = ["GPU_BEARER_TOKEN", "COSMOS3_REASON_URL", "COSMOS3_REASON_MODEL", "COSMOS_BBOX_SCALE",
        "COSMOS_EMBED1_URL", "COSMOS_EMBED1_MODEL", "YOLO_URL", "CANARY_1B_URL", "CANARY_1B_MODEL",
        "WANDB_API_KEY", "WANDB_TEAM", "WANDB_PROJECT", "WANDB_BASE_URL",
        "S3_ENDPOINT", "S3_REGION", "ACCESS_KEY", "SECRET_KEY", "S3_SEGMENTS_BUCKET",
        "VDB_ENDPOINT", "VASTDB_BUCKET", "VDB_SCHEMA", "VDB_COLLECTION"]
skip = {"PERJURY_MODE", "PERJURY_TEAM_CONFIG", "PERJURY_CACHE_DIR", "PERJURY_RUNS_DIR", "PERJURY_DEV_STUB"}
vals = {**{k: v for k, v in alias.items() if v}, **{k: e[k] for k in keys if e.get(k)},
        **{k: v for k, v in e.items() if k.startswith("PERJURY_") and k not in skip and v}}
fd = os.open(sys.argv[1], os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
with os.fdopen(fd, "w") as f:
    for k, v in vals.items():
        if "\n" not in v:
            f.write(f"{k}={v}\n")
missing = [k for k in ("VSS_URL", "VSS_PASSWORD", "COSMOS3_REASON_URL", "WANDB_API_KEY") if k not in vals]
print("   keys:", ", ".join(sorted(vals)))
if missing:
    print("   WARNING: not in team config:", ", ".join(missing))
PYEOF
kubectl -n "$NS" create secret generic "${APP_NAME}-secrets" --from-env-file="$OUT/secret.env" \
  --dry-run=client -o yaml | kubectl -n "$NS" apply -f - >/dev/null
echo "   secret/${APP_NAME}-secrets applied"

echo "== 3/5 ConfigMaps (server-side apply: a client-side apply annotation would cap them at 256 KiB)"
kubectl -n "$NS" apply --server-side --force-conflicts --field-manager=perjury-deploy -f "$OUT/configmaps.yaml"
# drop ConfigMaps from an earlier, larger deploy
keep="$(tr '\n' ' ' < "$OUT/configmaps.txt")"
for cm in $(kubectl -n "$NS" get configmap -l "app=${APP_NAME},perjury/part=files" -o name); do
  [[ " $keep " == *" ${cm#configmap/} "* ]] || kubectl -n "$NS" delete "$cm"
done

echo "== 4/5 Deployment + Service + Ingress (path /app on $APP_HOST)"
kubectl -n "$NS" apply -f "$OUT/app.yaml"

echo "== 5/5 rollout (pip install at start takes 1-3 min)"
kubectl -n "$NS" rollout status "deploy/${APP_NAME}" --timeout=420s
kubectl -n "$NS" get pods,svc,ingress -l "app=${APP_NAME}"
code="$(curl -sS -o /dev/null -w '%{http_code}' "http://${APP_HOST}/app/" || true)"
echo "   GET http://${APP_HOST}/app/ -> $code"
curl -sS "http://${APP_HOST}/app/health" || true
echo
echo "App: http://${APP_HOST}/app"
