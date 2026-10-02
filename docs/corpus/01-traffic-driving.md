# Corpus deep-dive 01: Traffic and driving packs (I-24 3D + PIE)

> **Cleanup note (2026-10-02):** some raw captures and docs cited below were moved to [`unwanted/`](../../unwanted/README.md) with their paths preserved (e.g. `docs/sources/x.md` is now `unwanted/docs/sources/x.md`). See `unwanted/MANIFEST.tsv`.

Prepared 2026-10-02, before we can see the clips. Everything below comes from the public source datasets, papers and repos. The pack descriptions are from `.firecrawl/starter-repos/official-vast-data/ARCHITECTURE_REFERENCE.md` ("Video corpus" section). Raw captures are in `.firecrawl/clips-traffic-*` (search JSON is `clips-traffic-s-*.json`).

How confident each claim is:
- **[S]**: stated in the source paper or README.
- **[D]**: derived from source numbers (arithmetic only).
- **[E]**: our estimate. Check it against the real clips on event day.

---

## TL;DR

| | Pack A: `i24_cam-1` (nashville) | Pack B: `pie_cam-3` (toronto) |
|---|---|---|
| Source dataset | **I24-3D** (Interstate-24 3D Multi-Camera Dataset), Vanderbilt, BMVC 2023 | **PIE** (Pedestrian Intention Estimation), York University, ICCV 2019 |
| Camera | **Fixed**, pole-mounted at 110 ft, 4K/30fps, 16-17 overlapping cameras per scene | **Moving** dashcam (ego-vehicle), 1920x1080/30fps, 157° wide-angle lens |
| Footage | 3 scenes × 16-17 cams = **~49-51 clips of 60-90 s**, about 57 min total | **53 × ~10-min clips in 6 sets**, about 8.4 h of video (909,480 frames) |
| Content | Highway only: free-flow, snow plus slow traffic, dense stop-and-go. **No pedestrians, no crashes.** | Downtown Toronto streets in daytime, clear weather (sunny or overcast). **1,842 annotated pedestrians**, 519 who cross in front of the car |
| License | No explicit license on the repo (GitHub `license: null`). Data is gated behind an i24motion.org account. The sibling I24V DUA allows academic and commercial use with citation. | **MIT** (videos and annotations) |
| Biggest gotcha | Anchor query "person close to a moving vehicle" has **zero true positives** here | Intention is not visible on screen, and ego speed/OBD is not in the video |

---

## Pack A: "I-24 / 3D traffic" → I24-3D dataset

### A1. Dataset identification (confirmed)

The `scene*_p*c*` naming matches **I24-3D**. It does not match the other I-24 MOTION releases.
- I24-3D refers to cameras as `p1c5`, `p1c6` (pole 1, camera 5/6), and its supplementary example file is literally `Scene3_p3c5.mp4` [S] (arXiv 2308.14833, Fig. 2 and supplementary list; `clips-traffic-i24-3d-pdf.md`). Each scene's videos sit in `{scene_id}_sequences/{camera_id}.mp4` [S] (Appendix I).
- The larger sibling **I24V** (WACV 2024, "So you think you can track?") names files differently: `PXXCXX_<ts>.mkv` (uppercase, poles 01-40, 1080p, 234 cameras, 234 h). It also has no "scene" prefix [S] (`clips-traffic-i24v-utils-readme.md`). That rules it out.
- The clip count matches as well. 3 scenes with 17 + 16 + 16 active cameras = **49 camera videos** [D]. That is close to VAST's "~51". The testbed section has 18 cameras on 3 poles, and periodic outages leave 16-17 active per scene [S], so VAST may have a couple of extra or partial camera files.

**Paper:** D. Gloudemans, Y. Wang, G. Gumm, W. Barbour, D. B. Work, "The Interstate-24 3D Dataset: a new benchmark for 3D multi-camera vehicle tracking," BMVC 2023. arXiv: https://arxiv.org/abs/2308.14833. Code: https://github.com/I24-MOTION/I24-3D-dataset. Parent testbed: Gloudemans et al., "I-24 MOTION: An instrument for freeway traffic science," Transportation Research Part C 155 (2023), arXiv https://arxiv.org/abs/2301.11198.

### A2. License and demo use

