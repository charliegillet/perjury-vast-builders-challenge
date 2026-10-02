> **SUPERSEDED (2026-10-02) by [FINAL-IDEA-v3.md](FINAL-IDEA-v3.md) (PERJURY).** ASSAY is kept as the **fallback**: the v3 §11 decision tree routes here at 10:45 only if the Pack A gates fail and the PIE mapping gate (G2 below) passes. Otherwise it routes to ASSAY-GOLD.

# FINAL IDEA v2: ASSAY

> **Replaces [FINAL-IDEA.md](FINAL-IDEA.md) (UNWATCHED).** Round-2 corpus research showed UNWATCHED's learned-normal story only holds on Pack D, which may be sparse and has one baseline day (n=1). The judge simulation below commits to **ASSAY**, which merges SCENARIO MINER, VOID, and QUORUM's camera wall. **The pre-decided pivot is NIGHTSHIFT + VOID** (§13).
> `[A]` marks an assumption that the 10:00–10:45 preflight (§6) must confirm. Every number on screen is computed by code in the repo. If we didn't measure it, it doesn't appear.

---

## 0. The pitch in one breath

**Name:** ASSAY. An assay measures what's really in the ore. We mine scenarios and measure them.

**One-liner:** *Ask for a driving scenario in plain English. ASSAY pulls every instance from hours of dashcam archive, has Cosmos3 verify each one, and grades itself against human labels: what it found, what it missed, and what it made up.*

**Stage line:** "Video search shows you hits. It can't tell you what it missed or what it made up. ASSAY can. On PIE it found **R%** of the human-labeled crossings at **P%** precision. On the I-24 highway, where there are provably no pedestrians, it confirmed **0** of the **N** clips that search ranked highest."

**Buyer:** the **scenario-curation / data lead on an AV, ADAS or robotics team**. Their job is "pull every unprotected pedestrian crossing from last month's fleet drives for the regression suite or the simulator."
- Today they write rules over perception logs, hand-scrub video, or pay for labeling.
- VLM search gives them a ranked list with no error bars, and a list without error bars can't go into a safety case.

---

## 1. Judge simulation (C = creativity, T = technical, I = impact; out of 10)

Judges are scored with their known lenses in mind:
- **Hassan** works on VSS 3.3, Physical AI Data Factory, and model evaluation and SDG.
- **Adam** is VSS product.
- **Ram and Brian** care whether VAST is used deeply and whether this is the "AI OS for unstructured data" story.
- **Anushrav** is CoreWeave's physical-AI solutions architect.
- **Arnav** is a SpaceXAI/Cursor field engineer who looks for agentic building and shipping speed.

| Finalist | Hassan | Adam | Ram | Brian | Anushrav | Arnav | **Mean /30** | Demo |
|---|---|---|---|---|---|---|---|---|
| **ASSAY** (SCENARIO MINER + VOID + QUORUM wall + held-out prompt tuning) | 9/9/9 | 9/8/9 | 8/8/8 | 9/8/9 | 9/8/9 | 8/9/8 | **25.7** | 8 |
| SCENARIO MINER + VOID (round-2 ideator version) | 8/8/9 | 8/7/8 | 7/7/7 | 8/7/8 | 8/8/9 | 7/8/7 | 23.2 | 7 |
| "Trust layer" across all packs (measured precision per pack) | 7/6/7 | 7/6/8 | 7/7/7 | 8/6/8 | 7/6/7 | 6/6/7 | 20.5 | 5 |
| NIGHTSHIFT + VOID | 6/7/7 | 6/7/7 | 7/7/7 | 8/7/7 | 6/7/6 | 6/7/6 | 20.2 | 6 |
| QUORUM + VOID | 7/6/5 | 7/6/6 | 8/7/6 | 7/6/6 | 7/6/6 | 8/7/5 | 19.3 | 8 |

**What each judge would say about ASSAY:**
- **Hassan:** "VSS 3.3 search returns confirmed and rejected clips. This tells me how often 'confirmed' is right, with a negative control. That's the eval I'd want in the Data Factory."
  - Risk: he will ask whether PIE's label matches the query. See Q&A 2.
- **Adam:** "It sits on top of VSS search and alert verification and quantifies them. It doesn't re-implement them. I'd demo this to an AV customer."
- **Ram:** "They pulled whole slices straight from VastDB, past the backend's top_k, and wrote the mined scenarios back as a table."
  - Minus one point because there's no custom DataEngine function. The rules forbid that anyway, so say so.
