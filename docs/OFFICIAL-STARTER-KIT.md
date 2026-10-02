# The official starter kit, and what it changes for UNWATCHED

> **Cleanup note (2026-10-02):** some raw captures and docs cited below were moved to [`unwanted/`](../unwanted/README.md) with their paths preserved (e.g. `docs/sources/x.md` is now `unwanted/docs/sources/x.md`). See `unwanted/MANIFEST.tsv`.

Found on 2026-10-01 at 18:16 PT (the night before SF) by searching GitHub for the event:
- **[vast-data/vast-builders-challenge](https://github.com/vast-data/vast-builders-challenge)**: the official starter repo. It is pre-cloned on the event VM and was last pushed 2026-10-01. Copied to `.firecrawl/starter-repos/official-vast-data/`.
- [relaxedtomato/vast-builders-challenge](https://github.com/relaxedtomato/vast-builders-challenge): an earlier version of the same repo. Copied to `.firecrawl/starter-repos/relaxedtomato/`.
- [virtualsheng/team-a-cross-city-safety-board](https://github.com/virtualsheng/team-a-cross-city-safety-board): a dry-run team's project with candid feedback. Copied to `.firecrawl/starter-repos/virtualsheng-team-a/`.

Other web results were the Luma, AWS Builder Center and PlanetZoop listings, plus LinkedIn posts by VAST, Ram Bansal, Brian Verkley, Andy Pernsteiner and W&B (Anna Shive), which LinkedIn blocked from scraping. The tokens& project gallery is still empty, and the Cosmos "Workshop" category has no public topics yet.

## How the day actually works (from BUILD_DAY.md and ARCHITECTURE_REFERENCE.md)
- **Access:** join the Cosmos Community, then open **`workshop.thecosmoslabs.com`** and click "Open Desktop". You get a browser-based **VM with the repo pre-cloned** at `~/vast-builders-challenge`. Run `agent`, the Cursor CLI, from there and set `/model` to Auto. *Nothing runs on your laptop.*
- **Teams:** pick your assigned team (e.g. `team-1`) at VM login. Teammates share **one ingest pipeline, one index and one set of credentials**.
- **Credentials:** they're already in the environment and in `/config/<team>.config`. Never run bare `env` or `printenv`; list names with `env | cut -d= -f1`. The variables are:
  - `USERNAME PASSWORD`
  - `S3_ENDPOINT ACCESS_KEY SECRET_KEY S3_CHUNKS_BUCKET S3_SEGMENTS_BUCKET`
  - `VDB_ENDPOINT VASTDB_BUCKET VDB_SCHEMA VDB_COLLECTION VDB_PROMPTS_COLLECTION`
  - `PIPELINE INGRESS_URL`
  - `WANDB_API_KEY WANDB_TEAM WANDB_PROJECT`
  - `COSMOS3_REASON_URL YOLO_URL COSMOS_EMBED1_URL CANARY_1B_URL COSMOS3_REASON_MODEL COSMOS_EMBED1_MODEL`
  - `GPU_BEARER_TOKEN`
- **Models** (shared CoreWeave GPU endpoints; you don't deploy them):

  | Model | What it does | Endpoint |
  |---|---|---|
  | **Cosmos3-Reason** (`nvidia/cosmos3-reason`) | Describes and reasons over segments | `/v1/chat/completions` (OpenAI-style), video sent as `{"type":"video_url","video_url":{"url":"data:video/mp4;base64,…"}}` |
  | **YOLO11s** | Object detection | `/v1/infer` with `video_base64`; health at `/healthz` |
  | **Cosmos-Embed1** | Embeddings, **256-d** | `/v1/embeddings`; video goes in as a data URI |
  | **Canary-1B** | Speech-to-text, **not wired into the pipeline** | An unused feature worth flexing |

  All of them take a `GPU_BEARER_TOKEN` bearer token.
- **Pipeline:** a DataEngine graph runs Segmenter, Detector (YOLO), Reasoner (Cosmos3), Embedder and VastDB writer, with a scheduled prompt-suggester alongside. *"Treat the graph as given — don't rebuild functions or redeploy the pipeline."* The official repo **removed** the earlier `dataengine-components` skills (build-function, triggers, pipeline-manifest).
- **Archive:** **pre-ingested**. Teams mostly **re-ingest** existing segments with a new prompt (`reingest-videos`, `reingest-chunk`; custom prompt ≤800 chars, scenario presets `surveillance traffic live_driving retail warehouse egocentric sports nhl general`).
  - Re-ingest takes a few minutes. Designate 1–2 people to run large re-ingests.
  - **Uploading new videos is supported** through `POST /api/v1/videos/upload` (multipart, max `app.max_upload_size_mb`, typically 25–100 MB). Indexing takes "tens of seconds to a few minutes".
  - *Don't ingest internet or YouTube video*, for licensing reasons.
- **Skills** in `.cursor/skills/`:
  - `ingest/`: upload-video, reingest-videos, reingest-chunk
  - `retrieval/`: search, agent-qa, videos, dashboard, list-metadata, suggest-prompts, login, vastdb-read
  - `gpu/`: model-health, model-smoke-test
  - `deployment/`: deploy-app-no-registry deploys to **your team's Kubernetes namespace at `/app`**; also build-yamls, deploy, health
  - `ask-cosmos`, `submission`
- **Search defaults:** `top_k` 15 and `min_similarity` (0.3–0.8 recommended). `chunk_results` answers "which video" and `results` answers "which moment".
- **Build a web app, CLI or script.** No native or mobile apps.
- **Submission:** the `submission` skill writes `SUBMISSION.md` (description under 40 words, stack, code link, optional live app link, feedback). That skill says never to collect personal details, while the tokens& portal asks for team names and emails, so **follow the portal**. A first round of judging is done **with each team at their table**, before the stage demos.

## The video corpus (pre-indexed)
| Pack | `camera_id` | What | Fit for UNWATCHED |
|---|---|---|---|
| A: Highway multi-cam (Nashville I-24) | `i24_cam-1` | ~51 multi-cam highway clips | Low |
| B: Live driving (Toronto PIE) | `pie_cam-3` | 6 long drive sets (dashcam) | Low, the camera moves |
| **C: Warehouse safety (SDG, synthetic)** | `sdg_warehouse_cam-2` | ~178 ceiling and aisle clips | **High**: a fixed camera, operational space, near-misses |
| **D: Neighborhood streets** | `neighborhood_cam-1` | **2 full days** (2026-09-01, 09-02) | **High**: a real "overnight / all-day nobody watched" story |
| E: SF streets | `sf_streets_cam-1..4` | 4 fixed cameras (*ingesting soon*) | Medium: multi-camera, public space, so watch the privacy framing |
| **F: Indoor smart spaces** | `smartspace_cam-1` | ~102 indoor facility clips | **High**: occupancy and after-hours |

The organizers' anchor query is *"person close to a moving vehicle"* across packs.

## Lessons from the dry run (virtualsheng, Team A's SUBMISSION.md)
- **Re-ingest is risky under time pressure.** One job stalled partway, **there is no cancel API**, and after a backend restart the job vanished while `pending_index` stayed at 62. → Re-ingest small batches early, and never on the critical path after about 14:00.
- **Hybrid search at the 0.35 threshold returned nothing** with a `general` ingest prompt. → Lower `min_similarity` and scope searches by `camera_id`.
- **Captions over-claim:** a car got labelled a bus. → Cross-check captions with YOLO classes and box sizes. That's our "second signal" argument.
- **The starter repo's `origin` is a shared template, and `SUBMISSION.md` is gitignored there,** so the team needed **a separate public GitHub repo**. → Ours is `nihalnihalani/vast-builders-challenge`; make it public before submitting.

## What changes in UNWATCHED (supersedes FINAL-IDEA §5 architecture)
1. **No custom DataEngine functions.** `nw-scorer`, `nw-verifier`, `nw-baseline-updater` and `nw-digest` become **one Python service in our app**, deployed with `deploy-app-no-registry` to team Kubernetes at `/app`, or run on the VM while iterating. It polls VastDB (`vastdb-read`, `vss-collection`: `vectors_visual`, `reasoning_content`, metadata) or the backend `videos/explore` endpoint for new segments, computes the per-camera centroid and distance, and calls the verifier.
   - *Pitch it honestly:* "the pipeline VAST gave us is the ingest; UNWATCHED is the watcher that sits on the VastDB index."
   - The pipeline still uses DataEngine through ingest, re-ingest and upload, and the scheduled prompt-suggester is a DataEngine schedule trigger we can point to.
2. **Verifier = direct Cosmos3-Reason calls** to `$COSMOS3_REASON_URL/v1/chat/completions` with the `GPU_BEARER_TOKEN` bearer. `src/verifier_backends.py` now reads these event variables. Cosmos3 beats Reason2 on VANTAGE event verification, which is good news (see TRENDS.md). Keep Gemini as an outage-only fallback, if the VM has outbound internet.
3. **Embeddings stay 256-d Cosmos-Embed1.** The 768-d anomaly embedder isn't on the event stack, so drop that idea.
4. **Archive = Packs C + F + D**: warehouse, indoor and neighborhood, with D's two full days as the "nobody watched this" proof. Re-ingest a subset with a UNWATCHED-specific custom prompt (≤800 chars) so the captions record what the verifier and digest need: people, carried objects, vehicles stopped, doors, time-of-day context.
5. **Live camera #5 = a webcam clip pushed through `upload-video`.** ⚠️ Indexing takes tens of seconds to minutes, so the "phone buzzes" beat needs a pre-recorded upload fallback.
   - **Better option:** for the live beat, **call Cosmos3-Reason directly on the recorded 5 s clip**, bypassing the pipeline. Then upload it for indexing in the background.
   - The VM is browser-based, so the webcam has to run on a laptop that can reach the Cosmos endpoint, or be recorded and uploaded. Check this on site.
6. **The digest** uses W&B Inference (`WANDB_*` env), with a Slack webhook if the VM has egress. Otherwise use an in-app "Morning digest" panel plus a QR code that teammates open on their phones.
7. **Optional flex:** Canary-1B transcribes audio on flagged clips (e.g. alarms, shouting). It's unused by the default pipeline, so it's a strong "unpopular feature" for the NVIDIA judges.

## First 30 minutes on site (replaces FINAL-IDEA §9 items that assumed DataEngine function deploys)
- [ ] Log into `workshop.thecosmoslabs.com`, pick the team, run `git pull`, then ask Cursor to "check that everything is working".
- [ ] Run `gpu/model-smoke-test`. Time Cosmos3-Reason on one 5 s clip (yes/no with `max_tokens` 8, vs a full reasoning answer).
- [ ] Run `vastdb-read`: confirm `vss-collection` has `vectors_visual` for Packs C, F and D, and set up the SSH tunnel.
- [ ] Run `list-metadata`: confirm the `camera_id`s and whether SF Pack E has finished ingesting.
- [ ] Check egress from the VM: `curl -sI https://hooks.slack.com` and `https://generativelanguage.googleapis.com`.
- [ ] Ask staff whether a laptop webcam clip may be uploaded (it isn't internet video, but confirm).
- [ ] Clone `nihalnihalani/vast-builders-challenge` onto the VM next to the starter repo. Our repo is the submission repo.
