# Corpus 02: Warehouse, Smart Spaces, Neighborhood, and SF Streets (Packs C, D, E, F)

> **Cleanup note (2026-10-02):** some raw captures and docs cited below were moved to [`unwanted/`](../../unwanted/README.md) with their paths preserved (e.g. `docs/sources/x.md` is now `unwanted/docs/sources/x.md`). See `unwanted/MANIFEST.tsv`.

*Prepared Oct 2, 2026 (event day, SF). We can't open the clips until doors open, so this doc works out where the footage probably comes from, using public dataset cards, NVIDIA/VAST docs, and the official starter kit. Anything inferred is labeled as inference. All raw captures are in `.firecrawl/clips-spaces-*` (18 searches, 24 scrapes). No video or archive files were downloaded.*

Official corpus definition: `.firecrawl/starter-repos/official-vast-data/ARCHITECTURE_REFERENCE.md` ("Video corpus", groups 3–6, packs C–F).

---

## TL;DR

| Pack | Most likely source | Confidence | Real or synthetic | License |
|---|---|---|---|---|
| **C** SDG warehouse RGB (`warehouse3`, `sdg_warehouse_cam-2`, ~178 clips) | **NVIDIA PhysicalAI SDG-Warehouse** (`nvidia/PhysicalAI-SDG-WareHouse`, which redirects to `PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes`), RGB tier | ~60% | Synthetic (Isaac Sim) | OpenMDW-1.1, commercial OK |
| | Alternate: **PhysicalAI-SmartSpaces** MTMC `Warehouse_003` | ~30% | Synthetic (Isaac Sim, Cosmos-Transfer augmented) | CC-BY-4.0 |
| | Alternate: PhysicalAI-Event-Videos (Veo 3 / Cosmos 3 generated) | ~10% | Generated | NVIDIA Dataset License + Google Veo terms |
| **F** Smart spaces (`indoor`, `smartspace_cam-1`, ~102 clips) | **NVIDIA PhysicalAI-SmartSpaces**, probably the `MTMC_Tracking_2024` people-only scenes (hospital, retail, warehouse, other) | ~70% | Synthetic (Omniverse) | CC-BY-4.0 |
| **D** Neighborhood cars (2 day merges, 2026-09-01/02) | **A private neighborhood camera**, real footage the organizers licensed or recorded themselves. No public dataset. | ~85% that it's private and real | Real | Organizer-cleared for this event only |
| **E** SF streets (`sf_streets_cam-1..4`, "ingesting soon") | **Unknown.** Probably organizer-sourced fixed cameras. No public SF multi-cam dataset matches. | Low | Probably real | Organizer-cleared |

The official BUILD_DAY says the confirmed sources are "real-world footage": dashcam (PIE), overhead highway (I-24), and "A private neighborhood camera capturing car movement". It also has `<!-- TODO: two more source types pending confirmation -->`, which are probably the warehouse and smart-space packs. It warns not to ingest internet or YouTube video because the provided sources were picked for licensing. [`starter-repos/official-vast-data/BUILD_DAY.md` L241–260]

---

## Pipeline facts that shape every pack

- **Segmenter cuts each upload into ~5 s clips** (`video-segmenter (~5s clips…)`). A "clip" in the UI is therefore about 5 s, so "~178 clips" is roughly 15 minutes of footage and "~102 clips" is roughly 8.5 minutes (inference from the clip length). [clips-spaces-p07-vast-vss-blueprint-gh.md]
- **The Detector stores YOLO11 `object_counts` as the peak concurrent count per class** (the most boxes of that class in any one frame), not unique objects. A parked car or a humanoid misread as a person raises the count. [clips-spaces-p14-vast-video-detector.md]
- **The Reasoner sees the YOLO class list in its prompt**, so YOLO mistakes (forklift→"truck") can carry into Cosmos' text. It asks for "searchable atoms (color, brand/logo, vehicle type, sign text, clear counts, action, likely next move)", capped at 1024 chars. The default model in the public repo is `cosmos-reason2-8b`; at the event it's Cosmos3-Reason. [clips-spaces-p13-vast-video-reasoner.md; ARCHITECTURE_REFERENCE.md]
- **YOLO11 = the 80 COCO classes.** No forklift, pallet, box, shelf/rack, ladder, fire/smoke, hard hat, safety vest, robot, wheelchair, stroller, scooter, cart, or door. Relevant classes that do exist: person, bicycle, car, motorcycle, bus, truck, train, traffic light, fire hydrant, stop sign, parking meter, bench, dog, backpack, handbag, suitcase, chair, couch, bed, potted plant, tv, laptop, bottle. [clips-spaces-p18-ultralytics-coco.md]

