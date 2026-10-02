#!/usr/bin/env bash
# Run PERJURY from the repo root.
#   ./run.sh              real endpoints → http://localhost:8080/
#   ./run.sh live         real endpoints (event VM: needs INGRESS_URL etc. in the env or /config/<team>.config)
#   ./run.sh test         run the test suite
#   PORT=9000 ./run.sh    another port
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

MODE="${1:-live}"
PORT="${PORT:-8080}"
VENV=.venv
PY="$VENV/bin/python"

# 1. Python 3.12 venv with the runtime deps (first run only, or when requirements.txt changes)
if [[ ! -x "$PY" ]]; then
  echo "== creating $VENV"
  if command -v uv >/dev/null; then uv venv -q -p 3.12 "$VENV"; else python3 -m venv "$VENV"; fi
fi
STAMP="$VENV/.requirements.sha"
SHA="$(cat requirements.txt | shasum | cut -d' ' -f1)"
if [[ ! -f "$STAMP" || "$(cat "$STAMP")" != "$SHA" ]]; then
  echo "== installing requirements"
  if command -v uv >/dev/null; then
    uv pip install -q --python "$PY" -r requirements.txt pytest pytest-asyncio
  else
    "$PY" -m pip install -q -r requirements.txt pytest pytest-asyncio
  fi
  echo "$SHA" > "$STAMP"
fi

case "$MODE" in
  test)
    exec "$PY" -m pytest -q
    ;;
  fixture)
    [[ -f cache/fixture_i24_index.json ]] || "$PY" tools/make_fixtures.py
    export PERJURY_MODE=fixture
    ;;
  live)
    # On the VM, pick up this team's config if the env doesn't already have it (values are never printed).
    if [[ -z "${INGRESS_URL:-}" && -z "${VSS_URL:-}" && -z "${PERJURY_TEAM_CONFIG:-}" ]]; then
      cfg="$(find /config -maxdepth 1 \( -type f -o -type l \) -name '*.config' 2>/dev/null | sort | head -n 1 || true)"
      [[ -n "$cfg" ]] && export PERJURY_TEAM_CONFIG="$cfg"
    fi
    [[ -f cache/i24_index.json ]] || echo "WARNING: cache/i24_index.json missing; run: $PY -m perjury.index_i24"
    [[ -f cache/scene_probes.json ]] || echo "WARNING: cache/scene_probes.json missing; run: $PY -m perjury.prerun_scene_probes"
    export PERJURY_MODE=live
    ;;
  *)
    echo "usage: $0 [fixture|live|test]" >&2; exit 2 ;;
esac

if lsof -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  echo "port $PORT is busy; try: PORT=8090 $0 $MODE" >&2; exit 1
fi
echo "== PERJURY ($PERJURY_MODE) → http://localhost:$PORT/   (Ctrl-C to stop)"
PORT="$PORT" exec "$PY" -m app.main