- **Brian:** "Unwatched fleet video becomes a curated, queryable asset with a quality number on it. That's the AI OS pitch."
- **Anushrav:** "Physical-AI teams spend their GPU budget curating data. 'Cosmos calls per mined scenario' is the metric they buy on."
- **Arnav:** "An agent that rewrites its own verify prompt against a dev split and touches the held-out test exactly once is real agent engineering, not a wrapper."

**Why the other finalists lose:**
- **NIGHTSHIFT:** Pack D may be empty, the baseline is n=1, and it overlaps Key events plus VSS alert verification. Its precision would come from 20 segments we labeled ourselves.
- **QUORUM:** cameras agreeing on generic traffic is trivially true. Its 0/16 headline is really VOID's result, so its best visual (the camera wall) moves into ASSAY as the negative-control panel.
- **Trust layer across packs:** C, D, E and F have no ground truth, so a cross-pack precision table would be mostly self-labeled. It becomes the **Future** slide instead.

**Convergence (disagree-and-commit):**
- The Devil's Advocate is the true believer. It named SCENARIO MINER + VOID "the stronger primary" and wrote its own fixes.
- The Demo-Designer ranked QUORUM's glance first and SCENARIO MINER's numbers as the most credible. ASSAY takes both.
- The Ideator's NIGHTSHIFT becomes the pivot.
- **COMMIT to ASSAY.**

---

## 2. Why this beats the baseline

The baseline is the stock search UI, the prompt-suggester's Key events, and NVIDIA VSS alert verification (plus the VSS 3.3 search that confirms or rejects clips).

| | Stock search UI | Key events | VSS alert verification / 3.3 confirmed-rejected search | **ASSAY** |
|---|---|---|---|---|
| Question it answers | "Show me some examples" | "What sounds interesting lately" | "Is this alert or clip real?" | **"Give me every instance, and how sure are you?"** |
| Output size | top_k (15), always non-empty | LLM-picked list | Per-item verdict | **Complete set over a slice, exported as scenario manifest rows** |
| Says "none"? | No. Ranking always returns something | No | Per item | **Yes. The I-24 wall shows 0** |
| Accuracy number | Relevance % (18–25%, not calibrated) | None | None reported to the user | **Event recall, segment precision, Wilson 95% CI, and false-positive rate on the negative control** |
| Gets better | No | No | No | **A tuning agent improves the verify prompt on dev, and the gain is measured on held-out test** |
| Explains errors | No | No | Reason text | **Each false positive is tagged, e.g. "PIE says this pedestrian waited at the curb"** |

**Say it this way:** "VSS confirms clips. ASSAY tells you how often a confirmation is right, and what never got shown to it."

---

## 3. Architecture (on the actual stack: no custom DataEngine functions)

```
                    data/pie_gt.json  (built TONIGHT from PIE annotations, MIT, baked into the repo)
                    data/scenarios.yaml (3 labeled scenarios + query text + verify prompts)
                                   │
 ┌─────────── RECALL STAGE (cheap, wide) ──────────────────────────────────────────────┐
 │ W&B Inference LLM → 6 paraphrases of the scenario                                   │
 │ backend POST /api/v1/search  (camera_id filter pie_cam-3 | i24_cam-1, top_k=K,      │
 │                               min_similarity 0.10; `results` = moments)             │
 │ + vastdb-read slice pull (reasoning_content, perception/object counts, source,      │
 │   original_video, timing) → caption-keyword + YOLO person-count prefilter           │
 │ + [stretch] Cosmos-Embed1 /v1/embeddings(text) · vectors_visual (if vector select OK)│
 │ union, dedupe by `source` → candidates C   (we report the recall ceiling = GT∩C)    │
 └─────────────────────────────────────────────────────────────────────────────────────┘
                                   │
 ┌─────────── VERIFY STAGE (expensive, narrow) ────────────────────────────────────────┐
 │ boto3 GET S3_SEGMENTS_BUCKET/<source> → ffmpeg 480p, 4 fps → base64 data URI        │
 │ Cosmos3-Reason $COSMOS3_REASON_URL/v1/chat/completions (bearer GPU_BEARER_TOKEN)    │
 │   scenario-specific JSON prompt → {present, evidence_t, bbox, in_ego_path, reason}  │
 │ [stretch] YOLO11 $YOLO_URL/v1/infer → per-frame person boxes → ego-corridor overlay │
 │ asyncio semaphore (concurrency from the preflight), disk cache keyed by             │
 │ (source, prompt_version)                                                            │
 └─────────────────────────────────────────────────────────────────────────────────────┘
                                   │
 ┌─────────── SCORE + TUNE ────────────────────────────────────────────────────────────┐
 │ map segment → (set, video, frame range) → match against GT intervals (τ = ±1 segment)│
 │ Weave Evaluation: dataset = dev/test slices, scorers = event-hit, seg-precision,    │
 │   hard-negative tag, JSON-valid, latency                                            │
 │ Tuning agent (W&B Inference): reads dev FPs/FNs + Cosmos reasons → verify prompt v2 │
 │   → re-score dev → FREEZE → test run exactly once per version                       │
 └─────────────────────────────────────────────────────────────────────────────────────┘
                                   │
 OUTPUTS: scenario manifest → Parquet in S3 + VastDB table `assay_scenarios` [A: writable]
          FastAPI + static UI, deployed with deployment/deploy-app-no-registry → team K8s /app
          cache/*.json results (UI renders from cache; only the live panel calls models)
```

