

## FILE: vss-blueprint/deployments/dataengine-vss-ingest-pipeline/README.md
Source: https://github.com/vast-data/vss-blueprint/blob/main/deployments/dataengine-vss-ingest-pipeline/README.md

```
# Deploy DataEngine Pipelines (VAST)

Deploy VSS serverless pipelines using **DataEngine UI** or **vastde CLI**:

1. **Ingest** — S3-triggered video processing (`video-realtime-processing-pipeline`)
2. **Enrichment** — scheduled prompt-suggester (`vss-enrichment-pipeline`)

Both pipelines share secret name **`vss2-secret`** (table/bucket values use `vss-*` — see templates).

## Prerequisites

- A running VAST DataEngine cluster
- User with permissions to setup DataEngine Pipelines (including Vector QueryEngine Identity-Policy)
- Pre-created Topic in VAST Event Broker (e.g., `video-topic`)
- A container registry added to your DataEngine tenant in VMS, with images you built and pushed (jump to **Build DataEngine function images** later in this file)
- GPU services (Reason2, Embed1, YOLO) reachable from DataEngine workers — see [vss-blueprint-models](../../scripts/vss-blueprint-models/README.md)

## Pipeline Overview

**Ingest — `video-realtime-processing-pipeline`**

```
vss-chunks bucket → video-segmenter
                            ↓
