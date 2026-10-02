# What we restored from unwanted/ and what to use it for

A second pass on 2026-10-02 asked of every file in `unwanted/`: *can it help make the project?* Three teams reviewed 616 non-junk files (101 empty or error captures were skipped) and restored **85** to their original paths. **632** stay in `unwanted/`; [MANIFEST.tsv](../unwanted/MANIFEST.tsv) gives the reason for each.

## Highest-value rescues
1. **`docs/sources/dr-gem-cmp-p17-sveta-field-notes.md`:** prompts that *assert* an event make VLMs see it (sycophancy). Keep verify prompts neutral and claim-agnostic. ⚠️ `src/verifier_backends.py:build_prompt()` still says *"A statistical baseline flagged this clip as unusual"*; rewrite it for the chosen project.
2. **`docs/deep-research/05-gemini-vs-cosmos.md`:** VANTAGE table (Reason2-8B specificity 57.6); class-specific prompts raise F1 from 0.09 to 0.64; few-shot raised the false-positive rate from 21.7% to 68.7%; CoT lowered F1 and added latency; latency rules for the G1 gate.
3. **`docs/deep-research/06-gemini-integration.md` + `docs/sources/dr-gem-int-p25-discuss-404-noaudio.md`:** Gemini fallback setup. Gemini 3 returns 404 on mp4s with no audio track, so add a silent track. SDK retries are off by default. Weave doesn't trace `interactions.create` automatically. google-genai needs a newer pydantic than the blueprint pins.
4. **`docs/FINAL-IDEA.md` (UNWATCHED, superseded):** reuse §5 verify-prompt skeleton and JSON schema, §5 Weave eval design, §6 cost meter, §10 latency hiding, §11 Q&A 3–5, and banner corrections 3/4/8/10. NIGHTSHIFT: correction 1 (prior art), correction 9 (privacy), and the digest rule "never mention an event not in the input".
5. **`docs/sources/dr-gem-cmp-r-arxiv-2603.25467.md` (GridVAD):** self-consistency (5 samples, keep answers that appear ≥3 times) removes hallucinated confirms; a 3×3 frame grid works for the keyframe degrade path.
6. **`.firecrawl/trend-models-p31-compact-vlm-vad.md` + `.firecrawl/trend-oss-frigate-genai-review.md`:** four prompt styles as the tuning agent's starting set; Frigate's "ALWAYS level X if…" rule-style prompt and 480p frame budget.
7. **`docs/sources/dr-comp-vera-html.md`:** VERA learns its guiding questions from labeled data, which is precedent for our tuning agent. A naive "any anomaly?" prompt scores only ~53–65 AUC.
8. **`docs/sources/dr-comp-auc-not-deployable.md` + `docs/sources/dr-gem-cmp-p12-ars-gemini-home.md`:** benchmarks don't transfer across scenes (~32k false alarms/hour), and Google's camera VLM reported people in empty rooms. That's the case for "measured, not claimed" and for negative controls.
9. **`.firecrawl/starter-repos/virtualsheng-team-a/safety-board/static/index.html`:** a working dry-run UI (dark VSS palette, YOLO boxes synced to video, before/event/after lightbox). Restoring it also fixes the kept `app.py`, which serves it.
10. **`.firecrawl/trend-mkt-p16-aitinkerers-nyc.md`:** a winning demo pattern: replay-mode fallback, $ per verdict on screen, downloadable JSONL trace.

⚠️ Four USE rows rest only on search snippets, so verify them before saying them on stage: `dr-comp-conntour`, `dr-comp-cookbook-anomaly` (Encord), `dr-gem-cmp-s04` (ARGUS/VideoHallu), `dr-tech-s1`.

## Every restored file, by component

