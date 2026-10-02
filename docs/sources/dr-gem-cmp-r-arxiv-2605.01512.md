Qwen3-VL’s type accuracy is 0.4620.462 on the 1,681 Pass-1-valid videos
(full-test C=0.474C{=}0.474 including the 17% physics fallback), well below its
spatial score, so we reassign typing to a second VLM. A 5 s clip spanning
\[t∗−3,t∗+2\]\[t^{\*}{-}3,\\,t^{\*}{+}2\] is extracted, spatially cropped around the Pass 1
center (x1,y1)(x\_{1},y\_{1}) at 2.5×2.5\\times box, and passed to
gemini-3.1-flash-lite-preview with a closed-world prompt that
enumerates 𝒞\\mathcal{C} and forbids abstention. On API failure we fall back
to c1c\_{1}. We crop around the Pass-1 center (x1,y1)(x\_{1},y\_{1}) rather than the
merged (x∗,y∗)(x^{\*},y^{\*}) because Pass 1 provides a more stable coarse region
for type classification. This split lifts full-test type accuracy from 0.4740.474 to 0.5910.591
(+25%+25\\% relative) at one extra API call per video.
## 4 Experiments

Table 1: Main results on ACCIDENT (2,027 real CCTV videos), official
evaluator at σt=1\\sigma\_{t}{=}1. Kaggle baselines \[ [11](https://arxiv.org/html/2605.01512#bib.bib2 "")\];
Naive/Molmo-7B/Best-of-baselines/Human from \[ [14](https://arxiv.org/html/2605.01512#bib.bib1 "")\].
T,S,CT,S,C: dataset-level means; ACCS\\mathrm{ACC}^{S}: per-video HM averaged
(leaderboard-reported for ours); CIs from 1,0001{,}000 bootstrap resamples.
| Method | TT | SS | CC | ACCS\\mathrm{ACC}^{S} |
| Optical Flow \[ [11](https://arxiv.org/html/2605.01512#bib.bib2 "")\] | — | — | — | .251 |
| BBox Dynamics + OF \[ [11](https://arxiv.org/html/2605.01512#bib.bib2 "")\] | — | — | — | .270 |
| Naive baseline \[ [14](https://arxiv.org/html/2605.01512#bib.bib1 "")\] | .30 | .25 | .34 | .289 |
| Molmo-7B \[ [4](https://arxiv.org/html/2605.01512#bib.bib22 "")\] | .48 | .60 | .27 | .396 |
| Best-of-baselines \[ [14](https://arxiv.org/html/2605.01512#bib.bib1 "")\] | .48 | .60 | .49 | .412 |
| Gemini 3.1 single-pass (ours) | .44 | .49 | .49 | .473 \[.46,.49\] |
| Qwen3-VL Pass 1 (ours) | .46 | .51 | .47 | .480 \[.47,.49\] |
| Ours (full) | .50 | .54 | .59 | .539\[.53,.55\] |
| Human \[ [14](https://arxiv.org/html/2605.01512#bib.bib1 "")\] | .98 | 1.0 | .92 | .843 |

### 4.1 Setup

We evaluate on the 2,027 real CCTV clips of ACCIDENT@CVPR 2026 with
per-video (time, 2D center, type) annotations; test-split labels were
released publicly post-competition with our hyperparameters frozen before
release (App. [B](https://arxiv.org/html/2605.01512#A2 "Appendix B Reproducibility & Cost ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video")). Per \[ [14](https://arxiv.org/html/2605.01512#bib.bib1 "")\],
ACCS\\mathrm{ACC}^{S} is the per-video harmonic mean averaged over videos;
reported T,S,CT,S,C are dataset-level component means
(≠3/(1/T+1/S+1/C){\\neq}3/(1/T{+}1/S{+}1/C) in general). TT: Gaussian at GT time
(σt=1\\sigma\_{t}{=}1 s); SS: anisotropic spatial Gaussian
(σx=0.127,σy=0.119\\sigma\_{x}{=}0.127,\\sigma\_{y}{=}0.119); CC: top-1 type accuracy.
Baselines: two Kaggle public notebooks \[ [11](https://arxiv.org/html/2605.01512#bib.bib2 "")\], the
benchmark paper’s naive, Molmo-7B, best-of-baselines oracle, and human
ceiling \[ [14](https://arxiv.org/html/2605.01512#bib.bib1 "")\].
### 4.2 Main Results

Our pipeline reaches ACCS=0.539\\mathrm{ACC}^{S}{=}0.539 (CI \[0.525,0.553\]\[0.525,0.553\]):
+0.127+0.127 over the best-of-baselines oracle and +0.143+0.143 over
Molmo-7B. T=0.497T{=}0.497 exceeds Molmo’s; S=0.538S{=}0.538 trails Molmo’s
0.5960.596; C=0.591C{=}0.591 is highest reported. _Gemini 3.1 alone_ on the
same 1 fps input scores only 0.4730.473\[.46,.49\]\[.46,.49\], below our Qwen
Pass 1 (0.4800.480); paired bootstrap shows our pipeline beats Gemini-alone
by Δ=+0.066\\Delta{=}{+}0.066 (p<0.001p{<}0.001). On the 1,681 Pass-1-valid videos
ACCS=0.554{}^{S}{=}0.554; the 346 fallback videos (App.
---
Each frame is
labeled with its precise timestamp. The time
window shown is from {start}s to {end}s.
A traffic accident occurs somewhere in this video.
If the collision happens within this time window,
identify:
1. Exact time: The precise moment (to 0.1 second)
   of collision or impact.
2. Exact location: The impact point, as
   coordinates between 0 and 1000.
If you cannot see a collision in these frames,
return time as -1.
Return ONLY a JSON object:
{"time": <seconds with 1 decimal or -1>,
 "x": <0-1000>, "y": <0-1000>}
```

### A.3 Type Classification (Gemini 3.1)

```
A traffic collision HAS occurred in this
surveillance clip. You MUST classify its type.
This clip shows ~6 seconds leading up to and
including the collision moment.
Collision types - pick exactly ONE:
- head_on: Two vehicles approach from OPPOSITE
  directions, collide front-to-front.
- rear_end: Two vehicles travel SAME direction;
  trailing one hits leading one from behind.
- t_bone: One vehicle strikes the SIDE of another
  at roughly 90 degrees.
- sideswipe: Two vehicles in parallel lanes make
  lateral/glancing contact.
- single: Only ONE vehicle involved.
Watch vehicle MOTION carefully across the clip.
You MUST pick the most likely type.
```

## Appendix B Reproducibility & Cost

- •

API cost (April 2026): Pass 1 ∼\\sim$4, Pass 2 ∼\\sim$6,
Gemini typing ∼\\sim$10\. Total ∼\\sim$20 on 2,027 videos
(∼\\sim$0.01/video).
- •

Wall-clock: ∼\\sim100 minutes at 5 workers for Pass 1;
∼\\sim180 minutes at 5 workers for Pass 2; ∼\\sim15 minutes at
10 workers for Gemini. Total ∼\\sim5 hours on a consumer
workstation with a single residential network connection.
- •

Hyperparameters were fixed during development by inspection
of the 2,2112{,}211 CARLA synthetic dev videos and a small debug sample
of public Kaggle dev-split real videos. Values: Δ=3\\Delta{=}3 s
window, τ=0.3\\tau{=}0.3 s temporal boundary tolerance, m=10m{=}10
spatial margin on the \[0,1000\]2\[0,1000\]^{2} grid, 2.5×2.5\\times type-clip crop.
No grid search was performed on the 2,0272{,}027 real test
videos; sensitivity to ±1\\pm 1-step perturbations of τ\\tau and mm
is ≤0.002\\leq 0.002 in ACCS\\mathrm{ACC}^{S} (Appendix [C](https://arxiv.org/html/2605.01512#A3 "Appendix C Hyperparameter Sensitivity ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video")).
- •

Physics fallback used on Pass 1 API failures (17%) is
YOLO26x + ByteTrack + multi-channel physics scoring. Its scorer
weights (approach, IoU-surge, sustained-IoU, interaction-bias) were
grid-searched on a 100100-video CARLA sim split during challenge
development and frozen before the real-test labels were released.
- •

Data provenance. Ground-truth annotations for the 2,0272{,}027
real test videos were released publicly by the ACCIDENT benchmark
organizers on Kaggle after the competition ended
( [https://www.kaggle.com/datasets/picekl/accident](https://www.kaggle.com/datasets/picekl/accident "")). We use them
only for evaluation and post-hoc failure analysis. All pipeline
hyperparameters and prompts were frozen before this release.
- •

Artifact release. To support reproducibility under API
drift, we will release per-video raw VLM JSON outputs and parsed
prediction CSVs alongside the camera-ready code.
- •

Evaluation script mirrors the public leaderboard’s
convention: σt=1\\sigma\_{t}{=}1 s Gaussian temporal similarity;
global mean GT bbox width and height
(σx=0.127\\sigma\_{x}{=}0.127, σy=0.119\\sigma\_{y}{=}0.119) for spatial; Top-1
accuracy for type; harmonic mean combines the three.
- •

Challenge compliance. ACCIDENT@CVPR 2026 is an open
prediction-file competition (participants upload a per-video CSV;
it is not a sandboxed, compute-capped code competition), and its
sole learning constraint is the prohibition on training or
fine-tuning on labeled real accident footage.
---
[D](https://arxiv.org/html/2605.01512#A4 "Appendix D Fallback Contribution Analysis ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video")) score
0.4570.457; naive-fill fallback yields 0.5010.501, confirming the VLM pipeline
drives the gain.
(a) Time bias, mean +1.55+1.55 s

(b) TMAET\_{\\mathrm{MAE}} vs. video length

![Refer to caption](https://arxiv.org/html/2605.01512v2/confusion_matrix.png)

(c) Type confusion

(d) Physics–VLM oracle: 2.132.13 s MAE

Figure 3: Failure diagnostics. (a) Pass 1 time is right-skewed,
mean +1.55+1.55 s. (b) Temporal MAE grows with video length. (c) Head-on
→\\to t-bone (79%), sideswipe →\\to rear-end (39%). (d) Oracle of
YOLO+physics (6.636.63 s) and Qwen-Pass 1 (3.203.20 s) reaches
2.132.13 s (−33.5%-33.5\\%).Table 2: Component ablation; TT at σt∈{1,2}\\sigma\_{t}{\\in}\\{1,2\\}, ACCS\\mathrm{ACC}^{S} at σt=1\\sigma\_{t}{=}1.
| Configuration | Tσ​1T\_{\\sigma 1} | Tσ​2T\_{\\sigma 2} | SS | CC | ACCS\\mathrm{ACC}^{S} |
| --- | --- | --- | --- | --- | --- |
| Pass 1 only (Qwen type) | 0.463 | 0.614 | 0.506 | 0.474 | 0.480 |
| \+ Gemini type | 0.463 | 0.614 | 0.506 | 0.590 | 0.514 |
| \+ Pass 2 time | 0.497 | 0.626 | 0.506 | 0.591 | 0.528 |
| \+ Pass 2 spatial | 0.497 | 0.626 | 0.538 | 0.591 | 0.539 |

### 4.3 Ablation

Table [2](https://arxiv.org/html/2605.01512#S4.T2 "Table 2 ‣ 4.2 Main Results ‣ 4 Experiments ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video") decomposes the gain. Replacing Qwen’s type head with
Gemini lifts CC by +0.12+0.12 (largest single jump); Pass 2 time refinement
adds +0.034+0.034 to T⁡(σt=1)T(\\sigma\_{t}{=}1); Pass 2 spatial merge adds +7%+7\\% to SS.
Cumulative gain over Pass 1 alone is +0.059+0.059ACCS\\mathrm{ACC}^{S}.
### 4.4 Failure Mode Analysis

Temporal: late-bias + length. Pass 1 (predicted −- GT)
time has mean +1.55+1.55 s, median +0.37+0.37 s (Fig. [3](https://arxiv.org/html/2605.01512#S4.F3 "Figure 3 ‣ 4.2 Main Results ‣ 4 Experiments ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video") a): the VLM
picks the post-collision wreckage frame, not contact. TMAET\_{\\mathrm{MAE}} also
grows from 0.940.94 s on ≤10\\leq 10 s clips to >4>4 s on ≥20\\geq 20 s clips
(Fig. [3](https://arxiv.org/html/2605.01512#S4.F3 "Figure 3 ‣ 4.2 Main Results ‣ 4 Experiments ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video") b), arguing for motion-adaptive sampling.
Type confusion. The confusion matrix (Fig. [3](https://arxiv.org/html/2605.01512#S4.F3 "Figure 3 ‣ 4.2 Main Results ‣ 4 Experiments ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video") c)
shows the two hardest classes collapsing: 79%79\\% of head-on is called t-bone,
39%39\\% of sideswipe is called rear-end. Per-type (App. [E](https://arxiv.org/html/2605.01512#A5 "Appendix E Per-Type Breakdown ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video")),
head-on and sideswipe fall near ACCS=0.12\\mathrm{ACC}^{S}{=}0.12 _from type alone_
– T,ST,S are healthy. The head-on→\\tot-bone collapse is plausibly driven by
monocular depth ambiguity in high-angle CCTV and web-data label bias.
Physics–VLM oracle. On the 1,681 Pass-1-valid videos,
an oracle of YOLO+physics (6.636.63 s) and Qwen-Pass 1 (3.203.20 s) reaches
2.132.13 s MAE (Fig. [3](https://arxiv.org/html/2605.01512#S4.F3 "Figure 3 ‣ 4.2 Main Results ‣ 4 Experiments ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video") d, −33.5%-33.5\\%).
### 4.5 Conclusion

Two-pass grounding plus a specialist VLM split achieves
ACCS=0.539\\mathrm{ACC}^{S}{=}0.539 on ACCIDENT@CVPR 2026 (+0.127+0.127 over the benchmark
paper’s best-of-baselines oracle, ∼\\sim$20 cost).
---
Our pipeline meets
this: every model is frozen and used zero-shot. The challenge
places no restriction on publicly available pretrained models or
external inference services – the organizers’ own baselines use
pretrained optical flow and CLIP \[ [14](https://arxiv.org/html/2605.01512#bib.bib1 ""), [11](https://arxiv.org/html/2605.01512#bib.bib2 "")\].
Both APIs we invoke, Qwen3-VL-Plus (Alibaba DashScope) and
Gemini 3.1 Flash-Lite (Google) \[ [1](https://arxiv.org/html/2605.01512#bib.bib10 ""), [7](https://arxiv.org/html/2605.01512#bib.bib12 "")\],
were publicly released, documented, and equally accessible to any
participant under standard pay-as-you-go commercial terms
throughout the submission window (April 2026), at a total cost of
∼\\sim$20 for the full 2,027-video test set. We use no
private models, privileged endpoints, or non-public data.
## Appendix C Hyperparameter Sensitivity

This is a post-hoc analysis. The numbers in
Table [3](https://arxiv.org/html/2605.01512#A3.T3 "Table 3 ‣ Appendix C Hyperparameter Sensitivity ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video") were computed on the publicly-released test
labels _after_ the competition closed and were _not_ used for
hyperparameter selection. Defaults τ=0.3\\tau{=}0.3 s and m=10m{=}10 were
fixed by inspection on the 2,211 CARLA development videos and frozen
before the labels were released (App. [B](https://arxiv.org/html/2605.01512#A2 "Appendix B Reproducibility & Cost ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video")). Each threshold
is swept while the other is held at its default to assess robustness.
Table 3: Sensitivity of ACCS\\mathrm{ACC}^{S} to the two gate thresholds on
2,027 real test videos (σt=1\\sigma\_{t}{=}1). Defaults marked with ⋆\\star.
| τ\\tau(s) | TT | SS | CC | ACCS\\mathrm{ACC}^{S} | mm | TT | SS | CC | ACCS\\mathrm{ACC}^{S} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 0.497 | 0.538 | 0.591 | 0.5393 | 0 | 0.497 | 0.462 | 0.591 | 0.5113 |
| 0.2 | 0.497 | 0.538 | 0.591 | 0.5393 | 5 | 0.497 | 0.538 | 0.591 | 0.5393 |
| ⋆\\star 0.3 | 0.497 | 0.538 | 0.591 | 0.5393 | ⋆\\star 10 | 0.497 | 0.538 | 0.591 | 0.5393 |
| 0.5 | 0.496 | 0.538 | 0.591 | 0.5385 | 20 | 0.497 | 0.538 | 0.591 | 0.5393 |
| 1.0 | 0.494 | 0.538 | 0.591 | 0.5377 | 50 | 0.497 | 0.538 | 0.591 | 0.5392 |

τ\\tau is effectively flat in \[0.1,0.3\]\[0.1,0.3\] and degrades by only
Δ​ACCS≤0.002\\Delta\\mathrm{ACC}^{S}{\\leq}0.002 even at τ=1.0\\tau{=}1.0 s – Pass 2’s
boundary-hedge detection (returning exact window endpoints) is sharp
enough that the tolerance window has negligible effect. In contrast, mm
has one critical transition at m=0m{=}0: disabling the margin admits
Qwen-returned invalid-coordinate responses (raw −1-1, after /1000/1000
normalization becomes −0.001-0.001) and costs Δ​S=−0.076\\Delta S{=}-0.076. Any
positive margin in \[5,50\]\[5,50\] is equivalent. Neither hyperparameter is
knife-edge, and the CARLA-tuned values transfer to real data without any
re-tuning on the released test labels.
## Appendix D Fallback Contribution Analysis

Pass 1 API failures trigger a fallback to the YOLO26x + ByteTrack +
multi-channel physics scorer for 346 videos (17.1% of the test split).
Table [4](https://arxiv.org/html/2605.01512#A4.T4 "Table 4 ‣ Appendix D Fallback Contribution Analysis ‣ Two-Pass Zero-Shot Temporal-Spatial Groundingof Rare Traffic Events in Surveillance Video") decomposes the final ACCS=0.539\\mathrm{ACC}^{S}{=}0.539 by
subset.
Table 4: Fallback contribution to the final score. VLM-success rows receive
Pass 1+Pass 2 Qwen3-VL grounding and Gemini type; fallback rows use
YOLO+physics for (t,x,y,c)(t,x,y,c). “Naive-fill” replaces the 346 fallback rows
with trivial defaults (midpoint time, image center, majority type
_single_) to estimate a pure-VLM ceiling with no informative fallback.