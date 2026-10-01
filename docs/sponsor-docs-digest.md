# Sponsor Docs Digest (build-day reference)

Source scrapes live in `.firecrawl/`. Items marked **[not in scrape]** come from general SDK knowledge, so check them before relying on them.

## 1. NVIDIA VSS 3.2.1 (latest)
*Sources: vss-release-notes.md, nvidia-vss-docs.md, vss-search.md, vss-rt-alert.md, vss-alert-verification.md, vss-lvs.md, vss-warehouse-agents.md*

**What's new.** 3.2.1 is a bug-fix release. It switches the default VLM for RT-VLM and the agent workflows to **Cosmos Reason 3 Nano** (`nvidia/cosmos3-nano-reasoner`). 3.2.0 was the first 3.x GA release and added:
- source code on GitHub
- Agent Skills (EA) for Claude Code/Codex/NemoClaw
- Helm charts for every workflow
- an Orchestrator MCP server
- audio-in-video through Nemotron Nano Omni
- Alerts post-processing modes (verify, contextualize, classify)

Older 2.x–3.1 images are deprecated and are removed from NGC on Sep 30 2026.

**Common deploy pattern:** `export NGC_CLI_API_KEY=...; deploy/docker/scripts/dev-profile.sh up -p <profile> [-m <mode>] -H <H100|RTXPRO6000BW|L40S|DGX-SPARK|OTHER> [--use-remote-llm|--use-remote-vlm] [--llm-device-id 1 --vlm-device-id 2]`. UI at `:7777`, Kibana at `:7777/kibana`, Phoenix at `:7777/phoenix`, VST at `:30888`, NVStreamer at `:31000`. Default LLM is `nvidia/nvidia-nemotron-nano-9b-v2`. Deployment takes about 15–20 min.

**RT-VLM microservice API (3.2.0 notes):**
- `/v1/generate_captions_alerts` was renamed to **`/v1/generate_captions`**. It accepts `url` (`http/https/s3/file://`), `media_type` and `creation_time`, and returns `chunk_id`.
- Optional flags: `enable_reasoning: true` returns `reasoning_description` for each chunk; `enable_audio: true` works with Omni models.
- `DELETE /v1/generate_captions/{stream_id}` stops a stream's caption jobs. Text-only calls go to `/v1/chat/completions`.
- Model selection: `VLM_MODEL_TO_USE=cosmos-reason3` with `MODEL_PATH=ngc:nim/nvidia/cosmos3-nano-reasoner:bf16-final`. Reason2 is still available as `ngc:nim/nvidia/cosmos-reason2-8b:0303-fp8-dynamic-kv8`.

**RT-Embed:** `POST /v1/generate_video_embeddings` now accepts base64 `data:` URIs. Stream endpoints: `POST /v1/stream/add|remove`. The new default model is **`Cosmos-Embed1-448p-anomaly-detection`** (to switch: `RTVI_EMBED_MODEL=cosmos-embed1-448p`, `MODEL_PATH=git:https://huggingface.co/nvidia/Cosmos-Embed1-448p`). A duplicate stream ID now returns HTTP 409.

