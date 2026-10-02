# 06 — Drop-in Gemini fallback verifier for `nw-verifier`

Researched 2026-10-02. Code: [`src/verifier_backends.py`](../../src/verifier_backends.py), [`src/eval_backends.py`](../../src/eval_backends.py). Raw captures: `docs/sources/dr-gem-int-*` (14 searches, 25 scrapes), plus `dr-gem-docs-{pricing,video,models}.md` and `dr-tech-*` from earlier passes.
Tags: **VERIFIED** = read in primary docs or SDK source today, or run locally. **UNVERIFIED** = check on-site.

## TL;DR
- Both backends sit behind one interface, `verify(clip_bytes, camera_ctx) -> Verdict` with fields `{escalate, event, severity: low|med|high, reason, box_2d: [ymin,xmin,ymax,xmax] 0–1000 | null}`, plus `backend`, `model`, and `latency_ms`. Cosmos is primary. Gemini takes over for `CB_COOLDOWN_MIN` minutes when Cosmos times out or returns 404/5xx, or after 3 consecutive soft failures. Every call has a Weave trace with `backend` and `breaker_state` attributes.
- **Use the native `google-genai` SDK. Don't use Gemini's OpenAI-compatible endpoint for this.** The compat endpoint does not take video input. Its docs cover only `image_url` and audio, and `/v1/videos` is Veo *generation* (also confirmed in 04-gemini-docs).
- **API path:** `GeminiBackend` uses the **Interactions API** (`client.interactions.create`, GA June 2026, the one Google recommends) by default. The installed SDK has it (VERIFIED in 2.27.0). It falls back to legacy `models.generate_content` if `interactions` is missing, or if `GEMINI_API_MODE=generate_content`. Both request shapes were tested against the live endpoint with a dummy key and got as far as the server's key check (`400 API key not valid`), so the SDK accepts both payloads. The interactions call sends `processing={"type":"static","fps":2}`, `resolution:"low"`, the text prompt *after* the video, `response_format={"type":"text","mime_type":"application/json","schema":…}`, `generation_config={"thinking_level":…}` and **`store=False`**, since Interactions are stored server-side by default.
- **Weave caveat (VERIFIED, weave 0.53.11 source):** autopatch covers `Models.generate_content`, `generate_content_stream`, `count_tokens` and `generate_images` only. **`interactions.create` is not autopatched.** Our own `@weave.op` (`gemini_verify`) still traces every call, with inputs and outputs. If you want token usage auto-captured in Weave, set `GEMINI_API_MODE=generate_content`.
- **Two gotchas that would break the demo:** (1) Gemini 3 returns **404 NOT_FOUND** (2.5-era: 500) for an mp4 **with no audio stream**, unless `media_resolution=HIGH` is set. Webcam chunks made with `ffmpeg -an` have no audio stream. The module adds a silent track with ffmpeg when it can, and otherwise switches to HIGH. (2) In SDK 2.27.0, **retries are off by default** (`retry_options=None` gives `stop_after_attempt(1)`). The troubleshooting page says the SDK retries automatically, but the SDK source says otherwise. We set retries explicitly.
- **Cost is the real limit on how much Gemini can carry.** The default fallback model is **`gemini-3.5-flash-lite`** with thinking `minimal`, at ~$0.0006–0.0007 per 5 s clip, which is **~$0.014 per camera-hour** at a 3% verify rate. `gemini-3.8-flash` (thinking forced to `low`, because `minimal` errors on 3.8) costs ~$0.053 per camera-hour, ~$38 per camera-month. Even Flash-Lite running 24/7 is ~$10 per camera-month, more than the $8 price. That means Gemini can only be the **outage fallback**. Self-hosted Cosmos stays primary.

## 1. Setup

