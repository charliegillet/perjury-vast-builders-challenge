# Deep Research: VAST Builders Challenge SF (tokensand.com/vastsf) and the UNWATCHED pitch

Compiled 2026-10-02, the morning of the SF event. Exhaustive tier: 5 parallel research passes, about 80 searches, and roughly 110 new pages scraped on top of the 58 from the first pass. The four detailed reports are:
- [EVENT-DETAILS.md](EVENT-DETAILS.md): the official portal (deadline, submission, prerequisites)
- [deep-research/01-technical.md](deep-research/01-technical.md): build-day cheat sheet with code
- [deep-research/02-competitive.md](deep-research/02-competitive.md): competitors, prior art, contrarian case
- [deep-research/03-judges-market.md](deep-research/03-judges-market.md): judges, organizer, market numbers
- [sponsor-docs-digest.md](sponsor-docs-digest.md): NVIDIA VSS workflows, VAST, CoreWeave ARIA, Weave, YOLO11

Raw captures are in `.firecrawl/` (first pass and portal) and `docs/sources/` (`dr-tech-*`, `dr-comp-*`, `dr-judge-*`).

## Executive Summary

The tokens& portal is the source of truth for SF today, and it changes the logistics.
- **Deadline:** submissions close at **4:30 PM PT**. Demos at 5:00 come after that.
- **What to submit:** a **public GitHub repo** plus a **shareable demo video**, a description of what was built and the tools used, and team contacts.
- **Build environment:** access goes through the VAST Cosmos Community, and only to the **first 100 attendees** who arrive.
- **Organizer guidance:** pick a narrow, specific use case. Search quality depends on the Cosmos prompt used at ingest, and teams can re-ingest with a different prompt on build day.

UNWATCHED is still the right idea, but its "nobody has done this" framing is false and would be caught on stage.
- **Products:** Avigilon (Motorola) has shipped rule-free, learned-per-scene "unusual activity" detection since 2018. Lumana and Coram claim that each camera learns its own normal. Google Home and Svid send unprompted daily digests.
- **Closest match:** an open-source Qdrant + Twelve Labs VSS demo from March 2026 scores clips by distance from a normal baseline and sends outliers to a VLM.
- **What's defensible:** the **combination**. That is a per-camera learned normal, plus Cosmos-Reason2 checking every outlier, plus a *measured* count of what was suppressed, plus a push digest over stored archives, all running inside VAST DataEngine.
- **The pitch should lead with the known failure.** In a 2017 IPVM thread, the site's founder said learned-normal systems flag about 100 unusual things for every real one. UNWATCHED adds the verify step that fixes that ratio.

On the technical side, the plan is buildable, with six corrections:
1. DataEngine has `Element` (S3) triggers and `Schedule` (Quartz cron) triggers, but no Kafka or database-row triggers.
2. VastDB has native vector search, but only through SQL over the ADBC driver (`array_cosine_distance`).
3. The starter blueprint already runs Cosmos-Reason2 on **every** 5-second segment.
4. Embeddings have 256 dimensions, and failed ones are stored as all zeros.
5. NVIDIA's hosted Reason2 endpoint has been returning 404, so use the venue's own NIM.
6. VSS 3.2.1+ defaults to Cosmos Reason 3 Nano.

The judge mix sharpens the pitch. The two NVIDIA judges *own* the features next to ours: Hassan Moustafa wrote the Sep 29 VSS 3.3 alert-verification blog, and Adam Ryason is the VSS Blueprint product manager. Pitch UNWATCHED as the layer for footage nobody wrote alerts for, not as something VSS is missing.

## Key Findings