vss-chunks-segments bucket → video-detector → video-reasoner → video-embedder → video-vastdb-writer
```

**Enrichment — `vss-enrichment-pipeline` (optional, after ingest is producing rows)**

```
Schedule trigger → prompt-suggester → vss-prompts-events (search chips + key events)
```

## Files in This Directory

| File | Used By | Description |
|------|---------|-------------|
| `vss-gui-secret-file-template.yaml` | GUI | Shared secret template (`vss2-secret`) for ingest + enrichment |
| `vss-cli-secret-file-template.yaml` | CLI | Shared secret template (`vss2-secret`) for ingest + enrichment |
| `vss-ingest-pipeline-file.yaml` | CLI | Ingest pipeline manifest for `vastde pipelines create` |
| `vss-enrichment-pipeline-file.yaml` | CLI | Enrichment pipeline manifest (scheduled prompt-suggester) |

---

# Option 1: Deploy with DataEngine UI

Ingest (steps 1–4) is required. Enrichment (step 5) is optional.

## Step 1: Configure Secret

Copy `vss-gui-secret-file-template.yaml` to a local file, fill credentials, and upload in DataEngine UI — **do not commit** files with real keys (templates with empty values are safe in git).

```bash
vim vss-gui-secret-file-template.yaml
```

Secret **name** in DataEngine must be `vss2-secret`. Bucket/table **values** use the `vss-*` namespace (`vss-chunks`, `vss-collection`, etc.). Same secret is reused for enrichment.

| Section | Key Settings |
|---------|--------------|
| **S3** | `s3accesskey`, `s3secretkey`, `s3endpoint` |
| **Reasoning** | Cosmos-Reason2 (`cosmos_host`, `cosmos_port: 8001`, `cosmos_model: nvidia/cosmos-reason2-8b`) |
| **Embedding** | Text + visual NIM (`embeddinghost` / `embeddingport: 8002`, `embeddingmodel: nvidia/cosmos-embed1`); recreate VastDB collection after schema changes |
| **VastDB** | `vdbendpoint`, `vdbaccesskey`, `vdbsecretkey`, `vdbbucket`, `vdbschema`, `vdbcollection` |
| **YOLO** | `yolo_infer_host`, `yolo_infer_port` (`8003` with [vss-blueprint-models](../../scripts/vss-blueprint-models/README.md); templates may still show `8022`), `detection_sidecar_prefix` |
| **Enrichment** | `vdbpromptscollection` (`vss-prompts-events`), `suggestions_*` (used by prompt-suggester) |
| **Processing** | `segment_duration`, `scenario` (default prompt key; see [video-reasoner README](../../source-code/ingest/video-reasoner/README.md). GUI scenario labels: [shared/ingest_metadata.py](../../source-code/shared/ingest_metadata.py)) |

## Step 2: Create Triggers

Navigate to **DataEngine UI → Triggers** and create:

| Trigger Name | Type | Bucket |
|--------------|------|--------|
| `video-chunk-land-trigger` | S3 Bucket | `vss-chunks` |
| `video-segment-land-trigger` | S3 Bucket | `vss-chunks-segments` |

## Step 3: Create Functions

Navigate to **DataEngine UI → Functions** and create:

| Function | Image (names from `build-vastde-functions.sh`) |
|----------|-------|
| `video-segmenter` | `your.registry/vss-video-segmenter:v1` |
| `video-detector` | `your.registry/vss-video-detector:v1` |
| `video-reasoner` | `your.registry/vss-video-reasoner:v1` |
| `video-embedder` | `your.registry/vss-video-embedder:v1` |
| `video-vastdb-writer` | `your.registry/vss-video-vastdb:v1` |

## Step 4: Create Pipeline

Navigate to **DataEngine UI → Pipelines → Create New Pipeline**

1. **Name:** `video-realtime-processing-pipeline`

2. **Upload secret:** `vss-gui-secret-file-template.yaml`

3. **Create connections:**
   - `video-chunk-land-trigger` → `video-segmenter`
   - `video-segment-land-trigger` → `video-detector` → `video-reasoner` → `video-embedder` → `video-vastdb-writer`

4. **Set resources (all functions):**
   - CPU: `1000m - 5000m`
   - Memory: `1280Mi - 2560Mi`

5. **Save and activate the pipeline**

## Step 5: Enrichment pipeline (optional)

Skip unless you want search suggestion chips and dashboard key events. Deploy after ingest is writing rows to `vss-collection`. Reuse **`vss2-secret`** — do not create a second secret. Details: [prompt-suggester](../../source-code/enrichment/prompt-suggester/README.md).

1. **Trigger:** DataEngine UI → Triggers → create `vss-prompt-suggester-scheduled-trigger` (type **Schedule**, e.g. every 5–15 minutes).
2. **Function:** create `prompt-suggester` with image `your.registry/vss-video-events:v1` (name used by `build-vastde-functions.sh`).
3. **Pipeline:** name `vss-enrichment-pipeline`; attach existing `vss2-secret`; connect `vss-prompt-suggester-scheduled-trigger` → `prompt-suggester`.
4. **Resources:** CPU `200m - 1000m`, memory `256Mi - 512Mi`. Activate.

---

# Option 2: Deploy with vastde CLI

Ingest (steps 1–5) is required. Enrichment (step 6) is optional.

## Step 1: Configure Secret

Edit `vss-cli-secret-file-template.yaml`:

```bash
vim vss-cli-secret-file-template.yaml
```

| Section | Key Settings |
|---------|--------------|
| **S3** | `s3accesskey`, `s3secretkey`, `s3endpoint` |
| **Reasoning** | Cosmos-Reason2 (`cosmos_host`, `cosmos_port: 8001`, `cosmos_model: nvidia/cosmos-reason2-8b`) |
| **Embedding** | Text + visual NIM (`embeddinghost` / `embeddingport: 8002`, `embeddingmodel: nvidia/cosmos-embed1`); recreate VastDB collection after schema changes |
| **VastDB** | `vdbendpoint`, `vdbaccesskey`, `vdbsecretkey`, `vdbbucket`, `vdbschema`, `vdbcollection` |
| **YOLO** | `yolo_infer_host`, `yolo_infer_port` (`8003` with [vss-blueprint-models](../../scripts/vss-blueprint-models/README.md); templates may still show `8022`), `detection_sidecar_prefix` |
| **Enrichment** | `vdbpromptscollection` (`vss-prompts-events`), `suggestions_*` (used by prompt-suggester) |
| **Processing** | `segment_duration`, `scenario` (default prompt key; see [video-reasoner README](../../source-code/ingest/video-reasoner/README.md). GUI scenario labels: [shared/ingest_metadata.py](../../source-code/shared/ingest_metadata.py)) |

## Step 2: Create Triggers

```bash
vastde triggers create \
  --name video-chunk-land-trigger \
  --type Element \
  --source-bucket vss-chunks \
  --events "ObjectCreated:*" \
  --broker-name <your-broker-name> \
  --broker-type Internal \
  --topic <your-topic>

vastde triggers create \
  --name video-segment-land-trigger \
  --type Element \
  --source-bucket vss-chunks-segments \
  --events "ObjectCreated:*" \
  --broker-name <your-broker-name> \
  --broker-type Internal \
  --topic <your-topic>
