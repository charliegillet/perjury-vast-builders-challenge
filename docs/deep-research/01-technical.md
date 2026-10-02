# 01: Build-day technical cheat sheet (UNWATCHED, SF Oct 2 2026)

Each section has copy-pasteable code, a source link, and a verification tag:

- **VERIFIED**: read directly in primary source code or official docs today.
- **UNVERIFIED**: inferred, or the docs disagree. Check it on-site in the first hour.
- **ESTIMATE**: a number we derived, not one that was published.

Raw captures live in `docs/sources/dr-tech-*.md`. They include full source files from `vast-data/vss-blueprint` (commit `9685512`, Sep 9 2026), `vast-data/dataengine-cli` (v5.5.0-sp2 docs), `vast-data/dataengine-pipelines`, `vast-data/vastdb_sdk` (2.0.14.1), `vast-data/vast-vector-store`, `vast-data/vastdb-adbc-driver` and `nvidia-cosmos/cosmos-reason2`.

---

## TL;DR: what changes in our plan

| Question | Answer | Status |
|---|---|---|
| Schedule/cron triggers in DataEngine? | **Yes.** Trigger type `Schedule`, written in **Quartz** cron syntax (UI "Advanced"). The CLI is `vastde triggers create schedule --cron-schedule ...`. The blueprint's own prompt-suggester already runs on one. | VERIFIED |
| Cron timezone? | Event timestamps are UTC (`+00:00`). The docs never state a timezone. | UNVERIFIED. Use the "every-minute + wall-clock guard" pattern (section 2.6) |
| DB-row triggers? | **No.** There are only two trigger types: `Element` (S3 `ObjectCreated:*`, `ObjectRemoved:*`, `ObjectTagging:Put/Delete`) and `Schedule`. | VERIFIED |
| Kafka-topic triggers? | Not a trigger type. Topics are the transport for triggers and links. Function→function hops are `links` in the pipeline manifest, and you can route conditionally with `event.set_trigger_labels()` (5.5 SDK). | VERIFIED (labels: 5.5 docs) |
| Native vector search in VastDB? | **Yes, through the Query Engine (ADBC driver + SQL).** The blueprint runs `array_cosine_distance(vectors_visual::FLOAT[256], ARRAY[...]::FLOAT[256])` with `ORDER BY distance LIMIT k`. That is brute force unless the table has a vector index (SDK ≥2.0: `VectorIndexSpec(col, 'l2sq'|'ip')`, `table.vector_search()`). | VERIFIED |
| Can the plain `vastdb` SDK read vector columns? | **No, not reliably.** The blueprint monkey-patches the SDK to *drop* vector columns from `select()`. Read vectors through ADBC SQL, or carry them in the event payload. | VERIFIED |
| Embedding dims | Cosmos-Embed1 = **256-d** for both text (`vectors`) and visual (`vectors_visual`) | VERIFIED |
| Segment length | **5 s** (`segment_duration: "5"`), not the 10 s we assumed. A 10 s webcam chunk becomes 2 segments. | VERIFIED |
| Does Cosmos-Reason2 run on 100% of segments in the blueprint? | **Yes.** The `video-reasoner` captions every segment, and the embedder **skips segments with no caption**, which means no row and no visual vector. Our "Cosmos only on 3%" claim is true for the *verify* call only. | VERIFIED. **Fix the pitch wording** |
| Cosmos-Reason2 latency per 5 s clip | **Not published** ("will be published shortly", HF card). Measure on-site: `SELECT avg(processing_time)` on the segments table. | ESTIMATE below |
| W&B Inference Nemotron IDs | `nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B`, `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B` | VERIFIED (docs updated Sep 29 2026) |

---

## 1. vss-blueprint internals

Repo: https://github.com/vast-data/vss-blueprint (captured in `dr-tech-vss-blueprint-pipeline.md` and `dr-tech-vss-blueprint-functions.md`)

### 1.1 Pipeline topology (VERIFIED, `deployments/dataengine-vss-ingest-pipeline/vss-ingest-pipeline-file.yaml`)
```
video-chunk-land-trigger (Element, bucket vss-chunks, ObjectCreated:*)  → video-segmenter
video-segment-land-trigger (Element, bucket vss-chunks-segments)        → video-detector → video-reasoner → video-embedder → video-vastdb-writer
vss-prompt-suggester-scheduled-trigger (Schedule)                       → prompt-suggester      (enrichment pipeline)
```
- The segmenter writes `segments/{base}_segment_{NNN}_of_{TTT}.mp4` into `<bucket>-segments`, and that write fires the second trigger.
- Detector→reasoner→embedder→writer are **function→function links**. Each function's **return dict becomes the next function's `event.get_data()`**.
- Every function returns `{"status": "error"|"skipped", ...}` on failure. Downstream functions check `data.get("status")` and skip.

Manifest shape to copy for our own pipeline:
```yaml
kubernetes_cluster_vrn: <vastde compute-clusters list>
namespace: <ns>
name: unwatched-pipeline
manifest:
  config:
    environment_variables: []
    secrets: [vss2-secret]          # reuse the blueprint secret (same keys)
  function_deployments:
    - function_vrn: vast:dataengine:functions:nw-scorer
      name: nw-scorer-1
      revision: 1
      config: {log_level: INFO}
      resources: {min_cpu: 200m, max_cpu: 1000m, min_memory: 256Mi, max_memory: 512Mi,
                  min_concurrency: 1, max_concurrency: 5, timeout: 300}
  links:
    - source: [nw-digest-tick-1]
      destination: [nw-digest-1]
      topic: vast:dataengine:topics:<broker-name>/<topic>
      config: {events_order: unordered, retries: 2}
  triggers:
    - name: nw-digest-tick-1
      vrn: vast:dataengine:triggers:nw-digest-tick   # trigger must already exist (name must match)
```

