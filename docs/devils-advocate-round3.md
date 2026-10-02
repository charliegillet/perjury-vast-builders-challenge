# Round 3: devil's advocate verdicts

| Idea | Verdict | Why |
|---|---|---|
| ARGUS | **KILL** (keep only the camera wall) | A serial chain of 7 links, each ≤85% reliable, gives ~10% odds live. Handing off between cameras without calibration means one visible ID swap ends it (best published HOTA on Scene 3 is 29). A 17-way 4K fan-out on a shared GPU host takes minutes. "Pickup with trailer" falls outside COCO. |
| **PERJURY** | **FIX-THEN-PROCEED (lead)** | The hero lie "pedestrians on I-24" is just a SQL filter (`object_classes` without `person`); Cosmos adds nothing. Subtle lies (count, order, lane, braking) are at chance on this stack. Cosmos only earns its place on claims outside COCO and on scene-level claims (trailer, semi vs box truck, snow, stop-and-go). |
| REWATCH | KILL as a live act | Re-ingest is chunk-level, takes minutes, can't be cancelled, and has vanished before. Prompt Golf can't run live. Allowed only as one pre-run repair before 11:30. |
| ASSAY | FIX, fallback only | Depends on G2; amazement 5. |
| FOUNDRY | KILL | It's auto-labeling with a nicer UI, on the most crowded pack, and nothing consumes the labels. YOLO probably proposes nothing for forklifts. |

## Platform facts missed earlier (all from repo files)
- **App URL is HTTP.** `deploy-app-no-registry` publishes `http://video-lab-team-N.cosmos.vastdata.com/app`, and `getUserMedia` needs a secure context. The pod Secret has VSS credentials but not necessarily `GPU_BEARER_TOKEN`, so check pod→GPU reachability.
- **Canary docs conflict.** The model id comes from `/v1/models` in one place and is a 404 in another. The endpoint wants WAV; browsers record webm/opus, so convert.
- **Segments are probably 4K.** The segmenter uses libx264 CRF 18 with no scale filter. Check `perception_json.frames[0].shape`.
- **YOLO limits.** It runs at the default 640 px with `conf=0.4`, so far-lane vehicles are lost. No track IDs. `object_counts` is the peak concurrent count. `/v1/infer` accepts a presigned `url`. Per-frame sidecars may already exist at `/videos/detections`.
- **The Reasoner prompt includes the YOLO class list and says "counts only when obvious"**, so Cosmos is not an independent counter.
- **Measure Cosmos latency free:** `avg(processing_time)` on `vss-collection`. With `max_tokens` 8 the answer can come back empty if the model emits `<think>`.
- **Cosmos grounding is documented for images only** (0–1000). Use a keyframe `image_url`.
- **I24-3D calibration and trajectories are gated** behind i24motion.org. Trailer IDs are listed for Scenes 1 and 3; semis are excluded.
- **One GPU host (166.19.38.112) serves every team.** W&B Inference returns 429 above its concurrency cap.
- **VANTAGE event verification:** Reason2-8B accepts 42% of non-events; Cosmos3-Super ~27%. Grounding is Cosmos3's strongest skill (F1@.5 74–87); temporal is its weakest (~50 mIoU).
- **GridVAD self-consistency** raises precision, lowers recall, and costs 5× the calls.

## Recommended merge: PERJURY-JURY on Pack A
- **Hero:** "A pickup is towing a trailer." It comes out FALSE on Scene 2 (snow) and TRUE on Scene 1 (free-flow). YOLO can't decide it, and the paper's trailer list is the ground truth. Warm-up: "three pedestrians crossing." Close: an honest UNVERIFIABLE on "the truck braked hard", citing the temporal numbers.
- **Architecture:**
  - T0: VastDB pushdown over 16–17 camera rows plus sidecars (no GPU, <1 s).
  - T1: Nemotron decomposes the claim and votes over 16 captions.
  - T2: Cosmos runs only on routed claims, on ≤6 diverse cameras, using keyframe grids and neutral prompts. A box must overlap a YOLO car/truck box in ≥2 frames.
  - A quorum across cameras replaces M=5 resampling.
  - JPEG tile wall; progressive reveal with the first pill at ~3 s.
- **Free sycophancy measurement:** every juror "yes" for a trailer on Scene 2 is a measured hallucination (eyeball-verify first). Run a bench of ≥40 claims reporting catch, false-accusation and decline rates, plus a jury-size curve for k = 1, 3, 8, 16.
- **Cuts:** ARGUS relay/follow-cam, Prompt Golf, FOUNDRY, Exhibit A on the critical path. The ribbon shows only chips that fired, with the rest greyed out. The receipt says "9 of 13".
- **Gates by 10:45:**
  - G0: HTTPS + pod→GPU
  - G1: shape and `processing_time`
  - G2: stock `agent/ask` on 10 lies; if it rejects ≥8, pitch "evidence audit" instead
  - G3: Cosmos trailer false-positive rate on Scene 2; if ≥25%, change the hero
  - G4: Canary within 20 min, otherwise type the claim
  - G5: non-empty yes/no at 6-way concurrency with p50 <10 s
  - G6: scan Scene 2 for false `person` detections
- **Odds (estimates):** PERJURY-JURY ~55% clean. ARGUS live 10–15%. REWATCH ~30%. ASSAY ~55% at amazement 5. FOUNDRY ~65% at amazement 5–6.
