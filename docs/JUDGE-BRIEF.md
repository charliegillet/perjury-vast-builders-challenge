# Judge brief, round 3 north star

> "There are many pre-ingested videos to build agents and apps around.
> The winning submission will be something that is **interesting** and something that **uses the set of services provided**.
> I am **prepared to be amazed**."

## Reading the brief
1. **Interesting:** novel, surprising, and memorable in one sentence. Not "search + summary", which is the stock UI, and not "near-miss dashboard", which the organizers' own playbook already suggests.
2. **Uses the set of services provided:** breadth *and* depth across the stack the organizers deployed. Every service should do real work, not appear as a logo on a slide.
3. **Amazed:** a demo moment the judges haven't seen before, live, on the pre-ingested footage.

## The set of services provided (scorecard)
From the official starter kit (`.firecrawl/starter-repos/official-vast-data/`, docs/OFFICIAL-STARTER-KIT.md):

| # | Service | What "real use" looks like |
|---|---|---|
| 1 | **VAST S3 buckets** (chunks + 5 s segments) | Fetch segments directly, write artifacts back |
| 2 | **VAST DataEngine pipeline** (Segmenter → YOLO → Cosmos3 → Embed1 → VastDB writer; scheduled prompt-suggester; event broker) | **Re-ingest** with a custom prompt (≤800 chars) and **upload** new video, driven by our agent. No custom function deploys. |
| 3 | **VastDB** (segment rows: captions, 256-d text + visual vectors, YOLO classes/counts, metadata) | `vastdb` SDK pushdown queries, vector SQL, writing our own tables |
| 4 | **VSS backend APIs** | `search`, `agent/ask`, `agent/search-and-answer`, `videos/synthesize`, `videos/stream`, `videos/detections`, `dashboard/stats`, `suggestions`, `dashboard/reingest`, `videos/upload` |
| 5 | **NVIDIA Cosmos3-Reason** (direct `/v1/chat/completions`, video in) | Reasoning, verification, 2D grounding, chain of thought |
| 6 | **NVIDIA Cosmos-Embed1** (direct `/v1/embeddings`, text *and* video) | Video-to-video similarity, custom indexes |
| 7 | **YOLO11** (direct `/v1/infer`, per-frame boxes) | Geometry, counts, tracks |
| 8 | **NVIDIA Canary-1B** (ASR and speech translation; **not wired into the pipeline**) | Voice in, audio transcripts, translation. This is the most under-used service. |
| 9 | **W&B Inference** (Nemotron 3.5 Lightning / Nemotron 3 Ultra / others) | The agent's own reasoning, planning, tool use |
| 10 | **W&B Weave** (traces, evals, leaderboards, feedback) | Every agent step traced; measured quality |
| 11 | **CoreWeave GPUs** (where every model runs) / **ARIA** research agent | Cost and throughput on screen; ARIA if accessible |
| 12 | **Cursor** (agent CLI + skills on the VM) | Built with it; skills reused by our own agent |
| 13 | **Team K8s deploy** (`deploy-app-no-registry` → `/app`) | A live URL judges can open |

## Hard constraints (unchanged)
- **Infrastructure:** a browser VM, a pre-deployed stack, and no custom DataEngine functions.
- **Timing:** build runs 10:00–16:30. Submit a public repo and a demo video by 16:30. Judges visit each table first, then stage demos are at 17:00.
- **Corpus** (docs/corpus/):

  | Pack | What it is |
  |---|---|
  | A | I-24, 3 scenes × ~16 overlapping cameras, no pedestrians |
  | B | PIE dashcam, ~8 h, 1,842 labeled pedestrians |
  | C | Synthetic SDG warehouse: near-miss, fire/evacuation, shelf hit, pickup; 5–10 synced cameras |
  | D | Real neighborhood camera, 2 days |
  | E | SF streets, maybe not ingested |
  | F | Synthetic indoor people flow |

- **Known stack behaviour:** relevance runs around 0.2, captions are generic, re-ingest can stall with no cancel, and YOLO has no forklift/fire classes.

## Incumbent candidates to beat
- **ASSAY** (docs/FINAL-IDEA-v2.md): scenario mining graded against PIE labels with an I-24 negative control. It is rigorous, uses about 7 of the 13 services, and its wow comes from numbers.
- **NIGHTSHIFT** (FINAL-IDEA-v2 §13): a two-day diff on Pack D.
- **LAST FRAME** (docs/LAST-FRAME.md, `lastframe/`, another team member's active build): pause before a transition, the viewer predicts, then reveal. It is a training-quiz loop.
