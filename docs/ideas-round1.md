# Round 1 — Ideator candidates (8)

1. **BLACKBOX** — postmortem-as-a-service for physical incidents. VastDB snapshots = "what did the system know 4 min before the alert"; Kafka alert stream fused with video segments; Weave-traced postmortem doc. Risk: snapshot semantics on-site.
2. **RECALL COURT** — multi-phone pickup-game highlight reels; cross-camera player re-id (jersey OCR) + entity graph over VastDB; ffmpeg auto-cut. Risk: re-id brittle, weak sponsor-feature flex.
3. **FOREMAN** — jobsite PPE agent that never cries wolf. Live webcam → YOLO gate → Cosmos-Reason2 verify → Slack alert with frame+bbox; live false-positive-suppressed counter. Risk: live ingest plumbing.
4. **GHOST SHIFT** — loss-prevention investigator agent; visible plan→replan loop; entity graph + SQL join of video rows with a badge-log table. Risk: re-id + many moving parts.
5. **GRAYBEARD** — palletizer that explains + fixes itself; Cosmos CoT + 2D grounding → MCP corrective command → retry; Weave success-rate eval. Risk: hardware; re-skin of Cosmos Cookoff winner.
6. **NIGHT WATCH** — the archive that watches itself. Push-not-pull: every new segment scored vs rolling "normal" embedding baseline in a DataEngine function; Cosmos only on outliers; unsolicited morning digest to Slack. Risk: noisy anomaly thresholds.
7. **DEPOSITION** — SQL over security footage → court-ready exhibit packets with bbox burned in (DuckDB/ADBC over VastDB). Risk: dry demo.
8. **LOADING DOCK** — ingest from legacy NVR network shares via NFSv4 triggers / Kafka, no S3; Catalog-as-table. Risk: NFSv4 triggers unverified.

Ideator ranking: NIGHT WATCH > BLACKBOX > FOREMAN > LOADING DOCK > GHOST SHIFT > DEPOSITION > RECALL COURT > GRAYBEARD.
