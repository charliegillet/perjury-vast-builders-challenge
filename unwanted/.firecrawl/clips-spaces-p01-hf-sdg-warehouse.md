Dataset Viewer

The dataset viewer is not available for this subset.

Job has been terminated due to a temporary spike in resource usage and may be restarted later.

Need help to make the dataset viewer work? Make sure to review [how to configure the dataset viewer](https://huggingface.co/docs/hub/datasets-data-files-configuration), and [open a discussion](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/discussions/new?title=Dataset+Viewer+issue&description=The+dataset+viewer+is+not+working.%0A%0Acc+%40lhoestq+%40cfahlgren1.) for direct support.

# PhysicalAI SDG-Warehouse

[![Hero — four warehouse-safety scenarios in synchronized multi-view simulation.](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/resolve/main/assets/hero_2x2.webp)](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/blob/main/assets/hero_2x2.webp)

PhysicalAI SDG-Warehouse is a synthetic, fully-annotated video dataset of staged industrial-safety events captured in a simulated warehouse environment. It contains approximately 123k video clips, totaling roughly 412 hours of footage at 1920x1080 resolution and 30 frames per second, organized across four scenarios: a forklift near-miss with a human worker, a warehouse fire with worker evacuation, a forklift collision with a storage shelf, and a routine box-pickup action. Every multi-camera simulation run is filmed from 5 to 10 synchronized viewpoints, and the entire pipeline is reproducible end-to-end from a single random seed.

This dataset is described in Appendix C.5 of the Cosmos3 technical report. This dataset is ready for commercial or non-commercial uses.

## Overview

The release is packaged as standard [WebDataset](https://github.com/webdataset/webdataset) tar shards, with one sample per simulation run. Inside each shard, all of a run's synchronized camera views share the same sample key, so a single iteration of the dataset yields a complete multi-view group together with its run-level metadata. The shards are sized at approximately 5GBs each, which is optimized for streaming directly into a training loop without first materializing the full dataset on disk.

The dataset is published in two complementary tiers under the same repository, joinable per-sample on `run_id`:

- The **RGB tier** (`rgb/`) contains the photoreal RGB video for every camera in every run, plus per-run metadata files (`meta.json` and `metadata.txt`) embedded inside each shard. It is 459 shards totaling approximately 2.24 TiB, and is the right entry point for video generation, video understanding, and any workflow that does not need pixel-level supervision.
- The **artifacts tier** (`artifacts/`) contains the full annotation stack for the same runs: metric depth, colorized instance segmentation, shaded segmentation, and canny edges as MP4 videos; the raw per-frame integer-id instance-segmentation arrays consolidated to a single compressed NPZ per camera; the per-camera consolidated `camera_params.jsonl` and `object_detection.jsonl` files with two- and three-dimensional bounding boxes and per-frame intrinsics and extrinsics; and the source RGB MP4s repeated in the same shard so that the artifacts tier is self-contained. The artifacts tier totals approximately 16.33 TiB across all four scenarios.

Two small Parquet indexes — `metadata/runs.parquet` (one row per run) and `metadata/clips.parquet` (one row per camera-clip) — enable filtering by scenario, seed, camera, or source kind without opening a single shard.

## Dataset at a glance

**Dataset owner(s).** NVIDIA Corporation.

**Dataset creation date.** 2026-05.

**Version.**
v1.0

Previous Version(s): None.

**License / terms of use.** This dataset is released under the [OpenMDW1.1](https://openmdw.ai/)

**Intended usage.** SDG-Warehouse is intended for research and development of physical-AI models — including but not limited to video understanding (action recognition, anomaly and incident detection, multi-camera person re-identification, worker activity recognition), pixel-level perception (monocular depth estimation, instance segmentation, edge prediction, 2D and 3D object detection and tracking), video generation and world modeling (text-to-video, conditional video generation, long-horizon prediction), and policy or planning research that benefits from controllable, reproducible safety-event footage. It is also a useful resource for studying sim-to-real transfer in warehouse and industrial settings, and as a controlled benchmark for evaluating model robustness across viewpoints, lighting, and agent appearance.

**Dataset characterization.**

- _Data collection method._ Synthetic. All footage was rendered in NVIDIA Isaac Sim using the Isaac Replicator Object and Isaac Replicator Agent components; no real-world footage was captured or used.
- _Labeling method._ Synthetic / Automated. All ground-truth annotations (depth, segmentation, edges, bounding boxes, camera parameters) are generated by the Isaac Sim Replicator pipeline as a deterministic byproduct of rendering. No human labeling was used.

**Dataset format.**

- _Modalities._ Video (photoreal RGB and 4 rendered annotation modalities — colorized metric depth, colorized instance segmentation, shaded segmentation, canny edges), per-frame integer-id instance-segmentation arrays, per-frame structured annotations (2D and 3D bounding boxes, camera intrinsics and extrinsics).
- _Container and codec._ MP4 (H.264) at 1920 × 1080, 30 fps, for both RGB and annotation videos.
- _Structured annotations._ JSON Lines (one JSON object per frame), consolidated per camera per run into `camera_params.jsonl` and `object_detection.jsonl`.
- _Raw instance ids._ NumPy compressed archive (`.npz`), one per camera per run, containing `frames` (`uint8[T, H, W, 4]`, the 4 channels encoding the integer id) and `frame_indices` (`int32[T]`).
- _Run-level metadata._ JSON (`meta.json`) and plain text (`metadata.txt`), embedded inside each WebDataset shard.
- _Packaging._ [WebDataset](https://github.com/webdataset/webdataset) tar shards, approximately 5GBs each, with one WebDataset sample per simulation run.
- _Indexes._ Apache Parquet — `metadata/runs.parquet` (one row per run) and `metadata/clips.parquet` (one row per camera-clip).

**Dataset quantification.**

- _Record count._ 122,967 camera-clips drawn from 29,195 multi-camera simulation runs (WebDataset samples). Aggregate footage is approximately 412 hours.
- _Feature count._ Per camera-clip, the dataset provides 5 video modalities (RGB, depth, instance segmentation, shaded segmentation, canny edges), 1 raw integer-id NPZ, and 2 structured-annotation JSONL files; per frame, the structured annotations contain 2D bounding boxes (both tight and loose axis-aligned), 3D oriented bounding boxes, and full camera intrinsics and extrinsics.
- _Total data storage._ Approximately 18.57 TiB: the RGB tier is approximately 2.24 TiB (459 shards) and the artifacts tier is approximately 16.33 TiB (5,261 shards).

## Why this dataset

Real footage of warehouse safety incidents is operationally rare, logistically difficult to capture at scale, and legally sensitive to redistribute. Even when such footage exists, it is almost never paired with the kind of dense, per-pixel ground truth that physical-AI training pipelines benefit from: depth, instance identity, segmentation, edges, and tracked bounding boxes for every visible agent and prop. Building a real-world dataset that covers all of these signals across a balanced mix of incident types is, in practice, infeasible.

We therefore generate the dataset in simulation. In a simulator, the event is guaranteed to happen, every event parameter is exposed and controllable, every camera viewpoint is precisely registered, and every frame is automatically paired with deterministic ground truth. Domain randomization over lighting, materials, asset choice, agent identity, agent motion, camera pose, and event parameters provides the variability that real-world capture would otherwise contribute. This approach lets us cover rare or operationally dangerous events — near-misses, evacuations, and rigid-body collisions — at scale, while keeping the dataset reproducible and extensible.

## Quickstart

Pulling a single scenario (RGB only) is the recommended starting point for most users, since each scenario's RGB tier is a few hundred GBs:

```bash
pip install -U "huggingface_hub[hf_xet]"

huggingface-cli download nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes \
  --repo-type dataset \
  --include "rgb/forklift_human_nearmiss/**" "metadata/**" \
  --local-dir ./PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes
```

The RGB and artifact tiers per scenario are summarized below.

| Scenario | RGB path | RGB shards | RGB size | Artifacts path | Artifact shards | Artifact size |
| --- | --- | --: | --: | --- | --: | --: |
| Forklift–human near-miss | `rgb/forklift_human_nearmiss/` | 113 | 549 GiB | `artifacts/forklift_human_nearmiss/` | 547 | 2.46 TiB |
| Warehouse fire | `rgb/warehouse_fire/` | 125 | 619 GiB | `artifacts/warehouse_fire/` | ~432 | ~1.93 TiB |
| Forklift–shelf collision | `rgb/forklift_shelf_collision/` | 114 | 559 GiB | `artifacts/forklift_shelf_collision/` | 2,989 | 6.80 TiB |
| Warehouse box pickup | `rgb/warehouse_box_pickup/` | 107 | 520 GiB | `artifacts/warehouse_box_pickup/` | 1,293 | 5.14 TiB |

The RGB tier totals approximately 2.24 TiB; the artifacts tier totals approximately 16.33 TiB. To pull a scenario together with its annotations, include both `rgb/<scenario>/**` and `artifacts/<scenario>/**`. For streaming pipelines that never materialize the data on disk, see [Loading examples](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes#loading-examples).

## Scenarios

Each scenario stages a different self-contained event inside a shared warehouse environment with shelves and props. Scenarios differ in which agents are spawned, what event is staged, and how the cameras are placed.

### Forklift–human near-miss

A worker stands at a fixed location while a forklift navigates along a planned path toward the same location. A configurable last-moment dodge distance distinguishes a near-miss from a direct-contact event, so the same scene composition can produce both event classes by varying a single parameter.

[![Forklift–human near-miss — full 10-second run shown across all 5 modalities (left to right: RGB, depth, instance segmentation, shaded segmentation, canny edges).](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/resolve/main/assets/clip_nearmiss.webp)](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/blob/main/assets/clip_nearmiss.webp)

### Warehouse fire

A localized volumetric fire ignites at a randomized position and time while a small crew of workers performs random walks. On ignition, each worker reacts: it orients toward the flame and then runs toward a designated exit waypoint along a navigation-mesh path. The result is rare emergency-response footage that combines dynamic flames, smoke, and coordinated human evacuation in a single shot. Cameras are placed at ceiling height to maximize floor coverage.

[![Warehouse fire — full 10-second run, ignition followed by coordinated evacuation, shown across all 5 modalities (left to right: RGB, depth, instance segmentation, shaded segmentation, canny edges).](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/resolve/main/assets/clip_fire.webp)](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/blob/main/assets/clip_fire.webp)

### Forklift–shelf collision

A forklift drives at a parameterized initial distance toward a storage shelf and impacts it, producing visible rigid-body knock-over and debris dynamics. An optional character can be placed along the forklift's path to extend the scenario to a three-body forklift–shelf–human event. Cameras are placed circularly around the impact site at varying heights, distances, and look-down angles.

[![Forklift–shelf collision — full 15-second run, drive into the shelf and ensuing debris, shown across all 5 modalities (left to right: RGB, depth, instance segmentation, shaded segmentation, canny edges).](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/resolve/main/assets/clip_forklift_collision.webp)](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/blob/main/assets/clip_forklift_collision.webp)

### Warehouse box pickup

A worker navigates to a randomly placed box, performs a contact-rich pickup motion, and carries the box through the warehouse. This scenario provides routine, non-incident action coverage as a counterpoint to the 3 safety scenarios. The camera rig is a mixed CCTV and eye-level configuration.

[![Warehouse box pickup — full 15-second run, walk plus contact-rich pickup plus carry, shown across all 5 modalities (left to right: RGB, depth, instance segmentation, shaded segmentation, canny edges).](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/resolve/main/assets/clip_box_pickup.webp)](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/blob/main/assets/clip_box_pickup.webp)

## Multi-view coverage

Every multi-camera simulation run is captured from 5 to 10 synchronized cameras. For the near-miss scenario, the rig consists of 5 ceiling-mounted CCTV-style cameras and 5 worker-height eye-level cameras, all pointed at the interaction. The figure below shows a single near-miss run from each of the 10 viewpoints; because all cameras share a clock and the same scene, the same instant in time appears across all 10 frames.

[![Multi-view coverage — one near-miss run from 10 synchronized cameras: 5 ceiling and 5 eye-level.](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/resolve/main/assets/multiview_grid.png)](https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/blob/main/assets/multiview_grid.png)

For the fire scenario, the rig is 5 ceiling cameras only. For the forklift–shelf collision, 6 cameras are arranged circularly around the impact site at varying heights and look-down angles. For the box-pickup scenario, the rig is a mixed CCTV plus eye-level configuration with 10 cameras.

## Ground-truth modalities

The synthetic origin of the dataset gives us access to deterministic, pixel-aligned ground truth for every frame, rendered directly by the simulator. 4 annotation modalities are exported as video alongside each RGB clip:

- **Depth** (`depth.mp4`): log-normalized colorized metric depth. Each pixel's color encodes the absolute distance from the camera in metres, convertible to a full depth map using the per-frame camera intrinsics.
- **Instance segmentation** (`segmentation.mp4`): each pixel is colorized by its instance ID, so every distinct agent and prop in the scene has a unique, consistent color across all frames.
- **Shaded segmentation** (`shaded_seg.mp4`): the same per-pixel instance identity rendered with surface-normal-based shading, preserving object boundaries and surface orientation while keeping per-instance identity visible.
- **canny edges** (`edges.mp4`): a canny edge map computed on the shaded segmentation, giving clean, noiseless structural outlines.

In addition, every run ships 2 types of structured per-frame annotations per camera:

- **`object_detection.jsonl`**: one JSON object per frame (one line per frame). Each object contains a list of detected agents and props, each with a class label, a 2D tight axis-aligned bounding box, a 2D loose axis-aligned bounding box, and an oriented 3D bounding box (center, dimensions, and rotation) in world coordinates.
- **`camera_params.jsonl`**: one JSON object per frame (one line per frame). Each object contains the camera intrinsics (focal lengths `fx`, `fy`, principal point `cx`, `cy`) and extrinsics (world-to-camera rotation matrix and translation vector), enabling projection between 3D world coordinates and 2D pixel space.

The raw per-pixel instance IDs are also available as a **compressed NumPy archive** (`instance_id_segmentation.npz`) per camera per run, containing 2 arrays:

- `frames`: shape `[T, H, W, 4]`, dtype `uint8`. The 4 channels (RGBA) together encode a 32-bit integer instance ID per pixel (`id = R + G×256 + B×65536 + A×16777216`). An ID of 0 means background. Each unique non-zero ID corresponds to a single tracked agent or prop, consistent across all frames of the run.
- `frame_indices`: shape `[T]`, dtype `int32`. The original frame numbers from the simulation run, useful when the exported clip is a trimmed or subsampled window of the full simulation.

## Dataset statistics

| Scenario | Number of clips | Number of runs (WebDataset samples) | Clip length | Cameras per run | Repository path |
| --- | --: | --: | --: | --: | --- |
| Forklift–human near-miss | 27,939 | 13,410 | 10 seconds | 10 | `rgb/forklift_human_nearmiss/` |
| Warehouse fire | 44,734 | 9,064 | 10 seconds | 5 | `rgb/warehouse_fire/` |
| Forklift–shelf collision | 24,617 | 4,120 | 15 seconds | 6 | `rgb/forklift_shelf_collision/` |
| Warehouse box pickup | 25,677 | 2,601 | 15 seconds | 10 | `rgb/warehouse_box_pickup/` |
| **Total** | **122,967** | **29,195** | — | — | — |

## Simulation pipeline

All 4 scenarios are built on NVIDIA Isaac Sim. Procedural scene composition — warehouse layout, shelf placement, prop variation, and per-light randomization of color temperature, intensity, exposure, and color — is handled by the Isaac Sim Replicator Object component. Agent and sensor population — worker spawning and behavior, forklift placement and navigation, and the camera rigs that define the dataset's multi-view viewpoints — is handled by the Isaac Sim Replicator Agent component. Camera placement is parametric, with height, distance, and look-down angle sampled per run. Worker assets and motions are sampled from Isaac Sim's character library to diversify human appearance and gait.

Each simulation run is seeded with a unique random seed that controls every randomized variable: scene composition, lighting, agent identity, agent motion, camera pose, and event timing. The seed is recorded in the Parquet indexes (and inside each shard's `meta.json`), so any individual run is fully reproducible from this dataset alone, and the same pipeline can be extended to additional scenarios outside this release without modification.

## Repository layout

```
nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/
├── README.md
├── assets/                     ← images used by this dataset card
├── metadata/
│   ├── runs.parquet            ← one row per WebDataset sample (run), with
│   │                             scenario, seed, source_kind, n_cameras,
│   │                             total_bytes, shard_path_in_repo, clip_keys
│   ├── clips.parquet           ← one row per (run × camera), with hash_filename,
│   │                             camera_alias, source_rgb_s3, size, etc.
│   └── manifests/              ← provenance copies of the source-S3 manifests
├── rgb/                        ← RGB tier (~2.24 TiB)
│   ├── forklift_human_nearmiss/    (113 shards, ~5GBs each)
│   ├── warehouse_fire/             (125 shards)
│   ├── forklift_shelf_collision/   (114 shards)
│   └── warehouse_box_pickup/       (107 shards)
└── artifacts/                  ← artifacts tier (~16.33 TiB)
    ├── forklift_human_nearmiss/    (547 shards, ~5GBs each)
    ├── warehouse_fire/             (~432 shards)
    ├── forklift_shelf_collision/   (2,989 shards)
    └── warehouse_box_pickup/       (1,293 shards)
```

Each `.tar` is a WebDataset archive. The 2 tiers share the same `__key__` (the `run_id`) so that joining them only requires opening the corresponding shard in each tier.

**RGB tier sample.** Every sample is a group of entries that share the run\_id stem, plus one MP4 per camera:

```
fd7cc35596b247b16b0b_run_8_seed_864110064.meta.json
fd7cc35596b247b16b0b_run_8_seed_864110064.metadata.txt
fd7cc35596b247b16b0b_run_8_seed_864110064.ceiling_00.rgb.mp4
fd7cc35596b247b16b0b_run_8_seed_864110064.ceiling_01.rgb.mp4
…
fd7cc35596b247b16b0b_run_8_seed_864110064.eye_04.rgb.mp4
```

**Artifacts tier sample.** Same `__key__`. Per camera, the tier ships the modality MP4s, the consolidated integer-id NPZ, and the 2 consolidated JSONL files; the RGB MP4 is repeated so each artifacts shard is self-contained:

```
fd7cc35596b247b16b0b_run_8_seed_864110064.meta.json
fd7cc35596b247b16b0b_run_8_seed_864110064.ceiling_00.rgb.mp4
fd7cc35596b247b16b0b_run_8_seed_864110064.ceiling_00.depth.mp4
fd7cc35596b247b16b0b_run_8_seed_864110064.ceiling_00.segmentation.mp4
fd7cc35596b247b16b0b_run_8_seed_864110064.ceiling_00.shaded_seg.mp4
fd7cc35596b247b16b0b_run_8_seed_864110064.ceiling_00.edges.mp4
fd7cc35596b247b16b0b_run_8_seed_864110064.ceiling_00.instance_id_segmentation.npz
fd7cc35596b247b16b0b_run_8_seed_864110064.ceiling_00.camera_params.jsonl
fd7cc35596b247b16b0b_run_8_seed_864110064.ceiling_00.object_detection.jsonl
… (repeated for each camera)
```

WebDataset readers yield one Python dictionary per run. For the RGB tier the dictionary has `__key__`, `meta.json`, `metadata.txt`, and one `{camera_alias}.rgb.mp4` per camera. For the artifacts tier the dictionary additionally has the 4 modality MP4s, the NPZ, and the 2 JSONL files per camera.

## Loading examples

### Stream directly from the Hub with WebDataset

The following example streams the fire scenario directly from the Hub using the standard WebDataset reader. Nothing is materialized on disk apart from the bytes that the iterator actually consumes.

```python
import os
import webdataset as wds
from huggingface_hub import get_token

token = get_token() or os.environ["HF_TOKEN"]
url = (
    "pipe:curl -s -L "
    "'https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes/resolve/main"
    "/rgb/warehouse_fire/fire-rgb-{00000..00124}.tar' "
    f"-H 'Authorization: Bearer {token}'"
)

dataset = wds.WebDataset(url, shardshuffle=True).decode()
for sample in dataset.shuffle(1000):
    run_id = sample["__key__"]
    meta = sample["meta.json"]            # dict: scenario, seed, cameras, etc.
    rgb_bytes = sample["ceiling_00.rgb.mp4"]  # raw mp4 bytes; decode with av/ffmpeg
    camera_keys = sorted(k for k in sample if k.endswith(".rgb.mp4"))
    print(run_id, meta["seed"], camera_keys)
    break
```

### Filter with the Parquet index, then fetch only the shards you need

`metadata/runs.parquet` contains one row per simulation run, with columns `scenario`, `seed`, `source_kind`, `n_cameras`, `total_bytes`, `shard_path_in_repo`, and `clip_keys`. `metadata/clips.parquet` contains one row per camera-clip, with columns `scenario`, `camera_alias`, `seed`, `source_kind`, `shard_path_in_repo`, `hash_filename`, and `size`. Use these indexes to select exactly the runs or clips you need and retrieve only the relevant shard files, without downloading the full dataset.

```python
import pandas as pd
from huggingface_hub import hf_hub_download

clips = pd.read_parquet(
    hf_hub_download(
        repo_id="nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes",
        repo_type="dataset",
        filename="metadata/clips.parquet",
    )
)

# Inspect available scenario names:
# print(clips.scenario.unique())

# All ceiling-camera views from near-miss runs with an even seed:
selection = clips[\
    (clips.scenario == "forklift_human_nearmiss")\
    & (clips.camera_alias.str.startswith("ceiling_"))\
    & (clips.seed.notna()) & (clips.seed % 2 == 0)\
]
unique_shards = sorted(selection.shard_path_in_repo.unique())
print(f"{len(selection):,} clips across {len(unique_shards)} shards")
```

### Pull one scenario only with the CLI

To pull RGB only:

```bash
huggingface-cli download nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes \
  --repo-type dataset \
  --include "rgb/warehouse_box_pickup/**" "metadata/**" \
  --local-dir ./PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes
```

To pull RGB plus the matching artifacts (depth, segmentation, shaded segmentation, canny edges, instance-id NPZ, and per-frame camera and bounding-box JSONL):

```bash
huggingface-cli download nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes \
  --repo-type dataset \
  --include "rgb/warehouse_box_pickup/**" \
            "artifacts/warehouse_box_pickup/**" \
            "metadata/**" \
  --local-dir ./PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes
```

### Pull a single shard programmatically

```python
from huggingface_hub import hf_hub_download

local_rgb = hf_hub_download(
    repo_id="nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes",
    repo_type="dataset",
    filename="rgb/forklift_human_nearmiss/nearmiss-rgb-00000.tar",
)
local_artifacts = hf_hub_download(
    repo_id="nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes",
    repo_type="dataset",
    filename="artifacts/forklift_human_nearmiss/nearmiss-artifacts-00000.tar",
)
```

## Known limitations and future work

The dataset is fully synthetic and exhibits a sim-to-real gap. Compared to real warehouse footage, the rendered material can have a computer-graphics-like appearance, simplified material response, and limited fidelity in volumetric effects such as smoke and fire. Models trained on the dataset should be carefully evaluated on real footage before being deployed in any safety-critical setting.

Agent motion is driven by procedural navigation and behavior, so reactions — and in particular the coordinated evacuation behavior in the fire scenario — can occasionally appear unnatural. Rigid-body interactions between the forklift and the storage shelves are physically simulated, but very fine-grained debris, deformation, and secondary contact effects are approximate.

The current release is concentrated on a single warehouse layout family. Future work will broaden environment diversity to additional warehouse, retail, and factory floor plans, will add additional incident types such as spills, dropped pallets, and shelf collapses without forklift involvement, and will broaden variation in worker attire and personal protective equipment.

## Citation

If you use SDG-Warehouse in your research, please cite the dataset itself as well as the Cosmos3 technical report it accompanies:

```bibtex
@dataset{dadhich2026sdgwarehouse,
  title        = {PhysicalAI SDG-Warehouse: A Synthetic Multi-View Video Dataset of Industrial-Safety Events},
  author       = {Dadhich, Nalin},
  year         = {2026},
  publisher    = {NVIDIA},
  howpublished = {\url{https://huggingface.co/datasets/nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes}}
}

@techreport{nvidia2026cosmos3,
  title       = {Cosmos 3: Omnimodal World Models for Physical AI},
  author      = {{NVIDIA}},
  year        = {2026},
  institution = {NVIDIA}
}
```

## Contact

Please reach out to the main author Nalin Dadhich ( [ndadhich@nvidia.com](mailto:ndadhich@nvidia.com)) for further enquiries.

## Ethical considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal developer teams to ensure this dataset meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report model quality, risk, security vulnerabilities or NVIDIA AI concerns [here](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail).

Copy to bucket new

Downloads last month

27,459

Total file size:

24.1 TB

## Collections including nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes

[Collection of open, commercial-grade datasets for physical AI developers•57 items•Updated Aug 11• 182](https://huggingface.co/collections/nvidia/physical-ai)

[11 items•Updated 8 days ago](https://huggingface.co/collections/nvidia/cosmos3-datasets)

## Article mentioning nvidia/PhysicalAI-WorldModel-Synthetic-Warehouse-Operations-Scenes

[**Welcome NVIDIA Cosmos 3: The First Open Omni-model for Physical AI Reasoning and Action**\\
\\
- ![](https://cdn-avatars.huggingface.co/v1/production/uploads/65df9200dc3292a8983e5017/Vs5FPVCH-VZBipV3qKTuy.png)\\
\\
nvidia\\
\\
•\\
\\
Jun 1\\
\\
• 90](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai)