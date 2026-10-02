# 03 — Trending Products, Startups, Launches, Hackathon Winners and Buzz in Fast Video Understanding (as of 2026-10-02)

This doc extends `docs/deep-research/02-competitive.md`. It doesn't repeat what's already there: Avigilon UMD, Lumana VIA-1 basics, Spot AI proposer-verifier, Google Home Brief, Svid, Verkada occlusion, the Qdrant + TwelveLabs VSS anomaly reference, Cosmos Cookoff 1, and the TwelveLabs Denver/LA hackathons. The focus here is **what changed in Jun–Oct 2026** and what that means for UNWATCHED on stage today.

Raw captures are in `.firecrawl/trend-mkt-s*.json` (44 searches) and `.firecrawl/trend-mkt-p*.md` (40 scrapes; Reddit and LinkedIn scrapes were blocked, so those claims rely on search snippets).
Source tags: **[A]** primary (vendor press release or blog, official doc). **[B]** press or secondary. **[C]** snippet, social, or forum only. **UNVERIFIED** means the date, placement, or number was not confirmed on a primary page.

---

## TL;DR

1. **The money and the narrative moved to "video as memory" and "always-on agents."** TwelveLabs ($100M Series B, Jul 1) now pitches "make every second of video addressable … by agents" and calls the archive "machine-readable memory". OpenAI launched **dots** (Sep 29), "always-on agents" that work toward your goals 24/7. NVIDIA rebranded VSS 3.2 around "**always-on video agents that alert, summarize and search**" (Jul 15). Judges have heard *always-on*, *agentic*, *memory*, and *archive* all quarter. UNWATCHED fits that vocabulary natively: storage-triggered, push, learned memory of normal.
2. **"Watch less, reason more" is now the industry consensus, and Google just productized it.** Gemini **agentic video understanding** (Sep 1) lets the model decide what to watch: "up to 88%" fewer tokens and "up to 66%" lower cost. Lumana's stated principle is "**We filter before we spend.**" UNWATCHED's "only ~3% of segments get the expensive verify pass" is the same thesis, done on the archive *at rest* and inside storage. Say it in those words.
3. **Security-video AI is the hottest applied vertical, with fresh rounds.** Coram $35M B (Jun 11), Hakimo $12M A2 (Jul 8), Verkada + NVIDIA investment (Jul 1) plus the Catalyst MCP (Sep 17), Orchestra (100 SF street cams, raising a seed, Jul 2), Conntour $7M seed (Mar), and Ambient doubling new ARR with Pulsar. Almost all of them are **pull** (NL search or "Deep Investigation") or **rule-by-prompt** (NL alert definitions). Lumana remains the only loud "learns normal per camera" voice.
4. **The backlash is a live headline, so lead with privacy design.** Texas froze state funding for Flock cameras (Sep 1). Hackers dumped a Flock camera's data (Wired, ~Sep 18). Indianapolis cops were charged with misuse. Forbes (Jul 22) showed Axon's AI reports "get facts wrong". The "no faces, no identity, events in private operational spaces, auditable suppression ledger" stance now reads as current, not as boilerplate.
5. **Hackathon winners in 2026 look alike:** (a) a *live* demo on real feeds, (b) **provenance and anti-hallucination discipline** ("the extraction refuses to guess", "models never grade", JSONL traces), (c) a named operator and a handoff artifact. **ZooVision** (3rd, TwelveLabs/Neo4j hack, SF, Jul 30) is "overnight … fixed-camera footage in … review-and-handoff workflow for the morning shift". That is UNWATCHED's frame. **"Anomaly Congestion in NYC"** (AI Tinkerers NYC) "learns what each block normally looks like, then flags the cameras that suddenly deviate". Both mean the idea is in the water. The difference has to be *verify + measured suppression + storage-native*.

---

## 1. Launch and funding timeline (Jun–Oct 2026; a few earlier anchors marked)

