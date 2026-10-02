# PERJURY build contract (branch `charlie`)

The spec is `docs/FINAL-IDEA-v3.md` (§ refs below). This file pins the interfaces between modules so they can be built in parallel. **If you need to change a shared interface, change this file too and say so in your report.**

## Ground rules
- Python 3.12 (pod is `python:3.12-slim`). Venv: `.venv/bin/python` (already has fastapi, uvicorn, httpx, pydantic, pyyaml, pillow, imageio-ffmpeg, python-multipart, pytest, pytest-asyncio, numpy, openai, weave). Add new deps to `requirements.txt` (runtime) or `requirements-dev.txt`.
- Run from repo root; packages are imported as `perjury.*`, `app.*`, `bench.*`.
- **Two modes** (`perjury/config.py`): `PERJURY_MODE=live` (real endpoints on the event VM/pod) and `fixture` (offline: fake clients in `perjury/fakes.py` over `cache/fixture_*.json`). Fixture mode must work with zero network and zero credentials. The UI shows a FIXTURE banner in fixture mode, a REPLAY banner in replay mode. Never fake a live chip.
- `cache/fixture_truth.json` is hidden ground truth: **only `perjury/fakes.py` may read it.**
- Never print or log secrets (`GPU_BEARER_TOKEN`, VSS password, S3 keys, `WANDB_API_KEY`). Redact base64 and tokens in anything sent to the UI ribbon or Weave.
- Weave is optional at import time: use `perjury/obs.py` (`op` decorator that is a no-op without weave/key).
- No custom DataEngine functions; never write `*.mp4` into the pipeline buckets (exhibits go through `videos/upload` only).
- Don't edit `lastframe/`, `src/`, `unwanted/`, `.firecrawl/`. Copy from them.
- Do **not** `git commit`; the lead commits.

## Shared modules (already written, lead-owned)
- `perjury/types.py`: `Atom`, `AtomType`, `Juror`, `Vote`, `AtomVerdict`, `ClaimVerdict`, `Segment`, `COCO_CLASSES`.
- `perjury/events.py`: `EventBus` (`emit`, `service`, `stream`, JSONL recording), `sse_format`, event names + payloads, `SERVICES`, `BADGES`.
- `perjury/config.py`: `Settings` / `settings()`; `CACHE`, `ROOT`.
- `perjury/obs.py`: `op(name)` Weave decorator (no-op without weave/key), `init()`, `redact()` (use it for ribbon request/response too), `current_call_url()`.
- `tools/make_fixtures.py` → `cache/fixture_i24_index.json`, `cache/fixture_scene_probes.json`, `cache/fixture_truth.json`.

### Index file (`cache/i24_index.json`, fixture twin `cache/fixture_i24_index.json`)
```json
{"version":1,"source":"vastdb|vss-tools|fixture","camera_id":"i24_cam-1",
 "scenes":{"1":{"label":"free-flow","duration":90,"cameras":["p1c1",...]},"2":{...},"3":{...}},
 "segments":[Segment, ...]}
```
### Scene probes (`cache/scene_probes.json`, twin `cache/fixture_scene_probes.json`)
```json
{"version":1,"probe_versions":{"P-COND":"v1","P-COUNT":"v1"},"ran_at":"<iso>",
 "scenes":{"2":{"p1c1":{"P-COND":{"parsed":{"road":"C","traffic":"B","light":"A"},"latency_ms":4100},
                         "P-COUNT":{"parsed":{"panels":[{"panel":1,"people_on_foot":0,"bicycles":0,"motorcycles":0,"visibility":"clear"}]},"latency_ms":3900},
                         "grid_times":[6.0,21.0,36.0,51.0]}}}}
```
`parsed` may be `null` (invalid JSON → juror abstains).

### Promotion state (`cache/promotion.json`, written by `bench/run_bench.py --freeze`; absent ⇒ defaults in `claim_types.yaml`)
```json
{"frozen_at":"<iso>","types":{"towing":{"promoted":true,"catch":0.9,"false_accusation":0.0,"n":7}}, "alpha":{"towing":0.1}, "m":{"towing":3}}
```

