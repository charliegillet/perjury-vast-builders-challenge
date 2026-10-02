[Skip to content](https://www.aicitychallenge.org/2026-track1/#content)

## 2026 Challenge Track Description

_**Track 1: Multi-Camera 3D Perception (Sim2Real)**_

- ## **Overview**


Challenge Track 1 tackles multi-camera 3D perception in large-scale indoor environments, requiring participants to detect and track people and mobile objects, including autonomous mobile robots (AMRs), humanoids, forklifts, and pallet trucks while maintaining consistent identities within and across all cameras in a scene.

Building on the 2025 edition, which introduced over 500 synthetic camera views generated via NVIDIA Omniverse along with 2D/3D bounding boxes, depth maps, and detailed calibration metadata, the 2026 edition advances the benchmark in three key directions. First, the synthetic training corpus is further expanded in scene diversity and annotation fidelity, now generated using the[Isaacsim.Replicator.Agent (IRA)](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_agent.html) and [Isaacsim.Replicator.Object (IRO)](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_object.html) extensions on the NVIDIA Omniverse platform, as well as Cosmos Transfer 2.5 (CT2.5), covering diverse warehouse layouts; participants are allowed to generate more data using these tools. Second, **real-world test sets** are introduced to explicitly evaluate **Sim2Real generalization**, pushing participants beyond purely synthetic benchmarks toward deployable perception systems. Third, depth maps are provided only for training and validation; participants must develop models that rely solely on RGB inputs at inference time, reflecting the limited availability of depth data in real-world CCTV scenarios.

Evaluation continues to use the 3D Higher Order Tracking Accuracy (HOTA) metric, which jointly balances detection, association, and localization quality. Submissions demonstrating **online tracking**, relying only on past-frame information, receive a **+10% multiplicative bonus** when determining the final winner and runner-up.

- ## **Task**


Teams should detect every object and keep the **same identity ID** while they move **within and across all cameras in a scene**.

- ## **Submission Format**


For compatibility with the official evaluation server, results must be a single **plain-text file** (track1.txt) where each line describes one detection:

〈scene\_id〉 〈class\_id〉〈object\_id〉〈frame\_id〉〈x〉〈y〉〈z〉〈width〉〈length〉〈height〉〈yaw〉

|     |     |     |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| scene\_id | int | Unique identifier for each multi-camera sequence. |
| class\_id | int | Starting from zero, denoting an object’s category. (Person→0, Forklift→1, NovaCarter→2, Transporter→3, FourierGR1T2→4, AgilityDigit→5, PalletTruck→6.) |
| object\_id | int | Positive, unique ID per scene & class. Remains constant across all cameras within the same scene and class. |
| frame\_id | int | Zero-based frame index **within that scene.** |
| x, y, z, | float | 3D coordinates of the bounding-box centroid in the world coordinate system which is in meters. |
| width, length, height | float | Box dimensions in meters along its x (width), y (length) and z (height) axes of the object-centered coordinate system, with the origin at the centroid. |
| yaw | float | Euler angle in radians about the y-axis of the object-centered coordinate system defining the box’s heading in the world coordinate system. (Pitch and roll are assumed zero.) |

![](https://www.aicitychallenge.org/wp-content/uploads/2025/04/aic25_track1_figure1.png)

Example: in scene 0, if a Person is assigned obj\_id = 5, then a Forklift cannot use obj\_id = 5 (it must use a different ID, e.g. 6).

Archive the text file as _**track1.zip**_ or **_track1.tar.gz_** before uploading.

**Important note on the submission file:**

- All floating-point numbers in the submission file must be rounded to **two decimal places**.
- The file size limit for each submission is **50 MB**.

- ## **Evaluation**


Scores are computed with **3D HOTA** \[1\], which jointly balances detection, association and localization quality. HOTA score will be computed per class within a scene which will be averaged. A weighted average will then be computed on these scores across all scenes based on the total no. of objects. 3D IoU will be used for matching GT & prediction objects.

- **Leaderboard** = raw HOTA on the hidden test set.
- **Online-tracker bonus**: If your paper + code prove that **only past frames** are used, a **+10 %** multiplicative bonus is applied _when deciding the final winner and runner-up_ (the public leaderboard itself shows the un-bonused score).

Example: Team A (offline) = 66 % HOTA; Team B (online) = 61 % ⇒ bonus → 67.1 % HOTA. Team B ranks higher in the final award list.

- ## **Data Access**

  - README: [https://huggingface.co/datasets/nvidia/PhysicalAI-SmartSpaces/blob/main/README.md](https://huggingface.co/datasets/nvidia/PhysicalAI-SmartSpaces/blob/main/README.md)
  - Train: [https://huggingface.co/datasets/nvidia/PhysicalAI-SmartSpaces/tree/main/MTMC\_Tracking\_2026/train](https://huggingface.co/datasets/nvidia/PhysicalAI-SmartSpaces/tree/main/MTMC_Tracking_2026/train)
  - Val: [https://huggingface.co/datasets/nvidia/PhysicalAI-SmartSpaces/tree/main/MTMC\_Tracking\_2026/val](https://huggingface.co/datasets/nvidia/PhysicalAI-SmartSpaces/tree/main/MTMC_Tracking_2026/val)

| **Split** | **Hours** | **Cameras** | **Scenes** | **Resolution / FPS** | **Objects in Training GT\*** | **File Size** |
| --- | --- | --- | --- | --- | --- | --- |
| Train + Val | 28.5 | 342 | 26 warehouse layouts from both IsaacSim and CT2.5 | 1080 p @ 30 fps | 1,379 instances (901 person + service robots / forklifts / pallet trucks) | ~50 GB ( depth maps optional, ~3 TB) |

\\* Counts refer to the **training + validation** ground-truth only; the test split is hidden before the release of the evaluation system.

\\* Teams are allowed to train with 2024 and 2025 data, as well as external public data.

Each scene provides temporally-synchronized RGB video, camera calibration, a top-down map, and per-frame 2D/3D annotations. Depth maps (PNG-in-HDF5) are included but very large; feel free to ignore them if storage or I/O is a concern, and download only the other files using Hugging Face CLI.

_By downloading you agree to the Physical AI Smart Spaces licence (CC-BY 4.0)._

References

\[1\] J. Luiten _et al._, “HOTA: A Higher Order Metric for Evaluating Multi-Object Tracking,” _IJCV_, 2021.

- [HOME](https://www.aicitychallenge.org/)
- [2018 CHALLENGE](https://www.aicitychallenge.org/2018-ai-city-challenge/)
- [WORKSHOP](https://www.aicitychallenge.org/2018-workshop/)
- CHALLENGE
▼

  - [Challenge Tracks](https://www.aicitychallenge.org/2018-challenge-tracks/)
  - [2018 Data and Evaluation](https://www.aicitychallenge.org/2018-data-sets/)
  - [Challenge Awards](https://www.aicitychallenge.org/2018-challenge-awards/)
  - [Winners](https://www.aicitychallenge.org/2018-winners/)
  - [GitHub Repos](https://github.com/NVIDIAAICITYCHALLENGE)
- INFO
▼

  - [Data Access Instructions](https://www.aicitychallenge.org/2018-participant-instructions/)
  - [Organizing Committee](https://www.aicitychallenge.org/2018-organizing-committee/)
  - [Important Dates](https://www.aicitychallenge.org/2018-important-dates/)
  - [Paper Reviewers](https://www.aicitychallenge.org/2018-paper-reviewers/)
  - [CVPR Workshop](http://cvpr2018.thecvf.com/program/workshops)
- [FAQs\\
▼](https://www.aicitychallenge.org/2018-faq/)
  - [General](https://www.aicitychallenge.org/?page_id=57#general)
  - [Track 1](https://www.aicitychallenge.org/?page_id=57#q1)
  - [Track 2](https://www.aicitychallenge.org/?page_id=57https://www.aicitychallenge.org/?page_id=57#q2)
  - [Track 3](https://www.aicitychallenge.org/?page_id=57#q3)