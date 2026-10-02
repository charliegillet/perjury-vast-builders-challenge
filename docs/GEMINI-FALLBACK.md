# Deep Research: Gemini video understanding as UNWATCHED's fallback verifier

Compiled 2026-10-02, the morning of the SF build. Exhaustive tier, 3 parallel passes: about 55 searches, about 100 pages scraped, and 4 papers read. Detailed reports:
- [deep-research/04-gemini-docs.md](deep-research/04-gemini-docs.md): the Gemini API reference, with exact parameters and snippets
- [deep-research/05-gemini-vs-cosmos.md](deep-research/05-gemini-vs-cosmos.md): benchmarks, failure modes, privacy, judge framing
- [deep-research/06-gemini-integration.md](deep-research/06-gemini-integration.md): setup, env vars, cost, latency, failover rules
- Code: [`src/verifier_backends.py`](../src/verifier_backends.py) and [`src/eval_backends.py`](../src/eval_backends.py)

Raw captures are in `docs/sources/dr-gem-docs-*`, `dr-gem-cmp-*` and `dr-gem-int-*`.

## Executive Summary

Gemini works as an **outage fallback** for the verify step. It should not be the primary verifier at today's hackathon.
- The fastest path is one call with the 5-second clip sent inline: base64 mp4, static processing, 2–4 fps, low resolution, `store=False`.
- That costs about **$0.0007 per clip** on `gemini-3.5-flash-lite`.
- Latency is the weak point. Measured time to the first answer token is around **5–9 s**, with occasional very long stalls. Self-hosted Cosmos reports about 1 s for alert verification.
- The hosted endpoint sends footage to Google, which conflicts with the "footage never leaves the cluster" story. On the free tier Google trains on inputs and human reviewers may see them.

The more important finding is about Cosmos itself. On **VANTAGE-Bench** (NVIDIA + Clemson, Sep 2026), a benchmark for fixed-camera footage:

| Model | Overall | Event verification | Specificity |
|---|---|---|---|
| Gemini 3.6 Flash | 69.5 | 82.0 | 76.3 |
| Cosmos3-Super | 63.6 | — | — |
| Cosmos3-Nano | 60.7 | — | — |
| Cosmos-Reason2-8B | 54.5 | 64.1 | **57.6** |

A specificity of 57.6 means Reason2-8B **accepted about 42% of events that never happened**. That directly threatens the "doesn't cry wolf" pitch, though the sample is only 163 clips. So:
- Use **Cosmos 3** (Super or Nano) if the venue serves it.
- Write **class-specific prompts**. Naming the event classes lifted F1 from 0.09 to 0.64 in one study.
- **Measure specificity on our ~60 labelled clips in Weave** before we claim anything.

## Key Findings

