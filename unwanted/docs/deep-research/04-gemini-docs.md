# 04 — Gemini API Video Understanding: Primary-Source Reference (as of 2026-10-02)

Scope: everything needed to send short (≈5 s) video clips and webcam frames to Gemini, get structured verdicts and bounding boxes, and budget tokens, cost, and rate limits. All facts come from Google docs captured on 2026-10-02 into `docs/sources/dr-gem-docs-*.md`, unless marked **UNVERIFIED** (third-party or inferred). Each fact cites its URL.

> **The API changed shape in 2026, so read this first.**
> 1. **The Interactions API (`client.interactions.create`) is now the default.** It went GA in June 2026 and Google recommends it for new projects. `generateContent` is "legacy" but "remains fully supported" ([interactions overview](https://ai.google.dev/gemini-api/docs/interactions)). The docs default to Interactions, and a toggle shows the generateContent variant ([generate-content video page](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding)).
> 2. **Vertex AI has been renamed "Gemini Enterprise Agent Platform."** The rename began April 22, 2026 ([name changes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes)). The SDK flag is now `genai.Client(enterprise=True, project=..., location="global")` or `GOOGLE_GENAI_USE_ENTERPRISE=true` ([PyPI google-genai 2.26.0, released Sep 30 2026](https://pypi.org/project/google-genai/)).
> 3. **Current model IDs are Gemini 3.x.** Gemini 2.5 access is now limited to projects that already used it ([changelog, Sep 18 2026](https://ai.google.dev/gemini-api/docs/changelog)).

---

## 1. Models that accept video (Gemini Developer API)

Source: [models](https://ai.google.dev/gemini-api/docs/models) and the per-model pages.

| Model ID | Status | Video in? | Context in/out | Thinking levels (default) | Notes |
|---|---|---|---|---|---|
| `gemini-3.8-flash` | Stable, GA Sep 2 2026 | Yes | 1,048,576 / 65,536 | low, medium, high (medium). **`minimal` returns an error** | Live API: not supported. Batch, Flex, Priority: supported ([model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash), [thinking](https://ai.google.dev/gemini-api/docs/thinking)) |
| `gemini-3.7-flash` | Stable | Yes | 1M | low/med/high (medium) | Agentic video supported |
| `gemini-3.6-flash` | Stable | Yes | 1M | minimal–high (medium) | Agentic video supported |
| `gemini-3.5-flash` | Stable ("legacy Flash") | Yes | 1M | minimal–high (medium) | More expensive than 3.8 (see §8) |
| `gemini-3.5-flash-lite` | Stable | Yes | 1,048,576 / 65,536 | minimal–high (**minimal**) | Cheapest current model with agentic video ([model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite)) |
| `gemini-3.1-flash-lite` | Stable | Yes ([Vertex video table](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding)) | 1M | n/a in thinking table | Cheapest per input token |
| `gemini-3.1-pro-preview` | Preview | Yes | 1M | low/med/high (high) | **No free tier** ([pricing](https://ai.google.dev/gemini-api/docs/pricing)) |
| `gemini-3-flash-preview` | Preview ("legacy") | Yes | 1M | minimal–high (high) | |
| `gemini-3.8-live` | Stable, GA Sep 15 2026 | Yes (Live API frames) | 131,072 / 65,536 | `thinkingLevel` not supported (omit it) | Output: **audio only**. Structured outputs **not supported** ([model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live)) |
| `gemini-3.8-live-extended-thinking` | Stable | Yes (Live) | — | low/med/high | Async (NON_BLOCKING) function calls only ([Live capabilities](https://ai.google.dev/gemini-api/docs/live-guide)) |
| `gemini-robotics-er-2-streaming-preview` | Preview | Yes (Live) | 131,072 / 65,536 | supported | **Live API with TEXT output.** Function calling yes, structured output no ([model page](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview)) |
| `gemini-2.5-flash` / `-flash-lite` / `-pro` | Restricted to prior users | Yes | 1M | | "For any new projects, use … 3.5 Flash-Lite or 3.8 Flash" ([changelog](https://ai.google.dev/gemini-api/docs/changelog)) |

The **"latest" alias** `gemini-flash-latest` is hot-swapped on each release, with 2 weeks' notice before breaking changes ([models](https://ai.google.dev/gemini-api/docs/models)). Pin `gemini-3.8-flash` or `gemini-3.5-flash-lite` for a demo.

---

## 2. Input methods and size limits

| Method | Limit | Persistence | Source |
|---|---|---|---|
| Inline base64 (`"data"` on a video content item) | **< 100 MB per request** (50 MB for PDFs) | None | [file-input-methods](https://ai.google.dev/gemini-api/docs/file-input-methods) |
| Files API upload | 2 GB per file, 20 GB per project, **auto-deleted after 48 h**, free of charge; user uploads cannot be downloaded | 48 h | [files](https://ai.google.dev/gemini-api/docs/files) |
| GCS URI registration (`files:register`) | 2 GB per file, no storage cap; one registration grants up to 30 days of access | Fetched per request | [file-input-methods](https://ai.google.dev/gemini-api/docs/file-input-methods) |
| External HTTPS / signed URL | 100 MB per payload; must be public or pre-signed; goes through a moderation check (`URL_RETRIEVAL_STATUS_UNSAFE`) | None | [file-input-methods](https://ai.google.dev/gemini-api/docs/file-input-methods) |
| YouTube URL | Public videos only. Free tier: max 8 h of YouTube per day. Max 10 videos per request on 2.5+ | — | [video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding) |

**Inconsistencies in the docs (flagged):**
- The video page's table says inline is "< 100MB". The same page's prose says inline suits videos "under 20MB total request size" and to "always use the Files API when the total request size … is larger than 20 MB". The legacy generateContent sample says "Only for videos of size <20Mb" ([video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding), [gc-video](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding)). **Treat 20 MB as the safe inline ceiling.** A 5 s 720p H.264 clip is typically 1–5 MB, so this doesn't matter for us.
- The video page says the Files API max is "20GB (paid) / 2GB (free)". The Files page says "per-file maximum size of 2 GB" and "20 GB of files per project". **UNVERIFIED** which is current for paid accounts. Irrelevant for 5 s clips.

**Supported video MIME types:** `video/mp4`, `video/mpeg`, `video/mov`, `video/avi`, `video/x-flv`, `video/mpg`, `video/webm`, `video/wmv`, `video/3gpp`. The Interactions API enum lists exactly these ([video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding), [Interactions API ref](https://ai.google.dev/api/interactions-api)). The generateContent page lists `video/quicktime` instead of `video/mov`.

**Max video length:** models with a 1M context window handle "up to 3 hours long by default (at low media resolution), or up to 1 hour long at high media resolution" ([video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding)). On Vertex/Agent Platform the limits are about 45 min with audio, about 1 h without audio, and 10 videos per prompt ([Vertex video](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding)).

**Images:** max 3,600 image files per request. Accepted formats: PNG, JPEG, WEBP, HEIC, HEIF ([image-understanding](https://ai.google.dev/gemini-api/docs/image-understanding)).

---

## 3. Processing parameters (exact names)

### 3.1 Interactions API (`VideoContent`)
From the [Interactions API reference](https://ai.google.dev/api/interactions-api) and [video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding):

```text
{ "type": "video",
  "data": "<base64>"  |  "uri": "<files URI | https URL | YouTube URL>",
  "mime_type": "video/mp4",
  "processing": "static" | "agentic" | {           # StaticMediaProcessing object
        "type": "static",                         # required, always "static"
        "fps": <number>,                          # sampling density
        "start_offset": "10.5s",                  # string, seconds + "s"
        "end_offset": "30s" },                    # must be > start_offset
  "resolution": "low" | "medium" | "high" | "ultra_high",
  "name": "<optional label the model can reference>" }
```

- **Default processing is static at 1 FPS.** Audio is processed at 1 Kbps mono, with timestamps added every second ([video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding)).
- **Clipping and custom fps work only in `"static"` mode** ([video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding)).
- **fps range is (0.0, 24.0], default 1.0.** This comes from the legacy `VideoMetadata` schema ([generateContent API ref](https://ai.google.dev/api/generate-content)). **UNVERIFIED** that the same cap applies to Interactions `processing.fps`, but it is most likely identical.
- **Offset types are inconsistent in the docs.** The guide's samples use integers (`"start_offset": 1200`). The reference says a string such as `"10.5s"`. **Use strings with an `s` suffix.**
- **Agentic mode** is supported on 3.8 Flash, 3.7 Flash, 3.6 Flash, and 3.5 Flash-Lite. The model navigates the video and fetches transcript, frames, or audio on demand. Google claims "up to 88% fewer tokens" on long-form video, but "navigation may slightly increase Time to First Token (TTFT) on short clips (<5 minutes)". Google recommends **static for latency-sensitive clips under 5 minutes** ([video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding)). Agentic responses add `processing_call` and `processing_result` steps.
- One external test found static mode used 26% fewer tokens than agentic on 10-minute synthetic videos, and one of six agentic outputs failed its JSON format ([MLQ summary of the PaperEdits forum benchmark](https://mlq.ai/news/google-expands-geminis-agentic-video-analysis-but-early-testing-finds-trade-offs/), third-party). **For 5 s clips use static.**
- **Prompt placement:** for text plus a single video, put the text **after** the video ([video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding)). The image page says put text **before** a single image ([image-understanding](https://ai.google.dev/gemini-api/docs/image-understanding)). The Files prompting guide says put the image or video first. These conflict, so follow the video page for video.
- **Timestamps:** prompt with `MM:SS`. On Vertex, use `MM:SS` at 1 FPS or below and `MM:SS.sss` above 1 FPS (`H:MM:SS(.sss)` past an hour) ([video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding), [Vertex video](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding)).
- **Long requests:** use `stream=True` or `background=True` to avoid 401 errors or timeouts during backend retries ([video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding)).

### 3.2 generateContent (legacy) equivalents
- The `Part` has `inline_data` / `file_data`, plus `video_metadata=VideoMetadata(start_offset="1250s", end_offset="1570s", fps=5)`, `media_resolution`, and `media_processing="AGENTIC"|"STATIC"` ([gc-video](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding), [API ref](https://ai.google.dev/api/generate-content)).
- **`VideoMetadata` is marked "Deprecated: Use `GenerateContentRequest.processing_options` instead"** ([API ref](https://ai.google.dev/api/generate-content)). `processing_options` has no documented schema. **UNVERIFIED.** The guide samples still use `video_metadata`.
- `MediaResolution` enum: `MEDIA_RESOLUTION_{UNSPECIFIED,LOW,MEDIUM,HIGH,ULTRA_HIGH}` ([API ref](https://ai.google.dev/api/generate-content)).
- On Vertex, `media_processing` agentic mode "is set to `STATIC` or disabled by default". Vertex's agentic list names 3.8 Flash **Cyber**, 3.7, 3.6, and 3.5 Flash-Lite ([Vertex video](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding)).

---

## 4. Tokens per second of video (static mode)

**Authoritative for Gemini 3 models** ([media-resolution](https://ai.google.dev/gemini-api/docs/media-resolution), confirmed by [Vertex video](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding)):

| `resolution` / `media_resolution` | Tokens per video frame | Audio | Image (for keyframes) |
|---|---|---|---|
| `unspecified` (default) | **70** | 25 tok/s | 1120 |
| `low` | 70 | 25 tok/s | 280 |
| `medium` | 70 (low and medium are "treated identically") | 25 tok/s | 560 |
| `high` | **280** | 25 tok/s | 1120 |
| `ultra_high` | N/A for video | N/A | 2240 (per-item only) |

**Per-second formula for Gemini 3, static mode:** `fps × 70` (or `× 280` at high) `+ 25` audio, plus small timestamp/metadata overhead.
- 1 fps, default: **≈95 tok/s**
- 1 fps, high: **≈305 tok/s**
- 5 fps, default: **≈375 tok/s**

Google recommends `high` for video only when you need OCR or small details ([media-resolution](https://ai.google.dev/gemini-api/docs/media-resolution)).

**Conflicting legacy numbers still appear in the docs (flagged):**
- The video page says 66 tokens/frame at low and 258 otherwise, with 32 tok/s audio, giving "≈100 tok/s default (low), ≈300 tok/s high" ([video-understanding](https://ai.google.dev/gemini-api/docs/video-understanding)). Vertex says these are **pre-Gemini 3** figures.
- The tokens page says "Video: 263 tokens per second" and "Audio: 32 tokens per second" in one place, then "~100 tokens/second by default" in another ([tokens](https://ai.google.dev/gemini-api/docs/tokens)).
- **Measure it.** Call `client.models.count_tokens(model=..., contents=[...])` before sending, or read `interaction.usage` (`total_input_tokens`, `total_output_tokens`, `total_thought_tokens`, `total_cached_tokens`, `total_tool_use_tokens`) ([tokens](https://ai.google.dev/gemini-api/docs/tokens)).

### Token budget for one 5 s clip (estimate)

| Config | Video+audio input | + ~250-token prompt and schema | Output (JSON ~150 + thinking) |
|---|---|---|---|
| 1 fps, default res | 5×70 + 5×25 ≈ **475** | ≈ 725 | 150 + thinking |
| 5 fps, default res | 25×70 + 125 ≈ **1,875** | ≈ 2,125 | 150 + thinking |
| 1 fps, high res | 5×280 + 125 ≈ **1,525** | ≈ 1,775 | 150 + thinking |
| Legacy formula (100 tok/s) | ≈ 500 | ≈ 750 | |

Thinking tokens are billed as output ([thinking](https://ai.google.dev/gemini-api/docs/thinking)). 3.8 Flash cannot go below `low`. 3.5 Flash-Lite defaults to `minimal`. The number of thinking tokens for a short verdict is **UNVERIFIED**. Assume roughly 0–200 at `minimal` and roughly 200–1,000 at `low`, and measure with `total_thought_tokens`.

---

## 5. Structured output (JSON schema)

Source: [structured-output](https://ai.google.dev/gemini-api/docs/structured-output).
- **Interactions:** `response_format={"type": "text", "mime_type": "application/json", "schema": <JSON Schema>}`. Pydantic's `Model.model_json_schema()` and Zod are supported. Read the result with `Model.model_validate_json(interaction.output_text)`.
- **generateContent:** `config={"response_mime_type": "application/json", "response_json_schema": ...}` (or `responseSchema`), per the `GenerationConfig` fields `responseMimeType`, `responseSchema`, and `responseJsonSchema` ([API ref](https://ai.google.dev/api/generate-content)).
- **Supported JSON Schema subset:**
  - Types: `string`, `number`, `integer`, `boolean`, `object`, `array`, `null` (as a type array).
  - Annotations: `title`, `description`.
  - Objects: `properties`, `required`, `additionalProperties`.
  - Strings: `enum`, `format` (date-time, date, time).
  - Numbers: `enum`, `minimum`, `maximum`.
  - Arrays: `items`, `prefixItems`, `minItems`, `maxItems`.
- Very large or deeply nested schemas may be rejected. The output is syntactically valid JSON, but you should still validate its semantics.
- Structured output is **not supported** on `gemini-3.8-live` or `gemini-robotics-er-2-streaming-preview`. Use function calling for typed results there ([3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live), [robotics streaming](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview)).

## 6. Object detection and segmentation

Source: [image-understanding](https://ai.google.dev/gemini-api/docs/image-understanding).
- **Bounding box format:** `box_2d = [ymin, xmin, ymax, xmax]`, normalized to **0–1000**. To get pixels: `y_px = v/1000*H` and `x_px = v/1000*W`.
- **Segmentation:** each item has `box_2d`, `label`, and `mask`. The mask is now **a polygon of `[x, y]` points normalized 0–1000**. Note the **x,y order, which is the reverse of box_2d's y,x**. Older docs described base64 PNG masks, which are no longer documented.
- **Doc bug:** the segmentation sample uses `gemini-3.8-flash` with `thinking_level: "minimal"`, but the 3.8 Flash model page says `minimal` "returns an error". Use `low` on 3.8 Flash, or use 3.5 Flash-Lite for `minimal`.
- **Image token cost:** for Gemini 3 the cost is set by `resolution` (280/560/1120/2240) ([media-resolution](https://ai.google.dev/gemini-api/docs/media-resolution)). The 258-tokens-per-768×768-tile formula on the image page is legacy.

## 7. Thinking control

Source: [thinking](https://ai.google.dev/gemini-api/docs/thinking), [openai](https://ai.google.dev/gemini-api/docs/openai).
- **Interactions:** `generation_config={"thinking_level": "minimal|low|medium|high", "thinking_summaries": "auto|none"}`.
- **`thinking_budget` (numeric)** applies only to 2.5 models. In the OpenAI compat mapping it is 1,024 / 8,192 / 24,576. "Reasoning cannot be turned off for Gemini 2.5 Pro or 3 models."
- `max_output_tokens` is a hard cap that **includes** thought tokens. If you hit it, status becomes `incomplete` and you are still billed for the thinking. Lower `thinking_level` instead of setting a small cap.

## 8. Pricing (Gemini Developer API, paid tier, USD per 1M tokens)

Source: [pricing](https://ai.google.dev/gemini-api/docs/pricing), updated 2026-10-01. Tabs: Standard / Batch / Flex / Priority.

| Model | Standard in | Standard out (incl. thinking) | Batch & Flex in/out | Priority in/out | Free tier |
|---|---|---|---|---|---|
| `gemini-3.8-flash` (also 3.7, 3.6) | **$0.75** until Dec 31 2026, then $1.50 | **$3.75**, then $7.50 | $0.375 / $1.875 | $1.35 / $6.75 | Free |
| `gemini-3.5-flash` | $1.50 | $9.00 | $0.75 / $4.50 | $2.70 / $16.20 | Free |
| `gemini-3.5-flash-lite` | **$0.30** (text/image/video/audio) | **$2.50** | $0.15 / $1.25 | $0.54 / $4.50 | Free |
| `gemini-3.1-flash-lite` | **$0.25** (text/image/video), $0.50 audio | $1.50 | $0.125 / $0.75 | $0.45 / $2.70 | Free |
| `gemini-3-flash-preview` | $0.50 (video), $1.00 audio | $3.00 | $0.25 / $1.50 | $0.90 / $5.40 | Free |
| `gemini-3.1-pro-preview` | $2.00 (≤200k) | $12.00 | $1.00 / $6.00 | $3.60 / $21.60 | **Not available** |
| `gemini-2.5-flash` (restricted) | $0.30 video, $1.00 audio | $2.50 | $0.15 / $1.25 | | Free |
| `gemini-2.5-flash-lite` (restricted) | $0.10 video, $0.30 audio | $0.40 | $0.05 / $0.20 | | Free |
| `gemini-3.8-live` | $1.00 image/video (**or $0.002/min**), $3.00 audio ($0.005/min), $0.75 text | $12 audio ($0.018/min), $4.50 text | n/a | n/a | Free |
| `gemini-robotics-er-2-streaming-preview` | $1.00 until Dec 31 2026 | $5.00 | n/a | n/a | Free |

- **3.x Flash models charge audio at the same rate as video.** 3.1 Flash-Lite and 3 Flash preview charge audio separately, at double the video rate.
- Context-cache reads cost 10% of input, e.g. $0.075 for 3.8 Flash. Storage costs $0.50–$1.00 per 1M tokens per hour.
- **Vertex/Agent Platform** list prices match on the `global` endpoint. Non-global regions cost about 10% more, e.g. 3.8 Flash at $0.825 in ([Vertex pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)).
- **Live per-minute cross-check (flagged):** at 70 tok/frame and 1 FPS, a minute of video is 4,200 tokens, or $0.0042 at $1/1M, which is double the stated "$0.002/min". Live may tokenize frames more cheaply. **UNVERIFIED** — measure with `usage_metadata`.

### Cost per 5 s clip (derived from the tables above; thinking tokens are an assumption)

| Model | Input (≈725 tok at 1 fps) | Output (150 JSON + thinking) | **Total per clip** | Per 1,000 clips |
|---|---|---|---|---|
| 3.5 Flash-Lite, `minimal` (≈+50 thought) | $0.00022 | 200 × $2.50/M = $0.00050 | **≈ $0.0007** | ≈ $0.72 |
| 3.1 Flash-Lite | $0.00018 | 150 × $1.50/M = $0.00023 | **≈ $0.0004** | ≈ $0.41 |
| 3.8 Flash, `low` (≈+400 thought) | $0.00054 | 550 × $3.75/M = $0.00206 | **≈ $0.0026** | ≈ $2.60 |
| 3.8 Flash at 5 fps (≈2,125 in) | $0.0016 | $0.0021 | **≈ $0.0037** | ≈ $3.70 |
| 3.8 Flash via Batch/Flex | half of the above | | ≈ $0.0013 | ≈ $1.30 |
| On the free tier | $0 (but data is used for training, see §10) | | **$0** | rate-limited |

Output tokens, especially thinking, dominate the cost. Keep the schema small and the thinking level low.

---

## 9. Rate limits and tiers

Source: [rate-limits](https://ai.google.dev/gemini-api/docs/rate-limits).
- Limits are tracked as **RPM, input TPM, and RPD**, **per project, not per API key**. RPD resets at **midnight Pacific**. Preview and experimental models get tighter limits.
- **Google no longer publishes per-model numbers.** "Rate limits depend on a variety of factors … and can be viewed in Google AI Studio" at `https://aistudio.google.com/rate-limit`. Check the live values for your project before the demo.
- **Tiers:**

  | Tier | Qualification | Billing cap |
  |---|---|---|
  | Free | Active project | — |
  | Tier 1 | Linked billing account (upgrade is instant) | $250 |
  | Tier 2 | $100 paid + 3 days | $2,000 |
  | Tier 3 | $1,000 paid + 30 days | $20k–$100k+ |

- **Spend-based limits per rolling 10 minutes:** Tier 1 $10, Tier 2 $50, Tier 3 $200. Exceeding one returns `429 RESOURCE_EXHAUSTED`.
- **Priority tier** gets 0.3× the standard rate limits by default.
- **Batch API:**
  - 100 concurrent batch jobs.
  - 2 GB input file limit, 20 GB file storage.
  - Enqueued-token caps for 3.8 Flash: 3M (Tier 1), 400M (Tier 2), 1B (Tier 3). For 3.5 Flash-Lite: 10M / 500M / 1B.
  - Cost is 50% of standard, with a 24 h target turnaround. Inline batches must be under 20 MB; larger ones use JSONL files ([batch-api](https://ai.google.dev/gemini-api/docs/batch-api)).
- **Flex:** 50% off. **Synchronous**, but with a 1–15 min latency target, best-effort delivery, and possible 503/429. Set client timeouts of 10 min or more ([flex-inference](https://ai.google.dev/gemini-api/docs/flex-inference)). Not suitable for a live demo.
- **UNVERIFIED third-party free-tier figures:** about 10 RPM / 250k TPM / 1,500 RPD for 3 Flash and about 15 RPM / 1,000 RPD for 3.1 Flash-Lite ([pecollective, Sep 2026](https://pecollective.com/tools/gemini-free-tier-guide/)). Other reports put some projects at 20 RPD ([laozhang](https://blog.laozhang.ai/en/posts/gemini-api-free-tier)). These numbers are unreliable, so check AI Studio.
- **UNVERIFIED (forum):** Live API Tier 1 allows about 50 concurrent sessions ([discuss.ai.google.dev](https://discuss.ai.google.dev/t/gemini-live-api-tier-2-project-still-limited-to-50-concurrent-connections-and-billed-as-tier-1/94634)).
- **Implicit caching** is on by default for 2.5+ models. The minimum prefix is **4,096 tokens** on 3.x Flash and 3.1 Pro, and 2,048 on 2.5. Check `usage.total_cached_tokens` ([caching](https://ai.google.dev/gemini-api/docs/caching)). A 5 s clip (about 500 tokens) won't trigger the cache unless a shared system prompt or few-shot prefix is at least 4,096 tokens.
- **Explicit caching** is `client.caches.create(model, config=CreateCachedContentConfig(contents=..., system_instruction=..., ttl="300s"))`, then pass `cached_content=cache.name` in a generateContent config ([caching API ref](https://ai.google.dev/api/caching)). Whether explicit caches attach to Interactions calls is **UNVERIFIED**.

## 10. Free-tier data use — read before uploading anyone's face

Source: [Gemini API Additional Terms, effective March 23 2026](https://ai.google.dev/gemini-api/terms); [pricing "Used to improve our products"](https://ai.google.dev/gemini-api/docs/pricing).
- **Unpaid services (free quota and AI Studio):** Google "uses the content you submit … and any generated responses to provide, improve, and develop Google products … and machine learning technologies". "**Human reviewers may read, annotate, and process your API input and output.**" "**Do not submit sensitive, confidential, or personal information to the Unpaid Services.**" The license covers "files such as images, videos". The pricing table shows "Used to improve our products: **Yes**" for every free tier.
- **Paid services** (any project with active Cloud Billing): Google "doesn't use your prompts (including … files such as images, videos …) or responses to improve our products". Prompts are processed under the Data Processing Addendum. They are logged "for a limited period of time" only for abuse detection and legal requirements. The pricing table shows "**No**".
- **EEA, Switzerland, and UK users get paid-tier data terms even on free quota.** You "may use only Paid Services when making API Clients available to users" in the EEA, Switzerland, or UK.
- **Storage by the Interactions API:** `store` defaults to `true`. Interactions are retained **55 days on paid** (configurable to 7/14/28/55 days in AI Studio) and **1 day on free**. Pass `store=False` to opt out. That disables `previous_interaction_id` and `background=True` ([interactions overview](https://ai.google.dev/gemini-api/docs/interactions)).
- Files API uploads auto-delete after 48 h. You can delete them sooner with `client.files.delete(name=...)` ([files](https://ai.google.dev/gemini-api/docs/files)).
- **Implication for a CCTV or real-people demo:** enable billing (Tier 1 is instant), even if spend stays near zero, and send `store=False`.

## 11. Live API (real-time webcam streaming)

Sources: [Live overview](https://ai.google.dev/gemini-api/docs/live), [capabilities](https://ai.google.dev/gemini-api/docs/live-guide), [session management](https://ai.google.dev/gemini-api/docs/live-session), [SDK quickstart](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk), [ephemeral tokens](https://ai.google.dev/gemini-api/docs/ephemeral-tokens), [Vertex streams](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api/send-audio-video-streams).
- **Transport:** a stateful WebSocket (WSS). In Python: `client.aio.live.connect(model=..., config=...)`.
- **Input formats:**
  - Audio: 16-bit PCM, 16 kHz, little-endian, as `audio/pcm;rate=16000`.
  - **Video:** individual JPEG or PNG frames, **max 1 frame per second**. Vertex recommends 768×768 at 1 FPS.
  - Text.
- **Output:** audio only (24 kHz PCM) on native-audio models. For text, set `output_audio_transcription: {}`. The Robotics ER 2 streaming model supports `response_modalities=["TEXT"]` ([robotics-streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming)).
- **Sending a frame:** `await session.send_realtime_input(video=types.Blob(data=jpeg_bytes, mime_type="image/jpeg"))`.
- **Frames alone don't trigger a model turn.** You need a text or audio prompt with them (stated for robotics streaming). On 3.8 Live, turn coverage defaults to `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO`: "only send frames when needed to manage context and cost" ([3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live)).
- **Session limits:**
  - Without compression, **audio+video sessions last 2 minutes** and audio-only sessions 15 minutes.
  - A single connection lives about **10 minutes**, and a `GoAway` message with `time_left` arrives before it closes.
  - Fixes: `context_window_compression=ContextWindowCompressionConfig(sliding_window=SlidingWindow())` for unlimited length, and `session_resumption=SessionResumptionConfig(handle=...)`. Resumption handles are valid for 2 h.
- **Context window:** 128k tokens on native-audio models, 32k on other Live models.
- **Media resolution:** set `media_resolution` in the session config.
- **Function calling on 3.8 Live:** async (`NON_BLOCKING`) is the default, with scheduling options `SILENT`, `WHEN_IDLE`, and `INTERRUPTED`.
- **Proactive audio** is always on in 3.8 Live; setting it to false returns an error. **Affective dialog has been removed.**
- **Browser clients:** use ephemeral tokens. Defaults are 1 min to start a session and 30 min of use, with `uses: 1`.
- **Partner integrations:** LiveKit, Pipecat, Fishjam, Stream Vision Agents, Voximplant, Agora, and Firebase AI Logic.

## 12. OpenAI-compatibility endpoint

`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"` ([openai](https://ai.google.dev/gemini-api/docs/openai)).
- Documented inputs are images (`image_url` with a data: URL) and audio (`input_audio`). There is **no video input section**.
- Google's own compatibility Colab says: "For videos support, use the Gemini API's Python SDK" ([cookbook](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb)).
- **Conclusion: video through OpenAI compat is not supported.** The workaround is to send extracted JPEG frames as multiple `image_url` parts (**UNVERIFIED** quality). `/v1/videos` exists, but it is Veo **generation**, not understanding.
- `reasoning_effort` maps to `thinking_level`. Gemini-specific fields go through `extra_body={"extra_body": {"google": {...}}}`, e.g. `cached_content` and `thinking_config`. The library is still in beta.

## 13. Regions

The Gemini Developer API is available in about 235 countries and territories, including the US, UK, EU member states, Canada, India, and Switzerland ([available-regions](https://ai.google.dev/gemini-api/docs/available-regions)). Outside those, use Agent Platform (Vertex). On Vertex the `global` endpoint is cheapest, and regional endpoints cost about 10% more ([Vertex pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)). Users must be 18 or older.

---

## 14. Python (`google-genai` ≥ 2.x, tested docs version 2.26.0) snippets

Setup: `pip install -U google-genai pydantic opencv-python`, then `export GEMINI_API_KEY=...`. `genai.Client()` reads the key from the environment. For Vertex/Agent Platform use `genai.Client(enterprise=True, project="P", location="global")`.

> The docs read results with `interaction.output_text` and `interaction.usage`. The PyPI README uses `interaction.outputs[-1].text`. **UNVERIFIED** which one your installed version exposes. Try `output_text` first.

### (a) Inline 5-second MP4 bytes with custom fps — the fastest path

```python
import base64
from google import genai

client = genai.Client()
clip_b64 = base64.b64encode(open("clip_5s.mp4", "rb").read()).decode()   # keep < 20 MB

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",            # or "gemini-3.8-flash" (then thinking_level="low")
    input=[
        {
            "type": "video",
            "data": clip_b64,
            "mime_type": "video/mp4",
            "processing": {"type": "static", "fps": 5},   # static only; fps range (0, 24]
            "resolution": "low",                          # 70 tok/frame on Gemini 3 ("high" = 280)
        },
        {"type": "text", "text": "Describe exactly what happens. Cite moments as MM:SS.sss."},
    ],
    generation_config={"thinking_level": "minimal", "max_output_tokens": 1024},
    store=False,                                          # no 55-day / 1-day server retention
)
print(interaction.output_text)
print(interaction.usage)   # total_input_tokens, total_output_tokens, total_thought_tokens ...
```

Legacy generateContent equivalent ([gc-video](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding)):

```python
from google.genai import types
resp = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=types.Content(parts=[
        types.Part(inline_data=types.Blob(data=open("clip_5s.mp4", "rb").read(), mime_type="video/mp4"),
                   video_metadata=types.VideoMetadata(fps=5)),      # deprecated-but-documented
        types.Part(text="Describe exactly what happens."),
    ]),
)
print(resp.text, resp.usage_metadata)
```

### (b) Files API upload and poll until ACTIVE

```python
import time
from google import genai

client = genai.Client()
f = client.files.upload(file="clip.mp4")
while not f.state or f.state.name != "ACTIVE":          # PROCESSING -> ACTIVE | FAILED
    if f.state and f.state.name == "FAILED":
        raise RuntimeError(f"File processing failed: {f.name}")
    time.sleep(1)                                     # docs use 5 s; 1 s is fine for short clips
    f = client.files.get(name=f.name)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "video", "uri": f.uri, "mime_type": f.mime_type,
         "processing": {"type": "static", "start_offset": "0s", "end_offset": "5s"}},
        {"type": "text", "text": "Summarize this clip."},
    ],
    generation_config={"thinking_level": "low"},
    store=False,
)
print(interaction.output_text)
client.files.delete(name=f.name)                      # otherwise auto-deleted after 48 h
```

### (c) Structured JSON verdict

```python
import base64
from typing import List, Literal
from pydantic import BaseModel, Field
from google import genai

class Event(BaseModel):
    t: str = Field(description="Timestamp MM:SS.sss within the clip")
    what: str = Field(description="One-sentence description of the observed action")

class Verdict(BaseModel):
    verdict: Literal["normal", "suspicious", "incident"]
    confidence: float = Field(ge=0.0, le=1.0, description="0-1 confidence")
    reason: str = Field(description="<= 25 words, grounded in visible evidence only")
    events: List[Event] = Field(max_length=5)

client = genai.Client()
clip_b64 = base64.b64encode(open("clip_5s.mp4", "rb").read()).decode()
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "video", "data": clip_b64, "mime_type": "video/mp4",
         "processing": {"type": "static", "fps": 2}},
        {"type": "text", "text": "Classify this security-camera clip. Only use visible evidence."},
    ],
    response_format={"type": "text", "mime_type": "application/json",
                     "schema": Verdict.model_json_schema()},
    generation_config={"thinking_level": "low"},
    store=False,
)
v = Verdict.model_validate_json(interaction.output_text)   # still validate semantics
print(v)
```

Keep the schema flat. Pydantic `Literal` becomes `enum`, and `ge`/`le` become `minimum`/`maximum`. All are inside the supported subset ([structured-output](https://ai.google.dev/gemini-api/docs/structured-output)).

### (d) Bounding boxes on a keyframe

```python
import base64, cv2
from typing import List
from pydantic import BaseModel, Field
from google import genai

cap = cv2.VideoCapture("clip_5s.mp4")
cap.set(cv2.CAP_PROP_POS_MSEC, 2500)                     # keyframe at 2.5 s
ok, frame = cap.read(); cap.release()
H, W = frame.shape[:2]
jpg = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 90])[1].tobytes()

class Box(BaseModel):
    box_2d: List[int] = Field(description="[ymin, xmin, ymax, xmax] normalized to 0-1000")
    label: str

class Boxes(BaseModel):
    boxes: List[Box]

client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Detect every person and any bag. "
                                  "box_2d is [ymin, xmin, ymax, xmax] normalized to 0-1000."},
        {"type": "image", "data": base64.b64encode(jpg).decode(), "mime_type": "image/jpeg",
         "resolution": "high"},                         # 1120 tokens on Gemini 3
    ],
    response_format={"type": "text", "mime_type": "application/json",
                     "schema": Boxes.model_json_schema()},
    generation_config={"thinking_level": "low"},        # NOT "minimal" on 3.8 Flash (errors)
    store=False,
)
for b in Boxes.model_validate_json(interaction.output_text).boxes:
    y0, x0, y1, x1 = b.box_2d
    px = (int(x0 / 1000 * W), int(y0 / 1000 * H), int(x1 / 1000 * W), int(y1 / 1000 * H))
    cv2.rectangle(frame, px[:2], px[2:], (0, 255, 0), 2)
    cv2.putText(frame, b.label, (px[0], max(px[1] - 4, 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
cv2.imwrite("keyframe_boxes.jpg", frame)
```

For segmentation, add `mask: List[List[int]]`, a polygon of **[x, y]** points normalized 0–1000 ([image-understanding](https://ai.google.dev/gemini-api/docs/image-understanding)).

### (e) Live API — webcam frames at 1 FPS with a typed callback

```python
import asyncio, cv2
from google import genai
from google.genai import types

client = genai.Client()
MODEL = "gemini-3.8-live"   # audio-out; use "gemini-robotics-er-2-streaming-preview" for TEXT out

report_event = types.FunctionDeclaration(
    name="report_event",
    description="Call whenever the scene shows a noteworthy event.",
    parameters={"type": "object",
                "properties": {"verdict": {"type": "string", "enum": ["normal", "suspicious", "incident"]},
                               "reason": {"type": "string"}},
                "required": ["verdict", "reason"]},
)

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],                       # native-audio models: AUDIO only
    output_audio_transcription=types.AudioTranscriptionConfig(),   # text transcript of speech
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_LOW,
    context_window_compression=types.ContextWindowCompressionConfig(
        sliding_window=types.SlidingWindow()),           # lifts the 2-min audio+video cap
    system_instruction="You watch a security camera. Call report_event for anything notable.",
    tools=[types.Tool(function_declarations=[report_event])],
)

async def send_frames(session):
    cap = cv2.VideoCapture(0)
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            frame = cv2.resize(frame, (768, 768))        # Vertex-recommended size
            jpg = cv2.imencode(".jpg", frame)[1].tobytes()
            await session.send_realtime_input(video=types.Blob(data=jpg, mime_type="image/jpeg"))
            await asyncio.sleep(1.0)                     # max 1 FPS
    finally:
        cap.release()

async def prompt_loop(session):
    while True:                                          # frames alone may not trigger a turn
        await asyncio.sleep(5)
        await session.send_realtime_input(text="Anything notable in the last 5 seconds?")

async def receive(session):
    async for msg in session.receive():
        if msg.tool_call:
            for fc in msg.tool_call.function_calls:
                print("EVENT:", fc.args)
            await session.send_tool_response(function_responses=[
                types.FunctionResponse(id=fc.id, name=fc.name, response={"ok": True})
                for fc in msg.tool_call.function_calls])
        sc = msg.server_content
        if sc and sc.output_transcription:
            print("Gemini:", sc.output_transcription.text)
        if msg.go_away is not None:
            print("Connection closing in", msg.go_away.time_left)   # reconnect with session_resumption

async def main():
    async with client.aio.live.connect(model=MODEL, config=config) as session:
        await asyncio.gather(send_frames(session), prompt_loop(session), receive(session))

asyncio.run(main())
```

The calls (`send_realtime_input(video=Blob)`, `output_audio_transcription`, `context_window_compression`, `tool_call` / `send_tool_response`, `go_away`) are all taken from the Live docs listed in §11. The tool-response loop is adapted from [get-started-sdk](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk). Whether a 5 s text nudge is the best way to trigger turns on `gemini-3.8-live` (the docs only spell it out for the robotics model) is **UNVERIFIED**. Test it.

---

## 15. UNVERIFIED and open items

1. Exact free-tier and Tier 1 RPM/RPD for `gemini-3.8-flash` and `gemini-3.5-flash-lite`. Google publishes these only in AI Studio.
2. Exact tokens per second: the Gemini 3 table (70/frame + 25/s audio) conflicts with legacy text (66/258 + 32, "263 tok/s", "~100 tok/s"). Confirm with `count_tokens`.
3. Live API video tokenization: the "$0.002/min" figure implies fewer tokens than 70 per frame.
4. `processing_options` (the replacement for deprecated `VideoMetadata`) has no documented schema.
5. Whether the fps cap of 24 applies to Interactions `processing.fps`, and whether offsets must be strings.
6. Files API max size for paid accounts: 2 GB vs 20 GB.
7. Whether explicit `cachedContents` attach to Interactions calls.
8. Live concurrency (forum report: about 50 sessions on Tier 1).
9. The SDK accessor: `interaction.output_text` vs `interaction.outputs[-1].text`.
10. Whether agentic mode is available for 3.8 Flash on Vertex. Vertex lists only 3.8 Flash Cyber, while the AI Studio docs list 3.8 Flash.

## Sources captured (docs/sources/dr-gem-docs-*.md)

The 43 page captures are: video, gc-video, models, pricing, media-res, tokens, files, file-input, structured, image, thinking, caching, batch, rate-limits, flex, live, live-guide, live-session, live-sdk, ephemeral, m-38flash, m-35flashlite, m-38live, robotics-stream, robotics-streaming, terms, openai, interactions, migrate, api-generate, api-caching, api-interactions, regions, changelog, vertex-video, vertex-names, vertex-live-av, vertex-pricing, pypi-genai, mlq-agentic, aa-38flash, pecollective, laozhang.

The 11 searches are saved as `dr-gem-docs-search-*.json`: vertex-video, enterprise-platform, free-rl, free-rl2, openai-video, live-video, latency, launch38, live-concurrent, files-processing, interactions-static-fps.
