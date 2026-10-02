|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| Method | Pixel-AUROC | Pixel-AP | Pixel-AUPRO | Pixel-F1 | RBDC | TBDC |
| AdaCLIP (Fully fine-tuned)\[ [4](https://arxiv.org/html/2603.25467#bib.bib28 "")\] | 53.06 | 4.97 | 50.66 | 11.19 | 12.3 | 15.5 |
| AnomalyCLIP (Fully fine-tuned)\[ [37](https://arxiv.org/html/2603.25467#bib.bib29 "")\] | 54.25 | 23.73 | 38.59 | 7.48 | 13.1 | 21.0 |
| DDAD (Fully trained)\[ [21](https://arxiv.org/html/2603.25467#bib.bib30 "")\] | 55.87 | 5.61 | 15.12 | 2.67 | 18.01 | 13.29 |
| SimpleNet (Fully trained)\[ [19](https://arxiv.org/html/2603.25467#bib.bib31 "")\] | 52.49 | 20.51 | 44.05 | 10.71 | 51.18 | 27.75 |
| DRAEM (Fully trained)\[ [34](https://arxiv.org/html/2603.25467#bib.bib32 "")\] | 69.58 | 30.63 | 35.78 | 10.89 | 44.26 | 70.64 |
| TAO (Partially fine-tuned)\[ [11](https://arxiv.org/html/2603.25467#bib.bib14 "")\] | 75.11 | 50.78 | 72.97 | 64.12 | 83.6 | 93.2 |
| AdaCLIP (Zero-shot)\[ [4](https://arxiv.org/html/2603.25467#bib.bib28 "")\] | 51.02 | 1.32 | 33.98 | 2.61 | 5.8 | 10.6 |
| AnomalyCLIP (Zero-shot)\[ [37](https://arxiv.org/html/2603.25467#bib.bib29 "")\] | 51.63 | 21.20 | 36.34 | 5.92 | 7.5 | 11.2 |
| GridVAD (Ours, Zero-shot) | 77.59 | 38.53 | 66.82 | 42.09 | 38.96 | 37.70 |

Table 3: Object-level comparison on ShanghaiTech Campus. Baseline numbers are transcribed
from the TAO paper\[ [11](https://arxiv.org/html/2603.25467#bib.bib14 "")\].
|     |     |     |
| --- | --- | --- |
| Method | RBDC | TBDC |
| OCAD\[ [12](https://arxiv.org/html/2603.25467#bib.bib12 "")\] | 20.7 | 44.5 |
| AED-SSMTL\[ [8](https://arxiv.org/html/2603.25467#bib.bib13 "")\] | 43.2 | 84.1 |
| HF2VAD\[ [18](https://arxiv.org/html/2603.25467#bib.bib11 "")\] | 45.4 | 84.5 |
| STPT\[ [22](https://arxiv.org/html/2603.25467#bib.bib33 "")\] | 51.6 | 84.6 |
| TAO\[ [11](https://arxiv.org/html/2603.25467#bib.bib14 "")\] | 62.1 | 85.4 |
| GridVAD (Ours) | 33.32 | 14.58 |

### 3.3 Ablation Study

#### Does SCC Reduce VLM Hallucinations?
A core premise of GridVAD is that VLMs are noisy proposers whose raw outputs
contain both genuine anomaly descriptions and confident-sounding hallucinations. Self-Consistency Consolidation (SCC) treats the VLM as a stochastic sensor and uses multiple independent samplings to separate signal from noise.
We isolate the effect of SCC by comparing M=1M{=}1 (raw VLM output, no consolidation) against M=5M{=}5 on a 15-video subset of ShanghaiTech Campus \[ [17](https://arxiv.org/html/2603.25467#bib.bib24 "")\], keeping all other pipeline
components (Grounding DINO, SAM2) fixed.
Table 4: Effect of SCC on ShanghaiTech Campus (15 videos).
SCC improves all pixel-level metrics while reducing object-level recall,
revealing a precision-recall tradeoff.
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| Config | Px-AUROC | Px-AP | Px-F1 | RBDC | TBDC |
| M=1M{=}1, no SCC | 62.71 | 25.36 | 29.64 | 32.31 | 33.18 |
| M=5M{=}5 | 70.04 | 37.90 | 43.43 | 27.97 | 25.91 |

Analysis.
As shown in Table [4](https://arxiv.org/html/2603.25467#S3.T4 "Table 4 ‣ Does SCC Reduce VLM Hallucinations? ‣ 3.3 Ablation Study ‣ 3 Experiments ‣ GridVAD: Open-Set Video Anomaly Detection via Spatial Reasoning over Stratified Frame Grids"), SCC produces a clear precision-recall tradeoff. The single-pass baseline (M=1M{=}1) achieves higher RBDC (+4.3) and TBDC (+7.3) because it retains every VLM proposal, including hallucinations, some of which happen to overlap ground-truth regions. However, these unchecked proposals also produce noisy masks: Pixel-AUROC drops by 7.3 points and Pixel-F1 by 13.8 points compared to the SCC-filtered configuration.
With M=5M{=}5, SCC discards proposals that do not recur across independent samplings. This removes hallucinated detections and improves mask quality across all pixel-level metrics.
---
RBDC and TBDC measure whether GT tracks are _found_, not how well they are segmented. The current pipeline deliberately prioritizes mask quality over exhaustive recall. Improving VLM proposal recall, through better prompting, adaptive re-querying of uncertain clips, or lightweight anomaly prior injection, is the most direct path to closing the gap with trained methods without sacrificing mask precision.
Computational cost and trade-offs.
By bounding VLM reasoning to a fixed M+1M+1 calls per clip (avoiding frame-by-frame 𝒪⁡(N)\\mathcal{O}(N) evaluation), GridVAD scales efficiently across time. However, using a 30B-parameter VLM carries a higher absolute compute footprint per clip than lightweight CLIP-based baselines. GridVAD intentionally trades per-clip inference compute for zero-shot open-set generalizability, decoupling high-level semantic proposal generation from specialized downstream execution models (Grounding DINO, SAM 2) that handle spatial grounding and temporal mask propagation.
Clip independence.
Each clip is processed independently. Anomalies that span clip boundaries may be partially missed or duplicated. Cross-clip context is currently handled only by the temporal overlap in the sliding window, not by any global reasoning.
## 4 Conclusion

We presented GridVAD, a training-free pipeline that repositions VLMs from direct anomaly detectors to open-set anomaly proposers within a propose-ground-propagate decomposition. By representing video clips as stratified spatial grids, GridVAD converts temporal anomaly detection into a single-pass image understanding task with a fixed per-clip VLM budget. Self-Consistency Consolidation filters hallucinations by retaining only proposals with cross-sampling support, while Grounding DINO and SAM2 provide precise spatial grounding and temporal mask propagation.
Experiments on UCSD Ped2 and ShanghaiTech Campus validate the feasibility of this decomposition: GridVAD achieves the highest Pixel-AUROC among all compared methods on UCSD Ped2, including partially fine-tuned baselines, in a fully zero-shot setting. The SCC ablation reveals a controllable precision-recall tradeoff that explains the gap between strong pixel-level and lower object-level scores. Improving VLM proposal recall, through better prompting, adaptive re-querying, or lightweight anomaly priors, is the most direct path to closing this gap without sacrificing mask quality.
## References

- \[1\]S. Bai, Y. Cai, R. Chen, K. Chen, X. Chen, Z. Cheng, L. Deng, W. Ding, C. Gao, C. Ge, W. Ge, Z. Guo, Q. Huang, J. Huang, F. Huang, B. Hui, S. Jiang, Z. Li, M. Li, M. Li, K. Li, Z. Lin, J. Lin, X. Liu, J. Liu, C. Liu, Y. Liu, D. Liu, S. Liu, D. Lu, R. Luo, C. Lv, R. Men, L. Meng, X. Ren, X. Ren, S. Song, Y. Sun, J. Tang, J. Tu, J. Wan, P. Wang, P. Wang, Q. Wang, Y. Wang, T. Xie, Y. Xu, H. Xu, J. Xu, Z. Yang, M. Yang, J. Yang, A. Yang, B. Yu, F. Zhang, H. Zhang, X. Zhang, B. Zheng, H. Zhong, J. Zhou, F. Zhou, J. Zhou, Y. Zhu, and K. Zhu (2025)Qwen3-vl technical report.
CoRRabs/2511.21631.
External Links: [Link](https://doi.org/10.48550/arXiv.2511.21631 ""),
[Document](https://dx.doi.org/10.48550/ARXIV.2511.21631 ""),
2511.21631Cited by: [§3.1](https://arxiv.org/html/2603.25467#S3.SS1.p7.1 "3.1 Experimental Setup ‣ 3 Experiments ‣ GridVAD: Open-Set Video Anomaly Detection via Spatial Reasoning over Stratified Frame Grids").
- \[2\]S. Bai, Z. He, Y. Lei, W. Wu, C. Zhu, M. Sun, and J. Yan (2019)Traffic anomaly detection via perspective map based on spatial-temporal information matrix.
In IEEE Conference on Computer Vision and Pattern Recognition Workshops,
CVPR Workshops 2019, Long Beach, CA, USA, June 16-20, 2019,
pp. 117–124.
---
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|  | {𝒢(m)}m=1M\\displaystyle\\{\\mathcal{G}^{(m)}\\}\_{m=1}^{M} | =Tile⁡(𝒱,M)\\displaystyle=\\mathrm{Tile}(\\mathcal{V};\\,M) |  | \[𝒪⁡(1)\\mathcal{O}(1) copy\] |  | (8) |
|  | {𝒜(m)}m=1M\\displaystyle\\{\\mathcal{A}^{(m)}\\}\_{m=1}^{M} | =Φ⁡({𝒢(m)}m=1M,𝒫)\\displaystyle=\\Phi(\\{\\mathcal{G}^{(m)}\\}\_{m=1}^{M},\\,\\mathcal{P}) |  | \[MM VLM forward passes\] |  | (9) |
|  | 𝒜⋆\\displaystyle\\mathcal{A}^{\\star} | =SCC⁡({𝒜(m)}m=1M)\\displaystyle=\\mathrm{SCC}(\\{\\mathcal{A}^{(m)}\\}\_{m=1}^{M}) |  | \[1 SCC pass\] |  | (10) |
|  | 𝒜†\\displaystyle\\mathcal{A}^{\\dagger} | ={aj∈𝒜⋆∣σj≥τ}\\displaystyle=\\{a\_{j}\\in\\mathcal{A}^{\\star}\\mid\\sigma\_{j}\\geq\\tau\\} |  | \[support filter\] |  | (11) |
|  | bj\\displaystyle b\_{j} | =GroundingDINO⁡(faj,dj)\\displaystyle=\\mathrm{GroundingDINO}(f\_{a\_{j}},\\,d\_{j}) |  | \[\|𝒜†\|\|\\mathcal{A}^{\\dagger}\| grounding calls\] |  | (12) |
|  | Stj\\displaystyle S\_{t}^{j} | =SAM2⁡({ft},bj,aj)\\displaystyle=\\mathrm{SAM2}(\\{f\_{t}\\},b\_{j},a\_{j}) |  | \[\|𝒜†\|\|\\mathcal{A}^{\\dagger}\| propagation passes\] |  | (13) |

where \|𝒜†\|\|\\mathcal{A}^{\\dagger}\| is the number of detected anomalies. The dominant cost is the MM VLM calls ( [9](https://arxiv.org/html/2603.25467#S2.E9 "Equation 9 ‣ 2.5 Full Pipeline Summary and Complexity ‣ 2 Related Work ‣ GridVAD: Open-Set Video Anomaly Detection via Spatial Reasoning over Stratified Frame Grids"));
all subsequent steps process only the anomalous window.
## 3 Experiments

### 3.1 Experimental Setup

Datasets.
We evaluate on two standard VAD benchmarks. In both datasets, the training set consists exclusively of normal video events, whereas anomalies appear only within the test set.
ShanghaiTech Campus\[ [17](https://arxiv.org/html/2603.25467#bib.bib24 "")\] contains 330 normal training videos and 107 test videos (480×856480{\\times}856 pixels) across 13 campus scenes, with test-set anomalies including fighting, robbery, and cycling in restricted areas.
UCSD Ped2\[ [20](https://arxiv.org/html/2603.25467#bib.bib25 "")\] contains 16 normal training videos and 12 test videos (240×360240{\\times}360 pixels), with test-set anomalies including cyclists, vehicles, and skateboarders operating in pedestrian zones.
Evaluation Metrics.
We adopt the same evaluation protocol as TAO\[ [11](https://arxiv.org/html/2603.25467#bib.bib14 "")\], spanning
three complementary granularities.
_Frame-level._ Frame-AUROC measures the model’s ability to distinguish anomalous from
normal frames, computed as the area under the
receiver operating characteristic curve using per-frame anomaly scores.
A score of 1.0 indicates perfect temporal discrimination.
_Pixel-level._ We evaluate four pixel-level metrics:
Pixel-AUROC assesses the model’s capability to differentiate between normal and anomalous pixels across thresholds.
Pixel-AUPRO evaluates segmentation accuracy based on region overlap.
Pixel-AP evaluates detection accuracy by balancing false positives and false negatives.
Pixel-F1 combines precision and recall into a single measure.
All pixel-level metrics are computed per annotated frame and averaged over frames, then over videos.
_Object-level._
We report the Region-Based Detection Criterion (RBDC) and
Track-Based Detection Criterion (TBDC) introduced
in \[ [9](https://arxiv.org/html/2603.25467#bib.bib17 "")\], following the same
protocol as \[ [11](https://arxiv.org/html/2603.25467#bib.bib14 "")\].
RBDC evaluates spatial accuracy based on intersection over union (IoU) with a threshold of α\\alpha.
TBDC assesses temporal consistency in tracking anomalous regions over frames.
Both metrics are computed globally across the entire test set, as in TAO\[ [11](https://arxiv.org/html/2603.25467#bib.bib14 "")\], rather than being averaged per video.
---
_Anomaly score construction._
For each verified proposal aj∈𝒜†a\_{j}\\in\\mathcal{A}^{\\dagger}, the propagated mask
StjS\_{t}^{j} is weighted by the proposal’s confidence pjp\_{j}, and the pixel-level
anomaly map for frame tt is the pixel-wise maximum over proposals active at tt:

|     |     |     |     |
| --- | --- | --- | --- |
|  | At(x,y)=maxj:t∈\[tsj,tej\]pj⋅Stj(x,y),A\_{t}(x,y)=\\max\_{j\\,:\\,t\\in\[t\_{s}^{j},\\,t\_{e}^{j}\]}p\_{j}\\cdot S\_{t}^{j}(x,y), |  | (14) |

with At=0A\_{t}=0 where no proposal is active. Frame-level scores are the spatial
maximum of this map, st=maxx,y⁡At​(x,y)s\_{t}=\\max\_{x,y}A\_{t}(x,y). Because StjS\_{t}^{j} is binary,
AtA\_{t} takes a small number of distinct values, so threshold-swept metrics are
evaluated over a correspondingly coarse operating range.
Implementation Details.
All experiments are conducted on 4×\\timesNVIDIA V100 32 GB GPUs.
We use _Qwen3-VL-30B-A3B-Instruct_\[ [1](https://arxiv.org/html/2603.25467#bib.bib27 "")\] for both
per-grid proposal generation and SCC consolidation, setting the support threshold to τ=3\\tau=3.
Spatial grounding is performed using _Grounding DINO_\[ [16](https://arxiv.org/html/2603.25467#bib.bib22 "")\]
with box and text confidence thresholds set to δ=0.05\\delta=0.05.
Pixel-level tracking uses _SAM2.1-Hiera-Tiny_\[ [23](https://arxiv.org/html/2603.25467#bib.bib23 "")\]
with a minimum mask area threshold of 50​px250\\,\\text{px}^{2}.
For each video clip, we set the grid dimension to g=3g=3 (K=9K=9 frames per grid) and sample M=5M=5 independent
stratified grids. No components are fine-tuned on the target datasets.
### 3.2 Comparison with State-of-the-Art

We compare GridVAD against representative training-based and training-free baselines on
UCSD Ped2\[ [20](https://arxiv.org/html/2603.25467#bib.bib25 "")\] and ShanghaiTech
Campus\[ [17](https://arxiv.org/html/2603.25467#bib.bib24 "")\].
As shown in Tables [2](https://arxiv.org/html/2603.25467#S3.T2 "Table 2 ‣ 3.2 Comparison with State-of-the-Art ‣ 3 Experiments ‣ GridVAD: Open-Set Video Anomaly Detection via Spatial Reasoning over Stratified Frame Grids")– [3](https://arxiv.org/html/2603.25467#S3.T3 "Table 3 ‣ 3.2 Comparison with State-of-the-Art ‣ 3 Experiments ‣ GridVAD: Open-Set Video Anomaly Detection via Spatial Reasoning over Stratified Frame Grids"), GridVAD achieves the highest Pixel-AUROC (77.59%) on UCSD Ped2 among all compared methods, including the partially fine-tuned TAO without any task-specific fine-tuning.
Furthermore, it delivers competitive performance across Pixel-AP, Pixel-AUPRO, and Pixel-F1, though its RBDC and TBDC scores remain relatively low.
The gap in RBDC and TBDC reflects the proposal-recall bottleneck discussed in Section [3.6](https://arxiv.org/html/2603.25467#S3.SS6 "3.6 Discussion and Limitations ‣ 3 Experiments ‣ GridVAD: Open-Set Video Anomaly Detection via Spatial Reasoning over Stratified Frame Grids"): GridVAD can only ground anomalies that the VLM first proposes in the temporal montage, while exhaustive per-frame methods like TAO track every object regardless. On ShanghaiTech Campus, this recall gap is more pronounced due to diverse scenes and subtle anomalies.
Table 2: Quantitative comparison on UCSD Ped2. Baseline numbers are transcribed from the
TAO paper\[ [11](https://arxiv.org/html/2603.25467#bib.bib14 "")\]; our results are in the last row.