```

## Step 3: Create Functions

Set `--container-registry` to the registry name as configured in VMS. Replace `YOUR_ORG` in `--artifact-source` with the repository namespace/path that registry uses for the image you pushed (for Docker Hub this is typically `username` or org name, so the source looks like `YOUR_ORG/vss-video-segmenter`).

```bash
vastde functions create \
  --name video-segmenter \
  --container-registry dockerio \
  --artifact-source YOUR_ORG/vss-video-segmenter \
  --artifact-type image \
  --image-tag v1

vastde functions create \
  --name video-detector \
  --container-registry dockerio \
  --artifact-source YOUR_ORG/vss-video-detector \
  --artifact-type image \
  --image-tag v1

vastde functions create \
  --name video-reasoner \
  --container-registry dockerio \
  --artifact-source YOUR_ORG/vss-video-reasoner \
  --artifact-type image \
  --image-tag v1

vastde functions create \
  --name video-embedder \
  --container-registry dockerio \
  --artifact-source YOUR_ORG/vss-video-embedder \
  --artifact-type image \
  --image-tag v1

vastde functions create \
  --name video-vastdb-writer \
  --container-registry dockerio \
  --artifact-source YOUR_ORG/vss-video-vastdb \
  --artifact-type image \
  --image-tag v1
```

## Step 4: Configure Pipeline Manifest

Edit `vss-ingest-pipeline-file.yaml` and fill in:
- `kubernetes_cluster_vrn` - Your Kubernetes cluster VRN (run `vastde compute-clusters list`)
- `namespace` - Target Kubernetes namespace
- `topic` fields in link entries (e.g., `vast:dataengine:topics:<broker-name>/<topic>`)

## Step 5: Create and Deploy Pipeline

```bash
vastde pipelines create \
  --name video-realtime-processing-pipeline \
  --config @vss-ingest-pipeline-file.yaml \
  --secret-file vss-cli-secret-file-template.yaml \
  --deploy
```

## Step 6: Enrichment pipeline (optional)

Skip unless you want search suggestion chips and dashboard key events. Deploy after ingest is writing rows to `vss-collection`. Reuse **`vss2-secret`** — do not create a second secret. Details: [prompt-suggester](../../source-code/enrichment/prompt-suggester/README.md).

Create the schedule trigger in DataEngine (name must match the YAML VRN: `vss-prompt-suggester-scheduled-trigger`). Then:

```bash
vastde functions create \
  --name prompt-suggester \
  --container-registry dockerio \
  --artifact-source YOUR_ORG/vss-video-events \
  --artifact-type image \
  --image-tag v1
```

Edit `vss-enrichment-pipeline-file.yaml` (`kubernetes_cluster_vrn`, `namespace`, `topic`), then:

```bash
vastde pipelines create \
  --name vss-enrichment-pipeline \
  --config @vss-enrichment-pipeline-file.yaml \
  --secret-file vss-cli-secret-file-template.yaml \
  --deploy
```

---

## Function Documentation

| Function | Description | Details |
|----------|-------------|---------|
| video-segmenter | Splits videos into segments | [README](../../source-code/ingest/video-segmenter/README.md) |
| video-detector | YOLO11 object detection + sidecar | [README](../../source-code/ingest/video-detector/README.md) |
| video-reasoner | AI video analysis (Cosmos-Reason2) | [README](../../source-code/ingest/video-reasoner/README.md) |
| video-embedder | Vector embeddings | [README](../../source-code/ingest/video-embedder/README.md) |
| video-vastdb-writer | Stores vectors in VastDB | [README](../../source-code/ingest/vastdb-writer/README.md) |
| prompt-suggester | Scheduled enrichment → search chips + key events | [README](../../source-code/enrichment/prompt-suggester/README.md) |

## Build DataEngine function images

Build all pipeline function images with the helper script (recommended):

```bash
REGISTRY=your.registry/vss TAG=v1 source-code/scripts/build-vastde-functions.sh
```

This runs `vastde functions build` for segmenter, detector, reasoner, embedder, vastdb-writer (`vss-video-vastdb`), and prompt-suggester (`vss-video-events`), then tags and pushes to your registry. DataEngine workloads typically target `linux/amd64`.

Manual builds with the [VAST DataEngine CLI](https://github.com/vast-data/dataengine-cli) (`vastde`):

From `vss-blueprint/`:

```bash
# video-segmenter
cd source-code/ingest/video-segmenter
vastde functions build vss-video-segmenter
docker tag vss-video-segmenter your.registry/vss-video-segmenter:v1
docker push your.registry/vss-video-segmenter:v1