1. **The deadline is 4:30 PM PT, and the submission needs a public repo plus a demo video.** Build-env access is limited to the first 100 arrivals and requires the VAST Cosmos Community. Prizes: 1st NVIDIA DGX Spark, 2nd Hugging Face Microduck. [tokensand.com/vastsf](https://tokensand.com/vastsf) (`.firecrawl/tokensand-vastsf.md`)
2. **The organizer says specificity wins.** Their own example is "flag someone missing a hard hat" rather than "watch for safety issues". The Cosmos ingest prompt controls what can be searched. (same source)
3. **Organizer criteria from tokens&'s London event:** idea, technical implementation, sponsor tool use, presentation, and **autonomy** ("acts on real-time data without manual intervention"). VAST's blog lists creativity, technical implementation and real-world impact. (`dr-judge-tokensand-*`, [VAST blog](https://www.vastdata.com/blog/lets-build-introducing-the-vast-builders-challenge))
4. **No VSS 3.2.1–3.3 workflow learns a per-camera baseline or sends an unprompted digest.** Real-Time Alerts are rules written for each sensor, and "shift summaries" are requested in chat. Two close items: Search's "temporal dedup" (about 60 recent embeddings, kept only to save storage), and the default embedder `Cosmos-Embed1-448p-anomaly-detection`, which covers 24 fixed anomaly types and is used only for search. ([docs.nvidia.com/vss/latest](https://docs.nvidia.com/vss/latest/); `sponsor-docs-digest.md`)
5. **Commercial prior art exists:** Avigilon unusual-activity detection (2018, 1–2 week learning period), Lumana's per-camera normal, Spot AI's propose-then-verify, and the Google Home and Svid daily digests. ([theverge.com Gemini for Home](https://www.theverge.com/tech/813523/gemini-for-home-google-nest-camera-hands-on), [support.google.com/googlehome/answer/15542305](https://support.google.com/googlehome/answer/15542305), [svid.ai guide](https://svid.ai/guides/how-to-search-through-hours-of-cctv-footage), [lumana.ai/blog](https://www.lumana.ai/blog); `dr-comp-avigilon-*`)
6. **The closest technical match:** the Qdrant + Twelve Labs "video anomaly detection edge-to-cloud" demo on VSS. It does distance from a normal baseline, sends outliers to a VLM, and guards against the baseline absorbing incidents. ([qdrant.tech blog](https://qdrant.tech/blog/video-anomaly-detection-edge-to-cloud/))
7. **The strongest academic attack:** a June 2026 preprint finds that off-the-shelf embedding distance scores 0.704 AUC on the same scene and 0.499 (chance) on a different one, with about 26–32k false alarms per hour. A frozen VLM asked "is there any anomaly?" scores 53–65 AUC. Reference scores: LAVAD 80.3, Holmes-VAD 84.6, VERA 86.6 (UCF-Crime). AnomalyRuler, which learns rules from normal footage, is our closest academic ancestor. ([arXiv 2404.01014 LAVAD](https://arxiv.org/abs/2404.01014), [arXiv 2406.12235 Holmes-VAD](https://arxiv.org/abs/2406.12235), [arXiv 2407.10299 AnomalyRuler](https://arxiv.org/abs/2407.10299); `dr-comp-auc-not-deployable.md`, `dr-comp-vera-html.md`)
8. **DataEngine triggers:** `Element` (S3 object created, removed or tagged) and `Schedule` (Quartz cron, e.g. `0 0/5 * ? * * *`), created with `vastde triggers create schedule --cron-schedule …`. A trigger must exist before the pipeline that uses it. The cron timezone is undocumented. ([github.com/vast-data/dataengine-cli](https://github.com/vast-data/dataengine-cli/tree/main/docs/references/commands); `01-technical.md`)
9. **Vector search in VastDB:** SQL over ADBC, e.g. `array_cosine_distance(vectors_visual::FLOAT[256], ARRAY[...]::FLOAT[256]) … ORDER BY distance LIMIT k`. The pinned SDK 1.3.2 can't read vector columns; SDK 2.x adds an indexed `table.vector_search()`. ([vss-blueprint](https://github.com/vast-data/vss-blueprint), [vastdb-adbc-driver](https://github.com/vast-data/vastdb-adbc-driver), [vastdb_sdk](https://github.com/vast-data/vastdb_sdk))
10. **Blueprint facts:** 5-second segments, Reason2 captions on every segment (no caption means no row), 256-dimension text and visual embeddings, and failed embeddings stored as zeros. The embedder's output carries the visual vector, YOLO peak counts and `camera_id`, so the scorer can branch off the embedder output. (`01-technical.md`, `dr-tech-*`)
11. **Cosmos-Reason2 requests:** video goes in as base64 mp4 or a frame list. Pass `fps` *or* `num_frames`, never both; asking for more frames than the video has returns 400. Bounding boxes are on a 0–1000 scale. Latency isn't published, so measure it with `SELECT avg(processing_time)` on the segments table. Unverified estimate per 5-second clip: 8B 2–5 s, 2B 1–2 s, plus 5–15 s when it reasons step by step. (`01-technical.md`)
12. **W&B Inference IDs:** `nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B` and `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B` at `https://api.inference.wandb.ai/v1`. Rate limits are per project. Weave feedback: `client.get_call(id).feedback.add_reaction("👍")`. ([docs.wandb.ai/inference](https://docs.wandb.ai/inference), [Weave feedback](https://docs.wandb.ai/weave/guides/tracking/feedback))
13. **Market:**
    - Video surveillance is **$27B in 2025** (Omdia, +4.3%; +12.8% forecast for 2026), or $60–80B+ on broader definitions.
    - Cloud video surveillance services: $5.3B → $5.9B (2026) → $12.0B (2032).
    - **Less than 1%** of recorded footage is watched live (IPVM). NVIDIA counts **2B+ cameras**.
    - Pricing comparisons: AI analytics add-ons $3–15 per camera per month, cloud management $15–30, remote monitoring $30–400+, and a guard's median wage $18.29/hr. That supports **$8 per camera per month**.
    - False alarms: 94–98% of alarm calls police respond to are false (US Justice Department guide; sensor alarms, not video).
    - Retention: California cannabis rules require 90 days of footage (16 CCR §15044(h)). The common claim that PCI requires 90 days of all footage is a myth.
    - Sources: `dr-judge-mkt-*` ([omdia.tech.informa.com](https://omdia.tech.informa.com/), [bls.gov](https://www.bls.gov/), [popcenter.asu.edu](https://popcenter.asu.edu/))
14. **What each judge cares about** (detail in `03-judges-market.md`):
    - **Moustafa:** VLM cost and alert verification (VSS 3.3).
    - **Ryason:** cited, timestamped reports pushed into Slack or Jira.
    - **Verkley:** AgentEngine, audit trails, thumbs-up/down feedback loops.
    - **Bansal:** video search and MCP; rewards using the DataEngine trigger chain.
    - **Vatsa:** how many experiments were actually evaluated; show the eval and a cost meter.
    - **Verma:** Cursor speed and polish.
15. **Likely collisions among about 25 teams:**
    - 2–4 teams building daily summaries on the starter kit's summarize feature.
    - 3–5 teams doing prompt-rule alerts to Slack.
    - **0–2 teams doing embedding-based anomaly scoring (the dangerous one).**
    - PPE and chat-with-footage teams don't overlap with us.
    - Past Cosmos winners rewarded visible reasoning, while prompt-rule webcam watchers and weapon detection are overdone. (`02-competitive.md`, `.firecrawl/cosmos-cookoff-winners.md`)

## Detailed Analysis

**What changes in the plan.** [FINAL-IDEA.md](FINAL-IDEA.md) now carries a corrections banner. In summary:
- **Timing:** freeze at 15:30, record the demo video 15:30–16:10, submit by 16:20. Fire the scheduled digest at 15:31 so it lands in the video.
- **Architecture:** `Element` triggers chain the ingest. The scorer branches off the embedder output, and DataEngine conditional routing (or a poller fallback) reaches the verifier. A `Schedule` trigger fires every minute and posts the digest once at 15:31 PT, with a laptop cron as backup. Live-cam chunks are 5 seconds.
- **Embedder:** test `Cosmos-Embed1-448p-anomaly-detection` against the default for the baseline. NVIDIA judges will recognise their own model being used in a new way.
- **Claims:** "only ~3% of segments get the extra Cosmos verify pass," never "Cosmos only sees 3%."

**Why the combination still wins.** Learned-normal detection failed commercially because it raised too many false alarms (the 2017 IPVM thread). VLM verification is NVIDIA's shipped answer for *rule* alerts, but nobody pairs it with *learned-normal* candidates and publishes the suppression numbers. Measured precision and recall on about 60 hand-labelled clips, shown in Weave, turns "trust us" into evidence. That plays to the CoreWeave and W&B judges and to tokens&'s autonomy criterion.

**Stage wording (use this):**
> "Cameras that learn what's normal aren't new — Avigilon shipped it in 2018. They never took off because for every real event they flagged a hundred harmless ones. UNWATCHED adds the missing step: Cosmos-Reason2 checks every outlier against what that camera normally sees, nobody gets paged until it passes, and we count and measure everything we chose not to show you."

Contrast line for NVIDIA judges: *"VSS answers questions you already know to ask; UNWATCHED handles the ones you don't."* Credit VSS's temporal dedup openly.

## Contrarian Views And Risks

- **"Embedding distance isn't anomaly detection."** The June 2026 preprint gives 0.499 AUC across scenes. *Rebuttal:* a baseline for each camera and time-of-day bucket (the paper's own recommended fix), scoring 5-second segments rather than single frames, and a VLM gate. Show our measured precision and recall instead of arguing.
- **"Cosmos already runs on every segment, so where are the savings?"** True of the blueprint. *Rebuttal:* the expensive part is the verify call, with step-by-step reasoning and bounding-box grounding, and it runs on about 3%. Production could use a cheaper caption, or none.
- **Baseline drift and poisoning** (lighting, crowds, camera shake, an incident being absorbed into "normal"). *Mitigation:* exclude escalated segments from the centroid update, use time-of-day buckets, and treat the first ~200 segments as learn-only.
- **Scale cost.** About 3% escalation means roughly 11–22 Cosmos calls per camera-hour, which a CoreWeave judge may push on at 10,000 cameras. Keep the GPU meter on screen.
- **Privacy and surveillance ethics.** The ACLU names learned-normal behaviour analytics as a chilling-effect risk. *Framing:* private operational spaces (stockrooms, server cages, after-hours docks), no face ID, no "suspicious person" language. ([aclu.org](https://www.aclu.org/news/national-security/video-analytics-brain-behind-eye))
- **Infrastructure risks:**
  - The Reason2 NIM is documented as not recovering after a crash.
  - The hosted endpoint returns 404.
  - Images built on Apple Silicon may be arm64, which DataEngine can't run.
  - The VAST Kafka broker only supports confluent-kafka 2.4–2.8 and caps messages at 126 KB.
  - Build-env seats are limited to the first 100 arrivals.
- **NVIDIA judges own the adjacent product.** If we frame it as competition with VSS we lose; if we frame it as an extension of VSS we win.

## Open Questions (resolve at 10:00 on site)
1. Which VLM does the venue serve, Reason2 8B, 2B or Reason 3 Nano, and what is its p50 latency on a 5-second clip?
2. Does the event cluster support DataEngine conditional routing (documented for 5.5)? If not, use the poller fallback.
3. What timezone do `Schedule` triggers use? Mitigated by firing every minute and gating in code.
4. Which SDK version is installed (1.3.2 vs 2.x `vector_search()`)?
5. What are the exact steps to enable DataEngine on the tenant? The community posts are stubs, so ask VAST staff.
6. Is `Cosmos-Embed1-448p-anomaly-detection` available in the venue stack?
7. Unverified items: Coram's "learns normal" (a press snippet only), Actuate (no evidence found), Verkley's anomaly-detection post and Verma's Cursor post (snippets only).

## Sources
Every claim above cites a file under `.firecrawl/` or `docs/sources/`. The per-angle reports list their full source sets:
- `01-technical.md`: 36 `dr-tech-*` captures, including seven public repos read (vss-blueprint, dataengine-cli, dataengine-pipelines, vastdb_sdk, vastdb-adbc-driver, vast-vector-store, cosmos-reason2) plus 20 doc pages.
- `02-competitive.md`: 39 sources (`dr-comp-*`): Avigilon, Lumana, Spot AI, Verkada, Google Home, Svid, Ambient, Qdrant/Twelve Labs, arXiv (LAVAD, Holmes-VAD, VERA, AnomalyRuler, the 2026 deployability preprint), IPVM, ACLU.
- `03-judges-market.md`: 30 scrapes and 24 searches (`dr-judge-*`): NVIDIA dev blogs (VSS 3.3, VSS enterprise), GTC 2026 announcements, VAST AgentEngine, MCP, FWD and webinars, tokens& home and events, Omdia, MarketsandMarkets, IPVM, BLS, the Justice Department/ASU POP Center false-alarm guide, California cannabis regulations, remote-monitoring cost guides.
- `sponsor-docs-digest.md`: VSS docs (search, real-time alerts, alert verification, video summarization, warehouse agents, release notes), VAST AI OS, CoreWeave ARIA, W&B Weave, YOLO11, NVIDIA Cosmos.
- Event: [tokensand.com/vastsf](https://tokensand.com/vastsf), [tokensand.com/vastnyc](https://tokensand.com/vastnyc), [luma.com/vastsf](https://luma.com/vastsf), [VAST blog post](https://www.vastdata.com/blog/lets-build-introducing-the-vast-builders-challenge), [Discord](https://discord.gg/VyhUqgn6pc).

## Rerun Inputs
workflow: firecrawl-deep-research
topic: VAST Builders Challenge SF (tokensand.com/vastsf) and the UNWATCHED pitch: event rules, build-day technical facts, competitors and prior art, judges and market
depth: exhaustive
output: markdown