| Workflow | What it does | APIs / knobs | Models / latency notes |
|---|---|---|---|
| **Search** (`-p search`) | Natural-language and image search over embedded archives. Four routes: embed, attribute, fusion, and search-by-image. | Direct `/api/v1/search`; agent `/chat/stream`. Results return `video_name, start_time/end_time (ISO), similarity, sensor_id, screenshot_url, object_ids, critic_result{result: confirmed\|rejected, criteria_met{}}`. Knobs: `fusion_method` (`weighted_linear` w_embed .35/w_attr .55, or `rrf_with_attribute_rank` rrf_k 60), `embed_confidence_threshold: 0.1`, `top_percent_filter: 0.9`, `ENABLE_CRITIC`, `critic_agent.num_videos_to_evaluate: 5`. ES indices: `mdx-embed-filtered-*`, `mdx-behavior-*`. Optional **temporal dedup** keeps a sliding window of ~60 vectors; a new vector is skipped if it has ≥3 consecutive similar neighbours. | RTVI-Embed (Cosmos-Embed1 anomaly variant), RTVI-CV (SigLIP2), critic = Cosmos3 Nano Reasoner. Needs 2–4 GPUs. Up to 100 streams; 16 tested at 1080p with no FPS drop. |
| **Real-Time Alerts** (`-p alerts -m real-time`) | The VLM processes **every chunk** of a live stream against a **user-written rule** ("Detect anyone without PPE on sensor X"). | Alert Bridge: `POST/GET /api/v1/realtime`, `GET/DELETE /api/v1/realtime/{id}`, `POST /api/v1/realtime/always-on`, `POST /api/v1/realtime/replay`, `GET /api/v1/realtime/incidents`. Add sensor: `POST /vst/api/v1/sensor/add {sensorUrl,name}`. Env: `RTVI_VLM_BASE_URL`, `RTVI_VLM_MODEL_TO_USE`, `ALWAYS_ON_RULES_CONFIG`. Notifications: `webhook.openclaw.enabled`. | `cosmos-reason3` through RTVI-VLM. Docs say it needs more GPU than verification. **1 stream by default.** Debug with `docker logs -f vss-rtvi-vlm`. |
| **Alert Verification** (`-p alerts -m verification`) | Grounding DINO detects, Behavior Analytics applies **rules**, then the VLM returns a yes/no on each alert clip to cut false positives. | `POST /api/v1/verification/ondemand`; CRUD on `/api/v1/verification/config/{alert_type}`. Prompt lives in `alert_type_config.json` (`user`, `output_category`). G-DINO `type_name` default is "person" at threshold 0.5. Custom parser: `parse(self, raw_response) -> dict` set through `vlm.response_parser`. `NUM_SENSORS` (4 streams at 10fps tested on RTX PRO 6000). | VLM timeout defaults to **5 s**; raise it for remote VLMs. The parser only accepts raw `Yes/No`/`A/B`. Indices: `mdx-incidents-*`, `mdx-vlm-incidents-*`. |
| **Video Summarization** (formerly LVS, `-p lvs`) | Splits long video into chunks, runs the VLM on each, and synthesizes a summary or report. Live-stream captions, summary and Q&A are EA. | Takes a scenario, an events list and objects of interest (there are defaults). Prompts: "Summarize the stream CAM_1 from 45 seconds till now", "Were there PPE violations in CAM_1 from <ISO> to <ISO>?". Outputs a PDF report. | Cosmos3 Nano Reasoner through RTVI-VLM. Plain VLMs handle clips under about 1 min. The stream caption prompt is **overwritten by the latest session**. |
| **Warehouse agents** | A top-level router agent with `report_agent` and `multi_report_agent` sub-agents. | Tools: `vst_sensor_list`, `vst_picture_url`, `get_fov_counts_with_chart`, `video_analytics__get_incidents`, `template_report_gen`, `chart_generator`. Config: `industry-profiles/warehouse-operations/vss-agent/configs/config.yml` (`workflow.prompt`, `vlm_prompts`). | Nemotron Nano 9B v2 + Cosmos3 Nano Reasoner. 3.2 adds always-on RTVI-VLM alerts for Load Quality, PPE, Spillover and Obstructions. |

## 2. Overlap check vs UNWATCHED
*Sources: vss-rt-alert.md, vss-search.md, vss-release-notes.md, vss-lvs.md, vss-alert-verification.md*

**Verdict: the differentiation claim holds, but it needs careful wording.**

- **No VSS workflow learns a per-camera baseline and flags deviations without being prompted.**
  - Real-Time Alerts sells "anomaly detection" and "unusual behavior detection", but each alert is a natural-language **rule** that a person writes for each sensor. "Always-on" only means pre-loaded rules start running automatically from a YAML file.
  - Alert Verification relies on rule-based Behavior Analytics running upstream.
- **Nearest prior art 1: Search's temporal dedup.** It keeps a sliding window of recent embeddings and stores only vectors that are "novel or transitional". The purpose is storage and recall reduction for search. It is short-horizon (about 60 vectors), alerts no one, scores nothing and verifies nothing, and it is lossy by design.
- **Nearest prior art 2: `Cosmos-Embed1-448p-anomaly-detection`.** NVIDIA ships an anomaly-tuned embedder but only uses it to match text queries for retrieval.
- **No scheduled or unsolicited digest exists.** "Shift summaries and daily activity reports" appear as Video Summarization *use cases*, but every summary or report is requested through chat or a skill and needs a time range plus a scenario and events list.

**Suggested phrasing:** "VSS answers questions you already know to ask: rules, searches, summaries on request. UNWATCHED handles the ones you don't. It learns what each camera normally sees and pages you only about deviations, and the archive sends you a briefing without being asked. NVIDIA's own anomaly-tuned Cosmos-Embed1 is used for search in VSS. We use it to model what normal looks like." Present it as a step that runs before Real-Time Alerts and Alert Verification, not as a replacement. Also say plainly that we drew on VSS temporal dedup and pushed it further: a long-horizon, per-camera baseline instead of a 60-vector window, plus a verifier and a digest.

## 3. VAST
*Sources: vast-enable-dataengine.md, vast-ai-os.md, vast-city-thinks-discussion.md, ../docs/research.md*

- **Enabling DataEngine on a tenant:** the scrape contains only the community post stub. The steps themselves are behind a KB link: `kb.vastdata.com/documentation/docs/enabling-data-engine-on-a-vast-cluster-tenant`. **No exact steps were captured, so scrape that KB page or ask VAST staff first thing.** Related: VAST 5.5 adds "Native Kubernetes", a managed compute layer for DataEngine functions. From research.md: the `vastde` CLI covers functions, pipelines, triggers, topics, compute-clusters, logs and traces, and `vastde doc` dumps every flag. Functions are chained by S3 triggers.
- **AI OS page:**
  - Pipeline: DataStore → DataBase (vectors stored next to tables) → **DataEngine** ("python functions and a built-in Kafka-compatible message bus, triggering agents the moment data changes") → DataSpace (global namespace).
  - Claims: 2M events/s ingest, 20x faster analytics than Iceberg, 1 GB/s per GPU.
  - Protocols: NFS/SMB/S3/SQL/Kafka. It also mentions MCP.
  - Use their words in the pitch: "a passive store into an active platform".
