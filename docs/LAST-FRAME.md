# Fresh project: LAST FRAME

Pitch: **“The next training exercise is already in your footage.”**

The footage is both the question and the answer key. Pause a segment before an observable transition, ask what the next segment shows, collect confidence, then reveal the continuation with evidence. Target fleet trainers and facility operations trainers. The prototype teaches observation and confidence, without grading workers, inferring intent or claiming certified safety instruction.

| Pack supplied by the user | Training opportunity | First-version choice |
|---|---|---|
| A: Nashville I-24, ~51 multi-camera clips | Stop-and-go versus sustained movement; compare viewpoints | One traffic-flow drill; calibrated speed and cross-camera linking are stretch work |
| B: Toronto dashcam, 6 sets | Pedestrian crossing versus waiting, bus-stop interaction | Primary live demo: two contrasting reviewed before/after pairs |
| C: Synthetic warehouse, ~178 clips | Worker/vehicle paths, pauses at shared junctions | Secondary demo; visibly identify synthetic source footage |
| D: Neighborhood street camera, 2 full days | Parked-to-moving transitions and other ordinary changes | Harvest timed pairs from the continuous archive |
| E: Four SF street cameras, still ingesting | Street interactions and multiple viewpoints | Discover later; never put on the critical path |
| F: Indoor facility, ~102 clips | Doorway passage and shared-space interactions | Optional third setting after inspecting actual clips |

Counts are the user's corpus inventory. Scenario availability and content must be checked against actual clips; the research documents contain estimates about source datasets, not proof of the ingested footage.

The build lives in [lastframe/](../lastframe/README.md). Six illustrative storyboards make the workflow runnable offline; they are explicitly separated from human-reviewed VSS scenarios. Existing UNWATCHED research and source code are preserved.

## Build-day sequence

1. Run on the VM and verify one search, parent timeline, and segment stream.
2. Watch five candidate Pack B videos. Select two adjacent segment pairs showing different observed continuations; reject pairs where the transition is already visible in the observation.
3. Author or draft setup/options. Inspect actual clips to verify the answer, timestamp and neutral title. Publish two drills.
4. Repeat with one Pack C pair. Display the synthetic source honestly.
5. Run the round lifecycle on live footage. Test replay, unlock, browser notes and export.
6. Label a small held-out set for W&B/Weave evaluation if time remains.
7. Freeze features, record the demo and complete the event submission.

The MVP runs in one Python service beside the existing pipeline; it does not need a custom ingest graph, training a model, metric calibration, re-identification, or live-camera recording. W&B drafts are two-pass, caption-backed and reviewed by a human. An ambiguous draft is rejected rather than scored as truth.

Demo differentiator: a judge makes a decision **before** seeing the answer. Then a contrasting clip shows why the same visible cue can lead to a different continuation. The product converts passive archive search into an active learning loop.
