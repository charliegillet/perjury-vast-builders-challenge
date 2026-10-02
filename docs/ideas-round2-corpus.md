# Round 2: ideas grounded in the actual corpus (ideator, 2026-10-01)

**Key corpus facts that reframe UNWATCHED:**
- Pack C (synthetic SDG warehouse) is staged 10 s event clips from many runs under one camera_id, so it has **no "normal"**.
- Pack F has **no incidents**.
- **Pack D (two real days, one fixed camera) is the only pack where a learned-normal baseline is honest.** It's up to about 34k segments, so score the existing rows and spend Cosmos only on flagged ones.

| # | Idea | One-liner | Packs | Biggest risk |
|---|---|---|---|---|
| 1 | **NIGHTSHIFT** (sharpened UNWATCHED) | "git diff for a street": diff Sep 2 against Sep 1 hour by hour, push only verified differences, report what was suppressed | D, plus C as a cutaway, plus the live cam | Parked cars dominate YOLO counts; night IR; D may have few events |
| 2 | **SCENARIO MINER** | Plain-English pedestrian scenario mining that exports sim-ready cards and scores itself live against PIE labels; auto-tunes the ingest prompt | B (519 crossings) | Mapping clips to PIE frames; internet access for the labels; re-ingest stalls |
| 3 | **QUORUM** | A claim isn't believed until k overlapping I-24 cameras agree; "person near vehicle" correctly returns 0 | A | Parsing scene/camera from filenames; few events; near-duplicate captions |
| 4 | **EVAC-CLOCK** | Fuse 5 synced ceiling cameras of the SDG fire into an evacuation timeline | C fire runs | Grouping clips by run; fire may be captioned poorly |
| 5 | **LOOKALIKE** | Query by video: cross-pack look-alikes and other angles of the same event (Embed1 video-to-video) | C, B, D, upload | Low similarity scores; modest wow |
| 6 | **ANCHOR** | VAST's anchor query, calibrated per pack against known truth | All | It's a dashboard; "close to" is ambiguous |
| 7 | **VOID** | Hallucination rate on footage that is provably empty (I-24 has no pedestrians) | A, C negatives | Too thin standalone; a bolt-on for specificity |
| 8 | **HEARSAY** | Canary-1B voice queries, plus speech transcripts if audio exists | Any | Clips may have no audio; reads as a gimmick |

**Ideator verdict:** keep UNWATCHED, but only as NIGHTSHIFT on Pack D, with VOID bolted on as free negatives for measuring specificity. Gate it at 10:30: Pack D has ≥10 real non-parked events at night, the two days visibly differ, and vastdb-read returns D's rows. If the gate fails, pivot to SCENARIO MINER. Add Canary voice if the clips have audio.
