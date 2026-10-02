# VAST Builders Challenge 2026 — Research Brief

Raw scrapes: `.firecrawl/` (initial + event-portal scrapes) and `docs/sources/` (deep-research scrapes), all committed. Compiled 2026-09-28, corrected 2026-10-02.

> **Official portal details (deadline, submission requirements, prerequisites) are in [EVENT-DETAILS.md](EVENT-DETAILS.md) and supersede anything below.** Key corrections: submission deadline **4:30 PM** (not 5:00); submit a **public GitHub repo + demo video link**; join the VAST Cosmos Community for build-env access (first 100 arrivals only); 2nd prize = Hugging Face Microduck.

## Event
- Official name: **Real-Time Video Agents Hack** (produced by tokens&, hosted with VAST Data + NVIDIA, SpaceXAI, CoreWeave, W&B; Cursor supplies credits).
- Theme: "Spend the day building agents to unlock the value of video. Because video is hard to search and analyze, most of it stays in storage, unwatched and underused."
- Dates: SF Fri Oct 2 (reg closed Sep 29), NYC Fri Oct 9 (reg closes Oct 2), London Sat Oct 17 (reg closes Oct 9). Luma: luma.com/vastsf, /vastnyc, /vastlondon.
- Schedule (SF, per tokens& portal): 9:30 doors + keynotes, **10:00 build → 16:30 submission deadline**, 17:00 demos, 19:00 awards (~6.5h build). NYC: 9:30 build → 16:30 deadline.
- Teams up to 4, prioritized. Register with the same email as your Cursor credits. 18+, physical photo ID. SF venue is an Amazon building.
- Prizes: 1st = **NVIDIA DGX Spark**; 2nd = **Hugging Face Microduck**; credits + gift cards split among team members.
- Judging: **creativity, technical implementation, real-world impact**.
- Judges:
  - SF: Hassan Moustafa (NVIDIA TME Multimodal AI), Adam Ryason PhD (NVIDIA Product), Ram Bansal (VAST Sr Dev Advocate), Brian Verkley (VAST Dir. AI Data Platform), Anushrav Vatsa (CoreWeave SA, Physical AI Lead), Arnav Verma (SpaceXAI Field Eng).
  - NYC: Diego Garzon (NVIDIA SA AI/AV Simulation), Ravi Garg (NVIDIA SA), Ram B., Brian Verkley, Prashanth Nalubandhu (CoreWeave Staff AI SA), Brandon Kates (CoreWeave Founding FDE), Vera A. (W&B Sr SA).
  - London: Abubakr Karali (NVIDIA), Ram B., Brian Verkley, Junaid Butt (W&B).

## Provided Builder Stack (from Luma)
- Video understanding: **NVIDIA Cosmos** (Cosmos-Reason2, 2B/8B, 256K ctx, CoT `<think>`, 2D grounding).
- Semantic search over hours of footage (natural language).
- Object detection + tracking: **YOLO** (YOLO11 in the blueprint).
- General LLMs via **W&B Inference** (OpenAI-compatible `https://api.inference.wandb.ai/v1`; Nemotron 3.5 Lightning, Nemotron 3 Ultra, DeepSeek V4, Qwen3.8, Kimi K2.7, GLM-5.3, Gemma 4, GPT-OSS, MiniMax M3, Llama 3.x).
- VAST AI OS = ingestion + data layer; models on CoreWeave GPUs; build with Cursor. Sample videos supplied; bring your own allowed.
- Blog also names NVIDIA Metropolis VSS Blueprint, Nemotron, NemoClaw (NemoClaw = sandbox runtime for coding agents, *not* a video tool).

## The Starter Kit (what every team gets) — `github.com/vast-data/vss-blueprint`
Ingest pipeline = serverless DataEngine functions chained by S3 triggers:
```
Upload → vss-chunks bucket
video-segmenter (~5s clips) → video-detector (YOLO11: classes, counts, bbox sidecars)
→ video-reasoner (Cosmos-Reason2 caption ≤1024) → video-embedder (text + visual vectors, Cosmos-Embed1)
→ vastdb-writer (segment rows in VastDB) → prompt-suggester (optional search chips)
```
- Retrieval: Angular UI + Python backend; hybrid vector search → clip cards → Reason2 synthesis.
- Agent APIs already exist: `/api/v1/tools/*`, `POST /api/v1/agent/ask`, `/search-and-answer`.
- VAST smart-city blog already shows: DB-row trigger → Cosmos Reason2 CoT → JSON `{event, severity, recommended_agent}` → route to downstream agent.
- **Implication: "search/summarize your footage" and "detect event → route to agent" are the baseline. Re-demoing them loses.**

## VAST APIs worth flexing
- `vastdb` SDK: PyArrow insert/select, Ibis predicate pushdown, parallel select across CNodes, Parquet import from S3, projections, **snapshots (time travel)**, VAST Catalog as a table (filesystem-as-DB), ADBC, DuckDB.
- `vastde` CLI (DataEngine): functions, pipelines, triggers, topics (Kafka), compute-clusters, logs, metrics, **traces**. `vastde doc` dumps all flags.
- AI OS 5.5: NFSv4 file triggers, Kafka mTLS, DataEngine Runtime SDK (S3/VASTDB/Kafka/Trino/Spark clients) — unverified.
- Other org repos: `vast-vector-store`, `vast-admin-mcp`, `dataengine-pipelines`, `vast-daft`, `Orbit` (sklearn-like on VastDB).
- VAST Event Broker (Kafka-compatible, 136M msg/s claims).

## NVIDIA VSS Blueprint (3.3)
- Real-time video intelligence → message broker (Kafka/Redis) → analytics (trajectories, incidents, verified alerts) → agentic layer incl. **MCP**.
- CA-RAG: vector + **graph DB** (knowledge graph from captions), NeMo rerank.
- Named workflows: Alert Verification (detector → VLM verify), Real-Time Alerts, Video Search, Long Video Summarization.
- Cosmos Reason2 NIM free tier: 40 RPM.

## What won comparable events (Cosmos Cookoff, 1,600 participants)
- "See How It Thinks" (Doosan): visible Cosmos reasoning driving a palletizing robot.
- Team Jarvis: autonomous drone; **YOLO as cheap perception gate → Cosmos only for reasoning** (latency fix).
- CoreWeave/W&B hacks reward visible agent loops (reason → act → catch mistakes → improve) + Weave traces.

## Whitespace (not in the blueprints)
1. Real multi-step agent on top of VSS tool APIs (plan → tool → replan → act in the world).
2. Graph / entity layer over VastDB rows (same person/vehicle across clips & cameras).
3. Cross-camera / multi-stream correlation into one narrative.
4. Live-stream (RTSP/webcam) → DataEngine continuous ingest.
5. Alert verification / false-positive reduction loop.
6. VastDB snapshots → "what did the system know at time T" forensic replay.
7. Analyst SQL over video tables (ADBC/DuckDB/Trino).
8. Kafka / NFSv4 triggers (NVR exports without S3 upload).
9. MCP client over VSS/VAST data.
10. W&B Weave tracing/evals of the video agent's reasoning.
11. **Proactive triage of unwatched archives** (push, not pull) — the literal theme, unsolved.
12. Frame + bounding-box-level citations in answers.

## Blocking unknowns (verify on-site)
- Which blueprint version is pre-provisioned; exact `vastde` create flags; ANN backend (`vast-vector-store` vs float columns); Cosmos endpoint quota; whether SpaceXAI/Grok API is offered (not in stack — don't depend on it).