---

## Pack C — Warehouse Safety ("SDG warehouse RGB")

### Likely source

**Primary (~60%): NVIDIA PhysicalAI SDG-Warehouse**, Cosmos 3 technical report Appendix C.5. The Cosmos 3 blog links it as `nvidia/PhysicalAI-SDG-WareHouse` ("Warehouse-Operations-Scenes … Warehouse safety"), and that ID redirects to `nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes`. [trend-models-p02-cosmos3-hf-blog.md L167; clips-spaces-p02-hf-sdg-warehouse-readme.md; clips-spaces-p19-cosmos3-arxiv.md §C.5]

Why it fits:
- The pack name has both **"SDG"** (the dataset's own short name) and **"RGB"**. The dataset ships an `rgb/` tier separate from an `artifacts/` tier (depth, segmentation, edges).
- The camera aliases are literally **`ceiling_00…04`** and `eye_00…04`, and the near-miss scenario plays out in an aisle. That matches "short ceiling / aisle clips".
- Clips are **10 s (near-miss, fire) or 15 s (collision, box pickup)**, which fits "short clips".
- The organizers' pitch is "near-miss" search: *"forklift near a person in an aisle"*. Forklift–human near-miss is this dataset's headline scenario.
- Pack F is already named after SmartSpaces (`smartspace_cam-1`), so Pack C probably comes from a different dataset.

**Alternate (~30%): PhysicalAI-SmartSpaces `MTMC_Tracking_2025/2026` scene `Warehouse_003`.** The location string `warehouse3` could map to that scene ID. In the 2026 edition, `Warehouse_003` is a Cosmos Transfer 2.5 augmented re-render of `Warehouse_002`. Content would be people, forklifts, pallet trucks, Nova Carter AMRs, transporters, and Fourier GR1-T2 / Agility Digit humanoids, filmed by ceiling cameras at 1080p30. [clips-spaces-p03-hf-smartspaces-readme.md]

**Long shot (~10%): PhysicalAI-Event-Videos.** This set includes Veo-3/Cosmos-3-generated "forklift-person near misses, falling boxes, fire and smoke, liquid spills, PPE violations". It is mostly 24 fps and spans many settings beyond warehouses, so it fits worse. [clips-spaces-p05-hf-event-videos-readme.md]

**How to tell them apart in the first 5 minutes on site:**
- **SDG-Warehouse:** each source clip is 10–15 s, and layout, lighting, and viewpoint change from clip to clip. You may see **fire/smoke, a shelf knock-over, or a box pickup**.
- **SmartSpaces:** one continuous multi-minute view with the same scene across segments, plus **humanoid robots or AMRs**.
- **Event-Videos:** a more photoreal "AI video" look, possibly with audio.

### What's in SDG-Warehouse (if primary)

| Attribute | Value |
|---|---|
| Scenarios | Forklift–human near-miss (23%), warehouse fire + evacuation (36%), forklift–shelf collision (20%), box pickup (21%) |
| Scale | 122,967 camera-clips / 29,195 runs / ~412 h |
| Resolution / fps | 1920×1080, 30 fps, H.264 |
| Clip length | 10 s (near-miss, fire), 15 s (collision, pickup) |
| Cameras per run | Near-miss: 10 (5 ceiling CCTV + 5 eye-level). Fire: 5 ceiling. Collision: 6 in a circle at varied heights. Pickup: 10 mixed CCTV and eye-level. All cameras are time-synced and look at the event. |
| Agents and objects | Workers from the Isaac character library, forklifts, storage shelves, boxes, props. In collision runs, a person may stand in the forklift's path. |
| Lighting | Randomized per light (color temperature, intensity, exposure, color). Indoor only, no day/night cycle. |
| Annotations (not in our index) | Depth, instance and shaded segmentation, Canny edges, 2D tight/loose boxes, 3D oriented boxes, per-frame intrinsics/extrinsics, run metadata (seed, dodge distance, fire location, exit waypoints) |
| Known artifacts | "computer-graphics-like appearance", limited smoke/fire fidelity, sometimes unnatural evacuation motion, one warehouse layout family |
| License | **OpenMDW-1.1**, "ready for commercial or non-commercial uses", fully synthetic with no real people |

[clips-spaces-p02-hf-sdg-warehouse-readme.md; clips-spaces-p19-cosmos3-arxiv.md L2456, L2744–2752]

### Camera setup implications
- `camera_id` is a single value (`sdg_warehouse_cam-2`), but the clips probably come from **many different runs and rigs**. Don't treat "same camera_id" as "same viewpoint" or "same timeline". Every clip is a self-contained staged event (inference).
- Multiple views of the same run may be in the archive. If so, "same moment from 5 angles" is a strong demo, but only if the filenames carry the run_id. Check this before relying on it.
- There is no long-horizon story: no shift changes and no occupancy trend over hours.

### Synthetic vs. real
- Fully synthetic, so there is no privacy issue. **Judges will notice the CG look.** Say it up front and present it as intended: "NVIDIA's SDG data exists because real near-miss footage is rare and legally sensitive, and that is exactly the long tail we're indexing." That framing comes from the dataset card's own "Why this dataset" section.
- Cosmos3-Reason may describe frames as "a simulated / 3D-rendered warehouse". Handle that with a re-ingest prompt, or tolerate it in search.

### Hard for YOLO / Cosmos
- **COCO has no forklift.** Expect forklifts to come out as `truck` or `car` (sometimes `train`), or not at all. **No pallet, box, shelf, fire, smoke, vest, or hard hat** classes either. YOLO-only filters like "object_class = forklift" won't work. Use Cosmos text and embeddings instead, or remap `truck` to "forklift?" when scenario = warehouse.
- **Humanoids and mannequin-like CG workers** score as `person`. That's fine for proximity, but a humanoid robot in the SmartSpaces variant inflates person counts.
- **Proximity from a single 2D view:** ceiling cameras foreshorten distance. A forklift "near" a person in 2D may be meters away. Use multiple views or cross-check with Cosmos.
- **Near-miss vs. contact** depends on a dodge-distance parameter and plays out within about 1 s. A 5 s segment sampled at Cosmos fps may miss the dodge. Expect "forklift drives toward person" captions without the outcome.
- **Fire/smoke rendering is low-fidelity.** Cosmos might call it "orange light" or "fog".

### Events you can build on (Pack C)
1. **Forklift–person near-miss** (the most common event): a worker stands still while the forklift approaches and swerves at the last moment. Proximity alerts, near-miss severity ranking, "closest approach" scrub.
2. **Forklift–shelf collision**: knock-over and debris. Optionally a person stands in the path (a three-body event). "Infrastructure damage" incidents.
3. **Fire + evacuation**: ignition, workers turn toward the flame, then run to exits. Time-to-evacuate and "person still inside after X s" queries.
4. **Box pickup** (normal baseline): walk, pick up, carry. Use these as **hard negatives** so "near-miss" queries don't return routine forklift-free activity.
5. **Blocked aisle / pallet in walkway**: not a scenario in the dataset card. It may show up incidentally through prop randomization, but don't promise it.

---

## Pack F — Indoor Smart Spaces

### Likely source
**NVIDIA PhysicalAI-SmartSpaces** (`nvidia/PhysicalAI-SmartSpaces`, ~70%). The name matches exactly. It is NVIDIA's "multi-camera 3D perception dataset for smart spaces", the AI City Challenge Track 1 data for 2024, 2025, and 2026. [clips-spaces-p03-hf-smartspaces-readme.md; clips-spaces-p15/p16-aicity*-track1.md]

The organizers chose the category "Crowds" and suggested queries like *"person walking through an aisle"*, *"group of people near equipment"*, *"empty corridor"*. That points to the **2024 people-only subset** (90 scenes, six environments "including a warehouse, retail store and hospital"; ~2,481 people). The 2025/2026 subsets are almost all warehouse scenes with vehicles. [clips-spaces-p17-nvidia-blog-aicity2024.md] (inference)

### Dataset facts
| Subset | Scenes | Hours | Cameras | Objects | Notes |
|---|---|---|---|---|---|
| MTMC_Tracking_2024 | 90 | 212 | 953 | Person: 2,481 | Warehouse, retail, hospital, and others. Scenes 071–080 have a storage room next to the retail space. `scene_071/camera_0649` is corrupt. |
| MTMC_Tracking_2025 | 23 | 42 | 504 | Person 292, Forklift 13, NovaCarter 28, Transporter 23, FourierGR1T2 6, AgilityDigit 1 | Warehouse_000–020, plus Lab_000 and Hospital_000 |
| MTMC_Tracking_2026 | 28 | 28.7 | 353 | Person 901, Forklift 121, PalletTruck 115, Transporter 71, GR1T2 70, Digit 69, NovaCarter 32 | 6 scenes are Cosmos Transfer 2.5 re-renders. `Warehouse_026/027` are **real-world** test captures (60 s each). |

- **1080p, 30 fps, H.264, time-synced multi-camera with overlapping views**, calibration and top-down map included. Average video per camera is about 13 min (2024) or about 5 min (2025/26) (computed: hours ÷ cameras).
- Generated with Isaac Sim Replicator Agent + Replicator Object: people walk on randomized trajectories, and shelving, pallets, and people get randomized procedural layouts. [clips-spaces-p24-aicity9-arxiv.md §3.1]
- Annotations (not in our index): MOTChallenge-format 2D boxes and global IDs (2024), JSON 2D/3D boxes and depth maps (2025/26).
- **License: CC-BY-4.0.** Demo-able with attribution ("NVIDIA PhysicalAI-SmartSpaces"). Synthetic (apart from the two real 2026 test scenes), so there is no privacy issue.

### Camera setup, lighting, activity
- Fixed, high-mounted, downward-angled CCTV views. The rendered indoor lighting is constant, with no day/night cycle.
- Activity is mostly **people walking randomly**: steady flow, occasional groups, people going in and out of view. In 2025/26 warehouse scenes, AMRs, forklifts, pallet trucks, and humanoids move on planned paths.
- The 2024 scenes were built for multi-camera tracking, not for incidents. **No falls, fights, or staged incidents** are documented. Expect "normal operations" footage.

### Hard for YOLO / Cosmos
- Lots of `person` detections; occlusion in crowded scenes lowers the peak count.
- **Humanoid robots (GR1-T2, Digit) will be detected as `person`**, and AMRs/transporters have no COCO class (sometimes `suitcase` or nothing).
- Hospital scenes: `bed`, `chair`, `couch`, `tv` work. There are **no wheelchair, gurney, or cart** classes.
- Cosmos may struggle with "is this a hospital or an office" in generic synthetic rooms. Re-ingest prompts with venue hints help.
- With ~102 clips, the pack is small. Retrieval demos will hit the same few scenes over and over.

### Events you can build on (Pack F)
1. **Occupancy curves**: person peak-count per segment over time ("busiest minute", "room empty → filled").
2. **Empty corridor / dwell**: segments with 0 persons vs. groups lingering near equipment.
3. **Cross-pack query "person in a warehouse aisle"**: the officially suggested link between C and F.
4. **Robot–person proximity** (only if 2025/26 scenes are present): AMR or humanoid passing close to walkers.
5. **Restricted area entry**: the storage room next to the retail space in scenes 071–080 is a natural "back-room access" zone, if those scenes are in the pack.

---

## Pack D — Neighborhood Streets

### Likely source
**A private residential camera, real footage**, not a public dataset. BUILD_DAY lists the confirmed sources and includes "A private neighborhood camera capturing car movement". The two "day merges" are dated **2026-09-01 and 2026-09-02**, about a month before the event, so this is fresh footage recorded or licensed for the challenge. No public "neighborhood" dataset from VAST or NVIDIA turned up in searches (clips-spaces-s11, s18). Confidence that it's private and real: ~85%.

Related clues:
- The organizers' overview video is **`vss2-blurred-3.mp4`** (146 MB, Google Drive). "vss2" is VAST's internal name for this pipeline (the detector's secret is `vss2-secret`), and **"blurred"** suggests faces or plates in real footage were blurred for the walkthrough. [clips-spaces-p21-gdrive-vss2-blurred.md; clips-spaces-p14-vast-video-detector.md] (inference, not downloaded)
- VAST's public repo has a YouTube capture service and timestamped chunk names (`20260901_224739_london-luxury-walk_chunk_0000.mp4` appears in the skills). That shows the organizers used date-stamped captures around 2026-09-01, but the event rules ban ingesting from the internet. [clips-spaces-p12-vast-video-streaming.md; starter-repos/.../reingest-chunk/SKILL.md]

### Expected characteristics (inference, check on site)
- One fixed camera: a home security or doorbell-style wide view of a residential street, probably at a typical 1080p or 2K security-cam resolution with a low frame rate (often 15–20 fps). Fixed exposure, a timestamp overlay is likely.
- "Day merge" probably means a long video for each calendar day. If it covers 24 h, expect **night IR (grayscale) segments, headlight glare, and dawn/dusk transitions**. Activity is sparse: long empty stretches, then a car passes.
- Real people and plates, so blur or avoid zooming on identifiable residents in the demo. Don't build person identification or tracking of residents on this pack. The license covers this event only.

### Hard for YOLO / Cosmos
- COCO covers this well: car, truck, bus, motorcycle, bicycle, person, dog. **Parked cars dominate `object_counts`** because the count is peak concurrent, so "many vehicles" queries will return dull parked-car segments. Filtering on motion has to come from Cosmos text.
- Delivery vans and SUVs come out as `car` or `truck`. There is no "van" or "package" class, so delivery detection relies on Cosmos ("person carrying a box to a door").
- In night IR, colors are gone. Color-based queries ("red car") fail and Cosmos may invent colors.
- Small or distant objects at a low frame rate: brief passes can fall between Cosmos sampled frames.

### Events you can build on (Pack D)
1. **Arrival/departure log**: car enters and parks, car leaves. Calculate dwell time across the two days.
2. **Day-over-day comparison** (Sep 1 vs. Sep 2): traffic counts by hour, "busier than usual" anomalies. This is the unique angle of this pack (the official doc calls it "Day-scale street vehicles").
3. **Two vehicles close together / passing on a narrow street** (official example query).
4. **Vehicle stopping at the curb**: deliveries, pickups, idling.
5. **Pedestrian or dog walker near a moving car**: the cross-pack "person close to a moving vehicle" query.

---

## Pack E — SF Streets

### Likely source
**Unknown, low confidence.** Four fixed San Francisco street cameras (`sf-streets/1…4`), listed as "**ingesting soon**". Possibilities:
- Organizer-recorded or licensed footage from SF street-level cameras. That fits the rule against internet sources.
- Public-agency feeds. Caltrans CCTV is publicly viewable, and some legal commentary treats state DOT feeds as public domain. But those are mostly highway views, not "pedestrians crossing while cars wait". [clips-spaces-s16-caltrans.json]
- Commercial webcams (SkylineWebcams/EarthCam Castro & Market, etc.) exist but have restrictive licenses and are probably not the source. [clips-spaces-s15-sf-webcams.json]

No public multi-camera SF street dataset from NVIDIA or VAST was found (clips-spaces-s09, s10, s17). Not related: NVIDIA's VSS `its.mp4` is a **synthetic** 2:10 traffic scene, not SF. [clips-spaces-p06-vss24-examples.md]

### Expected characteristics (inference)
- Fixed urban cameras, probably daytime, with dense pedestrians, cars, buses, Muni, cyclists, and robotaxis. Four views, but **not necessarily overlapping or time-synced**. The official query "same moment from two SF cameras" assumes synced timestamps, so check `upload time` and filenames first.
- Real people, so the same privacy care as Pack D applies.

### Hard for YOLO / Cosmos
- COCO has traffic light, stop sign, fire hydrant, bus, bicycle, and motorcycle. **It has no e-scooter, wheelchair, stroller, cable car/streetcar** (likely `train` or `bus`), and no class for **robotaxis** (Waymo = `car`; Cosmos may describe the roof sensor pod).
- Heavy crowd occlusion: person counts are capped by visibility.
- **Risk: the pack may not be indexed in time.** Build features so Pack E is optional, and drop it in only if `list-metadata` shows `sf_streets_cam-*`.

### Events you can build on (Pack E)
1. **Pedestrians crossing while cars wait**: crosswalk conflict and failure-to-yield.
2. **Busy intersection / congestion**: peak counts of car, bus, and person.
3. **Cross-camera "same moment"**: only if timestamps line up.
4. **Bus or vehicle blocking the crosswalk or bike lane.**
5. **Cross-city comparison** with Pack B (Toronto PIE) and Pack D (neighborhood) on the anchor query.

---

## NVIDIA VSS sample videos (for prompt ideas, not in our corpus)

| File | What it is | Source |
|---|---|---|
| `warehouse.mp4` | 3:30, "clips within a warehouse environment". Example alert "Box Dropped". Sample Qs: "When did the forklift first arrive?", "Did a worker drop any boxes?", "What breaches of safety protocol took place?" | VSS 2.4 examples |
| `warehouse_82min.mp4` | 82-min warehouse compilation (long-video summarization) | VSS 2.4 examples |
| `its.mp4` | 2:10 **synthetically generated** traffic scene. Qs about crash, police arrival | VSS 2.4 examples |
| `bridge.mp4` | 3-min drone bridge inspection | VSS 2.4 examples |
| `sample-warehouse-ladder.mp4` | Workers on ladder with or without PPE (GDINO "person" + VLM PPE check) | VSS 2.4 examples / VSS search docs |
| Conveyor-belt video | Isaac Sim synthetic, boxes in different conditions | VSS 2.4 examples |
| `warehouse_sample.mp4` | Default VSS 3.x search/RT-alert demo: "find all instances of forklifts" | `.firecrawl/vss-search.md`, `vss-rt-alert.md` |
| `warehouse-4cams-20mx20m-synthetic` | Bundled 4-camera synthetic warehouse for the MV3DT/BEV 3D tracking profile | clips-spaces-p09-vss-mv3dt.md |

The camera IDs and names don't match our packs, so these files are probably **not** what was ingested. Their prompts and alert categories (box drop, forklift arrival, PPE, ladder, "Pathway Obstruction", "Spillover", "proximity violation") are good templates for Pack C re-ingest prompts. [clips-spaces-p06-vss24-examples.md; clips-spaces-p10-vss-wh-2d.md]

---

## Cross-pack cheat sheet

| Pack | Biggest COCO gap | Biggest Cosmos risk | Best demo event | Privacy |
|---|---|---|---|---|
| C | forklift, pallet, box, shelf, fire | Calls it "simulation", misses sub-second dodge | Forklift–person near-miss | None (synthetic) |
| F | AMR, humanoid (→person), wheelchair | Can't tell venue type apart in generic rooms | Occupancy / empty-corridor | None (synthetic) |
| D | van, package. Parked cars inflate counts | Night IR colors, sparse events | Day-over-day arrivals/dwell | Real residents. Blur, no ID |
| E | scooter, stroller, streetcar, robotaxi | Crowd occlusion, maybe not indexed | Pedestrian–car crosswalk conflict | Real public. Blur, no ID |

**Day-1 checks before building:**
1. `list-metadata` for exact `camera_id`/`location` spellings and whether `sf_streets_cam-*` exists yet.
2. Open 3 Pack C clips. Do you see fire or shelf collisions (SDG-Warehouse) or humanoids/AMRs (SmartSpaces)?
3. Check `object_classes` on Pack C for what YOLO labels forklifts.
4. Look for night segments in Pack D.

## Sources (local captures → URLs)
- clips-spaces-p01/p02 — https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes (README)
- clips-spaces-p19 — Cosmos 3 tech report, https://arxiv.org/html/2606.02800v4 (§C.5, dataset table)
- trend-models-p02-cosmos3-hf-blog.md — alias `nvidia/PhysicalAI-SDG-WareHouse`
- clips-spaces-p03/p04 — https://huggingface.co/datasets/nvidia/PhysicalAI-SmartSpaces (README, tree)
- clips-spaces-p05 — https://huggingface.co/datasets/nvidia/PhysicalAI-Event-Videos
- clips-spaces-p08/p15/p16 — aicitychallenge.org 2024 data, 2025-track1, 2026-track1
- clips-spaces-p17 — https://blogs.nvidia.com/blog/ai-city-challenge-omniverse-cvpr/
- clips-spaces-p24 — 9th AI City Challenge, https://arxiv.org/html/2508.13564v1
- clips-spaces-p23 — https://huggingface.co/datasets/nvidia/PhysicalAI-Spatial-Intelligence-Warehouse (RGB-D images/VQA, ruled out: no video)
- clips-spaces-p06 — https://docs.nvidia.com/vss/2.4.0/content/examples.html
- clips-spaces-p09/p10 — VSS Warehouse MV3DT and 2D-with-agents profiles (docs.nvidia.com/vss/latest/warehouse-docs/)
- clips-spaces-p07/p12/p13/p14 — https://github.com/vast-data/vss-blueprint (README, video-streaming, video-reasoner, video-detector)
- clips-spaces-p18 — https://docs.ultralytics.com/datasets/detect/coco/
- clips-spaces-p20 — Isaac Sim environment assets (warehouse, hospital, office USDs)
- clips-spaces-p21 — Google Drive page for `vss2-blurred-3.mp4` (metadata only)
- starter-repos/official-vast-data/BUILD_DAY.md, ARCHITECTURE_REFERENCE.md — official corpus and licensing notes
- Searches: clips-spaces-s01 … s18 (.json)