| Date | Who | What | Relevance to UNWATCHED | Source |
|---|---|---|---|---|
| Mar 16, 2026 (anchor) | **Memories.ai** | Visual-memory layer for wearables and robots; partnered with NVIDIA at GTC using **Cosmos-Reason 2 + Metropolis VSS**; LVMM 2.0 on-device with Qualcomm | Same stack as ours. "Visual memory" is the buzzword | [A/B] techcrunch.com/2026/03/16/memories-ai-is-building-the-visual-memory-layer-for-wearables-and-robotics/ (`p08`) |
| Mar 26, 2026 (anchor) | **Conntour** (YC) | $7M seed (General Catalyst, YC). NL search over live and recorded security video, plus "preset rule" monitoring | Pull + rule-by-prompt. Contrast case | [B] techcrunch.com/2026/03/26/conntour-raises-7m-… (`p42`) |
| Apr 20, 2026 | **TwelveLabs** | NAB: **Pegasus 1.5** (time-based metadata extraction) and **Rodeo**, its first app-layer product (video-editing copilot) | TL is moving up-stack into apps | [A] prweb.com/releases/twelvelabs-unveils-the-next-era-of-video-intelligence-at-nab-show-2026-302746715.html (`p45`) |
| May 15, 2026 | **Gemini Live Agent Challenge** results | 11,878 participants and 1,536 projects. Grand prize: ORION, a voice-directed surgical co-pilot. Live Agent winner: drone-copilot | See §3 | [A] cloud.google.com/blog/…/winners-and-highlights-of-the-gemini-live-agent-challenge (`p15`) |
| Jun 11, 2026 | **Coram AI** | **$35M Series B** (Ansa, Battery; $66M total). "Deep Investigation": NL queries across cameras, badge readers, visitor logs. 1,500+ sites, 4x revenue | Retrofit-on-existing-cameras GTM = our "storage-native, no rip-and-replace" argument | [B] startupfortune.com/coram-ai-raises-35-million-… (`p03`); businessinsider.com/coram-turn-security-cameras-into-ai-detectives-2026-6 |
| Jun 25, 2026 | **Archetype AI** | **Newton Agents**: Rare Event Detection ("from only a handful of examples"), **Anomaly Discovery**, Task Verification (video), SOP generation | Physical-AI "anomaly discovery" language is mainstream in industrial | [A] finance.yahoo.com/…/archetype-ai-launches-newton-agents-… (`p12`) |
| Jul 1, 2026 | **TwelveLabs** | **$100M Series B** (NEA, NAVER, Amazon). "Video Cognition System": understand once, durable memory, "intelligence that compounds" | Their words: "The archive stops being passive storage." That is also VAST's pitch | [A] globenewswire.com/…/3320545/… (`p02`), twelvelabs.io/blog/twelvelabs-series-b-100m (`p31`) |
| Jul 1, 2026 | **Verkada × NVIDIA** | NVIDIA investment plus collaboration: Cosmos WFMs, multimodal embeddings, vector retrieval, "multi-model search agent architecture", reasoning models. 2.4M devices | Biggest camera OEM is now on Cosmos | [A] prnewswire.com/news-releases/verkada-accelerates-physical-ai-with-nvidia-302815190.html (`p05`) |
| Jul 2, 2026 | **Orchestra** | 100+ street cams in SF, 900 more planned. "Search engine for the physical world", "AGI for cities". Raising a seed | The public-space version. Expect privacy questions to be front of mind for judges | [B] businessinsider.com/this-startup-wants-to-make-city-streets-searchable-with-ai-2026-7 (`p06`) |
| Jul 8, 2026 | **Hakimo** | $12M Series A2 (Zigg). AI video monitoring | Remote-guarding category is still raising | [B] axios.com/pro/…/physical-ai-security-hakimo-software (`p04`) |
| Jul 9–11, 2026 | **OpenAI** | GPT-5.6 Sol/Terra/Luna and GPT-Live (full-duplex voice). HN users call Sol "the best video captioning model in the world by a mile", the first to caption sub-second motion | Model quality for short clips jumped. Hallucinated actions remain the cited failure | [C] news.ycombinator.com/item?id=49329575 (`p36`); patmcguinness.substack.com/p/ai-week-in-review-260711 |
| Jul 12, 2026 | **Frigate 0.18 beta** (OSS NVR) | Multi-provider GenAI (descriptions, **review summaries**, embeddings, chat). "VLM monitoring" runs a GenAI provider in a loop on a camera's live view | Hobbyist and home-lab default. LocalLLaMA users run it (§4) | [A] winterflow.io/catalog/frigate/releases/v0.18.0-beta1/ (`p33`) |
| Jul 15, 2026 | **NVIDIA Metropolis** | 80+ agent "skills": **VSS Blueprint 3.2** ("always-on video agents that alert, summarize and search across large camera networks"), DeepStream 9.1, TAO 7, Physical AI Data Factory. OMRON, Hitachi, Fujitsu (VSS + "Agentic Memory") | NVIDIA judges' vocabulary: *skills, always-on, agentic memory* | [A] blogs.nvidia.com/blog/japan-ecosystem-2026/ (`p30`), gamesbeat.com/nvidia-metropolis-speeds-… (`p07`) |
| Jul 2026 | **Amazon** | Deprecating most in-house Nova flagships (Premier, Omni, Reel, Canvas). Nova 2 Lite and Nova Multimodal Embeddings stay | AWS leans on TwelveLabs for video | [B] businessinsider.com/amazon-overhauls-ai-strategy-phasing-out-most-nova-models-2026-7 (snippet `s13`) |
| Jul 22, 2026 | **Axon** (body-cam) | Forbes: Draft One / Form One AI reports "get facts wrong" (names, plates). 600k reports. King County refuses AI-written reports | The *hallucination-in-summaries* story judges know | [B] forbes.com/sites/thomasbrewster/2026/07/22/… (`p21`) |
| Jul 30, 2026 | **Hack the Video Agent Context Graph** (SF, AWS Loft) | 151 builders, 37 projects (TwelveLabs + OpenAI + Neo4j + Strands). 1st MealPrep, 2nd Rehearsal, **3rd ZooVision (overnight fixed-cam → morning handoff)** | Closest hackathon analog to UNWATCHED (see §3) | [A] neo4j.com/blog/developer/one-starter-repo-three-winners-… (`p17`) |
| Aug 5–9, 2026 | **ByteDance SeedRealtime** | Native audio-visual full-duplex LLM ("watches, listens and speaks"), live in Doubao. No paper, weights, or API | Real-time *interactive* video is a consumer race; not our lane | [B] marktechpost.com/2026/08/09/bytedance-seed-introduces-seedrealtime-… (`p13`) |
| Aug 10, 2026 | **Meta Muse Glimmer 30B** | Apache-2.0 local agentic model with a 1.8B Perception Encoder | Open local VLM option; image-centric | [B] infoq.com/news/2026/08/meta-muse-glimmer/ (`p25`) |
| Aug 14–16, 2026 | **NVIDIA Seattle DGX Spark Hack** | Tracks See/Do/Spark. "See" won by **Kerberos** (shared spatial awareness for search-and-rescue) | NVIDIA hackathons reward perceive → reason → act | [C] LinkedIn/YouTube snippets (`s38`). UNVERIFIED detail |
| Sep 1, 2026 | **Google Gemini** | **Agentic video understanding** on 3.7 Flash / 3.6 Flash / 3.5 Flash-Lite: the model picks what, at what FPS, and which modality. Lists **anomaly detection** ("resample interesting time windows at higher FPS") as a use case | Validates "selective attention". Caveat: it's per-query routing, not archive triage | [A] blog.google/…/introducing-agentic-video-in-gemini/ (`p01`); analysis developersdigest.tech/blog/gemini-agentic-video-understanding-2026 (`p34`) |
| Sep 3 / Sep 10, 2026 | **TwelveLabs** | *Compliance by TwelveLabs* GA. **Marengo is the first video model in Bedrock Managed Knowledge Base** | Managed video-RAG is commoditizing. Pull/search is table stakes | [A] globenewswire.com (linked in `p02`) |
| Sep 8, 2026 | **Meta Muse** (personal agent app) | Topped iOS charts | Consumer "agent that acts for you" moment | [B] about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ (snippet `s36`) |
| ~Sep 15–24, 2026 | **Gemini 3.8 Live / Live Avatar; Gemini 3.8 Flash** | Live API voice/video models billed per minute. 3.8 Flash LVBench 87.8% agentic vs 87.1% static | Live-stream Q&A gets cheaper | [B] theverge.com/tech/1000328/…; [C] university-365.com (`p37`), UNVERIFIED numbers |
| Sep 17, 2026 | **Verkada (VerkadaOne)** | **Catalyst**, a read-only MCP so Claude/ChatGPT/Gemini can build workflows and reports over Verkada Command | Incumbents expose video to agents via MCP. Exposing an MCP/tool for our digest is an easy add | [A] prnewswire.com/…/verkada-expands-physical-ai-platform-…-mcp-integrations-302882121.html (`p43`) |
| Sep 18, 2026 | **Alibaba Qwen3.8-Omni-Flash** | API-only omni model, 1M context. ~$0.20 per minute of 720p video at 1 fps | Per-minute video cost is still real money at fleet scale, which helps our "filter before spend" argument | [B] startupfortune.com/alibabas-qwen38-omni-flash-… (`p41`) |
| Sep 29, 2026 | **OpenAI dots** | "Always-on agents" on GPT-6 Astra; "bring you work … sometimes before you even think to ask" | The push-not-pull zeitgeist, in OpenAI's words | [A] openai.com/index/introducing-dots/ (`p14`) |
| Sep 2026 (ongoing) | **Flock backlash** | Texas halts state funding (Sep 1). Wired camera-dump story. Indianapolis officers charged | Privacy is a live headline. Pre-empt it | [B] securitytoday.com/articles/2026/09/01/…; wired.com/story/hackers-flock-camera-data-… (snippets `s07`) |
| Background | **Ambient.ai** | Pulsar reasoning VLM (Nov 2025): "Agentic Video Walls" highlight the most interesting streams. New ARR doubled, 140%+ NRR, 200M video-hours/yr (Feb 18) | Closest "attention triage" incumbent, but live and edge-based | [A] prnewswire.com/…/ambientai-unveils-pulsar-… (`p10`); yahoo ARR (`p40`) |
| Background | **Lumana** (TNW feature, ~Aug–Sep 2026, UNVERIFIED date) | VIA-1 per-camera normal; 50k+ cameras; "up to 90%" fewer false alerts; **"We filter before we spend."** Admits re-learning after layout changes needs operator feedback | Direct claim overlap. Use the "normal changes" weakness | [B] thenextweb.com/news/video-first-frontier-ai-physical-world-lumana (`p11`) |
| Background | **Overshoot** (YC W26) | "<200ms" real-time VLM API over LiveKit/WebRTC; "1000+ developers … video agents in gaming, robotics and security" | Live-stream infra. We're archive-native | [A] ycombinator.com/launches/PQO-overshoot-ai-vision-in-real-time (`p09`) |

