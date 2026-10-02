[Technical Blog](https://developer.nvidia.com/blog)

[Subscribe](https://developer.nvidia.com/email-signup)

[Related Resources](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/#main-content-end)

[Computer Vision / Video Analytics](https://developer.nvidia.com/blog/category/computer-vision/)

English中文

# Integrating Context-Aware Video AI Agents Into Enterprise Workflows

![](https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/nvidia-metropolis-nemoclaw-1024x576.png)

Jul 16, 2026


By [Ilyas Bankole-Hameed](https://developer.nvidia.com/blog/author/ibankole/ "Posts by Ilyas Bankole-Hameed"), [Adam Ryason](https://developer.nvidia.com/blog/author/aryason/ "Posts by Adam Ryason"), [Zac Wang](https://developer.nvidia.com/blog/author/zacw/ "Posts by Zac Wang") and [Peter Chang](https://developer.nvidia.com/blog/author/pechang/ "Posts by Peter Chang")

+14

Like

[Discuss (0)](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/#entry-content-comments)

- [L](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintegrating-context-aware-video-ai-agents-into-enterprise-workflows%2F)
- [T](https://twitter.com/intent/tweet?text=Integrating+Context-Aware+Video+AI+Agents+Into+Enterprise+Workflows+%7C+NVIDIA+Technical+Blog+https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintegrating-context-aware-video-ai-agents-into-enterprise-workflows%2F)
- [F](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintegrating-context-aware-video-ai-agents-into-enterprise-workflows%2F)
- [R](https://www.reddit.com/submit?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintegrating-context-aware-video-ai-agents-into-enterprise-workflows%2F&title=Integrating+Context-Aware+Video+AI+Agents+Into+Enterprise+Workflows+%7C+NVIDIA+Technical+Blog)
- [E](mailto:?subject=I%27d%20like%20to%20share%20a%20link%20with%20you&body=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintegrating-context-aware-video-ai-agents-into-enterprise-workflows%2F)

## AI-Generated Summary

- [NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/) orchestrates the Video Search and Summarization and Retrieval-Augmented Generation blueprints to turn video analysis into coordinated actions such as ticket creation and workflow routing.
- The VSS agent uses human-in-the-loop prompts to capture user intent, retrieves organizational knowledge through the RAG Blueprint, and generates structured, timestamped reports with citations and recommended actions.
- In a healthy eating coach demonstration, NemoClaw processes a meal preparation video, enriches the analysis with nutritional guidelines, and automatically creates a Jira ticket that tracks dietary adjustments to completion.
- Partner deployments show the pipeline reducing footage-to-work-order time from 30–45 minutes to roughly 19 seconds for predictive maintenance and enabling real-time video analytics on the VAST DataEngine.
- The integrated solution delivers enterprise-grade video AI with faster response times, consistent application of reference knowledge, full traceability from evidence to decision, and automation of routine workflows.

### Next Steps

- Clone the [VSS repository](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization) to deploy the agent with knowledge retrieval enabled.
- Run the [NVIDIA Blueprints](https://build.nvidia.com/blueprints) installer to set up NemoClaw and connect it to your existing systems such as Jira or Slack.

Powered by NVIDIA Nemotron. AI-generated content may summarize information incompletely. Verify important information. [Learn more](https://www.nvidia.com/en-us/agreements/trustworthy-ai/terms/)

A video analytics [AI agent](https://www.nvidia.com/en-us/ai/) that can perceive, reason, and act based on massive amounts of video footage must be integrated with existing workflows and applications to be useful. These include content management systems, messaging platforms, databases, ticket queue, and escalation paths.

This integration is challenging because video systems, enterprise knowledge bases, and operational tools are usually siloed. Developers need to capture user intent, retrieve the correct organizational context, generate structured reports, and route findings into downstream systems.

In a [previous post](https://developer.nvidia.com/blog/make-sense-of-video-analytics-by-integrating-nvidia-ai-blueprints/), we explained how to enrich video analysis with document knowledge using NVIDIA Blueprints. This post continues with the topic and explains how to unlock the ability to not just analyze video, but to programmatically act on those analyses by introducing NVIDIA NemoClaw. You’ll learn how to:

- Extend VSS for guided, context-aware video analysis
- Orchestrate the VSS and RAG blueprints as a composable service using NVIDIA NemoClaw
- Generate structured reports enriched with organizational and reference knowledge
- Build multistep workflows where video analysis feeds into other business processes
- Deploy and scale this solution across enterprise environments

This approach is the next step in context-aware video AI agents, which involves moving from “What does this video show?” to “What should we do about what this video shows, and how do we coordinate that action at scale?”

## What are NVIDIA NemoClaw and NVIDIA Blueprints? [Scroll to What are NVIDIA NemoClaw and NVIDIA Blueprints? section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#what_are_nvidia_nemoclaw_and_nvidia_blueprints)

[NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/) is a collection of open blueprints for building autonomous agents. It enables the ecosystem to build domain-specialized, always-on agents that are safer, faster, and operate more cost efficiently across digital and physical workflows.

[NVIDIA Blueprints](https://build.nvidia.com/blueprints) are customizable reference workflows for building [agentic AI](https://www.nvidia.com/en-us/glossary/ai-agents/) pipelines at enterprise scale. They combine specialized microservices, optimized models, and composable APIs to accelerate time-to-value while maintaining modularity. In addition to NemoClaw, the main blueprints used in this post are:

- [NVIDIA Metropolis Blueprint for Video Search and Summarization (VSS)](https://build.nvidia.com/nvidia/video-search-and-summarization) ingests streaming or archival video, generates captions and visual metadata, and supports semantic search, interactive Q&A, and event summarization.
- [NVIDIA AI Blueprint for Retrieval-Augmented Generation (RAG)](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline) indexes proprietary enterprise documents—manuals, policies, regulations, SOPs, and reference data—into a GPU-accelerated vector store for fast semantic search.

## How does VSS capture intent, retrieve knowledge, and generate reports from video? [Scroll to How does VSS capture intent, retrieve knowledge, and generate reports from video? section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#how_does_vss_capture_intent_retrieve_knowledge_and_generate_reports_from_video)

VSS provides guided, context-aware video analysis through a set of tools built into the agent. Human-in-the-loop (HITL) prompts capture what the user wants before any processing begins. The agent retrieves the relevant organizational knowledge and produces a structured, timestamped report.

When combined with [NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/) blueprints for building autonomous agents, this system can go beyond simple video analysis to programmatically act on those analyses. This unlocks the ability to generate tickets, compare patterns across multiple sources, draft revised procedures, escalate anomalies, and feed results into downstream workflows.

Three agent tools work together to make this happen:

- **Long video summary (LVS)** **video understanding tool:** Performs long video summarization with mandatory HITL parameter collection. Users interactively specify the scenario (what the video is about), events of interest (what to detect), objects of focus (what to track), and an optional knowledge-retrieval query.
- **Knowledge retrieval (frag) tool:** Calls the RAG Blueprint to retrieve organization-specific context from documents, policies, reference data, and knowledge bases. The RAG Blueprint handles embedding, reranking, and vector search internally.
- **Report generation tool:** Produces a structured report combining the video analysis with the retrieved context, complete with timestamps, narrative analysis, and citations. It can use HITL to let the user confirm or edit the prompt before the report is generated.

Together, these tools collect user intent through HITL, query the RAG Blueprint for contextual knowledge, process the video with that context, and hand off to the report generation tool for formatted output.

## Generating assessments and recommended actions from a video [Scroll to Generating assessments and recommended actions from a video section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#generating_assessments_and_recommended_actions_from_a_video)

To demonstrate this process, we will create a “healthy eating coach” that analyzes food videos to assess a user’s eating habits and return concrete, tracked next steps they can act on. The process is detailed in the following sections.

### User uploads a video and specifies what to analyze [Scroll to User uploads a video and specifies what to analyze section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#user_uploads_a_video_and_specifies_what_to_analyze)

To start, a user uploads a meal preparation video through the VSS interface (Figure 1).

![Screenshot of the VSS web interface showing an upload panel where a user can drag and drop or browse to select a breakfast video file to ingest into the system. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/nvidia-vss-blueprint-user-interface.webp)_Figure 1. In the VSS user interface, you can drag and drop a video to upload it into the system_

NemoClaw then begins the workflow. It reads the vss-generate-video-report-rag skill definition (SKILL.md) to learn which parameters the analysis needs and hands the request to the VSS agent, which walks the user through a short series of HITL prompts in their terminal (Figure 2).

![Screenshot of a terminal session in which the user answers NemoClaw’s human-in-the-loop prompts, specifying the scenario, events, objects, and reference knowledge to retrieve before the video is analyzed. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/guided-hitl-interaction-nemoclaw.webp)_Figure 2. The guided NemoClaw HITL interaction that captures intent before processing begins on the user-side terminal_

The prompts ask what to analyze, the scenario, the events of interest, the objects to track, and an optional RAG Blueprint query for the reference knowledge to retrieve, such as the nutritional or regulatory guidelines. Capturing this intent up front scopes the analysis to what the user actually cares about before any video is processed. For automated batch runs, these answers can be supplied programmatically instead of interactively.

### NemoClaw orchestrates VSS and the RAG Blueprint [Scroll to NemoClaw orchestrates VSS and the RAG Blueprint section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#nemoclaw_orchestrates_vss_and_the_rag_blueprint)

Next, with the parameters confirmed, NemoClaw orchestrates the pipeline. The LVS video understanding tool first queries the RAG Blueprint for the relevant nutritional guidelines, and the RAG Blueprint returns the matching reference documents, handling the vector search internally.

It then passes those parameters, the video, and the retrieved context to the LVS service, which summarizes the video hierarchically and weaves the reference knowledge into its findings. The report generation tool combines the result into a structured, timestamped report that includes detected events with timestamps, a narrative analysis grounded in the reference material, citations to the relevant source documents, and concrete recommended actions.

Figure 3 shows this orchestration in the NemoClaw terminal, including the agent’s reasoning and tool calls.

![Screenshot of the NemoClaw terminal displaying the agent’s reasoning trace and tool calls as it orchestrates the pipeline, invoking VSS for video analysis and the RAG Blueprint to retrieve nutritional guidelines. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/nemoclaw-terminal-vss-rag-blueprint-agent-calls.webp)_Figure 3. The NemoClaw terminal shows the orchestration of VSS and the RAG Blueprint, including the agent’s reasoning and tool calls_

### NemoClaw creates a Jira ticket [Scroll to NemoClaw creates a Jira ticket  section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#nemoclaw_creates_a_jira_ticket%C2%A0)

NemoClaw reads the finished report and turns it into coordinated action. It presents the completed analysis with links to the Markdown and PDF reports and the video playback, a summary of why the meal is healthy, and recommended next steps (Figure 4). It then automatically creates a Jira ticket that summarizes the findings and the recommended dietary adjustments, with an appropriate priority and assignment so the action items are tracked to completion (Figure 5).

![Screenshot of the NemoClaw terminal after the breakfast analysis completes. It lists download links for a Markdown report, a PDF report, and the video playback, then explains why the breakfast is healthy (minimally processed ingredients, whole grains such as oats, good hygiene practices) and lists actionable next steps, ending with a note that it will now create a Jira ticket. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/nemoclaw-video-analysis-recommended-next-steps.webp)_Figure 4. The NemoClaw terminal presents the completed video analysis, with links to the Markdown and PDF reports and the video playback, a summary, and recommended next steps before the Jira ticket is created_

![Screenshot of a Jira ticket created automatically by NemoClaw. The ticket summarizes the video findings and lists recommended dietary next steps, with a priority and an assignee so the action items are tracked to completion. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/jira-ticket.webp)_Figure 5. The Jira ticket is automatically generated by NemoClaw, summarizing the findings and recommended next steps_

This downstream step generalizes well beyond Jira. Depending on what the report contains, NemoClaw can also:

- Create tickets for the findings, with the right priority and assignment.
- Escalate or summarize patterns that emerge across multiple runs.
- Bundle supporting evidence for review or compliance.
- Route gaps to the appropriate follow-up workflow.

At this point, the report is no longer a static document. It becomes the trigger for coordinated action across the systems your team already uses.

Figure 6 shows the architecture in four layers:

- **Orchestration:** The NemoClaw agent, the vss-generate-video-report-rag skill, and the HITL prompts
- **VSS agent:** Tools include video I/O, search, understanding, LVS, knowledge retrieval, and report generation. Knowledge retrieval is part of the agent, not a separate extension
- **RAG Blueprint:** NVIDIA RAG API, Milvus vector database, [NVIDIA Nemotron reranking NIM](https://build.nvidia.com/models?q=rerank), and the indexed reference and organizational documents
- **LLM fusion:** Enrichment of the VSS-provided summary with the context retrieved through the RAG Blueprint

Data flows downward through the system, with the agent’s tools orchestrating calls to the LVS service and the RAG Blueprint, both of which feed into the report generation tool for final output.

![Layered architecture diagram with NemoClaw at the top orchestrating the vss-frag skill, the VSS Agent core and its frag tools, and the RAG Blueprint. Arrows show data flowing from orchestration through video analysis and retrieval into report generation. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/architecture-vss-rag-blueprint-nemoclaw.webp)_Figure 6. Architecture of VSS 3.1 and the RAG Blueprint orchestrated by NemoClaw_

## How to deploy the VSS agent with knowledge retrieval [Scroll to How to deploy the VSS agent with knowledge retrieval section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#how_to_deploy_the_vss_agent_with_knowledge_retrieval)

Follow the steps below to implement the solution for your own workflow.

### Prerequisites [Scroll to Prerequisites section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#prerequisites)

- NVIDIA GPU(s) with at least 24 GB VRAM
- Docker Engine plus Docker Compose v2
- NGC API key ( [ngc.nvidia.com](http://ngc.nvidia.com/))
- NVIDIA Build API key ( [build.nvidia.com](http://build.nvidia.com/))
- RAG Blueprint deployed and reachable from the agent (its server URL accessible), and its collection name
- NemoClaw installed (for programmatic access)

### Step 1: Clone the VSS repo and authenticate with NGC [Scroll to Step 1: Clone the VSS repo and authenticate with NGC section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#step_1_clone_the_vss_repo_and_authenticate_with_ngc)

|     |
| --- |
| `git clone https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization.git ~/vss-public`<br>`cd ~/vss-public`<br>`echo "$NGC_CLI_API_KEY" | docker login nvcr.io --username '$oauthtoken' --password-stdin` |

### Step 2: Configure the environment [Scroll to Step 2: Configure the environment section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#step_2_configure_the_environment)

Edit the LVS profile .env file, `deploy/docker/developer-profiles/dev-profile-lvs/.env`. All the variables exist in that file, except the `RAG_ values`, which the agent’s RAG config reads and you add yourself.

|     |
| --- |
| `# Deployment selection`<br>`MODE=2d`<br>`BP_PROFILE=bp_developer_lvs`<br>`HARDWARE_PROFILE=H100         # H100, L40S, RTXPRO4500BW, RTXPRO6000BW, DGX-SPARK, IGX-THOR, AGX-THOR, or OTHER`<br>``<br>`# LLM / VLM placement`<br>`LLM_MODE=local_shared         # local_shared runs LLM and VLM on one GPU; use 'local' for separate GPUs`<br>`VLM_MODE=local_shared`<br>`LLM_DEVICE_ID='0'`<br>`VLM_DEVICE_ID='0'`<br>``<br>`# Paths (you MUST set these)`<br>`VSS_APPS_DIR="<PATH>/vss-public/deploy/docker"`<br>`VSS_DATA_DIR="<PATH>/vss-apps-data"`<br>`HOST_IP='<YOUR_IP>'`<br>``<br>`# Agent image + config`<br>`VSS_AGENT_VERSION=3.2.0`<br>`# Enable knowledge retrieval (frag): point at config_rag.yml (default config.yml has it off)`<br>`VSS_AGENT_CONFIG_FILE=./deploy/docker/developer-profiles/dev-profile-lvs/vss-agent/configs/config_rag.yml`<br>``<br>`# Credentials`<br>`NGC_CLI_API_KEY='nvapi-...'`<br>`NVIDIA_API_KEY='nvapi-...'`<br>``<br>`# RAG Blueprint connection (read by config_rag.yml)`<br>`RAG_SERVER_URL='http://<RAG_SERVER>:8081/v1'`<br>`RAG_API_KEY='<YOUR_RAG_API_KEY>'`<br>`KNOWLEDGE_COLLECTION='<YOUR_COLLECTION>'` |

Setting `VSS_AGENT_CONFIG_FILE` to `config_rag.yml` enables the frag knowledge-retrieval tool. Those three RAG\_ values are the only RAG settings the agent needs: it calls the RAG server’s search endpoint, and the RAG Blueprint handles embedding, reranking, and vector search internally. Configure the vector database, embedding, and reranker on the RAG Blueprint deployment itself, following its own documentation.

### Step 3: Deploy the VSS stack [Scroll to Step 3: Deploy the VSS stack section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#step_3_deploy_the_vss_stack)

Create the data directories the bind mounts need, then bring up the stack. The compose profile is selected automatically from `COMPOSE_PROFILES` in the .env file.

|     |
| --- |
| `export VSS_DATA_DIR=<PATH>/vss-apps-data`<br>`mkdir -p "$VSS_DATA_DIR"/data_log/{elastic/data,elastic/logs,kafka,redis/data,redis/log}`<br>`chmod -R 777 "$VSS_DATA_DIR/data_log"`<br>``<br>`cd ~/vss-public/deploy/docker`<br>`docker compose \`<br>```--env-file developer-profiles/dev-profile-lvs/.env \`<br>```-f compose.yml \`<br>```up -d` |

The compose stack starts all infrastructure (VST, Redis, Elasticsearch, LVS, NIM) and the agent using the RAG-enabled config. The dev-profile helper, `./deploy/docker/scripts/dev-profile.sh up --profile lvs --hardware-profile H100`, does the same and creates the data directories for you.

### Step 4: Verify that the services are healthy [Scroll to Step 4: Verify that the services are healthy section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#step_4_verify_that_the_services_are_healthy)

Note that the NIM may take 5 to 15 minutes to load.

|     |
| --- |
| `docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'`<br>`curl -sS http://localhost:8000/health       # VSS agent`<br>`curl -f http://127.0.0.1:38111/v1/ready         # LVS backend`<br>`curl -f http://127.0.0.1:8018/v1/health/ready   # RT-VLM`<br>`curl -f http://127.0.0.1:30081/v1/health/ready  # LLM NIM` |

## NemoClaw setup [Scroll to NemoClaw setup section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#nemoclaw_setup)

NemoClaw acts as the orchestration layer, configuring the sandbox, network policy and skill so it can drive the full workflow.

### Step 1: Run the NemoClaw installer [Scroll to Step 1: Run the NemoClaw installer  section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#step_1_run_the_nemoclaw_installer%C2%A0)

From the repo root; `NEMOCLAW_PROVIDER` is required; use `build` for NVIDIA-hosted models.

|     |
| --- |
| `NEMOCLAW_PROVIDER=build \`<br>`NVIDIA_API_KEY="$NVIDIA_API_KEY" \`<br>```bash deploy/docker/scripts/nemoclaw/init_nemoclaw.sh demo` |

This single command handles the full setup: it onboards NemoClaw, configures the model provider, applies the VSS sandbox policy (which grants the sandbox access to the VSS agent on port 8000), installs the repo skills—including vss-generate-video-report-rag—into the sandbox as an OpenClaw plugin, and prints the OpenClaw UI URL.

To use your own OpenAI-compatible endpoint instead (for example a local vLLM):

|     |
| --- |
| `NEMOCLAW_PROVIDER=custom with NEMOCLAW_ENDPOINT_URL and COMPATIBLE_API_KEY` |

### Step 2: Test the end-to-end workflow [Scroll to Step 2: Test the end-to-end workflow section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#step_2_test_the_end-to-end_workflow)

|     |
| --- |
| `nemoclaw SANDBOX_NAME connect`<br>`openclaw tui` |

The OpenClaw UI is now open. The next two actions happen inside that UI, not in your shell:

1. Type /new and press Enter to start a fresh session.
2. Type your request as a message and press Enter: I want to generate a video summary report for `<VIDEO_NAME>`.

The agent then collects the analysis parameters through the HITL prompts, generates the report with LVS and the RAG Blueprint, and can create a Jira ticket or send notifications based on the results.

## Latency and performance of the end-to-end pipeline [Scroll to Latency and performance of the end-to-end pipeline section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#latency_and_performance_of_the_end-to-end_pipeline)

Adding NemoClaw orchestration and HITL parameter collection introduces minimal latency overhead. The HITL phase is asynchronous—NemoClaw and human users interact while the system stands by—so once parameters are confirmed, video processing proceeds.

![Horizontal bar chart titled "Runtime % by Component" showing VSS video analysis accounting for about 92% of end-to-end runtime, with NemoClaw at roughly 5.7%, Enterprise-RAG retrieval at 1.3%, and LLM fusion at 1.0%. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/runtime-percentage-percentage-video-analysis-jira-pipeline.webp)_Figure 7. Runtime percentage by system component for the video analysis to Jira action-item pipeline_

## How are industries and NVIDIA partners using NemoClaw, VSS 3, and the RAG Blueprint? [Scroll to How are industries and NVIDIA partners using NemoClaw, VSS 3, and the RAG Blueprint? section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#how_are_industries_and_nvidia_partners_using_nemoclaw_vss_3_and_the_rag_blueprint)

The combination of video understanding, knowledge retrieval, and agentic orchestration unlocks new capabilities across industries. Here is how partners are deploying this solution.

- [**Computacenter**](https://www.computacenter.com/en-us) deployed the full DETECT → REASON → ACT pipeline on a Run:AI cluster for predictive maintenance, using VSS 3 to analyze drone, borescope, and thermal inspection footage, RAG Blueprint for OEM context, and NemoClaw to auto-draft Maximo work orders—cutting footage-to-work-order time from 30–45 minutes to roughly 19 seconds across four asset classes.
- [**VAST Data**](https://www.vastdata.com/) uses NemoClaw to orchestrate a real-time VSS pipeline on the VAST DataEngine, processing live game streams with VAST RAG over VastDB and vectors; built on the NVIDIA blueprint with cosmos-reason2 and Nemotron, it runs end-to-end on NVIDIA DSX AIR.

## What are the benefits of actionable video AI? [Scroll to What are the benefits of actionable video AI? section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#what_are_the_benefits_of_actionable_video_ai)

The integration of VSS 3, RAG Blueprint, and NemoClaw represents a fundamental shift in how enterprises can approach video analytics. Video analysis has typically produced static reports. Understanding what happened in a video required manual interpretation and manual action initiation.

With this integrated solution, video understanding is now a starting point. Agentic orchestration translates that understanding into coordinated action—creating tickets, alerting teams, comparing patterns, escalating anomalies, and feeding results into downstream workflows.

The implications are significant:

- **Speed:** Response time drops from hours or days to minutes.
- **Scale:** Analyze thousands of videos across multiple sources and surface enterprise-wide patterns.
- **Consistency:** Reference knowledge (policies, procedures, regulations, guidelines) is consistently applied.
- **Accountability:** Every decision is traced back to video evidence and source documents.
- **Automation:** Routine workflows (alert generation, ticket creation, documentation) run without manual intervention.

This is what enterprise-grade video AI looks like: specialized analysis engines (the VSS and RAG blueprints) composed into general-purpose agentic workflows (NemoClaw) that embed organizational intelligence into every decision.

## Get started with actionable, enterprise-grade video AI [Scroll to Get started with actionable, enterprise-grade video AI section](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/\#get_started_with_actionable_enterprise-grade_video_ai)

Together, VSS, RAG Blueprint, and NemoClaw illustrate a broader architectural principle: no single model or service is optimal for every problem, but specialized systems composed through clean, well-defined APIs can deliver capabilities that exceed the sum of their parts. This can be done without sacrificing the modularity, scalability, and governance that enterprise deployments demand.

The result reframes what video analytics is for. Rather than terminating in a static report that waits on human interpretation, video understanding becomes the entry point to an orchestrated workflow—one that retrieves the relevant organizational knowledge, grounds every conclusion in evidence, and drives downstream action automatically.

Enterprises can act on video insights as quickly as they can generate them, consistently and at scale. The footage is already being captured. The next opportunity is to turn it into coordinated, accountable action, and the blueprints to do so are now available. Ready to get started? Use the steps presented in this post, swapping in your own video source and reference knowledge, such as inspection footage paired with OEM manuals, retail floor cameras paired with merchandising policies, or live broadcasts paired with a rulebook.

[Clone the VSS repo](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization), deploy the VSS agent with knowledge retrieval (frag) enabled, point the RAG Blueprint at your documents, and connect NemoClaw to the system your team already uses, such as Jira, Slack, a database or a ticket queue. Start with one recurring loop from video to decision to action, pilot it end-to-end, and expand from there.

[Discuss (0)](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/#entry-content-comments)

+14

Like

## Tags

[Agentic AI / Generative AI](https://developer.nvidia.com/blog/category/generative-ai/) \| [Computer Vision / Video Analytics](https://developer.nvidia.com/blog/category/computer-vision/) \| [Developer Tools & Techniques](https://developer.nvidia.com/blog/category/development/) \| [General](https://developer.nvidia.com/blog/recent-posts/?industry=General) \| [Blueprint](https://developer.nvidia.com/blog/recent-posts/?products=Blueprint) \| [Metropolis](https://developer.nvidia.com/blog/recent-posts/?products=Metropolis) \| [Intermediate Technical](https://developer.nvidia.com/blog/recent-posts/?learning_levels=Intermediate+Technical) \| [Tutorial](https://developer.nvidia.com/blog/recent-posts/?content_types=Tutorial) \| [AI Agent](https://developer.nvidia.com/blog/tag/ai-agent/) \| [featured](https://developer.nvidia.com/blog/tag/featured/) \| [NemoClaw](https://developer.nvidia.com/blog/tag/nemoclaw/) \| [Retrieval Augmented Generation (RAG)](https://developer.nvidia.com/blog/tag/retrieval-augmented-generation-rag/) \| [Video Analytics](https://developer.nvidia.com/blog/tag/tracking-video-analytics/)

## About the Authors

![Avatar photo](https://developer-blogs.nvidia.com/wp-content/uploads/2025/11/ilyas-square-262x262.jpg)

**About Ilyas Bankole-Hameed**


Ilyas is a senior generative AI solutions architect at NVIDIA, where he pushes the boundaries of what's possible with AI. His passion lies in training, fine-tuning, optimizing AI models, and building architectures that take on real-world challenges. He holds a Master’s in Artificial Intelligence from Carnegie Mellon University’s School of Computer Science, and is driven by the belief that technology should solve meaningful problems and make a lasting impact. At heart, he's a builder, actively searching for the next breakthrough that will change the world for the better.




[View all posts by Ilyas Bankole-Hameed](https://developer.nvidia.com/blog/author/ibankole/)

![Avatar photo](https://developer-blogs.nvidia.com/wp-content/uploads/2025/04/Adam-Ryason-262x262.jpg)

**About Adam Ryason**


Adam Ryason is a product manager on the NVIDIA Metropolis team and leads the AI Blueprint for Video Search and Summarization project. An experienced startup founder and researcher, his background consists of vision-based AI, digital twins, and human-computer interaction. He holds a Ph.D. in mechanical engineering from Rensselaer Polytechnic Institute.




[View all posts by Adam Ryason](https://developer.nvidia.com/blog/author/aryason/)

![Avatar photo](https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/cropped-zac-wang-262x262.webp)

**About Zac Wang**


Zac Wang is a principal software engineer working on building vision agents and agentic software for video search and summarization. Zac obtained a BE degree from Tsinghua University Beijing and a master's degree from Johns Hopkins University. His technical focus is agentic AI and systems.




[View all posts by Zac Wang](https://developer.nvidia.com/blog/author/zacw/)

![Avatar photo](https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/cropped-peter-chang-262x262.webp)

**About Peter Chang**


Peter Chang is a senior software engineer working on deep research agentic AI at NVIDIA. His industry experience covers a wide breadth of technologies and industries; including telecom, gaming, finance, and ML/agentic AI. Peter holds a BS in Computer Science from the University of Colorado, Boulder, and an MS in Computer Science and Technology from Hanyang University in Seoul, South Korea.




[View all posts by Peter Chang](https://developer.nvidia.com/blog/author/pechang/)

## Comments

### Start the discussion at [forums.developer.nvidia.com](https://forums.developer.nvidia.com/t/integrating-context-aware-video-ai-agents-into-enterprise-workflows/377081)

- [![](https://developer-blogs.nvidia.com/wp-content/uploads/2026/08/5370350-gtc26-berlin-mktg-kit-golden-ticket-email-footer-1360x180-copy.webp)](https://developer.nvidia.com/gtc-golden-ticket-contest)
- [![](https://developer-blogs.nvidia.com/wp-content/uploads/2026/08/5370463-gtc26-berlin-training-mktg-kit-email-footer-1360x180-copy.webp)](https://www.nvidia.com/gtc/)

ClosePrevious

![](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/)

![](https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/)

Next

- [L](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintegrating-context-aware-video-ai-agents-into-enterprise-workflows%2F)
- [T](https://twitter.com/intent/tweet?text=Integrating+Context-Aware+Video+AI+Agents+Into+Enterprise+Workflows+%7C+NVIDIA+Technical+Blog+https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintegrating-context-aware-video-ai-agents-into-enterprise-workflows%2F)
- [F](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintegrating-context-aware-video-ai-agents-into-enterprise-workflows%2F)
- [R](https://www.reddit.com/submit?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintegrating-context-aware-video-ai-agents-into-enterprise-workflows%2F&title=Integrating+Context-Aware+Video+AI+Agents+Into+Enterprise+Workflows+%7C+NVIDIA+Technical+Blog)
- [E](mailto:?subject=I%27d%20like%20to%20share%20a%20link%20with%20you&body=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintegrating-context-aware-video-ai-agents-into-enterprise-workflows%2F)

- [Join](https://developer.nvidia.com/login)