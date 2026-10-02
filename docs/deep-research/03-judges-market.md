# 03 — Judges, Organizer, Market (UNWATCHED)

Researched 2026-10-02 (morning of SF build day). Raw scrapes and search JSON: `docs/sources/dr-judge-*.{md,json}` (24 search result sets, 30 page scrapes). This uses only public professional information: blogs, talks, press, and public post snippets.

**Source quality key:** **[A]** primary source (vendor press release or own blog, government or regulator, analyst press release). **[B]** credible secondary source (trade press, IPVM, industry body). **[C]** vendor marketing blog or search snippet only. Treat C as directional.

---

## 1. SF judges: what each one works on, and what will impress them

| Judge | What they publicly work on / value | What will impress this judge | Tailored pitch sentence |
|---|---|---|---|
| **Hassan Moustafa**, NVIDIA TME, Multimodal AI (Metropolis) | Lead author of **"Lower the Cost of Building and Running Visual AI Agents with NVIDIA VSS Blueprint 3.3"** (Sep 29 2026). Its themes: VLM token cost is the operating-cost driver, and **Adaptive EVS** prunes unchanged visual patches and batches VLM work "around moments of activity," giving 80% fewer VLM input tokens and 46% more concurrent streams. He also covers alert verification and the `vss-build-vision-ai` skill. His bio covers VSS, Cosmos, the Physical AI Data Factory, "performance sizing." He gave the GTC26 lab DLIT81774, "Build a Video Analytics AI Agent With VLMs." [A] `dr-judge-moustafa-vss33.md`, `dr-judge-s-moustafa.json` | A measured cost/accuracy trade-off: the percentage of segments that reach Cosmos, tokens saved, and precision/recall with the gate on vs. off. Benchmark on representative footage, which is exactly his own advice in the blog. | "EVS prunes unchanged patches inside a clip. UNWATCHED applies the same idea to the whole archive: a CPU embedding distance decides which 3% of segments are worth a Cosmos call, and the eval shows we didn't lose the incidents." |
| **Adam Ryason, PhD**, NVIDIA Product (PM, leads the VSS Blueprint) | Leads the VSS Blueprint, and is a former startup founder (vision AI, digital twins, HCI). Posts: **"Integrating Context-Aware Video AI Agents Into Enterprise Workflows"** (Jul 2026), where NemoClaw + VSS + RAG produce *structured, timestamped reports with citations* and *route findings to Jira/Slack*, with "full traceability from evidence to decision." Also "Transform Video Into Instantly Searchable, Actionable Intelligence with AI Agents and Skills" (May 2026), GTC Paris "Bringing Physical AI to Cities," and a co-authored VAST InsightEngine + NVIDIA Blueprints blog. [A] `dr-judge-ryason-author.md`, `dr-judge-ryason-enterprise.md`, `dr-judge-s-ryason.json` | Product framing: a named buyer, a workflow that lands in the tools that buyer already uses, and a clear statement of what VSS does vs. what you added. The morning digest as a *cited, timestamped report pushed to Slack* is close to his own NemoClaw pattern, applied unprompted. | "VSS answers when you ask. UNWATCHED is the agent that asks for you: every morning it pushes a cited, timestamped digest of the 3 things on 40 cameras nobody looked at, and each item links to the clip and to the reason it was flagged." |
| **Ram Bansal**, VAST Sr Developer Advocate (since Sep 2025; previously DevRel at Nylas) | Co-author of the VAST video-search blog (DataEngine **triggers → serverless functions → VastDB embeddings**) and of **"Talk to Your Data Infrastructure: Accelerate Infrastructure Management with MCPs"** (VAST Admin MCP, natural-language cluster admin). His DevRel career is about "empowering developers… with APIs to create innovative products." VAST Live webinars exist (YouTube playlist), but I found no Bansal-specific webinar. VAST Forward speaker page exists with no sessions listed. [A] `dr-judge-bansal-mcp.md`, `dr-judge-s-bansal.json`, `dr-judge-bansal-forward.md` | Idiomatic DataEngine use: a custom function placed in the trigger chain, Event Broker topics, `vastde` traces. Also a clean public repo a developer could fork. Bonus points for exposing the baseline/verdicts as an MCP tool. | "We didn't build next to your pipeline, we built inside it: one extra function in the segment trigger chain scores every clip against its camera's learned baseline, and only outliers go on to the Cosmos function on the Event Broker." |
| **Brian Verkley**, VAST Director, AI Data Platform | Wrote **"Introducing AgentEngine"**. Its pillars: agent runtime, the MCP Toolbox, and *observability*. He calls out logging of prompts/responses, chain-of-thought tracing, "a clear audit trail," and **feedback loops ("thumbs-up/down ratings")** so agents keep improving. Also wrote "S3 over RDMA: Scaling the KV Cache Data Plane" and the Cosmos community launch blog, and wrote for The New Stack. Public post: "NVIDIA Nemotron 3: Efficient AI for **Anomaly Detection**" (snippet only). He is a recurring speaker on "your AI problem is a data problem." [A]/[C] `dr-judge-verkley-agentengine.md`, `dr-judge-s-verkley*.json` | Treat data as state: the baseline lives in VastDB, every verdict has an audit row (which baseline, which snapshot, which model), and a human 👎 closes the learning loop. That is literally his AgentEngine pitch, and he has publicly shown interest in anomaly detection. | "Every dismissal is auditable. It records the VastDB baseline snapshot it was judged against, and a single 👎 in Slack folds the segment back into 'normal.' It's the feedback loop you described for AgentEngine, running on camera data." |
| **Anushrav (Anu) Vatsa**, CoreWeave Staff Account SA, Physical AI Lead | Physical AI on CoreWeave + W&B. At CoreWeave Fully Connected he presented adapting NVIDIA's DreamZero world-action model to two arms, with the line "**four attempts that actually got evaluated**" against **233 failed experiments that were never evaluated** (Turing Post). His GTC post: "Embodied AI from 0 to 100" with CoreWeave hardware + **W&B Models**. Also evaluates world models' zero-shot generalization. CoreWeave launched **Physical AI Field Engineering** in Sep 2026. [B] `dr-judge-vatsa-turingpost.md`, `dr-judge-s-vatsa.json`, `dr-judge-s-cwphysical.json` | Evaluation discipline plus unit economics. A Weave eval of the 8B vs 2B verifier on labeled clips, with failed runs shown rather than hidden, and a live **$/camera-hour** GPU meter that holds up at 10k cameras. | "We ran the evaluation you'd want before any of this ships: a Weave leaderboard of 60 labeled clips, 8B vs 2B Cosmos, precision and recall. The GPU meter shows Cosmos touched 3.1% of segments, which is why the $/camera-hour still works on CoreWeave at 10,000 cameras." |
| **Arnav Verma**, SpaceXAI (Cursor) Field Engineer (since Apr 2026) | Previously a Forward Deployed Engineer at Anyscale, co-founder of Clodo (YC S25, an AI assistant for real-estate agents), a Solutions Engineer at Databricks, and at AWS. Public post on Cursor's internal "pstack": it lets "a single field engineer ship nuanced demos and push the edge" (snippet). A founder plus forward-deployed profile. [C] `dr-judge-s-verma*.json` | Shipping velocity and a demo that clearly works, built visibly in Cursor (rules, agent runs, commit cadence). He'll also respond to founder-grade customer clarity: who pays, and the wedge. | "We built this in Cursor in six hours. The repo has our `.cursor/rules` and the agent transcripts, and the wedge is the one thing a security manager reads at 7 a.m.: the digest." |

