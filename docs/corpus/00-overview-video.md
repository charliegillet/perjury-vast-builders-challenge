# What the organizers' overview video shows (vss2-blurred-3.mp4)

- **Source:** https://drive.google.com/file/d/1qUrT0QaBGS6mXxHTEG2vnLM2pT1KY4RD, linked from tokensand.com/vastsf. It's a 2 min 13 s screen recording of the VAST VSS Blueprint UI at 3760×2160 and 60 fps, with the video thumbnails blurred.
- **How it was analyzed:** frames were extracted every 3 s. Contact sheets are in `overview-frames/s_01…s_11.jpg`.

> ⚠️ **This is a demo deployment, not our event corpus.** It shows NYC walking footage: locations jersey-city and 5th–10th ave, cameras `sim1–sim6` and `manh1`, uploaded Jul 5–6 2026, captions from **Cosmos-Reason2-8B**. Tomorrow's stack uses **Cosmos3-Reason** on Packs A–F. What carries over is the **UI, the APIs, what the captions look like, and the pipeline**.

## What we learned, frame by frame

**1. Login and DataEngine console** (`s_01`, `s_02`)
- The login reads "Vast VSS Blueprint — Video Search & Summarization powered by DataEngine".
- The DataEngine dashboard shows **32 functions**. Pipelines include `vss2`, `vss-cosmos2`, `research-assistant`, `fraud-enrichment`, `fraud-detection-ingest-pipeline`, `imaging-engine`, `vastav-engine` and `genomics-pipeline`.
- The `vss2` pipeline graph in the Visual Builder:
  - `vss2-chunks-1` → `vss2-segmenter-4`
  - `vss2-events-3` → `vss2-events-func-9`
  - `vss2-chunks-segments-2` → `detector-10` → `reasoner-6` → `embedder-7` → `vastdb-8`
- Trigger `vss2-chunks-segments` is type **Element / Object Created** on view `vss2-chunks-segments`, with object-key filter prefix `segments`, suffix `.mp4`. Its destination is the event broker view **`vast-broker`**, topic **`vss2-topic`**.
- The trigger list (24) includes **`vss-alerting-schedul…`** (a scheduled alerting trigger already exists), plus `vss-video-segment-la…`, `vss-video-chunk-land…`, `pos-inventory-lake`, `update-vector-db-res…` and others.
- Function deployment settings: concurrency 1–4, CPU 100m–2000m, memory 128Mi–2560Mi, auto-scaling RPS factor 1.

**2. Search tab** (`s_03`–`s_06`)
- **Scope:** All Videos, My Videos or Public Only.
- **Time selection:** All Time, Last 5 min, 15 min, 1 h, 24 h, week, or a custom date/time range.
- **Filters on upload metadata:** Camera ID, Capture Type, Location and Object class.
- **Controls:** Upload, Hide Filters, and **"Reveal Similarity Query"**.
- **Suggestion chips** ("Try something like…", updated every few minutes by the prompt-suggester), e.g. "Truck turning into narrow alley", "Bus stopping abruptly at crosswalk".
- The demo query was *"pedestrian with blue shirt is carrying a suitcase in the intersection"* with 9th-ave, 7/6 08:00–13:00.
- A pipeline animation shows four stages: **Generating Embedding** (hybrid caption + video query vectors, cosmos-embed1 256-d) → **Searching VastDB** (cosine similarity) → **Applying Permissions** (allowed_users, is_public) → **Generating Summary** (Cosmos-Reason2-8B).
- Timings: **Embedding 1229 ms, Search 260 ms, summary 5.25 s, 8,563 tokens** for 3 clips. Expect a ~5 s LLM step in any "ask" flow.
- **"Top 3 Clips — Summary"** card: Answer, **Notable moments with timestamps** (e.g. "0:25–0:30 (Clip 1) …") and **Gaps**.