# video-detector
cd ../video-detector
vastde functions build vss-video-detector
docker tag vss-video-detector your.registry/vss-video-detector:v1
docker push your.registry/vss-video-detector:v1

# video-reasoner
cd ../video-reasoner
vastde functions build vss-video-reasoner
docker tag vss-video-reasoner your.registry/vss-video-reasoner:v1
docker push your.registry/vss-video-reasoner:v1

# video-embedder
cd ../video-embedder
vastde functions build vss-video-embedder
docker tag vss-video-embedder your.registry/vss-video-embedder:v1
docker push your.registry/vss-video-embedder:v1

# vastdb-writer (pushed image name vss-video-vastdb)
cd ../vastdb-writer
vastde functions build vss-video-vastdb
docker tag vss-video-vastdb your.registry/vss-video-vastdb:v1
docker push your.registry/vss-video-vastdb:v1

# prompt-suggester (pushed image name vss-video-events)
cd ../../enrichment/prompt-suggester
vastde functions build vss-video-events
docker tag vss-video-events your.registry/vss-video-events:v1
docker push your.registry/vss-video-events:v1
```

Replace `your.registry` with your real registry. Use the same names and tags in the DataEngine UI, in `vastde functions create` (see Step 3), and in your VMS registry configuration.

See [scripts README](../../source-code/scripts/README.md) for `REGISTRY` / `TAG` overrides.

```


## FILE: vss-blueprint/deployments/dataengine-vss-ingest-pipeline/vss-ingest-pipeline-file.yaml
Source: https://github.com/vast-data/vss-blueprint/blob/main/deployments/dataengine-vss-ingest-pipeline/vss-ingest-pipeline-file.yaml

```
kubernetes_cluster_vrn: <your-kubernetes-cluster-vrn>
namespace: <your-namespace>
manifest:
  config:
    environment_variables: []
    secrets:
      - vss2-secret
  function_deployments:
    - function_vrn: vast:dataengine:functions:video-segmenter
      name: video-segmenter-2
      revision: 1
      config:
        log_level: INFO
      resources:
        min_cpu: 1000m
        max_cpu: 5000m
        min_memory: 1280Mi
        max_memory: 2560Mi
        min_concurrency: 1
        max_concurrency: 10
        timeout: 600
    - function_vrn: vast:dataengine:functions:video-detector
      name: video-detector-7
      revision: 1
      config:
        log_level: INFO
      resources:
        min_cpu: 1000m
        max_cpu: 5000m
        min_memory: 1280Mi
        max_memory: 2560Mi
        min_concurrency: 1
        max_concurrency: 5
        timeout: 600
    - function_vrn: vast:dataengine:functions:video-reasoner
      name: video-reasoner-3
      revision: 1
      config:
        log_level: INFO
      resources:
        min_cpu: 1000m
        max_cpu: 5000m
        min_memory: 1280Mi
        max_memory: 2560Mi
        min_concurrency: 1
        max_concurrency: 5
        timeout: 600
    - function_vrn: vast:dataengine:functions:video-embedder
      name: video-embedder-4
      revision: 1
      config:
        log_level: INFO
      resources:
        min_cpu: 1000m
        max_cpu: 5000m
        min_memory: 1280Mi
        max_memory: 2560Mi
        min_concurrency: 1
        max_concurrency: 5
        timeout: 600
    - function_vrn: vast:dataengine:functions:video-vastdb-writer
      name: video-vastdb-writer-5
      revision: 1
      config:
        log_level: INFO
      resources:
        min_cpu: 1000m
        max_cpu: 5000m
        min_memory: 1280Mi
        max_memory: 2560Mi
        min_concurrency: 1
        max_concurrency: 10
        timeout: 600
  links:
    - source:
        - video-chunk-land-trigger-1
      destination:
        - video-segmenter-2
      topic: vast:dataengine:topics:<your-broker-name>/<your-topic>
      config:
        events_order: unordered
        retries: 3
    - source:
        - video-segment-land-trigger-6
      destination:
        - video-detector-7
      topic: vast:dataengine:topics:<your-broker-name>/<your-topic>
      config:
        events_order: unordered
        retries: 3
    - source:
        - video-detector-7
      destination:
        - video-reasoner-3
      config:
        events_order: unordered
        retries: 3
    - source:
        - video-reasoner-3
      destination:
        - video-embedder-4
      config:
        events_order: unordered
        retries: 3
    - source:
        - video-embedder-4
      destination:
        - video-vastdb-writer-5
      config:
        events_order: unordered
        retries: 3
  triggers:
    - name: video-chunk-land-trigger-1
      vrn: vast:dataengine:triggers:video-chunk-land-trigger
    - name: video-segment-land-trigger-6
      vrn: vast:dataengine:triggers:video-segment-land-trigger


```


