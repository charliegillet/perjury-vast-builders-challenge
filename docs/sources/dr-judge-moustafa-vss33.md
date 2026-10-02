[Technical Blog](https://developer.nvidia.com/blog)

[Subscribe](https://developer.nvidia.com/email-signup)

[Related Resources](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/#main-content-end)

[Computer Vision / Video Analytics](https://developer.nvidia.com/blog/category/computer-vision/)

# Lower the Cost of Building and Running Visual AI Agents with NVIDIA VSS Blueprint 3.3

![](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/robotics-press-nurec-devpage-kv-1600x900-1-1024x576-png.webp)

Sep 29, 2026


By [Hassan Moustafa](https://developer.nvidia.com/blog/author/hmoustafa/ "Posts by Hassan Moustafa"), [Debraj Sinha](https://developer.nvidia.com/blog/author/debrajsinha/ "Posts by Debraj Sinha") and [Ashwani Agarwal](https://developer.nvidia.com/blog/author/ashwania/ "Posts by Ashwani Agarwal")

+5

Like

[Discuss (0)](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/#entry-content-comments)

- [L](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Flower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3%2F)
- [T](https://twitter.com/intent/tweet?text=Lower+the+Cost+of+Building+and+Running+Visual+AI+Agents+with+NVIDIA+VSS+Blueprint+3.3+%7C+NVIDIA+Technical+Blog+https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Flower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3%2F)
- [F](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Flower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3%2F)
- [R](https://www.reddit.com/submit?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Flower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3%2F&title=Lower+the+Cost+of+Building+and+Running+Visual+AI+Agents+with+NVIDIA+VSS+Blueprint+3.3+%7C+NVIDIA+Technical+Blog)
- [E](mailto:?subject=I%27d%20like%20to%20share%20a%20link%20with%20you&body=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Flower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3%2F)

## AI-Generated Summary

- The NVIDIA Metropolis Blueprint for Video Search and Summarization (VSS) 3.3 connects vision-language models such as [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/), LLMs such as NVIDIA Nemotron, retrieval-augmented generation, and Model Context Protocol tools to turn live and recorded video into natural-language search, visual Q&A, verified alerts, and automated reporting.
- The Build Vision Agent skill (vss-build-vision-ai) composes multi-workflow deployments from a single prompt, starting from one of four validated developer profiles and adding only the services a requested capability actually reaches while converging shared infrastructure such as Kafka, Redis, and Elasticsearch onto single instances.
- In a bottling-line demonstration, the skill produced a live, previewable deployment with search, alert verification, and shift reporting in under 30 minutes on a two-GPU RTX PRO 6000 Blackwell host, reusing the detector's GPU for FP8 Cosmos 3 Nano.
- Adaptive Efficient Video Sampling (EVS) reduces runtime VLM processing by dynamically pruning unchanged visual patches per frame and batching VLM work around moments of activity, cutting alert contextualization latency 17% and increasing concurrent real-time VLM streams 46% on an RTX PRO 6000 Blackwell running Cosmos 3 Super FP8.
- Adaptive EVS also summarized a 60-minute video in about half the time with 80% fewer VLM input tokens, with results varying by scene motion, chunk length, and similarity threshold.

### Next Steps

- Clone the [VSS Blueprint repository](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization) to access the 3.3 skills and deployment code.
- Install the [VSS Agent Skills](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization/tree/develop/skills/vss-build-vision-ai) in your coding agent's standard skills directory.
- Join the [live session on Oct. 1 at 9 a.m. PT](https://www.youtube.com/watch?v=PQJKs1dyK7I) to see a visual AI agent built from a single prompt.

Powered by NVIDIA Nemotron. AI-generated content may summarize information incompletely. Verify important information. [Learn more](https://www.nvidia.com/en-us/agreements/trustworthy-ai/terms/)

Vision-language models have made it possible to build visual AI agents that understand video at production scale. The harder problem is turning that capability into a maintainable system that combines ingestion, stream processing, event detection, retrieval, summarization, and reporting.

[The NVIDIA Metropolis Blueprint for Video Search and Summarization (VSS)](https://build.nvidia.com/nvidia/video-search-and-summarization) and its agent skills help developers build [visual AI agents](https://www.nvidia.com/en-us/use-cases/video-analytics-ai-agents/) faster. VSS connects vision-language models (VLMs) such as [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/), LLMs such as [NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/), retrieval-augmented generation (RAG), and Model Context Protocol (MCP) tools to turn live and recorded video into natural-language search, visual Q&A, verified alerts and automated reporting.

VSS Blueprint 3.3 also reduces costs from both sides: faster application composition with the new Build Vision Agent skill (`vss-build-vision-ai`), and cheaper VLM processing at runtime with Adaptive Efficient Video Sampling (EVS).

This post covers both sides of that cost reduction. On the development side, a single prompt builds and deploys a bottling-line overflow agent in under 30 minutes, with a few dollars of coding-agent usage. On the runtime side, Adaptive EVS delivers 80% fewer VLM input tokens for a 60-minute summary and 46% more concurrent streams on the same GPU.

To learn more, [join us live](https://www.youtube.com/watch?v=PQJKs1dyK7I) on Oct. 1 at 9 a.m. PT, where we will build a visual AI agent from a single prompt.

Build a Visual AI Agent in Under 30 Minutes with NVIDIA VSS Blueprint 3.3 - YouTube

Tap to unmute

[Build a Visual AI Agent in Under 30 Minutes with NVIDIA VSS Blueprint 3.3](https://www.youtube.com/watch?v=PPXoPSCdGyU) [NVIDIA Developer](https://www.youtube.com/channel/UCBHcMCGaiJhv-ESTcWGJPcw)

NVIDIA Developer225K subscribers

[Watch on](https://www.youtube.com/watch?v=PPXoPSCdGyU)

_Video 1: One prompt builds and deploys a visual AI agent for an orange juice bottling line, then the agent raises and verifies an overflow alert. The spill is synthetically generated for the demo_

## Why visual AI agents are expensive [Scroll to Why visual AI agents are expensive  section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#why_visual_ai_agents_are_expensive_)

A production [visual AI agent](https://www.nvidia.com/en-us/use-cases/video-analytics-ai-agents/) usually spans more than one workflow. A smart city application may need vehicle detection, collision alerting, searchable incident clips, hourly summaries, and an operator report. A warehouse application may need people and forklift tracking, near-miss alerts, SOP checks, and follow-up Q&A. Each workflow is useful by itself, but real deployments become valuable when those workflows work together.

That creates 3 recurring cost drivers:

- **Development cost:** Teams must choose and connect microservices, shared services such as Kafka, Redis, Elasticsearch, and Video IO and Storage (VIOS), model endpoints, environment variables, and APIs without duplicating infrastructure.
- **Operating cost:** Visual AI workloads can lead to heavy token usage, every additional stream, frame window, prompt, and visual token can increase GPU usage, queueing delay, and end-to-end summarization latency.
- **Change cost:** Teams must move from proof of concept to production, add capabilities, and keep configuration, documentation, and operations aligned.

## VSS 3.3 updates for building and running video analytics AI agents [Scroll to VSS 3.3 updates for building and running video analytics AI agents section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#vss_33_updates_for_building_and_running_video_analytics_ai_agents)

VSS Agent Skills let coding agents such as Claude Code, Codex, or any agentskills.io-compatible agent deploy and operate VSS from natural-language requests. VSS 3.3 adds two updates that reduce cost on both sides of a deployment:

- **Build Vision Agent skill (vss-build-vision-ai):** Combines VSS workflows such as alerting, search, and summarization into one application for use cases such as SOP compliance or traffic management, and extends a running deployment without rebuilding the whole stack.
- **Adaptive EVS:** This new feature reduces redundant VLM processing by pruning the visual tokens for parts of a frame that did not change compared to the previous one, and by batching VLM work around the moments when something happens. EVS already ships in vLLM and the Cosmos NIM microservices at a fixed pruning rate. The adaptive version in VSS 3.3 is integrated into the real-time VLM microservice and decides which tokens to keep per patch and per frame.

![Animation of a prompt assembling VSS services, validating resolved.yml, starting each service, and returning confirmed and rejected search clips plus a reasoned answer to “Is this a safety violation?” ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/image2.gif)_Figure 1. One prompt becomes a composed, validated, running visual AI agent, here for a warehouse, then answers questions about its video_

The Build Vision Agent skill reduces development and change costs by composing and extending deployments. Adaptive EVS lowers operating cost by reducing VLM tokens and GPU time spent on unchanged video.

## Reduce development cost with the Build Vision Agent skill [Scroll to Reduce development cost with the Build Vision Agent skill section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#reduce_development_cost_with_the_build_vision_agent_skill)

Earlier VSS skills handled individual operations such as deployment, camera setup, summarization, search, alerts, and analytics. VSS 3.3 organizes them as deployment skills, operation skills, tools, and benchmarks, with vss-build-vision-ai composing the rest.

Developers describe the application they want, and the Build Vision Agent skill translates that intent into a deployment plan spanning profiles, microservices, configuration, and runtime operations.

Rather than generate a deployment from scratch, the skill starts with the closest of four validated developer profiles, each a complete, tested stack for one workflow (see Table 1, below). The skill calls that starting profile the Foundation and changes only what the request requires.

|     |     |
| --- | --- |
| **Profile** | **Capability** |
| `base` | VLM dense captioning and Q&A on clips |
| `alerts` | Real-time VLM alerting, or RT-CV detection with behavior analytics and VLM alert verification |
| `lvs` | Long video summarization |
| `search` | Object and video embeddings with agentic search |

_Table 1: The four developer profiles a build can start from. The skill selects one as the Foundation and computes the smallest delta on top of it_

The skill then computes the smallest delta: adds or removes only exact service keys, keeps only the services that a requested capability actually reaches, and converges shared roles onto one instance.

Two capabilities that both need a detector get one detector. Two that both need Kafka and Elasticsearch share one message bus and one Elasticsearch deployment, each writing its own indices. When the rules cannot settle a choice, the skill asks one structured question instead of guessing.

![Animation mapping a request to capabilities, selecting the search Foundation by delta size, adding required services, pruning unreachable ones, merging duplicate infrastructure, and validating resolved.yml. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/image3-1.gif)_Figure 2: Every build is a delta on a validated Foundation: add only what a capability needs, prune what nothing reaches, and converge shared roles to one instance_

### What the skill automates [Scroll to What the skill automates section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#what_the_skill_automates)

- Maps the application goal to the required VSS workflows and microservices.
- Combines workflows such as alerting, search, and summarization in one deployment plan.
- Reuses shared infrastructure, including VIOS, Kafka, Redis, Elasticsearch, HAProxy ingress, and MCP services.
- Generates the deployment as a self-contained build: \_builds/<name>/override.env (the Foundation, the effective Compose profiles, and only the settings you changed), compose.yml, and resolved.yml, one flattened Compose file produced with docker compose config that deploys on its own. The repository’s deploy/docker/ tree is never modified.
- Shows an architecture diagram for review before anything is written or deployed, then runs validation, deployment, and readiness checks so the developer can verify the stack before building application logic on top.
- Asks whether to deploy an agent harness. The default is [NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/), a host-side sandbox with the VSS skills installed; answering no produces a headless stack driven by the VSS CLI.
- Extends a running deployment through a smaller delta that reuses existing services.

This shortens discovery, makes composition repeatable, and avoids duplicate ingestion, storage, messaging, and analytics infrastructure across workflows.

## Build a bottling line visual AI agent with VSS [Scroll to Build a bottling line visual AI agent with VSS section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#build_a_bottling_line_visual_ai_agent_with_vss)

For an orange juice bottling line, the team wants an agent that watches filler and capper cameras, alerts on overflows or spills, searches past incidents, and generates shift reports.

Manual development would connect event detection, alert verification, storage, search ingestion, summarization, and reporting. With the Build Vision Agent skill, development begins with the desired outcome.

### Sample prompt [Scroll to Sample prompt section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#sample_prompt)

`Build a VSS vision agent for an orange juice bottling line. Use two RTSP cameras on the filler and capper. Detect bottle overflows and juice spills, verify each alert with the VLM, make alert clips searchable, and generate a shift report for the line supervisor.`

**What the agent assembles**

- VIOS-backed ingestion for RTSP cameras and recorded clips.
- Real-time detection, tracking, captioning, or VLM-based alerts, depending on the Foundation profile.
- Behavior analytics or rules for overflow, spill, and line-stoppage events.
- VLM verification that confirms alerts and explains its reasoning.
- Natural-language search across validated clips and indexed video.
- Summarization and reporting for operator handoff and incident review.
- Shared messaging, storage, APIs, and observability.

On a two-GPU RTX PRO 6000 Blackwell host, the skill combines search and alerts by reusing existing services and adding only an alert bridge and real-time VLM. FP8 Cosmos 3 Nano shares the detector’s GPU, avoiding duplication. A recorded alerts build reached a live, previewable deployment in under 30 minutes.

The result is a reusable pattern: ingest video once, share evidence across workflows, and give operators natural-language search, alerts, summaries, and reports.

## How adaptive EVS reduces operating cost [Scroll to How adaptive EVS reduces operating cost section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#how_adaptive_evs_reduces_operating_cost)

Once the bottling line agent from the example above is running, its cameras keep producing video around the clock, and most of each frame never changes: the filler, the guards, the floor. Only the bottles moving through it do, and an overflow is rare.

Every frame window still becomes visual context for the VLM, so the model spends most of its compute re-reading regions that look exactly like the frame before. That VLM processing is one of the main runtime cost drivers in a deployed visual AI agent, and it is the cost Adaptive EVS goes after.

![A two-by-two grid of illustrated scenes: a traffic intersection, a warehouse loading dock, a retail store aisle, and a skate park. Each shows a quiet frame and an event frame with a strip of 40 token squares beneath. The intersection is empty at night and packed at rush hour; the dock is empty until a truck backs in; the aisle is still until a shopper reaches for an item; the skate park is empty until a skater does an ollie. Quiet frames keep two or three green tokens, event frames keep more than thirty. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/image4.gif)_Figure 3: Four scenes where most frames repeat the one before. Adaptive EVS spends VLM tokens on the events, not the waiting_

### What Adaptive EVS changes in the pipeline [Scroll to What Adaptive EVS changes in the pipeline section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#what_adaptive_evs_changes_in_the_pipeline)

- **Dynamic pruning.** Each patch is compared with the prior frame using cosine similarity; unchanged patches are dropped before reaching the language model.
- **Event-aware batching.** Token retention indicates activity: clips above about 70% are batched as events, those below about 30% are dropped or flushed, and the rest run normally.

![A six-frame filmstrip shows repeated patches removed from five quiet frames while the jumping-cat event retains most tokens. The count falls from 240 to 75, with the same model description. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/image1.gif)_Figure 4: Most frames repeat the one before them. Adaptive EVS keeps only the patches that changed, drops the quiet frames, keeps the event, and the VLM’s answer stays the same on a fraction of the tokens_

## Performance impact [Scroll to Performance impact section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#performance_impact)

On an NVIDIA RTX PRO 6000 Blackwell running Cosmos 3 Super FP8, Adaptive EVS:

- Cut alert contextualization latency 17%, from 1,021 ms to 844 ms, while similarly reducing token usage.
-  Increased concurrent real-time VLM streams 46%, from 13 to 19.
-  Summarized a 60-minute video in about half the time with 80% fewer VLM input tokens.

Results vary with scene motion, chunk length, and similarity threshold; benchmark representative footage before choosing production defaults.

Adaptive EVS is most useful when VLMs read many frames and produce short responses, as in dense captioning, long-video summarization, and alert verification. It offers less benefit for long outputs from few frames, runs inside the RT-VLM container rather than against remote endpoints, and is optional. Enable it in override.env, then benchmark accuracy, throughput, and latency on representative footage:

|     |
| --- |
| `VIA_EVS_SESSION=true`<br>`VLM_VIDEO_PRUNING_RATE=0.5             # 0.0 to 1.0; higher prunes more`<br>`VLLM_EVS_SIMILARITY_THRESHOLD=0.2` |

## Cost impact: What changes for teams [Scroll to Cost impact: What changes for teams section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#cost_impact_what_changes_for_teams)

- Lower integration effort through natural-language composition of multi-workflow applications.
- Less duplicate infrastructure across alerting, search, summarization, reporting, and Q&A.
- Higher GPU efficiency by pruning unchanged visual regions.
- Lower summarization and incident-review latency by skipping uneventful video.
- Easier extension through incremental deltas that reuse a running deployment.

Together, these changes reduce upfront development work and the GPU work required to process video with VLMs across environments and applications.

## Getting started With VSS 3.3 [Scroll to Getting started With VSS 3.3 section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#getting_started_with_vss_33)

1. Clone the VSS Blueprint repository and check out the branch containing the 3.3 skills.
2. Install the VSS skills in your coding agent’s standard skills directory.
3. Describe the desired agent, including video sources, workflows, and deployment constraints, or say “build a vision agent” for guidance.
4. Review the architecture diagram and \_builds/<name>/override.env, especially GPU placement, model endpoints, ports, storage, and security boundaries.
5. For RT-VLM workloads, enable Adaptive EVS, tune the pruning rate, and benchmark accuracy, throughput, and latency on representative video.
6. Deploy on a trusted, isolated network with authentication, TLS, rate limiting, and external controls.

**Example setup commands**

|     |
| --- |
| `git clone https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization.git`<br>`cd video-search-and-summarization` |

Ask your coding agent to install the skills:

|     |
| --- |
| `Read skills/README.md and every SKILL.md under skills/. Install each skill for this host`<br>`using the standard skills directory, symlinking rather than copying so a git pull keeps`<br>`them current.` |

After the skills are installed, you can start with a prompt such as:

|     |
| --- |
| `Build a VSS vision agent that combines alert verification, natural-language video search,`<br>`and hourly summarization for my warehouse cameras. Reuse existing Kafka and Elasticsearch`<br>`services where possible, and produce a deployment plan before running Docker Compose.` |

## Going further [Scroll to Going further section](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/\#going_further)

- Clone the [VSS Blueprint repository](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization)
- Install the [VSS Agent Skills](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization/tree/develop/skills/vss-build-vision-ai)
- Try the Build Vision Agent skill with the sample prompt above on your own cameras

[Discuss (0)](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/#entry-content-comments)

+5

Like

## Tags

[Computer Vision / Video Analytics](https://developer.nvidia.com/blog/category/computer-vision/) \| [Manufacturing](https://developer.nvidia.com/blog/recent-posts/?industry=Manufacturing) \| [Retail / Consumer Packaged Goods](https://developer.nvidia.com/blog/recent-posts/?industry=Retail+%2F+Consumer+Packaged+Goods) \| [Smart Cities / Spaces](https://developer.nvidia.com/blog/recent-posts/?industry=Smart+Cities+%2F+Spaces) \| [Cosmos](https://developer.nvidia.com/blog/recent-posts/?products=Cosmos) \| [Metropolis](https://developer.nvidia.com/blog/recent-posts/?products=Metropolis) \| [Nemotron](https://developer.nvidia.com/blog/recent-posts/?products=Nemotron) \| [Intermediate Technical](https://developer.nvidia.com/blog/recent-posts/?learning_levels=Intermediate+Technical) \| [featured](https://developer.nvidia.com/blog/tag/featured/) \| [VLMs](https://developer.nvidia.com/blog/tag/vlms/)

## About the Authors

![Avatar photo](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/cropped-Hassan-Headshot-262x262.webp)

**About Hassan Moustafa**


Hassan Moustafa is a technical marketing engineer on the NVIDIA Metropolis team, working at the intersection of video AI, physical AI, and agentic systems. His work spans VSS, Cosmos, and Physical AI Data Factory workflows, from model evaluation and synthetic data generation to deployment, performance sizing, and developer education.




[View all posts by Hassan Moustafa](https://developer.nvidia.com/blog/author/hmoustafa/)

![Avatar photo](https://developer-blogs.nvidia.com/wp-content/uploads/2021/06/Debraj-headshot-262x262.jpg)

**About Debraj Sinha**


Debraj Sinha is a Product Marketing Manager for Metropolis at NVIDIA, focusing on building smarter spaces around the world with AI-enabled video analytics. Debraj collaborates with partners ranging from startups to Fortune 500 companies to market AI applications that drive safety and efficiency gains. He holds an MBA degree from Haas School of Business, University of California, Berkeley and a Master's degree in Computer Science from Cornell University.




[View all posts by Debraj Sinha](https://developer.nvidia.com/blog/author/debrajsinha/)

![Avatar photo](https://developer-blogs.nvidia.com/wp-content/uploads/2024/07/Ashwani_pic-262x262.jpeg)

**About Ashwani Agarwal**


Ashwani Agarwal is a senior software engineer in the Intelligent Video Analytics group currently focusing on generative AI applications in video analytics. Ashwani has a work experience of over 5 years in the field of video analytics using AI. He completed his M.Sc. in electrical and computer engineering from Northeastern University, Boston.




[View all posts by Ashwani Agarwal](https://developer.nvidia.com/blog/author/ashwania/)

## Comments

### Start the discussion at [forums.developer.nvidia.com](https://forums.developer.nvidia.com/t/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/384704)

- [![](https://developer-blogs.nvidia.com/wp-content/uploads/2026/08/5370350-gtc26-berlin-mktg-kit-golden-ticket-email-footer-1360x180-copy.webp)](https://developer.nvidia.com/gtc-golden-ticket-contest)
- [![](https://developer-blogs.nvidia.com/wp-content/uploads/2026/08/5370463-gtc26-berlin-training-mktg-kit-email-footer-1360x180-copy.webp)](https://www.nvidia.com/gtc/)

ClosePrevious

![](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/)

![](https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/)

Next

- [L](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Flower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3%2F)
- [T](https://twitter.com/intent/tweet?text=Lower+the+Cost+of+Building+and+Running+Visual+AI+Agents+with+NVIDIA+VSS+Blueprint+3.3+%7C+NVIDIA+Technical+Blog+https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Flower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3%2F)
- [F](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Flower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3%2F)
- [R](https://www.reddit.com/submit?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Flower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3%2F&title=Lower+the+Cost+of+Building+and+Running+Visual+AI+Agents+with+NVIDIA+VSS+Blueprint+3.3+%7C+NVIDIA+Technical+Blog)
- [E](mailto:?subject=I%27d%20like%20to%20share%20a%20link%20with%20you&body=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Flower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3%2F)

- [Join](https://developer.nvidia.com/login)