**What's reused vs new:**
- **Reused, untouched:** the DataEngine ingest graph (Segmenter → YOLO → Cosmos3 → Embedder → VastDB), the backend search API, and the starter skills `retrieval/search`, `retrieval/vastdb-read`, `retrieval/list-metadata`, `gpu/model-smoke-test`, `deployment/deploy-app-no-registry` and `submission`.
- **New:** one Python package `assay/` plus one app `app/`.
- **Pitch it honestly:** "VAST's pipeline is the ingest. ASSAY is the miner and auditor on top of the VastDB index."

**Sponsor features, one hook per judge:**
- **VAST**
  - `vastdb` SDK pulls the whole slice with pushdown (`camera_id = 'pie_cam-3'`), bypassing the backend's top_k. That's what makes recall measurable at all.
  - Direct segment fetch from the S3 segments bucket.
  - Mined scenarios written back as a VastDB table that is queryable with SQL.
  - *Stretch:* re-ingest the dev slice with a scenario-specific custom prompt (≤800 chars, `live_driving`) and measure the gain in caption-level recall. Never after 12:30.
- **NVIDIA**
  - Cosmos3-Reason as a measured verifier, with its 2D-grounding bbox burned into each scenario card.
  - Cosmos-Embed1 used directly for text→video.
  - YOLO11 called directly for per-frame geometry (*stretch*).
- **W&B:** Weave Evaluations with a version-comparison leaderboard and a dev/test split, plus W&B Inference for paraphrasing and the tuning agent.
- **CoreWeave:** a cost meter showing Cosmos calls per footage-hour and per confirmed scenario, plus GPU-seconds.
- **Cursor:** the whole thing was built with the `agent` CLI and starter skills on the VM. The tuning loop is itself an agent.
- **Canary-1B:** skip unless `ffprobe` shows audio on PIE segments. It's not on the critical path.

---

## 4. Packs and scenarios

| Role | Pack | What we use |
|---|---|---|
| **Positives, external labels** | B `pie_cam-3` (PIE, MIT) | Dev slice ≈ 20 min and test slice ≈ 30 min. They come from **different videos** (split by video, never by segment). Chosen tonight from the parser so that each has ≥25 S1 events. |
| **Negative control** | A `i24_cam-1` (I24-3D) | By dataset design there are **no pedestrians or crashes** [S, Appendix VII]. We use the top-ranked candidates from the same recall stage, which are the hardest negatives search can find. |
| Hard negatives inside B | PIE pedestrians who intend to cross but don't (~894 labeled) | Gives strict precision real teeth |
| Not used | C, D, E, F | Kept for the Future slide. D is reserved for the pivot. |

**Scenarios with ground truth** (from PIE labels; definitions are fixed tonight in `data/scenarios.yaml`):

