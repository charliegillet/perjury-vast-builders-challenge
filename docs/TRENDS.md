# Fast video understanding: what's trending (Oct 2026) and what it means for UNWATCHED

> **Cleanup note (2026-10-02):** some raw captures and docs cited below were moved to [`unwanted/`](../unwanted/README.md) with their paths preserved (e.g. `docs/sources/x.md` is now `unwanted/docs/sources/x.md`). See `unwanted/MANIFEST.tsv`.

This is a web-wide sweep run with firecrawl on 2026-10-02 by 3 parallel agents: about 110 searches and about 120 pages scraped. Raw captures are in `.firecrawl/trend-models-*`, `trend-oss-*` and `trend-mkt-*`. The detailed reports are:
- [trends/01-fast-video-models.md](trends/01-fast-video-models.md): models, speed techniques, embedders, benchmarks
- [trends/02-trending-oss.md](trends/02-trending-oss.md): open-source projects, with stars and licenses from the GitHub API
- [trends/03-products-startups-buzz.md](trends/03-products-startups-buzz.md): launches, funding, hackathon winners, what builders are saying

## TL;DR: change these today
1. **Verifier model order: Cosmos3-Super, then Cosmos3-Nano, then Reason2-8B.** VANTAGE Event Verification scores are 71.3, 68.9 and 64.1. Reason2-8B's specificity is 57.6, meaning it accepts about 42% of events that never happened. ([01](trends/01-fast-video-models.md))
2. **Verify in two steps.** First a 1-token YES/NO gate (Reason2-8B takes 0.58 s on an H100, Nano 146 ms). Only on YES, run the full reasoning prompt for the Slack explanation. Today `src/verifier_backends.py` always asks for up to 1,024 tokens of reasoning, which is the slowest option.
3. **Set `COSMOS_FPS=2`** (the NIM default is 4, and throughput roughly halves each time fps doubles). If we run our own vLLM server, add `--video-pruning-rate 0.6`; it skips patches that don't change between frames and gives up to 4× faster first tokens on fixed cameras.
4. **Embedder decision before ingest:** `Cosmos-Embed1-448p-anomaly-detection` outputs **768-d** vectors (the 224p model is 256-d). Switching means a different VastDB column and different centroids, so decide by 11:00.
5. **Fast pre-filter if the GPU is crowded:** Cosmos3-Edge (4B) gives a yes/no in about 142 ms and scores 63.4 on event verification, close to Reason2-8B.
6. **Skip streaming VLMs for 5 s clips.** They underperform general models on OVO-S-Bench, and SimpleStream shows that feeding the last 4 frames to a standard model matches them.

## Positioning, updated
- **The new vocabulary is "always-on agents."** OpenAI dots (Sep 29), NVIDIA VSS 3.2's "always-on video agents" (Jul 15), and TwelveLabs' $100M round with "the archive stops being passive storage" (Jul 1). Lead with **always-on, filter before you spend, verified, provenance**. Don't headline "anomaly detection" or "real-time," and avoid "search engine for the physical world" or "God-mode" after the backlash against Orchestra.
- **Google productized "decide what to watch" inside a single video:** Gemini agentic video, Sep 1, with up to 88% fewer tokens. Stage line: *"Gemini decides what to watch inside one video; UNWATCHED decides which of 10,000 camera-hours deserve a question at all."*
- **The open-source overlap is Frigate (36k★).**
  - Version 0.17 added AI review summaries with a threat level 0–2, plus a hand-written description of what's normal for each camera.
  - Version 0.18 (Sep 12) added a chat agent with on-demand recaps.
  - Stage line: *"Frigate makes you write down normal; UNWATCHED learns it."*
- **Closest prior art to credit:**
  - Qdrant `video-anomaly-edge` (Mar 2026): distance from a normal baseline, with about 10% sent to VSS. Its baseline comes from a dataset and its VLM only enriches clips, never blocks them.
  - ZooVision, 3rd at the SF TwelveLabs/Neo4j hack (Jul 30): overnight footage turned into a morning handoff.
  - NOVA and MoniTor (arXiv, Sep 2026): research that learns what normal looks like.
- **Market signal:**
  - Coram raised a $35M Series B and Hakimo a $12M Series A2.
  - NVIDIA invested in Verkada, and Verkada's Catalyst MCP launched Sep 17.
  - Products that only answer questions on request are now table stakes, while push-and-verify is still open.
- **Privacy is in the news:** Texas froze state funding for Flock, Wired covered a Flock data dump, and Axon's AI police reports were shown to get facts wrong. Our "no faces, no identity, private operational spaces" framing reads as current.
- **Expected number of rival learned-normal teams today:** raised from 0–2 to **0–3**.

## Demo patterns that won video hackathons in 2026
1. A live run plus an offline replay fallback. Frigate's Debug Replay legitimises replaying stored footage through the pipeline.
2. A clip and timestamp behind every claim.
3. A model that is allowed to decline. Show the decoy being dismissed, with Cosmos's reason.
4. Cost per verdict on screen. CurbWatch showed $0.03 per verified complaint, so show our $/camera-hour.
5. A named operator receiving the handoff.
6. **Three visible lanes:** distance nominates, Cosmos verifies, a human gives 👍/👎.
7. A QR code to the digest. Stretch goal: a read-only MCP for the digest, in the same pattern as Verkada Catalyst.

Patterns to copy from open source:
- **Frigate's verdict format:** title, summary, confidence, threat 0–2, with at most 20 frames at 480p.
- **Qdrant's baseline hygiene:** escalated clips never enter "normal", plus guards against poisoning and a reported escalation rate.
- **Scrypted's** thumbnail-montage push notifications.

## What builders complain about (and our answer)
| Pain | Evidence | UNWATCHED answer |
|---|---|---|
| Cost: about 352K visual tokens per minute at 30 fps | trends/03 | Cosine scoring on CPU; Cosmos verify on ~3% at 2 fps |
| Misses fast or sub-second events | HN on Gemini Pro | 5 s segments, YOLO counts as a second signal |
| Hallucinated actions | HN, Forbes on Axon | Grounded box plus a clip citation; the verifier may decline |
| Reasoning adds latency | r/LocalLLaMA | Two-step verify: YES/NO gate first, reasoning only on YES |
| Drift after layout changes | Lumana | Time-of-day buckets, 👍/👎 feedback, escalated clips excluded |

## Open questions and gaps
- Is the VSS 3.2.1 default really "Cosmos 3 Nano Reasoner"? Check on site. NVIDIA's Cosmos 3 latency tables don't state the clip length.
- No Jul–Oct launch data was found for Spot AI, Volt, Field AI, Dyna, Reka or VideoDB. Treat them as unknown.
- Reddit and LinkedIn couldn't be scraped, so claims from them come from search snippets (marked in the reports).