## Client interfaces (`Clients` bundle; live in `perjury/*.py`, fakes in `perjury/fakes.py`)
All network methods are `async`. Every live call reports to the ribbon through the `bus` argument when given: `bus.service(name, "firing")` then `bus.service(name, "done", ms=..., gpu=<True for GPU-host models>, request=<redacted>, response=<redacted/truncated>)`, or `"error"`.

```python
# perjury/clients.py
@dataclass
class Clients:
    llm: LLM; cosmos: Cosmos; embed: Embed; yolo: Yolo; canary: Canary; vss: VSSClient; media: Media
def build_clients(s: Settings) -> Clients   # live or fakes depending on s.mode

class LLM:      # W&B Inference, OpenAI-compatible, service "wandb_inference"
    async def complete_json(self, system: str, user: str, *, temperature=0.0, max_tokens=1200, bus=None, purpose="") -> dict
class Cosmos:   # service "cosmos3"; semaphore(s.cosmos_concurrency); disk cache keyed (image_sha, probe_version, prompt_sha) in cache/cosmos/
    async def probe(self, image_jpeg: bytes, prompt: str, probe_version: str, *, timeout_s: float, bus=None) -> ProbeResult
# ProbeResult(BaseModel): parsed: dict|None, raw_text: str, latency_ms: int, cached: bool, cached_at: str|None, image_sha: str, error: str|None
#   <think> stripped, JSON repaired; temperature 0; max_tokens 512; image sent as {"type":"image_url","image_url":{"url":"data:image/jpeg;base64,..."}}
class Embed:    # service "embed1"
    async def embed_text(self, text: str, *, bus=None) -> list[float]            # request_type "query", 256-d
    def visual_vectors(self) -> dict[str, list[float]] | None                     # source -> 256-d (cache/embed_visual.json/.npy); None if unavailable
class Yolo:     # service "yolo"
    async def infer(self, *, url: str|None = None, video_b64: str|None = None, bus=None) -> dict   # raw /v1/infer response
    async def zoom_check(self, crop_mp4: bytes|None, crop_url: str|None, *, min_cover=0.30, bus=None) -> ZoomResult
# ZoomResult(BaseModel): ok: bool, label: str|None, conf: float|None, cover: float|None, frames_ok: int, error: str|None
class Canary:   # service "canary"
    async def transcribe(self, wav: bytes, *, bus=None) -> dict   # {"text","model_id","latency_ms"}
class VSSClient:  # service "vss" (and "dataengine" for upload/suggestions)
    async def detections(self, source) -> dict|None; def stream_url(self, source) -> str
    async def search_and_answer(self, claim: str, camera_id: str, *, bus=None) -> dict   # §6 stock A/B prompt, exact text
    async def ask(self, question, original_video=None, *, bus=None) -> dict
    async def synthesize(self, original_video, question="Summarize what happens in this video", max_segments=20, *, bus=None) -> dict
    async def suggestions(self, *, bus=None) -> list[dict]; async def dashboard_stats(self, *, bus=None) -> dict
    async def upload(self, mp4: bytes, filename: str, metadata: dict, *, bus=None) -> dict
    async def segments(self, original_video) -> list[dict]; async def explore(self, limit=48, offset=0) -> dict
class Media:    # service "s3" for presigned GETs; ffmpeg via imageio-ffmpeg
    def presign(self, source: str, expires=3600) -> str
    async def keyframes(self, source: str, times: list[float], width: int = 1920) -> list[bytes]   # JPEGs; seek with -ss before -i
    def grid2x2(self, frames: list[bytes], labels: list[str] | None = None) -> bytes              # 1920x1080 JPEG, panel numbers 1-4 burned in
    async def crop_clip(self, source: str, t: float, box_px: tuple[int,int,int,int], dur: float = 0.5) -> bytes  # 4K crop as mp4
    async def tile(self, scene: int, camera: str) -> bytes   # 480 px wall thumbnail (cache/tiles/), warmed at boot
```