| ID | Query | Positive event = | Notes |
|---|---|---|---|
| **S1 (hero)** | "pedestrian crossing the street in front of the car" | A pedestrian with `attributes.crossing == 1`. Interval = the frames whose per-frame `cross` == crossing. If the track ends at the crossing point, use `[crossing_point, crossing_point+60]` `[A: parser handles both]`. | ~519 in total, about 1/min |
| S2 | "pedestrian waiting at the curb who does not cross" | `intention_prob ≥ 0.5` and `crossing == 0`. Interval = the track. | Scenario that tests hard negatives |
| S3 (live, rare) | "pedestrian gesturing to the driver / waving the car through" | Per-frame `gesture ∈ {hand_ack, hand_yield, hand_rightofway, nod}` | The needle in the haystack. Small n, so show the CI. |
| Free text | Anything a judge types | **No ground truth**, so the UI says "precision unmeasured: audit mode" and shows Cosmos-confirmed cards only | We refuse to show a number we didn't measure |

---

## 5. Numbers on screen and how each is computed honestly

Notation:
- G = the set of GT events in the slice.
- H = the hits ASSAY confirmed.
- τ = 1 segment (5 s) of tolerance, declared on screen.

| # | Number | Formula | Honesty guard |
|---|---|---|---|
| 1 | **Event recall** | \|{e ∈ G : ∃h ∈ H, overlap(h, e ± τ)}\| / \|G\| | Wilson 95% CI next to it. Test slice only. |
| 2 | **Segment precision (strict)** | \|{h ∈ H : overlaps some S1 interval ± τ}\| / \|H\| | Strict = in-path crossing only |
| 3 | Segment precision (lenient) | Same, but also counts `crossing-irrelevant` (crossing outside the ego path) | Shown smaller, labelled "lenient" |
| 4 | **Recall ceiling** | \|G ∩ candidates\| / \|G\| | Separates "search never surfaced it" from "Cosmos rejected it" |
| 5 | **Baseline rows** | (a) stock search top-15, scenario text, min_sim 0.2 · (b) the same K candidates *without* verify · (c) caption keyword grep | (b) is the fair comparison. It has the same candidates, so the precision gain is attributable to verify alone. |
| 6 | **Tuning gain** | Test recall/precision for v2 − v1. v2 was chosen on dev only. | Test is run once per version. The Weave leaderboard shows the timestamps. |
| 7 | **VOID: I-24 confirmed** | k confirmed out of N candidates examined (N = top-ranked I-24 candidates from the same recall stage, ~100) | "Hardest N", not "all segments". **Every confirmed I-24 hit is shown on screen.** Before reporting, two teammates eyeball each one. |
| 8 | Stock search on I-24 | The number of clips the stock search returns for S1 scoped to `i24_cam-1` at the same min_sim | The wall tiles turn red for those |
| 9 | FP breakdown | Each FP is tagged: `hard-negative` (overlaps a PIE pedestrian labelled not-crossing), `unlabeled-audit` (two of us say it's a real crossing PIE didn't label), or `wrong` | Unlabeled-audit FPs stay counted as FPs in metric 2 and are reported separately. We never quietly relabel. |
| 10 | Cost | Cosmos calls / footage-hours. GPU-seconds = Σ latency. Calls per confirmed scenario. | Uses measured latencies only |

---

## 6. First 45 minutes: preflight checks and decision tree (decide by **10:45**, no pivot after **11:00**)

`assay/preflight.py` (pre-built tonight) prints a PASS/FAIL table for every gate.

| Gate | Owner | Check | PASS threshold | Done by |
|---|---|---|---|---|
| **G1 Platform** | Nihal | Run `model-smoke-test`. Time a Cosmos3 yes/no on one PIE 5 s segment fetched from S3 (480p/4 fps). Run 4 concurrent calls. | Segment mp4 readable. p50 ≤ 10 s. 4-way concurrency without 429s, i.e. sustained throughput **≥ 8 clips/min**. | 10:20 |
| **G2 PIE mapping** | P2 | `vastdb-read`: count `pie_cam-3` rows, print columns plus 5 rows (`source`, `original_video`, timing, metadata). Work out which mapping case applies: (A) one file per PIE video; (B) concatenated set, so offset = cumulative frames of earlier videos + segment offset; (C) chunked, so chunk_idx × chunk_len + seg_idx × 5. Then the **anchor test**: 3 large, unoccluded GT crossings at the start, middle and end of 2 videos or sets. Open the predicted segment. | ≥ 300 PIE rows covering ≥ 2 distinct videos. **≥ 5 of 6 anchors visibly show the crossing within ±1 segment.** A constant offset can be fixed from 2 anchors if the 3rd then validates. | 10:40 |
| **G3 Negatives** | P4 | `i24_cam-1` rows ≥ 300. Stock search for S1 scoped to i24 at min_sim 0.2 returns ≥ 5 clips. Do filenames carry `scene*_p*c*`? | Rows ≥ 300. (If search returns < 5, the stock-baseline row on the wall uses caption grep. Not a blocker.) | 10:30 |
| **G4 Pack D** (pivot only) | P4 | 10-min peek: can capture time be recovered from filename or chunk offset? Count non-parked events in 30 sampled segments across both days, using captions plus eyeballing. | Time recoverable and ≥ 10 real non-parked events | 10:40 |
| G5 Egress | P3 | `curl` W&B Inference and Weave. Is GitHub reachable from the VM? | W&B reachable. (If not, paraphrases come from a fixed list and the tuner runs on a laptop.) | 10:15 |

