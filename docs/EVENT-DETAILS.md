# Real-Time Video Agents Hack — Official Event Details

> **Cleanup note (2026-10-02):** some raw captures and docs cited below were moved to [`unwanted/`](../unwanted/README.md) with their paths preserved (e.g. `docs/sources/x.md` is now `unwanted/docs/sources/x.md`). See `unwanted/MANIFEST.tsv`.

Source of truth: **tokens& hackathon portal** ([tokensand.com/vastsf](https://tokensand.com/vastsf), [tokensand.com/vastnyc](https://tokensand.com/vastnyc)), scraped 2026-10-02. Raw scrapes are in `.firecrawl/` and `docs/sources/` (both committed). Where this page and the Luma pages disagree, this page wins (it's the submission portal).

## Links
| What | URL |
|---|---|
| SF hackathon portal | https://tokensand.com/vastsf |
| SF submit (sign-in with Google or email code) | https://tokensand.com/vastsf/submit |
| SF project gallery | https://tokensand.com/vastsf/projects |
| NYC portal | https://tokensand.com/vastnyc (submit: /vastnyc/submit) |
| London portal | **not live yet** (tokensand.com/vastlondon returns 404 as of Oct 2) |
| Discord | https://bit.ly/discord-17 → https://discord.gg/VyhUqgn6pc |
| Luma (SF / NYC / LDN) | luma.com/vastsf · luma.com/vastnyc · luma.com/vastlondon |
| VAST Cosmos Community (**required** for build-env access) | https://community.vastdata.com/?utm_campaign=event26-builders-challenge |
| Video search overview (organizer video, 146 MB mp4 `vss2-blurred-3.mp4`) | https://drive.google.com/file/d/1qUrT0QaBGS6mXxHTEG2vnLM2pT1KY4RD/view |

## What you're building (verbatim intent)
> Build a video agent that searches footage, answers questions, spots events, or takes action. One idea, working by the end of the day.

Organizer guidance:
- **Pick a specific use case** — "flag someone missing a hard hat," not "watch for safety issues."
- **Adapt your idea to the footage available on build day.** (Sample videos are provided; bring-your-own allowed per VAST blog.)
- **Search quality depends on the prompt used to describe each video segment.** You can re-ingest video with a different prompt on build day. → Our Cosmos ingest prompt is a first-class lever.

Linked resources on the portal: Video search overview (Drive video), YOLO11 docs (docs.ultralytics.com/models/yolo11), CoreWeave GPUs, **ARIA research agent** (CoreWeave Forge — AI Research & Iteration Agent; analyzes experiments, proposes next run, launches with approval).

## What to submit ⚠️
- **A public GitHub repository** ← our repo is currently **private**; flip to public before submitting.
- **A short demo video with a shareable link** ← record it before the deadline; demos happen *after* submissions close.
- What you built and the tools you used
- Team names and contact emails
- Optional: working website, project screenshot
- Must be built during the event. One project per team, up to 4 people.
- New tokens& builder profiles are public by default (can be made private in Profile).

## Schedule
| | SF — Fri Oct 2 (PT) | NYC — Fri Oct 9 (ET) |
|---|---|---|
| Doors + breakfast | 9:30 AM | 8:30 AM |
| Opening keynotes | 9:30 AM | 9:00 AM |
| Build begins / submissions open | 10:00 AM | 9:30 AM |
| Lunch | 1:00 PM | 12:30 PM |
| **Submission deadline** | **4:30 PM** | **4:30 PM** |
| Demos | 5:00 PM | 5:00 PM (per Luma; verify) |
| Closing & awards | 7:00 PM | ~6:30 PM (Luma says event ends 6:30) |

**Effective build window: SF 6.5 h (10:00–16:30), NYC 7 h (9:30–16:30), including recording the demo video.**
London: Sat Oct 17 — portal not published yet; Luma has 8:30 doors.

## Before you arrive (checklist)
- [ ] Join the **VAST Cosmos Community** — this is how you get access to the VAST build environment.
- [ ] Create a **Cursor** account with your **registration email** (event credits are added to it).
- [ ] Create a **Weights & Biases** account (serverless inference + Weave).
- [ ] Join the Discord.
- [ ] Laptop + charger. Physical government photo ID (18+). SF venue is an Amazon building — no scooters/bikes, no parking.
- [ ] ⚠️ **Build-environment access is limited to the first 100 attendees to arrive.** Arrive at doors-open.

## Prizes
- **1st place: NVIDIA DGX Spark™**
- **2nd place: Hugging Face Microduck**
- Two teams win overall prizes. Credits and gift cards are split among all team members. (Luma also lists Cursor credits + cash gift cards.)

Judging (VAST blog): **creativity, technical implementation, real-world impact.**

## Tech partners & resources (as listed on the portal)
- **VAST Data** — VAST AI OS powers video ingestion and keeps vectors, metadata, and video together. [AI OS](https://www.vastdata.com/platform/ai-os) · [Video search example blog](https://www.vastdata.com/blog/unlock-video-intelligence-build-real-time-video-search-and-ai-summary) · Cosmos Community.
- **SpaceXAI (Cursor)** — build in Cursor; sign up with registration email for credits. (On this event, "SpaceXAI" = the Cursor sponsor slot.)
- **CoreWeave (Weights & Biases)** — CoreWeave provides GPUs; W&B provides serverless inference, experiment tracking, observability. [Inference docs](https://docs.wandb.ai/inference) · [Weave](https://wandb.ai/site/weave/).
- **NVIDIA** — video search stack uses **VSS Blueprint** + **Cosmos** to turn segments into searchable descriptions and embeddings. [VSS docs](https://docs.nvidia.com/vss/latest/) · [Cosmos](https://www.nvidia.com/en-us/ai/cosmos/).

## Judges
- **SF:** Hassan Moustafa (NVIDIA, TME Multimodal AI) · Adam Ryason PhD (NVIDIA, Product) · Ram Bansal (VAST, Sr Dev Advocate) · Brian Verkley (VAST, Dir. AI Data Platform) · Anushrav Vatsa (CoreWeave, SA / Physical AI Lead) · Arnav Verma (SpaceXAI, Field Eng)
- **NYC:** Diego Garzon (NVIDIA, Sr SA AI/AV Sim) · Ravi Garg (NVIDIA, SA) · Ram B. · Brian Verkley · Prashanth Nalubandhu (CoreWeave, Staff AI SA) · Brandon Kates (CoreWeave, Founding FDE) · Vera A. (W&B, Sr SA)
- **London:** Abubakr Karali (NVIDIA) · Ram B. · Brian Verkley · Junaid Butt (W&B)

## Implications for UNWATCHED (see FINAL-IDEA.md)
1. **Deadline is 4:30, not 5:00** — the build plan must end coding by ~15:45 to record the demo video and submit.
2. **Demo video is mandatory** — record the two-proof demo (overnight digest + live camera #5) as a backup video anyway; that video *is* the submission.
3. **Public repo** — make `nihalnihalani/vast-builders-challenge` public (and scrub `.env`/keys) before submitting.
4. **Specific use case wording** — organizers explicitly reward specificity; pitch UNWATCHED as one concrete job (e.g., "flag after-hours removal of equipment from a stockroom nobody watches"), not "anomaly detection."
5. **Ingest prompt is tunable** — the Cosmos description prompt controls what's searchable/scorable; design ours for the anomaly scorer.
6. **First 100 get build env** — arrive early.
