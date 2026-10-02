# 05: Gemini vs Cosmos-Reason2 / Cosmos 3 Nano as the UNWATCHED verifier

Researched 2026-10-02 (exhaustive tier). 30 searches and 4 paper-index reads. Raw captures are in `docs/sources/dr-gem-cmp-*` (32 page scrapes plus search JSON).

**The question:** a 5-second CCTV segment was flagged by the embedding-distance baseline. Should Cosmos or Gemini decide whether it is a real event (for example, equipment removed after hours) or something benign?

**How to read this document:**
- **[P]** means a primary source (paper, model card, official docs).
- **[V]** means a vendor-affiliated benchmark or claim.
- **[R]** means a practitioner or press report.
- **[S]** means a search snippet only; the page was not scraped. Reddit blocks scraping, so all Reddit items are snippets.

**Related reports:** `04-gemini-docs.md` has the API facts (models, pricing, parameters). `06-gemini-integration.md` has the fallback code. This report covers evidence, benchmarks and risk only.

---

## TL;DR

1. **On fixed-camera footage, which is our domain, Gemini 3.6 Flash beats every Cosmos model zero-shot. The benchmark showing this is NVIDIA's own.**
   - **VANTAGE-Bench** (NVIDIA + Clemson, arXiv 2609.09396, Sep 2026; featured in Jensen's Computex keynote). Overall scores: Gemini 3.6 Flash **69.52**, Cosmos3-Super 63.62, Cosmos3-Nano 60.67, Cosmos-Reason2-8B **54.46**.
   - **Event Verification**, the task closest to ours, by macro F1: Gemini 3.6 Flash **82.00**, Cosmos3-Nano 68.88, Cosmos-Reason2-8B **64.09**.
2. **Cosmos-Reason2-8B is biased toward saying yes.** On VANTAGE event verification it accepted **42% of events that never happened** (specificity 57.63, sensitivity 71.15). Gemini 3.6 Flash rejected 76% of false events (specificity 76.27, sensitivity 87.50). [P/V] UNWATCHED's verifier exists to *reject* false outliers, so this is the most important number in this report. Two caveats: the sample is small (n=163), and **we must measure this on our own clips**.
3. **Cosmos still wins in places:**
   - **2D object localisation:** Cosmos-Reason2-8B 83.88 and Cosmos3-Super 86.97, vs Gemini 3.6 Flash 81.57.
   - **Temporal localisation** is roughly tied at the top (51.9 vs 51.5). Gemini 3.5 Flash-Lite scores **24.0** here, which is bad, so don't trust Flash-Lite timestamps.
   - **Physical-AI domains:** NVIDIA's model card shows Reason2-8B far ahead of its own Qwen3-VL-8B base on warehouse questions (69.96 vs 42.66). [V]
   - **Latency on local GPUs:** NVIDIA reports alert verification at about 0.84–1.0 s on an RTX PRO 6000. [V]
4. **Gemini zero-shot anomaly detection on CCTV is conservative, not trigger-happy.** On ShanghaiTech and CHAD, Gemini 2.5 Flash-Lite had **high precision (about 85–100%) and recall that collapsed to 1–6%** with a generic "is this anomalous?" prompt. Class-specific instructions raised peak F1 from 0.09 to 0.64. [P] For a *verify* step this bias is mostly what we want, provided the prompt names the event class ("equipment/asset removed").
5. **Consumer Gemini on real home cameras hallucinates people and animals.** Ars Technica reported a dog called a "deer" and empty rooms reported as containing "a person", and Google acknowledged "inferential mistakes". Android Authority reported invented names ("Michael was seen taking out the trash"). [R] These are a different product and prompt from ours, but the same failure class. Never let Gemini name people.
6. **Latency is the operational risk for Gemini, not accuracy.**
   - Artificial Analysis measures about **8.8 s to first answer token** for 3.5 Flash-Lite at 10k input tokens. [V]
   - Practitioners report **5–10 s typical, with occasional 2-minute** responses on the same video, and Files API `PROCESSING` stalls of 2–25 minutes during regressions. [R]
   - Fixes: send inline bytes (no Files API), use static mode, set thinking to minimal or low, use a hard timeout.
7. **Privacy and judging:**
   - The free tier lets Google use inputs and lets **human reviewers read them**, and it says "do not submit … personal information". [P] Use a paid key, or don't send real people's footage.
   - Google's Prohibited Use Policy bans uses that "track or monitor people without their consent". [P] Frame UNWATCHED as monitoring assets and areas, with no identification.
   - At an NVIDIA/VAST/CoreWeave event, present Gemini **only** as an outage fallback and as an A/B arm in Weave. Never present it as the brain.

---

## 1. Benchmarks: who wins where

### 1.1 VANTAGE-Bench: fixed infrastructure cameras (the most relevant benchmark found)

Source: arXiv 2609.09396 (`dr-gem-cmp-p21-vantage-arxiv.md`) and leaderboard vantage-bench.org (`dr-gem-cmp-p22-vantage-site.md`).
- **Quality:** [P], but **NVIDIA-authored** (correspondence zbhat@nvidia.com). That cuts in our favour: Gemini winning on NVIDIA's own benchmark is not partisan evidence.
- **Setup:** zero-shot, 17 models, warehouse, transportation and smart-spaces footage.

| Model | Overall | Event Verif. (macro F1) | VQA | Obj Loc | Temporal Loc (mIoU) | Tracking |
|---|---|---|---|---|---|---|
| **Gemini 3.6 Flash** | **69.52** | **82.00** | **76.82** | 81.57 | 51.50 | **75.99** |
| Cosmos3-Super 64B | 63.62 | 71.28 | 69.46 | **86.97** | **51.90** | 64.66 |
| Gemini 3.1 Pro | 62.66 | 68.57 | 71.46 | 77.21 | 45.69 | 67.88 |
| Cosmos3-Nano 16B ("Reason 3 Nano") | 60.67 | 68.88 | 68.95 | 74.11 | 48.04 | 59.21 |
| Qwen3-VL-32B | 55.38 | 60.04 | 71.30 | 72.67 | 46.80 | 44.19 |
| **Cosmos-Reason2-8B** | 54.46 | 64.09 | 67.95 | 83.88 | 47.30 | 37.69 |
| Gemini 3.5 Flash-Lite | 53.25 | 70.41 | 65.61 | 65.73 | **24.00** | 55.77 |
| Gemini 3.1 Flash-Lite | 52.61 | 63.78 | 68.03 | 71.74 | 37.72 | 46.68 |
| Qwen3-VL-8B (Reason2's base) | 50.07 | 59.39 | 66.44 | 59.93 | 44.32 | 33.12 |
| Cosmos-Reason2-2B | 45.94 | 55.27 | 64.69 | 73.56 | 38.95 | 26.85 |

Event Verification broken down (Table 7; n=163, of which 104 are true events and 59 are not):

| Model | Macro F1 | Sensitivity (true events caught) | Specificity (false events rejected) |
|---|---|---|---|
| Gemini 3.6 Flash | 82.00 | 87.50 | 76.27 |
| GPT-5.6 Sol | 76.14 | 77.88 | 76.27 |
| Cosmos-Reason2-32B | 73.58 | 83.65 | 62.71 |
| Cosmos3-Super | 71.28 | 72.12 | 72.88 |
| Gemini 3.1 Pro | 68.57 | 71.15 | 67.80 |
| Cosmos-Reason2-8B | 64.09 | 71.15 | **57.63** |
| Qwen3-VL-8B | 59.39 | 50.96 | 74.58 |

The authors' own reading: Cosmos-Reason2-8B is "accepting events that did not occur", while Qwen3-VL-8B is conservative.

Other findings:
- **Gap from consumer benchmarks:** event verification, referring expressions and temporal localisation all drop **9–24 points** on fixed-camera footage compared with the same models' published scores on consumer benchmarks.
- **Temporal grounding is unsolved:** no model exceeds **55.7 mIoU** on temporal localisation. Qwen3-VL-32B falls from 61.2 mIoU on Charades-STA to 46.8 here.
- **Physical-AI training helps unevenly:** going from Qwen3-VL-8B to Cosmos-Reason2-8B to Cosmos3-Nano adds +26.1 tracking, +14.2 object localisation and +9.5 event verification, but only +3.7 temporal localisation.

**What this means for us.** Our verifier's job is to reduce false positives, so *specificity* is the metric that matters.
- On this benchmark, a Reason2-8B verify gate would let through about 42% of false candidates. Gemini 3.6 Flash would let through about 24%.
- The usual demo setting is Cosmos3-Nano (VSS 3.2.1+ default). Its macro F1 is 68.88. Specificity is not published in Table 7.
- **Action:** run all three backends on our ~60 hand-labelled clips in Weave and report specificity as its own number.

### 1.2 NVIDIA's own Cosmos-Reason2 card (model vs its base) [V]

Source: `dr-gem-cmp-p01-reason2-hf.md` (HF model card, updated 03/10/2026, "reduced hallucinations").

Reason2-8B vs its Qwen3-VL-8B base:

| Domain | Reason2-8B | Qwen3-VL-8B |
|---|---|---|
| Smart Spaces / Warehouse AI | **69.96** | 42.66 |
| AV Collision | 74.0 | 34.0 |
| VideoPhy2 | 36.80 | 28.24 |
| General overall | 73.73 | 71.98 |

- **Not compared:** the card has no comparison with Gemini, and no Video-MME, MVBench, EgoSchema or Charades-STA scores for Reason2. **We found no published Reason2 numbers on those benchmarks.**
- **Stated limitations:** "fast camera movements, overlapping human-object interactions, **low lighting with high motion blur**, and multiple people performing different actions simultaneously." That describes after-hours CCTV closely.
- **Usage notes:** use `fps=4`, matching the training setup. The model reads timestamps burned into the bottom of each frame. Latency is "will be published shortly", so NVIDIA has not published it.

### 1.3 General video benchmarks (lower relevance)

- **Video-MME** (llm-stats aggregator; self-reported; low quality) [S/V]: Gemini 2.5 Pro 84.8, Qwen3-VL-30B-A3B 74.5, Qwen3-VL-8B 71.4. Cosmos-Reason2 is not listed. Gemini 3.x and Qwen3.7/3.8 rows are mostly vendor-reported. (`dr-gem-cmp-p15-llmstats-videomme.md`)
- **SiT-Bench** (arXiv 2601.03590; spatial reasoning from *text descriptions only*, no pixels) [P]: Gemini-3-Flash **59.46**, Qwen3-VL-8B 45.66, Cosmos-Reason2-8B **42.13**. The authors say "Cosmos-Reason2-8B is outperformed by the general-purpose Qwen3-VL-8B". The same paper gives latency: Reason2-2B 0.34 s and Reason2-8B 0.44 s, vs Gemini-3-Flash with thinking at **40.11 s**. Caveat: these are text-only tasks, not video perception. (`dr-gem-cmp-p03-spatial-arxiv.md`)
- **VANE-Bench** (NAACL'25; older models) [P]: on real anomaly datasets, Gemini-1.5-Pro scored UCF-Crime 76.84, Avenue 100, UCSD-Ped2 94.44, vs GPT-4o at 83.16, 84.85 and 86.11. All open video-LMMs were under 40. Caveat: 10 hand-picked frames per clip containing the anomaly, multiple choice, so this overstates real-world performance. (`dr-gem-cmp-p29-vanebench.md`)
- **Cosmos 3** claims #1 open model on VANTAGE, PAI-Bench, Physics-IQ and RoboLab, and leads the AI City 2026 Traffic Anomaly Reasoning board. [V] Note that the VANTAGE lead is among *open* models only. The Cosmos 3 Reasoner NIM is built on vLLM with EVS token pruning, and Nano is 16B. (`dr-gem-cmp-p02-cosmos3-blog.md`) The VSS docs map "cosmos-reason3" to `cosmos3-nano-reasoner`. (`dr-tech-s5-reason2-latency.json`)

### 1.4 Where each one wins

| Need | Best choice | Evidence |
|---|---|---|
| Yes/no "did this event really happen", rejecting false positives | **Gemini 3.6 Flash** > Cosmos3-Super ≈ Nano > Reason2-8B | VANTAGE EV table |
| Box or localisation of the object in the frame | **Cosmos** (Reason2-8B 83.9, Super 87.0) | VANTAGE Obj Loc |
| Timestamp of the event inside the clip | Roughly a tie (≤ 52 mIoU for all). **Avoid Gemini Flash-Lite** (24.0) | VANTAGE Temp Loc |
| Physical plausibility, AV and warehouse domain questions | **Cosmos** over its own base model | HF card [V] |
| On-prem latency, no data leaving the site | **Cosmos NIM** (~0.84–1.0 s alert verify) | VSS 3.3 blog [V] |
| Sponsor alignment / judges | **Cosmos**, by definition | — |

---

## 2. Video anomaly detection with Gemini specifically

1. **"Are MLLMs Ready for Surveillance?"** (arXiv 2603.04727, Mar 2026) [P]. The most direct Gemini CCTV evaluation found. (`dr-gem-cmp-p11-mllm-surveillance-reality.md`)
   - **Setup:** Gemini 2.5 Flash-Lite as the primary model ("Gemini fast" and "Gemini pro" prompt variants), on ShanghaiTech and CHAD, using 1/2/3-second clips framed as binary anomalous vs normal.
   - **Finding:** "a pronounced conservative bias … high precision but a recall collapse."
   - **Numbers:**
     - Generic prompts: precision 85–100%, recall 1.2–6.5%, F1 0.02–0.13.
     - Class-specific prompts: peak F1 on ShanghaiTech rose from 0.09 to 0.64.
     - More prompt detail did *not* reliably help, and longer clips plateaued.
   - **For us:** Gemini as a verifier will rarely invent events on a generic prompt. It *will* miss real ones unless the prompt names the target classes ("equipment removed from rack/shelf", "door propped open", "person present after hours").
2. **Two-pass zero-shot traffic-event grounding** (arXiv 2605.01512) [P]. (`dr-gem-cmp-r-arxiv-2605.01512.md`)
   - **Gemini 3.1 Flash-Lite** was used on cropped **5 s clips** for typing.
   - Gemini 3.1 alone at 1 fps scored **0.473** for joint temporal-spatial grounding, below a Qwen3-VL pass (0.480) and the full pipeline (0.539).
   - **Cost:** about **$0.01 per video**.
   - **Wall-clock:** about 15 minutes at 10 workers for 2,027 videos, which works out to **≈4.4 s per clip per worker**, end to end, from a home connection.
3. **Evaluation of Vision-LLMs in Surveillance Video** (arXiv 2510.23190) [P]. Small open VLMs, not Gemini, but the dynamics carry over. (`dr-gem-cmp-p06-surveillance-vllm.md`)
   - **Few-shot raises false positives:** Gemma-3-4B's false-positive rate went from 21.7% to 68.7% on UCF-Crime.
   - **Privacy filters raise false positives:** face blur added 2–10.5 points of false positives on RWF-2000.
   - **Lesson:** don't add few-shot example images to the verify prompt without measuring the effect.
4. **Compact VLMs for clip-level CCTV** (PMC12653427) [P].
   - Chain-of-thought and few-shot prompts *lowered* F1 and *raised* latency (Gemma-3-4B: F1 0.818 → 0.684, latency 9.1 s → 15.2 s).
   - LoRA fine-tuning reached F1 of about 0.91.
   - **Lesson:** keep the verify prompt short. (`dr-gem-cmp-p07-pmc-compact-vlm.md`)
5. **Gemini on real home cameras** [R]. This is Google's own product, Gemini for Home on Nest.
   - **Ars Technica:** dogs reported as "deer"; "Gemini mistake[s] dogs and totally empty rooms … for a person"; "one person … becomes several people"; a package delivery denied. Google's spokesperson cited "inferential mistakes". (`dr-gem-cmp-p12-ars-gemini-home.md`)
   - **Android Authority:** invented names ("Michael", "Sarah"); Google says it is improving facial identification. (`dr-gem-cmp-p14-androidauth-names.md`)
   - **The Verge:** "Only sometimes it tells me about things that aren't there." (`dr-comp-verge-gemini.md`)
   - **Wirecutter:** review headline about hallucinations. [S]
   - **Takeaway:** the product failure is a *false-positive person*. Our prompt must give the verdict on objects and areas, and require visible evidence.
6. **Low light and grainy footage** (no Gemini-specific number found).
   - **DarkQA** (arXiv 2512.24985): VLM accuracy falls steadily as light drops. Sensor noise makes it worse. At the most extreme low-light level, some VLMs scored *below a text-only LLM that sees no image at all*. [P]
   - **SynDORBench** (arXiv 2609.31823): at night "no model attains an F1-score of 0.8 … all evaluated LVLMs become effectively non-operational". Night-vision enhancement recovered some of the loss. Models tested were open VLMs and gpt-4o-mini, not Gemini. [P]
   - **Cosmos:** the card lists low light with motion blur as a known limitation.
   - **Takeaway: neither model is safe on dark, noisy clips. Stage the demo with lit footage**, or tag dark clips as "low-confidence: needs human".

---

## 3. Latency

| Path | Number | Source / quality |
|---|---|---|
| Cosmos 3 Super FP8, VSS alert contextualisation, RTX PRO 6000 Blackwell | **1,021 ms → 844 ms** with Adaptive EVS | VSS 3.3 blog [V] (`dr-judge-moustafa-vss33.md`) |
| Cosmos-Reason2-2B / 8B (text-only prompts, vLLM) | 0.34 s / 0.44 s | SiT-Bench [P] |
| Cosmos-Reason2 on a 5 s clip with step-by-step reasoning | unpublished; 01-technical estimates 2–5 s (8B), +5–15 s with reasoning | `01-technical.md` (estimate) |
| Gemini 3.5 Flash-Lite, time to first *answer* token, 10k input tokens | **~8.8 s** (includes thinking); 350 output tok/s | Artificial Analysis [V] (`dr-gem-cmp-p32-*`) |
| Gemini 3.5 Flash-Lite TTFT | "~1.2 s vs 4.5 s for 3.6 Flash" | aireiter blog [S, low quality] |
| Gemini 3.1 Flash-Lite, 5 s clip, end to end incl. network | **≈4.4 s per clip-worker** (derived) | arXiv 2605.01512 [P] |
| Gemini-3-Flash with thinking on (text) | **40.1 s** | SiT-Bench [P] |
| Same video, Files API, repeated calls | "sometimes 5–10s, other times it runs for 2 minutes" | Google support thread [R] (`dr-gem-cmp-p27-*`) |
| Files API `PROCESSING` → `ACTIVE` regression | 5–10 s → 2–5 min; some 15–25 min (May 2025; Google pushed fixes) | discuss.ai.google.dev [R] (`dr-gem-cmp-p25/p26-*`) |
| Gemini 2.5 Flash / Flash-Lite TTFT | "60+ seconds" in one report | discuss.google.dev [S] |
| Gemini 3 Flash calls | "now take over 5 minutes" (Jan 2026) | r/Bard [S] |
| Full video to Gemini | "perfect accuracy but takes 30 seconds" | r/learnmachinelearning [S] |

**Rules for us:**
- Send **inline bytes** (a 5 s clip is well under 100 MB; Google says to use inline for clips under a minute). Inline skips Files API processing entirely.
- Use **static** mode. Google says agentic navigation "may slightly increase TTFT on short clips (<5 minutes)".
- Use the lowest thinking level, and set **a hard 8–10 s timeout**.
- `dr-gem-cmp-p05-gemini-video-docs.md` and `04-gemini-docs.md` §3 have the details.
- Also check the AI Studio status page, which lists several 2026 incidents including a **May 21, 2026 infrastructure outage affecting the Gemini API**. (`dr-gem-cmp-p28-aistudio-status.md`)

---

## 4. Failure modes and limitations

1. **1 fps default sampling.**
   - The docs say the default "may miss details in videos with rapid motion or quick scene changes".
   - In a practitioner test with a 4 fps counter video, Gemini read only frames 2, 6, 10, 14 and 18, confirming about 1 fps. [P/R] (`dr-gem-cmp-p05-*`, `dr-gem-cmp-p09-sanand-fps.md`)
   - At 1 fps a 5 s clip gives Gemini just **5 frames**. A quick grab of a laptop from a desk can fall between frames.
   - **Fix:** set `fps` to 2–5. For 5 s that's about 10–25 frames; the cost is trivial. 06 uses fps=2; consider 4 to match Cosmos's training setting.
2. **Timestamps.** Gemini adds a timestamp every second (MM:SS). Within a 5 s clip, timestamp resolution is effectively 1 s at default fps.
   - Temporal localisation on fixed cameras peaks at about 52 mIoU for every model. 3.5 Flash-Lite scores **24**.
   - **Don't put Gemini-reported sub-second timestamps on the demo screen.** Use the segment's own start and end time from VAST.
3. **Hallucinated people and objects.** See §2.5. Mitigations:
   - Require `evidence` to name the object and its location.
   - Require escalation to cite before-and-after frames.
   - Never ask "who".
4. **Safety filters and people.**
   - Gemini's configurable safety filters are **Off by default** on current models (`dr-gem-cmp-p18-gemini-safety.md`). Non-configurable protections, such as child safety, remain.
   - We found **no reports of Gemini refusing ordinary CCTV-of-people activity description**. Google itself runs Gemini over Nest camera footage of people.
   - The risk is in *identification*. Google's Prohibited Use Policy bans uses that violate "privacy … using personal data or biometrics without legally-required consent" and anything that "tracks or monitors people without their consent". (`dr-gem-cmp-p19-prohibited-use.md`)
   - **Inference (not verified):** prompts asking to identify or describe a specific person are the ones most likely to be refused or to break policy.
   - **Handle `finishReason == SAFETY`** as "no verdict, fall back to human", never as "benign".
5. **429 quota errors.**
   - Limits apply **per project**, not per key.
   - Preview models have tighter limits.
   - There are also **spend-based** 429s: Tier 1 is limited to $10 per 10 minutes.
   - 503 `UNAVAILABLE` is a separate capacity error.
   - Practitioners report 429s after 5–7 calls a minute on the free tier. [P/S] (`dr-gem-cmp-p20-rate-limits.md`, `dr-gem-cmp-s08-*.json`)
   - About 3% of 5 s segments go to the verifier, which across a few demo cameras is well under any paid-tier RPM. **Use a billed key.**
6. **Region.**
   - Unsupported locations get `400 FAILED_PRECONDITION: User location is not supported`.
   - In the EEA, Switzerland and the UK, only **Paid Services** may be used for API clients. [P] (`dr-gem-cmp-p10-gemini-terms.md`, `dr-gem-cmp-s28-*.json`)
   - SF is fine. For the **London (Oct 17) edition**, use a billed key.
   - VAST DataEngine function egress to googleapis.com is **unverified** (06 §6).
7. **Silent-audio 404 on Gemini 3** for mp4 files without an audio track. Confirmed in 06; add a silent track.

---

## 5. Policy, privacy and judging risk

**Data use (primary source: Gemini API Additional Terms, `dr-gem-cmp-p10-gemini-terms.md`):**
- **Unpaid** (AI Studio, free quota):
  - Google "uses the content you submit … to provide, improve, and develop Google products … and machine learning technologies".
  - "Human reviewers may read, annotate, and process your API input and output."
  - "**Do not submit sensitive, confidential, or personal information to the Unpaid Services.**"
  - CCTV of identifiable people is personal information, so **the free tier is ruled out for real footage.**
- **Paid:**
  - Google does not use prompts, including video files, to improve products.
  - It logs them "for a limited period of time" for abuse detection.
  - Data "may be stored transiently or cached in any country".
  - This is acceptable for a hackathon. For production, call it out as a data-residency issue, which is the opposite of the "inside your VAST cluster" story.
- **Hackathon rules:** we found no rule banning non-sponsor models. The judging criteria do reward *sponsor tool use* (`EVENT-DETAILS.md`, `DEEP-RESEARCH.md` §3), so Gemini doing the core work costs points.
- **Ethics framing:** the ACLU flags behaviour analytics that learn "normal" as a chilling-effect risk (already in 02). Google's own policy bans monitoring people without consent. Keep the framing as before: private operational spaces, signage and consent, assets and areas only, no face ID, no "suspicious person".

---

## Contrarian risks (things that could bite us)

- **"Your own benchmark says Gemini is better. Why use Cosmos?"** A sharp NVIDIA judge could raise VANTAGE.
  - *Answer:* Cosmos3-Super is the top *open* model.
  - Our gate needs a box and grounding (Cosmos leads object localisation).
  - The footage never leaves the cluster.
  - We measured both in Weave and publish the specificity of each.
- **Cosmos-Reason2-8B's yes-bias (specificity 57.6) works against the suppression pitch.**
  - If the venue serves Reason2-8B, a naive "is this a real event?" prompt may confirm too many outliers.
  - *Mitigations:*
    - Ask the model to describe the change, then decide.
    - Use a closed list of event classes, with "nothing notable" as an explicit option.
    - Use Reason 3 Nano if it is available.
    - Show the measured precision either way.
- **Gemini may be *too* conservative** (recall collapse on generic prompts). With a generic prompt, the A/B could show Gemini "suppressing" real events. Use the same class-specific prompt for both arms.
- **Every benchmark here is zero-shot on someone else's footage.** VANTAGE has only n=163 for event verification. Our ~60-clip eval is the only number that should appear on stage.
- **Gemini latency tail.** One 2-minute stall during the live demo would undo the "pages you in seconds" claim. Mitigations: hard timeout, circuit breaker, and pre-recorded fallback clips.

---

## Verdict: when to fall back to Gemini (decision rule)

The default is **Cosmos (venue NIM) on every escalated segment.** Route to Gemini only when one of these holds:

1. **Outage.** Cosmos returns 404/5xx, times out after more than 10 s, or fails 3 times in a row (soft errors), which opens the circuit breaker. Gemini takes over for `CB_COOLDOWN_MIN` minutes. (Mechanics are in 06.)
2. **Evaluation arm.** In the Weave eval, *every* labelled clip goes to both backends offline. This is not on the live path.
3. **Optional tie-break (consider; off by default).** Cosmos says "escalate", but has low confidence or no box, **and** the clip is lit (luma above a threshold). Gemini's higher specificity on VANTAGE makes it a reasonable second opinion that *can only veto*. It cannot create alerts. Turn this on only if the Weave A/B shows that it improves precision on our clips.

Never send to Gemini:
- footage with identifiable faces on the free tier;
- any request to identify a person;
- dark or IR clips as a "better model". Both models degrade there; route those to a human.

Settings when Gemini is used:
- **Model:**
  - `gemini-3.6-flash` if the A/B shows the accuracy gain is worth it. It has the best VANTAGE event-verification score.
  - Otherwise `gemini-3.5-flash-lite`, the cheapest. Its event-verification score of 70.4 still beats Reason2-8B's 64.1, but **don't use its timestamps** (24.0 temporal localisation).
  - `gemini-3.8-flash` is not on VANTAGE, so its performance there is unmeasured.
- **Request:** inline bytes, static mode, `fps` 2–4, low media resolution, minimal or low thinking, JSON schema, `store=False`, 10 s timeout, a billed key.
- **Prompt:** the same class-specific prompt as Cosmos, with "nothing notable" as an explicit option. The verdict must cite a visible object or area.

## How to frame it to judges

- **Lead with Cosmos.** "Cosmos-Reason2 (or Reason 3 Nano) verifies every outlier on the venue's NIM, inside the VAST cluster. The footage never leaves."
- **Gemini is the seatbelt.** "Hosted Reason2 has been 404ing, and NIMs don't recover from a crash. So we built a circuit breaker: if Cosmos is down, a hosted fallback keeps the pipeline honest, and Weave tags every verdict with which backend made it."
- **Turn the comparison into a W&B story.** "We didn't pick a model on vibes. Here's our Weave eval: the same 60 labelled clips through Cosmos and through a frontier API model, with precision, specificity and latency side by side." This plays to Vatsa (CoreWeave) and the W&B judges, and shows rigour without saying Gemini is better.
- **If an NVIDIA judge asks about VANTAGE:**
  - Credit it: "NVIDIA's own VANTAGE-Bench is exactly why we measure. Cosmos3 is the top open model there."
  - Then pivot: "and open plus on-prem is the whole point for footage like this."
- **Don't say:** "Gemini is our verifier", "we use whichever is better", or any claim that Cosmos is less accurate. The point is the eval, not a ranking.
- **Privacy line:** "The fallback runs on a paid key with no training on our data. In production it's off by default, because the right answer for CCTV is on-prem Cosmos."

---

## Sources (captured under `docs/sources/`)

**Primary: papers and docs**
- arXiv 2609.09396, VANTAGE-Bench (NVIDIA/Clemson): `dr-gem-cmp-p21-vantage-arxiv.md`, `dr-gem-cmp-p22-vantage-site.md`
- arXiv 2603.04727, MLLMs ready for surveillance? (Gemini 2.5 Flash-Lite VAD): `dr-gem-cmp-p11-*`
- arXiv 2605.01512, two-pass zero-shot traffic-event grounding (Gemini 3.1 Flash-Lite): `dr-gem-cmp-r-arxiv-2605.01512.md`
- arXiv 2510.23190, Evaluation of Vision-LLMs in Surveillance Video: `dr-gem-cmp-p06-*`
- PMC12653427, compact VLMs for clip-level surveillance anomaly detection: `dr-gem-cmp-p07-*`
- arXiv 2601.03590, SiT-Bench (Gemini-3-Flash vs Cosmos-Reason2, latency): `dr-gem-cmp-p03-*`
- arXiv 2406.10326, VANE-Bench: `dr-gem-cmp-p29-*`
- arXiv 2512.24985, DarkQA: `dr-gem-cmp-r-arxiv-2512.24985.md`
- arXiv 2609.31823, SynDORBench (night visibility): `dr-gem-cmp-r-arxiv-2609.31823.md`
- arXiv 2603.25467, GridVAD (checked; no Gemini number): `dr-gem-cmp-r-arxiv-2603.25467.md`
- HF model card nvidia/Cosmos-Reason2-8B: `dr-gem-cmp-p01-*`
- NVIDIA Cosmos 3 technical blog: `dr-gem-cmp-p02-*`
- NVIDIA VSS 3.3 blog (EVS latency): `dr-judge-moustafa-vss33.md`
- Gemini API video-understanding docs: `dr-gem-cmp-p05-*`
- Gemini API Additional Terms: `dr-gem-cmp-p10-*`
- Safety settings: `dr-gem-cmp-p18-*`
- Rate limits: `dr-gem-cmp-p20-*`
- Google Generative AI Prohibited Use Policy: `dr-gem-cmp-p19-*`
- Gemini 3.5 Flash model card: `dr-gem-cmp-p23-*`
- Google blog: Gemini 3.6 Flash / 3.5 Flash-Lite: `dr-gem-cmp-p31-*`
- AI Studio status page: `dr-gem-cmp-p28-*`

**Vendor or third-party benchmarks**
- Artificial Analysis, Gemini 3.5 Flash article and 3.5 Flash-Lite providers page: `dr-gem-cmp-p24-*`, `dr-gem-cmp-p32-*`
- llm-stats Video-MME leaderboard: `dr-gem-cmp-p15-*`
- Jetson AI Lab Cosmos-Reason2-8B page: `dr-gem-cmp-p16-*`

**Practitioner and press**
- Ars Technica, Gemini for Home: `dr-gem-cmp-p12-*`
- Android Authority, invented names: `dr-gem-cmp-p14-*`
- The Verge: `dr-comp-verge-gemini.md`
- Google AI forum, Files API slow / ACTIVE regression: `dr-gem-cmp-p25-*`, `p26-*`
- Google support, inconsistent latency: `p27-*`
- S. Anand, 1 fps test: `p09-*`
- Sveta Morag, "Notes from the field" (Google Cloud Medium): `p17-*`
- HN Show HN SentrySearch (Gemini Embedding 2 for sentry footage): `p30-*`

**Snippets only (Reddit and others not scrapable)**
- r/learnmachinelearning "30 seconds" thread
- r/Bard Gemini 3 Flash slow
- r/googlecloud 429s
- r/LocalLLaMA Cosmos-Reason2 edge benchmark
- discuss.google.dev "60+ s TTFT"
- aireiter TTFT
- Wirecutter review
- Search JSON: `dr-gem-cmp-s01…s30-*.json`