**Decision tree (10:45):**
```
G1 ✓ and G2 ✓ ─────────────────────────────► ASSAY-PIE   (primary, as written)
G1 ✓ and G2 ✗ (mapping unrecoverable) ─────► ASSAY-GOLD  (same code, same pitch; GT = blind gold set:
                                              P3+P4 each label the same 200 dev+test PIE segments,
                                              10:45–11:45; keep only segments they agree on; report
                                              Cohen's κ; say "our labels, double-blind" on screen)
G1 ✗ (throughput < 8/min or mp4 unreadable) ► still ASSAY, with verify capped at
  but PIE rows OK                              throughput × 60 min, plus
                                              caption-only verification for the rest, labelled as such
PIE unusable (< 300 rows, or segments
  unplayable) AND G4 ✓ ────────────────────► PIVOT: NIGHTSHIFT + VOID (§13)
PIE unusable AND G4 ✗ ─────────────────────► ASSAY-GOLD on whatever pack has the most
                                              unambiguous events (C near-miss clips), with I-24 as VOID
```
ASSAY-GOLD is a **degraded mode**, not a pivot. The only thing that changes is where the labels come from.

---

## 7. Demo scripts

**UI layout (one screen):**
- Top: scenario picker (S1/S2/S3/free text) and the slice selector (dev/test).
- Left: **scorecard** with these rows: stock top-15, search top-K without verify, ASSAY v1, ASSAY v2 (tuned on dev, scored on test).
- Center: the **drive barcode**. A timeline of the test slice: GT events are ticks (green when found, red when missed), and FPs are grey marks with a tag.
- Right: the **VOID wall** of I-24 tiles. Red means stock search returned the tile; it turns grey when Cosmos rejects it; it would turn blue if confirmed, and none are.
- Bottom: a **scenario card stream**. Each card has a keyframe with the Cosmos bbox, the reason, a GT badge (TP / hard-negative / unlabeled-audit), and an export button.

### 7a. Table-side (3 min, technical, laptop on the VM browser plus the /app URL)
| t | Beat |
|---|---|
| 0:00–0:20 | "AV teams don't need examples. They need **every** pedestrian crossing in the fleet video, plus an error bar. Search gives examples with no error bar." |
| 0:20–0:50 | Scorecard on the S1 test slice. Read across the rows: stock top-15 → K without verify (high recall ceiling, low precision) → ASSAY v1 → v2. Point at the CI. "The test videos were never used for tuning." |
| 0:50–1:20 | Barcode. Click a red tick (a miss): "the recall ceiling says search never surfaced it, so the miss is in recall, not verify." Click a grey FP: "PIE labelled this pedestrian as **waiting**. It's a hard negative, and that's exactly the error we report." |
| 1:20–1:45 | VOID wall: "Same question on the I-24 highway, which has zero pedestrians by design. Stock search returned 15. Cosmos confirmed **0 of the N hardest**." |
| 1:45–2:25 | **Live:** pick S3 (gesture) or have the judge type a free-text scenario. Paraphrases appear, then search, then the top 12 are verified live in about 30 s and cards stream in. For S3 a live precision@12 is shown against GT. For free text, the label reads "audit mode, unmeasured". |
| 2:25–2:50 | Weave: the leaderboard of v1 vs v2 on dev and test, plus one trace with the tuning agent's diff of the prompt. Cost meter: "Cosmos ran on X% of segments, Y calls per confirmed scenario." |
| 2:50–3:00 | `assay_scenarios` table in VastDB. "The mined set is now a dataset you can query." |