### Verify (prompts, parsing, latency) (24)
| File | Use it for |
|---|---|
| `.firecrawl/ava-paper.md` | recall/verify: App. A.3 Listing 3 traffic prompt (pedestrians waiting/crossing) as template for scenario-specific re-ingest prompt |
| `.firecrawl/trend-mkt-p41-qwen38-omni.md` | Q&A 4 scale/cost: VLM-on-everything ≈ $0.20/min of 720p video → justifies recall-wide, verify-narrow candidate gating |
| `.firecrawl/trend-models-p04-cosmos-github.md` | verify.py + Q&A: Cosmos3 Reasoner prompt guide, dashcam hazard demo, Cosmos Curator/Evaluator comparables for Hassan |
| `.firecrawl/trend-models-p07-cosmos-embed-ad.md` | recall.py stretch: Cosmos-Embed1 variants/dims (224p=256, 448p=768), 8 frames 1-2 fps, text→video shared space |
| `.firecrawl/trend-models-p14-simplestream.md` | verify.py degrade path: SimpleStream shows 4 recent frames match complex video stacks; 2/4/8/16-frame ablation table |
| `.firecrawl/trend-models-p17-efficient-video-2026.md` | verify.py gating: VideoAuto-R1 direct answer ≈ CoT at far fewer tokens; 352K tokens/min math for cost Q&A 4 |
| `.firecrawl/trend-models-p31-compact-vlm-vad.md` | verify prompts + tune.py: CCTV study compares instruction/zero-shot/few-shot/CoT prompts, binary 0/1 output, prompt sensitivity |
| `.firecrawl/trend-oss-frigate-genai-review.md` | verify prompt: explicit decision-rule template, confidence field, 480p frame budget; §13 prior art for VLM-reviewed street cams |
| `.firecrawl/trend-oss-sv-zones.md` | verify.py stretch in_ego_path: supervision PolygonZone API (BOTTOM_CENTER anchor) over YOLO_URL person boxes |
| `.firecrawl/trend-oss-trackers.md` | verify.py stretch: ByteTrackTracker.update(sv.Detections) snippet, Apache-2.0 → link YOLO_URL per-frame boxes into tracks |
| `docs/deep-research/05-gemini-vs-cosmos.md` | tune/verify: class-specific prompts F1 0.09->0.64, CoT/few-shot raise FPs; VANTAGE specificity Q&A; latency table for G1 |
| `docs/demo-designer-round1.md` | UI live panel: stream Cosmos reasoning + stage chip strip to hide verify latency; search-box+clip-cards looks like starter kit |
| `docs/sources/dr-comp-cookbook-anomaly.json` | pitch Market comparable: Encord integrates Cosmos Reason+Embed for data curation (snippet; verify tonight) |
| `docs/sources/dr-comp-cosmos-embed-anomaly.md` | recall.py Embed1 stretch: T2V text <=128 tokens, short action phrases; 256 vs 768 dims; 8 frames; check indexed variant |
| `docs/sources/dr-comp-lavad-abs.md` | Q&A: LAVAD needs cleaning of noisy per-frame VLM captions -> caption-grep baseline row (c) is weak without verify |
| `docs/sources/dr-comp-vera-html.md` | tune.py + Q&A: VERA learns verify questions from labeled data (=our tuner); naive frozen-VLM prompt ~53-65 AUC |
| `docs/sources/dr-gem-cmp-p07-pmc-compact-vlm.md` | verify prompt: CoT/few-shot lowered F1 0.818->0.684 and raised latency -> A/B CoT on/off in Weave |
| `docs/sources/dr-gem-cmp-p17-sveta-field-notes.md` | verify/tune prompt: MLLMs "see" what prompt asserts -> never tell Cosmos search thinks it is a crossing |
| `docs/sources/dr-gem-cmp-r-arxiv-2603.25467.md` | verify.py: self-consistency (5 samples, keep >=3) cuts hallucinated confirms; 3x3 frame grid for keyframe degrade |
| `docs/sources/dr-gem-cmp-r01-temporal.md` | verify prompt: VLMs confidently wrong on timestamps, yes/no probing works -> per-segment yes/no with tau |
| `docs/sources/dr-gem-docs-api-generate.md` | verify.py generate_content path: VideoMetadata fps (0,24], MediaResolution, responseJsonSchema, finishReason fields |
| `docs/sources/dr-gem-int-p05-gc-structured.md` | verify.py generate_content path: response_json_schema subset for the verdict JSON |
| `docs/sources/dr-gem-int-p09-datature-cr2.md` | verify.py Cosmos parsing: <think>/<answer> output patterns, FPS=4, enough max_tokens (Reason2 family) |
| `docs/sources/dr-tech-s1-cosmos-reason2-api.json` | verify.py: pointer to Cosmos3 Reasoner NIM cookbook; pitch: Uber+NVIDIA post-train Reason2 for AV captions |

