# 02 — Trending Open-Source: Video Understanding / Video Agents (sweep as of 2026-10-02)

Scope: OSS projects around video RAG/agents, real-time CV + VLM, video anomaly detection (VAD), and home/security NVRs with AI, judged against **UNWATCHED** (learned per-camera normal → Cosmos verify gate → suppression counter → push digest, on VAST DataEngine).

Method: 33 Firecrawl searches + 43 page scrapes (raw captures in `.firecrawl/trend-oss-*`). Stars, license, last push and latest release come from the GitHub API on 2026-10-02 (`.firecrawl/trend-oss-gh-stats.tsv`). "Push" is the last commit date.

---

## TL;DR

1. **No public project ships our full loop.** That loop is a learned per-camera normal over stored footage, a VLM verify gate that suppresses most outliers, a counted and measured suppression log, and an unprompted digest. Two projects have most of the pieces:
   - **Qdrant `video-anomaly-edge`** (Mar 2026): kNN distance from a normal baseline, then VSS/VLM incident reports.
   - **Frigate 0.17/0.18**: per-camera text "normal activity" prompt, threat levels 0–2, review-report API, and a new VLM monitoring loop.
2. **The video-agent repos going viral are pull-based**: "let my coding agent watch a video" (`bradautomates/claude-video`, about 17.9k★ in 5 months; `claude-real-video`, 2.2k★ and 167 HN points). That is the opposite of UNWATCHED's push and triage model, so it strengthens our framing. Pitch line: "everyone is teaching agents to watch video on request; nobody is watching the video nobody asked about."
3. **No video-understanding repo is on GitHub's monthly Python trending list** (checked 2026-10-02). Coding agents, skills and memory dominate it. Activity in video OSS is steady (Frigate, supervision, VSS and Pixeltable all committed in the last 48h), but it is not breaking out.
4. **Academic work is converging on "model the normal side"**: NOVA (arXiv, Sep 2026) builds a per-video "Visual Normality Anchor", and MoniTor uses a memory scoring queue. This is the research version of our per-camera centroid. Cite it as validation, not as competition.

---

## Ranked table (ranked by relevance to UNWATCHED, not by stars)