```bash
# nw-verifier/requirements.txt  (do NOT copy the blueprint's pydantic==2.5.2 pin into this function)
google-genai==2.27.0        # pure-Python wheel (py3-none-any), Python >=3.10, NO grpc; deps: httpx, pydantic>=2.12.5,
                            # google-auth, tenacity<9.2, websockets, anyio, requests  (VERIFIED: pip METADATA, PyPI)
openai>=1.40                # Cosmos NIM client (OpenAI-compatible); weave autopatches it too
weave                       # 0.53.11 tested; autopatches google.genai + openai on weave.init()
pydantic>=2.12.5
# Aptfile (optional but recommended): ffmpeg   -> used to add a silent audio track for Gemini 3
```
- **Pydantic conflict (VERIFIED):** `google-genai` 2.27 requires `pydantic>=2.12.5`, but the blueprint's shared block pins `pydantic==2.5.2` / `pydantic-settings==2.1.0`. `nw-verifier` is a new function, so give it its own requirements. If you're forced onto the old pin, call Gemini over raw REST with `requests` instead (section 6). Weave won't autopatch that path, but the `@weave.op` wrapper still traces it.
- Build: `vastde functions init python-pip nw-verifier` → copy both modules in → `vastde functions build nw-verifier --image-tag v1` (linux/amd64; see 01-technical Gotcha #6).
- Handler (blueprint import style):
```python
from verifier_backends import verify, SEV_TO_INT
def handler(ctx, event):
    d = event.get_data()                                   # from nw-scorer: {"segment_id", "source", "camera_ctx", ...}
    clip = s3.get_object(Bucket=b, Key=k)["Body"].read()   # pass S3 URIs on the event, never base64 video
    v = verify(clip, d["camera_ctx"])                      # raises BackendError if BOTH backends fail -> let DataEngine retry
    return {**d, **v.model_dump(), "severity_int": SEV_TO_INT[v.severity], "status": "success"}
```
- Gemini key: create it in AI Studio. Keys made there are restricted to the Gemini API by default. **Since June 19 2026 the Gemini API rejects unrestricted keys** (forum announcement in `dr-gem-int-p23`). Put it in the DataEngine secret, never in the image.

### Env vars
| Var | Default | Notes |
|---|---|---|
| `COSMOS_NIM_URL` | — (required) | e.g. `http://<cosmos_host>:8001/v1` (venue NIM from `vss2-secret`) |
| `COSMOS_MODEL` | `nvidia/cosmos-reason2-8b` | `-2b` for speed |
| `COSMOS_API_KEY` | `not-used` | Bearer for hosted/gateway NIMs |
| `COSMOS_TIMEOUT_S` | `20` | set **12** for the live stage camera |
| `COSMOS_FPS` | unset (NIM default 4) | sent as `media_io_kwargs` (UNVERIFIED on venue NIM) |
| `COSMOS_BBOX_SCALE` | `1000` | set `1024` if on-site test shows Qwen-style 0–1024 |
| `GEMINI_API_KEY` | — (required for fallback) | |
| `GEMINI_MODEL` | `gemini-3.5-flash-lite` | `gemini-3.8-flash` for higher quality (GA Sep 2 2026) |
| `GEMINI_API_MODE` | `interactions` | `generate_content` = legacy path, autopatched by Weave |
| `GEMINI_FPS` | `2` | default sampling is 1 fps; a 5 s clip at 1 fps = 5 frames, too sparse for "picks up box" |
| `GEMINI_THINKING` | `minimal` | auto-coerced to `low` on 3.8 Flash, where `minimal` returns an error |
| `GEMINI_TIMEOUT_S` | `15` | SDK timeout is in **ms** internally (`HttpOptions.timeout`) |
| `CB_FAILS` / `CB_COOLDOWN_MIN` | `3` / `5` | breaker thresholds |
| `WANDB_API_KEY`, `WEAVE_PROJECT` | — / `unwatched` | eval + traces |

## 2. Backend details

| | CosmosNIMBackend | GeminiBackend |
|---|---|---|
| Transport | OpenAI SDK → `{COSMOS_NIM_URL}/chat/completions`, `max_retries=0` | `google-genai` `interactions.create(store=False)` (default) or `models.generate_content` |
| Video | `{"type":"video_url","video_url":{"url":"data:video/mp4;base64,…"}}` (blueprint format, VERIFIED 01-technical §1.5) | Interactions: `{"type":"video","data":b64,"mime_type":"video/mp4","processing":{"type":"static","fps":2},"resolution":"low"}`. Legacy: `Part(inline_data=Blob, video_metadata=VideoMetadata(fps=2))` + `media_resolution`. Text goes **after** the video. Inline limit **<20 MB** request (VERIFIED). **Never agentic** for 5 s clips |
| Structured output | Prompt-enforced: `<think>…</think>` then JSON. The parser strips think and fences, then validates with Pydantic | Interactions: `response_format={"type":"text","mime_type":"application/json","schema":VerdictOut.model_json_schema()}` → `output_text`. Legacy: `response_mime_type` + `response_json_schema`. Enum, nullable, and min/maxItems are in the supported subset (VERIFIED) |
| Box | asks for `bbox_2d: [x1,y1,x2,y2]` 0–1000, converted by `xyxy_to_box2d` | asks for `box_2d: [ymin,xmin,ymax,xmax]` 0–1000 natively |
| Retries | none (breaker handles it) | Legacy: explicit `HttpRetryOptions(attempts=2, 0.5–2 s, codes 408/429/5xx)`, because the default is none. Interactions client (Speakeasy-generated) has its own default of up to 4 retries with 0.5–8 s backoff on 408/409/429/5XX (VERIFIED in `_gaos/_internal.py`). The per-call `timeout=GEMINI_TIMEOUT_S` bounds the request (UNVERIFIED whether it bounds the whole retry loop or each attempt) |
| Tokens | NIM | Gemini 3, video at `low`: **70 tok/frame**; audio **25 tok/s**; `high` = 280 tok/frame (VERIFIED, media-resolution doc) |

**Box coordinate order:**
- Gemini: `[ymin, xmin, ymax, xmax]`, origin top-left, each axis normalized to 0–1000 (VERIFIED: ai.google.dev image-understanding, Vertex bounding-box doc).
- Cosmos-Reason2: the NIM docs only state that **points** are 0–1000 with x right and y down, each axis independent (VERIFIED). The bbox *shape* follows Qwen3-VL, `{"bbox_2d":[x1,y1,x2,y2],"label":…}` on a 0–1000 scale (Qwen3-VL/ms-swift docs, HN, DebuggerCafe). One Cosmos fine-tuning guide (Datature) says Qwen-family examples "use … 0-1024". So Cosmos is **xyxy** while Gemini is **yxyx**, and the scale is UNVERIFIED (expect 1000). Check it at 10:00 with one image, then set `COSMOS_BBOX_SCALE`.
- The canonical form is Gemini's. `box2d_to_pixels(box, W, H)` gives `(x1,y1,x2,y2)` pixels for the Slack keyframe burn-in.

**Severity mapping:** `SEV_TO_INT = {low:2, med:3, high:4}`. The pusher's "sev ≥ 4" rule from FINAL-IDEA §5 becomes `severity == "high"`.

## 3. Failure rules (circuit breaker)

| Condition (Cosmos) | Classified | Action |
|---|---|---|
| Client timeout > `COSMOS_TIMEOUT_S` | hard | trip now; **this clip** re-verified on Gemini |
| HTTP 404 (hosted "Function not found for account", known since Jan 2026) | hard | trip now |
| HTTP 5xx; connection refused/reset (mapped to 503) | hard | trip now |
| 429, 4xx, no JSON, schema mismatch | soft | count; **3 consecutive** → trip. This clip still goes to Gemini |
| Breaker OPEN | — | all traffic → Gemini for `CB_COOLDOWN_MIN` (5 min) |
| Cooldown elapsed (HALF-OPEN) | — | next clip probes Cosmos. Success closes the breaker; any failure re-opens it for another cooldown |
| Gemini also fails (after its 2 SDK attempts) | — | `BackendError` raised → handler lets DataEngine retry (blueprint `TransientError` pattern). **Never** default to "dismiss" silently |
| Gemini 404/500 on a no-audio clip (reported for generateContent; assumed to apply to Interactions too, UNVERIFIED) | — | prevented up front: `_has_audio_track` (mp4 `hdlr…soun`) → ffmpeg `anullsrc` remux (`-c:v copy`) or `MEDIA_RESOLUTION_HIGH` |
| Gemini 400 (bad schema / param) | — | bug. Don't retry; fix the schema |

- Breaker state lives **in memory, per pod**. With N verifier pods, each one trips on its own first hard failure, so the cost is at most one slow clip per pod. If you want one shared state (stretch), put it in a 1-row VastDB table `nw_breaker(open_until)`.
- Gemini guidance matches this design: retry 429/503 with exponential backoff (troubleshooting page). Long synchronous requests under backend retries can show up as **401 or timeout** (video doc), which is another reason to keep clips short and timeouts tight.
- Rate limits are **per project, not per key**. Paid Tier 1 also has a **$10 per 10-minute spend cap** (VERIFIED). Fallback volume (~22 calls per camera-hour) is far below that.

## 4. Latency budget (live camera #5, verify stage only)

| Path | Estimate | Basis |
|---|---|---|
| Cosmos-8B verify with `<think>`, max_tokens 1024 | 5–15 s | 01-technical §4.4 estimate (UNVERIFIED; measure `processing_time`) |
| Gemini inline upload of a 1–3 MB 5 s clip | 0.3–1 s | venue Wi-Fi 20–50 Mbps (UNVERIFIED) |
| Gemini 3.8 Flash, static 2 fps, thinking low, ~1.3k input / ~400 output tokens | ~2–6 s | No published TTFT for short video. The docs say static mode is the low-latency choice for clips under 5 min, and agentic mode raises TTFT on short clips. **Measure** with `eval_backends.py --only gemini` (latency scorer) |
| ffmpeg silent-audio remux (if needed) | <0.3 s | `-c:v copy`, tested locally on a 5 s clip |
| **Worst case, first clip after an outage** | `COSMOS_TIMEOUT_S` + ~5 s ≈ **17 s at 12 s timeout** | breaker cost; later clips skip Cosmos |
| Stage target | verdict ≤ 10 s after the segment lands | streaming the `<think>` text covers the wait |

Don't turn on Gemini "agentic" video processing. It is meant for long-form video and adds TTFT on short clips.

## 5. Cost per camera-hour at ~3% verify rate (cite: ai.google.dev pricing, `dr-gem-docs-pricing.md`)

Assumptions: 720 five-second segments per camera-hour × 3% = **21.6 verify calls/hr**. Per call input = 10 frames × 70 + 5 s × 25 audio + ~450 prompt ≈ **1,275 tokens**. Output (JSON plus thinking) ≈ **400** at `low`, ≈100 at `minimal`.

| Model (paid tier, per 1M in/out) | $/call | **$/camera-hour** | $/camera-month (720 h) |
|---|---|---|---|
| gemini-3.8-flash, $0.75 / $3.75 (promo through Dec 31 2026) | $0.0025 | **$0.053** | $38 |
| gemini-3.8-flash from Jan 1 2027, $1.50 / $7.50 | $0.0049 | $0.106 | $76 |
| gemini-3.8-flash **Flex/Batch** $0.375 / $1.875 (archive path, not live) | $0.0012 | $0.027 | $19 |
| gemini-3.5-flash-lite, $0.30 / $2.50, thinking low | $0.0014 | $0.030 | $22 |
| **gemini-3.5-flash-lite, thinking minimal (DEFAULT fallback)** | $0.0006 | **$0.014** | $10 |
| gemini-3.5-flash, $1.50 / $9.00 | $0.0055 | $0.119 | $86 |
| no-audio clip at `HIGH` (280 tok/frame), 3.8 Flash | $0.0039 | $0.085 | $61 |

**What this means for the pitch:** at ~$0.05 per camera-hour, Gemini works as an outage fallback. If Cosmos is down 5% of the time, it adds ~$2 per camera-month. Gemini can't be the primary verifier at the $8/camera/month price, so the pitch should stay "self-hosted Cosmos on the GPU we already run, Gemini only when it's down." **Turn billing on before sending any real CCTV footage.** Free-tier inputs are "used to improve our products" (pricing page, "Used to improve our products: Yes" for free, "No" for paid). Use the free tier only for synthetic or staged demo clips.

## 6. Egress from DataEngine functions (UNVERIFIED — test at 10:00)

- No VAST doc mentions egress. Functions run on a **customer-attached Kubernetes cluster** (KB "Overview of VAST DataEngine"), so outbound internet depends on that cluster's NetworkPolicy and NAT.
- There is indirect evidence that egress is normal. The blueprint's embedder has a cloud mode (`embedding_local_nim=false` → `Authorization: Bearer nvidia_api_key` to a hosted NIM), and the secret template carries `nvidia_api_key`.
- `google-genai` uses httpx with `trust_env=True`, so `HTTPS_PROXY` in the function env is respected (VERIFIED, SDK README).
- 10:00 smoke test from inside a function (header auth, never key-in-URL):
```python
requests.get("https://generativelanguage.googleapis.com/v1beta/models", headers={"x-goog-api-key": key}, timeout=5).status_code
```
- **If egress is blocked:** run the same `GeminiBackend` from the laptop as a poller over `nw_verdicts WHERE verdict='error'` (FINAL-IDEA §10 fallback pattern). Same module, same Weave project.
- REST fallback (for the pydantic-pin case, or if the SDK misbehaves): `POST /v1beta/models/{model}:generateContent`, body `{"contents":[{"parts":[{"inline_data":{"mime_type":"video/mp4","data":b64},"video_metadata":{"fps":2}},{"text":prompt}]}],"generationConfig":{"responseMimeType":"application/json","responseJsonSchema":schema,"mediaResolution":"MEDIA_RESOLUTION_LOW","thinkingConfig":{"thinkingLevel":"low"}}}`. Field casing follows the REST reference. Check it with a single curl before relying on it.

## 7. Weave
- `weave.init(project)` autopatches `openai` (Cosmos) and `google.genai` `generate_content`. Each backend `verify` is an `@weave.op` (`cosmos_verify` / `gemini_verify`) under the router op `nw_verify`. `weave.attributes({"backend", "breaker_state", "camera_id"})` makes the traces filterable by backend. `postprocess_inputs=_redact` replaces raw clip bytes with `<N bytes>`, so video never lands in W&B.
- `eval_backends.py` runs one `weave.Evaluation` ("nw-verifier-backends") over `clips/labels.jsonl`, once per backend (`display_name = backend:model`). Scorers: `correct`, `tp`/`fp`/`fn` (precision/recall, false pages), `valid_json`, `latency_ms`, `under_10s`, bbox `iou` (only on rows with `expected_box_2d`). Compare the runs in the Weave Evaluations tab. It was tested locally with fake backends (Weave summary keys `true_count`/`true_fraction`/`mean` confirmed). It also prints a one-line summary per backend.
- Run: `python src/eval_backends.py --labels clips/labels.jsonl --project <team>/unwatched` (add `--only gemini` to test the fallback alone).

## 8. Verified locally
- `python3 -m py_compile` passes for both files. Import check passes in a scratch venv (google-genai 2.27.0, openai 3.23.0, weave 0.53.11, pydantic 2.13.5, Python 3.14).
- Unit checks passed: xyxy→yxyx conversion, including swapped corners and the 1024 scale; pixel conversion; JSON extraction from `<think>` + fenced output; the mp4 audio-track detector; ffmpeg silent-audio remux (no audio → has audio); `GenerateContentConfig` / `Part` / `VideoMetadata` / `ThinkingConfig` construct without error. Breaker transitions: hard error → open → Gemini only → half-open → Cosmos success → closed; 3 soft errors → open.
- Shape test: both Gemini paths (Interactions and generateContent) × both models were sent to the real endpoint with a dummy key. All four returned `400 API key not valid`, which means the SDK accepted the payloads. The no-audio test clip was remuxed with ffmpeg first. `BackendError.status` was extracted correctly from both error types.
- **Not tested:** real verdicts from Gemini or Cosmos, because no keys or endpoint were available here. Run `eval_backends.py` at 10:00.

## Sources
1. PyPI google-genai 2.26.0 (Sep 30 2026), py3-none-any, Python ≥3.10 — https://pypi.org/project/google-genai/ (`dr-gem-int-p01`). Installed 2.27.0 METADATA checked locally.
2. Weave × Google integration, autopatch of the GenAI SDK — https://docs.wandb.ai/weave/guides/integrations/google (`p02`); weave 0.53.11 `integrations/google_genai/google_genai_sdk.py` (patches `Models.generate_content`, `generate_content_stream`, `count_tokens`, `generate_images`).
3. Gemini OpenAI compatibility (image/audio input only; `/v1/videos` = Veo) — https://ai.google.dev/gemini-api/docs/openai (`p03`)
4. Structured output (Interactions API) — https://ai.google.dev/gemini-api/docs/structured-output (`p04`)
5. Structured output (generateContent), JSON-Schema subset — https://ai.google.dev/gemini-api/docs/generate-content/structured-output (`p05`)
6. Image understanding / object detection, `box_2d [ymin,xmin,ymax,xmax]` 0–1000 — https://ai.google.dev/gemini-api/docs/image-understanding (`p06`)
7. Troubleshooting, retry strategy for 429/503 — https://ai.google.dev/gemini-api/docs/troubleshooting (`p07`)
8. Rate limits, per-project and spend caps — https://ai.google.dev/gemini-api/docs/rate-limits (`p08`)
9. Datature, fine-tuning Cosmos-Reason2 (Qwen 0–1024 note) — https://datature.io/blog/finetuning-your-own-cosmos-reason2-model (`p09`)
10. ms-swift Qwen3-VL best practice (`bbox_2d`, normalized 1000) — https://swift.readthedocs.io/en/v3.9/BestPractices/Qwen3-VL-Best-Practice.html (`p10`)
11. Vertex/Gemini Enterprise bounding-box detection (image **and video frames**) — https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/bounding-box-detection (`p11`)
12. Media resolution, Gemini 3 token table (video 70/280 per frame, audio 25/s) — https://ai.google.dev/gemini-api/docs/media-resolution (`p12`)
13. python-genai #2019, VideoMetadata fps on inline_data — https://github.com/googleapis/python-genai/issues/2019 (`p13`)
14. python-genai #854, `video_metadata` 500s fixed by adding an audio track — https://github.com/googleapis/python-genai/issues/854 (`p14`)
15. VAST KB, DataEngine overview (external K8s cluster) — https://kb.vastdata.com/documentation/docs/overview-of-vast-dataengine-2 (`p15`)
16. Weave Evaluations — https://docs.wandb.ai/weave/guides/core-types/evaluations (`p16`)
17. Gemini API errors (404 model_not_found, 429, 500, 503, 504) — https://ai.google.dev/gemini-api/docs/api-errors (`p17`)
18. Thinking levels per model — https://ai.google.dev/gemini-api/docs/thinking (`p18`)
19. Google Cloud blog, reduce 429s (backoff with jitter) — https://cloud.google.com/blog/products/ai-machine-learning/reduce-429-errors-on-vertex-ai (`p19`)
20. Weave leaderboard quickstart — https://docs.wandb.ai/weave/cookbooks/leaderboard_quickstart (`p21`)
21. HN, "Is Gemini 2.5 good at bounding boxes?" — https://news.ycombinator.com/item?id=44520292 (`p22`)
22. Forum, audio-track extraction failures, plus the June 19 2026 unrestricted-key notice — https://discuss.ai.google.dev/t/gemini-silently-failing-if-audio-cant-be-extracted-from-video-container/129898 (`p23`)
23. Weave EvaluationLogger — https://docs.wandb.ai/weave/guides/evaluation/evaluation_logger (`p24`)
24. Forum, **Gemini 3 404 on video without audio unless MEDIA_RESOLUTION_HIGH** — https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805 (`p25`)
25. Gemini pricing (3.8 Flash promo, 3.5 Flash-Lite, Flex/Batch) — https://ai.google.dev/gemini-api/docs/pricing (`dr-gem-docs-pricing.md`)
26. Gemini video understanding (inline <20 MB, fps, static vs agentic, prompt after video, 401/timeout note) — https://ai.google.dev/gemini-api/docs/video-understanding (`dr-gem-docs-video.md`)
27. Gemini models list (model IDs) — https://ai.google.dev/gemini-api/docs/models (`dr-gem-docs-models.md`)
28. NIM Cosmos-Reason2 API (video_url data URI, 0–1000 point coords) — https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html (`dr-tech-nim-cosmos-reason2-api.md`)
29. vss-blueprint functions (cloud NIM mode, transient-status retry pattern) — `dr-tech-vss-blueprint-functions.md`
30. Circuit breaker pattern, closed/open/half-open — https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker ; TrueFoundry LLM failover — https://www.truefoundry.com/blog/llm-failover-load-balancing-provider-outages (`s12`)
31. Teammate digest of Gemini docs (Interactions API GA, model and thinking table, `store=False`, processing params) — `docs/deep-research/04-gemini-docs.md`
32. Search result sets: `dr-gem-int-s01…s14.json` (SDK version, Weave/genai, OpenAI compat, DataEngine egress ×2, retry, Cosmos bbox, Gemini video bbox, fps metadata, Weave eval, latency, circuit breaker, no-audio errors, EvaluationLogger).