### Tune (agent / Weave eval) (4)
| File | Use it for |
|---|---|
| `.firecrawl/trend-mkt-p32-nvidia-vision-agent-omni.md` | §7b Future/Hassan: Metropolis Video Data Augmentation/SDG skills expand scenario coverage; Gartner "90% of edge data unprocessed" |
| `.firecrawl/trend-mkt-s11-nvidia-metropolis.json` | Judge vocabulary: NVIDIA CVPR AV agent skills, VSS + Video Augmentation "automate the build-and-evaluate loop" → tune.py framing |
| `.firecrawl/trend-models-p19-mixpeek-embed.md` | recall eval + Q&A: open video-embedding benchmark harness (NDCG/Recall); best text→video NDCG 0.76 → search alone misses |
| `docs/sources/dr-gem-cmp-s04-gemini-cctv-hallucination.json` | Q&A: pointers to ARGUS (hallucination+omission) and VideoHallu (positive-control-only evals) -> backs VOID control |

### Recall (search / embeddings) (6)
| File | Use it for |
|---|---|
| `.firecrawl/trend-mkt-p02-twelvelabs-seriesb.md` | §7b Market: TwelveLabs $100M for video search (Amazon, Bedrock) → search is funded/commoditized; nobody measures misses |
| `.firecrawl/trend-mkt-p05-verkada-nvidia.md` | §7b Market/Hassan: Verkada cites 68% search-mAP gain via Cosmos + Physical AI Data Factory → NVIDIA touts measured search |
| `.firecrawl/trend-mkt-p27-forasoft-vms.md` | §7b precision SLA line: vendor accuracy is "vendor-reported, not independent benchmarks"; precision/recall must be verified per scene |
| `docs/sources/dr-comp-conntour.json` | pitch Market/Q&A: plain-English camera scenario search raised $7M (GC/YC) yet reports no error bars |
| `docs/sources/dr-comp-spotai-agents.md` | Q&A 1: Spot AI ships proposer->verifier gating; ASSAY adds measured precision/recall and a negative control |
| `docs/sources/dr-gem-cmp-p30-hn-sentry.md` | Q&A/Market: SentrySearch does NL dashcam search ("green car cutting me off") ~$2.50/hr, no error bars |

### UI / demo (3)
| File | Use it for |
|---|---|
| `.firecrawl/starter-repos/official-vast-data/docs/hackathon/vss-search-tab.png` | pitch §2 baseline slide: clean stock-search UI screenshot (kept vss-search.png carries a tutorial arrow) |
| `.firecrawl/starter-repos/virtualsheng-team-a/safety-board/static/index.html` | UI: kept app.py serves it; drawYolo video-synced box overlay, before/event/after lightbox, threshold ladder for card stream |
| `.firecrawl/trend-mkt-p17-neo4j-video-hack.md` | §7 demo/pitch: 2026 winners "refuses to guess", "models never grade", timecoded provenance → matches "measured, not claimed" |

### Pitch / Q&A (5)
| File | Use it for |
|---|---|
| `.firecrawl/trend-mkt-p21-forbes-axon.md` | §7b Problem/Q&A: Axon AI reports get facts wrong across 600k reports → unmeasured AI output fails; motivates measured precision |
| `.firecrawl/trend-mkt-p22-latent-video-agents.md` | Q&A 5 why VAST: ex-Cosmos lead says storing/moving video datasets is costly, egress > storage → mine in place |
| `.firecrawl/trend-mkt-s31-physical-ai-fund.json` | §7b Market: physical-AI data rounds (Mecka ~$500M val, Ropedia $30M) → capital chasing curated real-world video data |
| `.firecrawl/trend-oss-artesca-vss.md` | Q&A 5 why VAST: Scality ships a VSS console beside ARTESCA; ASSAY answers with pushdown slice + VastDB table |
| `docs/sources/dr-comp-verge-gemini.md` | pitch "made up": Verge says Google camera VLM reports "things that aren't there" -> measured, not claimed |