## FILE: vss-blueprint/deployments/dataengine-vss-ingest-pipeline/vss-enrichment-pipeline-file.yaml
Source: https://github.com/vast-data/vss-blueprint/blob/main/deployments/dataengine-vss-ingest-pipeline/vss-enrichment-pipeline-file.yaml

```
# DataEngine pipeline: scheduled LLM prompt + key-event suggestions → vss-prompts-events
# Register function VRN after building/pushing prompt-suggester image to DataEngine.
# Same secret as ingest: vss2-secret (see vss-gui / vss-cli secret templates in this directory).
kubernetes_cluster_vrn: <your-kubernetes-cluster-vrn>
namespace: <your-namespace>
name: vss-enrichment-pipeline
config:
  environment_variables: []
  secrets:
    - vss2-secret
function_deployments:
  - function_vrn: vast:dataengine:functions:prompt-suggester
    name: prompt-suggester-1
    revision: 1
    config:
      log_level: INFO
    resources:
      min_cpu: 200m
      max_cpu: 1000m
      min_memory: 256Mi
      max_memory: 512Mi
      min_concurrency: 1
      max_concurrency: 2
      timeout: 300
links:
  - source:
      - vss-prompt-suggester-scheduled-trigger-1
    destination:
      - prompt-suggester-1
    topic: vast:dataengine:topics:<your-broker-name>/<your-topic>
    config:
      events_order: unordered
      retries: 2
triggers:
  - name: vss-prompt-suggester-scheduled-trigger-1
    vrn: vast:dataengine:triggers:vss-prompt-suggester-scheduled-trigger
    # Set schedule in DataEngine trigger config (e.g. every 5–15 minutes).

```


## FILE: vss-blueprint/deployments/dataengine-vss-ingest-pipeline/vss-cli-secret-file-template.yaml
Source: https://github.com/vast-data/vss-blueprint/blob/main/deployments/dataengine-vss-ingest-pipeline/vss-cli-secret-file-template.yaml