### 7b. Stage (3 min, in the required order: Problem → Solution → Market → Validation → Demo → Business Model → Future → Team)
| t | Section | Beat |
|---|---|---|
| 0:00–0:20 | **Problem** | "Every AV team has petabytes of drive video and one question: *show me every time a pedestrian stepped out in front of us.* VLM search gives a list and no error bars. You can't put a list without error bars into a safety case." |
| 0:20–0:40 | **Solution** | "ASSAY mines a scenario across the whole archive on VAST, has Cosmos3 verify every candidate, and grades itself against human labels: found, missed, made up." |
| 0:40–0:55 | **Market** | Buyer: AV/ADAS and robotics data and simulation teams. Comparables `[A: verify the figures tonight]`: Voxel51 (data curation, VC-backed), Scale Nucleus, Applied Intuition's data tooling, Foretellix. RefAV (scenario mining benchmark) shows off-the-shelf VLMs score low on this task. "Mining is the bottleneck." |
| 0:55–1:20 | **Validation** | Scorecard: "R% recall, P% precision on held-out PIE drives that human annotators labelled. Our tuning agent improved test recall from a to b and never saw the test set. On I-24: 0 of N." |
| 1:20–2:15 | **Demo** | Barcode → one hard-negative FP explained → VOID wall turns grey → a live S3 gesture query with cards streaming in |
| 2:15–2:35 | **Business model** | Priced per footage-hour mined plus a platform seat. We can offer a **precision SLA** because we measure precision. Cost floor = the on-screen Cosmos calls per hour. Land through the VAST AI OS and the NVIDIA Physical AI Data Factory ecosystem. |
| 2:35–2:50 | **Future** | The same auditor on every pack: synthetic SDG as controlled positives, any camera's empty hours as free negatives, human audits fed back as Weave labels, and export to OpenSCENARIO / Cosmos-Transfer for sim. |
| 2:50–3:00 | **Team** | Nihal (agent and backend; SRE background, the evals-and-error-budgets mindset) + teammates. "Measured, not claimed." |

---

## 8. Submission video (freeze 15:30, record 15:35–16:05, upload by 16:15, submit by 16:20)
- **Length 2:30.** Built from the stage script, recorded from the cached run (the scorecard and barcode render from `cache/*.json`).
- **The live segment** is a screen recording of a real live S3 run done at 15:35. Say: "this part ran live; the scorecard is from the 13:45 frozen test run."
- **Shots, in order:** the problem title card → scorecard → barcode click → VOID wall → live cards → Weave leaderboard → VastDB table → close.
- **Logistics:** record with the VM's screen recorder or the laptop's QuickTime. Upload as an unlisted YouTube or Drive link and check the link in an incognito window.

---

## 9. Hour-by-hour plan (10:00–16:30)
- **Roles:** **Nihal** = agent/backend lead. **P2** = VAST infra and mapping. **P3** = UI and deploy. **P4** = ground truth, eval, Weave, pitch.
- With 3 people, P3 also takes P4's work and the gold-label fallback becomes 120 segments.

| Time | Nihal | P2 | P3 | P4 |
|---|---|---|---|---|
| 10:00–10:15 | Log in, `git pull`, clone our repo next to the starter repo, run `preflight.py`, G1 starts | SSH tunnel, `list_catalog.py` | G5 egress check. Deploy the UI skeleton to /app with fixture data **now** to prove the deploy path. | `list-metadata`, `ffprobe` audio |
| 10:15–10:45 | G1: latency, concurrency, verify v1 on 5 PIE segments | **G2 mapping + anchor test** | Deploy finished, health check | G3 (I-24) + G4 (Pack D peek) |
| **10:45** | **DECISION** (§6). Write the decision as the first line of the README. | | | |
| 10:45–12:00 | `recall.py` live (paraphrases → search → union) and `verify.py` batch runner + cache | `mapping.py` finalized → `cache/seg_gt_{dev,test}.json`; vastdb slice pull; S3+ffmpeg fetch | UI on real cache files: scorecard + card stream | Weave Evaluation harness; baseline rows (a)(b)(c) on **dev** |
| 12:00–13:00 | v1 verify on dev in the background → first dev scorecard | I-24 run (recall + verify on the hardest ~100) | Barcode + VOID wall | Two-person FP audit on dev; eyeball every I-24 confirm |
| 13:00–13:45 | **Tuning agent** → v2 on dev. **Freeze v2 at 13:45.** | Scenario manifest → Parquet/S3 + `assay_scenarios` table | Live panel (SSE stream, top-12) | Slides, stage script with blanks for the numbers |
| **13:45** | **Launch TEST runs v1 and v2, once each** (background, cached) | | | |
| 14:00–15:00 | Live-path hardening (S3 query, timeouts, 2B/4-frame degrade); cost meter | Redeploy to /app; README "tools used"; repo-public dry run (scrub secrets) | bbox burn-in on cards, polish | Fill the numbers into the slides from the test cache; Weave screenshots |
| 15:00–15:30 | **Numbers frozen at 15:15**. Rehearsal 1. | Health / stability | UI freeze | `submission` skill → SUBMISSION.md (<40 words) |
| 15:30–16:10 | **Code freeze.** Record the live segment 15:35, record the full video by 16:05 | Make the repo public, last secret scan | Screenshot for the portal | Video edit + upload, check the link |
| 16:10–16:30 | **Submit on the tokens& portal by 16:20** | Watch quota | Reset the UI to the S1 test view | Confirm the submission shows in the gallery |
| 16:30–17:00 | Q&A drill | Hold the VM session open | Table-side laptop setup | Rehearse the stage script |