### Fake behaviour (`perjury/fakes.py`, fixture mode) — must make the §14 demo come out right
- Latency: sleep `s.fixture_latency × realistic_ms` (Cosmos 2.5–6 s, Embed 0.15 s, YOLO 0.4 s, LLM 0.6–1.2 s, Canary 0.8 s). `fixture_latency=0` ⇒ instant (tests).
- **FakeCosmos** recognises the probe by `probe_version` prefix (`P-TOW`, `P-GROUND`, `P-COND`, `P-COUNT`, `P-LEAD`). The image it receives is produced by `FakeMedia`, which embeds a tiny JSON tag in the JPEG comment (`COM` segment) naming `source` + `times`; FakeCosmos reads that to look up `fixture_truth.json`. P-TOW: yes on truth panels; false-yes with prob 0.05 per juror on non-towing grids (deterministic hash). P-LEAD: says `witness_correct: true` with prob 0.6 regardless (sycophancy). P-GROUND: a plausible box. P-COND/P-COUNT: answer from `scene_conditions` / zero people.
- **FakeYolo.zoom_check** ok iff the crop came from a truth-towing segment (or a false-yes, 50%).
- **FakeLLM**: atomizer requests ⇒ return `None`-equivalent so the **rules parser** is used (labelled "rules" in the trace) — or a rules-derived JSON; T1 labeller ⇒ contradiction-first keyword labelling of the snippets it is given.
- **FakeEmbed.embed_text** ⇒ deterministic 256-d vector; `visual_vectors()` ⇒ vectors where towing-truth segments score highest against any text containing "trailer|tow".
- **FakeCanary** ⇒ returns the text in a `X-Fixture-Transcript` side channel or "A pickup is towing a trailer." **FakeVSS**: canned responses (stock agent answers "TRUE ..." for most lies — G2 unknown; it is labelled FIXTURE).
- **FakeMedia**: Pillow-rendered 480/1920 px dark frames with lanes, little vehicle rectangles, snow speckle for scene 2, "FIXTURE · scene{n} {cam} t=…" watermark.

## Core pipeline (`perjury/pipeline.py`)
```python
@dataclass
class Context:
    settings: Settings; clients: Clients; index: SceneIndex; probes: dict; router: Router
async def testify(text: str, scene: int, ctx: Context, bus: EventBus, *, transcript_source="typed",
                  stock_ab=False, jury_size: int|None = None, probe_overrides: dict|None = None) -> ClaimVerdict
def load_context(s: Settings | None = None) -> Context
```
Emits, in order: `run`, `transcript`, `atoms`, then per atom any of `t0`/`t1`/`summon`/`juror`/`ground`/`zoom`, `atom_verdict`; then `verdict`, (`stock`), `receipt`, `done`. Atoms are processed concurrently; per-atom 20 s cap; per-juror 8 s cap. Also returns the `ClaimVerdict`. `bench` calls the same function with a throwaway bus.

`perjury/index.py`: `SceneIndex.load(path)`; `.segments(scene, camera=None)`, `.cameras(scene)`, `.scene_parent(scene, camera)`, `.captions(scene)`.

