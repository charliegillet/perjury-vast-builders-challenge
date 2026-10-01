[Skip to main content](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html#main-content)

Back to top`⌘` + `K`

[![VSS - Home](https://docs.nvidia.com/vss/latest/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg)![VSS - Home](https://docs.nvidia.com/vss/latest/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg)\\
VSS](https://docs.nvidia.com/vss/latest/index.html)

3.2.1

[3.2.1](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html) [3.2.0](https://docs.nvidia.com/vss/3.2.0/agent-workflow-lvs.html) [3.1.0](https://docs.nvidia.com/vss/3.1.0/agent-workflow-lvs.html) [3.0.0](https://docs.nvidia.com/vss/3.0.0/agent-workflow-lvs.html) [2.4.1](https://docs.nvidia.com/vss/2.4.1/agent-workflow-lvs.html) [2.4.0](https://docs.nvidia.com/vss/2.4.0/agent-workflow-lvs.html) [2.3.1](https://docs.nvidia.com/vss/2.3.1/agent-workflow-lvs.html) [2.3.0](https://docs.nvidia.com/vss/2.3.0/agent-workflow-lvs.html) [2.2.0](https://docs.nvidia.com/vss/2.2.0/agent-workflow-lvs.html)

LightDarkSystem Settings

# Video Summarization Workflow [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#video-summarization-workflow "Link to this heading")

The Video Summarization Workflow enables analysis and summarization of video content without being constrained by the standard VLM context window limitations, allowing for the analysis of long-form video content.

**Capabilities**

- Summarize uploaded videos that are longer than the standard VLM context window.

- Generate reports for one or more uploaded videos.

- Configure live streams for caption generation (experimental).

- Summarize live streams over a time range (experimental).

- Generate reports for live streams over a time range (experimental).

- Ask questions over stored stream captions and events (experimental).

- Review extracted events in the Kibana dashboard.


**Use Cases**

- Automated incident report generation

- Event detection in extended video archives

- Shift summaries and daily activity reports

- Question answering over captioned live streams (experimental)


**Technical Approach**

Standard VLMs are limited to processing short video clips, usually less than 1 minute, depending on the number of subsampled frames and level of detail required. This workflow uses the Video Summarization microservice to segment longer videos, analyze each segment with a VLM, and synthesize the results into coherent summaries with timestamped events. For live streams, the workflow can store VLM captions and events so the agent can answer later questions or generate stream summaries. Stream summary and stored-caption Q&A are experimental.

**Estimated Deployment Time:** 15-20 minutes

The following diagram illustrates the video summarization architecture:

![Vision Agent with Video Summarization Architecture](https://docs.nvidia.com/vss/latest/_images/profile-lvs-arch.png)

**Key Features of the Vision Agent with Video Summarization:**

- Generate narrative summaries for uploaded video files.

- Generate reports for a single uploaded video or for multiple uploaded videos in one request.

- Formulate timestamped highlights based on user-defined events.

- Configure live streams for caption generation with a monitoring scenario, events, and optional objects of interest (experimental).

- Summarize live streams, generate reports, and answer questions using stored captions and events (experimental).

- Return results through the AI agent interface.


## What’s being deployed [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#what-s-being-deployed "Link to this heading")

- **VSS Agent:** Agent service that uses a configured LLM endpoint to route requests and orchestrate tool calls to VSS microservices and model endpoints (LLM/VLM NIMs) to answer questions and generate outputs

- **VSS Agent UI:** Web UI with chat, video upload, and different views

- **VSS Video IO & Storage (VIOS):** Video ingestion, recording, and playback services used by the agent for video access and management

- **Nemotron LLM (NIM):** LLM inference service used for reasoning, tool selection, and response generation

- **Cosmos3 Nano Reasoner (NIM):** Vision-language model with physical reasoning capabilities

- **RTVI-VLM:** Real-Time Video Intelligence VLM service used by the Video Summarization profile for VLM calls

- **VSS Video Summarization:** Microservice for segmenting and summarizing video content (uploaded files of any length, plus RTSP live streams)

- **Kafka:** Message bus used for stream caption and summary events

- **ELK:** Elasticsearch, Logstash, and Kibana stack for storing and reviewing Video Summarization events and captions

- **Phoenix:** Observability and telemetry service for agent workflow monitoring


## Prerequisites [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#prerequisites "Link to this heading")

Before you begin, ensure all of the prerequisites are met. See [Prerequisites](https://docs.nvidia.com/vss/latest/prerequisites.html) for more details.

## Deploy [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#deploy "Link to this heading")

Note

For instructions on downloading sample data and the deployment package, see [Download Sample Data and Deployment Package](https://docs.nvidia.com/vss/latest/quickstart.html#quickstart-download-sample-data-and-package) in the Quickstart guide.

### With Agent Skills [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#with-agent-skills "Link to this heading")

#### Step 1: Deploy the Agent [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#step-1-deploy-the-agent "Link to this heading")

Use VSS Agent Skills from an agent such as Claude Code, Codex, or NemoClaw to deploy and operate the video summarization workflow.
First, install the `vss-deploy-profile` skill as described in [Agent Skills](https://docs.nvidia.com/vss/latest/agent-skills.html#agent-skills) and make it
accessible to your agent. The host must meet the same deployment requirements listed above (supported GPU/hardware for that profile)
and must meet the [Prerequisites](https://docs.nvidia.com/vss/latest/prerequisites.html).

The `vss-deploy-profile` skill will choose the `<platform>` and `<mode>` to match your system, as detailed in [Development Profile GPU Requirements](https://docs.nvidia.com/vss/latest/prerequisites.html#vss-development-profile-gpu-requirements).
Refer to the requirements table for valid platform and mode combinations compatible with your hardware.

Deploy prompt structure [#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html#id3 "Link to this code")

```
Deploy the VSS video summarization profile (lvs).
```

Copy to clipboard

What the agent does:

1. Loads the `vss-deploy-profile` skill and detects the repository, GPU hardware, and host networking values.

2. Validates required credentials (such as `NGC_CLI_API_KEY`) and prompts you if any are missing.

3. Selects the `lvs` profile and a platform and mode that fit your hardware, then builds the deployment configuration.

4. Reviews the configuration with you, then deploys the containers.

5. Waits until all services are healthy and returns the agent UI endpoint.


#### Step 2: Upload a Video [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#step-2-upload-a-video "Link to this heading")

To operate the video summarization and report generation workflow from your agent, install the `vss-manage-video-io-storage`, `vss-summarize-video`, and `vss-generate-video-report` skills as described in [Agent Skills](https://docs.nvidia.com/vss/latest/agent-skills.html#agent-skills).
Your agent can then upload videos, summarize them, and generate reports through VSS with natural-language prompts, without requiring manual interaction with the UI.

Upload a video through the `vss-manage-video-io-storage` skill.

Upload a video to VIOS [#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html#id4 "Link to this code")

```
Upload warehouse_sample.mp4 to VIOS.
```

Copy to clipboard

What the agent does:

1. Loads the `vss-manage-video-io-storage` skill and verifies that VIOS is reachable.

2. Uploads the video file to VIOS.

3. Confirms that VIOS lists the new video.


#### Step 3: Summarize a Video and Generate Reports [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#step-3-summarize-a-video-and-generate-reports "Link to this heading")

Ask your agent to summarize an uploaded video or generate a structured report for it. The `vss-summarize-video` skill handles direct summary requests through the Video Summarization microservice (with a VLM fallback). For report requests, the `vss-generate-video-report` skill uses the LVS summarization path when the `lvs` profile is ready and renders the result into a report template.

##### Summarize an Uploaded Video [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#summarize-an-uploaded-video "Link to this heading")

Summarize an uploaded video [#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html#id5 "Link to this code")

```
Summarize warehouse_sample with scenario 'warehouse monitoring' and events ['boxes falling', 'forklift stuck', 'person entering restricted area'].
Summarize warehouse_sample using the default scenario and events.
```

Copy to clipboard

What the agent does:

1. Loads the `vss-summarize-video` skill and probes the Video Summarization service readiness, routing to the LVS microservice when it is ready and to the VLM fallback otherwise.

2. Resolves the clip URL, stream ID, and timeline through the `vss-manage-video-io-storage` skill.

3. Collects the monitoring scenario, events, and optional objects of interest, or uses defaults when told to run autonomously.

4. Calls the Video Summarization service with the clip URL, scenario, events, and chunking parameters.

5. Renders the narrative summary and timestamped events.


##### Generate a Report [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#generate-a-report "Link to this heading")

Generate a report for an uploaded video [#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html#id6 "Link to this code")

```
Generate a report for warehouse_sample with scenario 'warehouse monitoring' and events ['boxes falling', 'forklift stuck', 'person entering restricted area'].
Generate a report for warehouse_sample using the default scenario and events.
```

Copy to clipboard

What the agent does:

1. Loads the `vss-generate-video-report` skill and selects the per-clip report mode.

2. Detects that the `lvs` profile is deployed (the Video Summarization service is ready), so it delegates to the `vss-summarize-video` skill for the summary and timestamped events instead of the VLM-direct path.

3. Resolves a browser-playable clip URL through the `vss-manage-video-io-storage` skill for the clip links in the report.

4. Renders the summary and events into the report template.

5. Returns the rendered report.


Note

Stream summary and Q&A are experimental and are not available through Agent Skills. Use the deployed VSS Agent chat UI instead, as described in [Step 4: Summarize and query a live stream](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html#lvs-stream-manual) in the manual flow below.

### Manually [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#manually "Link to this heading")

#### Step 1: Deploy the Agent [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#lvs-step-1-deploy-the-agent "Link to this heading")

Note

- Set the NGC CLI API key, then run the deploy commands for your GPU type.

- Refer to [VSS-Agent-Customization-configure-llm](https://docs.nvidia.com/vss/latest/vss-agent/configure-llm.html) and [VSS-Agent-Customization-configure-vlm](https://docs.nvidia.com/vss/latest/vss-agent/configure-vlm.html) for all LLM and VLM (local and remote) configuration options.

- For advanced settings and Agent Customization, see the deploy command help.


```
# Set NGC CLI API key
export NGC_CLI_API_KEY='your_ngc_api_key'

# View all available options
deploy/docker/scripts/dev-profile.sh --help
```

Copy to clipboard

H100

Shared GPU

```
deploy/docker/scripts/dev-profile.sh up -p lvs -H H100
```

Copy to clipboard

Dedicated GPU

```
deploy/docker/scripts/dev-profile.sh up -p lvs -H H100 \
    --llm-device-id 0 --vlm-device-id 1
```

Copy to clipboard

Remote LLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H H100 \
    --use-remote-llm
```

Copy to clipboard

Remote VLM

```
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H H100 \
    --use-remote-vlm
```

Copy to clipboard

Remote LLM + VLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H H100 \
    --use-remote-llm --use-remote-vlm
```

Copy to clipboard

RTXPRO6000BW

Shared GPU

```
deploy/docker/scripts/dev-profile.sh up -p lvs -H RTXPRO6000BW
```

Copy to clipboard

Dedicated GPU

```
deploy/docker/scripts/dev-profile.sh up -p lvs -H RTXPRO6000BW \
    --llm-device-id 0 --vlm-device-id 1
```

Copy to clipboard

Remote LLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H RTXPRO6000BW \
    --use-remote-llm
```

Copy to clipboard

Remote VLM

```
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H RTXPRO6000BW \
    --use-remote-vlm
```

Copy to clipboard

Remote LLM + VLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H RTXPRO6000BW \
    --use-remote-llm --use-remote-vlm
```

Copy to clipboard

L40S

Dedicated GPU

```
deploy/docker/scripts/dev-profile.sh up -p lvs -H L40S \
    --llm-device-id 0 --vlm-device-id 1
```

Copy to clipboard

Remote LLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H L40S \
    --use-remote-llm
```

Copy to clipboard

Remote VLM

```
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H L40S \
    --use-remote-vlm
```

Copy to clipboard

Remote LLM + VLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H L40S \
    --use-remote-llm --use-remote-vlm
```

Copy to clipboard

OTHER

See [Local LLM and VLM deployments on OTHER hardware](https://docs.nvidia.com/vss/latest/faq.html#faq-other-hardware) for known limitations and constraints.

Shared GPU

```
deploy/docker/scripts/dev-profile.sh up -p lvs -H OTHER \
    --llm-env-file /path/to/llm.env --vlm-env-file /path/to/vlm.env
```

Copy to clipboard

Dedicated GPU

```
deploy/docker/scripts/dev-profile.sh up -p lvs -H OTHER \
    --llm-device-id 0 --vlm-device-id 1 \
    --llm-env-file /path/to/llm.env --vlm-env-file /path/to/vlm.env
```

Copy to clipboard

Remote LLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H OTHER \
    --use-remote-llm --vlm-env-file /path/to/vlm.env
```

Copy to clipboard

Remote VLM

```
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H OTHER \
    --use-remote-vlm --llm-env-file /path/to/llm.env
```

Copy to clipboard

Remote LLM + VLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p lvs -H OTHER \
    --use-remote-llm --use-remote-vlm
```

Copy to clipboard

This command will download the necessary containers from the NGC Docker registry and start the agent. Depending on
your network speed, this may take a few minutes.

**This deployment uses the following defaults:**

- Host IP: src IP from `ip route get 1.1.1.1`

- LLM model: nvidia/nvidia-nemotron-nano-9b-v2

- VLM model: nvidia/cosmos3-nano-reasoner


**To use a different IP than the one derived:**

- `-i`: Manually specify the host IP address.

- `-e`: Optionally specify an externally accessible IP address for services that need to be reached from outside the host.


Note

When using a remote VLM of model-type `nim` (not `openai`), see [How does a remote nim VLM access videos?](https://docs.nvidia.com/vss/latest/faq.html#faq-remote-nim-access-requirements) for access requirements.

Once the deployment is complete, check that all the containers are running and healthy:

```
docker ps
```

Copy to clipboard

Once all the containers are running, you can access the agent UI at `http://<HOST_IP>:7777/`.

Note

Kubernetes deployment is supported by the Video Summarization Helm chart in `deploy/helm/developer-profiles/dev-profile-lvs`.
Use the chart README and `values-lvs.yaml` in the source repository for the complete values reference.
At minimum, configure the NGC API key, storage class, external host, and Kibana public URL before running
`helm dependency build` and `helm upgrade --install`.

#### Example prompts [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#example-prompts "Link to this heading")

Use natural language prompts in the chat interface. The agent routes the request to the appropriate Video Summarization, VLM, VIOS, or report tool.

| Task | Example prompt |
| --- | --- |
| Summarize an uploaded video | `Summarize video1.mp4` |
| Generate a report for an uploaded video | `Generate a report for video1.mp4` |
| Generate reports for multiple uploaded videos | `Generate reports for video1.mp4 and video2.mp4` |
| Start stream captioning (experimental) | `Start generating captions for stream CAM_1` |
| Summarize a stream (experimental) | `Summarize the stream CAM_1 from 45 seconds till now` |
| Generate a report for a stream (experimental) | `Generate a report for stream CAM_1 from 45 seconds till now` |
| Ask about stored stream captions (experimental) | `Were there PPE violations in CAM_1 from 2026-05-13T21:00:00Z to 2026-05-13T21:05:00Z?` |

#### Step 2: Upload a video [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#id2 "Link to this heading")

In the video management tab, drag and drop the video `warehouse_sample.mp4` into the upload area.

![Video Management tab with upload area](https://docs.nvidia.com/vss/latest/_images/lvs_upload_video.png)

Once the video is uploaded, the video will appear in the video list.

![Video uploaded](https://docs.nvidia.com/vss/latest/_images/lvs_upload_sample_warehouse.png)

#### Step 3: Generate a report for uploaded videos [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#step-3-generate-a-report-for-uploaded-videos "Link to this heading")

Ask the agent to generate a report about the uploaded video. Here is an example prompt:

```
Can you generate a report for warehouse_sample using video summarization?
```

Copy to clipboard

To generate reports across multiple uploaded videos, include the video names in one prompt:

```
Generate reports for warehouse_sample_1 and warehouse_sample_2.
```

Copy to clipboard

The agent will prompt you with 4 dialog windows to customize the Video Summarization microservice parameters.

You can cancel the workflow at any time by typing “/cancel” in the pop-up input box.

**Scenario**

Describe the monitoring context. For example:

```
warehouse monitoring
```

Copy to clipboard

![Pop-up for scenario input](https://docs.nvidia.com/vss/latest/_images/lvs-popup-scenario.png)**Events**

List events of interest to track. For example:

```
box falling, accident, person entering restricted area
```

Copy to clipboard

![Pop-up for events input](https://docs.nvidia.com/vss/latest/_images/lvs-popup-events.png)**Objects of Interest**

Specify objects to monitor. For example:

```
forklifts, pallets, workers
```

Copy to clipboard

![Pop-up for objects of interest input](https://docs.nvidia.com/vss/latest/_images/lvs-popup-objects-of-interests.png)**Confirmation**

Confirm the prompts by clicking “Submit”.

You can also redo the prompts by typing “/redo” or cancel the workflow by typing “/cancel”.

![Pop-up for confirmation](https://docs.nvidia.com/vss/latest/_images/lvs-popup-confirmation.png)

If you did not cancel the workflow, the agent will show the intermediate steps of the agent’s reasoning while the response is being generated and then output the final answer. You can download the report in PDF format by clicking
on “PDF Report” in the agent’s response:

![Report generated](https://docs.nvidia.com/vss/latest/_images/lvs-response.png)

#### Step 4: Summarize and query a live stream [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#step-4-summarize-and-query-a-live-stream "Link to this heading")

Note

Stream summary, stream report generation, and stored-caption Q&A are experimental. The supported flow is to add a stream from the Video Management tab, ask the agent to start generating captions for the stream, wait for captions to accumulate, and then request a summary or a report for a timestamp range covered by stored captions.

The Video Summarization profile can also analyze live streams. First add a stream from the Video Management tab, then ask the agent to start caption generation for that stream. The agent prompts for the same monitoring scenario, events, and optional objects of interest that are used for uploaded-video analysis.

Example prompt:

```
Start generating captions for stream CAM_1.
```

Copy to clipboard

After caption generation starts, allow time for captions to accumulate before asking for summaries or questions over the stream.

| Task | Example prompt |
| --- | --- |
| Summarize a stream time range | `Summarize the stream CAM_1 from 45 seconds till now.` |
| Generate a stream report for a time range | `Generate a report for stream CAM_1 from 45 seconds till now.` |
| Ask about stored stream captions | `Were there PPE violations in CAM_1 from 2026-05-13T21:00:00Z to 2026-05-13T21:05:00Z?` |

If no captions are available in Elasticsearch for the requested stream and time period, the summary or Q&A request can return empty results. This can happen when the requested time period is before caption generation started, or when the caption generation prompt causes no captions to be stored for that time period.

If multiple agent sessions or agent instances connect to the same backend, the caption generation prompt is overwritten by the latest query. The agent does not have visibility into caption prompts set by other agent instances.

Note

If you ask for a stream summary or report before caption generation has been started for that stream, the agent prompts you to start caption generation first instead of running the request.

Note

Stream reports differ from uploaded-video reports in their format. For example, stream reports use ISO 8601 timestamps instead of seconds, and they do not include per-event screenshots, per-event `[Watch Clip]` links, or a `Resources` playback URL.

#### Step 5: Search for specific events in the Dashboard [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#step-5-search-for-specific-events-in-the-dashboard "Link to this heading")

On the left sidebar, click on “Dashboard” to open the Kibana dashboard in the main window. From the menu icon,
choose the “Discover” tab.

![Dashboard tab](https://docs.nvidia.com/vss/latest/_images/lvs-dashboard-tab.png)

Set `default_*` in the `Data view` dropdown. Here you can see the events detected in the video or stream. When you click on a row item, a panel opens on the right side with details about the backend request and the event.

![Discover tab](https://docs.nvidia.com/vss/latest/_images/lvs-dashboard-discover.png)

#### Step 6: Teardown the Agent [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#step-6-teardown-the-agent "Link to this heading")

To teardown the agent, run the following command:

```
deploy/docker/scripts/dev-profile.sh down
```

Copy to clipboard

This command will stop and remove the agent containers.

## Service Endpoints [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#service-endpoints "Link to this heading")

Once deployed, the following services are available:

| Service | URL |
| --- | --- |
| VSS UI | `http://<HOST_IP>:7777` |
| Kibana UI | `http://<HOST_IP>:7777/kibana/app/home#/` |
| NVStreamer UI | `http://<HOST_IP>:31000/#/dashboard` |
| VST UI | `http://<HOST_IP>:30888/vst/#/dashboard` |
| Phoenix UI | `http://<HOST_IP>:7777/phoenix/projects` |

Service Endpoints [#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html#id7 "Link to this table")

## Optional: Use Nemotron-3-Nano-Omni (audio-aware VLM) [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#optional-use-nemotron-3-nano-omni-audio-aware-vlm "Link to this heading")

The LVS profile defaults to **Cosmos3 Nano Reasoner** as the VLM.
To swap in **Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8** for audio-aware
summarization, edit `deploy/docker/developer-profiles/dev-profile-lvs/.env`
and set the following variables (replace `<your_hf_token>` with your Hugging
Face token):

```
RTVI_VLM_MODEL_TO_USE=vllm-compatible
RTVI_VLM_MODEL_PATH='git:https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8'
VLM_MODEL_SUPPORTS_AUDIO=true
VLM_TRUST_REMOTE_CODE=true
INSTALL_PROPRIETARY_CODECS=true
HF_TOKEN=<your_hf_token>
```

Copy to clipboard

Also, turn on the `ENABLE_AUDIO` flag in the same file:

```
ENABLE_AUDIO=true
```

Copy to clipboard

In addition, update the model name at the top of the same file:

```
VLM_NAME=Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
```

Copy to clipboard

The default `RTVI_VLLM_GPU_MEMORY_UTILIZATION` of `0.35` is tuned for
Cosmos3 Nano Reasoner. Tune it for the Nemotron-3-Nano-Omni model and export it
before running `dev-profile.sh`. For example:

```
export RTVI_VLLM_GPU_MEMORY_UTILIZATION=0.45
bash deploy/docker/scripts/dev-profile.sh up -p lvs
```

Copy to clipboard

After the deployment is complete, verify with:

```
curl http://${HOST_IP}:8018/v1/models | jq
```

Copy to clipboard

The response should show `"audio_support": true` and the
Nemotron-3-Nano-Omni model ID.

For full RTVI-VLM environment variable reference, see [Real-Time VLM Microservice](https://docs.nvidia.com/vss/latest/real-time-vlm.html#vss-rtvi-vlm).

## Next steps [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#next-steps "Link to this heading")

Once you’ve familiarized yourself with the Video Summarization workflow, you can explore adding other agent workflows, such as search and alerting.

Additionally, you can dive deeper into the agent tools for video management, report generation, and video understanding.

### Known Issues [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#known-issues "Link to this heading")

- For OpenAI remote VLM endpoint, please use gpt-4o for now. Other models are not supported yet.

- **Not supported:** OpenAI VLM with a build.nvidia.com LLM. When using a build.nvidia.com LLM, do not use an OpenAI VLM or set `OPENAI_API_KEY`.


For known issues and limitations, see:

- [Agent Known Issues](https://docs.nvidia.com/vss/latest/vss-agent/VSS-Agent-Known-Issues.html) \- VSS Agent known issues and limitations

- [Known Issues](https://docs.nvidia.com/vss/latest/vss-ui.html#vss-ui-known-issues) \- VSS Agent UI known issues


## Troubleshooting [\#](https://docs.nvidia.com/vss/latest/agent-workflow-lvs.html\#troubleshooting "Link to this heading")

When encountering issues with the Video Summarization workflow:

1. **View container logs** \- See [Viewing Container Logs](https://docs.nvidia.com/vss/latest/vss-agent/vss-agent-Observability.html#viewing-container-logs) for instructions on viewing and analyzing container logs

2. **Navigate the Phoenix UI** \- See [Navigating the Phoenix UI](https://docs.nvidia.com/vss/latest/vss-agent/vss-agent-Observability.html#navigating-phoenix-ui) for step-by-step guidance on viewing traces and debugging agent workflows

3. **Check known issues** \- Review [Agent Known Issues](https://docs.nvidia.com/vss/latest/vss-agent/VSS-Agent-Known-Issues.html) (agent) and [Known Issues](https://docs.nvidia.com/vss/latest/vss-ui.html#vss-ui-known-issues) (UI) for documented limitations and workarounds


On this page