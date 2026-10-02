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
| ⭐ [docs/FINAL-IDEA-v2.md](docs/FINAL-IDEA-v2.md) | **Current plan: ASSAY.** Plain-English scenario mining over the PIE dashcam archive, Cosmos3-verified, graded against human labels, with I-24 as a no-pedestrian negative control. Includes the 10:45 decision tree and the pre-build list for tonight |
| [docs/corpus/](docs/corpus/) | What's actually in each footage pack (A–F) plus the organizer overview-video analysis |
| 🚨 [docs/OFFICIAL-STARTER-KIT.md](docs/OFFICIAL-STARTER-KIT.md) | **Read first.** Official starter repo `vast-data/vast-builders-challenge`: browser VM, pre-deployed stack, skills, corpus packs, dry-run lessons, and how UNWATCHED adapts |
| [docs/EVENT-DETAILS.md](docs/EVENT-DETAILS.md) | Official rules: **4:30 PM PT deadline**, submit **public repo + demo video**, join VAST Cosmos Community (build env = first 100 arrivals) |
| [docs/FINAL-IDEA.md](docs/FINAL-IDEA.md) | Locked idea **UNWATCHED** — architecture, demo script, hour-by-hour plan, Q&A (read the corrections banner first) |
| [docs/DEEP-RESEARCH.md](docs/DEEP-RESEARCH.md) | Cited synthesis: what changed, competitors, judges, market, open questions |
| [docs/deep-research/01-technical.md](docs/deep-research/01-technical.md) | Build-day cheat sheet: DataEngine triggers, VastDB vector SQL, Cosmos API, W&B, Slack |
| [docs/deep-research/02-competitive.md](docs/deep-research/02-competitive.md) | Prior art + safe stage wording |
| [docs/deep-research/03-judges-market.md](docs/deep-research/03-judges-market.md) | Judges, organizer, market numbers |
| [docs/TRENDS.md](docs/TRENDS.md) | Web-wide sweep: fast video models, trending OSS (Frigate, Qdrant), launches & hackathon winners — **6 changes to make today** |
| [docs/GEMINI-FALLBACK.md](docs/GEMINI-FALLBACK.md) | Gemini as outage-only fallback verifier; Cosmos vs Gemini benchmarks (VANTAGE) |
| [src/verifier_backends.py](src/verifier_backends.py) | Cosmos + Gemini verifier backends with circuit breaker; [src/eval_backends.py](src/eval_backends.py) runs the Weave comparison |
| `.firecrawl/`, `docs/sources/` | Raw scrapes of every page used |

## Idea

**ASSAY** (current, see FINAL-IDEA-v2): *ask for a driving scenario in plain English; ASSAY pulls every instance from the archive, Cosmos3 verifies each one, and it grades itself against human labels: found, missed, made up.* Previous pick, now the pivot: **UNWATCHED** — the archive that watches itself and doesn't cry wolf. Every new segment is scored against what that camera normally sees; Cosmos-Reason2 verifies outliers before anyone is paged; a suppression counter shows what it chose not to show you; an unsolicited digest lands in Slack.

## Setup

_TBD_