**Panel read:** 2 NVIDIA judges (VSS PM + VSS TME) = the people who *own* alert verification. Our differentiator has to be stated relative to VSS, not hidden from it: VSS verifies alerts someone configured, and UNWATCHED finds what nobody configured, in footage nobody reviews. 2 VAST judges = data-as-state, DataEngine-native, auditability. 1 CoreWeave = eval plus GPU economics. 1 Cursor = velocity and polish.

---

## 2. tokens& (organizer)

- **Who:** tokens& ("tokensand, LLC") describes itself as connecting "AI companies with exceptional engineers, researchers and founders through hackathons, technical summits and community events." They have two sites. tokensand.ai is the community/events site. tokensand.com is a builder platform with credits/perks, a stack builder, and project "proof" rankings, plus an enterprise side that sells developer adoption to infra/dev-tool companies ("Reach AI developers. Drive adoption and pipeline."). [A] `dr-judge-tokensand-ai-events.md`, `dr-judge-tokensand-events.md`, `dr-judge-tokensand-home.md`
- **Past events (2025–26):** Autonomous Agents Hackathon (SF, Feb 27 2026, AWS Builder Loft), Deep Agents Hackathon (SF, RSAC 2026), Multimodal Hack (SF, Mar 28 2026), NYC hack (Feb 21 2026), Ship-to-Prod / Ship Demo Day (Apr 2026), Long Horizon Agents Hackathon (with OpenAI, AWS, Liquid AI, Broccoli AI), Loop Engineering Hackathon (Pomerium MCP challenge), London Multiagents (Devpost), Swarm, Harness, Open Model hacks, and the Agentic Engineering Summit. Upcoming: the Cyberdefense Hackathon (SF, Oct 9) and Production Agent Lab (Oct 10). Most SF events run at the **AWS Builder Loft** (same venue as today). [A]/[B] `dr-judge-tokensand-ai-events.md`, `dr-judge-awsloft.md`
- **How they judge (pattern):** tokens& Hacks London (Devpost) published the criteria **Idea (real-world value), Technical Implementation, Tool Use (sponsor tools), Presentation, Autonomy** ("How well does the agent act on real-time data without manual intervention?"). Today's VAST blog says **creativity, technical implementation, real-world impact**. Expect the sponsor judges to weight **tool use** heavily, even though it isn't listed. The **Autonomy** criterion is a gift for UNWATCHED, because the unsolicited digest *is* autonomy. [A] `dr-judge-tokensand-devpost-multiagents.md`
- **Gallery / winners:** the vastsf gallery is empty pre-submission. tokens& surfaces featured projects on tokensand.com's home page ("Copy what builders are shipping"): Breakout (a live AI news desk on the GitHub firehose), Vithia (verifiable long-horizon agents), Seekr (an embodied visual shopping agent), Mood Canvas, Clinical Trial Matcher. Nihal's own **Dead Reckoning** (from the Long Horizon hack) is featured there too. Featured projects share three traits: a **one-sentence, concrete hook**, **a recording link**, and **a public GitHub repo**. Public winner lists are thin. One public LinkedIn bio mentions 1st place "Best Use of Kiro" at the tokens& Deep Agents Hackathon, which suggests sponsor-specific "best use of X" prizes are common. [A]/[C] `dr-judge-tokensand-home.md`, `dr-judge-s-tokensand-winners.json`
- **Implication:** submit early with a crisp one-line description and the recording. Featured projects are curated from submissions with repo + video.