Skipped as generative (not understanding): Higgsfield $400M at $5.4B (Aug), Reactor $59M (May), LTX-2.5, Grok Imagine. Physical-AI *data* rounds (Mecka ~$500M valuation Sep 11, Ropedia $22–30M Jul 23) show capital chasing video-as-training-data, which is adjacent to VAST's data story [B] (`s31`).
Gaps: Spot AI and Volt had no new 2026 round found. Field AI, Dyna, Reka, and VideoDB produced no Jul–Oct launch hits in our searches (treat as unknown, not as absent).

---

## 2. Viral and notable launches (Product Hunt, HN, X, Reddit)

There was no single breakout "AI that watches your cameras" launch on Product Hunt or Show HN in the window. PH leaderboards were dominated by general agents. The buzz sits in model launches and OSS NVR tooling:

| Item | Where | Why it spread | Link |
|---|---|---|---|
| Gemini agentic video ("model decides what to watch") | Google blog, dev newsletters, HN | 88% token cut; a one-flag API change | blog.google/…/introducing-agentic-video-in-gemini/ |
| HN on Gemini Flash for video | HN thread *Gemini 3.7 Flash* | "Crazy it's still the only video understanding endpoint" (icelancer). A rebuttal says it's "just sampling the frames" | news.ycombinator.com/item?id=49289112 [C] |
| HN on GPT-5.6 Sol vision | HN | "best video captioning model … by a mile". Earlier GPT-5 was "hallucinating actions that didn't happen". Gemini Pro "can't see almost anything sub-second" | news.ycombinator.com/item?id=49329575 [C] |
| Frigate 0.18 GenAI review summaries + VLM monitoring | GitHub / r/frigate_nvr | Home-lab "AI on my cameras" default | winterflow.io/catalog/frigate/releases/v0.18.0-beta1/ |
| r/LocalLLaMA "Best Local VLMs – July 2026" | Reddit | Users "analyze a series of consecutive frames from a security camera paired with metadata of what was detected using traditional object detection" | reddit.com/r/LocalLLaMA/comments/1uoalfq/ [C, scrape blocked] |
| r/LocalLLaMA "Local LLMs for non-coding" | Reddit | "giving it security camera footage and having it summarise days/nights" | reddit.com/r/LocalLLaMA/comments/1vb4s1n/ [C] |
| r/LocalLLaMA vision benchmark (Jun 21) | Reddit | "benchmarking VLMs for video tasks. Forcing reasoning adds latency and noise." | reddit.com/r/LocalLLaMA/comments/1ubx4rw/ [C] |
| Orchestra "God-mode" for SF streets | Business Insider | Viral for the wrong reasons (privacy) | businessinsider.com/this-startup-wants-to-make-city-streets-searchable-with-ai-2026-7 |
| Latent Space "Why Video Agent models are next" (Ethan He, xAI) | Podcast | "the next Sora won't be a better video model, but a video agent". Also flags "the hidden cost of storing and moving massive video datasets" | latent.space/p/video-agents (`p22`) |
| Overshoot playground | YC Launch | "<200ms" live vision demos | overshoot.ai |

