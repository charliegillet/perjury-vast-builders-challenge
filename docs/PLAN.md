# PLAN: PERJURY, built to the judge's brief

> **Status (2026-10-03):** the SF event was Oct 2, so this targets the next one. NYC is Fri Oct 9 (doors 8:30, build 9:30–16:30 ET). London is Sat Oct 17 (its portal isn't live yet). The SF clock times in [FINAL-IDEA-v3.md](FINAL-IDEA-v3.md) shift 30 min earlier for NYC.
> **Nothing is built yet.** This plan says what to build, in what order, and how each part answers the brief.
> Sources: [JUDGE-BRIEF.md](JUDGE-BRIEF.md), the full spec in [FINAL-IDEA-v3.md](FINAL-IDEA-v3.md), and the evidence in [REUSE-FROM-UNWANTED.md](REUSE-FROM-UNWANTED.md).

## 1. The brief, and our answer to each word

> "There are many pre-ingested videos to build agents and apps around. The winning submission will be something that is **interesting** and something that **uses the set of services provided**. I am **prepared to be amazed**."

| Brief | Our answer |
|---|---|
| **Interesting** | **PERJURY: every claim about the footage takes the stand.** You *say* something about the video. An agent splits it into atomic claims, cross-examines each one against the pixels using the cheapest witness that can settle it, and rules SUPPORTED, CONTRADICTED, or *"the pixels can't tell."* It also cross-examines the stock VSS agent's own answers. Nobody else will build a court for video claims. |
| **Uses the set of services provided** | All **13 services do real work**, and each one lights up on screen as it fires (§3). Two of them aren't on the verdict path: DataEngine (repair re-ingest and exhibit upload run in the background) and CoreWeave (a measured GPU meter, not a call). Every receipt says honestly which chips fired. |
| **Amazed** | A judge speaks a sentence. Sixteen highway cameras deliberate on screen like a jury. The verdict lands with evidence boxes, and the same sentence flips from TRUE to FALSE when the scene changes. Then the judge's own Cursor agent calls PERJURY as a tool. |

## 2. The demo in three acts (≈3 min)

**Act 1: Testimony (voice → verdict).**
- The judge says *"Three pedestrians are crossing the highway in the snow."*
- Canary transcribes it, and Nemotron splits it into atoms: `pedestrians` · `crossing` · `highway` · `snow`.
- Results:
  - **highway:** SUPPORTED (VastDB metadata).
  - **snow:** SUPPORTED, by a 16/16 camera quorum (Cosmos3, pre-run).
  - **pedestrians:** CONTRADICTED. YOLO finds 0 people in any segment, and the jury agrees.
  - **crossing:** MOOT.
- **The red strike-through on "pedestrians"** is the first gasp.

**Act 2: The jury (YOLO can't settle this one).**
- *"A pickup is towing a trailer."* COCO has no trailer class, so a jury of six cameras watched by Cosmos3 decides.
- Embed1 chooses which moments go before the jury, and YOLO zoom-checks each "yes" on a 4K crop.
- **Scene 1 (free-flow):** TRUE.
- **Same sentence, Scene 2 (snow):** FALSE. The I24-3D paper lists trailers in Scenes 1 and 3 only, so the ground truth is free.
- **The tiles flipping as the scene changes** is the second gasp.
- Close Act 2 with *"…and the truck braked hard"*, which gets UNVERIFIABLE and the reason ("temporal claims are below what any model can judge from these pixels"). The honest decline builds trust.

**Act 3: The witness stand (it audits the stock agent, then becomes a tool).**
- Ask the stock VSS `agent/search-and-answer` the same question. Its answer is split sentence by sentence, and PERJURY rules on each one next to it.
- Then, in the **Cursor agent CLI on the VM**, someone types *"is it true that a pickup tows a trailer on I-24 scene 1?"* Cursor loads our `perjury-verify` skill and calls PERJURY, and the verdict comes back in the terminal.
- **"Any agent can now ask before it answers."** That's the third gasp.
- The receipt shows *"13 of 13 services · 31 calls · 7.8 s · 41 GPU-s"* (real numbers only).

## 3. All 13 services, with real work, and where each shows on screen

| # | Service | Real work in PERJURY | Visible as | When |
|---|---|---|---|---|
| 1 | **VAST S3** | Presigned GET of 5 s segments for keyframes and 4K crops. Writes exhibit JSON under `perjury/` (never `segments*.mp4`). | Ribbon chip → request JSON | Act 2, live |
| 2 | **VAST DataEngine** | **(a) Repair re-ingest:** for a claim type the captions never mention (e.g., "trailer"), the agent writes a ≤800-char prompt patch and re-ingests **one** chunk. We fire it in the morning, before the 11:15 cutoff. On stage, stock search now finds trailers it missed. **(b) Exhibit A:** the evidence reel goes back in via `videos/upload` and the pipeline re-describes it. **(c)** The scheduled prompt-suggester's "key events" are cross-examined as witnesses. | Chip turns "indexed ✓"; before/after search panel | Act 3; background job finishes before the demo |
| 3 | **VastDB** | T0 pushdown on `vss-collection` (classes, counts, metadata, captions, `processing_time`). Vector SQL on `vectors_visual` for jury retrieval. Writes our own **`perjury_verdicts`** table, queried live. | Chip; a SQL row in the Witness tab | Act 1, live |
| 4 | **VSS backend APIs** | `agent/search-and-answer` + `agent/ask` (the witness under cross-examination), `videos/synthesize`, `videos/detections` (sidecar boxes), `videos/stream`, `suggestions`, `dashboard/stats`, `dashboard/reingest`, `videos/upload` | Chip; A/B split screen | Acts 1–3 |
| 5 | **Cosmos3-Reason** | The jurors: neutral, contradiction-first probes on 2×2 keyframe grids, then **2D grounding** boxes on each "yes" | Tiles turning green or red; boxes on exhibits | Act 2, live |
| 6 | **Cosmos-Embed1** | **Text→video:** finds the 6 moments most likely to *prove* the claim, so a CONTRADICTED verdict faces the hardest evidence. **Video→video:** from Exhibit A, finds look-alike moments in other packs ("where else does this happen?"). | Chip; "jury selected by Embed1" label | Act 2, live |
| 7 | **YOLO11** | Zoom-check: a 4K crop around Cosmos's box must contain a car or truck, or the vote is thrown out. T0 also reads the pipeline's own YOLO classes and counts. | Chip; "zoom-checked ✓" on each juror | Acts 1–2 |
| 8 | **Canary-1B** | **Testimony ASR**, and **translation** if the endpoint exposes it. A Spanish or German claim gets ruled on in English. It's the stack's most under-used service, and here it *is* the input. | Waveform → transcript; chip | Act 1, live |
| 9 | **W&B Inference** | **Nemotron 3.5 Lightning:** splits claims into atoms, labels captions (T1), splits the stock agent's answers into sentences. **Nemotron 3 Ultra:** offline bench error analysis that proposes router changes. | Chip; atom pills | Every act |
| 10 | **W&B Weave** | `@weave.op` on every step; the 47-claim **bench** as a Weave Evaluation (lies caught / true claims wrongly accused / declined, jury-size curve, stock-agent A/B); judge 👍/👎 → Weave feedback | Trace waterfall; Bench tab leaderboard | Every act |
| 11 | **CoreWeave GPUs** (+ARIA) | Every model runs here. We **meter it**: GPU-seconds and calls per verdict from measured latencies, plus a cost-per-verdict line. If ARIA is reachable, point it at the Weave bench runs and show the next experiment it proposes. | Meter on the receipt; ARIA panel only if real | Every act |
| 12 | **Cursor** | Built with the `agent` CLI and starter skills. **Real runtime use:** (a) our agent loads the starter `SKILL.md` files as its tool docs; (b) we ship a `perjury-verify` skill so **a Cursor agent calls PERJURY as a tool** (Act 3). | Terminal split-screen in Act 3 | Act 3, live |
| 13 | **Team K8s deploy** | The app runs at `/app` via `deploy-app-no-registry`. Its pod name and `/health` show on the chip, and a QR code lets judges open it on their phones (read-only, to protect the shared GPUs). | Chip; QR code | Always |

**Honesty rule:** a chip lights only if that service did work for *this* verdict. Clicking a chip shows the real request and response, with tokens redacted. The receipt counts only lit chips. Never fake a chip.

## 4. How we use "the many pre-ingested videos"

| Pack | Role |
|---|---|
| **A, I-24** (3 scenes × ~16 cameras) | The courtroom. The overlapping cameras form the jury. Free ground truth: no pedestrians; Scene 2 is snow; trailers appear in Scenes 1 and 3. |
| **C, SDG warehouse** (stretch) | One extra claim YOLO can't settle: *"The forklift hit the worker"* → CONTRADICTED, because the near-miss scenario ends in a dodge. Run it only if those clips are confirmed on site. |
| **B, PIE** | Bench-only atoms, if the PIE mapping works ("a pedestrian crossed in front of the car"). |
| **All packs** | Embed1 video→video "where else does this happen" from Exhibit A. The Witness tab cross-examines prompt-suggester events from any pack. |

## 5. Why this beats the incumbents
- **ASSAY:** about 7 of 13 services, and its wow is a scorecard. PERJURY has a voice, a jury and a tool call, plus *all* of ASSAY's rigor (the bench, measured rates, a negative control).
- **NIGHTSHIFT:** one camera, sparse footage, and it overlaps the stock Key events.
- **LAST FRAME:** a quiz loop with about 5 services. PERJURY keeps the "judge participates" magic but makes the system, not the human, the one being tested.

## 6. Build plan

### Before the event (pre-build so only the on-site unknowns remain)
Owners and files are in FINAL-IDEA-v3 §13. In short:
1. **Core:**
   - `perjury/cosmos.py`: refactor `src/verifier_backends.py` and **replace its `build_prompt()`**, which asserts the event.
   - `atomize.py`, `router.py` + `claim_types.yaml`, `quorum.py` (with tests), `tiers.py`.
2. **Data and models:**
   - `perjury/vss.py`: pattern from `lastframe/vss.py`; copy it, don't edit `lastframe/`.
   - `index_i24.py`, `media.py` (imageio-ffmpeg), `yolo.py`, `embed.py`, `witness.py`, `exhibit.py`, `repair.py` (writes the prompt patch and runs the re-ingest).
3. **App:** `app/main.py` (FastAPI + SSE) and `app/static/`, using the virtualsheng palette and lightbox. Includes `wav.js` (browser WAV encoder for Canary), the service ribbon, the receipt and a replay mode.
4. **Cursor:** `.cursor/skills/perjury-verify/SKILL.md` and `.cursor/rules`.
5. **Bench:** `bench/claims.yaml` (47 claims), `run_bench.py` (pattern from `src/eval_backends.py`), `stock_ab.py`, `report.py`.
6. **`preflight.py`** for gates G0–G6, and `deploy/` (code and cache ConfigMaps, a Secret built from `/config` without echoing it, `requirements.txt` with imageio-ffmpeg).
7. **Five recorded testimony WAVs** (16 kHz mono), one of them in Spanish.
8. Everything runs on fixtures shaped like the real API responses.

### Event day (NYC times; SF/London = +30 min)

| Time | What |
|---|---|
| 8:30–9:30 | Arrive at doors-open (first 100 get the build environment). VM at `workshop.thecosmoslabs.com`, **select the assigned team**. `git pull` the starter repo, then `git clone` our repo to `~/perjury`. |
| 9:30–10:15 | `python preflight.py` runs gates G0–G6 (reachability and mic, Pack A index, stock agent baseline, trailer false-positive rate on Scene 2, Canary, Cosmos throughput, YOLO noise). **Fire the one repair re-ingest now.** |
| **10:15** | **Decide**, and write the decision as the first line of the README. Trailer fails G3 → hero = snow flip. Cosmos unusable → PERJURY-LITE. Pack A unusable → ASSAY. |
| 10:15–11:30 | The typed path end to end on the VM. Pre-run scene probes on all 49 cameras in the background. Embed1 vectors. |
| **11:30** | **E2E check:** the typed trailer claim → Scene 2 FALSE / Scene 1 TRUE. |
| 11:30–13:30 | Voice path, jury wall, exhibits, ribbon; witness stand + `perjury-verify` Cursor skill; bench pass on **dev**. |
| **13:30** | **Freeze** prompts, thresholds and router; run the **test** split once. |
| 13:30–15:00 | Deploy to `/app`, polish the progressive reveal, rehearse twice. Numbers frozen at 14:45. |
| 15:00–15:40 | Code freeze. Record a live run (it doubles as the replay) and the 2-min video. `submission` skill → `SUBMISSION.md`. |
| 15:40–16:20 | Secret scan → **make the repo public** → **submit** on the tokens& portal (public repo link + video link + what we built and the tools used + team names and emails). |
| 16:30– | Table-side walkthrough (laptop Chrome with the insecure-origin flag for the mic, replay ready), then the stage demo at 17:00. |

## 7. Risks that could kill the "amazed" moment, and the pre-decided answer

| Risk | Answer |
|---|---|
| A judge improvises a claim we can't settle | The router sends it to UNVERIFIABLE with a reason. Hard verdicts only for claim types the bench promoted (catch ≥ 80%, false-accusation ≤ 10%). |
| Sycophancy (Cosmos agrees with whatever it's told) | Neutral, contradiction-first prompts; a quorum across cameras; a YOLO zoom-check. A juror who sees a trailer on Scene 2 is a **measured** hallucination, and we show the rate. |
| Mic is dead over HTTP | Chrome insecure-origin flag on the laptop → VM localhost → recorded file → typed |
| Shared GPU is slow at demo time | Progressive reveal (first pill in ~3 s), 6 → 3 jurors under load, pre-run walls, replay tagged REPLAY |
| Stock agent already rejects the lies (G2) | Same demo, but the pitch changes to "evidence audit: atoms, exhibits, measured rates" |
| Re-ingest stalls | Fire it once in the morning; Act 3's before/after is shown only if it finished, otherwise we cut it |

## 8. The one-sentence pitch
*"Video agents will say anything about your footage. PERJURY puts every sentence on the stand: sixteen cameras, three models and a measured error rate. Any agent can now ask before it answers."*
