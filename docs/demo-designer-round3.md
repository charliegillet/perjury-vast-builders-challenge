# Round 3: demo-designer scores (judge brief: "prepared to be amazed")

| Idea | Amazement | Demo-ability | Services visibly firing (V/partial/badge) | Biggest stage risk |
|---|---|---|---|---|
| ARGUS | 9 if it lands, 6 risk-adjusted | 4 | 7/3/3 | Re-ID errors visible to NVIDIA judges who know AI City multi-camera tracking; a free target can't be fully cut at the table |
| **PERJURY** | **8** | **7** | **9/1/3** | A confidently wrong verdict on a judge-chosen claim |
| REWATCH | 7 | 5 | 6/4/3 | G2 is unresolved; re-ingest stalls; it reads like ASSAY |
| HINDSIGHT | 7 (8 when cached, 5 live) | 5 | 5/2/3 | Masks may not flip the verdict live |
| FOUNDRY | 7 | 7 | 9/1/3 | The payoff is a precision number; Pack C identity |
| ASSAY | 5 | 8 | 5/4/3 | The judge sees a scorecard, not a moment; ~30 s of dead air |

**Recommendation:** PERJURY with ARGUS's tile wall as a live "jury", plus a **service ribbon** showing all 13 services, plus Exhibit A (an auto-cut evidence clip uploaded via `videos/upload`). The REWATCH appeal is a conditional, cached beat. Cut HINDSIGHT, FOUNDRY and the full ARGUS relay.

**Service ribbon:** a persistent 13-chip dock in 4 lanes (DATA / MODELS / AGENT / PLATFORM).
- Chips have four states: idle, firing (live ms), done (ms, ×n calls), fallback.
- Clicking a chip opens the real request/response JSON with tokens redacted.
- A Weave-style trace waterfall sits above the dock, and each case ends with a receipt: "9 of 13 services fired · 23 calls · 4.1 s".
- Cursor, CoreWeave and K8s are honest badges (skills invoked at runtime, GPU-seconds meter, pod `/healthz` + QR code). Never fake a chip.

**Hero:** Pack A Scene 2 (snow). Claim: "Three pedestrians are crossing the highway in the snow."
- highway: SUPPORTED
- snow: SUPPORTED in 16/16 Scene 2 cameras only
- pedestrians: CONTRADICTED (YOLO 0 persons, Cosmos "vehicles only")
- crossing: MOOT
- "pedestrians" is struck through in red. ~4 s to the first pill, ~8 s to the full verdict; budget ×2 at 17:00.

**Mitigating the main risk:** only route claims about YOLO-class presence/absence/count, scene condition (snow, free-flow, congestion) and semi/trailer to a hard verdict. Everything else returns "UNVERIFIABLE from these pixels", with the decline rate shown. Use contradiction-first prompts, and never let Cosmos3 override a YOLO count of 0.

**Preflight by 10:45:**
- G1: mic → Canary in ≤1.5 s over HTTPS from the laptop browser
- G2: filenames map to scene/pole/camera (49 cameras)
- G3: Cosmos3 yes/no latency at 8-way concurrency
- G4: sycophancy check, 10 planted lies vs 10 truths, ≤20% pass
- G5: does stock `agent/ask` fall for the hero lie?
- G6: `videos/upload` round trip

The scripts (table-side 3:00, stage 3:00, video 2:00 with the gasp at 0:08) are in the demo-designer report in the session transcript. The orchestrator-judge folds them into the final plan.