### Fallback (Gemini outage path) (26)
| File | Use it for |
|---|---|
| `.firecrawl/trend-mkt-p16-aitinkerers-nyc.md` | §7/§11 demo: CurbWatch replay-mode fallback, $0.03 per verdict, JSONL trace, timeline replay; §13 Anomaly Congestion prior art |
| `.firecrawl/trend-mkt-p36-hn-gpt56-vision.md` | Q&A/Problem: HN builders report VLMs hallucinating actions, Gemini Pro blind sub-second → why verify output must be scored |
| `.firecrawl/vast-research-agent.md` | fallback Q&A: VAST's own blueprint ships MODEL_PROVIDER=nvidia/gemini/vertex, precedent for env-switched Gemini fallback |
| `docs/deep-research/04-gemini-docs.md` | fallback verify.py: Interactions video request, JSON-schema subset, box_2d yxyx order, thinking levels, spend-cap 429s, store=False |
| `docs/deep-research/06-gemini-integration.md` | fallback: no-audio mp4 404 fix, SDK retries off, Weave misses interactions.create, breaker rules, REST body, pydantic pin |
| `docs/sources/dr-gem-cmp-p12-ars-gemini-home.md` | pitch/Q&A "made up": Gemini saw a person in empty rooms; Google cites "inferential mistakes" -> VOID wall |
| `docs/sources/dr-gem-cmp-p18-gemini-safety.md` | fallback: filters off by default; treat SAFETY/empty output as no-verdict, never as rejected |
| `docs/sources/dr-gem-cmp-p19-prohibited-use.md` | fallback + pivot privacy: policy bans monitoring people without consent -> ask activity, never identity |
| `docs/sources/dr-gem-cmp-r-arxiv-2605.01512.md` | verify/fallback: two-pass crop-around-box recheck on 5 s traffic clips; 17% API failures needed a fallback |
| `docs/sources/dr-gem-docs-api-interactions.md` | verify.py fallback: exact Interactions VideoContent processing/resolution/store/response_format schema |
| `docs/sources/dr-gem-docs-gc-video.md` | verify.py generate_content fallback: inline_data + VideoMetadata fps request shape (legacy path in code) |
| `docs/sources/dr-gem-docs-image.md` | verify.py/UI cards: Gemini box_2d [ymin,xmin,ymax,xmax] 0-1000 -> pixel conversion for bbox burn-in |
| `docs/sources/dr-gem-docs-m-35flashlite.md` | fallback default model page (gemini-3.5-flash-lite): video input, minimal thinking default, limits |
| `docs/sources/dr-gem-docs-m-38flash.md` | fallback alternate model: minimal thinking errors (code forces low); capabilities |
| `docs/sources/dr-gem-docs-media-res.md` | fallback cost/latency: 70 vs 280 tokens/frame; HIGH only for the no-audio path |
| `docs/sources/dr-gem-docs-pricing.md` | cost meter: per-token prices for fallback calls (3.5 Flash-Lite $0.30/$2.50; 3.8 promo to Dec 31) |
| `docs/sources/dr-gem-docs-pypi-genai.md` | verify.py: google-genai SDK client, HttpOptions/retry options, interactions usage reference |
| `docs/sources/dr-gem-docs-rate-limits.md` | fallback ops: per-project limits, Tier-1 $10/10-min spend cap returns 429; check AI Studio pre-demo |
| `docs/sources/dr-gem-docs-terms.md` | fallback data policy: free tier trains and human-reviews -> billed key, store=False for PIE/I-24 people |
| `docs/sources/dr-gem-docs-thinking.md` | verify.py fallback: thinking levels, 3.8 rejects minimal, max_output_tokens includes thought tokens |
| `docs/sources/dr-gem-docs-tokens.md` | cost meter: count_tokens and usage fields to price any fallback calls honestly |
| `docs/sources/dr-gem-int-p02-weave-google.md` | Weave: autopatch covers generate_content only; interactions path needs @weave.op for fallback traces |
| `docs/sources/dr-gem-int-p07-troubleshooting.md` | retry/backoff: retry only 429/408/5xx with jitter; safety-block and blocked-key handling |
| `docs/sources/dr-gem-int-p17-api-errors.md` | breaker/retry: Gemini error taxonomy (400/403 no-retry; 429/503/504 retry; 404 model_not_found) |
| `docs/sources/dr-gem-int-p25-discuss-404-noaudio.md` | verify.py fallback: Gemini 3 404s on mp4 without audio unless HIGH -> 480p ffmpeg must keep/add audio |
| `docs/trends/03-products-startups-buzz.md` | pitch: 2026 winning-demo patterns (model may decline, cost/verdict, replay fallback), hallucination receipts; NIGHTSHIFT words to avoid |

