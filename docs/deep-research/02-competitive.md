# 02 — Competitors, Prior Art, Contrarian Risks for UNWATCHED

Research date: 2026-10-02 (SF build day). Raw scrapes are in `docs/sources/dr-comp-*.md|json`. Older shared scrapes were moved by another agent to `.firecrawl/` (e.g. `.firecrawl/vss-rt-alert.md`, `.firecrawl/cosmos-cookoff-winners.md`).
Source-quality tags: **[A]** primary docs, paper, or vendor documentation. **[B]** vendor marketing or blog. **[C]** forum, social media, or search snippet only.

---

## TL;DR (read this before going on stage)

1. **"No shipped product does it" is false. Do not say it.** Avigilon (Motorola) has shipped *Unusual Motion Detection* since 2018. It has "no predefined rules", "continuously learns what typical activity in a scene looks like", and flags the unusual. Lumana markets per-camera, time-of-day "normal" baselines. Google Home sends a daily **unsolicited** camera digest (Home Brief). Svid sends a daily summary email. Spot AI ships a proposer→verifier pipeline.
2. **The closest technical prior art is an open-source NVIDIA-VSS reference from March 2026.** Qdrant's *Video Anomaly Detection: Twelve Labs + NVIDIA VSS* does a kNN distance from a normal baseline, escalates to a VLM and Pegasus, and covers baseline governance (quarantine and poisoning prevention). The NVIDIA judges may have seen it.
3. **NVIDIA ships `Cosmos-Embed1-448p-anomaly-detection`, and it is now a VSS RT-Embed default.** It is *supervised* (LoRA-tuned on 24 anomaly categories from Vad-Reasoning). It does not learn a per-camera baseline. That gap is our wedge, and it's also an embedder we should try.
4. **What is still ours:** learned normal applied to **archive at rest** (a storage-triggered DataEngine function, not live-stream analytics) **+** a Cosmos-Reason2 verifier with grounded reasoning shown on screen **+** a *measured* suppression counter (Weave precision/recall, with 👍/👎 fed back into the baseline) **+** a push digest that comes with an attention budget ("41 seconds"). No single vendor we found publicly ships all four. Each piece on its own has prior art.
5. **The strongest technical attack** is a June 2026 audit paper. Frozen-embedding kNN anomaly detection averages **0.704 AUC on the same scene and 0.499 (chance) on a different scene**, with false alarms "on the order of 31,931 per hour". Our rebuttal: per-camera baselines (the paper's own recommended fix), segment-level scoring rather than frame-level, and a VLM gate.

---

## 1. Commercial products: do they learn a per-camera baseline, and do they push unsolicited summaries?

| Product | Learns per-camera/scene "normal"? | Pushes unsolicited summary/digest? | VLM verify step? | Evidence (quote) | Quality |
|---|---|---|---|---|---|
| **Avigilon / Motorola UMD + Unusual Activity Detection** | **YES.** Shipped 2017–18. Learning period: 2 weeks (UMD) / 1 week (UAD) | No. It feeds a timeline, "Focus of Attention", event search, and rule triggers | No (classic ML) | "Without any predefined rules or set up, UMD technology continuously learns what typical activity in a scene looks like, and then detects and flags unusual motion" (Motorola PR, Jun 7 2018). Docs table: "Initial Learning Period: 2 weeks, but events are reported while the device is learning". | [A] `dr-comp-avigilon-pr.md`, `dr-comp-avigilon-docs.md` |
| **Lumana (VIA-1)** | **YES** (claimed). Per camera and per time of day | Not evidenced. Real-time alerts only | Not stated. Integrates NVIDIA VSS | "The AI learns what normal activity looks like for each camera at different times of day. A crowded lobby at 9 AM is normal; the same crowd at 3 AM is not." VIA-1: "the world's first video intelligence model that enables any camera to learn from its own video data". | [B] `dr-comp-lumana-blog.md`, `dr-comp-lumana-normal.md`, `dr-comp-lumana-via1.md` |
| **Coram AI** | Claimed in press ("learn the normal behavior of the area") | Not evidenced | Agents; not specified | Business Insider snippet: "allows the camera to 'learn' the normal behavior of the area and send alerts based on unusual activity". | [C] `dr-comp-coram.json` (snippet only) |
| **Spot AI (AI Agents)** | "detect anomalies, patterns" (no explicit per-camera baseline) | "upcoming" trend synthesis | **YES: Proposer-Verifier** | "Central to AI Agents is our Proposer-Verifier framework … only verified, high-confidence events trigger alerts". | [B] `dr-comp-spotai-agents.md` |
| **Google Home / Nest (Gemini for Home)** | No | **YES: Home Brief every evening, plus AI notifications** (consumer) | VLM descriptions | "you will receive a Home Brief every evening in the Activity tab that provides an overview of what happened at home that day". Reviews are poor (see §6). | [A] `dr-comp-google-gemini-home.md` |
| **Svid AI** | No ("no training on your site") | **YES: Daily Summary email at close** | VLM describes frames | "One message at the end of the day with everything that mattered." | [B] `dr-comp-svid.md` |
| **Verkada** | Only for occlusion ("baseline reference image", about 1 day to calibrate) | No. AI search and Unified Timeline are pull | NL "AI-Powered Alerts" (prompt rules) | "Occlusion Alerts may take up to one day to calibrate as the system learns the scene and creates a baseline reference image." Activity alerts are named behaviors (fall, climb, fight). | [A] `dr-comp-verkada-occlusion.md`, `dr-comp-verkada*.json` |
| **Ambient.ai** | No. A library of "150+ verified threat signatures" (predefined) | No | Contextual AI | Press: threat signatures "reduce false alarms by 93%". | [C] `dr-comp-ambient.json` (snippets; the blog scrape was cookie-walled) |
| **Rhombus** | "Unusual behavior" plus posture | No | — | Its own guide: "treat anomaly alerts as prompts for human review because unusual behavior does not always indicate a security incident." | [C] `dr-comp-rhombus.json` |
| **Conntour** (YC, $7M seed Mar 2026) | No. Natural-language scenarios | Real-time alerts on NL queries | VLM | "supports unlimited, highly specific scenarios described in plain language". This is the *rule-by-prompt* model. | [B/C] `dr-comp-conntour.json` |
| **Volt.ai** | Marketing claims "learn normal patterns" | No. A human checks every alert | Human-in-the-loop | "a trained person checks every alert before it reaches your team". | [B] `dr-comp-volt-actuate.json` |
| **Twelve Labs** | Platform/API. Pull (search, Pegasus Q&A) | No | — | Marketing lists "anomaly detection". The actual baseline method lives in Qdrant's reference app (below). | [B] `dr-comp-twelvelabs.json` |
| **BriefCam (Milestone)** | No | No. But **"review hours of video in minutes"** via Video Synopsis | No | Owns the "8 hours in N seconds" framing (operator-pull). | [B] `dr-comp-briefcam.json` |
| Eagle Eye, Genetec, Hanwha, Axis, Kloudspot | Not evidenced. Rule-based analytics (loitering, line-cross, tamper) and NL search | No | — | EEN: "Loitering detection, Object Counting, Line crossing, Intrusion Detection, and Tampering." | [C] `dr-comp-vms-anomaly.json`, `dr-comp-kloudspot.json` |
| Actuate | Not resolved by search (only Volt results returned) | — | — | Gap. Treat as unknown. | — |

**Reference implementation (not a product, but the closest analog):** Qdrant + Twelve Labs + **NVIDIA Metropolis VSS** (blog dated Mar 15 2026; GitHub `qdrant/video-anomaly-edge`; also an AI Dev 26 SF talk). They "reframe anomaly detection as a nearest-neighbor search problem": `anomaly_score = 1 - mean(top_k_cosine_similarities)` against a normal baseline, edge triage on Jetson that "reduces cloud processing volume by ~6x while catching ~95% of true anomalies", VLM captions and incident reports from VSS, plus "baseline governance including quarantine, scrubbing, and poisoning prevention". Reported AUC: Marengo **0.9696**, EfficientNet-B0 ~0.85, CLIP ViT-B/32 **0.23** ("single-frame … fails"). [A/B, vendor-run on their own data] `dr-comp-qdrant-vad1.md`, `dr-comp-qdrant-blog.md`

**Honest read:** the *components* (learned normal, verify step, daily digest) have all shipped. The *combination* has not been publicly shipped by anyone we found: archive-at-rest triage, learned normal plus VLM verification, a measured "what we suppressed" counter, and a digest with an attention budget. The 2017 IPVM thread is telling. An integrator imagined exactly our use ("users coming in Monday morning and run a search for any unusual events for over weekend"), and IPVM's founder named the blocker: "the system alerts you to 100 'unusual' things and only 1 is real" (`dr-comp-ipvm-umd.md`, [C] but an authoritative industry forum). **That 100:1 problem is the hole UNWATCHED fills. Lead with it.**

## 2. NVIDIA's own stack: is there any baseline learning?

- **VSS Real-Time Alert Workflow:** "generates alerts when the VLM detects anomalies or specified events". Rules are created from a prompt that names a sensor and a *detection condition* ("Start real-time alert for boxes dropped on sensor warehouse_sample"). **There's no learned baseline. It's prompt-defined.** [A] `.firecrawl/vss-rt-alert.md`
- **VSS Alert Verification:** verifies alerts from an upstream CV or behavior-analytics rule, and returns `confirmed` or `rejected`. A known issue: Alert Bridge parses only raw `Yes/No` / `A/B` verdicts, so a semantically valid Cosmos "rejected" can fail in the UI. Worth knowing if we call it. [A] `.firecrawl/vss-alert-verification.md`, `.firecrawl/vss-rt-alert.md`
- **`Cosmos-Embed1-448p-anomaly-detection`** (HF, VSS 3.x RT-Embed default for the Search profile): LoRA fine-tune on the Vad-Reasoning SFT set (1,755 videos, 24 anomaly categories, 5 s chunks). Zero-shot anomaly *classification*: Top-1 hit 23.2% → **46.4%**, Top-5 46.0% → 83.7%, macro F1 19.5% → 38.9%, with Kinetics-400 top-1 falling only slightly (87.96 → 85.18). **It classifies known anomaly types. It does not model normal per camera.** [A] `dr-comp-cosmos-embed-anomaly.md`, `.firecrawl/vss-release-notes.md`
  - *Action for the build team:* try this variant as the segment embedder. It should spread anomalous segments further from a per-camera centroid than base Embed1. That's an NVIDIA-native talking point too ("your anomaly-tuned embedder, used one-class").
- **Lumana integrates the VSS blueprint** (`dr-comp-nv-anomaly.json`), so a VSS-based "learns normal" commercial story already exists in NVIDIA's partner ecosystem.

## 3. Academic numbers to pre-empt judges

| Work | Setting | Headline number | Failure mode / caveat to cite |
|---|---|---|---|
| **LAVAD** (CVPR'24) | Training-free: VLM captions → LLM scores → cross-modal cleanup | UCF-Crime AUC **80.28**, XD-Violence **85.36** (per VERA's tables) | Per-frame captions are noisy, hence the need for "cleaning noisy captions". [A] `dr-comp-lavad-abs.md` |
| **VERA** (CVPR'25) | Frozen VLM + learned guiding questions | UCF-Crime **86.55**, XD **88.26**. **A frozen VLM asked "is there any anomaly?" scores 53.05–65.03 AUC** | Naive prompting is near chance. Without guiding questions AUC drops to 78.81. → *Our verifier prompt must be specific and baseline-conditioned.* [A] `dr-comp-vera-html.md` |
| **Holmes-VAD** (2024) | Instruction-tuned MLLM on VAD-Instruct50k | UCF-Crime **84.61** (no instruction tuning, per VERA) | "existing methods often exhibit biased detection when faced with challenging or unseen events". [A] `dr-comp-holmes-abs.md` |
| **AnomalyRuler** (ECCV'24) | **One-class:** LLM induces rules from few-shot *normal* samples, then deduces | SOTA on 4 benchmarks (claimed) | **The closest academic analog to our "baseline summary in the Cosmos prompt."** An AAAI-SS follow-up says inducing rules from normal-only data "may increase false positives". Cite it as lineage, not competition. [A] `dr-comp-anomalyruler-abs.md`, `dr-comp-anomalyruler.json` |
| **"Benchmark AUC Is Not Deployable Reliability"** (arXiv 2606.29506, Jun 2026) | Frozen CLIP/DINOv2/ResNet/EffNet + kNN distance to normal | Same-scene AUC avg **0.704**, cross-scene **0.499**. Median false alarms **26,406/hr** calibrated, **31,931/hr** overall (at 0.9 recall, 10 fps, frame-level) | "it has learned the camera, not the concept of anomaly". The only fix it recommends: "test-time adaptation that updates the normal model from a short slice of the new camera's footage" (= our per-camera baseline). Caveats: an unreviewed preprint, frame-level scoring, single-frame features, grayscale UCSD. [A-, preprint] `dr-comp-auc-not-deployable.md` |
| Qdrant reference | Video-native kNN | Marengo 0.9696 vs CLIP 0.23 | Single-frame embeddings fail because anomalies live *between* frames. Cosmos-Embed1 is 8-frame and video-native, which is good. [B] |

**Field failure modes with sources:**
- **Lighting:** "even having cloud activity changing the light levels is causing false notifications" (IPVM, Hikvision) [C]. Lumana says baselines must handle "seasonal lighting shifts" and snowstorms [B].
- **Time-of-day density:** the same crowd is normal at 9 AM and anomalous at 3 AM (Lumana) [B]. *If the baseline isn't bucketed by hour-of-day, a judge will ask.*
- **Camera shake, rain, reflections, single-frame glitches:** handled with temporal smoothing (Fora Soft playbook, a vendor blog, low quality) [C]. Qdrant uses "temporal smoothing and hysteresis thresholding" [B].
- **Baseline poisoning:** a slow-onset event becomes normal. Qdrant has a whole governance section [B]. Our plan already excludes escalated segments, so say so.
- **VLM hallucination in digests:** The Verge: Nest "sometimes … tells me about things that aren't there". A Home Brief user says summaries read "like a rambling, confusing recollection of the day's events from a toddler" and "If there were legitimate security issues baked into the summary, I wouldn't realize it." [B/C] `dr-comp-verge-gemini.md`, `dr-comp-nest-summary.md`. → **Our digest must be short, ranked, and link every line to a clip with Cosmos's grounded reason. The anti-Home-Brief is the point.**

**Translate for Q&A.** Per camera, 5–10 s segments come to 360–720 segments/hr. A 3% escalation rate means 11–22 Cosmos calls per camera-hour. That's fine for the demo, but at 10k cameras it's 110k–220k VLM calls/hr. Be ready to say the threshold is a budget knob: a per-camera top-k per hour, not a fixed percentile.

## 4. Prior video-AI hackathon winners: what wins, what's overdone

- **NVIDIA Cosmos Cookoff** (1,600+ participants, 4 weeks, 1st prize DGX Spark). Winners: **Team Zenith / Doosan Robotics, "See How It Thinks"** (palletizing robot that *explains every action* with Reason2); a disaster/wildfire simulation project; **Team LiveKit, "Voice Controlled AI Video Intelligence"** (Reason2 over many live streams plus a voice Q&A interface). Placement conflicts between sources: a Ming-Yu Liu LinkedIn snippet says LiveKit was 3rd, a Facebook repost says 1st. [A transcript `.firecrawl/cosmos-cookoff-winners.md`; C for placements `dr-comp-cookoff.json`]. **Lessons:** NVIDIA rewards *visible reasoning* (CoT on screen) and multi-stream operator relief. Our Reason2 `<think>` panel lines up with both. LiveKit's "monitor many streams by asking questions" is the **pull** baseline we contrast against.
- **Twelve Labs hackathons** (Denver, LA): winners were consumer and niche-domain projects (ski-trick scoring, workout-form feedback, park advisor). Webcam-alert projects (CamSense AI) only got "notable". [B] `dr-comp-tl-denver.md`. **Lesson:** generic "AI watches webcam and alerts" doesn't place.
- **Devpost "Cameron"** ("describe what to look out for … Cameron builds the logic … takes action") and **Watchful.AI** (school-shooting detection). Prompt-rule watchers and weapon detection are overdone. [B] `dr-comp-cameron.md`, `dr-comp-video-hack.json`
- **tokens& events:** the SF gallery was empty at research time, and there's no prior VAST event to learn from (NYC is Oct 9). Other tokens& winners skew toward "real infra + agent that ships as a product" [C] `dr-judge-s-tokensand-winners.json`.

## 5. Predicted builds from the other ~25 teams (and collision risk)

The starter kit is the VAST VSS blueprint. It has 5 s segment → Cosmos caption → embed → VastDB, NL search, **"Explore mode … summarize any video on demand"**, and analysis-prompt presets for "surveillance, traffic, live_driving" (`.firecrawl/vast-vss-blueprint.md`, `.firecrawl/vast-video-intel-blog.md`). The organizer's own example is "flag someone missing a hard hat".

| Likely build | Est. teams | Collides with UNWATCHED? |
|---|---|---|
| PPE / hard-hat / forklift-safety alerting (organizer example + VSS warehouse sample) | 4–6 | Low. Ours has no rules. Useful contrast line. |
| "Chat with your footage" / NL search agent / Q&A over the archive | 5–7 | Low (pull vs push). Their demo looks like the baseline we beat. |
| Incident report or **daily/shift summary generator** (Explore + Summarize preset) | 2–4 | **HIGH on the digest.** If a team ships a "morning summary" first, ours must stand out on *suppression + attention budget + verified* rather than "summary". |
| Real-time Cosmos alert → Slack/SMS on a prompt rule (VSS RT-alert pattern) | 3–5 | **MEDIUM on the "push notification on stage" beat.** Our difference is the decoy that gets *dismissed*. |
| Traffic incident / smart-city (VAST "When the City Thinks" blog) | 2–3 | Low |
| Retail loss / loitering / shoplifting | 1–3 | Low–medium ("unusual" language) |
| Fall / medical-emergency detection | 1–2 | Low |
| **Embedding-outlier / "anomaly" scoring** (Cosmos-Embed1 is in the kit; the anomaly-tuned variant is a VSS default) | 0–2 | **HIGH if it happens.** Survival depends on per-camera baseline, Cosmos verification, and a measured suppression precision. |
| Robotics / AV sim (Cosmos Cookoff-style) | 1–2 | None |

## 6. Contrarian case: the strongest judge attacks and best rebuttals

1. **"Avigilon shipped learned-normal in 2018. What's new?"** (any VAST or NVIDIA product judge)
   *Rebuttal:* "Right. Learned-normal is proven. What killed it was the ratio IPVM described in 2017: 100 'unusual' alerts for 1 real one. The new part is a reasoning VLM that checks every outlier against what that camera normally sees before anyone is paged. And we *measure* the suppression: here's precision and recall in Weave."
2. **"This is the Qdrant/Twelve Labs VSS anomaly demo."** (Hassan or Adam might know it)
   *Rebuttal:* "Same core idea, kNN from normal, which is why it's credible. They triage live edge streams. We triage the *archive at rest*: a DataEngine function fires when a segment lands in VAST, the baseline and verdicts live in VastDB next to the video, and the output is a ranked digest with a suppression ledger rather than an alert stream."
3. **"Embedding distance measures novelty, not threat. A new delivery van is novel."**
   *Rebuttal:* "Agreed, which is why distance only *nominates* and never alerts. Cosmos decides, and the walk-by decoy proves it on stage. The distance stage is tuned for recall (the 1% random audit measures misses), and the VLM stage is tuned for precision." VERA supports this: a frozen VLM alone scores 53–65 AUC with naive prompts, so the *combination* and a baseline-conditioned prompt are what matter.
4. **"Frozen-embedding kNN is at chance across scenes (0.499 AUC, 30k false alarms/hr)."** (the most technical judge)
   *Rebuttal:* "That audit trains on one scene and tests on another. We never do that: each camera gets its own baseline, which is the fix the paper itself recommends. It also scores single frames at 10 fps. We score 8-frame video embeddings per segment, and video-native embeddings beat single-frame ones by a wide margin (Qdrant: 0.97 vs 0.23 AUC)." Don't overclaim. Same-scene AUC was only ~0.70 in that audit, so the verifier really is necessary.
5. **"How does the baseline handle lighting, night/day, shift changes?"**
   *Rebuttal:* hour-of-day buckets per camera (if implemented; if not, say "next" and don't bluff), a rolling 15-minute recompute, and escalated segments excluded so incidents can't be absorbed into normal. 👎 is the only way a flagged pattern becomes normal.
6. **"Your digest will hallucinate, like Google Home Brief."**
   *Rebuttal:* every digest line is a verified clip with a timestamp and Cosmos's grounded reason. No line exists without a clip, and the digest is capped (3 items / 41 s).
7. **"3% to the GPU still means ~20 VLM calls per camera-hour. 10k cameras is ~200k calls/hr."** (CoreWeave SA)
   *Rebuttal:* the escalation budget is per camera per hour (top-k), not a percentile. The cost meter shows dollars per camera-hour, and the 2B model plus keyframe sampling is a fallback tier.
8. **Privacy / surveillance ethics.** The ACLU explicitly names this design: "If video analytics operates by establishing normal patterns of movement in a public space and drawing attention to anything 'out of the norm,' that could pressure Americans to conform" (`dr-comp-aclu-analytics.md`, [A] advocacy primary). The EU AI Act Art. 5 bans emotion recognition in workplaces and schools (`dr-comp-euaiact.json`, [B]).
   *Rebuttal / design stance:* no face recognition, no identity, no emotion inference. It ranks *events* in *private operational spaces* (warehouses, loading docks, server rooms) the operator already records. Keep a retention-neutral audit trail of why something was flagged or suppressed (the VastDB verdicts, plus snapshots as a stretch). Don't pitch public spaces, schools, or "suspicious people". Pitch "spills, propped doors, equipment left out, after-hours activity in a closed area".
9. **"Who buys this over Verkada/Lumana, who already claim 'learns normal'?"**
   *Rebuttal:* it's VMS-agnostic and storage-native. It sits on the archive the customer already keeps in VAST, so it adds value to footage they already pay to store, with no rip-and-replace. Lumana and Avigilon lock it to their own VMS or cameras.

## Differentiation verdict

**Does the claim hold?** *"No shipped product does it" does NOT hold* and would be caught by any VAST, NVIDIA, or industry judge (Avigilon UMD since 2018; Lumana per-camera baselines; Google Home Brief unsolicited digests; Spot AI proposer→verifier; the Qdrant + NVIDIA VSS kNN reference). **The narrower claim does hold** on everything we could find: *no public product combines learned per-camera normal, VLM verification of every outlier, a measured suppression ledger, and a push digest over archived footage at rest.* The defensible novelty is the **verify-and-measure layer on top of a known detection idea**, plus **archive-native execution in VAST**.

**Safe wording to use on stage (use verbatim):**
> "Cameras that learn what's normal aren't new. Avigilon shipped that in 2018. They never took off because for every real event they flagged a hundred harmless ones. UNWATCHED adds the missing step. Every outlier gets checked by Cosmos-Reason2 against what *that* camera normally sees, nobody gets paged until it passes, and we count and measure everything we chose not to show you. It runs on the archive itself, inside VAST, so footage nobody watched now sends you its own morning briefing."

**Words to avoid:** "first", "no one does this", "detects threats", "suspicious people", "anomaly detection" as the headline. Use "attention triage", "learned normal", "verified", "suppressed".
**Say it before they do:** credit AnomalyRuler/LAVAD/VERA as academic lineage and the Qdrant + VSS reference as "the same core math, live-stream edition".

## Likely collisions

1. **Daily/shift summary teams (2–4)** built on the kit's "Summarize Video". *Defense:* our digest is *selective and verified* (3 items, 41 s, with a suppressed count). Theirs summarizes everything (the Home Brief failure mode).
2. **Prompt-rule real-time alert → Slack teams (3–5).** *Defense:* the live decoy-vs-real beat, where the same YOLO trigger gets one dismissed and one escalated. A rule-based system fires on both.
3. **An embedding-anomaly team (0–2)**, possibly using `Cosmos-Embed1-448p-anomaly-detection` zero-shot. *Defense:* theirs classifies *known* anomaly types globally. Ours models *this camera's* normal and shows Weave precision/recall for suppression.
4. **PPE/hard-hat teams (4–6).** No collision. Use them as contrast: "they wrote a rule, we didn't."
5. **NL search / chat-with-footage (5–7).** No collision. They're pull, we're push.

## Source list (39 scraped or searched here, plus shared sources)
Scrapes: `dr-comp-avigilon-docs.md`, `-avigilon-pr.md`, `-lumana-blog.md`, `-lumana-normal.md`, `-lumana-via1.md`, `-spotai-agents.md`, `-nest-summary.md`, `-svid.md`, `-google-gemini-home.md`, `-verge-gemini.md`, `-cosmos-embed-anomaly.md`, `-qdrant-vad1.md`, `-qdrant-blog.md`, `-lavad-abs.md`, `-anomalyruler-abs.md`, `-vera-html.md`, `-holmes-abs.md`, `-auc-not-deployable.md`, `-tl-denver.md`, `-cameron.md`, `-aclu-analytics.md`, `-ipvm-umd.md`, `-verkada-occlusion.md`, `-ambient-sig.md` (cookie wall, little content).
Searches (JSON): verkada, verkada-ai, coram, coram2, spotai, ambient, avigilon, lumana, lumana-via, rhombus, digest, googlebrief, conntour, volt-actuate, vms-anomaly, briefcam, twelvelabs, kloudspot, nv-anomaly, damiba, lavad, vera, anomalyruler, holmes, vad-critique, vad-failure, tl-hack, video-hack, cookoff, aclu, euaiact, ipvm-umd, cookbook-anomaly, contrarian-novelty, vendor-reports.
Shared (`.firecrawl/`): `vss-rt-alert.md`, `vss-alert-verification.md`, `vss-release-notes.md`, `cosmos-cookoff-winners.md`, `vast-vss-blueprint.md`, `vast-video-intel-blog.md`.
Gaps: Actuate wasn't resolved. Coram's "learns normal" rests on a press snippet only. Ambient's details are snippets only. Cookoff placements conflict between sources.