## App (`app/main.py`, FastAPI) — routes are relative to `/` (Ingress strips `/app`), so the UI must use **relative URLs** (`api/testify`, not `/api/testify`).
- `GET /` UI · `GET /health` → `{"ok":true,"mode","pod","index_segments","probes":bool}`
- `POST /api/testify` JSON `{text, scene, stock_ab?, transcript_source?}` → `text/event-stream` (SSE)
- `POST /api/transcribe` multipart `file` (16 kHz mono WAV) → `{text, model_id, latency_ms}`
- `GET /api/scene/{n}` → scene meta + cameras + T0 summary for the wall
- `GET /api/tile?scene=&camera=` → JPEG · `GET /api/exhibit?run_id=&atom_id=&camera=` → exhibit JSON + `GET /api/exhibit.jpg?...`
- `GET /api/bench` → `cache/bench_report.json` · `GET /api/witness` → `cache/witness.json` · `POST /api/witness/run`
- `GET /api/replays` · `GET /api/replay/{name}` → SSE re-emit with original timing, every event carries `replay: true`
- `POST /api/feedback` `{run_id, thumbs: "up"|"down", note}` → Weave feedback + `cache/feedback.jsonl`
- CORS on (option c in §10).
- Additive (app): `/api/transcribe` also returns `transcript_id`. `/api/testify` accepts `transcript_id` and `jury_size`. With `transcript_source:"canary"` and an unedited transcript, the app emits the real Canary call as `bus.service("canary","done",…)` *before* calling `testify`, so the pipeline must not emit a canary service event itself. `GET /api/stream?run_id=&atom_id=&camera=` is a Range proxy to VSS `videos/stream`, so the token stays server-side. `GET /api/replay/{name}?speed=` (0 = instant). `/health` adds `pipeline`, `pipeline_error`, `dev_stub`, `weave`, `tiles_warm`. Replays are listed from `cache/runs/` and `cache/replays/` (curated, shipped to the pod).
- Ribbon rendering: a `service` event with state `"pipeline"`, or a note starting with "pipeline", renders as an outlined (pipeline-output) chip. `done` renders solid (live call).

## Ownership (parallel build)
| Owner | Files |
|---|---|
| core | `perjury/atomize.py`, `router.py`, `claim_types.yaml`, `quorum.py`, `verdict.py`, `tiers.py`, `pipeline.py`, `index.py`, `probes.py`, `tests/test_atomize_spans.py`, `tests/test_quorum.py`, `tests/test_router.py`, `tests/test_pipeline_fixture.py` |
| clients | `perjury/clients.py`, `cosmos.py`, `llm.py`, `vss.py`, `yolo.py`, `embed.py`, `canary.py`, `media.py`, `fakes.py`, `index_i24.py`, `prerun_scene_probes.py`, `witness.py`, `exhibit.py`, `store.py` (verdict rows: VastDB `perjury_verdicts` if writable else `cache/verdicts.jsonl`), `preflight.py` (repo root), `tests/test_clients_fake.py`, `tests/test_media.py` |
| app | `app/**`, `deploy/**`, `requirements.txt`, `docs/CHROME-FLAG-CARD.md`, `tests/test_app.py` |
| bench | `bench/**`, `tests/test_bench.py`, `.cursor/rules/perjury.mdc`, `.cursor/skills/perjury-verify/SKILL.md`, `docs/slides/`, `docs/QA-CARD.md` |

## Alignment with the official BUILD_DAY.md (checked 2026-10-02 against vast-data/vast-builders-challenge@main)
- **GPU endpoints need no auth token** (config.example, ARCHITECTURE_REFERENCE). `GPU_BEARER_TOKEN` is optional everywhere; the bearer header is sent only when set.
- **Model ids:** `COSMOS3_REASON_MODEL=nvidia/cosmos3-reason`, `COSMOS_EMBED1_MODEL=nvidia/cosmos-embed1`; `CANARY_1B_MODEL` is unset on purpose (we try it first if set, then the §10 variants).
- **/config files may be team-prefixed:** `kubeconfig` | `<team>-k8s.yaml`. WANDB_* may live only in the environment.
- **"Nothing runs on your laptop."** Voice option (c) (laptop localhost copy of the UI) is dropped. The laptop is a browser only (option a).
- **Max 2 VMs per team.** The §12 four-person table assumes 4 terminals; P3/P4 work through a teammate's VM or the VSS UI.
- **"You don't call [the models] directly, you query the vectors generated"** (BUILD_DAY recap) describes the default path; the gpu/ skills and ARCHITECTURE_REFERENCE ("Ask Cursor how to call each model", Canary "hook it in") allow direct calls. PERJURY reads the pipeline's vectors/captions/YOLO first (T0/T1) and calls models directly only for T2 jurors, zoom-checks and ASR; say this plainly if asked.
- **Corpus:** BUILD_DAY now names three kinds of footage (dashcam, I-24 highway, neighborhood). Pack A (`i24_cam-1`) is still there; ASSAY's PIE fallback too.
