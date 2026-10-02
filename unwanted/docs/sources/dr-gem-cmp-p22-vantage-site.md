# VANTAGE-Bench

Video ANalysis Tasks Across Generalized Environments

Clemson University, School of Computing

[vantage.bench.competition@gmail.com](mailto:vantage.bench.competition@gmail.com)

A multi-task benchmark for evaluating Vision-Language Models on real-world fixed-camera footage across Warehouse, Transportation, and Smart Spaces, spanning Spatial, Spatio-Temporal, Temporal, and Semantic understanding.

[Paper](https://arxiv.org/pdf/2609.09396) [GitHub](https://github.com/Clemson-Capstone/VANTAGE-Bench) [Dataset](https://huggingface.co/datasets/nvidia/PhysicalAI-VANTAGE-Bench) [Leaderboard](https://huggingface.co/spaces/clemson-computing/VANTAGE-Bench-Leaderboard) [Submit predictions](https://vantage-bench.org/submit)

News

\[2026-06-01\]VANTAGE-Bench featured in Jensen Huang's keynote at NVIDIA GTC Taipei / Computex 2026 — Cosmos 3 named top open-weight model on VANTAGE-Bench for fixed-camera vision understanding

[↗ Read NVIDIA blog post](https://blogs.nvidia.com/blog/cosmos-3-physical-ai-open-world-foundation-model/)

\[2026-05-27\]Leaderboard live — zero-shot rankings published across all four reasoning pillars

\[2026-05-27\]Evaluation harness released — clone and run on GitHub

\[2026-04-24\]VANTAGE-Bench dataset released on Hugging Face

## Introduction

We introduce VANTAGE-Bench, a benchmark for evaluating vision-language models on fixed-camera operational video. Instead of internet video, egocentric clips, or broadcast footage, it focuses on real-world scenes from warehouses, intersections, and public spaces where the camera remains fixed and the model must reason from a stable vantage point.

VANTAGE-Bench contains 35,027 expert-curated annotations across 3,346 media assets. It spans three operational domains and four reasoning pillars across both image and video. The benchmark stands out for its domain relevance, modality breadth, task diversity, and evaluation novelty, culminating in the first quantitative single-object tracking benchmark for VLMs in fixed-camera operational footage.

![VANTAGE-Bench task taxonomy: three infrastructure AI domains mapped through four evaluation pillars to eight tasks](https://vantage-bench.org/assets/dataset_overview.png)

Task taxonomy and distribution of VANTAGE-Bench across three operational domains and four reasoning pillars.

![Representative prompts and expected answers for all eight VANTAGE-Bench tasks, grouped by reasoning pillar](https://vantage-bench.org/assets/task_examples.png)

Representative examples from all eight tasks, grouped by reasoning pillar. Each task pairs fixed-camera footage with its prompt format and expected answer.

The architecture of VANTAGE-Bench is driven by the fundamental disconnect between how VLMs are currently evaluated and how operational video systems actually work. Existing video benchmarks rely on a cinematic prior, with dynamic and human-centric framing, and reduce evaluation to a single format, typically multiple choice. VANTAGE-Bench addresses both limitations. It uses footage from fixed-infrastructure cameras that remove internet-video priors and extends evaluation beyond multiple choice to include generative dense captioning, precise coordinate prediction, and continuous spatio-temporal tracking. These are tasks that cannot be solved by selecting from a predefined set of answers.

## Leaderboard

Zero-shot evaluation of frontier and open-weight models across all four reasoning pillars. All models evaluated under identical conditions — greedy decoding, no chain-of-thought.

| # | Model | Overall | Spatial | Spatio-Temporal | Temporal | Semantic |
| --- | --- | --- | --- | --- | --- | --- |
| Obj Loc | Ref Exp | Pointing | SOT | Temp Loc | DVC | Event Ver | VQA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 🥇 | Gemini 3.6 Flash<br>new<br>Google  ·  proprietary✓ verified | 69.52 | 81.57 | 75.78 | 79.20 | 75.99 | 51.50 | 36.15 | 82.00 | 76.82 |
| 🥈 | GPT-5.6 Sol<br>new<br>OpenAI  ·  proprietary✓ verified | 68.04 | 69.30 | 69.44 | 81.90 | 75.02 | 55.71 | 37.28 | 76.14 | 78.08 |
| 🥉 | Cosmos3-Super· 64B<br>new<br>NVIDIA  ·  open-weight✓ verified | 63.62 | 86.97 | 76.23 | 72.94 | 64.66 | 51.90 | 29.54 | 71.28 | 69.46 |
| 4 | Gemini 3.1 Pro<br>Google  ·  proprietary✓ verified | 62.66 | 77.21 | 67.17 | 72.04 | 67.88 | 45.69 | 35.55 | 68.57 | 71.46 |
| 5 | Cosmos3-Nano· 16B<br>new<br>NVIDIA  ·  open-weight✓ verified | 60.67 | 74.11 | 75.57 | 74.83 | 59.21 | 48.04 | 31.42 | 68.88 | 68.95 |
| 6 | Qwen3-VL-32B-Instruct· 32B<br>Alibaba  ·  open-weight✓ verified | 55.38 | 72.67 | 72.39 | 75.62 | 44.19 | 46.80 | 29.40 | 60.04 | 71.30 |
| 7 | Cosmos-Reason2-8B· 8B<br>NVIDIA  ·  open-weight✓ verified | 54.46 | 83.88 | 70.26 | 68.60 | 37.69 | 47.30 | 32.50 | 64.09 | 67.95 |
| 8 | Gemini 3.5 Flash-Lite<br>new<br>Google  ·  proprietary✓ verified | 53.25 | 65.73 | 74.46 | 43.08 | 55.77 | 24.00 | 32.29 | 70.41 | 65.61 |

Bold = best in column  ·  ✓ verified = independently confirmed  ·  Updated 2026-09-10

[Submit your predictions →](https://vantage-bench.org/submit) [Click here to see full leaderboard →](https://huggingface.co/spaces/clemson-computing/VANTAGE-Bench-Leaderboard)

## Infrastructure AI

**Infrastructure AI** is a sub-domain of Physical AI focused on fixed-infrastructure cameras such as CCTV networks, elevated sensors, and wide-angle lenses. These systems are deployed for safety monitoring, access control, traffic understanding, and operational logging. Unlike Embodied AI, which centers on moving agents navigating environments, Infrastructure AI operates from a persistent, stationary vantage point.

VANTAGE-Bench is purpose-built for this setting. Its footage, drawn from warehouses, roads, and public spaces, comes from cameras that remain fixed. Models must reason from a wide-area, static perspective rather than from edited, human-centered video.

Frontier models are largely trained on internet-crawled data and are therefore biased toward standard photographic perspectives. Under fixed-camera conditions, this prior breaks down. Models must instead rely on spatial-temporal reasoning. A model can achieve state-of-the-art performance on internet video while still exhibiting dangerous performance deficits in the environments that matter most.

**No motion cues**

Fixed cameras produce no optical flow. Models trained on dynamic video cannot rely on motion to localize objects or events. They must reason spatially from static context alone.

**Dense, multi-instance scenes**

Distinguishing between dozens of identical pallets, vehicles, or pedestrians from an elevated oblique viewpoint requires precise spatial reasoning that internet-video training does not provide.

**Sparse, safety-critical events**

Events of interest occupy a tiny fraction of the timeline. Models must search through extended periods of inactivity to localize brief, high-stakes moments.

**No egocentric framing**

Without human-centric composition, standard photographic priors fail. Models must reason geometrically from wide-angle, elevated perspectives with no compositional guidance.

## Operational Domains

VANTAGE-Bench evaluates models across three structurally distinct deployment environments. Each domain requires different reasoning capabilities and exposes different failure modes in current VLMs.

W![Warehouse domain image](https://vantage-bench.org/assets/warehouse.png)

Warehouse

Dense logistics environments with structured layouts, repeated objects, and human-robot interaction. Footage from elevated fixed cameras captures forklift operations, pallet movements, worker activity, and access control.

Forklift trackingPallet localizationWorker detectionAccess controlRobot profiles

T![Transportation domain image](https://vantage-bench.org/assets/traffic.png)

Transportation

Roadside and intersection monitoring with multi-vehicle scenes. Fixed roadside cameras capture traffic flow, pedestrian crossings, and safety-critical events.

Vehicle detectionCollision verificationTraffic flowPedestrian crossing

SS![Smart Spaces domain image](https://vantage-bench.org/assets/smartspaces.png)

Smart Spaces

Unstructured public and semi-public environments with ambiguous human behavior. Models must reason about access control, tailgating, and crowd dynamics without structured interaction cues.

Crowd safetyAccess controlActivity detectionTailgating

## Dataset

Available on Hugging Face: [nvidia/PhysicalAI-VANTAGE-Bench →](https://huggingface.co/datasets/nvidia/PhysicalAI-VANTAGE-Bench)

VANTAGE-Bench was built around footage that is genuinely hard to source — specifically fixed-infrastructure cameras in real operational environments. Annotations were produced by trained professionals using domain-specific guidelines rather than crowdsourcing, and each annotation was reviewed by a secondary expert before inclusion.

Supplemental sources

Three targeted external sources supplement the core footage:

- **RefDrone** : aerial drone imagery used for 2D Referring Expressions, chosen for its elevated oblique perspective which mirrors fixed-camera conditions
- **PhysicalAI-SmartSpaces** : multi-camera warehouse sequences used for Single Object Tracking
- **NVIDIA Omniverse DRIVE Sim** : high-fidelity synthetic footage covering safety-critical collision scenarios absent from real-world data, used in approximately 20% of VQA and Temporal splits

| Task | Pillar | Annotations | Annotation type | Media | Modality |
| --- | --- | --- | --- | --- | --- |
| Event Verification | Semantic | 163 | Binary event labels | 163videos | Video |
| Video Question Answering | Semantic | 1,195 | 4-choice MCQ questions | 282videos | Video |
| 2D Referring Expressions | Spatial | 3,276 | Expression–box pairs | 1,503images | Image |
| 2D Spatial Pointing | Spatial | 1,005 | 4-choice coordinate MCQ | 361images | Image |
| 2D Object Localization | Spatial | 27,404 | Bounding boxes | 628images | Image |
| Temporal Localization | Temporal | 1,067 | Temporal segment labels | 203videos | Video |
| Dense Video Captioning | Temporal | 717 | Timestamped event captions | 104videos | Video |
| Single Object Tracking | Spatio-Temp | 200 | Object trajectories (8–32 frames) | 102videos | Interleaved |
| **Total** | — | 35,027 | — | 3,346 | Image + Video |

Privacy & ethics

All footage was collected in compliance with applicable privacy regulations. 70% of recordings were obtained with explicit informed consent from individuals; the remainder was captured in spaces with posted notice of camera operation, where presence constitutes acknowledgment of monitoring. All assets underwent automated PII obfuscation followed by manual human-in-the-loop verification before release. The dataset is released under the NVIDIA Evaluation Data License, which restricts use to evaluation and benchmarking and strictly prohibits biometric identification and demographic profiling.

## Task Taxonomy & Metrics

VANTAGE-Bench is organized around four reasoning pillars. Each pillar targets a capability that current VLMs handle well in internet-video settings, but struggle with when the camera stops moving.

Pillar I

### Semantic Understanding

Can the model understand what happened and why, not just what is visible?

Standard VLM benchmarks test whether a model can describe a scene. VANTAGE-Bench asks something harder: whether a model can reason causally about operational events in raw, unorchestrated footage — without the narrative structure that edited video provides. This means verifying that a tailgating incident actually occurred, or answering multi-step logical questions about untrimmed surveillance footage where the event of interest may occupy only seconds of a long recording.

| Task | Metric | Modality |
| --- | --- | --- |
| Event Verification | Macro F1 | Video |
| Video Question Answering | Top-1 Accuracy | Video |

Pillar II

### Spatial Understanding

Can the model localize the right object in a scene where everything looks the same?

Internet-video benchmarks evaluate spatial reasoning on well-lit, centered, distinct objects. Fixed-camera footage presents the opposite: dozens of identical pallets in a warehouse, a row of identical vehicles at an intersection, pedestrians in uniform from an overhead angle.

VANTAGE-Bench forces models to perform dense semantic disambiguation: grounding language to the correct object among many near-identical candidates, selecting precise coordinates, and detecting every instance of a class at once.

| Task | Metric | Modality |
| --- | --- | --- |
| 2D Referring Expressions | mIoU | Image |
| 2D Spatial Pointing | Top-1 Accuracy | Image |
| 2D Object Localization | F1@0.5 | Image |

Pillar III

### Temporal Understanding

Can the model find when something happened, not just whether it happened?

Existing temporal benchmarks use scripted, continuous human actions where the event dominates the timeline. Operational video is characterized by long quiescent periods; a warehouse camera may run for hours before a safety violation occurs.

VANTAGE-Bench requires models to search through this inactivity, predict exact event boundaries, and autonomously caption multiple events in chronological order with correct timing.

| Task | Metric | Modality |
| --- | --- | --- |
| Temporal Localization | mIoU | Video |
| Dense Video Captioning | SODAc | Video |

Pillar IV

### Spatio-Temporal Understanding

Novel

Can the model follow an object through time while preserving precise spatial grounding?

This is the hardest pillar and the one that exposes the deepest gap in current VLMs. Spatial reasoning and temporal reasoning are evaluated separately in every existing benchmark, but operational AI requires both simultaneously. VANTAGE-Bench introduces the first quantitative VLM tracking benchmark, filling a gap that no prior evaluation suite has addressed.

A model must not only know where an object is in a single frame, but maintain that spatial identity as the object moves, is partially occluded, or merges with similar-looking objects across dozens of frames.

| Task | Metric | Modality |
| --- | --- | --- |
| Single Object Tracking | Success AUC | Video (interleaved frames) |

SOT presents frames as interleaved image tokens in a single context window rather than as a continuous video stream. Sequences contain 8, 16, or 32 frames.

## Benchmark Comparison

How does VANTAGE-Bench fit into the existing evaluation landscape?

Most VLM benchmarks focus on a single reasoning dimension and typically cover only one modality. VANTAGE-Bench is the first benchmark to jointly evaluate all four reasoning dimensions across both image and video in a single suite.

Table 1 — Scope comparison

What this shows: how VANTAGE-Bench compares to the benchmarks it most directly relates to in terms of scale, modality coverage, and task diversity.

| Benchmark | Modality | \# Media | \# Annot. | Reasoning coverage | Annotation source |
| --- | --- | --- | --- | --- | --- |
| VideoMME | Video | 900 | 2,700 | Semantic only | Human |
| BLINK | Image | 3,683 | 1,906 | Spatial only | Human, Existing |
| RefCOCO avg. | Image | 3,982 | 30,969 | Spatial only | Human, Existing |
| ODinW-13 | Image | 4,608 | 10,966 | Spatial only | Human, Existing |
| Charades-STA | Video | 1,334 | 3,720 | Temporal only | Human, PL |
| ActivityNet Cap. | Video | 5,044 | 17,750 | Temporal only | Human |
| **VANTAGE-Bench** | Image + Video | 3,346 | 35,027 | All four pillars | Human + Synthetic + PL |

PL = programmatically generated labels from human-verified annotations
Table 1: VANTAGE-Bench is the only benchmark spanning all four reasoning dimensions across both image and video modalities.

### Does VANTAGE-Bench actually measure something different?

Yes, and by a significant margin. The table below compares the same model (Qwen3-VL-8B) on published scores on standard consumer-centric benchmarks against its scores on equivalent tasks in VANTAGE-Bench.

Table 2 — The performance gap

Qwen3-VL-8B zero-shot scores on the standard reference benchmark for each task vs. its score on the equivalent VANTAGE-Bench task. A negative gap means the model performs worse on VANTAGE-Bench. All scores are scaled 0–100.

| Task | Reference benchmark | Ref. score | VANTAGE score | Gap (∆) |
| --- | --- | --- | --- | --- |
| Semantic Understanding |
| Video Question Answering | VideoMME | 71.40 | 65.47 | -5.93 |
| Event Verification | MLVU | 78.10 | 48.14 | -29.96 |
| Spatial Understanding |
| 2D Spatial Pointing | BLINK | 69.10 | 45.54 | -23.56 |
| 2D Referring Expressions | RefCOCO | 89.10 | 71.55 | -17.55 |
| 2D Object Localization | ODinW-13 | 44.70 | 37.72 | -6.98 |
| Temporal Understanding |
| Temporal Localization | Charades-STA | 56.00 | 41.35 | -14.65 |
| Spatio-Temporal Understanding |
| Single Object Tracking | No prior benchmark exists | n/a | 31.44 | n/a |

Table 2: Performance gap for Qwen3-VL-8B across tasks. Negative values indicate degradation on VANTAGE-Bench relative to the standard reference benchmark for that task. The largest drops occur in Event Verification (−29.96) and 2D Spatial Pointing (−23.56), confirming that fixed-camera footage breaks priors that models rely on in consumer-centric settings. Single Object Tracking has no reference score because no prior VLM tracking benchmark exists. \* Qwen3-VL-8B scored 31.44 AUC on SOT; best overall is Gemini 3.1 Pro at 64.35 AUC.

## Citation

If you use VANTAGE-Bench, the leaderboard, or its evaluation resources in your research, please cite:

BibTeXCopy

```
@article{vantagebench2026,
  title   = {VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models},
  author  = {Bhat, Zaid Pervaiz and Nayyar, Nimra and Jain, Arihant and Chan, Lap Fung and Suchanek, John and Wang, Yu and Praveen, Varun and Kornuta, Tomasz and Murali, Vidya Nariyambut},
  journal = {arXiv preprint arXiv:2609.09396},
  year    = {2026}
}
```

## How to Evaluate

To evaluate your model on VANTAGE-Bench, use the official evaluation harness. The harness handles data loading, prompt formatting, and inference, and exports predictions in the required LLaVA submission format automatically.

Once inference is complete, archive your prediction files and submit through the submission portal. Our server scores predictions against held-out ground truth. Results are emailed to you after evaluation.

Full setup instructions, task-specific configurations, and format documentation are in the GitHub repository. Per-task prediction schemas are documented on the [submission page →](https://vantage-bench.org/submit)

[GitHub](https://github.com/Clemson-Capstone/VANTAGE-Bench) [Submit your predictions](https://vantage-bench.org/submit)