- The GitHub repo has **no license file**. The API returns `"license": null` (`clips-traffic-i24-3d-ghapi.md`). The README only asks you to cite the work and star the repo. The data is distributed through i24motion.org behind a free, approved account (`clips-traffic-i24-data.md`).
- The paper on arXiv is CC BY 4.0. The BMVC copyright note says the document may be distributed unchanged.
- The closest written terms are the sibling **I24V Data Use Agreement**: "free to use the data in academic and commercial work", derivatives allowed, citation required, and **re-identifying individuals is prohibited** [S] (`clips-traffic-i24v-utils-readme.md`). We are inferring that I24-3D follows the same spirit. The I24V terms do not formally cover it.
- Privacy: the authors visually checked the footage and ran plate-blurring software so license plates are not readable. Driver faces are not discernible. The work is IRB-approved [S] (Appendix VII).
- **Verdict:** showing the clips VAST provides in an on-stage demo, with attribution to Vanderbilt I-24 MOTION, is low risk. Don't redistribute raw video, and don't pitch anything that sounds like "identify the driver or plate".

### A3. Camera setup

- **Fixed** cameras on **110-foot roadside poles** (testbed-wide poles are 110-135 ft), with poles about 500 ft apart. Three poles cover **about 2,000 ft** of I-24 [S].
- Each pole has a 6-camera cluster mounted orthogonal to the roadway. The cameras are 4K PTZ IP models, aligned for a 180° overlapping field of view per pole and overlap between poles [S] (MOTION paper §III-A).
- Video is **3840×2160 H.264 at 30 fps nominal** [S]. The live MOTION system records 1080p, but I24-3D was released at 4K.
- Every stretch of road is seen by at least 2 cameras, so the **same vehicle appears in several clips** at slightly different times. Camera clocks are out of phase by 0.1-1 s, with doubled and skipped frames. The dataset includes corrected timestamps [S] (Appendix III).
- The view is steep and oblique-overhead, and covers **both directions** (EB and WB), with 4-5 lanes each way [S]. The far lanes (EB lane 1, WB lane 4) have the smallest vehicles and the most missed detections [S].

### A4. Duration and clips

| Scene | Length per clip | Cameras | Unique vehicles | 3D boxes | Description [S] |
|---|---|---|---|---|---|
| 1 | 90 s | 17 | 324 | 291k | Free-flow traffic |
| 2 | 60 s | 16 | 114 | 146k | **Slow traffic, snow conditions** |
| 3 | 60 s | 16 | 282 | 440k | **Congested, stop-and-go** |
| Total | 210 s of wall-clock | ~49 videos | 720 | 877k | **~57 min of video** |

Source: Table 1 of arXiv 2308.14833. All cameras in a scene record the **same 60-90 s window**, so the pack has only **3.5 minutes of unique real-world time**, seen from about 49 angles [D].

### A5. Scene content

- **Traffic density:** a full range. Scene 1 is high-speed free flow. Scene 2 is slow because of snow. Scene 3 is dense stop-and-go with heavy occlusion "potentially for hundreds of frames" [S]. The corridor carries about 150k vehicles/day, with 10-15% heavy trucks, and has reliable rush-hour stop-and-go waves [S] (MOTION paper §III).
- **Weather/lighting:** Scene 2 has snow, and snow occludes parts of the frame [S]. The paper does not state time of day. The example frames look like daylight [E]. Expect no night footage, because the MOTION paper says night video is noisy and the released benchmarks are daytime [E].
- **Vehicle classes (6):** sedan, midsize (SUV/minivan), van, pickup, semi (tractor-trailer), truck [S]. Fourteen vehicle IDs tow trailers: 8 in Scene 1 (IDs 288, 133, 7, 138, 43, 270, 245, 216) and 6 in Scene 3 (225, 105, 15, 148, 247, 219) [S].
- **No pedestrians are visible anywhere, and no anomalous events such as crashes occur** [S] (Appendix VII, privacy section).

### A6. Original annotations (what is actually in the footage)

- Hand-annotated **3D boxes** (x, y in roadway feet, l/w/h, direction EB/WB) for every vehicle in every camera, with vehicle **class**, **global ID across cameras**, camera, timestamp and frame [S]. Positional agreement across cameras is 1.24 ft, and dimension error is 0.5 ft.
- Spline-smoothed **continuous trajectories** per vehicle (`*_splobj.json`, `*_resampled.csv` with 8 projected 3D corners per box) [S].
- Per-camera **homographies**, roadway-curvature fits, **lane-grid** overlays and **ROI masks** [S].
- These give exact lane positions over time. A lane change is a y-coordinate crossing a 12-ft lane boundary, and speed or braking is the derivative of x. So the ground-truth events can be computed from the original labels even though VSS does not store them.