```
# Video VSS Blueprint - Pipeline Secret
# Used by all ingest pipeline functions
#
# Usage:
#   vastde pipelines create --config deployment/data-engine-pipeline/ingest-pipeline.yaml --secret-file deployment/data-engine-pipeline/vss-video-ingest-secret-template.yaml

name: vss2-secret

kubernetes_cluster_vrn: <your-kubernetes-cluster-vrn>
namespace: <YOUR_NAMESPACE>

entries:
  # S3 Settings
  # Used by: video-segmenter, video-reasoner
  - key: s3accesskey
    value: ""

  - key: s3secretkey
    value: ""

  - key: s3endpoint
    value: ""

  # Cosmos-Reason2 Settings
  # Function: video-reasoner
  - key: cosmos_host
    value: ""

  - key: cosmos_port
    value: ""

  - key: cosmoshttpscheme
    value: "http"

  # - key: cosmos_authorization
  #   value: ""

  - key: cosmos_model
    value: "nvidia/cosmos-reason2-8b"

  - key: cosmos_max_tokens
    value: "6000"

  - key: cosmos_temperature
    value: "0.2"

  # Cosmos-Embed1 (used by: video-embedder)
  - key: embedding_local_nim
    value: "true"

  - key: embeddinghost
    value: "127.0.0.1"

  - key: embeddingport
    value: "8002"

  - key: embeddinghttpscheme
    value: "http"

  # - key: embedding_authorization
  #   value: ""  # optional Bearer token for hosted/routed embedding APIs (e.g. gateway)

  - key: embeddingmodel
    value: "nvidia/cosmos-embed1"

  - key: embeddingdimensions
    value: "256"
  - key: visual_embedding_enabled
    value: "true"
  - key: visual_embedding_model
    value: "nvidia/cosmos-embed1"
  - key: visual_embedding_dimensions
    value: "256"

  # nvidia_api_key: required when embedding_local_nim is false
  - key: nvidia_api_key
    value: ""

  # Video Reasoner Settings
  # Used by: video-reasoner
  - key: max_video_size_mb
    value: "100"

  - key: scenario
    value: "general"

  # VastDB Settings
  # Used by: video-vastdb-writer
  # Note: embeddingdimensions (above) is also used by video-vastdb-writer
  #       to create the vector column schema. Must match your embedding model.
  - key: vdbendpoint
    value: "http://"

  - key: vdbbucket
    value: "vss-db"

  - key: vdbschema
    value: "vss-schema"

  - key: vdbaccesskey
    value: ""

  - key: vdbsecretkey
    value: ""

  - key: vdbcollection
    value: "vss-collection"

  # Prompt suggester (scheduled function + shared with ingest secret vss2-secret)
  - key: vdbpromptscollection
    value: "vss-prompts-events"

  - key: suggestions_max_segments
    value: "48"

  - key: suggestions_search_count
    value: "10"

  - key: suggestions_events_count
    value: "30"

  - key: suggestions_max_events_per_video
    value: "3"

  - key: suggestions_lookback_hours
    value: "168"

  # Video Segmenter Settings
  # Used by: video-segmenter
  - key: segment_duration
    value: "5"

  - key: output_codec
    value: "libx264"

  - key: output_format
    value: "mp4"

  - key: output_bucket_suffix
    value: "-segments"

  # YOLO11 object detector (video-detector)
  - key: yolo_infer_host
    value: ""

  - key: yolo_infer_port
    value: "8022"

  # - key: detector_authorization
  #   value: ""

  - key: yolo_conf
    value: "0.4"

  - key: yolo_model
    value: "yolo11s.pt"

  - key: yolo_presign_ttl
    value: "3600"

  - key: detection_sidecar_prefix
    value: "detections/"

  - key: detection_store_frames
    value: "true"
```


## FILE: vss-blueprint/.cursor/skills/dataengine-function/SKILL.md
Source: https://github.com/vast-data/vss-blueprint/blob/main/.cursor/skills/dataengine-function/SKILL.md