1. **The API surface has changed.** Google now recommends the Interactions API (`client.interactions.create`, GA June 2026); `generateContent` is legacy but still works. Current models are `gemini-3.8-flash` (GA Sep 2) and `gemini-3.5-flash-lite`. Vertex AI is now "Gemini Enterprise Agent Platform". ([ai.google.dev video understanding](https://ai.google.dev/gemini-api/docs/video-understanding); `04-gemini-docs.md`)
2. **The OpenAI-compatible endpoint doesn't accept video.** Use the native `google-genai` SDK. (`04`)
3. **Inline limit:** about 20 MB is safe; the docs contradict themselves with "<100 MB". Default sampling is 1 fps, which gives only 5 frames per 5 s clip, and the cap is 24 fps. Use static mode, because agentic mode adds time to the first token on clips under 5 minutes. (`04`)
4. **Tokens per 5 s clip:** about 475 at 1 fps and low resolution, and about 1,875 at 5 fps, plus about 250 for the prompt and schema. Google's pages conflict on per-frame figures, so check with `count_tokens` or `usage`. (`04`)
5. **Cost per clip on the paid tier:** 3.5 Flash-Lite about $0.0007, 3.1 Flash-Lite about $0.0004, 3.8 Flash about $0.0026 (promo price until Dec 31). Output and thinking tokens make up most of it. 3.8 Flash can't go below `low` thinking; `minimal` returns an error. (`04`)
6. **Rate limits are no longer published per model.** They're per project and shown in AI Studio. Tier 1 has a $10 per 10-minute spend cap, and going over it returns 429. Check AI Studio before 10:00. (`04`)
7. **Data policy:** on the free tier Google trains on inputs and human reviewers may read them. Interactions are stored by default (1 day free, 55 days paid) unless you send `store=False`. EEA, Switzerland and UK users get paid terms, which matters for London. Google's policy bans identifying people, or tracking or monitoring them, without consent. (`04`, `05`)
8. **Bounding boxes:** Gemini returns `box_2d = [ymin,xmin,ymax,xmax]` on a 0–1000 scale. Cosmos, following the Qwen3-VL family, returns `bbox_2d = [x1,y1,x2,y2]`, and its 0–1000 vs 0–1024 scale is **unverified**, so it's set through `COSMOS_BBOX_SCALE`. (`06`)
9. **Gemini 3 returns an error on an mp4 with no audio track** unless resolution is high. Webcam chunks recorded with `-an` have none, so the code adds a silent track with ffmpeg. (`06`)
10. **Live API:** `gemini-3.8-live` takes at most 1 JPEG frame per second and answers only in audio. It has no structured output, and sessions are short (2 minutes for audio plus video without compression). It's not suitable for camera #5. (`04`)
11. **Benchmarks:** Cosmos wins on locating objects in the frame (83.9–87.0 vs 81.6), on warehouse and self-driving questions, and on on-prem latency. Timestamps inside a clip are roughly a tie (≤52 mIoU for all), and Flash-Lite's 24 is poor. (`05`, VANTAGE-Bench)
12. **Gemini on CCTV anomaly datasets** is conservative with a generic prompt: 85–100% precision but 1–6% recall. Class-specific prompts help a lot. Google's own Gemini for Home has publicly hallucinated people and animals (Ars Technica, Android Authority, The Verge). (`05`)
13. **No Gemini low-light numbers exist.** Every model tested degrades badly at night, and the Cosmos-Reason2 card lists low light with motion blur as a known limitation. (`05`)
14. **Cost at a 3% verify rate** (21.6 calls per camera-hour):

    | Model | Per camera-hour | Per camera-month |
    |---|---|---|
    | Flash-Lite | ~$0.014 | ~$10 |
    | 3.8 Flash | ~$0.053 | ~$38 |

    Both are above our $8/camera/month price, which confirms Gemini can only be a fallback. (`06`)

## Detailed Analysis

**Decision rule (implemented in `verifier_backends.py`):**
- **Primary:** Cosmos on the venue's model server. Prefer Cosmos 3 Super or Nano over Reason2-8B if both are offered.
- **Fail over to Gemini immediately** on a Cosmos timeout (10–20 s), a 404 or 5xx error, or a refused connection.
- **Also fail over after 3 soft failures in a row:** a 429, invalid JSON, or the wrong schema.
- **Stay on Gemini for 5 minutes,** then send one clip back to Cosmos to see if it has recovered.
- **The failed clip is always re-checked on Gemini.** If both backends fail, the code raises an error so DataEngine retries; it never quietly dismisses the clip.
- **Every verdict records which backend and model produced it,** both in the verdict and in Weave, so the dashboard and Slack can show which model decided.

**The eval at 10:00 (`eval_backends.py`):** run both backends over the ~60 labelled clips and log a Weave Evaluation comparing precision, recall, **specificity**, JSON validity and p50/p95 latency. That table is the evidence for:
- (a) which model is primary,
- (b) whether to turn on an optional *veto-only* Gemini second opinion, which is only worth it if it improves precision,
- (c) our stage claim about suppressed false alarms.

**Setup checklist** (detail in `06`):
- Turn on billing for a paid key, and never send real faces on the free tier.
- Set `GEMINI_API_KEY`, `GEMINI_MODEL=gemini-3.5-flash-lite`, `GEMINI_FPS=2`, `COSMOS_NIM_URL` and `WANDB_API_KEY`.
- Give `nw-verifier` its own requirements file, because the blueprint pins `pydantic==2.5.2` and google-genai needs 2.12.5 or later.
- Add ffmpeg to the container.
- Test outbound internet from a DataEngine function at 10:00. It isn't documented anywhere, and if functions can't reach Google, the Gemini fallback has to run from a laptop service.

## Contrarian Views And Risks
- **"Why not just use Gemini? It scores higher."** On VANTAGE overall and on event verification, it does. *Answer:* footage stays on the cluster with open models, on-prem latency is about 1 s versus 5–9 s, there's no cost per call, and Cosmos 3 is the top open model on that benchmark. Credit the benchmark rather than dodging it.
- **Sponsor optics.** NVIDIA, VAST and CoreWeave are judging, and Gemini is no sponsor's product. Keep it off the main path in the demo. Mention it only as resilience ("circuit-breaker fallback, here's the Weave comparison").
- **Latency spikes.** Practitioners report occasional 2-minute responses and Files API stalls of 2–25 minutes. Send clips inline only, and keep a hard timeout.
- **Cost of thinking.** Output and thinking tokens drive the cost. Keep thinking at minimal or low.
- **Hallucinated identities.** Never ask Gemini or Cosmos *who* someone is. Ask about activity only.
- **Our own claim at risk.** If our specificity measurement comes out like VANTAGE's (about 58% for Reason2-8B), "doesn't cry wolf" is false. Measure it before the demo video and present the number honestly.

## Open Questions
1. Which Cosmos model does the venue serve: Reason2 2B/8B, Reason 3 Nano, or Cosmos3-Super?
2. Can DataEngine functions reach the internet (generativelanguage.googleapis.com)?
3. What are the project's real Gemini rate limits in AI Studio, and how many tokens does a 5 s clip actually use (`count_tokens`)?
4. Is the Cosmos bounding-box scale 0–1000 or 0–1024?
5. Does the Interactions API take clip offsets as strings or numbers? (Not needed for whole 5 s clips.)
6. Are Gemini's real latencies on venue wifi within a 10 s budget?

## Sources
Each detailed report lists every URL and its capture file:
- `04-gemini-docs.md`: 43 Google doc pages and 11 searches (`dr-gem-docs-*`): ai.google.dev video understanding, Files API, Interactions API, structured output, object detection, Live API, pricing, rate limits, terms and data use, the OpenAI-compatibility page, Vertex / Agent Platform docs.
- `05-gemini-vs-cosmos.md`: 32 scrapes, 30 searches and 4 papers (`dr-gem-cmp-*`): the VANTAGE-Bench paper (NVIDIA + Clemson, Sep 2026), the Cosmos-Reason2 model card, VLM anomaly-detection papers, Artificial Analysis latency, NVIDIA VSS alert-verification latency, Gemini for Home coverage (Ars Technica, Android Authority, The Verge), Google's prohibited-use policy.
- `06-gemini-integration.md`: 25 scrapes and 14 searches (`dr-gem-int-*`): the google-genai SDK and PyPI pages, Weave integrations, retry guidance, box_2d docs, Qwen3-VL grounding format, Cosmos fine-tuning guides.
- Entry point: https://ai.google.dev/gemini-api/docs/video-understanding

## Rerun Inputs
workflow: firecrawl-deep-research
topic: Gemini API video understanding as a fallback verifier for UNWATCHED (vs Cosmos-Reason2/Cosmos 3), starting from https://ai.google.dev/gemini-api/docs/video-understanding
depth: exhaustive
output: markdown
