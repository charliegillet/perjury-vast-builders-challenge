# Round 1 — Devil's advocate verdicts

Verified prior art:
- NVIDIA ships `vss-alert-verification` (NGC microservice, VSS 3.0 docs): detector → VLM verify → enriched alert. = FOREMAN, pre-built.
- PPE + VLM compliance alerting is a productized Metropolis use case (Grid Dynamics).
- Push-not-pull unsolicited archive digest: academic prior art (LAVAD CVPR'24, VERA) but **no shipped product**. Genuinely open.

| Idea | Verdict | Why |
|---|---|---|
| BLACKBOX | FIX-THEN-PROCEED | Snapshot granularity unverified; if bucket-level only it degrades to a WHERE clause. Test in first 30 min. |
| RECALL COURT | KILL | Jersey-OCR re-id breaks live; weak sponsor flex; "why not Hudl". |
| FOREMAN | KILL (standalone) | Re-skin of NVIDIA's own alert-verification NIM; live RTSP risk. |
| GHOST SHIFT | KILL | 3–4 chained unverified subsystems. |
| GRAYBEARD | KILL | Needs hardware; collides with Cosmos Cookoff winner. |
| NIGHT WATCH | FIX-THEN-PROCEED | Most differentiated; risk = noisy baseline. Mitigate: curated footage, live suppression counter, 45-min tuning timebox + percentile fallback. |
| DEPOSITION | KILL (standalone) | Dry; steal SQL/exhibit-packet as secondary evidence feature. |
| LOADING DOCK | KILL | All-or-nothing on unverified NFSv4 triggers; plumbing, not an agent. |

Crowding: 4–6+ teams will build detector + VLM verify + alert. NIGHT WATCH and BLACKBOX least likely duplicated.

**Merge:** NIGHT WATCH + FOREMAN's verify step → "the archive that watches itself, and doesn't cry wolf." Baseline scorer = cheap gate; Cosmos-Reason2 verifies before anything hits the digest; live suppression counter. BLACKBOX = backup pitch only.