### A7. Events you can build on (Pack A)

The frequencies are [E] unless noted. Each real-world event shows up in about 2-4 overlapping camera clips.

| # | Searchable moment | Where | Est. frequency |
|---|---|---|---|
| 1 | **"dense stop-and-go traffic / queue of cars barely moving"** | Every Scene 3 clip | 16 clips (all of Scene 3) [S] |
| 2 | **"highway traffic in snow / snow-covered lanes"** | Every Scene 2 clip | 16 clips [S] |
| 3 | **"free-flowing highway traffic at speed"** | Scene 1 | 17 clips [S] |
| 4 | **"semi-truck / tractor-trailer"** in frame | All scenes | About 70-110 heavy-vehicle trajectories (10-15% of 720). Visible in most clips. |
| 5 | **"pickup or SUV towing a trailer"** | Scenes 1 and 3 | 14 vehicles [S]. Each is seen in several cameras. |
| 6 | **"vehicle changing lanes"** / **"truck changing lanes"** (VAST's suggested query) | All, most in Scenes 1 and 3 | Rough guess 40-100 lane changes across the 720 vehicles over the 2,000 ft. A few per clip. Truck lane changes are maybe 5-15 total. |
| 7 | **"brake lights / car braking in congestion"**, "vehicle braking hard" | Scene 3 (waves), Scene 2 | Continuous low-speed braking in Scene 3. True hard braking from speed is probably rare, 0-5 events. |
| 8 | **"large truck occluding cars in far lanes"** | Scene 3 | Frequent. The paper calls occlusion the main difficulty [S]. |
| 9 | **"same vehicle seen from multiple cameras"** (cross-camera hand-off) | All | Every vehicle, by design [S] |
| 10 | Opposing-direction contrast, **"one direction jammed while the other flows"** | Likely in Scene 3 (rush-hour asymmetry is typical [S]) | Check on the day |

**Absent:** pedestrians, cyclists, crashes, debris, emergency vehicles [S for the first three]. Treat any caption that claims these as a hallucination.

### A8. What will be hard for Cosmos / YOLO (Pack A)

- **Tiny far-lane vehicles.** YOLO11s at about 640 px input on a 3840 px frame is a ~6× downscale, so a far-lane car that is 60 px wide at 4K becomes ~10 px [D]. Even purpose-built 3D detectors miss far lanes most often [S]. Expect YOLO counts to be well below the real count in Scenes 1 and 3.
- **Unusual viewpoint.** The steep top-down view from 110 ft is unlike typical COCO training images. Pickups, semis and trucks all map to COCO `truck` or `car`, so the dataset's 6 fine-grained classes collapse.
- **Snow (Scene 2)** hides lane markings and partly hides vehicles [S].
- **Near-duplicate captions.** 16-17 cameras show the same 60-90 s. Cosmos captions will be nearly identical across clips and searches will return clusters of near-duplicates. That is good for a "multi-camera corroboration" demo and bad for result variety.
- **Speed and lane-change semantics** need temporal reasoning over a fixed view. Cosmos can describe "congested" and "flowing" reliably. Expect it to miss a specific lane change unless the segment is short and the vehicle is large and near.
- **Anchor-query trap:** VAST's anchor "person close to a moving vehicle" should return **nothing** from I-24. If it does, those results are false positives, such as YOLO calling signs or poles `person`. You can turn this into a precision story.
- **Timestamp skew.** Cameras disagree by 0.1-1 s [S], so cross-camera alignment by timestamp alone is a little off.

### A9. Research tasks a project could echo

- **Multi-camera 3D vehicle tracking / re-ID.** The best published pipeline reaches HOTA 44.8 on average and only **29.1 on congested Scene 3**. Even with ground-truth detections it reaches only 59.6 [S]. A pitch could be: "VLM-assisted cross-camera hand-off that tells you which clips show the same truck."
- **Traffic-science analytics.** I-24 MOTION exists to study **stop-and-go waves**, fundamental diagrams and incident bottlenecks. The parent data release includes days with crashes, though I24-3D itself has none [S] (MOTION paper Table VII). Possible demo: "find the shockwave", "estimate queue length from captions".
- **3D detection from monocular traffic cams**, homography-based speed estimation, and camera time-sync correction.

---

## Pack B: "PIE drives" → Pedestrian Intention Estimation dataset

### B1. Dataset identification (confirmed)

PIE videos are organized as `PIE_clips/set01 … set06/video_000N.mp4`. There are **6 sets corresponding to different routes driven in Toronto** [S] (`clips-traffic-pie-readme.md`, `clips-traffic-pie-clips-index.md`). VAST's "6 long drive sets set01…set06" lines up exactly. Clips within a set are continuous chunks of one recording, so VAST most likely concatenated each set.

**Paper:** A. Rasouli\*, I. Kotseruba\*, T. Kunic, J. K. Tsotsos, "PIE: A Large-Scale Dataset and Models for Pedestrian Intention Estimation and Trajectory Prediction," ICCV 2019. https://openaccess.thecvf.com/content_ICCV_2019/html/Rasouli_PIE_A_Large-Scale_Dataset_and_Models_for_Pedestrian_Intention_Estimation_ICCV_2019_paper.html. Site: https://data.nvision2.eecs.yorku.ca/PIE_dataset/. Annotations: https://github.com/aras62/PIE.

### B2. License and demo use

The dataset site states that **"the videos and annotations are released under the MIT License"** [S] (`clips-traffic-pie-site.md`, `clips-traffic-pie-license.md`). That is fully permissive, so on-stage demos and derivatives are fine with attribution. The footage does show real pedestrians' faces on public streets, so avoid any feature that identifies people.

### B3. Camera setup

- **Moving**, forward-facing, calibrated monocular dashcam (Waylens Horizon) with a **157° wide-angle lens**, mounted inside the car below the rear-view mirror [S] (ICCV paper §3.1). Camera intrinsics are in the repo under `camera_params/`.
- **1920×1080 at 30 fps** [S].
- One camera with no overlap. The ego-vehicle's **OBD and GPS** data (speed, heading, lat/lon, pitch/roll/yaw, acceleration, gyroscope) are synced per frame in the annotations [S]. **None of that is in the video**, so VSS only sees pixels.

### B4. Duration and clips

- **53 clips** of about 10 min each, split into 6 sets [S] (annotations README).
- The site says "over 6 hours", but 909,480 frames at 30 fps is **~8.4 h** [D]. 293,437 frames (~2.7 h) carry annotations [S].
- Per-set size from the server index (74.0 GB total) and estimated duration [D/E]:

| Set | Clips | Size | Est. duration | Official split (pie_data.py) |
|---|---|---|---|---|
| set01 | 4 | 4.3 GB | ~30-35 min | train |
| set02 | 3 | 2.9 GB | ~20-25 min | train |
| set03 | 19 | 27.7 GB | **~3 h** | test |
| set04 | 16 | 23.4 GB | **~2.6 h** | train |
| set05 | 2 | 2.2 GB | ~15 min | val |
| set06 | 9 | 13.5 GB | ~1.5 h | val |

(The WACV 2021 benchmark uses a different split: train 01/02/06, val 04/05, test 03.) **set03 and set04 hold about 70% of the footage**, so most search hits will come from them [D].

### B5. Scene content

- Downtown and urban Toronto routes, "from busy one-way streets to wide boulevards", plus narrow high-foot-traffic streets [S].
- **Daytime only, clear weather (sunny or overcast)** [S] (WACV 2021 benchmark: "recorded in Toronto, Canada in clear weather"; PIE paper figure caption: "daytime under sunny/overcast"). **Expect no night, rain or snow footage.**
- Toronto-specific content: **streetcars** (annotated as vehicle `train`), buses, transit stops and "transit_station" objects, cyclists, pedestrian-crossing signs, construction signs [S].
- The ego car drives through ordinary traffic. It stops at lights, waits for crossing pedestrians and turns at intersections. The WACV benchmark notes that large close-range pedestrian samples usually have the ego-vehicle **stationary or moving slowly** [S].

### B6. Original annotations (what is actually in the footage)

- **1,842 pedestrians** with full tracks (mean 401 frames, about 13 s) and **738,970 pedestrian boxes**. Occlusion flags: none, part (25-75%), full (>75%) [S].
- Per-frame pedestrian behavior: **action** walking/standing; **look** looking/not-looking at the ego car; **cross** crossing / not-crossing / *crossing-irrelevant* (crossing but not in the ego path); **gesture** `hand_ack`, `hand_yield`, `hand_rightofway`, `nod`, other [S].
- Per-pedestrian attributes: age (child/adult/senior), gender, `num_lanes`, `signalized` (n/a / C crosswalk / S signal-or-stop / CS both), `traffic_direction` (one-way/two-way), `intersection` (midblock, T, T-left, T-right, four-way), `crossing_point` frame, and `intention_prob` from a **human study**: 5 lab subjects plus 10 AMT workers per pedestrian [S].
- Crossing breakdown [S] (site stats): **519 intend to cross and do cross**, **894 intend to cross but don't** (blocked, red light, car didn't yield), **429 no intention** (waiting for a bus, hailing a taxi, talking). The paper's own counts are slightly different (512/808/430). The WACV benchmark counts 512 crossing vs 1,322 non-crossing.
- **2,353,983 traffic-object boxes** for vehicles (car, truck, bus, train/streetcar, bicycle, bike), **traffic lights** (regular/transit/pedestrian, with **red/yellow/green state**), **signs** (ped_blue/yellow/white/text, **stop_sign**, bus_stop, train_stop, construction, other), **crosswalks** and transit stations [S].
- Ego-vehicle OBD/GPS: speed, heading, IMU per frame [S]. This means hard braking and stops are **known in the labels**, even though VSS cannot read them.

