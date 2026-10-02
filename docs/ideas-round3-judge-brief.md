# Round 3: ideas for the judge brief ("interesting · uses the services provided · amazed")

Context: [JUDGE-BRIEF.md](JUDGE-BRIEF.md) (13-service scorecard). Ideator round 3, 2026-10-02.

## Facts that shaped the ideas
- **No documented audio in any pack**, so Canary-1B hears the *judge's voice*, not the footage. Confirm with `ffprobe` at 10:05.
- **Only Pack A is guaranteed multi-camera.** Files are `scene*_p*c*`, 16–17 cameras per scene on the same 60–90 s window, with clocks skewed 0.1–1 s. SDG multi-camera needs run IDs in filenames (unverified).
- **Free ground truth comes from dataset structure:**
  - I-24 has no pedestrians.
  - Scenes are: 1 free-flow, 2 snow, 3 stop-and-go.
  - The I24-3D paper lists 8 trailer vehicles in Scene 1 and 6 in Scene 3.
  - SDG near-miss clips end in a dodge.
  - PIE labels need the G2 mapping.
- **Platform traps:**
  - Re-ingest works on whole chunks, keeps no record of the original prompt, and has no cancel.
  - Never write `segments*.mp4` to the buckets yourself (that fires the trigger); use `videos/upload`.
  - The Reasoner sees YOLO class names, so YOLO errors leak into captions.
  - GPUs are shared, so cache everything for 17:00.

## Candidates (score = Interesting / Services / Amazement)

| Rank | Idea | One-liner | 20-second "amazed" moment | Services | Score |
|---|---|---|---|---|---|
| 1 | **ARGUS** | Sixteen fixed I-24 cameras become one virtual follow-cam, directed by voice | Judge: "follow the pickup with the trailer." The 17-tile wall lights the 5–6 cameras that see it, a relay hops pole to pole, then a close-up follow-cam is cut, uploaded and re-described. The same request on Scene 2 (snow) finds nothing. | 13/13 | 9/10/9 = 28 (high build risk) |
| 2 | **PERJURY** | A lie detector for claims about video: the judge speaks a claim, the agent checks each atomic claim against the pixels | Judge: "Three pedestrians are crossing the highway in the snow." Result: pedestrians CONTRADICTED (YOLO 0 persons, Cosmos "vehicles only"), highway SUPPORTED, snow SUPPORTED. Verdict FALSE with an evidence frame, shown next to the stock `agent/ask` answer. Optional "jury": 16 cameras turn red. | 13/13 | 8/9/9 = 26 (medium) |
| 3 | **REWATCH** | ASSAY, but the agent re-watches what its own index missed: it diagnoses each miss, then rewrites the ingest prompt, zooms in, or raises fps | Red missed ticks flip to green live and the recall ceiling climbs. The judge plays "Prompt Golf" against the agent with their own 800-character prompt. | 12/13 | 8/9/8 = 25 (needs G2) |
| 4 | **HINDSIGHT** | Rewind from an event to the earliest visible cue; mask entities to find the decisive actor (counterfactual) | The scrubber runs backward on yes/no probes and stops next to PIE's own "first looks" tick. One of three masks flips the verdict. | 12/13 | 8/8/8 = 24 (needs G2) |
| 4 | **FOUNDRY** | The judge names a class COCO lacks ("forklift"), and the agent builds a labeled dataset with measured precision | Spoken class → 12 Pack C keyframes boxed (YOLO "truck" + Cosmos "forklift", IoU 0.71) → judge swipes 3 → "47 labels, precision 87% (CI 74–94)" | 13/13 | 7/10/7 = 24 |
| 6 | **ANALOG** | The archive remembers what happened next: Embed1 video-to-video finds 9 twins and their next 5 s autoplay | "6/9 show a pedestrian entering the road vs ~10% base rate" | 12/13 | 7/8/7 = 22 |
| 6 | **LEDGER** | EXPLAIN ANALYZE for video: plan the columns (cheap from YOLO, expensive from Cosmos), run them, answer with SQL plus estimated vs actual cost | "In which scene are the most trucks stopped?" A costed plan, then a chart with sanity ticks | 13/13 | 7/9/6 = 22 |
| 8 | **ARENA** | LAST FRAME with voice, a synced-camera wall, and Cosmos3 and Nemotron as contestants | The judge predicts out loud, models predict, the reveal plays and Weave ranks everyone | 13/13 | 5/9/7 = 21 (collides with LAST FRAME) |
| 9 | ASSAY (incumbent) | Scenario mining graded against PIE labels | Scorecard + VOID wall | ~7/13 | 7/6/6 = 19 |
| 10 | NIGHTSHIFT (incumbent) | Two-day diff on Pack D | — | ~6/13 | 5/6/4 = 15 |
| 11 | LAST FRAME (incumbent) | Pause, predict, reveal | — | ~5/13 | 5/4/5 = 14 |

## Ideator recommendation
**PERJURY, with REWATCH's repair loop as Act 2.** ARGUS has the best raw score but stacks too many risks to land in 6.5 h: tiny far-lane vehicles, 17-way fan-out on shared GPUs, possibly downscaled segments, and the ffmpeg cut. PERJURY has these advantages:
- It needs no PIE mapping and no SDG run IDs.
- Its truth comes from dataset structure.
- It works at a 3-minute table visit and uses all 13 services meaningfully.

The PERJURY plan:
- **Act 2 (repair):** for claims the pixels can answer but the captions can't, the agent drafts an ingest-prompt patch and re-ingests; the stock `agent/ask` then catches the same lie.
- **Cutaway:** ARGUS's 16-camera wall serves as the "jury".
- **Numbers:** catch rate, false-accusation rate and decline rate on a planted-lie bench, plus an A/B against stock `agent/ask`.
- **Expected attack:** sycophancy (VLMs agree with the claim). Answer it with contradiction-first prompting, a YOLO count backstop, and a reported decline rate.