---

## 3. Market: validated and corrected numbers

### 3a. How much footage is never watched
| Claim | Value | Source / quality |
|---|---|---|
| Share of recorded surveillance video monitored live | **"less than 1%"** (estimate from IPVM's live-monitoring usage survey); "only a small fraction is actually later watched" | IPVM [B] `dr-judge-mkt-ipvm-unwatched.md`. **Best citable figure.** |
| "98–99% of CCTV footage is never watched" | 98–99% | Vendor blogs (Fortix, Arcadian) [C]. Use only as "industry estimates say ~99%." Prefer the IPVM "<1% watched live." |
| Retail behavior | 64% of retail managers only review footage after an incident | SecurityCameraKing blog [C] |
| Operator attention | "attention span… drops 50% in 20 minutes" (an anecdote retold on IPVM). Vendor blogs say "miss 95% after 22 minutes" | [C]. Folklore with no primary source found. **Avoid** in the pitch, or attribute it loosely. |
| Installed base | **"over two billion cameras worldwide"** (Deepu Talla, NVIDIA VP Robotics & Edge AI, 2026 Metropolis briefing) | GamesBeat quoting NVIDIA [B] `dr-judge-nvidia-metropolis-gtc.md`. Quoting NVIDIA back to NVIDIA judges is good. |

### 3b. Market size (correct the FINAL-IDEA "$50B+")
| Segment | Number | Source / quality |
|---|---|---|
| Global video surveillance (Omdia definition: equipment/software) | **$27B in 2025, +4.3% YoY. Forecast +12.8% in 2026**, driven by component price inflation. Omdia also notes "software captures a growing share," with monetization of AI analytics and VSaaS | **Omdia press release, Jul 29 2026** [A] `dr-judge-mkt-omdia.md`. **Most credible.** |
| Broad "video surveillance market" (research-firm definitions incl. services/installation) | $63.1B 2025 (GMI); $83.5B 2025 → $94.1B 2026 (Grand View); $65.8B 2025 surveillance+VSaaS (Grand View) | [B/C] `dr-judge-s-mkt-size.json` |
| VSaaS | **$5.28B 2025 → $5.88B 2026 → $12.01B 2032 (12.6% CAGR)** (MarketsandMarkets). Mordor: $7.62B 2026 → $15.64B 2031 | [B] `dr-judge-mkt-mnm-vsaas.md`, `dr-judge-s-mkt-vsaas.json` |
| Video surveillance storage | $10.93B 2026 → $15.55B 2031 (MarketsandMarkets) | [B]. A VAST-relevant adjacency. |

**Correction:** replace "roughly $50B+ market" with **"a $27B market by Omdia's count (up to $60–80B+ on broader definitions), with VSaaS at ~$6B growing 12–15%/yr, and Omdia says software and AI analytics are taking a growing share."**

### 3c. Cost of watching (anchors for pricing)
| Item | Value | Source / quality |
|---|---|---|
| Remote video monitoring, per camera/month | Basic alarm-response **$30–75**. Standard **$50–150**. AI-enhanced **$100–200+**. Continuous live **$200–400+** | Guardian Integrated Security 2026 pricing guide [C]. Pioneer Security and Safe&Sound give the same $30–150 band [C]. `dr-judge-mkt-rvm-cost.md` |
| Security guard wage (US) | **Median $18.29/hr, $38,050/yr (2025)**; 1.30M jobs | **BLS OOH** [A] `dr-judge-mkt-bls-guards.md` |
| Overnight guard coverage (CA, 9 pm–6 am) | $6,750–8,100/month at $25–30/hr | Guardian guide [C] |
| AI video analytics software, per camera/month | **$3–15** | Wavestore (search snippet) [C] |
| Cloud VMS license | $15–30/camera/month. Verkada ~$199+/yr per camera license | LiveReach, iFovea, Fora Soft [C] `dr-judge-s-mkt-aiprice.json` |

**Price validation:** FINAL-IDEA's **"$5–10 per camera per month" is validated**. It sits in the middle of the AI-analytics add-on band ($3–15) and under cloud-VMS licenses ($15–30). It is **~1/5 to 1/30 the cost of the cheapest human remote-monitoring tier** ($30–150). Suggested framing: **"$8 per camera per month, about a tenth of what a monitoring center charges just to look at alarms."** A 100-camera multi-site operator works out to ~$9.6k/yr, versus ~$80k+/yr for one overnight guard post.

### 3d. False alarms (supports "the alerts you already have are mostly noise")
| Claim | Value | Source / quality |
|---|---|---|
| Police alarm calls that are false | **94–98%** (higher in some jurisdictions). Dallas 2004: only **2.8%** valid. Each false alarm ≈ **20 min of police time, usually 2 officers** | **US DOJ COPS / ASU Center for Problem-Oriented Policing, "False Burglar Alarms, 2nd ed."** [A] `dr-judge-mkt-popcenter-falsealarms.md`. Caveat: these are *intrusion alarms* (sensors), the data is ~2002–2005, and it is not about video analytics. |
| Alarm-receiving-centre signals that aren't genuine | 76% | Davantis (vendor) [C] |
| AI filtering claims | "up to 90%" (Lumana), "up to 99.95%" (Scylla) false-positive reduction | Vendor [C]. Don't cite in the pitch. |

### 3e. Retention requirements (why archives are big and unwatched)
| Rule | Value | Source / quality |
|---|---|---|
| California cannabis licensees | **"Surveillance recordings shall be kept for a minimum of 90 calendar days"** (16 CCR §15044(h)), immediately viewable on request | **Westlaw, CA Code of Regs** [A] `dr-judge-mkt-ca-cannabis-retention.md` |
| Cannabis boards generally | 30–180 days. Casino regulators 3–30 (Nevada casinos: 7 days baseline) | mentatnoc, EEN [C] `dr-judge-s-mkt-retention.json` |
| PCI DSS | 3 months, but only for cameras/access controls monitoring sensitive cardholder-data areas. "All footage 90 days for PCI" is a common myth | Fora Soft, SCW [C]. Use carefully. |

**Pitch math:** one camera at 90-day retention = **2,160 hours** of footage. A 40-camera site holds **86,400 camera-hours**. At "<1% watched live," roughly 85,500 of those hours are never seen by a person.

---

## 4. Sponsor vocabulary to mirror

**VAST** [A]
- "**The AI Operating System company**." The AI OS "consolidates foundational data and compute services and agentic execution into one scalable platform… reason over real-time data, and automate…" (press boilerplate). `dr-judge-vast-foundation-stacks.md`
- "**Thinking machine**": "a computer that would continuously learn from new data" (HPCwire on VAST Forward, Feb 2026). Hallak: "a system that could **continuously refine data into intelligence and action**." The original AI OS launch: "built to capture data from the natural world at extreme scale." `dr-judge-vast-hpcwire-thinking.md`, `dr-judge-s-vast-thinking.json`. **UNWATCHED's per-camera baseline that keeps learning is a small thinking machine. Say it.**
- **TuningEngine + AgentEngine = the "learning loop"** (VAST Forward 2026). AgentEngine has an audit trail and thumbs-up/down feedback loops.
- **VAST Foundation Stacks** (GTC, Mar 16 2026): an open-source library extending NVIDIA Blueprints. The first one is the **VSS-based stack in `vast-data/cosmos-labs/dataengine-vss-blueprint`**, which is what we build on. `dr-judge-vast-foundation-stacks.md`
- **Hyperscale Vector Index** (Feb 2026): "In a video RAG workflow, semantically relevant clips can be retrieved while **filtering by time range, camera ID, location**… within a single execution path." Vectors and metadata live together. Our per-camera centroid query is this exact use. `dr-judge-vast-next-release.md`
- Other VAST terms: DASE, DataEngine (triggers + functions), Event Broker, VastDB, InsightEngine, Cosmos Community. "Physical AI at scale" (NCS + VAST video).

**NVIDIA** [A]/[B]
- **VSS 3 (GTC San Jose, Mar 2026):** modular, *agentic search for actions and temporal events*, **Real-Time Video Intelligence (RTVI)** microservices, smart-city and warehouse reference workflows. `dr-judge-nvidia-gtc-sj26.md`
- **VSS 3 GA with agent skills** (GTC Taipei, GA Jun 8 2026). **Cosmos 3**: "world's first fully open omni-model for physical AI" (Nano/Super). **Metropolis "made agentic," 80+ skills**, "6× faster" development (VSS 3.2, DeepStream 9.1, TAO 7, Physical AI Data Factory). `dr-judge-nvidia-gtc-taipei.md`, `dr-judge-nvidia-metropolis-gtc.md`
- **VSS 3.3 (Sep 29 2026):** `vss-build-vision-ai` skill, **Adaptive EVS**, alert verification, "always-on video agents that alert…". Livestream "Build Visual AI Agents From a Prompt" was Oct 1. `dr-judge-moustafa-vss33.md`
- NVIDIA phrasing: "vision AI is transforming beyond passive perception and dashboards into agentic systems that can **understand, reason and act in real time**."

**CoreWeave:** "Physical AI Field Engineering" (Sep 2026). Its physical-AI stack is pitched as "end to end, so a checkpoint that fails in the field traces back to the exact run and dataset." Lineage and eval matter here. `dr-judge-s-cwphysical.json`

---

## 5. Pitch lines to use

1. **(Market stat → IPVM, NVIDIA)** "NVIDIA counts over two billion cameras worldwide, and by IPVM's estimate less than 1% of what they record is ever watched live. UNWATCHED is the reviewer for the other 99%." (IPVM `dr-judge-mkt-ipvm-unwatched.md`; Deepu Talla via GamesBeat `dr-judge-nvidia-metropolis-gtc.md`)
2. **(Hassan Moustafa / Adam Ryason → VSS 3.3)** "VSS 3.3's Adaptive EVS skips unchanged patches inside a clip. We apply the same idea across the archive: a CPU baseline decides which ~3% of segments deserve Cosmos, and VSS-style verification confirms them before anyone gets paged." (`dr-judge-moustafa-vss33.md`)
3. **(Brian Verkley / Ram Bansal → VAST thinking machine, AgentEngine)** "VAST set out to build a thinking machine, a computer that continuously learns from new data. Each camera's baseline in VastDB is a small one: it relearns every 15 minutes, every verdict is auditable to a snapshot, and one 👎 teaches it what normal looks like." (`dr-judge-vast-hpcwire-thinking.md`, `dr-judge-verkley-agentengine.md`)
4. **(Anushrav Vatsa → CoreWeave/W&B eval culture)** "We don't ask you to trust the demo. The Weave leaderboard scores the verifier on labeled clips, 8B vs 2B, precision and recall, and the GPU meter shows the cost per camera-hour at 10,000 cameras." (`dr-judge-vatsa-turingpost.md`)
5. **(Price, Arnav Verma / Ryason → cost-of-watching stats)** "A monitoring center charges $30–150 per camera per month just to look at alarms, and 94–98% of alarm calls police respond to are false. UNWATCHED costs about $8 per camera per month and shows up unprompted at 7 a.m. with the three things that mattered." (`dr-judge-mkt-rvm-cost.md` [C]; DOJ COPS/POP Center `dr-judge-mkt-popcenter-falsealarms.md` [A])

---

### Housekeeping notes
- **The older `docs/sources/` scrapes have moved.** Files like luma-sf.md and vast-video-intel-blog.md now live in `/.firecrawl/`, and `docs/sources/` holds only `dr-*` files. EVENT-DETAILS.md links still say `docs/sources/`.
- **Unverified items:** Verkley's Nemotron anomaly-detection post (snippet only, LinkedIn blocked scraping), Verma's pstack post (snippet only), and Wavestore's $3–15 figure (meta-description only).
