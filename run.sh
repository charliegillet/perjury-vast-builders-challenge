#!/usr/bin/env bash
# Run PERJURY from the repo root, writing a thorough debug log of every run to logs/.
#   ./run.sh              live on the event VM (a /config/*.config or INGRESS_URL exists), else the offline demo
#   ./run.sh fixture      offline demo on fake Pack A data (FIXTURE banner) → http://localhost:8080/
#   ./run.sh live         real endpoints (event VM: needs INGRESS_URL etc. in the env or /config/<team>.config)
#   ./run.sh test         run the test suite
#   PORT=9000 ./run.sh    another port
#   LOG_LEVEL=INFO ./run.sh   quieter app log (default DEBUG: every request and pipeline event, redacted)
#
# Log: logs/run-<timestamp>-<mode>.log, with logs/latest.log pointing at the newest one.
# It records the environment diagnosis (versions, git state, which config keys are SET, cache files, port),
# every setup step with timings, and the app's full output. Secret VALUES are never written: only key names.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

DEFAULT_MODE=fixture
if [[ -n "${INGRESS_URL:-}${VSS_URL:-}${PERJURY_TEAM_CONFIG:-}" ]] || compgen -G "/config/*.config" >/dev/null; then
  DEFAULT_MODE=live
fi
MODE="${1:-$DEFAULT_MODE}"
PORT="${PORT:-8080}"
LOG_LEVEL="${LOG_LEVEL:-DEBUG}"
VENV="${PERJURY_VENV:-.venv}"
# live mode on the VM: endpoints and model overrides (gitignored; see live-env.example.sh)
if [[ "$MODE" == live && -f live-env.sh ]]; then
  # shellcheck disable=SC1091
  source ./live-env.sh
fi
PY="$VENV/bin/python"
START_EPOCH="$(date +%s)"

mkdir -p logs
LOG="logs/run-$(date +%Y%m%d-%H%M%S)-$MODE.log"
ln -sf "$(basename "$LOG")" logs/latest.log
# Everything from here on goes to the terminal and the log.
exec > >(tee -a "$LOG") 2>&1

ts() { date +%H:%M:%S; }
say() { echo "[$(ts)] $*"; }
section() { echo; echo "[$(ts)] ===== $* ====="; }
on_err() { say "ERROR: '${BASH_COMMAND}' failed with exit $? at run.sh line $1"; say "full log: $LOG"; }
on_exit() { local rc=$?; say "run.sh exiting: code=$rc after $(( $(date +%s) - START_EPOCH ))s · log: $LOG"; }
trap 'on_err $LINENO' ERR
trap on_exit EXIT

section "PERJURY run.sh · mode=$MODE · port=$PORT · log_level=$LOG_LEVEL"
say "log file: $LOG"
say "started: $(date '+%Y-%m-%d %H:%M:%S %Z')"
say "cwd: $(pwd)"

section "system"
say "os: $(uname -srm)"
say "shell: $BASH_VERSION"
say "user: $(id -un)"
say "disk free here: $(df -h . | awk 'NR==2{print $4" of "$2}')"
say "python3 on PATH: $(command -v python3 || echo none) $(python3 --version 2>&1 || true)"
say "uv: $(command -v uv >/dev/null && uv --version 2>&1 || echo 'not installed')"
say "system ffmpeg: $(command -v ffmpeg || echo 'none (imageio-ffmpeg bundles one)')"
say "kubectl: $(command -v kubectl || echo none)"

section "git"
if git rev-parse --git-dir >/dev/null 2>&1; then
  say "branch: $(git branch --show-current) @ $(git rev-parse --short HEAD) ($(git log -1 --format='%cd · %s' --date=format:'%Y-%m-%d %H:%M'))"
  dirty="$(git status --porcelain --untracked-files=no | wc -l | tr -d ' ')"
  say "uncommitted tracked changes: $dirty file(s)"
  [[ "$dirty" == 0 ]] || git status --short --untracked-files=no | sed 's/^/    /'
else
  say "not a git checkout"
fi

section "python environment"
if [[ ! -x "$PY" ]]; then
  say "creating $VENV"
  if command -v uv >/dev/null; then
    uv venv -p 3.12 "$VENV"
  elif command -v python3.12 >/dev/null; then
    python3.12 -m venv "$VENV"
  else
    python3 -c 'import sys; assert sys.version_info >= (3, 12), "Python 3.12 or newer is required"'
    python3 -m venv "$VENV"
  fi
fi
"$PY" -c 'import sys; assert sys.version_info >= (3, 12), "This virtual environment needs Python 3.12 or newer; set PERJURY_VENV to a compatible environment"'
say "venv python: $("$PY" --version 2>&1) at $PY"
STAMP="$VENV/.requirements.sha"
SHA="$(shasum requirements.txt | cut -d' ' -f1)"
if [[ ! -f "$STAMP" || "$(cat "$STAMP")" != "$SHA" ]]; then
  say "installing requirements (requirements.txt changed or first run)"
  t0=$(date +%s)
  if command -v uv >/dev/null; then
    uv pip install --python "$PY" -r requirements.txt pytest pytest-asyncio
  else
    "$PY" -m pip install -r requirements.txt pytest pytest-asyncio
  fi
  echo "$SHA" > "$STAMP"
  say "install took $(( $(date +%s) - t0 ))s"
