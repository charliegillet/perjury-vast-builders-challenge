# VAST Builders Challenge 2026

Project repo for the [VAST Builders Challenge 2026](https://www.vastdata.com/lp/vast-builders-challenge) — a three-city technical event series for building production-ready AI systems on AI infrastructure.

## Events

| City | Date |
|------|------|
| San Francisco | Fri, Oct 2, 2026 |
| New York | Fri, Oct 9, 2026 |
| London | Sat, Oct 17, 2026 |

Applications required (space limited); registration closes one week before each event. Register via the Luma pages linked from the event site.

**Partners:** VAST Data, CoreWeave, SpaceXAI, NVIDIA, Weights & Biases

## Start here (teammates)

**New build: [LAST FRAME](lastframe/README.md)** — a video decision trainer built around Packs A–F. Run `python3 lastframe/app.py --port 8787` to try the clearly labeled storyboard demo. The scenario studio connects to the workshop VSS index to author human-reviewed drills from adjacent footage segments. [Idea, corpus fit and demo plan](docs/LAST-FRAME.md).

| Doc | What it is |
|---|---|
| ⭐ [docs/FINAL-IDEA-v3.md](docs/FINAL-IDEA-v3.md) | **Current plan: PERJURY.** Say anything about the footage; each atomic claim goes to the cheapest witness that can settle it (VastDB records, YOLO, captions, or a jury of I-24 cameras watched by Cosmos3), and gets SUPPORTED / CONTRADICTED / "the pixels can't tell" with evidence and measured error rates. Routing table, 13-service roles, bench, gates, hour plan, scripts |
| [docs/FINAL-IDEA-v2.md](docs/FINAL-IDEA-v2.md) | **Fallback: ASSAY.** Plain-English scenario mining over the PIE dashcam archive, Cosmos3-verified, graded against human labels, with I-24 as a no-pedestrian negative control. Includes the 10:45 decision tree and the pre-build list for tonight |
| [docs/corpus/](docs/corpus/) | What's actually in each footage pack (A–F) plus the organizer overview-video analysis |
| 🚨 [docs/OFFICIAL-STARTER-KIT.md](docs/OFFICIAL-STARTER-KIT.md) | **Read first.** Official starter repo `vast-data/vast-builders-challenge`: browser VM, pre-deployed stack, skills, corpus packs, dry-run lessons, and how UNWATCHED adapts |
| [docs/EVENT-DETAILS.md](docs/EVENT-DETAILS.md) | Official rules: **4:30 PM PT deadline**, submit **public repo + demo video**, join VAST Cosmos Community (build env = first 100 arrivals) |
| [docs/deep-research/01-technical.md](docs/deep-research/01-technical.md) | Build-day cheat sheet: VastDB vector SQL, Cosmos API, W&B/Weave (its DataEngine-function and Slack parts were for UNWATCHED) |
| [docs/deep-research/03-judges-market.md](docs/deep-research/03-judges-market.md) | Judges and organizer (its surveillance market numbers were for UNWATCHED) |
| [docs/TRENDS.md](docs/TRENDS.md) | Fast video models: Cosmos3 order, two-step verify, fps, VANTAGE-Bench |
| [docs/GEMINI-FALLBACK.md](docs/GEMINI-FALLBACK.md) | Gemini as an outage-only fallback verifier; Cosmos vs Gemini benchmarks (VANTAGE) |
| [src/verifier_backends.py](src/verifier_backends.py) | Cosmos + Gemini verifier backends with circuit breaker (base for ASSAY's verify step); [src/eval_backends.py](src/eval_backends.py) runs a Weave comparison |
| `.firecrawl/`, `docs/sources/` | Raw scrapes of the pages the kept docs rely on |
| [docs/REUSE-FROM-UNWANTED.md](docs/REUSE-FROM-UNWANTED.md) | 85 files restored from `unwanted/` and what each is for: verify-prompt evidence, Gemini fallback gotchas, Weave/tuner precedent, UI starter, pitch receipts |
| [docs/JUDGE-BRIEF.md](docs/JUDGE-BRIEF.md) · [docs/ideas-round3-judge-brief.md](docs/ideas-round3-judge-brief.md) | The judge's brief ("interesting · uses the services provided · amazed"), the 13-service scorecard, and round-3 ideas (ARGUS, PERJURY, REWATCH…) |
| [unwanted/](unwanted/README.md) | Files not needed for ASSAY (superseded UNWATCHED plan, round-1 ideation, Gemini deep-dives, duplicate or junk scrapes). Paths are preserved, and [MANIFEST.tsv](unwanted/MANIFEST.tsv) gives the reason for each |

## Idea

**PERJURY** (current, see [FINAL-IDEA-v3](docs/FINAL-IDEA-v3.md)): *"Every claim about the footage takes the stand."* Built for the judge's brief: interesting, uses the set of services provided, amazing. Hero claim on Pack A (I-24): **"A pickup is towing a trailer"**, which should come out TRUE on the free-flow scene and FALSE on the snow scene. YOLO can't settle it, so a jury of cameras watched by Cosmos3 does. The I24-3D paper gives the ground truth.
- **Fallback:** ASSAY ([v2](docs/FINAL-IDEA-v2.md)), scenario mining graded against PIE labels.
- **Older ideas:** NIGHTSHIFT and UNWATCHED ([v1](docs/FINAL-IDEA.md)).

## Setup

_TBD_
