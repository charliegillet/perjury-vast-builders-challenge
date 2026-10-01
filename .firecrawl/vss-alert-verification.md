[Skip to main content](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html#main-content)

Back to top`⌘` + `K`

[![VSS - Home](https://docs.nvidia.com/vss/latest/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg)![VSS - Home](https://docs.nvidia.com/vss/latest/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg)\\
VSS](https://docs.nvidia.com/vss/latest/index.html)

3.2.1

[3.2.1](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html) [3.2.0](https://docs.nvidia.com/vss/3.2.0/agent-workflow-alert-verification.html) [3.1.0](https://docs.nvidia.com/vss/3.1.0/agent-workflow-alert-verification.html) [3.0.0](https://docs.nvidia.com/vss/3.0.0/agent-workflow-alert-verification.html) [2.4.1](https://docs.nvidia.com/vss/2.4.1/agent-workflow-alert-verification.html) [2.4.0](https://docs.nvidia.com/vss/2.4.0/agent-workflow-alert-verification.html) [2.3.1](https://docs.nvidia.com/vss/2.3.1/agent-workflow-alert-verification.html) [2.3.0](https://docs.nvidia.com/vss/2.3.0/agent-workflow-alert-verification.html) [2.2.0](https://docs.nvidia.com/vss/2.2.0/agent-workflow-alert-verification.html)

LightDarkSystem Settings

# Alert Verification Workflow [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#alert-verification-workflow "Link to this heading")

Two approaches for leveraging VLMs to generate alerts are showcased as part of the agent workflows:

- **Alert Verification**: The VLM analyzes video snippets corresponding to alerts generated upstream for verification; original alerts are generated through a combination of object detection/tracking and behavior analytics microservices that process video streams in real time. This approach invokes the VLM more sporadically and hence has lower GPU requirements, but depends on an upstream entity to generate “candidate” alerts for verification.

- **Real-Time Alerts**: The VLM continuously processes segments from a video source (for example, a camera) at periodic intervals based on a user-defined chunk duration. This approach leverages the generalizability of VLMs to trigger alerts for a broad set of cases (VLM fine-tuning or prompt tuning may be needed). However, it has higher GPU requirements due to more frequent VLM usage.


This section addresses the Alert Verification workflow; see [Real-Time Alerts](https://docs.nvidia.com/vss/latest/agent-workflow-rt-alert.html) for the other approach.

**Use Cases for Alert Verification**

- PPE compliance verification (hard hats, safety vests)

- Restricted area monitoring

- Asset presence/absence detection

- Custom object detection scenarios


**Estimated Deployment Time:** 15-20 minutes

The following diagram illustrates the alert verification workflow architecture:

![Vision Agent with Alert Verification Architecture](https://docs.nvidia.com/vss/latest/_images/profile-alerts-verification-arch.png)

**Key Features of the Alert Verification Agent:**

- RTVI CV for real-time object detection using Grounding DINO (open-vocabulary detection)

- Behavior Analytics for rule-based and configurable alert generation from detection results

- Alert Verification for VLM-based alert clip review to reduce false positives

- Alert storage for querying and reporting

- Report Generation


## What’s being deployed [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#what-s-being-deployed "Link to this heading")

- **NVStreamer:** Video streaming service for dataset video playback, thereby replicating live cameras in a real-world deployment

- **Video IO & Storage (VIOS):** Video ingestion (of NVStreamer video streams) supporting live streaming, recording, and playback features used by the agent

- **RTVI CV:** Real-Time Video Intelligence CV Microservice for object detection that processes VIOS live streams to output metadata to Kafka

- **Behavior Analytics:** Processes metadata from RTVI CV to generate alerts

- **Alert Verification:** Verification of alert video using VLM

- **RTVI VLM:** [Real-Time VLM Microservice](https://docs.nvidia.com/vss/latest/real-time-vlm.html) for vision-language model inference used by Alert Verification

- **ELK:** Elasticsearch, Logstash, and Kibana stack for log storage and analysis

- **VSS Agent:** Agent service that uses a configured LLM endpoint to route requests and orchestrate tool calls to VSS microservices and model endpoints (LLM/VLM NIMs) to answer questions and generate outputs

- **Nemotron LLM (NIM):** LLM inference service used for reasoning, tool selection, and response generation

- **Phoenix:** Observability and telemetry service for agent workflow monitoring


## Prerequisites [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#prerequisites "Link to this heading")

Before you begin, ensure all of the prerequisites are met. See [Prerequisites](https://docs.nvidia.com/vss/latest/prerequisites.html) for more details.

Note

For instructions on downloading sample data and the deployment package, see [Download Sample Data and Deployment Package](https://docs.nvidia.com/vss/latest/quickstart.html#quickstart-download-sample-data-and-package) in the Quickstart guide.

If you have already completed those steps for another agent workflow, skip to [Step 1: Deploy the Agent](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html#alert-verification-step-1-deploy-the-agent) in the Deploy section below.

## Deploy [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#deploy "Link to this heading")

### Step 1: Deploy the Agent [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#step-1-deploy-the-agent "Link to this heading")

Note

- Set the NGC CLI API key, then run the deploy commands for your GPU type.

- Refer to [VSS-Agent-Customization-configure-llm](https://docs.nvidia.com/vss/latest/vss-agent/configure-llm.html) and [VSS-Agent-Customization-configure-vlm](https://docs.nvidia.com/vss/latest/vss-agent/configure-vlm.html) for all LLM and VLM (local and remote) configuration options.
For RTVI-VLM configuration options, see [Real-Time VLM](https://docs.nvidia.com/vss/latest/real-time-vlm.html).

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
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H H100
```

Copy to clipboard

Dedicated GPU

```
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H H100 \
    --llm-device-id 1 --vlm-device-id 2
```

Copy to clipboard

Remote LLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H H100 \
    --use-remote-llm
```

Copy to clipboard

Remote VLM

```
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H H100 \
    --use-remote-vlm
```

Copy to clipboard

Remote LLM + VLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H H100 \
    --use-remote-llm --use-remote-vlm
```

Copy to clipboard

RTXPRO6000BW

Shared GPU

```
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H RTXPRO6000BW
```

Copy to clipboard

Dedicated GPU

```
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H RTXPRO6000BW \
    --llm-device-id 1 --vlm-device-id 2
```

Copy to clipboard

Remote LLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H RTXPRO6000BW \
    --use-remote-llm
```

Copy to clipboard

Remote VLM

```
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H RTXPRO6000BW \
    --use-remote-vlm
```

Copy to clipboard

Remote LLM + VLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H RTXPRO6000BW \
    --use-remote-llm --use-remote-vlm
```

Copy to clipboard

RTXPRO4500BW

Note

On NVIDIA driver 580.105.08, `nvidia-smi` may not identify RTX PRO 4500 Blackwell GPUs, causing `-H RTXPRO4500BW` to fail the hardware check. Use NVIDIA driver 580.126.09 or later, or run `export SKIP_HARDWARE_CHECK=true` before the quickstart command.

Remote LLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H RTXPRO4500BW \
    --use-remote-llm
```

Copy to clipboard

L40S

Dedicated GPU

```
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H L40S \
    --llm-device-id 1 --vlm-device-id 2
```

Copy to clipboard

Remote LLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H L40S \
    --use-remote-llm
```

Copy to clipboard

Remote VLM

```
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H L40S \
    --use-remote-vlm
```

Copy to clipboard

Remote LLM + VLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H L40S \
    --use-remote-llm --use-remote-vlm
```

Copy to clipboard

SPARK

Remote LLM

See [VSS-Agent-Customization-configure-llm](https://docs.nvidia.com/vss/latest/vss-agent/configure-llm.html) for remote LLM endpoint options.

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H DGX-SPARK \
    --use-remote-llm
```

Copy to clipboard

IGX-THOR

Remote LLM

See [VSS-Agent-Customization-configure-llm](https://docs.nvidia.com/vss/latest/vss-agent/configure-llm.html) for remote LLM endpoint options.

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H IGX-THOR \
    --use-remote-llm
```

Copy to clipboard

AGX-THOR

Remote LLM

See [VSS-Agent-Customization-configure-llm](https://docs.nvidia.com/vss/latest/vss-agent/configure-llm.html) for remote LLM endpoint options.

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H AGX-THOR \
    --use-remote-llm
```

Copy to clipboard

OTHER

See [Local LLM and VLM deployments on OTHER hardware](https://docs.nvidia.com/vss/latest/faq.html#faq-other-hardware) and
[Local RTVI-VLM deployments on OTHER hardware](https://docs.nvidia.com/vss/latest/faq.html#faq-rtvi-vlm-other-hardware)
for known limitations and configuration constraints.

Shared GPU

```
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H OTHER \
    --llm-env-file /path/to/llm.env --vlm-env-file /path/to/vlm.env
```

Copy to clipboard

Dedicated GPU

```
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H OTHER \
    --llm-device-id 1 --vlm-device-id 2 \
    --llm-env-file /path/to/llm.env --vlm-env-file /path/to/vlm.env
```

Copy to clipboard

Remote LLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H OTHER \
    --use-remote-llm --vlm-env-file /path/to/vlm.env
```

Copy to clipboard

Remote VLM

```
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H OTHER \
    --use-remote-vlm --llm-env-file /path/to/llm.env
```

Copy to clipboard

Remote LLM + VLM

```
export LLM_ENDPOINT_URL=https://your-llm-endpoint.com
export VLM_ENDPOINT_URL=https://your-vlm-endpoint.com
deploy/docker/scripts/dev-profile.sh up -p alerts -m verification -H OTHER \
    --use-remote-llm --use-remote-vlm
```

Copy to clipboard

This command will download the necessary containers from the NGC Docker registry and start the agent. Depending on
your network speed, this may take a few minutes.

**This deployment uses the following defaults:**

- Host IP: src IP from `ip route get 1.1.1.1`

- LLM model: nvidia/nvidia-nemotron-nano-9b-v2

- VLM model: cosmos-reason3 (served via RTVI VLM container)


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

#### Deploy with Agent Skills [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#deploy-with-agent-skills "Link to this heading")

As an alternative to running the deployment command manually, you can use VSS
Agent Skills from a coding agent such as Claude Code, Codex, or NemoClaw.
First, install the `deploy` skill as described in [Agent Skills](https://docs.nvidia.com/vss/latest/agent-skills.html#agent-skills) and make it
accessible to your coding agent. The host must meet the same deployment requirements listed above (supported GPU/hardware for that profile)
and must meet the [Prerequisites](https://docs.nvidia.com/vss/latest/prerequisites.html).

The deploy skill will choose the `<platform>` and `<mode>` to match your system, as detailed in [Development Profile GPU Requirements](https://docs.nvidia.com/vss/latest/prerequisites.html#vss-development-profile-gpu-requirements).
Refer to the requirements table for valid platform and mode combinations compatible with your hardware.

Deploy prompt structure [#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html#id1 "Link to this code")

```
Deploy the VSS alerts verification profile.
```

Copy to clipboard

For edge platforms, ask the deploy skill to use a remote LLM when possible.
Local LLM/VLM sharing on the edge GPU is supported, but a remote LLM is recommended for better response time.
See [VSS Agent Customization - Configure LLM](https://docs.nvidia.com/vss/latest/vss-agent/configure-llm.html) for remote LLM endpoint options.

Recommended edge deployment prompts [#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html#id2 "Link to this code")

```
Deploy the VSS alerts verification profile on this DGX-SPARK machine with a remote LLM.
Deploy the VSS alerts verification profile on this IGX-THOR machine with a remote LLM.
Deploy the VSS alerts verification profile on this AGX-THOR machine with a remote LLM.
```

Copy to clipboard

If you would like to modify the workflow to work with other videos or usecases, you can update the following files:

- `deploy/docker/developer-profiles/dev-profile-alerts/vlm-as-verifier/configs/alert_type_config.json`

  - Modify the “output\_category” and “user” fields here. “output\_category” modifies the category type that shows up in the agent UI. “user” is the user prompt that is sent to the VLM for verification of each alert clip.
- `deploy/docker/developer-profiles/dev-profile-alerts/deepstream/configs/config_triton_nvinferserver_gdino.txt`

  - Update the “type\_name” field under “postprocess” to change the objects that are detected by Grounding DINO. By default this is “person” with a threshold of 0.5. This can be modified to support multiple classes by using “ . “ as a delimiter.
- `deploy/docker/developer-profiles/dev-profile-alerts/vss-behavior-analytics/configs/vss-behavior-analytics-config.json`

  - Update the “value” field under `"name": "fovCountViolationIncidentObjectType"` to change the objects that Behavior Analytics creates alerts for.
- `deploy/docker/developer-profiles/dev-profile-alerts/vlm-as-verifier/parsers/` _(optional)_

  - Drop a Python module exposing a parser class with a `parse(self, raw_response: str) -> dict` method, then set `vlm.response_parser` in `config.yml` to its dotted path. Use this to replace the built-in YES/NO verification parsing with classification, analytics, or enrichment outputs. See [Pluggable Response Parser](https://docs.nvidia.com/vss/latest/alert-verification-service.html#alert-verification-pluggable-parser) for the full contract, examples, and error handling.

### Step 2: Add a video stream [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#step-2-add-a-video-stream "Link to this heading")

Add an RTSP stream by clicking the **\+ Add RTSP** button on the **Video Management** tab in the agent UI. If you do not have an RTSP stream, you can use [NVStreamer](https://docs.nvidia.com/vss/latest/vios-nvstreamer.html) at `http://<HOST_IP>:31000` to upload a video file and create an RTSP stream.

For this profile, use the `sample-warehouse-ladder.mp4` stream.

![Upload RTSP Stream](https://docs.nvidia.com/vss/latest/_images/alerts-video-add.png)

Note

By default, this profile only supports up to one stream being processed at a time.

This can be increased by modifying the `NUM_SENSORS` environment variable in the `deploy/docker/developer-profiles/dev-profile-alerts/.env` file before deployment. On RTX PRO 6000, up to 4 streams at 10fps have been tested to work.

On edge platforms like DGX Spark, IGX Thor, and AGX Thor, up to 1 stream at 10fps has been tested to work due to GPU requirements.

### Step 3: Verify pipeline components [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#step-3-verify-pipeline-components "Link to this heading")

Open the Kibana UI at `http://<HOST_IP>:7777/kibana/app/home#/` and navigate to the Discover tab.

Verify the following data indices are populated. It may take a few minutes for data to start appearing after adding the stream:

- `mdx-raw-*` \- Raw detection data

- `mdx-incidents-*` \- Generated incidents

- `mdx-vlm-incidents-*` \- VLM-verified alerts


If the indices do not show data, check the following items:

- Ensure that the Perception service is running and processing the stream. View the container logs with `docker logs -f vss-rtvi-cv` and confirm that the engine files are built and the added stream is being processed. Common causes of failure include model download errors during startup and insufficient GPU memory.

- Confirm that the labels emitted by the Perception model match the labels that Behavior Analytics expects. Behavior Analytics processes only the object type specified by the `fovCountViolationIncidentObjectType` field in `deploy/docker/developer-profiles/dev-profile-alerts/vss-behavior-analytics/configs/vss-behavior-analytics-config.json`.


### Step 4: View alerts in the Agent UI [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#step-4-view-alerts-in-the-agent-ui "Link to this heading")

Launch the Agent UI at `http://<HOST_IP>:7777/`.

List streams to verify connectivity, then use the **Alerts** tab to list alerts. Select the verified alerts option to view VLM-verified alerts.

![Alerts Tab in the Agent UI](https://docs.nvidia.com/vss/latest/_images/alert-verification-alerts.png)

You can then click on a video thumbnail to play the video and view the alert. When the bounding box overlay is enabled, playback includes bounding boxes over objects of interest. This overlay is off by default; to enable it, set `vst_config.add_overlay: true` on the alert verification service and `NEXT_PUBLIC_ALERTS_TAB_MEDIA_WITH_OBJECTS_BBOX=true` for the Agent UI.

![Video Playback with Bounding Boxes](https://docs.nvidia.com/vss/latest/_images/alert-verification-bbox.png)

### Step 5: Generate a Report for the Alert [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#step-5-generate-a-report-for-the-alert "Link to this heading")

You can use the chat interface to request creation of a report for the generated alerts. The report is currently generated in markdown format and displayed in the VSS UI.

As a first step, identify the alert ID for which the report needs to be generated. Use the chat interface to retrieve the ID by listing recent alerts by count, or expand any alert in the **Alerts** tab to display the **Id** field along with associated metadata.

Now, use the ID to request generation of the report while also specifying the associated sensor, as shown in the sample image below.

![Report Generation](https://docs.nvidia.com/vss/latest/_images/report-gen.png)

### Step 6: Teardown the Agent [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#step-6-teardown-the-agent "Link to this heading")

To tear down the agent, run the following command:

```
deploy/docker/scripts/dev-profile.sh down
```

Copy to clipboard

This command will stop and remove the agent containers.

## Service Endpoints [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#service-endpoints "Link to this heading")

Once deployed, the following services are available:

| Service | URL |
| --- | --- |
| VSS UI | `http://<HOST_IP>:7777` |
| Kibana UI | `http://<HOST_IP>:7777/kibana/app/home#/` |
| NVStreamer UI | `http://<HOST_IP>:31000/#/dashboard` |
| VST UI | `http://<HOST_IP>:30888/vst/#/dashboard` |
| Phoenix UI | `http://<HOST_IP>:7777/phoenix/projects` |

Service Endpoints [#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html#id3 "Link to this table")

## Next Steps [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#next-steps "Link to this heading")

Once you’ve familiarized yourself with the alert verification workflow, you can explore:

- Modifying the alert prompt in the Alerts Microservice configuration.

- Adjusting rate limit settings to control alert verification frequency.

- Configuring G-DINO prompting and class thresholds for custom detection scenarios.


### Known Issues [\#](https://docs.nvidia.com/vss/latest/agent-workflow-alert-verification.html\#known-issues "Link to this heading")

- Some VLM inaccuracies might be observed depending on the model and configuration used with the RTVI VLM container.

- On RTX PRO 4500 Blackwell systems with NVIDIA driver 580.105.08, `nvidia-smi` may not identify the GPU model. As a result, the quickstart command with `-H RTXPRO4500BW` can fail with a hardware mismatch. Upgrade to NVIDIA driver 580.126.09 or later, or run `export SKIP_HARDWARE_CHECK=true` before running the quickstart command.

- Video snippets generated for alerts may be short (for example, only a couple of seconds) depending on behavior analytics processing of the specific video, which could impact VLM accuracy. To address this issue, modify the _fovCountViolationIncidentThreshold_ setting to the desired minimum alert clip duration in _deploy/docker/developer-profiles/dev-profile-alerts/vss-behavior-analytics/configs/vss-behavior-analytics-config.json_.

- Video playback duration for verified alerts may not exactly match the alert timestamps.

- Report generation may produce inaccurate results. As a potential workaround, remove the `use_base64: true` line under `video_understanding_iso` in `developer-profiles/dev-profile-alerts/vss-agent/configs/config.yml`.

- If perception crashes and restarts, streams are not automatically re-added and alerts will not be generated.

- For remote VLM and LLM deployments, the alert verification timeout may need to be increased from the default value of 5 seconds. See [Alert Verification VLM Configuration Options](https://docs.nvidia.com/vss/latest/alert-verification-service.html#alert-verification-vlm-config-options) for specific details.

- VLM verdict verification can fail in the UI even when VLM requests are processed successfully. Alert Bridge response parsing accepts only raw verdicts such as `A/B` or `Yes/No` before serializing them to `confirmed` or `rejected`. As a result, a semantically valid `rejected` verdict from Cosmos Reason can fail schema validation and be persisted as `verification-failed`.

- The VST UI is externally accessible on both port 30000 and 30888 because both ports are exposed on the host network. For security hardening, consider using a firewall to allowlist only the required VST ingress port.

- Spurious records in the `mdx-vlm-incidents-1970-01-01` index may be generated by RTVI VLM. Workaround: add this near the top of the Logstash `filter { }` block in `deploy/docker/services/infra/elk/logstash/pipelines/kafka/mdx-logstash.conf`:





```
# Drop internal RT-VLM activity-detector noise before indexing.
if [analyticsModule][id] == "vlm-activity-detector" and [analyticsModule][info][streamType] == "file" {
    drop { }
}
```

Copy to clipboard



If `streamType` is unavailable, use the following fallback:





```
if [analyticsModule][id] == "vlm-activity-detector" and [category] == "vlm-alert" {
    drop { }
}
```

Copy to clipboard


On this page