else
  say "requirements up to date (sha ${SHA:0:12})"
fi
"$PY" - <<'PYEOF'
import importlib, sys
mods = ["fastapi", "uvicorn", "httpx", "pydantic", "yaml", "PIL", "numpy", "openai", "weave", "imageio_ffmpeg", "pytest"]
for m in mods:
    try:
        mod = importlib.import_module(m)
        print(f"    {m:<15} {getattr(mod, '__version__', getattr(mod, 'VERSION', '?'))}")
    except Exception as e:
        print(f"    {m:<15} MISSING ({type(e).__name__}: {e})")
try:
    import imageio_ffmpeg
    print(f"    ffmpeg binary   {imageio_ffmpeg.get_ffmpeg_exe()}")
except Exception as e:
    print(f"    ffmpeg binary   UNAVAILABLE ({e})")
for m in ("vastdb", "pyarrow"):
    try:
        importlib.import_module(m); print(f"    {m:<15} installed (VM jobs)")
    except Exception:
        print(f"    {m:<15} not installed (only needed for index_i24 on the VM: pip install -r requirements-vm.txt)")
PYEOF

if [[ "$MODE" == test ]]; then
  section "tests"
  "$PY" -m pytest -q -rs
  exit $?
fi

section "configuration (key names only, never values)"
case "$MODE" in
  fixture)
    export PERJURY_MODE=fixture
    [[ -f cache/fixture_i24_index.json ]] || { say "fixtures missing: generating"; "$PY" tools/make_fixtures.py; }
    ;;
  live)
    export PERJURY_MODE=live
    # On the VM, pick up this team's config if the env doesn't already have it (values are never printed).
    if [[ -z "${INGRESS_URL:-}" && -z "${VSS_URL:-}" && -z "${PERJURY_TEAM_CONFIG:-}" ]]; then
      cfg="$(find /config -maxdepth 1 \( -type f -o -type l \) -name '*.config' 2>/dev/null | sort | head -n 1 || true)"
      if [[ -n "$cfg" ]]; then export PERJURY_TEAM_CONFIG="$cfg"; say "team config: $cfg"
      else say "WARNING: INGRESS_URL unset and no /config/*.config found: live calls will fail"; fi
    fi
    ;;
  *)
    say "usage: $0 [fixture|live|test]"; exit 2 ;;
esac
export PERJURY_LOG_LEVEL="$LOG_LEVEL"
"$PY" - <<'PYEOF'
from perjury.config import Settings
s = Settings()
keys = ["INGRESS_URL", "VSS_URL", "USERNAME", "PASSWORD", "GPU_BEARER_TOKEN", "COSMOS3_REASON_URL", "COSMOS3_REASON_MODEL",
        "YOLO_URL", "COSMOS_EMBED1_URL", "COSMOS_EMBED1_MODEL", "CANARY_1B_URL", "CANARY_1B_MODEL", "WANDB_API_KEY",
        "WANDB_TEAM", "WANDB_PROJECT", "S3_ENDPOINT", "ACCESS_KEY", "SECRET_KEY", "S3_SEGMENTS_BUCKET", "VDB_ENDPOINT",
        "VASTDB_BUCKET", "KUBERNETES_SERVICE_HOST"]
print(f"    resolved mode   {s.mode}")
print("    set:     " + (", ".join(k for k in keys if s.env.get(k)) or "(none)"))
print("    not set: " + (", ".join(k for k in keys if not s.env.get(k)) or "(none)"))
tuning = sorted(k for k in s.env if k.startswith("PERJURY_"))
print("    PERJURY_*: " + ", ".join(f"{k}={s.env[k]}" for k in tuning if k != "PERJURY_TEAM_CONFIG"))
print(f"    weave tracing   {'on' if s.weave_enabled else 'off (no WANDB_API_KEY)'}")
print(f"    index file      {s.index_path}  {'OK' if s.index_path.exists() else 'MISSING'}")
print(f"    probes file     {s.probes_path}  {'OK' if s.probes_path.exists() else 'MISSING'}")
PYEOF

section "cache"
if compgen -G "cache/*" >/dev/null; then
  ls -la cache | sed 's/^/    /'
else
  say "cache/ is empty"
fi
[[ "$MODE" != live || -f cache/i24_index.json ]] || say "WARNING: cache/i24_index.json missing; run: $PY -m perjury.index_i24"
[[ "$MODE" != live || -f cache/scene_probes.json ]] || say "WARNING: cache/scene_probes.json missing; scene-wide claims will be UNVERIFIABLE (run: $PY -m perjury.prerun_scene_probes)"

section "port"
if lsof -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  say "port $PORT is busy:"
  lsof -iTCP:"$PORT" -sTCP:LISTEN | sed 's/^/    /'
  say "stop it (pkill -f app.main) or use another port: PORT=8090 $0 $MODE"
  exit 1
fi
say "port $PORT is free"

section "app"
say "PERJURY ($PERJURY_MODE) → http://localhost:$PORT/   (Ctrl-C to stop)"
say "health check once it's up: curl -s localhost:$PORT/health"
PORT="$PORT" "$PY" -u -m app.main