```
---
name: dataengine-function
description: >-
  Author VAST DataEngine serverless functions (init/handler, VastEvent, vss2-secret,
  VastDB SDK, OpenTelemetry). Use when creating or changing DataEngine functions,
  enrichment/ingest pipelines, vastde deploys, scheduled triggers, or prompt-suggester-style jobs.
---

# DataEngine serverless functions (VSS blueprint)

Follow existing functions under `source-code/ingest/*` and `source-code/enrichment/*` before inventing new structure.

## Layout

```
<function-name>/
├── main.py              # init(ctx), handler(ctx, event: VastEvent)
├── requirements.txt     # standard stack + function-specific deps
├── README.md            # secret keys, deploy notes
└── common/
    ├── models.py        # Settings.from_ctx_secrets, event/result models
    ├── vastdb_client.py # VastDB connect, select/insert (if needed)
    ├── vastdb_patch.py  # vector-column select patch (if reading collection table)
    └── …                # domain logic (LLM client, parsers, etc.)
```

## Entry points

```python
from opentelemetry import trace
from vast_runtime.vast_event import VastEvent  # type: ignore

def init(ctx):
    """Initialize the serverless function"""
    with ctx.tracer.start_as_current_span("<Name> Initialization"):
        settings = Settings.from_ctx_secrets(ctx.secrets)
        ctx.settings = settings
        ctx.vastdb_client = VastDBClient(settings)  # if VastDB
        ctx.logger.info("[INIT] …")

def handler(ctx, event: VastEvent):
    """Main handler function for vast serverless runtime"""
    with ctx.tracer.start_as_current_span("<Name> Handler") as handler_span:
        try:
            data = event.get_data()
            event_type = getattr(event, "get_type", lambda: "element_trigger")()
            handler_span.set_attribute("event_type", event_type)
            # pipeline: honor data.get("status") == "error"|"skipped" like vastdb-writer
            …
            return {"status": "success", …}
        except Exception as e:
            handler_span.set_attribute("error", True)
            handler_span.record_exception(e)
            ctx.logger.error(f"…: {e}")
            return {"status": "error", "error": str(e)}
```

- **Pipeline functions**: default `event_type` `element_trigger`; parse `event.get_data()` from upstream.
- **Scheduled enrichment**: default `scheduled_trigger`; may ignore empty `data`; use nested spans per phase (fetch → compute → VastDB write).

## Settings (`common/models.py`)

- Load from `secrets["vss2-secret"]` only.
- Field names match secret YAML keys (lowercase, no underscores): `vdbendpoint`, `vdbcollection`, `cosmos_host`, etc.
- Use `from_ctx_secrets` pattern:

```python
@classmethod
def from_ctx_secrets(cls, secrets: Dict[str, Any]) -> "Settings":
    raw = secrets["vss2-secret"]
    config = {k: raw[k] for k in cls.__annotations__ if k in raw}
    return cls(**config)
```

- Add function-specific keys to `deployments/dataengine-vss-ingest-pipeline/vss-gui-secret-file-template.yaml` (and vss2 copy).

## Standard `requirements.txt`

Start **every** DataEngine function (ingest, enrichment, new jobs) with this full block — copy verbatim, do not drop lines:

```
# Cloud events
cloudevents==1.10.1

# VastDB Python SDK and dependencies
vastdb==1.3.2
ibis-framework[duckdb]==9.0.0

# PyArrow for data handling
pyarrow

# Data validation
pydantic==2.5.2
pydantic-settings==2.1.0

# OpenTelemetry for tracing (all four required by DataEngine runtime)
opentelemetry-api==1.38
opentelemetry-sdk==1.38
opentelemetry-exporter-otlp==1.38
opentelemetry-processor-baggage==0.59b0
```

**OpenTelemetry:** include `opentelemetry-processor-baggage==0.59b0` on every function. Older ingest `requirements.txt` files often omitted it — add it whenever you touch deps.

Ingest functions that must carry the full OTel block: `video-segmenter`, `video-reasoner`, `video-embedder`, `vastdb-writer`.

Add only what the function needs below this block, with versions aligned to siblings:

| Need | Add |
|------|-----|
| S3 | `boto3`, `botocore` (see video-segmenter) |
| HTTP / LLM / NIM | `requests==2.31.0` (see video-reasoner) |
| Do **not** add | `httpx`, unpinned `vastdb`, `pandas` unless required |

## VastDB reads on `vss-collection`

Tables include `vectors` / `vectors_visual`. Import `common/vastdb_patch.py` before `table.select()` so vector columns are excluded from projections.

- Use `vastdb.connect(endpoint=…, access=…, secret=…, ssl_verify=False)`.
- Prefer `arrow.to_pylist()` over pandas.
- Client class name: **`VastDBClient`** with `self.bucket`, `self.schema_name`, `self.table_name`.
- Log `[VASTDB]` / `[COMPLETE]` like ingest functions.

## Pipeline YAML

- Ingest: `deployments/dataengine-vss-ingest-pipeline/vss-ingest-pipeline-file.yaml`
- Enrichment (scheduled): `deployments/dataengine-vss-ingest-pipeline/vss-enrichment-pipeline-file.yaml`
- Pattern: `secrets: [vss2-secret]`, `function_deployments`, `links` (trigger → function), `triggers` with Schedule VRN.

## Reference implementations

| Type | Example |
|------|---------|
| Pipeline write | `source-code/ingest/vastdb-writer/` |
| Pipeline LLM | `source-code/ingest/video-reasoner/` |
| Scheduled enrichment | `source-code/enrichment/prompt-suggester/`, `fraud-detection-blueprint/.../fraud-detector/` |

## Checklist for a new function

1. Copy layout + standard `requirements.txt` (including `opentelemetry-processor-baggage==0.59b0`).
2. `Settings` + secret template keys.
3. `init` stores clients on `ctx`; `handler` uses spans and structured return dict.
4. VastDB patch if selecting from collection table.
5. Pipeline YAML + DataEngine function register/build.
6. If output feeds UI/backend, add `vdb_*` / API read path in video-backend secret (`vdb_prompts_collection` pattern).

```


## FILE: vss-blueprint/docs/COSMOS_LOCAL_STACK.md
Source: https://github.com/vast-data/vss-blueprint/blob/main/docs/COSMOS_LOCAL_STACK.md

```
# Local Cosmos stack (Reason2 + Embed1 + YOLO)

Deploy the GPU services with Docker from **[scripts/vss-blueprint-models](../scripts/vss-blueprint-models/README.md)** (`./deploy.sh` on a host with NVIDIA GPUs).

## Services

| Service | Container / image | Host port | Used for |
|---------|-------------------|-----------|----------|
| **Cosmos-Reason2** | `cosmos-reason2-8b` (`nvcr.io/nim/nvidia/cosmos-reason2-8b:1.7.0`) | **8001** | `video-reasoner` (plain `reasoning_content`) + `prompt-suggester` |
| **Cosmos-Embed1** | `cosmos-embed1` (`nvcr.io/nim/nvidia/cosmos-embed1:1.1.0`) | **8002** | `video-embedder` + search backend |
| **YOLO11** | `yolo-infer` (built from `yolo-infer/`) | **8003** | `video-detector` |

## Secret alignment (`vss-gui-secret-file-template.yaml` / CLI / `backend-secret.yaml`)

- `cosmos_host` / `cosmos_port: 8001` / `cosmos_model: nvidia/cosmos-reason2-8b`
- `embeddinghost` / `embeddingport: 8002` / `embeddingmodel: nvidia/cosmos-embed1`
- `embeddingdimensions: 256` (required — Embed1 is **256-dim**, not 2048)
- `yolo_infer_host` / `yolo_infer_port: 8003` (script default; templates may still show `8022`)

Backend `backend-secret.yaml` must use the same embed host/port/model/dimensions for search.

## How embeddings work in code

| Column | Ingest | API |
|--------|--------|-----|
| `vectors` | `reasoning_content` → Cosmos-Embed1 text (`request_type: query` / `bulk_text`) | Text query embed |
| `vectors_visual` | Segment **MP4** → Cosmos-Embed1 video (`data:video/mp4;base64,...`) | Text query embed (same model space) |

Client: `source-code/ingest/video-embedder/common/cosmos_embed_client.py`

## DataEngine networking

Use the IP/hostname that **DataEngine workers** can reach (not always `127.0.0.1` if functions run on another node). Same for the K8s backend calling embed for search.

## VastDB

Recreate the collection when switching to 256-dim vectors (was 2048 for Llama embed models).

```


## FILE: vss-blueprint/scripts/vss-blueprint-models/README.md
Source: https://github.com/vast-data/vss-blueprint/blob/main/scripts/vss-blueprint-models/README.md

```
# VSS GPU models (Reason2, Embed1, YOLO)

Deploy **Cosmos-Reason2**, **Cosmos-Embed1**, and **YOLO11** on a bare-metal GPU host with Docker. Used by the VSS ingest pipeline and K8s backend.

This directory lives at `scripts/vss-blueprint-models/` in [vss-blueprint](../../README.md).

## Quick start

From the **blueprint repo root**:

```bash
cd scripts/vss-blueprint-models
export NGC_API_KEY='<your-ngc-api-key>'
./deploy.sh EMBED_YOLO_GPU REASONER_GPU
```

Example — embed + YOLO on GPU 2, reasoner on GPU 3:

```bash
./deploy.sh 2              # all services on GPU 2
./deploy.sh --embedder --yolo 2
./deploy.sh 2 3 --reasoner-port 8001 --embed-port 8002 --yolo-port 8003
```

Default ports (**8001 / 8002 / 8003**) match VSS convention. Point `cosmos_*`, `embedding*`, and `yolo_infer_*` in `vss2-secret` / `backend-secret.yaml` at a host DataEngine and K8s can reach (not always `127.0.0.1`).

## Contents

| Path | Purpose |
|------|---------|
| `deploy.sh` | Deploy script (Reason2, Embed1, YOLO) |
| `DEPLOY.md` | Full usage, options, troubleshooting |
| `yolo-infer/` | YOLO FastAPI service (`main.py`, `Dockerfile`) |

## Documentation

See **[DEPLOY.md](DEPLOY.md)** for prerequisites, GPU layout, environment variables, health checks, and tear down.

Secret field names: [Ingest pipeline](../../deployments/dataengine-vss-ingest-pipeline/README.md) and [K8s application](../../deployments/vss-k8s-application/README.md). Vector dims / local NIM notes: [COSMOS_LOCAL_STACK.md](../../docs/COSMOS_LOCAL_STACK.md).

```