**Hard rules:**
- No re-ingest after 12:30.
- Never tune after 13:45.
- The test split is only touched by the 13:45 runs, plus the live S3 demo, which is a different scenario.

---

## 10. Pre-build TONIGHT (so tomorrow only the unknowns are left)
1. **`assay/gt/pie_parse.py` + `data/pie_gt.json`.**
   - Download `annotations.zip`, `annotations_attributes.zip` and `annotations_vehicle.zip` from `github.com/aras62/PIE` on the laptop and parse them.
   - Output, per set and video: `num_frames`, fps 30, the cumulative frame offset within the set, and per-pedestrian tracks with the attributes we use (`crossing`, `intention_prob`, `crossing_point`), per-frame `cross`/`gesture`/`action`, and box heights.
   - Emit the S1/S2/S3 event intervals.
   - Commit the JSON with MIT attribution. The VM then needs no internet beyond GitHub.
2. **`assay/gt/mapping.py`.** Implement mapping cases A, B and C plus a 2-anchor offset fit. Also `pick_anchors.py`, which prints 6 large, unoccluded crossings (box height > 150 px) at the start, middle and end of each candidate video, with predicted timestamps for every case.
3. **Choose the slices.** From the parser output, pick dev ≈ 20 min and test ≈ 30 min from **different videos**, each with ≥ 25 S1 events. Prefer the val/test sets (set05, set06, set03 subsets). Write them to `data/slices.yaml`, with backups in case those videos aren't indexed.
4. **`assay/score.py` + `tests/test_score.py`.** Event recall with τ, strict and lenient precision, recall ceiling, Wilson CI, FP tagging (hard-negative / unlabeled-audit / wrong), Cohen's κ for GOLD mode. Unit tests run on synthetic intervals.
5. **`assay/verify.py`.**
   - Cosmos3 client in OpenAI format with a `video_url` data URI, ffmpeg downscale, JSON extraction and repair, async semaphore, disk cache, `@weave.op`.
   - Degrade path: 4 keyframes as images.
   - Gemini only as an outage fallback, off by default.
   - **Verify prompts v1 for S1/S2/S3**, plus two alternates.
6. **`assay/recall.py`.** JWT login and the search client (camera_id filter, top_k, min_similarity), the paraphrase prompt on W&B Inference (with a fixed-list fallback), the vastdb slice pull (excluding vector columns), and the caption/YOLO prefilter.
7. **`assay/tune.py`.** The tuning-agent prompt. Input: dev FPs/FNs with Cosmos reasons and GT tags. Output: a prompt diff of ≤ 800 chars with a rationale. Runs as a Weave op.
8. **`assay/preflight.py`.** Gates G1–G5 with PASS/FAIL thresholds hard-coded from §6.
9. **`app/`.** FastAPI + static HTML/JS: scorecard, barcode (SVG), VOID wall grid, card stream (SSE). It renders from `cache/fixture_*.json` with fake data, so the UI is done before 10:00. Also a Dockerfile and manifest compatible with `deploy-app-no-registry` (read that SKILL tonight).
10. **`nightshift/` pivot stub.** `diff.py` (bin D rows by capture hour per day, moving-vs-parked caption keywords, rank the top-20 day-over-day differences) reusing `verify.py` and `score.py`.
11. **Pitch assets.** Slide shells with `{R}`, `{P}` and `{N}` placeholders, the Q&A card, and a check of the comparables figures `[A]`.