### 1.2 Handler interface (VERIFIED, every `source-code/ingest/*/main.py`)
```python
from opentelemetry import trace
from vast_runtime.vast_event import VastEvent  # type: ignore   # blueprint import (pre-5.5 style)

def init(ctx):                          # once per pod start
    with ctx.tracer.start_as_current_span("X Init"):
        raw = ctx.secrets["vss2-secret"]          # dict of secret entries: raw["vdbendpoint"], ...
        ctx.settings = raw

def handler(ctx, event: VastEvent):     # per event; may be `async def`
    with ctx.tracer.start_as_current_span("X Handler") as span:
        data = event.get_data()          # S3 event dict OR upstream function's return dict
        if data.get("status") in ("error", "skipped"):
            return {"status": "skipped", "reason": data.get("reason") or data.get("error")}
        ctx.logger.info("[INPUT] ...")
        return {"status": "success", **data}      # dict/str is auto-wrapped as next VastEvent
```
The 5.5 Runtime SDK docs import `from vast.dataengine.sdk import VastEvent, Context, VastEventList, event_batching_handler` (source: https://kb.vastdata.com/documentation/docs/event-handling-55). The blueprint uses `vast_runtime.vast_event`. **Copy the blueprint's import.** It is proven against the event's cluster version.

Typed casts in 5.5: `event.as_element_event()`, `event.as_schedule_event()` (gives `.cron_schedule`, `.timer_elapsed_timestamp`), `event.as_function_event()`.

S3 element event payload (VERIFIED, from a real log in `dataengine-pipelines/python-s3-hello-world/README.md`):
```python
data["Records"][0]["s3"]["bucket"]["name"], data["Records"][0]["s3"]["object"]["key"]   # key is URL-encoded → urllib.parse.unquote
# event type: 'vastdata.com:Element.ElementCreated'; eventName 'ObjectCreated:Put'
```
Schedule event (VERIFIED, real log): `type: 'vastdata.com:Schedule.TimerElapsed'`, `data: {'message': 'Activating trigger by cron'}`, `cronschedule: '0 0/5 * ? * * *'`, `time: '...+00:00'` (UTC).

### 1.3 Secret `vss2-secret` keys (VERIFIED, `vss-cli-secret-file-template.yaml`)
`s3accesskey s3secretkey s3endpoint | cosmos_host cosmos_port(8001) cosmoshttpscheme cosmos_authorization? cosmos_model(nvidia/cosmos-reason2-8b) cosmos_max_tokens(6000) cosmos_temperature(0.2) | embedding_local_nim embeddinghost embeddingport(8002) embeddingmodel(nvidia/cosmos-embed1) embeddingdimensions(256) visual_embedding_enabled visual_embedding_dimensions(256) nvidia_api_key | max_video_size_mb scenario | vdbendpoint vdbbucket(vss-db) vdbschema(vss-schema) vdbaccesskey vdbsecretkey vdbcollection(vss-collection) vdbpromptscollection(vss-prompts-events) | segment_duration(5) output_bucket_suffix(-segments) | yolo_infer_host yolo_infer_port(8003, template says 8022) yolo_conf(0.4) yolo_model(yolo11s.pt) detection_sidecar_prefix(detections/)`

Secret file format for `--secret-file`:
```yaml
name: nw-secret
kubernetes_cluster_vrn: <vrn>
namespace: <ns>
entries:
  - {key: slack_bot_token, value: ""}
  - {key: wandb_api_key,   value: ""}
```
**Do not commit filled-in copies.**

### 1.4 VastDB segment table schema (VERIFIED, `vastdb-writer/common/vastdb_client.py`)
Table path: `vss-db` / `vss-schema` / `vss-collection` (from the secret). One row per 5 s segment. The writer dedupes on `source` and **skips rows with an empty `reasoning_content`**.
```
pk utf8 | source utf8 (s3://vss-chunks-segments/segments/..._segment_003_of_012.mp4) | filename | segment_number uint32
segment_start_sec f64 | segment_end_sec f64 | reasoning_content utf8 (≤1024 chars) | perception_json string
object_classes utf8 ("person,chair") | object_counts utf8 (JSON {"person":2} = PEAK concurrent per class)
max_detection_conf f32 | perception_ok bool | perception_source | detection_sidecar_uri | detection_frame_count | detection_count
vectors        list<float32, 256>   # Cosmos-Embed1 TEXT embedding of reasoning_content
vectors_visual list<float32, 256>   # Cosmos-Embed1 VIDEO embedding of the segment mp4 ; ZERO-FILLED if visual embed failed!
cosmos_model | embedding_model | visual_embedding_model | tokens_used i32 | cached_prompt_tokens i32
processing_time f64   # ← Cosmos-Reason2 wall-clock seconds for this segment's caption = free latency benchmark
timestamp utf8 | allowed_users list<utf8> | is_public bool | upload_timestamp timestamp[ns] | duration f64
total_segments uint32 | original_video utf8 | tags list<utf8> | camera_id utf8 | capture_type utf8 | location utf8
extra_metadata string (JSON: stream_id, chunk_index, chunk_start_sec, stream_position_sec, ingest_kind, visual_embedding_ok)
```
**How to set `camera_id`:** S3 object metadata on the upload. The keys are `camera-id`, `capture-type`, `location`, `scenario`, `custom-prompt` (URL-encoded, ≤800 chars), `tags`, `is-public`, `stream_id`, `chunk_index`, `capture_timestamp` (VERIFIED, `video-segmenter/common/models.py`, `shared/ingest_metadata.py`):
```python
import boto3, urllib.parse
s3 = boto3.client("s3", endpoint_url=S3_ENDPOINT, aws_access_key_id=AK, aws_secret_access_key=SK,
                  verify=False, config=boto3.session.Config(signature_version="s3v4", s3={"addressing_style": "path"}))
s3.upload_file("chunk.mp4", "vss-chunks", f"cam-05-live/{ts}.mp4",
    ExtraArgs={"Metadata": {"camera-id": "cam-05-live", "location": "stage-corner",
                            "capture-type": "streets", "scenario": "surveillance", "is-public": "true",
                            "custom-prompt": urllib.parse.quote("Describe objects on the table ...", safe="")}})
```
Hold the custom prompt to 800 characters or fewer. It *replaces* the scenario prompt. The reasoner then appends YOLO classes and the plain-text instruction.

### 1.5 Cosmos-Reason2 call and caption prompt used by the reasoner (VERIFIED, `video-reasoner/common/clients.py`, `prompts.py`, `reasoning_prompt.py`)
- URL: `{cosmoshttpscheme}://{cosmos_host}:{cosmos_port}/v1/chat/completions` (OpenAI-compatible NIM).
- Payload: `messages=[{"role":"user","content":[{"type":"text","text":prompt},{"type":"video_url","video_url":{"url":"data:video/mp4;base64,<b64>"}}]}]`, `max_tokens=cosmos_max_tokens`, `temperature=0.2`. It sends **no** `media_io_kwargs`, so the NIM default is 4 fps. It does **not** use `<think>`.
- `surveillance` scenario prompt: *"Analyze this surveillance footage. Focus on people, unusual behavior, safety hazards, abandoned objects, vehicles, crowds, and security concerns. Be specific about locations within the frame."* Other scenarios: `traffic, live_driving, nhl, sports, retail, warehouse, egocentric, general (default), nyc_control, nyc_safety_surveillance`.
- Appended: `"Detected objects in this clip: {yolo classes}."` and a plain-prose instruction ("dense, searchable description… colors; brand/logo; vehicle type; sign text; exact counts only when obvious; main action; likely next move… under 1024 characters").
- Error handling: 401/403/408/429/5xx raise `TransientError`, so the pipeline redelivers (`retries: 3`).

### 1.6 Embedder and vector storage (VERIFIED, `video-embedder/main.py`, `common/cosmos_embed_client.py`)
- Text: `POST {embed}/v1/embeddings {"input": reasoning_content, "model":"nvidia/cosmos-embed1", "request_type":"query", "encoding_format":"float"}` gives `vectors`.
- Visual: downloads the segment mp4, then `{"input": "data:video/mp4;base64,<b64>", "request_type":"query", ...}` gives `vectors_visual`. On failure it continues text-only and the writer fills **zeros**. **Filter `json_extract(extra_metadata,'$.visual_embedding_ok')` or norm>0 before scoring** (cosine of a zero vector is NaN).
- Its output event carries **everything**: `visual_embedding` (list[256]), `embedding`, `object_counts`, `camera_id`, `segment_*`, `reasoning_content`, `upload_timestamp`, `source`. **Design implication:** link `video-embedder → [video-vastdb-writer, nw-scorer]` (fan-out). The scorer then has the visual vector in `event.get_data()["visual_embedding"]` with **no DB read**. The writer's return is tiny (no vectors), so linking *after* the writer would force an ADBC read.

### 1.7 YOLO detector (VERIFIED, `scripts/vss-blueprint-models/yolo-infer/main.py`, `video-detector/README.md`)
- FastAPI: `POST :8003/v1/infer {"video_base64": "...", "filename": "seg.mp4", "include_frames": true}` (or `{"url": presigned}`). `GET /healthz`. Model `yolo11s.pt`, conf 0.4, `model.predict(stream=True)` over every frame. **There is no tracker, so IDs are not unique.**
- `object_counts` in the row = **max boxes of a class in any single frame** (peak concurrency). Use it directly as the class-z feature.
- Sidecar `s3://vss-chunks-segments/detections/{segment_stem}.json.gz` holds per-frame bboxes for the keyframe burn-in.

### 1.8 Backend agent API (VERIFIED, `retrieval/video-backend/README.md`)
`POST /api/v1/auth/login {username,password}` (VAST creds) returns a JWT. Then `POST /api/v1/agent/ask {question, original_video?, top_k}`, `POST /api/v1/agent/search-and-answer` (full `VideoSearchRequest`: `query, top_k, time_filter('5m'|'15m'|'1h'|'24h'|...), metadata_filters {"camera_id": "cam-05-live"}, min_similarity`), `GET /api/v1/tools/segment?source=…`, `GET /api/v1/tools/detections?source=…`.

---

## 2. DataEngine function authoring

CLI docs: https://github.com/vast-data/dataengine-cli/tree/main/docs/references/commands (captured in `dr-tech-dataengine-cli-reference.md`). Examples: https://github.com/vast-data/dataengine-pipelines

### 2.1 Install and log in (VERIFIED)
```bash
curl -fsSL -o vastde https://github.com/vast-data/dataengine-cli/releases/download/v5.5.0-sp2/vastde_darwin_arm64 && chmod +x vastde && sudo mv vastde /usr/local/bin
vastde config init
vastde config set --vms-url https://<vms> && vastde config set --username <u> --password <p> --tenant <t>
vastde functions list && vastde compute-clusters list && vastde topics list && vastde buckets list
vastde doc   # regenerates full CLI docs locally, use it if flags differ on the event build
```

### 2.2 Scaffold, build, push, register (VERIFIED)
```bash
vastde functions init python-pip nw-scorer          # main.py, requirements.txt, Aptfile, customDeps, README.md
# requirements.txt: copy the blueprint block verbatim (SKILL.md):
#   cloudevents==1.10.1 vastdb==1.3.2 ibis-framework[duckdb]==9.0.0 pyarrow pydantic==2.5.2 pydantic-settings==2.1.0
#   opentelemetry-api==1.38 opentelemetry-sdk==1.38 opentelemetry-exporter-otlp==1.38 opentelemetry-processor-baggage==0.59b0
#   + requests==2.31.0 (HTTP) / boto3 (S3) / confluent-kafka==2.8.* (if producing) / slack_sdk / weave
cd nw-scorer && vastde functions build nw-scorer --image-tag v1          # Docker must run; default Python 3.12.*
docker tag nw-scorer:v1 <registry-host>/<org>/nw-scorer:v1 && docker push <registry-host>/<org>/nw-scorer:v1
#   (Apple Silicon: DataEngine targets linux/amd64. If the build output is arm64, see Gotcha #6)
vastde functions create --name nw-scorer --container-registry <registry-name-in-VMS> \
  --artifact-source <org>/nw-scorer --artifact-type image --image-tag v1
# new code later:
vastde functions update nw-scorer --image-tag v2 --publish     # then bump `revision:` in pipeline yaml / redeploy
```
Local loop, without the cluster:
```bash
vastde functions localrun nw-scorer -c config.yaml            # config.yaml: {envs: {...}, secrets: {...}}
vastde functions invoke --generate-event --url http://localhost:8080/
vastde functions invoke --event my-event.yaml --url http://localhost:8080/   # custom CloudEvent
vastde functions invoke --generate-event --event-type vastdata.com:Element.ObjectCreated
```

### 2.3 Triggers (VERIFIED)
```bash
# S3 element trigger (prefix filter is useful: only the live cam)
vastde triggers create element --name nw-live-land --event "ObjectCreated:*" \
  --source-bucket vss-chunks --name-prefix "cam-05-live/" --broker-type Internal --broker-name <broker> --topic-name <topic>
# Schedule trigger
vastde triggers create schedule --name nw-baseline-15m --cron-schedule "0 0/15 * ? * * *" \
  --broker-type Internal --broker-name <broker> --topic-name <topic>
vastde triggers list
```
- The **UI** Schedule trigger takes **Quartz** syntax: `sec min hour dom month dow [year]`. The repo example `0 0/5 * ? * * *` means every 5 minutes. The CLI help example shows 5-field `"0 * * * *"`, so the two disagree. **Use the Quartz 7-field form, which is the one proven in the repo README.** (UNVERIFIED which form the CLI accepts. Try `--dry-run`.)
- 15:31 PDT = **22:31 UTC**, giving `0 31 22 ? * * *` *if* the scheduler runs in UTC (UNVERIFIED).
- There are no DB-row or topic-consumer trigger types. Allowed element events: `ObjectCreated:*`, `ObjectRemoved:*`, `ObjectTagging:Put`, `ObjectTagging:Delete`.

### 2.4 Pipelines, logs, traces (VERIFIED)
```bash
vastde pipelines create --config @pipeline.yaml --secret-file nw-secret.yaml --deploy
vastde pipelines deploy <name>     # or: vastde pipelines update <name> --config @pipeline.yaml
vastde logs tail <pipeline> --function nw-scorer --since 10m          # --severity ERROR, --trace-id
vastde logs get  <pipeline> --function nw-verifier --since 1h --output json
vastde traces list <pipeline> --since 15m --status ERROR              # default --since is 1m!
vastde traces get <trace-id>
vastde topics list
```
`vastde logs tail` is the "under the hood" screen for the Ram/Brian judges.

### 2.5 Conditional routing replaces the Kafka hop (VERIFIED in 5.5 docs, UNVERIFIED on the event cluster)
In `nw-scorer`, label the event and add a labeled link `nw-scorer → nw-verifier` (label `route=candidate`):
```python
def handler(ctx, event):
    d = event.get_data()
    ...
    if is_candidate:
        event.set_trigger_labels({"route": "candidate"})
    else:
        event.set_trigger_labels({"noRoute": "skip"})   # empty dict raises ValueError
    return {**slim_payload}
```
Hop-by-hop only. All labels on a link must match. `ctx.pipeline_triggers_map` shows the downstream links. Source: https://kb.vastdata.com/documentation/docs/event-handling-55

If you still want an explicit Kafka topic (Event Broker), use **confluent-kafka 2.4–2.8 only** (aiokafka is unsupported). Topics must be **pre-created**: there is no auto-create, no compression, no transactions, no idempotent producer, and **values are capped at 126 KB**. **Never put base64 video on the topic.** Pass `source` URIs. Source: https://kb.vastdata.com/documentation/docs/kafka-protocol-support
```python
from confluent_kafka import Producer
p = Producer({"bootstrap.servers": "<broker-VIP>:9092"})          # port UNVERIFIED, ask VAST staff
p.produce("nw.candidates", key=seg_id, value=json.dumps(payload)); p.flush(5)
```

### 2.6 The 15:31 digest: make it robust (recommended pattern)
Use a Schedule trigger **every minute** (`0 0/1 * ? * * *`). The function itself decides whether to post, which makes it timezone-proof and idempotent:
```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
def handler(ctx, event):
    now = datetime.now(ZoneInfo("America/Los_Angeles"))
    if not (now.hour == 15 and now.minute >= 31) or already_posted_today():   # check nw_digests row
        return {"status": "skipped", "reason": "not digest time"}
    post_digest(); record_posted()
```
Fallback if schedule triggers aren't permitted for our user: put the same function on a laptop `launchd`/`cron`, or `while True: sleep(30)`. Say so honestly in the pitch.

---

## 3. Vector search in VastDB

Captured in `dr-tech-vastdb-vector-search.md`.

### 3.1 What the blueprint does (VERIFIED, `retrieval/video-backend/src/services/vastdb_service.py`)
```python
import adbc_driver_manager.dbapi   # pip install adbc-driver-manager==1.0.0
DRIVER = "/opt/adbc-driver/libadbc_driver_vastdb.so"   # repo ships an x86-64 Linux .so (12.7 MB)
# fallback download used by the blueprint:
# https://artifactory.vastdata.com/files/vastdb-native-client/1955131/libadbc_driver_vastdb.so
with adbc_driver_manager.dbapi.connect(driver=DRIVER, db_kwargs={
        "vast.db.endpoint": VDB_ENDPOINT, "vast.db.access_key": AK, "vast.db.secret_key": SK}) as conn:
    with conn.cursor() as cur:
        q = f'''SELECT source, camera_id, reasoning_content, object_counts,
                       array_cosine_distance(vectors_visual::FLOAT[256], ARRAY{centroid}::FLOAT[256]) AS distance
                FROM "vss-db/vss-schema"."vss-collection"
                WHERE camera_id = 'cam-05-live'
                ORDER BY distance DESC LIMIT 20'''          # DESC = most anomalous first
        cur.execute(q); tbl = cur.fetch_arrow_table()
```
- Table path quoting: `"bucket/schema"."table"`.
- Cosine distance = `1 - similarity`. The blueprint converts it with `similarity = 1.0 - distance`.
- Hybrid search runs the text branch (`vectors`) and the visual branch (`vectors_visual`) separately and merges them.

### 3.2 SDK-native path (VERIFIED in `vastdb_sdk` 2.0.14, UNVERIFIED on the event cluster version)
```python
# pip install 'vastdb[adbc]'   (pulls adbc-driver-vastdb~=0.0.25, may have a mac wheel: UNVERIFIED)
from vastdb._internal import VectorIndexSpec
schema.create_table("nw_x", arrow_schema, vector_index=VectorIndexSpec("embedding", "l2sq"))  # metrics: 'l2sq' | 'ip' ONLY
reader = table.vector_search(vec=q.tolist(), columns=["id", "camera_id"], limit=10, predicate=table["camera_id"] == "cam-05")
```
The blueprint pins **`vastdb==1.3.2`**, and `vector_search()` does not exist there. Stick with raw ADBC SQL. `langchain-vastdb` maps `cosine` to `cosine_distance(...)` and `l2sq` to `array_distance`, `ip` to `array_inner_product`. Session settings for ANN: `vast.db.setting.vector_search_min_prob`, etc.

### 3.3 Recommendation for `nw-scorer` (design, low risk)
- Get the vector from the **embedder event** (fan-out link). There is no DB read.
- Keep the per-camera centroid as a running mean in `nw_baseline.centroid list<float32,256>`, plus `n`, p50/p95/p99 of recent distances. Read and write it with the normal SDK, which works because the `select()` patch only breaks *vector* projections on the **segments** table. If our own list column also gets dropped, store the centroid as a JSON string. UNVERIFIED.
- Score in Python: `d = 1 - dot(v,c)/(|v||c|)`. Skip if `|v| == 0`.
- Use ADBC SQL only for dashboard "top-k most anomalous" and live queries ("Run a VastDB query live" demo beat).

VastDB SDK basics (VERIFIED, `.firecrawl/vastdb-sdk.md`):
```python
import vastdb, pyarrow as pa
from ibis import _
s = vastdb.connect(endpoint=EP, access=AK, secret=SK, ssl_verify=False)
with s.transaction() as tx:
    sch = tx.bucket("vss-db").schema("vss-schema")
    t = sch.table("nw_scores", fail_if_missing=False) or sch.create_table("nw_scores", pa.schema([...]))
    t.insert(pa.Table.from_pylist(rows, schema=t.arrow_schema))
    rows = t.select(columns=["segment_id","score"], predicate=(_.camera_id == "cam-05-live") & (_.score > 0.3)).read_all().to_pylist()
# snapshots: bucket.list_snapshots()[0].schema('s').table('t').select()
```

---

## 4. Cosmos-Reason2 and Cosmos-Embed1

### 4.1 Reason2 request format (VERIFIED, NIM 1.7.0 docs, https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html)
Model IDs: `nvidia/cosmos-reason2-8b`, `nvidia/cosmos-reason2-2b`. The blueprint image is `nvcr.io/nim/nvidia/cosmos-reason2-8b:1.7.0` on port **8001**.

Three video input forms:
1. `{"type":"video_url","video_url":{"url":"https://...mp4"}}` (the NIM downloads it)
2. `{"type":"video_url","video_url":{"url":"data:video/mp4;base64,<b64>"}}` (what the blueprint uses)
3. `{"type":"video_frames","video_frames":["data:image/jpeg;base64,<f1>", ...]}` keeps temporal order and uses fewer tokens than separate `image_url`s

```python
from openai import OpenAI
import base64
cosmos = OpenAI(base_url=f"http://{COSMOS_HOST}:8001/v1", api_key="not-used")   # or Bearer cosmos_authorization
b64 = base64.b64encode(open("seg.mp4","rb").read()).decode()
VERIFY_SUFFIX = ("\nAnswer the question in the following format: <think>\nyour reasoning\n</think>\n\n"
                 "<answer>\nyour answer\n</answer>.")
r = cosmos.chat.completions.create(
    model="nvidia/cosmos-reason2-8b",
    messages=[{"role":"user","content":[
        {"type":"video_url","video_url":{"url":f"data:video/mp4;base64,{b64}"}},
        {"type":"text","text": VERIFY_PROMPT + VERIFY_SUFFIX}]}],
    max_tokens=2048, temperature=0.3, top_p=0.3, stream=True,
    extra_body={"media_io_kwargs": {"video": {"fps": 2.0}},                       # default 4.0; fps>actual → HTTP 400
                "mm_processor_kwargs": {"size": {"shortest_edge": 1568, "longest_edge": 262144}}})  # smaller = faster
for ch in r:
    if ch.choices and ch.choices[0].delta.content: stream_to_dashboard(ch.choices[0].delta.content)
```
- `fps` and `num_frames` are mutually exclusive. Asking for more fps or frames than the video has returns a **400**.
- Default pixel budget: `shortest_edge=3136, longest_edge=12845056` per image, about 2×longest_edge per 2-frame temporal group for video. One token = 32×32×2 px. The model is tested best at **≤16k multimodal tokens**.
- Reasoning: the HF card says to put the `<think>/<answer>` suffix in the **system** prompt. The NIM doc appends it to the **user** prompt. Both work. Use **max_tokens ≥ 4096** to avoid truncated CoT (HF card), or cap at ~1024–2048 for latency and repair the JSON.
- 8B-only option: `-e NIM_VIDEO_PRUNING_RATE=0.3` (EVS) prunes 30% of frames. 2B doesn't support it.
- GPU memory: 2B ≥24 GB, 8B ≥32 GB. Context up to 256K, but the vLLM recipe uses `--max-model-len 16384`.
- Timestamps: "recognizes timestamps added at the bottom of each frame". Burn `ffmpeg drawtext` timestamps into the frames to get better `evidence_t`.

### 4.2 Grounding / bbox (PARTIAL)
- VERIFIED: the official prompt (`cosmos-reason2/prompts/2d_grounding.yaml`) is `"Locate the bounding box of {object_name}. Return a json."`. Point coordinates are **normalized 0–1000**, origin top-left, independent per axis (NIM docs, 2D trajectory section). Grounding is documented for **image** inputs.
- UNVERIFIED: the output shape. The model is Qwen3-VL based, so expect `[{"bbox_2d":[x1,y1,x2,y2],"label":"..."}]` in 0–1000 space. Convert with `px = v/1000*W`. **Ground on a single keyframe image** (the frame at `evidence_t`) in a second, cheap call rather than asking for a bbox inside the video verify JSON. Fallback: use the YOLO sidecar bbox of the `person`/object class closest to `evidence_t`.

### 4.3 Hosted build.nvidia.com (RISK)
`https://integrate.api.nvidia.com/v1/chat/completions` lists `nvidia/cosmos-reason2-8b` in `/v1/models`, yet a Jan 2026 forum thread reports **`404 Function not found for account`**. Also, build.nvidia.com now redirects to **cosmos3-nano-reasoner** (Cosmos 3, and the cosmos-reason2 repo says it is in maintenance mode). The free tier is **~40 RPM** per user (`.firecrawl/nim-cosmos-reason2.md`). **Use the venue's self-hosted NIM (the `cosmos_host` in the provided secret).** Only use the hosted endpoint as a fallback, and test it at 10:00.

### 4.4 Latency (ESTIMATE, measure first)
No official per-clip numbers exist. Measure in 30 seconds on-site:
```sql
SELECT cosmos_model, count(*) n, avg(processing_time) avg_s, max(processing_time) max_s, avg(tokens_used) tok
FROM "vss-db/vss-schema"."vss-collection" GROUP BY cosmos_model
```
That is the real caption latency per 5 s segment (non-reasoning, ≤1024 chars) on the shared GPU. Our estimate: 8B caption **~2–5 s**, 2B **~1–2 s**. With `<think>`, add **~300–1000 tokens of CoT**, which is **+5–15 s for 8B** (UNVERIFIED, depends on GPU and contention). On stage: stream the tokens, use fps 2, use the smaller pixel budget, and cap max_tokens at 1024.

### 4.5 Cosmos-Embed1 (VERIFIED, https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html)
`POST :8002/v1/embeddings`, model `nvidia/cosmos-embed1` (224p variant), **256-d**, with no `dimensions` param.
```python
requests.post(f"http://{EMB}:8002/v1/embeddings", json={"model":"nvidia/cosmos-embed1","request_type":"query",
      "input":"a person picks up a box from a table","encoding_format":"float"}).json()["data"][0]["embedding"]
# video: "input": "data:video/mp4;base64,<b64>"  (query mode ONLY for full base64 video)
# bulk:  request_type "bulk_video", ≤64 items, each "data:video/mp4;presigned_url,<url>" or 8-frame "data:video_frames/jpg;base64,{f0,...,f7}"
# bulk_text ≤64 strings. Recommended clip ≤15 s. Health: GET /v1/health/ready ; metrics: GET /health/metrics
```
Text and video share one space, so `text→video` similarity works. That enables a bonus "describe the anomaly you want to whitelist" feature.

---

## 5. W&B Inference and Weave

### 5.1 Inference (VERIFIED, https://docs.coreweave.com/products/inference/serverless/models and /api-reference)
`docs.wandb.ai/inference/*` now redirects to CoreWeave docs.
```python
import openai
llm = openai.OpenAI(base_url="https://api.inference.wandb.ai/v1",
                    api_key=WANDB_OR_FORGE_KEY,          # docs now say "CoreWeave Forge API key"; W&B key worked historically
                    project="<team>/<project>")          # usage attribution; default project "inference"
r = llm.chat.completions.create(model="nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B", messages=[...], max_tokens=800)
```
| Role | Model ID |
|---|---|
| Digest (quality) | `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B` (262k ctx, MoE 55B active) |
| Baseline summary / fast | `nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B` (3B active) |
| Alternatives | `openai/gpt-oss-20b`, `meta-llama/Llama-3.1-8B-Instruct`, `Qwen/Qwen3.6-35B-A3B` (vision), `google/gemma-4-26B-A4B-it` (vision) |

Limits: concurrency is capped **per W&B project and per user** and returns `429 Concurrency limit reached for requests`. The free tier caps spend at $100/month. Nemotron models may emit reasoning, so strip `<think>` before posting to Slack (UNVERIFIED).

### 5.2 Weave quickstart (VERIFIED, https://docs.wandb.ai/weave/guides/tracking/feedback, /core-types/evaluations)
```python
import weave, asyncio
client = weave.init("<team>/unwatched")          # WANDB_API_KEY env; autopatches openai client calls

@weave.op()
def verify(segment_id: str, prompt_version: str, model: str) -> dict:
    ...                                           # Cosmos call + JSON parse
    call_id = weave.require_current_call().id     # stash in nw_verdicts.weave_call_id → link in Slack
    return {"verdict": "...", "severity": 4, "weave_call_id": call_id}

# or after the fact:
result, call = verify.call("seg-123", "v2", "8b"); call_id = call.id

# Slack 👍/👎 → Weave feedback
c = client.get_call(call_id)
c.feedback.add_reaction("👍")                     # or "👎"
c.feedback.add("label", {"correct": True, "user": "U123"})
c.feedback.add_note("operator: real removal")   # ≤1024 chars
client.get_feedback(reaction="👎", limit=50)     # pull the labels for eval

# Evaluation: 60 labeled clips, 8B vs 2B × prompt v1 vs v2
examples = [{"segment_id": "seg-001", "source": "s3://...", "expected": "escalate"}, ...]
@weave.op()
def verdict_correct(expected: str, output: dict) -> dict:
    return {"correct": output.get("verdict") == expected,
            "tp": expected == "escalate" and output.get("verdict") == "escalate",
            "fp": expected == "dismiss" and output.get("verdict") == "escalate",
            "json_ok": isinstance(output, dict) and "verdict" in output}
class Verifier(weave.Model):
    model: str
    prompt_version: str
    @weave.op()
    def predict(self, segment_id: str, source: str) -> dict: ...
ev = weave.Evaluation(dataset=examples, scorers=[verdict_correct], evaluation_name="nw-verifier")
for m in ["nvidia/cosmos-reason2-8b", "nvidia/cosmos-reason2-2b"]:
    asyncio.run(ev.evaluate(Verifier(model=m, prompt_version="v2"), __weave={"display_name": f"{m}-v2"}))
```
Precision and recall come from aggregating the `tp`/`fp` booleans (Weave shows true-fraction per bool). Add `trials=` for repeats. Use `EvaluationLogger` for imperative logging if the Model class gets in the way. Set `WEAVE_PARALLELISM=4` so 60 clips don't run into the Cosmos 429s (env var name UNVERIFIED).

---

## 6. YOLO11 tracking (VERIFIED, https://docs.ultralytics.com/modes/track/, models/yolo11)
```python
from ultralytics import YOLO
m = YOLO("yolo11n.pt")                       # current docs default to yolo26n; yolo11 still supported
for r in m.track(source="seg.mp4", stream=True, persist=True, tracker="bytetrack.yaml", conf=0.4, classes=[0, 24, 26, 28, 39]):
    if r.boxes is not None and r.boxes.is_track:
        ids = r.boxes.id.int().cpu().tolist(); xyxy = r.boxes.xyxy.cpu().tolist(); cls = r.boxes.cls.int().tolist()
# frame loop variant: m.track(frame, persist=True)  ← persist=True keeps IDs across calls (one model per stream)
```
- Trackers: `bytetrack.yaml`, `botsort.yaml`, `ocsort.yaml`, `tracktrack.yaml` (the new default).
- Speed at 640 px (official): **yolo11n 56 ms CPU-ONNX / 1.5 ms T4-TRT. yolo11s 90 ms CPU / 2.5 ms T4.** That is ~18 fps (n) / ~11 fps (s) on CPU. On an M-series Mac, `device="mps"` is typically faster (UNVERIFIED). For the live cam, a local `yolo11n` at 5 fps sampling is plenty to drive the "person in frame" chip.
- Blueprint YOLO has **no tracker**. "Person entered and left" and "object disappeared" are best computed locally on the laptop, or from the per-frame sidecar.

---

## 7. Slack: image and Block Kit (VERIFIED, https://docs.slack.dev/tools/python-slack-sdk/web/, image-block, socket-mode)
Incoming webhooks **cannot upload files**, and `image_url` must be **publicly reachable by Slack's servers**, which VAST S3 is not. Use a bot token with `chat:write` and `files:write`, invite the bot to the channel, then:
```python
import time, os
from slack_sdk import WebClient
sc = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
up = sc.files_upload_v2(channel=CH, file="keyframe_bbox.jpg", title="cam-05 14:02:31")   # simplest: shows image + comment
fid = up["file"]["id"]
for _ in range(10):                                   # v2 upload is async: poll until shared (issue #1521)
    if sc.files_info(file=fid)["file"].get("shares"): break
    time.sleep(0.5)
sc.chat_postMessage(channel=CH, text="Equipment removed from table (sev 4)", blocks=[
  {"type":"header","text":{"type":"plain_text","text":"🚨 cam-05 · Equipment removed"}},
  {"type":"image","slack_file":{"id":fid},"alt_text":"keyframe with Cosmos bbox"},
  {"type":"section","text":{"type":"mrkdwn","text":"*Cosmos:* person removes boxed equipment and exits\n<https://wandb.ai/...|Weave trace> · `seg-05-0231`"}},
  {"type":"actions","elements":[
     {"type":"button","text":{"type":"plain_text","text":"👍 Real"},"style":"primary","action_id":"fb_up","value":"seg-05-0231"},
     {"type":"button","text":{"type":"plain_text","text":"👎 Not an event"},"style":"danger","action_id":"fb_down","value":"seg-05-0231"}]}])
```
Buttons need an interactivity endpoint. **Socket Mode avoids a public URL.** Enable it, create an app-level token `xapp-…` with `connections:write`:
```python
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
app = App(token=os.environ["SLACK_BOT_TOKEN"])
@app.action("fb_up")
def up(ack, body): ack(); record_feedback(body["actions"][0]["value"], "up", body["user"]["id"])
@app.action("fb_down")
def down(ack, body): ack(); record_feedback(body["actions"][0]["value"], "down", body["user"]["id"])
SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()   # run on the laptop
```
The phone buzz needs the mobile app's notifications set to "All new messages" for the channel, or an `@here` in `text` (the `text` field is what drives the push).

---

## Top 10 build-day gotchas

1. **The blueprint runs Cosmos-Reason2 on *every* segment** (caption step), and the embedder **drops segments with no caption**. The visual vector cannot exist without a Reason2 call. Reword the pitch to: "the *expensive verify-with-reasoning* call runs on ~3%". The caption is the cheap, short, non-CoT pass. Or set a minimal `custom-prompt` on the archive cams to make captioning cheaper.
2. **Segments are 5 s, not 10 s.** A 10 s webcam chunk becomes 2 segments (2 Reason2 calls, 2 rows). Upload 5 s chunks for the live cam to halve latency, and set `segment_duration` and the chunk length to match.
3. **The SDK can't read vector columns.** The blueprint monkey-patches `vastdb._internal.build_query_data_request` to drop `list<float>` columns. Get vectors from the **embedder event (fan-out link)**, or from ADBC SQL. Do not use `table.select()`.
4. **`vectors_visual` is zero-filled when the visual embed fails.** Guard `norm == 0` and check `extra_metadata.visual_embedding_ok`, or the cosine NaN will poison the centroid.
5. **Schedule triggers use Quartz cron and the timezone is unconfirmed (UTC timestamps).** Use an every-minute trigger plus a wall-clock guard in America/Los_Angeles, plus an idempotent `nw_digests` row. Have a laptop-cron fallback ready by 15:00.
6. **Apple Silicon builds.** `vastde functions build` builds with Docker. If the image comes out arm64, DataEngine (linux/amd64) will fail to start it. Check `docker inspect --format '{{.Architecture}}'`. If needed, build on a Linux box or the venue builder (`vastde builders list/set`). UNVERIFIED whether `vastde` cross-builds.
7. **A trigger must exist before `pipelines create`.** The name in the YAML must match exactly, or the create fails. Resource names are tenant-shared, so prefix them with `$USER`/team (`nw-…`) to avoid collisions with other teams on the same tenant.
8. **Event Broker limits:** pre-create topics (no auto-create), confluent-kafka **2.4–2.8** only, values **≤126 KB**, no compression. Prefer function→function links with `set_trigger_labels` over a hand-rolled topic.
9. **Cosmos request pitfalls:** `fps` greater than the video's real fps, or `num_frames` greater than its frame count, returns **HTTP 400**. Send `fps` *or* `num_frames`, never both. CoT needs a big `max_tokens`, or the JSON gets truncated, so always regex-extract the last `{...}` and retry once. The hosted build.nvidia.com Reason2 may 404 ("Function not found for account"). Use the venue's NIM at `cosmos_host:8001`. The free tier is ~40 RPM and likely venue-shared.
10. **Slack:** `files_upload_v2` is async, so referencing `slack_file.id` immediately gives `invalid_blocks`. Poll `files.info` until `shares` appears, or post the image with `initial_comment` and the buttons as a threaded reply. Buttons need Socket Mode (`xapp-` token) or a public URL. Webhooks can't attach images.

Bonus:
- Every `vastde traces list` defaults to `--since 1m`. Pass `--since 30m` when demoing.
- `/v1/infer` YOLO on the GPU host is shared with every team. Run the live-cam person gate on the laptop (`yolo11n`).
- W&B Inference 429s are **per project**. Use separate projects for the eval run and the live demo.

---

## Source index (this session)
Primary repos (git-cloned, files captured):
- https://github.com/vast-data/vss-blueprint: `dr-tech-vss-blueprint-pipeline.md`, `dr-tech-vss-blueprint-functions.md`
- https://github.com/vast-data/dataengine-cli/tree/main/docs/references/commands: `dr-tech-dataengine-cli-reference.md`
- https://github.com/vast-data/dataengine-pipelines: `dr-tech-dataengine-pipelines-examples.md`
- https://github.com/vast-data/vastdb_sdk, https://github.com/vast-data/vastdb-adbc-driver, https://github.com/vast-data/vast-vector-store: `dr-tech-vastdb-vector-search.md`
- https://github.com/nvidia-cosmos/cosmos-reason2: `dr-tech-cosmos-reason2-repo.md`
- (`vast-data/vast-code-snippets` is an empty repository.)

Scraped docs (firecrawl):
- NIM Reason2 API 1.7.0: `dr-tech-nim-cosmos-reason2-api.md`
- HF Cosmos-Reason2-8B: `dr-tech-hf-cosmos-reason2-8b.md`
- HF Reason2 blog: `dr-tech-hf-blog-reason2.md`
- NVIDIA forum 404: `dr-tech-nvforum-function-not-found.md`
- NIM Cosmos-Embed1 API: `dr-tech-nim-cosmos-embed1-api.md`
- W&B/CoreWeave models: `dr-tech-wandb-inference-models.md`
- CoreWeave limits: `dr-tech-cw-inference-limits.md`
- CoreWeave API: `dr-tech-cw-inference-api.md`
- Weave feedback: `dr-tech-weave-feedback.md`
- Weave evaluations: `dr-tech-weave-evaluations.md`
- Ultralytics track: `dr-tech-ultralytics-track.md`
- Slack web SDK: `dr-tech-slack-python-sdk-web.md`
- Slack image block: `dr-tech-slack-image-block.md`
- Slack Socket Mode: `dr-tech-slack-bolt-socket-mode.md`
- slack-sdk issue #1521: `dr-tech-slack-issue-1521.md`
- KB Creating a Trigger: `dr-tech-kb-creating-a-trigger.md`
- KB Creating a Function: `dr-tech-kb-creating-a-function.md`
- KB Runtime SDK index: `dr-tech-kb-runtime-sdk.md`
- KB Event Handling 5.5: `dr-tech-kb-event-handling.md`
- KB Kafka protocol support: `dr-tech-kb-kafka-protocol.md`

Search result sets: `dr-tech-s1…s10-*.json` (10 searches).