| # | Project | ★ | Push / latest release | License | What it does (one line) | Relevance to UNWATCHED |
|---|---|---|---|---|---|---|
| 1 | [qdrant/video-anomaly-edge](https://github.com/qdrant/video-anomaly-edge) | 15 | 2026-09-02 / — (created Mar 2026) | none listed | kNN distance of VideoMAE/Marengo clip embeddings from a "normal" baseline in Qdrant Edge, escalating about 10% of clips to cloud VSS for VLM captions and incident reports. UCF-Crime: 94% recall, 0.97 AUC. | **Closest prior art.** Same "embedding outlier → VLM" shape, but the baseline is built from a dataset, the VLM is an *enricher* rather than a *suppressing gate*, there is no suppression counter or digest, and it is edge-to-cloud rather than archive-in-place. Credit it openly. |
| 2 | [blakeblackshear/frigate](https://github.com/blakeblackshear/frigate) | 36.3k | 2026-10-01 / v0.18.0 (2026-09-12) | MIT | The leading OSS NVR. 0.17 (Feb 2026) added GenAI **review summaries** with structured JSON and threat level 0/1/2, a per-camera `activity_context_prompt`, and **review reports** over a time range. 0.18 added a **Chat agent** with a recap tool, **VLM monitoring** (a loop on a live camera), remote embeddings, Motion Search and Debug Replay. | **Biggest UX competitor for the digest and verify half.** But "normal" is a *hand-written text prompt*, triggers are *object detections* (person/car), and reports are *on request*. There is no learned normal and no measured suppression. Steal its schema (see below). |
| 3 | [NVIDIA-AI-Blueprints/video-search-and-summarization](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization) (VSS) | 1.9k | 2026-10-02 / v3.2.1 (2026-07-23) | NVIDIA (NOASSERTION) | Reference video-agent stack with five workflows: Q&A/report, **Alert Verification** (CV rule → VLM verify), **Real-Time Alerts** (prompted VLM on sampled frames), Video Search (embeddings, alpha), and Long Video Summarization. Ships agent skills for Claude Code and NemoClaw. | Our substrate. RT-Alerts detects what *you prompt for*, and Alert Verification verifies *rules you wrote*. Neither learns normal. UNWATCHED fills the slot before alert verification ("events nobody wrote a rule for"). |
| 4 | [NVIDIA/context-aware-rag](https://github.com/NVIDIA/context-aware-rag) | 90 | 2026-10-01 | Apache-2.0 | The CA-RAG library behind VSS: knowledge-graph ingestion and retrieval over dense captions. | Optional for digest Q&A. Not on the critical path. |
| 5 | [valentinfrlch/ha-llmvision](https://github.com/valentinfrlch/ha-llmvision) | 1.5k | 2026-09-17 / v1.7.2 | Apache-2.0 | Home Assistant integration: multimodal LLM descriptions of camera/Frigate events, an event **timeline**, and memory of people, pets and objects. | Shows demand for timeline and digest. It is per-event captioning with no novelty scoring. |
| 6 | [koush/scrypted](https://github.com/koush/scrypted) (NVR AI Summaries) | 6.0k | 2026-09-28 / v0.147.0 | NOASSERTION | Scrypted NVR **AI Summaries**: an AI title and summary per detection burst, push notification with a **thumbnail montage**, and **"Stories"** cards that jump to the timeline. | Best push-notification UX reference. Triggered by detections, no learned normal. |
| 7 | [SharpAI/DeepCamera](https://github.com/SharpAI/DeepCamera) (+ Aegis app) | 3.1k | 2026-09-17 / v2026.3 | MIT | "AI camera skills" platform: local VLMs (Qwen, SmolVLM…), YOLO26, ReID, SKILL.md plugins, agent chat, Telegram/Discord/Slack alerts, **HomeSec-Bench** (143-test LLM/VLM security eval), depth-map privacy transform. | Agentic "security camera agent" positioning overlaps the vibe, but it is detect-then-describe with no learned per-camera normal. HomeSec-Bench and the depth-privacy idea are worth citing. |
| 8 | [roboflow/supervision](https://github.com/roboflow/supervision) | 51.1k | 2026-10-01 / 0.30.6 | MIT | CV utilities: PolygonZone, LineZone, heatmaps, annotators, smoothing. | Cheap structured features (zone dwell, line crossings) to add to the embedding score if time allows. |
| 9 | [roboflow/trackers](https://github.com/roboflow/trackers) | 3.9k | 2026-10-01 / 2.6.1 | Apache-2.0 | Clean-room SORT, ByteTrack, OC-SORT, BoT-SORT and McByte, with camera-motion compensation. | Track IDs would allow "dwell longer than usual" outliers. Stretch only. |
| 10 | [roboflow/rf-detr](https://github.com/roboflow/rf-detr) | 9.7k | 2026-10-01 / 1.11.1 | Apache-2.0 | Real-time DETR detection and segmentation, SOTA on COCO. | Not needed: our stage-1 is embeddings, not detection. |
| 11 | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | 62.2k | 2026-10-01 / v8.4.171 | **AGPL-3.0** | YOLO26/YOLO27 detection, segmentation and pose. | Avoid. AGPL, and detection-first is exactly the paradigm we are not using. |
| 12 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | 8.2k | 2026-10-02 / v0.6.9 | Apache-2.0 | Real-time voice and vision agents over WebRTC: YOLO/Roboflow/Moondream processors feeding Gemini Live or OpenAI realtime. Examples include a golf coach and cricket DRS. | The trendiest "real-time video agent" framework. Live-interaction focus, not archive triage. |
| 13 | [livekit/agents](https://github.com/livekit/agents) | 14.4k | 2026-10-01 / 1.8.4 | Apache-2.0 | Realtime voice and video agent framework with vision input ([docs](https://docs.livekit.io/agents/multimodality/vision/)). | Not relevant beyond the "live" theme. |
| 14 | [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) | 16.1k | 2026-10-02 / v1.12.0 | BSD-2 | Voice and multimodal agent pipelines, including a [Moondream vision example](https://github.com/pipecat-ai/pipecat/blob/main/examples/vision/vision-moondream.py). | Same as LiveKit. |
| 15 | [HKUDS/VideoRAG](https://github.com/HKUDS/VideoRAG) (+ Vimo desktop) | 3.4k | 2026-03-18 | NOASSERTION | Graph and multimodal RAG over hundreds of hours of video (KDD'26). Chat with your videos. | Pull-based Q&A over archives. Contrast slide. |
| 16 | [HKUDS/VideoAgent](https://github.com/HKUDS/VideoAgent) | 1.9k | 2026-07-22 | MIT | All-in-one agent for video understanding, editing and remaking (EMNLP'26). | Not relevant (creative editing). |
| 17 | [video-db/Director](https://github.com/video-db/Director) | 1.5k | 2026-01-23 | MIT | "ChatGPT for videos": 20+ prebuilt agents for search, clip, summarize and compile on the VideoDB cloud. | Pull-based, and less active since Jan 2026. |
| 18 | [microsoft/DeepVideoDiscovery](https://github.com/microsoft/DeepVideoDiscovery) | 422 | 2025-11-03 | MIT | Deep-research-style agentic search with tools over long videos. | Pull-based. Stale. |
| 19 | [om-ai-lab/OmAgent](https://github.com/om-ai-lab/OmAgent) | 2.7k | 2025-03-19 | Apache-2.0 | Multimodal agent framework (complex video understanding). | Stale. |
| 20 | [pixeltable/pixeltable](https://github.com/pixeltable/pixeltable) | 1.6k | 2026-10-02 / v0.7.12 | Apache-2.0 | Multimodal table store with computed columns: frame extraction, `clip()`, VLM UDFs and embeddings in one place. | Conceptual twin of "VastDB holds baseline + verdicts". A good analogy, not a dependency. |
| 21 | [Eventual-Inc/Daft](https://github.com/Eventual-Inc/Daft) | 5.8k | 2026-10-01 | Apache-2.0 | Distributed dataframe engine for multimodal data (video, images). | Batch re-scoring of archives at scale. Not needed for the demo. |
| 22 | [mit-han-lab/streaming-vlm](https://github.com/mit-han-lab/streaming-vlm) | 1.1k | 2025-10-15 | MIT | Real-time VLM over infinite streams with a compact KV cache. | Background research. |
| 23 | [m87-labs/moondream](https://github.com/m87-labs/moondream) | 10.1k | 2026-04-20 | Apache-2.0 | Tiny VLM. Common in webcam and security demos. | Possible cheap pre-verifier. We use Cosmos. |
| 24 | [ngxson/smolvlm-realtime-webcam](https://github.com/ngxson/smolvlm-realtime-webcam) | 5.6k | 2025-05-12 | NOASSERTION | The viral SmolVLM + llama.cpp real-time webcam caption demo. | Showed the "VLM narrates my webcam" appetite in 2025. Now a commodity. |
| 25 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | 5.6k | 2026-10-02 / v0.7.4 | MIT | VLM inference and fine-tuning on Apple Silicon. | Laptop fallback verifier if the venue NIM fails (alongside Gemini). |
| 26 | [huggingface/nanoVLM](https://github.com/huggingface/nanoVLM) | 5.0k | 2025-10-27 | Apache-2.0 | Minimal VLM training repo. | Not relevant. |
| 27 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) / [ollama](https://github.com/ollama/ollama) | 130k / 182k | 2026-10-02 | MIT | Local inference. Frigate 0.18 added a dedicated llama.cpp GenAI provider. | Offline fallback only. |
| 28 | [roflcoopter/viseron](https://github.com/roflcoopter/viseron) | 3.6k | 2026-10-01 / v3.7.0 | MIT | Local-only NVR with object, motion and face detection. | No GenAI-summary angle found. |
| 29 | [ispysoftware/iSpy](https://github.com/ispysoftware/iSpy) / Agent DVR | 1.6k | 2026-02-13 | NOASSERTION | Agent DVR's "Ask AI" uses OpenAI, Claude, Gemini or local LLMs ([docs](https://www.ispyconnect.com/docs/agent/ai-config)). | Per-event description, no learned normal. |
| 30 | [open-nvr/open-nvr](https://github.com/open-nvr/open-nvr) | 141 | 2026-09-30 | **AGPL-3.0** | New (Mar 2026) self-hosted NVR with an "any AI model" adapter and apps. | Emerging. Same detect-then-act paradigm. |
| 31 | [cosmo-wander-ai/cosmo-edge](https://github.com/cosmo-wander-ai/cosmo-edge) | 1.2k | 2026-09-30 / v1.1.0 | Apache-2.0 (core) | C++ edge engine (Sophon, Rockchip, x86) for video analytics and on-device VLM with alarms. Created Jun 2026. | A fast riser in the video-analytics topic. Edge-side, not archive-side. |
| 32 | [machinefi/trio-retina](https://github.com/machinefi/trio-retina) | 189 | 2026-07-21 | Apache-2.0 | "OpenTelemetry for perception": YOLO, VLM or DINO output becomes events (`zone.enter`, `dwell`, `line.cross`) plus a latent `vec` on the same record. | Its schema idea (event plus embedding on one row) maps directly onto our VastDB verdict row. |
| 33 | [scality/artesca-vss-console](https://github.com/scality/artesca-vss-console) | 0 | 2026-10-01 (created Aug 2026) | Apache-2.0 | Scality's operator console for NVIDIA VSS on its ARTESCA object store: cameras, alert scenarios, VLM prompt tuning, incidents. | **Competitive intel for VAST judges.** A storage rival is already wrapping VSS. Our answer is that DataEngine runs the logic *inside* the data platform rather than as a console beside it. |
| 34 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | 17.9k | 2026-09-25 (created Apr 2026) | MIT | `/watch` skill: a URL or file becomes timestamped frames and a transcript for Claude Code or Codex. | **The viral video-agent repo of 2026.** Pull-based "watch this for me". Use it as the contrast. |
| 35 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | 2.2k | 2026-10-01 (created Jun 2026) | MIT | ffmpeg scene detection plus pixel-diff dedup, so any LLM gets scene-aware frames ([HN, 167 pts](https://news.ycombinator.com/item?id=48766005)). | Its frame-dedup trick is worth stealing for verify-frame selection. |
| 36 | [IliasHad/edit-mind](https://github.com/IliasHad/edit-mind) | 1.8k | 2026-06-30 | NOASSERTION | Local indexing of 669 GB of GoPro footage (Whisper, 1 fps scene captions, faces, three vector collections) ([blog](https://iliashaddad.com/blog/i-indexed-669-gb-of-my-gopro-videos-using-my-m1-max-computer), [HN](https://news.ycombinator.com/item?id=48528029)). | Shows "my archive is unwatched" is a felt pain, but its answer is search, not triage. |
| — | **VAD research code**: [LAVAD](https://github.com/lucazanella/lavad) (151★, CVPR'24, stale), [VERA](https://github.com/vera-framework/VERA) (87★, 2026-03), [Holmes-VAD](https://github.com/pipixin321/HolmesVAD) (157★, MIT), [AnomalyRuler](https://github.com/Yuchen413/AnomalyRuler) (107★, MIT), [VADTree](https://github.com/wenlongli10/VADTree) (20★), [PANDA](https://github.com/showlab/PANDA) (34★, NeurIPS'25), [MoniTor](https://github.com/YsTvT/MoniTor) (30★), NOVA ([arXiv 2609.06360](https://arxiv.org/html/2609.06360v1), Sep 2026), Cascading multi-agent VAD ([arXiv 2601.06204](https://arxiv.org/html/2601.06204v2)) | low | mostly 2024–25 | mixed | Training-free, LLM/VLM-based VAD on UCF-Crime and XD-Violence benchmarks. | Validation for our approach (training-free, normal-side modeling, verbalized rules), not products. None ships an archive-triage service. |

Two other items:
- [vast-data/mattsvlm](https://github.com/vast-data/mattsvlm) (21★, a VAST video + VLM POC) is worth a glance for VAST-native idioms.
- `github.com/topics/video-understanding` and `/topics/vlm` are polluted with throwaway spam accounts (e.g. `Resolved-ecclesiasticallaw51/...`), so treat topic-page "recently updated" lists as noise.

---

## Steal-worthy patterns for UNWATCHED

1. **Frigate review-summary JSON schema** ([docs](https://docs.frigate.video/configuration/genai/genai_review/)). Make our Cosmos verifier return:
   - `title`
   - `shortSummary` (2 sentences, used verbatim in the Slack push)
   - `scene`
   - `confidence` (0–1)
   - `potential_threat_level` (0/1/2)
   - `other_concerns[]`

   This is a proven, battle-tested notification contract that 36k-star users already understand. Add our own `verdict: surfaced|suppressed` and `baseline_distance` fields.
2. **Per-camera "activity context"**. Frigate lets each camera define normal activity in text. Combine that with our *learned* centroid: the verify prompt gets (a) the distance score, (b) 3 nearest "normal" thumbnails from the baseline, and (c) an optional one-line operator note ("dock doors open 5–7am"). Pitch line: "Frigate makes you write down what normal looks like. UNWATCHED learns it."
3. **Review-report API shape for the digest.** Frigate's `POST /api/review/summarize/start/{ts}/end/{ts}` maps onto our digest function: same inputs, but ours runs unprompted on a DataEngine `Schedule`.
4. **Frame budgeting.** Frigate sends at most 20 frames, extracts at 480p from recordings, and fills about 98% of the context window. Use the same caps for Cosmos verify calls. Pick verify frames with **claude-real-video's scene-detect plus pixel-diff dedup** so the 5 s segment's few frames aren't near-duplicates.
5. **Baseline governance (Qdrant).** Their design adds hygiene we should copy:
   - an immutable baseline shard plus a mutable live shard
   - **quarantine** of escalated clips so they never pollute "normal"
   - explicit poisoning prevention
   - a loose stage-1 threshold ("prefer false positives at stage 1, the verifier is the filter")

   Their `evaluate.py` reports recall, precision, AUC and **escalation rate**. Report the same four numbers in Weave.
6. **Scrypted push UX.** A push notification with an AI title and a **montage of thumbnails**, plus "Stories" cards that deep-link to the timestamp. Our 15:31 digest should be a story card list where each card has a thumbnail strip, a link to the 5 s clip, and the reason it passed verification.
7. **Frigate 0.18 "Motion previews where no object was detected."** This is the same insight as ours (the interesting stuff is what detectors miss). Use it as a talking point: even Frigate now surfaces untracked motion, but leaves the triage to a human.
8. **Frigate Debug Replay** replays recordings through the pipeline as if they were a live camera. This legitimizes our demo approach of uploading 5 s chunks of a stored "live" cam: "replay mode is how the best OSS NVR tests too."
9. **Frigate "cases."** Group surfaced clips into a named case (an incident folder). Cheap to add in VastDB (a `case_id` column) and it makes the digest feel like a product.
10. **Trio Retina's record shape.** An event plus a latent `vec` on the same record. Our VastDB verdict table should keep `embedding`, `distance`, `verdict`, `cosmos_reasoning` and `baseline_snapshot_id` in one row.
11. **Supervision zones and trackers (stretch).** `PolygonZone` time-in-zone plus ByteTrack IDs give a second, interpretable outlier signal ("person dwelled 4× longer than this camera's p95"). Only if the core loop is done.
12. **DeepCamera HomeSec-Bench and depth-map privacy.** Cite the existence of a 143-test security VLM benchmark when explaining our specificity eval. A depth/blur privacy transform on digest thumbnails supports our "no face ID" framing.
13. **NOVA's research findings** ([arXiv](https://arxiv.org/html/2609.06360v1)):
    - Ambiguous verbs ("running", "chasing") in *normal* descriptions blur the decision boundary, so keep them out of the class-specific verify prompts.
    - A "visual normality anchor" built from early frames is the academic version of our centroid. Cite it to show the idea is academically grounded.

---

## Do any of these already do our idea? (honest evidence)

**Our idea, decomposed:**
- (a) a learned per-camera normal from embeddings
- (b) over stored archive segments
- (c) a VLM verify gate that *suppresses* most outliers
- (d) suppression counted and measured (precision/recall)
- (e) an unprompted push digest

| Project | a | b | c | d | e | Verdict |
|---|---|---|---|---|---|---|
| Qdrant video-anomaly-edge | ◐ kNN baseline of normal clips (built from UCF-Crime normals; the tutorial discusses drift and governance, but the baseline is not per camera by default) | ◐ clips, edge-first | ✗ VLM *enriches* incidents; scoring is an edge+cloud ensemble | ◐ recall, precision, AUC and escalation rate offline; no live suppression log | ✗ dashboard, no digest | **Closest. Shares (a)+(c-lite).** 15★, single-commit demo repo from Mar 2026. Credit it on stage. |
| Frigate 0.17/0.18 | ✗ normal is a hand-written `activity_context_prompt` | ✓ recordings | ◐ GenAI rates threat level 0–2; non-suspicious items stay in review (soft suppression), triggered only by object detections | ✗ no measured suppression | ◐ on-demand report API / HA automation can schedule it; 0.18 chat "recap" tool | **Strongest UX overlap on (c)+(e). No learned normal.** |
| NVIDIA VSS 3.2.1 | ✗ | ✓ | ✓ Alert Verification verifies *rule-generated* alerts | ✗ | ◐ report generation | Verify gate exists, but downstream of rules. We sit upstream. |
| Scrypted AI Summaries / LLM Vision / Agent DVR / DeepCamera | ✗ | ✓ | ✗ (describe, don't gate) | ✗ | ◐ push summaries, timeline, Stories | Per-event captioning products. |
| NOVA / MoniTor / LAVAD / VERA (research) | ◐ per-video normal anchor (NOVA), memory queue (MoniTor) | benchmark videos | ✗ | ✓ AUC on benchmarks | ✗ | Academic only, no service, mostly no maintained code. |
| claude-video / claude-real-video / VideoRAG / Director / DVD / edit-mind | ✗ | ✓ | ✗ | ✗ | ✗ (pull) | Opposite paradigm: ask, then watch. |

**Conclusion:** no OSS project we found does all of (a)–(e). The two honest caveats to say out loud:
- Qdrant/Twelve Labs already published "embedding outlier → VLM" (Mar 2026).
- Frigate already ships structured VLM review summaries with threat levels and time-range reports, and in 0.18 a VLM monitoring loop and chat recap.

Our defensible claim (matches FINAL-IDEA corrections) is the **combination**: a learned per-camera normal plus a Cosmos *gate* (not just captions) plus a measured suppression counter plus an unprompted digest, running inside VAST DataEngine on stored archives. Do **not** claim "first anomaly-on-embeddings" or "first AI camera digest."

**Risk to watch:** Frigate's monthly release pace (0.17 in Feb, 0.18 in Sep, with a chat agent and VLM monitoring) means home users may get a "VLM-gated recap" soon. Position UNWATCHED at enterprise archive scale (10k cameras, stored footage, cost per camera-hour), not home NVR.

---

## Sources (primary)
- Frigate GenAI review docs: https://docs.frigate.video/configuration/genai/genai_review/ · object descriptions: https://docs.frigate.video/configuration/genai/genai_objects/ · 0.18.0 release notes: https://github.com/blakeblackshear/frigate/releases/tag/v0.18.0 · 0.17 discussion: https://github.com/blakeblackshear/frigate/discussions/22137
- Qdrant VAD: https://github.com/qdrant/video-anomaly-edge · https://qdrant.tech/documentation/tutorials-build-essentials/video-anomaly-edge-part-1/ · https://qdrant.tech/blog/video-anomaly-detection-edge-to-cloud/
- VSS: https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization · RT alert workflow: https://docs.nvidia.com/vss/latest/agent-workflow-rt-alert.html
- Scrypted AI Summaries: https://docs.scrypted.app/scrypted-nvr/ai-summaries.html
- LLM Vision: https://github.com/valentinfrlch/ha-llmvision
- DeepCamera: https://github.com/SharpAI/DeepCamera
- Vision Agents: https://github.com/getstream/Vision-Agents
- Trackers: https://github.com/roboflow/trackers · Supervision zones: https://supervision.roboflow.com/latest/detection/tools/polygon_zone/
- NOVA: https://arxiv.org/html/2609.06360v1 · MoniTor: https://arxiv.org/html/2510.21449v1 · Cascading VAD: https://arxiv.org/html/2601.06204v2 · LAVAD: https://lucazanella.github.io/lavad/ · VERA: https://vera-framework.github.io/
- Viral pull-based agents: https://github.com/bradautomates/claude-video · https://github.com/HUANGCHIHHUNGLeo/claude-real-video · https://news.ycombinator.com/item?id=48766005 · https://iliashaddad.com/blog/i-indexed-669-gb-of-my-gopro-videos-using-my-m1-max-computer
- GitHub trending (monthly, Python): https://github.com/trending/python?since=monthly · topics: /topics/video-understanding, /topics/video-analytics, /topics/vlm, /topics/video-rag
- Scality ARTESCA VSS console: https://github.com/scality/artesca-vss-console