---

## 11. Fallbacks
| Risk | Fallback |
|---|---|
| PIE mapping drifts | 2-anchor offset fit; widen τ to ±2 segments and **show τ on screen**; failing that, use GOLD mode |
| Cosmos slow or rate-limited | Cap the candidates per version at throughput × 30 min. Use 4 keyframes instead of the clip. The live panel verifies top-8 instead of top-12. |
| Vector select fails in vastdb | Skip the Embed1 stretch and use the backend search for vector recall |
| Search returns nothing at min_sim 0.2 | Use 0.1, rank without a threshold, and scope by camera_id (dry-run lesson) |
| The 13:45 test run doesn't finish | Report the dev numbers **labelled "dev"**, or report test on the v1 subset that finished |
| VastDB table not writable | Parquet to the S3 segments bucket prefix `assay/`, queried with the vastdb SDK or DuckDB |
| W&B Inference down | Fixed paraphrase list. Tuner runs as a hand-written v2 prompt, and we say so. |
| /app deploy fails | Run uvicorn on the VM and demo from the VM browser |
| A confirmed I-24 hit appears | Show it. "Here's the 1 of N. It's a {sign/pole} at 300 ft." Report specificity honestly. |
| Live query hangs on stage | Replay the recorded 15:35 live run and say so |

---

## 12. Judge Q&A
1. **"VSS 3.3 search already confirms and rejects clips. What's new?"** VSS decides about the clips it was shown. ASSAY measures how often those decisions are right, against external labels with a negative control, and measures what was never shown (the recall ceiling). In production we'd happily call VSS's verifier and audit it the same way.
2. **"PIE labels intention. Does the label match your query?"**
   - We chose queries that map one-to-one onto annotated fields: crossing == 1 with in-path frames, not-crossing pedestrians, and gesture labels.
   - Tolerance is declared, and we show strict vs lenient.
   - Pedestrians PIE didn't label are audited and reported separately. They stay counted as FPs.
3. **"Did you tune on the test set?"** No. The split is by video. v2 was chosen on dev and frozen at 13:45, and test was run once per version. The Weave timestamps show the order.
4. **"Does this scale to a fleet: 10k hours, 7M segments?"**
   - Recall is vector search plus a pushdown scan on VastDB, which takes sub-seconds and needs no GPU.
   - GPU cost scales with candidates, not hours. The meter shows calls per footage-hour, and the tuning gain lowers it.
   - Verify calls are stateless and batch horizontally across CoreWeave endpoints.
5. **"Why VAST instead of S3 + pgvector + Voxel51?"** Video, captions, vectors and the mined scenario table all live in one system, and the full slice pull with pushdown is what makes recall measurable. Re-ingesting with a better prompt is one DataEngine call. There's no ETL between the object store, the vector DB and the warehouse.
6. **"Who buys this, and how do you get the first customer?"**
   - Buyer: AV/robotics scenario-curation leads.
   - Wedge: open-source the eval harness ("measure your video search") and sell the managed miner with a precision SLA.
   - Channel: the VAST AI OS and the NVIDIA Physical AI Data Factory partner ecosystem.
   - First design partners: mid-stage AV/ADAS and delivery-robot companies with large drive archives `[A]`.

---

## 13. Pivot plan: NIGHTSHIFT + VOID (only if the §6 tree selects it at 10:45)
- **What it is:** "git diff for a street." Diff 2026-09-02 against 2026-09-01 on Pack D, hour by hour. Cosmos verifies only the top-20 differences, and only verified differences get surfaced.
- **Numbers on screen:**
  - segments scanned → flagged → confirmed
  - **precision n of 20** (two-person blind label)
  - suppression ratio
  - VOID I-24 FP rate (unchanged from ASSAY)
- **Reuse:** `verify.py`, `score.py`, Weave, the UI shell (the barcode becomes a two-day timeline) and the VOID wall. New code: `nightshift/diff.py` (stubbed tonight). Roughly 60 Cosmos calls in total.
- **Wording:** a literal two-day diff. Never "anomaly detection" (n = 1).
- **Privacy:** real residents, so blur faces and plates in screenshots and never identify anyone.
- **Plan shift:** the hour plan keeps its shape. 10:45–12:00 becomes D row pull + capture-hour binning, and the tuning slot becomes the hand-label slot.
