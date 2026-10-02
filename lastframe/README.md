# LAST FRAME

**Turn a video archive into a decision room.** Watch a short observation window, commit a prediction and confidence level, then see the continuation and replay the evidence.

This is a fresh project built around the hackathon corpus. The entry point is Pack B's Toronto dashcam footage, with Pack C warehouse interactions as the second use case. Ordinary scenes are useful: crossing versus waiting, pausing versus passing, and traffic moving versus stopping. An incident is not required.

## Run locally

```sh
python3 lastframe/app.py --port 8787
```

Open http://127.0.0.1:8787. Python 3.10+; no third-party runtime dependencies, npm install, external fonts, or internet connection needed for the storyboard demo.

**Current data:** six explicitly labeled schematic storyboards, authored from the corpus descriptions. They are not real event footage, model predictions, or results from the VSS index. No event credentials or videos are present in this checkout. The VSS adapter and W&B drafting path are implemented; their live connectivity remains unverified until run on the workshop VM.

## What's implemented

- Observation playback, a decision freeze, choice and 50/70/90% confidence.
- Outcome and evidence withheld on the server until a choice is committed. Live continuation stream is also gated. A round cannot change its answer after commitment.
- Continuation playback and timestamped evidence replay.
- Six storyboards across driving, warehouse, highway, indoor and neighborhood scenes; Pack E remains pending ingestion.
- Local browser session notes, matched-continuation totals, binary Brier score and Markdown export. Scores describe this practice sample, not driving ability or certification.
- Studio: VSS search → parent timeline → adjacent segment selection → preview both → manual authoring or optional two-pass W&B draft → human review → publication.
- Persistent reviewed scenarios in `lastframe/data/scenarios.json`. Originals stay in VSS; no video copies are stored locally.
- Server-side VSS authentication, token refresh on 401, streaming with Range forwarding, bounded requests and explicit errors. No API key or JWT goes into the frontend.

## Connect the workshop VM

Use **your assigned team's config**, not another team's. The app reads that exact file as data and never executes it as shell code:

```sh
export LASTFRAME_TEAM_CONFIG=/config/<assigned-team>.config
python3 lastframe/app.py --port 8787
```

Alternatively, supply `INGRESS_URL` and `VSS_TOKEN` in the process environment, or `INGRESS_URL`, `USERNAME` and `PASSWORD`. Do not paste credentials into chat, commit config files, or put them in browser URLs.

The studio uses the official starter-kit contracts:

- `POST /api/v1/auth/login`
- `POST /api/v1/search` (ranked hits, low initial threshold)
- `GET /api/v1/tools/segments?original_video=…`
- `GET /api/v1/videos/stream?source=…&token=…` (server-to-server)

Only segment sources returned by this app's search/timeline are eligible for publishing or studio playback. Timing aliases are normalized in `vss.py`; unfamiliar response shapes fail explicitly. Confirm the live VM's shape during the first smoke test. Missing timing, gaps, or different parent videos block publication. The prototype assumes these stream sources are individual segment clips, as documented by the starter kit.

For optional W&B/Forge drafting:

```sh
export LASTFRAME_WANDB_MODEL='<model ID available to your workshop account>'
```

The process also needs `WANDB_API_KEY`. The default OpenAI-compatible base is `https://api.inference.wandb.ai/v1`; `WANDB_BASE_URL` overrides it. The first pass receives **only the observation caption** and drafts the context/question/options. The second pass receives the options and continuation caption to propose an answer and evidence. Ambiguous answers are rejected. A human watches the actual footage, verifies the timestamps and edits the draft before publication. Caption text is never presented as independently verified video understanding.

## Architecture

```text
Existing VAST pipeline (unchanged)
  video → YOLO / Cosmos descriptions / embeddings → VSS / VastDB
                                                        │
Studio: search → adjacent segments → two-pass draft → human review
                                                        │
                              persistent scenario definitions
                                                        │
Learner: observe → commit choice + confidence → unlock continuation
                                                        │
                                      evidence replay / session notes
```

`app.py` is the HTTP service, `engine.py` owns round state and validation, `vss.py` integrates the workshop, and `web/` contains the responsive UI and schematic renderer. Round state expires after two hours. Scenarios persist; active rounds do not survive server restart. Learner notes stay in the browser and are capped at 200 attempts.

The scenario studio is a **trusted local instructor tool**, with no separate instructor login. The server binds to loopback by default. Before exposing it to a public audience, add authenticated instructor/learner roles and access control; instructor preview deliberately has access to continuations. Use the official deployment skill to route it on the workshop VM, confirming those boundaries before allowing untrusted users.

## Tests

```sh
python3 -m unittest discover -s lastframe/tests -v
node --check lastframe/web/app.js
```

Tests cover hidden future data, locked streams, immutable/idempotent answers, confidence scoring, concurrent commitment, round isolation/expiry, live-scenario validation, publication persistence, HTTP lifecycle, same-origin commits, response normalization and separation of model drafting inputs. VSS and model responses in tests are mocks, not evidence of live integration success.

## Two-minute demo

1. **0:00–0:15:** “A video archive already contains what happens next. We turn it into practice.” Show the six-pack corpus map.
2. **0:15–0:45:** Play The curbside pause. Ask a judge to choose an outcome and confidence. Commit, reveal, replay evidence.
3. **0:45–1:10:** Play Beside the bus stop. Similar setup, different continuation. Show the learner's confidence change and session notes.
4. **1:10–1:35:** Switch to the warehouse drill to show the same workflow transfers to a different setting.
5. **1:35–2:00:** On the connected VM, show one human-reviewed VSS drill and its source segments in the studio. “The next training exercise is already in your footage.”

For a local demo, say **storyboard** explicitly and show the implemented connection workflow; do not imply the archive has been queried. For submission, replace the first two drills with reviewed Pack B clips and show actual playback.

## Highest-value additions

1. **Clip harvesting:** search a few B/C queries, select 8–12 contiguous before/after pairs and publish human-reviewed drills. This is the immediate next step once VSS is accessible.
2. **Weave evaluation:** measure draft answer agreement, caption unsupported-claim rate, timestamp validity and drafting latency against human-labeled pairs. Optional observability is not implemented yet.
3. **Temporal option ordering:** shuffle options and evaluate the learner on held-out clips. Keep calibration statistics separate for first attempts and repeats.
4. **Adaptive practice:** choose the next unseen drill from skills with weaker first-attempt performance.
5. **Multi-view evidence for A/E:** link synchronized views when metadata supports it. Do not assume the camera_id alone identifies a physical viewpoint or attempt cross-camera identity matching.
6. **Instructor tools:** cohort assignments, review queues, role-based access and a reviewed scenario export/import format.
7. **Vision verification:** on the VM, independently verify drafted answers against clips through the provided Cosmos endpoint. Keep human review until measured accuracy supports more automation.

Build these after real VSS playback works; the core demo already demonstrates the complete training interaction.