### Pivot (NIGHTSHIFT) (17)
| File | Use it for |
|---|---|
| `.firecrawl/trend-mkt-p06-orchestra.md` | §13 pivot privacy: Flock backlash (50 cities cancelled), "God-mode"/"search engine for physical world" words to avoid; AV buyers street data |
| `.firecrawl/trend-mkt-p11-lumana-tnw.md` | §13 pivot prior art: Lumana VIA-1 learns per-camera normal, 50k cams → NIGHTSHIFT must say "two-day diff", not anomaly detection |
| `.firecrawl/trend-oss-qdrant-vae-gh.md` | §13 pivot prior art (embedding outlier→VLM); evaluate.py reports recall/precision/AUC/escalation rate → score.py + cost meter |
| `.firecrawl/trend-oss-qdrant-vae-p1.md` | §13 pivot prior art + Q&A: single-frame CLIP 0.23 AUC vs temporal 0.97 → verify on clips, not single keyframes |
| `docs/FINAL-IDEA.md` | verify: <think>+JSON prompt, 'passing through is not an event' clause; Weave model×prompt leaderboard; cost meter; NIGHTSHIFT baseline/digest prompts |
| `docs/deep-research/02-competitive.md` | pivot: NIGHTSHIFT prior art (Avigilon/Lumana/Qdrant/Spot AI), words to avoid, ACLU rebuttal; Q&A: VERA naive-prompt AUC 53-65 |
| `docs/sources/dr-comp-auc-not-deployable.md` | pitch/Q&A + pivot: benchmark AUC fails cross-scene (0.499, ~31,931 FA/hr) -> measure on own footage, negative control |
| `docs/sources/dr-comp-avigilon-docs.md` | pivot Q&A: shipped learned-normal needs 2-week learning period; NIGHTSHIFT has n=1, so call it a literal diff |
| `docs/sources/dr-comp-avigilon-pr.md` | pivot prior-art receipt: Avigilon UMD learned-normal shipped 2018 -> never say "first" or "anomaly detection" |
| `docs/sources/dr-comp-ipvm-umd.md` | pivot + pitch: IPVM "100 unusual alerts, 1 real" -> NIGHTSHIFT surfaces only Cosmos-verified diffs |
| `docs/sources/dr-comp-lumana-normal.md` | pivot prior art: baselines by time-of-day/day-of-week; frame NIGHTSHIFT as literal two-day diff, not learned normal |
| `docs/sources/dr-comp-qdrant-blog.md` | pivot Q&A: closest prior art (kNN-from-normal + VSS); single-frame CLIP 0.23 AUC vs video-native 0.97 |
| `docs/sources/dr-comp-qdrant-vad1.md` | pivot Q&A: Qdrant+Twelve Labs+NVIDIA VSS reference judges may know; edge triage ~6x then VLM escalation |
| `docs/sources/dr-gem-cmp-p06-surveillance-vllm.md` | verify/tune: few-shot raised FP rate 21.7->68.7%; face blur adds FPs -> blur screenshots only (pivot) |
| `docs/sources/dr-judge-mkt-ipvm-unwatched.md` | pivot Market beat: IPVM estimates <1% of recorded surveillance video is watched live |
| `docs/sources/dr-judge-mkt-omdia.md` | pivot Market beat: Omdia $27B video-surveillance market 2025, software share rising |
| `docs/trends/02-trending-oss.md` | pivot prior-art matrix (Qdrant/Frigate); verify-frame dedup; supervision PolygonZone ego corridor; Scality VSS console intel |
