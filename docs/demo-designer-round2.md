# Round 2: demo-designer scores (corpus-grounded)

| Rank | Idea | Demo | Hero moment | Looks like the stock VSS UI? |
|---|---|---|---|---|
| 1 | QUORUM | **8** | A 16-camera wall flips tile by tile to "14/16 agree", then the judge types "person near vehicle" and gets **0/16** | No |
| 2 | SCENARIO MINER | **7** | A drive "barcode": 519 PIE ground-truth ticks turn green or red, with a recall/precision scorecard and the gain from prompt tuning | No |
| 3 | NIGHTSHIFT | 6 | A two-day diff timeline and suppression counter; depends on Pack D having events | Partly |
| 4 | EVAC-CLOCK | 5 | A fire timeline across 5 cameras | No |
| 5 | LOOKALIKE | 4 | A grid of similar clips | **Yes** |
| 6 | ANCHOR | 4 | A per-pack calibration table | **Yes** (reads like the Dashboard) |
| 7 | VOID | 4 alone / 8 bolted on | "Hallucinated K of N on empty I-24" | No |
| 8 | HEARSAY | 4 | Voice query (audio likely absent) | No |

- **Most credible numbers:** SCENARIO MINER (graded against external labels, plus the gain from tuning).
- **Most dramatic single glance:** QUORUM's 0/16.
- **QUORUM is fully live:** one search call (1.2 s embed + 0.26 s search), voting done in the browser, no LLM on the critical path.
- **SCENARIO MINER:** the labels are baked into the repo, and the before/after tuning is shown as a recorded run (re-ingest stalls).
- **Gates:** QUORUM needs scene/camera in the filenames and a score that separates hits from a null baseline. SCENARIO MINER needs the PIE frame offset in segment metadata.
- **Submission video:** freeze at 15:30, record 15:45–16:15, record from a cached run, and say "live" only for the parts that are live.
- **First-30-minutes checklist:** `list-metadata` (A: scene/camera; B: set/video/offset), `vastdb-read` for A/B/D, one Cosmos3 yes/no timing, egress curls, PIE ground-truth JSON baked into the repo.