---

## 3. Hackathon winners in 2026: what won and the demo patterns

| Event (date) | Winner(s) relevant to video | Pattern | Source |
|---|---|---|---|
| **Hack the Video Agent Context Graph**, SF (Jul 30) | 1st **MealPrep** (graph from cooking videos; "the extraction refuses to guess", writing 0 calories rather than estimating). 2nd **Rehearsal** (presenter gives a live talk and gets a timestamped debrief: "the thing did the thing, live, on the presenter"). 3rd **ZooVision**: "Overnight animal-welfare monitoring … Fixed-camera footage in … timestamped activity timeline out, with a review-and-handoff workflow for the morning shift". Severity from 8 deterministic rules; "Models extract, normalize, and phrase. They never grade." Provenance tracks per evidence layer; QR code to try it live | **Anti-hallucination discipline + live self-demo + overnight→morning handoff** | neo4j.com/blog/developer/one-starter-repo-three-winners-neo4j-at-hack-the-video-agent-context-graph/ [A] |
| **AI Tinkerers NYC vision hack** (2026, exact date UNVERIFIED; placements not shown) | **Anomaly Congestion in NYC**: "learns what each block normally looks like, then flags the cameras that suddenly deviate … and explains why". **CurbWatch**: detector → Gemini "cross-checks the detector's labels against the image, corrects mislabels"; human approves; JSONL trace; "≈ $0.03 to verify one complaint"; replay-mode fallback "if a camera goes dark on stage". **Blockwatch**: "the difference between a camera and an observer" | **Learned-normal on public cams + cheap-detector→VLM-verify + cost-per-verdict + offline fallback** | nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/showcase [A for content, C for ranking] |
| **Gemini Live Agent Challenge** (May 15) | ORION (surgical voice co-pilot), drone-copilot (voice + autonomous visual inspection) | Real-world hardware + live multimodal loop | cloud.google.com/blog/…/winners-and-highlights-of-the-gemini-live-agent-challenge [A] |
| **NVIDIA Cosmos Cookoff** (Apr) | Zenith (explainable palletizing, Reason2 LoRA), JARVIS (2nd), LiveKit (3rd) | Visible reasoning (already in 02-competitive) | forums.developer.nvidia.com/t/…/366130 [A] |
| **NVIDIA Seattle Spark Hack** (Aug 14–16) | Kerberos (See track: shared spatial awareness for SAR), LifeKit (Spark track: offline survival companion) | Perceive → reason → act on local hardware | LinkedIn/YouTube snippets [C] |
| **TwelveLabs LA M&E hack** (Mar 28–29) | Gallery dominated by **compliance** tools ("reduce manual review time by 95%", "instant audit trails") | Vertical workflow + audit trail | twelve-labs-la-me-2026.devpost.com [A gallery; winners not parsed] |
| Caltech Hacktech "Sentinel" (Apr) | Camera *placement* optimizer (not video understanding) | n/a | devpost.com/software/sentinel-qkt9cn [B] |

