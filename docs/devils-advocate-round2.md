# Round 2: devil's advocate verdicts (corpus-grounded)

| Idea | Verdict | Corpus-grounded reason |
|---|---|---|
| NIGHTSHIFT | **FIX** | One baseline day (n=1) means it's a diff, not anomaly detection. Peak-concurrent YOLO counts are flat noise when cars are parked. Re-ingest can't cover ~34k segments. Hour-of-day needs a capture time we can recover (search filters on upload time). Overlaps the Key events list and VSS alert verification. |
| SCENARIO MINER | **FIX (gated bonus)** | The only idea with real ground truth. PIE annotations are zips (`set_video_object`, per-video frames). Mapping VAST's 5 s segments to PIE frames may drift if VAST concatenated the sets. Needs internet access from the VM. RefAV (CVPR 2026) validates scenario mining, and off-the-shelf VLMs score low, so pitch "measured baseline + prompt tuning". |
| QUORUM | KILL | Pack A has no people or crashes, so quorum is trivially true on generic traffic. Its headline result is really VOID's. |
| EVAC-CLOCK | KILL | Run IDs probably aren't in filenames; fire renders at low fidelity. Expect 3+ teams on fire/evacuation. |
| LOOKALIKE | KILL | A feature the platform already has (hybrid video vectors). ~0.2 relevance looks random. |
| ANCHOR | KILL | A dashboard, and the organizers already ship the anchor query and the Dashboard tab. |
| VOID | **Bolt-on** | Pack A is the only negative set with labels (zero pedestrians). Eyeball the hits before reporting a rate. |
| HEARSAY | **Bolt-on if audio exists** | Check with ffprobe in minute 5. Kill it if there's no audio. |

**Crowded (5+ teams likely):** Pack C near-miss board, the "person near vehicle" anchor query, fire/evacuation, PPE prompts, Pack F occupancy, cross-pack dashboards.
**Uncrowded:** Pack D diffing, PIE with real labels, Canary, Pack A negatives.

**Recommendation:** NIGHTSHIFT reframed as a *literal two-day diff* ("what changed between the two days", not "anomaly"). Hand-label the top-20 flagged segments and report precision ("n of 20 confirmed"), report the ratio scanned vs surfaced, and add VOID for the false-positive rate on I-24.
- **New gate:** capture time is recoverable from filenames/metadata, the two days visibly differ, and vastdb-read returns D's rows.
- **In parallel:** spend 20 minutes checking whether segments map to PIE frames. If they do, **SCENARIO MINER + VOID** (PIE positives + I-24 negatives = real precision/recall) becomes the stronger primary.
- Pre-write the PIE parser tonight.