- **City-Thinks discussion:** a stub that links to the blog `vastdata.com/blog/vast-nvidia-cosmos-reason-smart-cities`. Related threads include a "Building Real-Time Video Agents with VAST Data Engine" workshop and the `vast-data/cosmos-labs` GitHub repo. From research.md, the blog's pattern is DB-row trigger → Cosmos Reason2 CoT → JSON `{event, severity, recommended_agent}`.

## 4. Other sponsors
- **CoreWeave ARIA** *(coreweave-aria.md)*: an "AI Research and Iteration Agent" built into the **CoreWeave Forge** dashboard (W&B). It analyzes experiments, proposes and launches the next run as an Automation, drafts PRs, renders charts in chat, and keeps project-scoped memory. It targets training and eval loops, not video inference. **Hackathon use:** only if we have a Forge/W&B account. The most it could do is analyze our Weave eval runs ("propose a better suppression threshold"). Treat it as optional flair.
- **W&B Weave** *(wandb-weave.md, marketing page only)*: tracing with sessions, turns and tools as first-class objects; an imperative eval API; Guardrails scorers; leaderboards; signals that **route alerts to Slack and webhooks**; an MCP server for Claude Code. **API [not in scrape]:** `weave.init("unwatched")`; decorate with `@weave.op`; `result, call = fn.call(...)` returns the call; `call.feedback.add_reaction("👍")` / `call.feedback.add("note", {...})`; `weave.Evaluation(dataset=rows, scorers=[fn]).evaluate(model)` (async).
- **YOLO11** *(yolo11-docs.md)*: AGPL-3.0. YOLO26 now exists. Tasks: detect, seg, cls, pose, obb.

  | Model | mAP50-95 | CPU ONNX (ms) | T4 TRT10 (ms) | Params (M) |
  |---|---|---|---|---|
  | n | 39.5 | 56.1 | 1.5 | 2.6 |
  | s | 47.0 | 90.0 | 2.5 | 9.4 |
  | m | 51.5 | 183.2 | 4.7 | 20.1 |
  | l | 53.4 | 238.6 | 6.2 | 25.3 |
  | x | 54.7 | 462.8 | 11.3 | 56.9 |

  Usage: `YOLO("yolo11n.pt")(src)`. Tracking **[not in scrape]**: `model.track(src, persist=True, tracker="bytetrack.yaml")` (BoT-SORT is the default).
- **Cosmos** *(nvidia-cosmos.md)*: the page now covers only **Cosmos 3**, an omni-model (Mixture-of-Transformers covering text, image, video, sound and action) that serves as a VLM, a world simulator, a policy backbone and a synthetic-data generator. License is OpenMDW 1.1. Models are on HF `nvidia/cosmos3` and build.nvidia.com. Tools: Cosmos Curator and Cosmos Evaluator. **The page never mentions Reason2 or Embed1.** Reason2-8B is still a NIM (VSS Base profile default) and Embed1-448p is on HF.

## 5. Gotchas for build day
1. **The default VLM is now Cosmos Reason 3 Nano, not Reason2.** Decide early which one we demo. Reason2 NIM "can fail to recover after a stop/crash; redeploy the stack" (release notes).
2. Pick **`Cosmos-Embed1-448p-anomaly-detection`** as our embedder. It is the default in VSS, and judges will recognize it.
3. VSS profiles need 2–4 large GPUs. On a 48 GB L40S a shared LLM+VLM may not fit, so use remote endpoints or call the NIMs directly instead of running the full stack.
4. RT Alerts, Alert Verification and Summarization process **1 stream by default**. Our 5 cameras should go through our own DataEngine path, not through VSS.
5. Embedding a newly added RTSP stream is async, so results lag. ES indices expire after **48 h**.
6. The Alert Verification VLM timeout is **5 s**. Remote VLM calls need more, and our Reason2 verifier needs its own timeout and retry.
7. The Alert Bridge parser only accepts raw `Yes/No`. If we reuse it, force a terse output format.
8. In Summarization, the caption prompt is overwritten by the last session. Run one agent per backend.
9. `mdx-vlm-incidents-1970-01-01` collects spurious records from captions that contain "yes" or "true". Filter them out or keep our own VastDB table.
10. Use `/v1/generate_captions`, not `_alerts`. Repeat calls start duplicate jobs, and duplicate stream IDs return 409.
11. `file://` URLs need `FILE_URL_ALLOWED_DIRS`. URL downloads are capped at 8 GB.
12. **The DataEngine tenant enablement steps are not captured.** Get the KB page or ask VAST staff at check-in.
13. YOLO11 is AGPL. Fine for a hackathon, but mention it if asked about commercial use.