### B7. Events you can build on (Pack B)

Frequencies come from the annotation counts over ~8.4 h, about 505 min [D unless marked E].

| # | Searchable moment | Est. frequency |
|---|---|---|
| 1 | **"pedestrian crossing the street in front of the car"** | **~519 crossings**, about **1 per minute** of drive. Highest-value query. |
| 2 | **"pedestrian waiting at the curb / standing at crosswalk"** (intends but doesn't cross) | **~894**, about 1.8/min. Very common. |
| 3 | **"person waiting at a bus/streetcar stop"**, **"person hailing a taxi"**, "man leaving his parked car" (no-intent pedestrians; the paper's Fig. 5 shows these) | **~429**, about 0.85/min |
| 4 | **"red traffic light with pedestrians crossing"**, "car stopped at red light" | Traffic lights with state are annotated throughout. Likely every few minutes downtown [E]. |
| 5 | **"zebra crosswalk / pedestrian crossing sign"** | Common; `signalized=C/CS` [E] |
| 6 | **"streetcar / tram on the road"**, "bus at a stop" | Frequent on downtown routes [E] |
| 7 | **"cyclist next to the car"** | Annotated class. Moderate frequency [E]. |
| 8 | **"pedestrian waving the car through / hand gesture to driver"** (`hand_yield`, `hand_ack`, `hand_rightofway`, `nod`) | **Rare**, maybe tens of instances [E]. A strong "needle in haystack" demo if Cosmos can catch one. |
| 9 | **"jaywalking / mid-block crossing"** (`intersection=midblock`, `signalized=n/a`) | A minority of crossings, maybe 10-20% of the ~519, so about 50-100 [E] |
| 10 | **"child or senior pedestrian near the road"** (age attribute) | Minority of 1,842, perhaps under 10% [E] |
| 11 | **"car slowing / stopping for a pedestrian"** (ego yields) | Close to the 519 crossings. The car is often stopped or slow [S]. |
| 12 | **"vehicle ahead braking / brake lights"** (VAST's suggested query) | Common in city traffic, but **not labeled** in PIE [E] |
| 13 | **"construction zone sign"** | `construction` sign class exists. Occasional [E]. |
| 14 | **"pedestrian not looking at traffic while crossing"** (look = not-looking + crossing) | A subset of crossings [E] |

**Absent or very unlikely:** night, rain, snow [S for clear weather]. No crash or collision events are reported. A "near-miss" would only be a pedestrian stepping out close to a slowing car. No highway driving.

**This pack is the natural home of VAST's anchor query.** "Person close to a moving vehicle" should hit many PIE crossings (#1, #11). With I-24 contributing zero, PIE plus the street and warehouse packs carry that query.

### B8. What will be hard for Cosmos / YOLO (Pack B)

- **Small pedestrians.** Most labeled pedestrians are **80-120 px tall** in 1080p, and accuracy falls off sharply **below 80 px** even for dedicated models [S] (WACV 2021). At a ~640-px YOLO input they become 30-60 px. Detection still works, but behavior cues such as head turns and gestures are lost.
- **157° fisheye-like distortion** at the image edges, which is exactly where curbside pedestrians stand. Add windshield glare and reflections from an in-cabin mount [E].
- **Intention is not observable.** "About to cross" was defined by human raters watching ~3 s before the event [S]. Captions will describe "standing at the curb", not intent. Zero-shot VLM baselines are modest: GPT-4V reached ~57% accuracy on crossing prediction, and Gemini 2.5 Pro (BF-PIP) reached ~73% on JAAD [S] (`clips-traffic-pie-bfpip-arxiv.md`). Cosmos captions per segment will be weaker than a task-specific prompt.
- **"Crossing in front of us" vs "crossing-irrelevant"** depends on the ego path, which the model has to infer [S].
- **Ego motion.** The camera moves, so "vehicle ahead braking" and "car stopped" depend on brake lights and optical flow. No speed is available to VSS.
- **Crowds and occlusion** on busy streets. Partial occlusion is common [S].
- **Long, homogeneous drives.** Hours of similar downtown footage, so many segments get bland "city street with cars and pedestrians" captions. Retrieval ranking quality matters more than recall.

### B9. Research tasks a project could echo

- **Pedestrian crossing intention estimation** (PIEPredict: 79% accuracy, ICCV 2019) [S].
- **Crossing action prediction at TTE 1-2 s:** WACV 2021 benchmark with PCPA and other baselines, https://github.com/ykotseruba/PedestrianActionBenchmark [S].
- **Pedestrian trajectory prediction** conditioned on intention and ego speed [S].
- **Ego-speed prediction** from video [S].
- **Traffic-light-aware intention** (TA-STGCN, 2025, uses light states) [S].
- **VLM-based intention** (GPT-4V zero-shot; WACV 2025 VLM fine-tuning on PIE/PSI/JAAD; BF-PIP zero-shot with Gemini 2.5 Pro on raw video) [S]. A Cosmos-Reason version ("explain *why* this pedestrian will or won't cross") is a natural hackathon echo of that line of work.

---

## Cross-pack takeaways for our project

1. **Ground truth can be reconstructed.** Both datasets have public annotations (I24-3D trajectories; PIE XML with crossing points and light states). If we can map VAST clip names and timestamps to source frames, we can **score Cosmos/YOLO search results against real labels** on stage, for example "our agent found 47 of the 519 crossings". The annotations are text or XML on GitHub and need no video download.
2. **Fixed vs moving camera.** I-24 is the fixed, multi-view, vehicle-only lens. PIE is the egocentric, human-interaction lens. One query sees opposite failure modes in each: tiny objects in I-24, unobservable intent in PIE.
3. **Weather and lighting are narrow.** All footage is daytime. The only adverse weather is I-24 Scene 2 (snow). Don't promise night or rain demos from these packs.
4. **Anchor query precision:** I-24 should contribute zero "person near vehicle" hits, and PIE should contribute hundreds. That makes a clean false-positive check.

## Sources

- I24-3D: arXiv 2308.14833 (HTML and PDF incl. appendices) → `clips-traffic-i24-3d-arxiv.md`, `clips-traffic-i24-3d-pdf.md`; GitHub README → `clips-traffic-i24-3d-readme.md`, `clips-traffic-i24-3d-ghtree.md`, API → `clips-traffic-i24-3d-ghapi.md`; publication page → `clips-traffic-i24-3d-pub.md`; YouTube scene previews (unlisted, 1:00) → `clips-traffic-i24-3d-yt-scene*.md`
- I-24 MOTION: arXiv 2301.11198 → `clips-traffic-i24-motion-arxiv.md`; https://i24motion.org/how-it-works → `clips-traffic-i24-how-it-works.md`; https://i24motion.org/data → `clips-traffic-i24-data.md`; I24V utils/DUA → `clips-traffic-i24v-utils-readme.md`; GitHub org → `clips-traffic-i24-gh-org.md`
- PIE: ICCV 2019 paper → `clips-traffic-pie-paper.md`; site → `clips-traffic-pie-site.md`; GitHub README / annotations README / LICENSE / pie_data.py → `clips-traffic-pie-readme.md`, `clips-traffic-pie-annotations-readme.md`, `clips-traffic-pie-license.md`, `clips-traffic-pie-data-py.md`; clip server indices → `clips-traffic-pie-clips-index.md`, `clips-traffic-pie-set0[1-6]-index.md`
- PIE benchmarks: WACV 2021 action benchmark → `clips-traffic-pie-wacv21-benchmark.md`, `clips-traffic-pie-pcpa-readme.md`; BF-PIP (arXiv 2507.21161) → `clips-traffic-pie-bfpip-arxiv.md`; TA-STGCN (arXiv 2507.12433) → `clips-traffic-pie-traffic-aware-arxiv.md`
- Context: VAST + Cosmos Reason smart-city blog → `clips-traffic-vast-cosmos-blog.md`; 16 search result sets → `clips-traffic-s-*.json`