**3. Clip view** (`s_06`–`s_08`)
- A **match timeline** of six 5-second segments for a 30 s video, plus a **BBOXES on/off** overlay.
- Each segment shows its caption, YOLO class chips with counts (e.g. "29 bench", "30 backpack", "7 motorcycle", "11 truck"), and **relevance %**.
- ⚠️ **Relevance scores are low: 18–25% even for "QUERY HIT" segments.** This confirms the dry-run lesson that a 0.35 threshold returns nothing. Use 0.1–0.2, or rank instead of thresholding.
- Captions are **generic and repetitive** ("A bustling urban street scene with pedestrians walking past outdoor dining areas…"). The **ingest prompt matters a lot**, so re-ingest with a targeted prompt.
- Captions name real-world specifics, e.g. "Nathan's Famous hot dog stand", "Dior store".

**4. Explore tab** (`s_07`, `s_09`)
- "Browse by upload date", filterable by day and location, with video cards (e.g. `nyc_20260706_062215_…mp4`, "6 segments · 0:30") and a **Summarize** button on each video.

**5. Dashboard tab** (`s_09`, `s_10`)

| Section | What it shows (demo numbers) |
|---|---|
| Totals | **367** total rows / segment rows, **77** S3 chunk MP4s, **449** S3 segment MP4s, **67** unique videos, **363** public / **4** private segments, **11** stream sessions, **0** re-ingest rows |
| Ingest quality | Structured JSON parsed 100%, detector coverage 100%, rows with object classes 100% |
| Uploads over time | Segment rows per upload day (07/05: 65, 07/06: 302) |
| Object detection heatmap | Segments containing each YOLO class: person 357, car 315, handbag 264, traffic light 251, truck 225, bicycle 163, backpack 147, bus 123 |
| Upload metadata | Counts by `camera_id` (sim2 161, sim5 90 …), `capture_type` (walk-west 217, walking 92, rain-west 36, walk-fifa-26 18, streets 4) and `location` |
| Key events | **64 events** from the prompt-suggester, each with a short title, a subtitle, the upload time, and the segment file. Examples: "Handbag dropped on sidewalk", "Bicycle avoiding open door", "Pedestrian walking near water's edge", "Woman walking past Dior store", "American flags lining the road". A search icon opens the event clip. |

**6. Event clip modal** (`s_11`)
- The caption carries **structured fields**: `… | Objects: 1028 car, 3097 person, 105 handbag, 12 truck, 2 bus, 682 traffic light | Actions: … | Events: Active public or pedestrian activity`.
- The reasoner's structured JSON includes **objects, actions and events**, not just prose. Those fields are our scorer's second signal.

## Implications for UNWATCHED (and any project)
1. **The UI already has a "Key events" list** built by the scheduled prompt-suggester, and a `vss-alerting-schedul…` trigger exists. UNWATCHED's "unsolicited digest" must be clearly **different**:
   - Key events = an LLM picks "interesting-sounding" captions from recent segments. There's no baseline, no verification, no suppression count and no push.
   - UNWATCHED = **deviation from each camera's learned normal**, a **Cosmos3 verify gate**, a **measured suppression rate**, and **push to a human**.
   - Say this on stage: *"The blueprint's Key Events tells you what sounds interesting. UNWATCHED tells you what's unusual for this camera, and proves it."*
2. **Relevance is low and captions are generic.** Rank, don't threshold. Re-ingest our packs with a prompt that writes what the anomaly scorer and verifier need: who and what is present, counts, what's moving, doors, carried objects, vehicles stopping.
3. **Object counts per segment are already in the row.** Per-camera **count z-scores** (e.g. person count at an unusual time, a stopped vehicle where traffic usually flows) are cheap and explainable, alongside embedding distance.
4. **Expect about 1.2 s to embed, 0.26 s to search, and 5 s for an LLM summary.** For the live beat, call Cosmos3-Reason directly with a short yes/no gate.
5. **Wording judges will recognize:** "Notable moments" and "Gaps" are the UI's summary structure. Mirror it in the digest: *what happened · when · evidence · what we're unsure about.*