**Winning-demo patterns, distilled:**
1. **It ran live, on real feeds, and had a fallback.** CurbWatch kept a cached replay mode; ZooVision put a QR code on the slide; Rehearsal demoed on the presenter.
2. **Provenance over prose.** Every claim links to a clip, frame, and timestamp. Models are explicitly "non-authoritative". There's an append-only trace (JSONL, graph, or ledger).
3. **The model is allowed to decline.** "Refuses to guess", "states honestly when the detector is wrong", "never grade". Judges now reward restraint because of the Axon/Home Brief hallucination stories.
4. **Cost per verdict on screen.** "$0.03 per verified complaint", "$29 to sweep 963 cameras", "Gemini … called once per report, not once per frame".
5. **A named human and a handoff artifact.** The morning-shift keeper, the DOT operator, the compliance reviewer.
6. **A cheap detector nominates and a VLM verifies** appears in at least two NYC projects and Spot AI's product. It's common, so it isn't a differentiator alone.

---

## 4. Social buzz: what builders are excited about, and the pain points they cite

- **Excitement:** "the model decides what to watch" (agentic video); sub-second captioning (GPT-5.6 Sol); always-on agents (dots, Muse); local VLMs on home cameras (Frigate + llama.cpp); video agents as "the next Sora".
- **Pain: cost/tokens.** One minute of 30 FPS video is ~352K visual tokens, and an hour is ~21M before compression (v-chandra.github.io/efficient-video-intelligence/, `p23`). Qwen's cheap omni model is still ~$0.20 per minute of video. The agentic-video caveat is that savings vanish for "summarize every segment" queries, since it's "a routing claim, not a compression claim" (developersdigest, `p34`).
- **Pain: temporal blindness.** "Gemini Pro … can't see almost anything sub-second". Frame sampling misses events between frames (HN `p36`; matches Qdrant's 0.97 vs 0.23 single-frame result in 02-competitive).
- **Pain: hallucination.** GPT-5 era was "hallucinating actions that didn't happen" (HN). Axon reports get names and plates wrong (Forbes). Starbucks retired NomadGo after it "hallucinated stock counts" (startupfortune, `p03` sidebar, [B]).
- **Pain: latency vs reasoning.** "Forcing reasoning adds latency and noise" (r/LocalLLaMA, [C]). Overshoot sells "<200ms".
- **Pain: normal drifts.** Lumana concedes re-learning after layout or shift changes takes operator feedback, with no fixed time (TNW `p11`).
- **Pain: privacy and trust.** Flock, Orchestra, ACLU. Lumana and Orchestra both stress "no facial recognition".

---

## 5. What this means for UNWATCHED today

### Positioning (one line)
> **"Everyone this year built agents that watch video when you ask. UNWATCHED is for the 99% of footage nobody will ever ask about. It filters before it spends, verifies before it pages, and shows you what it chose *not* to show you."**

- Frame it as **"always-on, push, archive-native"**, the dots and VSS 3.2 language applied to storage. Pull/NL-search is now commodity (Coram, Conntour, Ambient, Verkada, TwelveLabs on Bedrock KB).
- Borrow Lumana's line openly and go one step further. Their version is "filter before you spend" at the edge. Ours is: **filter at rest, inside VAST, then verify with Cosmos-Reason2, then measure what we suppressed.**
- Pre-empt Gemini agentic video: *"Gemini now decides what to watch inside one video when you ask a question. We decide which of 10,000 camera-hours deserve a question at all."* (per-query routing vs fleet-level triage).
- Pre-empt ZooVision and NYC "Anomaly Congestion": *"Learned-normal demos are popping up at hackathons this summer. That's the idea working. What they didn't have: a reasoning verifier on every outlier, and a measured precision/recall on what got suppressed."*

### Demo tricks the 2026 winners used (adopt them)
1. **Offline replay fallback** (CurbWatch). Pre-record the 5 s segments and verdicts in case the live cam or GPU dies.
2. **Cost per verdict on screen**: "$/camera-hour" and "Cosmos calls avoided". It mirrors "$0.03 per complaint".
3. **"The model declined" moment**: show the decoy *dismissed*, with Cosmos's grounded reason. That's the restraint judges now reward.
4. **Provenance lanes** in the UI (ZooVision's separate tracks). Show embedding distance (nominated), then Cosmos verdict (verified), then human 👍/👎 (ground truth) as three visibly separate layers. Say "distance never pages anyone".
5. **QR code to the digest** on the final slide, so judges get the morning brief on their phones.
6. Optional quick win: expose the digest and ledger as a **read-only MCP/tool** (Verkada Catalyst did this Sep 17), so "ask Claude/Gemini about last night" works. Only do it if time allows.

### Words judges are hearing this quarter (use them)
*always-on agents* · *agentic video understanding* · *filter before you spend* · *video as memory / the archive stops being passive storage* · *agent skills* (NVIDIA) · *verified alerts / proposer-verifier* · *provenance / audit trail* · *physical AI* · *open-set* · *MCP*.

### Words to avoid (2026-specific additions to 02-competitive's list)
*"search engine for the physical world"* / *"God-mode"* (Orchestra backlash) · *"watches people"* · *"anomaly detection"* as the headline (Gemini, Archetype, and NVIDIA all use it now, so it sounds generic) · *"real-time"* as the hero claim (Overshoot <200ms and Gemini Live own that; ours is archive-native).

### Collision update (vs 02-competitive §5)
- **Daily/shift-summary teams**: risk is higher. ZooVision proves "overnight → morning handoff" wins prizes. Defend on *selective + verified + suppression ledger + attention budget*.
- **Learned-normal teams**: now **0–3** teams (was 0–2). The NYC hack shows the pattern is easy to reach for with public cams + Gemini. Defend on per-camera baselines in VastDB, the Cosmos verify gate, and measured precision.

---

## Sources (primary captures)
Scrapes `.firecrawl/trend-mkt-p01…p45` (Reddit p18–p20 and LinkedIn p38–p39 failed: unsupported or blocked). Searches `.firecrawl/trend-mkt-s01…s44`. Key URLs are cited inline above.
