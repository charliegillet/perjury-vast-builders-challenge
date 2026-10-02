Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2603.22911v2 \[cs.CV\] 12 Apr 2026

# ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling

Shaobo Ju11footnotemark: 1Affiliation:  Key Laboratory of Multimedia Trusted Perception and Efficient ComputingMinistry of Education of China, Xiamen University, 361005, P.R. China.
Email: [changchao@nudt.edu.cn](mailto:changchao@nudt.edu.cn)Baiyang Song
††thanks: Equal contribution.Affiliation:  Key Laboratory of Multimedia Trusted Perception and Efficient ComputingMinistry of Education of China, Xiamen University, 361005, P.R. China.
Email: [wanghuaixi@nudt.edu.cn](mailto:wanghuaixi@nudt.edu.cn)Tao Chen
Affiliation:  Key Laboratory of Multimedia Trusted Perception and Efficient ComputingMinistry of Education of China, Xiamen University, 361005, P.R. China.
Jiapeng Zhang
Affiliation:  Key Laboratory of Multimedia Trusted Perception and Efficient ComputingMinistry of Education of China, Xiamen University, 361005, P.R. China.
Qiong Wu
Affiliation:  Key Laboratory of Multimedia Trusted Perception and Efficient ComputingMinistry of Education of China, Xiamen University, 361005, P.R. China.
Chao Chang
Affiliation:  National University of Defense Technology.{jushaobo,songbaiyang,chentao,zhangjiapeng,qiong}@stu.xmu.edu.cn, {zhouyiyi, rrji}@xmu.edu.cn,HuaiXi Wang
Affiliation:  National University of Defense Technology.{jushaobo,songbaiyang,chentao,zhangjiapeng,qiong}@stu.xmu.edu.cn, {zhouyiyi, rrji}@xmu.edu.cn,Yiyi Zhou
††thanks: Corresponding Author.Affiliation:  Key Laboratory of Multimedia Trusted Perception and Efficient ComputingMinistry of Education of China, Xiamen University, 361005, P.R. China.
Rongrong Ji
Affiliation:  Key Laboratory of Multimedia Trusted Perception and Efficient ComputingMinistry of Education of China, Xiamen University, 361005, P.R. China.

###### Abstract

Due to the great saving of computation and memory overhead, token compression has become a research hot-spot for MLLMs and achieved remarkable progress in image-language tasks. However, for the video, existing methods still fall short of high-ratio token compression. We attribute this shortcoming to the insufficient modeling of temporal and continual video content, and propose a novel and training-free token pruning method for video MLLMs, termed _ForestPrune_, which achieves effective and high-ratio pruning via Spatial-temporal Forest Modeling. In practice, ForestPrune construct token forests across video frames based on the semantic, spatial and temporal constraints, making an overall comprehension of videos. Afterwards, ForestPrune evaluates the importance of token trees and nodes based on tree depth and node roles, thereby obtaining a globally optimal pruning decision.
To validate ForestPrune, we apply it to two representative video MLLMs, namely _LLaVA-Video_ and _LLaVA-OneVision_, and conduct extensive experiments on a bunch of video benchmarks.
The experimental results not only show the great effectiveness for video MLLMs, _e.g._, retaining 95.8% average accuracy while reducing 90% tokens for LLaVA-OneVision, but also show its superior performance and efficiency than the compared token compression methods, _e.g._, +10.1% accuracy on MLVU and -81.4% pruning time than FrameFusion on LLaVA-Video.
Ourcode is given in the [ForestPrune](https://github.com/luminousllsa/ForestPrune "").

Figure 1: Comparison between the proposed _ForestPrune_ (Ours) and the existing compression methods  \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 ""), [6](https://arxiv.org/html/2603.22911v2#bib.bib1 ""), [60](https://arxiv.org/html/2603.22911v2#bib.bib44 ""), [13](https://arxiv.org/html/2603.22911v2#bib.bib54 "")\] on VideoMME. The base model used is LLaVA-Video-7B. As pruning ratio increases, existing methods will encounter obvious performance drops, while ForestPrune is still robust.

## 1 Introduction

Recent years have witnessed the rapid development of _multimodal large language models_ (MLLMs) \[ [24](https://arxiv.org/html/2603.22911v2#bib.bib23 ""), [23](https://arxiv.org/html/2603.22911v2#bib.bib6 ""), [10](https://arxiv.org/html/2603.22911v2#bib.bib27 ""), [1](https://arxiv.org/html/2603.22911v2#bib.bib31 ""), [43](https://arxiv.org/html/2603.22911v2#bib.bib30 ""), [8](https://arxiv.org/html/2603.22911v2#bib.bib9 ""), [30](https://arxiv.org/html/2603.22911v2#bib.bib25 ""), [38](https://arxiv.org/html/2603.22911v2#bib.bib28 ""), [32](https://arxiv.org/html/2603.22911v2#bib.bib24 ""), [27](https://arxiv.org/html/2603.22911v2#bib.bib37 ""), [31](https://arxiv.org/html/2603.22911v2#bib.bib29 "")\] and their great breakthroughs made in a variety of vision-language tasks \[ [19](https://arxiv.org/html/2603.22911v2#bib.bib39 ""), [35](https://arxiv.org/html/2603.22911v2#bib.bib32 ""), [37](https://arxiv.org/html/2603.22911v2#bib.bib33 ""), [36](https://arxiv.org/html/2603.22911v2#bib.bib34 ""), [28](https://arxiv.org/html/2603.22911v2#bib.bib7 ""), [42](https://arxiv.org/html/2603.22911v2#bib.bib10 "")\].
Despite the great success, high latency and excessive computation overhead remain open problems that plague the application of MLLMs.
In pursuit of stronger visual understanding, recent MLLMs \[ [30](https://arxiv.org/html/2603.22911v2#bib.bib25 ""), [38](https://arxiv.org/html/2603.22911v2#bib.bib28 ""), [32](https://arxiv.org/html/2603.22911v2#bib.bib24 "")\] typically use a large number of visual tokens to represent a single image, leading to a quadratic increase in computation and obvious visual redundancy \[ [51](https://arxiv.org/html/2603.22911v2#bib.bib43 ""), [5](https://arxiv.org/html/2603.22911v2#bib.bib40 "")\].
These cases become much more prominent for MLLMs when handling the video-based tasks, where dozens to hundreds of image frames are used as the model input \[ [65](https://arxiv.org/html/2603.22911v2#bib.bib8 ""), [29](https://arxiv.org/html/2603.22911v2#bib.bib35 ""), [39](https://arxiv.org/html/2603.22911v2#bib.bib4 ""), [25](https://arxiv.org/html/2603.22911v2#bib.bib3 ""), [22](https://arxiv.org/html/2603.22911v2#bib.bib17 ""), [66](https://arxiv.org/html/2603.22911v2#bib.bib16 ""), [49](https://arxiv.org/html/2603.22911v2#bib.bib14 ""), [3](https://arxiv.org/html/2603.22911v2#bib.bib15 ""), [7](https://arxiv.org/html/2603.22911v2#bib.bib12 ""), [50](https://arxiv.org/html/2603.22911v2#bib.bib13 "")\].

In this case, numerous efforts \[ [6](https://arxiv.org/html/2603.22911v2#bib.bib1 ""), [4](https://arxiv.org/html/2603.22911v2#bib.bib2 ""), [60](https://arxiv.org/html/2603.22911v2#bib.bib44 ""), [58](https://arxiv.org/html/2603.22911v2#bib.bib45 ""), [20](https://arxiv.org/html/2603.22911v2#bib.bib46 ""), [61](https://arxiv.org/html/2603.22911v2#bib.bib38 ""), [53](https://arxiv.org/html/2603.22911v2#bib.bib41 ""), [54](https://arxiv.org/html/2603.22911v2#bib.bib42 ""), [21](https://arxiv.org/html/2603.22911v2#bib.bib71 "")\] have recently been devoted to the exploration of visual token compression for MLLMs, so as to reduce the expenditure of both computation and memory overhead while retaining high performance.
These endeavors often resort to the principles of token pruning \[ [6](https://arxiv.org/html/2603.22911v2#bib.bib1 ""), [58](https://arxiv.org/html/2603.22911v2#bib.bib45 ""), [61](https://arxiv.org/html/2603.22911v2#bib.bib38 "")\] or merging \[ [4](https://arxiv.org/html/2603.22911v2#bib.bib2 ""), [60](https://arxiv.org/html/2603.22911v2#bib.bib44 ""), [44](https://arxiv.org/html/2603.22911v2#bib.bib48 "")\], and design approaches based on the metrics of visual saliency \[ [58](https://arxiv.org/html/2603.22911v2#bib.bib45 ""), [57](https://arxiv.org/html/2603.22911v2#bib.bib65 "")\] and diversity \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 ""), [71](https://arxiv.org/html/2603.22911v2#bib.bib47 "")\] or cross-modal relevance \[ [40](https://arxiv.org/html/2603.22911v2#bib.bib49 ""), [64](https://arxiv.org/html/2603.22911v2#bib.bib64 "")\].
In this case, existing compression methods can reduce the visual redundancy via retaining the most important tokens, which have achieved remarkable success for image-based MLLMs and tasks \[ [30](https://arxiv.org/html/2603.22911v2#bib.bib25 ""), [31](https://arxiv.org/html/2603.22911v2#bib.bib29 ""), [15](https://arxiv.org/html/2603.22911v2#bib.bib50 ""), [17](https://arxiv.org/html/2603.22911v2#bib.bib51 ""), [33](https://arxiv.org/html/2603.22911v2#bib.bib52 "")\].

However, for the video tasks, existing compression methods still have ample room to improve, especially considering the high-ratio compression settings.
As shown in Fig [1](https://arxiv.org/html/2603.22911v2#S0.F1 "Figure 1 ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"), existing compression methods, such as G-Prune \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] and VisionZip \[ [60](https://arxiv.org/html/2603.22911v2#bib.bib44 "")\], can still maintain high performance while compressing about half of the visual tokens on the video benchmarks like Video-MME \[ [12](https://arxiv.org/html/2603.22911v2#bib.bib22 "")\].
However, as the compression ratio increases, their performance gap becomes much more obvious, distinct from their effects for image-based tasks \[ [15](https://arxiv.org/html/2603.22911v2#bib.bib50 ""), [17](https://arxiv.org/html/2603.22911v2#bib.bib51 ""), [33](https://arxiv.org/html/2603.22911v2#bib.bib52 "")\].
This case can be attributed to the insufficient modeling of video content.
Also shown in Fig [2](https://arxiv.org/html/2603.22911v2#S1.F2 "Figure 2 ‣ 1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"), under the high compression ratio, the retained visual tokens of G-Prune in adjacent frames are prone to similarity and redundancy, and this case suggests that existing compression methods mainly focus on image-wise importance, while lacking a sufficient evaluation of global visual redundancy across video frames.

![Refer to caption](https://arxiv.org/html/2603.22911v2/visual_v10.png)Figure 2: Visualization of token pruning by G-Prune  \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] and our ForestPrune. The image-centric G-Prune can well keep the important tokens for each frame, but also leads to obvious redundancy across frames. In contrast, our ForestPrune can obtain a globally optimal pruning via spatial-temporal forest modeling.

In this paper, we investigate this problem from the perspective of _spatial-temporal forest modeling_, and propose an innovative and training-free method termed _ForestPrune_ for video MLLMs.
In principle, ForestPrune aims to model the importance of visual tokens across frames via building semantic trees based on both their spatial and temporal priors.
In this case, we can evaluate the global importance of visual tokens based on the depth of trees and the role of nodes, _e.g._, the root or trunk nodes of a deeper tree are more important. In practice, ForestPrune first obtains the representative tokens of each video frame and then considers them as the potential tree nodes.
Afterwards, ForestPrune constructs a spatial-temporal forest by gating tokens with semantic similarity, spatial alignment and temporal order. Given the constructed token forests, we perform the budgeted selection of tokens via prioritizing the pruning of leaf and tail nodes.
In this case, ForestPrune can obtain a global optimal pruning decision across video frames.

To validate ForestPrune, we apply it to two representative MLLMs, namely LLaVA-Video \[ [66](https://arxiv.org/html/2603.22911v2#bib.bib16 "")\] and LLaVA-OneVision \[ [22](https://arxiv.org/html/2603.22911v2#bib.bib17 "")\], and conduct extensive experiments on five highly competitive video benchmarks \[ [56](https://arxiv.org/html/2603.22911v2#bib.bib20 ""), [12](https://arxiv.org/html/2603.22911v2#bib.bib22 ""), [68](https://arxiv.org/html/2603.22911v2#bib.bib21 ""), [52](https://arxiv.org/html/2603.22911v2#bib.bib19 ""), [26](https://arxiv.org/html/2603.22911v2#bib.bib18 "")\].
The experimental results not only show the outstanding compression results of ForestPrune for two MLLMs, _e.g._, retaining 95.8% average accuracy while pruning 90% tokens of LLaVA-OneVision, but also show its superiority than the compared methods, _e.g._, +10.1% accuracy than FrameFusion \[ [13](https://arxiv.org/html/2603.22911v2#bib.bib54 "")\] on MLVU while reducing 81.4% more computation on LLaVA-Video.
Moreover, using ForestPrune to scale up input frames can also help LLaVA-Video approach SOTA performance on some metrics, _e.g._, 72.5 on MLVU.
These results well validate the effectiveness of our ForestPrune for video-MLLMs in terms of high-ratio visual compression, and also confirm our intuition about spatial-temporal modeling for video redundancy evaluation.

Overall, our contributions are three-fold:

- •


We reveal the critical ingredient for effective video token compression, _i.e._, the spatial and temporal modeling for continuous video content.

- •


We propose a novel and training-free approach for video MLLMs, termed _ForestPrune_, which adopts spatial-temporal forest modeling to evaluate the global importance of visual tokens across video frames.

- •


The proposed ForestPrune helps two video-MLLMs well retain the performance while reducing a large number of redundant tokens. Moreover, it also shows obvious merits than the compared compression methods in terms of both performance and efficiency.


## 2 Related Work

### 2.1 Video LLMs

Recent multimodal LLMs have been extended to videos \[ [1](https://arxiv.org/html/2603.22911v2#bib.bib31 ""), [41](https://arxiv.org/html/2603.22911v2#bib.bib11 ""), [48](https://arxiv.org/html/2603.22911v2#bib.bib26 ""), [27](https://arxiv.org/html/2603.22911v2#bib.bib37 ""), [63](https://arxiv.org/html/2603.22911v2#bib.bib5 ""), [9](https://arxiv.org/html/2603.22911v2#bib.bib36 ""), [32](https://arxiv.org/html/2603.22911v2#bib.bib24 ""), [65](https://arxiv.org/html/2603.22911v2#bib.bib8 ""), [22](https://arxiv.org/html/2603.22911v2#bib.bib17 ""), [66](https://arxiv.org/html/2603.22911v2#bib.bib16 ""), [49](https://arxiv.org/html/2603.22911v2#bib.bib14 ""), [3](https://arxiv.org/html/2603.22911v2#bib.bib15 ""), [7](https://arxiv.org/html/2603.22911v2#bib.bib12 ""), [50](https://arxiv.org/html/2603.22911v2#bib.bib13 ""), [34](https://arxiv.org/html/2603.22911v2#bib.bib58 "")\]. LLaVA-OneVision \[ [22](https://arxiv.org/html/2603.22911v2#bib.bib17 "")\] unifies image and video in a single framework, transferring visual knowledge across scenarios with high-resolution inputs. LLaVA-Video \[ [66](https://arxiv.org/html/2603.22911v2#bib.bib16 "")\] scales to large synthetic video-instruction data, yielding strong results across diverse video QA/reasoning benchmarks. Beyond LLaVA family models, Qwen2-VL \[ [49](https://arxiv.org/html/2603.22911v2#bib.bib14 "")\] emphasizes high-resolution encoders and long-context handling, Qwen2.5-VL \[ [3](https://arxiv.org/html/2603.22911v2#bib.bib15 "")\] upgrades Qwen2-VL with stronger recognition and long-video comprehension under a unified image–video paradigm. NVILA \[ [34](https://arxiv.org/html/2603.22911v2#bib.bib58 "")\] targets efficiency by scaling spatial and temporal resolution while compressing visual tokens for a better accuracy–latency trade-off. Despite these advances, processing multiple frames leads to a surge in visual tokens and heavy compute costs, motivating efficient token compression for video LLMs. InternVL 3.5 \[ [50](https://arxiv.org/html/2603.22911v2#bib.bib13 "")\] adopts a Visual Resolution Router and Decoupled Vision-Language Deployment to significantly improve the performance of open-source video MLLMs.

### 2.2 Visual Token Compression Methods

Visual token compression methods were initially developed for image tasks and later extended to video domains \[ [6](https://arxiv.org/html/2603.22911v2#bib.bib1 ""), [58](https://arxiv.org/html/2603.22911v2#bib.bib45 ""), [4](https://arxiv.org/html/2603.22911v2#bib.bib2 ""), [60](https://arxiv.org/html/2603.22911v2#bib.bib44 ""), [62](https://arxiv.org/html/2603.22911v2#bib.bib59 ""), [67](https://arxiv.org/html/2603.22911v2#bib.bib60 ""), [59](https://arxiv.org/html/2603.22911v2#bib.bib61 ""), [2](https://arxiv.org/html/2603.22911v2#bib.bib62 ""), [11](https://arxiv.org/html/2603.22911v2#bib.bib63 ""), [46](https://arxiv.org/html/2603.22911v2#bib.bib56 ""), [69](https://arxiv.org/html/2603.22911v2#bib.bib69 ""), [55](https://arxiv.org/html/2603.22911v2#bib.bib70 "")\]. FastV \[ [6](https://arxiv.org/html/2603.22911v2#bib.bib1 "")\] drops low-contribution visual tokens using early-layer attention scores to reduce computation while keeping accuracy. VisionZip \[ [60](https://arxiv.org/html/2603.22911v2#bib.bib44 "")\] first selects a small set of anchor tokens via saliency and then semantically merges the remaining tokens into compact composites. FitPrune \[ [61](https://arxiv.org/html/2603.22911v2#bib.bib38 "")\] selects retained tokens by minimizing the attention distribution difference before and after pruning. G-Prune \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] builds a similarity graph and preserves a representative set of tokens by propagating importance to avoid redundant picks. HoloV \[ [71](https://arxiv.org/html/2603.22911v2#bib.bib47 "")\] allocates the pruning budget across spatial regions to prevent repeatedly keeping highly similar “hotspot” tokens. For video visual token compression methods, PruneVid \[ [16](https://arxiv.org/html/2603.22911v2#bib.bib53 "")\] leverages LLMs’ reasoning capabilities to selectively prune visual features which are relevant to question. FrameFusion \[ [13](https://arxiv.org/html/2603.22911v2#bib.bib54 "")\] aligns adjacent frames to merge duplicated regions early and prunes by importance in deeper layers to balance speed and accuracy. STTM \[ [18](https://arxiv.org/html/2603.22911v2#bib.bib55 "")\] performs multi-granularity merging within and across frames to explicitly model spatial–temporal redundancy. Holitom \[ [45](https://arxiv.org/html/2603.22911v2#bib.bib57 "")\] employs outer-LLM pruning through global redundancy-aware temporal segmentation, followed by spatial-temporal merging to reduce visual tokens.
Overall, existing methods are more effective for single images but also easy to keep redundancy across frames.

![Refer to caption](https://arxiv.org/html/2603.22911v2/Temporal_Forest_Method_Fig_v12.png)Figure 3: Illustration of the proposed ForestPrune.
Input video frames are first encoded by the visual encoder, based on which ForestPrune will select a set of tokens of each frame as the candidate nodes. Afterwards, ForestPrune constructs the token trees based on the semantic similarity τs\\tau\_{s}, spatial distance τp\\tau\_{p} and the frame temporal orders, thereby forming the _spatial-temporal forest_ (a). When obtaining excessive trees (root nodes), we will merge them before pruning (b). Then, we sort the trees in a descending order of depth (c) and then progressively prune the leaf and tail nodes until meeting the compression budget (d). Via the spatial-temporal modeling, ForestPrune can well estimate the frame-wise redundancy and obtain a globally optimal pruning decision.

## 3 Method

### 3.1 Overview

In this paper, we propose an innovative and training-free method termed _ForestPrune_ for video MLLMs, of which framework is illustrated in Fig [3](https://arxiv.org/html/2603.22911v2#S2.F3 "Figure 3 ‣ 2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").
ForestPrune aims to model the visual tokens across frames via building semantic trees based on both their spatial and temporal priors.
In this case, we can evaluate the global importance of visual tokens based on the tree depth and node roles.

Concretely, given a video VV sampled for TT frames, each frame is processed by the image encoder, and we obtain the frame features 𝐅ti∈ℝN×d\\mathbf{F}\_{t\_{i}}\\in\\mathbb{R}^{N\\times d}, where NN denotes the number of tokens and dd is the feature dimension. Thus, the whole video features can be denoted by 𝐅V∈ℝ(T×N)×d\\mathbf{F}\_{V}\\in\\mathbb{R}^{(T\\times N)\\times d}.

In terms of visual compression, the optimization aims to reduce the number of visual tokens according to a predefined compression budget bb:

|     |     |     |     |
| --- | --- | --- | --- |
|  | min𝒟(G(𝐅V′),G(𝐅V))s.t.b.\\min\\mathcal{D}\\big(G(\\mathbf{F}\_{V}^{\\prime}),\ \ G(\\mathbf{F}\_{V})\\big)\ s.t.\ b. |  | (1) |

Here, G⁡(⋅)G(\\cdot) denotes the MLLM and 𝒟⁡(⋅)\\mathcal{D(\\cdot)} denotes the difference between the outputs of MLLM before and after compression.
𝐅V′∈ℝK×d\\mathbf{F}\_{V}^{\\prime}\\in\\mathbb{R}^{K\\times d} is the compressed video features, which can be achieved via token pruning \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] or merging  \[ [60](https://arxiv.org/html/2603.22911v2#bib.bib44 "")\]. And the budget bb is calculated by K/(T×N)K/(T\\times N).

Existing compression methods \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 ""), [60](https://arxiv.org/html/2603.22911v2#bib.bib44 "")\] for image MLLMs often focus on image-wise token compression, _i.e._, 𝐅ti∈ℝk×d\\mathbf{F}\_{t\_{i}}\\in\\mathbb{R}^{k\\times d}, where kk is the number of retained tokens per frame, yielding a multi-frame compression budget b=T×k/T×Nb=T\\times k/T\\times N. However, this paradigm is prone to losing the overall consideration of all visual tokens, and also lacks of temporal and continual modeling of videos.

In this case, ForestPrune models the token compression via _spatial-temporal forests_. Concretely, for the better construction of node forests (trees), we first select the representative tokens of each frame as the nodes, of which process can be conducted via existing token pruning methods \[ [60](https://arxiv.org/html/2603.22911v2#bib.bib44 ""), [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] or random sampling.

Thus, we can obtain the slimmed video features, denoted as 𝐅n​o​d∈ℝ(T×N′)×d\\mathbf{F}\_{nod}\\in\\mathbb{R}^{(T\\times N^{\\prime})\\times d}, where N′<NN^{\\prime}<N.
Based on 𝐅n​o​d\\mathbf{F}\_{nod}, we then construct the semantic trees based on the semantic distance, spatial constraint and temporal order, of which process will be detailed later. Then, we can obtain a spatial-temporal forest consisting of token trees, denoted by 𝐅t​r​e​ei∈ℝk×d\\mathbf{F}\_{tree}^{i}\\in\\mathbb{R}^{k\\times d}, where kk denotes the number of tree nodes.

Afterwards, we rank the importance of these trees based on their depths, and then select the token nodes based on their roles, _i.e._, the root or trunk nodes.
In this case, we can obtain the compressed video features 𝐅v′∈ℝK×d\\mathbf{F}\_{v}^{\\prime}\\in\\mathbb{R}^{K\\times d}, where K<<T×NK<<T\\times N.
The detailed procedure of spatial-temporal tree construction and token selection is given in the following selections.

### 3.2 Spatial-Temporal Forest Construction

In terms of token tree construction, we not only measure the semantics among nodes \[ [4](https://arxiv.org/html/2603.22911v2#bib.bib2 "")\], but also consider the spatial and temporal priors.
In this case, we also record the coordinate information of each token in their default frames,
S∈ℝ(T×N′)×2S\\in\\mathbb{R}^{(T\\times N^{\\prime})\\times\\text{2}}, as well as their temporal timesteps,
T∈ℝ(T×N′)×1\\mathrm{T}\\in\\mathbb{R}^{(T\\times N^{\\prime})\\times\\text{1}}, for spatial-temporal forest modeling .

Concretely, given the representative node features of all frames 𝐅n​o​d\\mathbf{F}\_{nod}, we first compute their adjacency matrix of cosine similarity A∈ℝ(T×N′)×(T×N′)A\\in\\mathbb{R}^{(T\\times N^{\\prime})\\times(T\\times N^{\\prime})}:

|     |     |     |     |
| --- | --- | --- | --- |
|  | A=𝐅n​o​d​𝐅n​o​dT.A=\\mathbf{F}\_{nod}\\mathbf{F}\_{nod}^{\\text{T}}. |  | (2) |

Meanwhile, we also compute the spatial distances between nodes, forming the distance matrix D∈ℝ(T×N′)×(T×N′)D\\in\\mathbb{R}^{(T\\times N^{\\prime})\\times({T\\times N^{\\prime}})} based on SS. And its element is

|     |     |     |     |
| --- | --- | --- | --- |
|  | di​j=∥si−sj∥2,d\_{ij}=\\lVert s\_{i}-s\_{j}\\rVert\_{2}\ , |  | (3) |

where si∈ℝ2s\_{i}\\in\\mathbb{R}^{2} represents the coordinates of the ii-th node.

Based on AA and DD, we can build a connection matrix C∈ℝ(T×N′)×(T×N′)C\\in\\mathbb{R}^{(T\\times N^{\\prime})\\times(T\\times N^{\\prime})} between nodes thresholded by the semantic and temporal constraints, denoted as τs\\tau\_{s} and τp\\tau\_{p}, respectively. The element of CC is defined by

|     |     |     |     |
| --- | --- | --- | --- |
|  | ci​j={1if ​(ai​j≥τs)∧(di​j≤τp),0otherwise.c\_{ij}=\\begin{cases}1\\quad\\text{if }\ (a\_{ij}\\geq\\tau\_{s})\\land(d\_{ij}\\leq\\tau\_{p}),\\\<br>0\\quad\\text{otherwise}.\\end{cases} |  | (4) |

We further update CC based on the temporal timesteps of nodes TT:

|     |     |     |     |
| --- | --- | --- | --- |
|  | ci​j={1if​(ci​j=1)∧(ti<tj),0otherwise.c\_{ij}=\\begin{cases}1\\quad\\text{if}\ (c\_{ij}=1)\\land(t\_{i}<t\_{j}),\\\<br>0\\quad\\text{otherwise}.\\end{cases} |  | (5) |

Via Eq. [4](https://arxiv.org/html/2603.22911v2#S3.E4 "Equation 4 ‣ 3.2 Spatial-Temporal Forest Construction ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling")- [5](https://arxiv.org/html/2603.22911v2#S3.E5 "Equation 5 ‣ 3.2 Spatial-Temporal Forest Construction ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"), we can obtain the potential connections of nodes under the semantic, spatial and temporal constraints. However, the building of spatial-temporal trees remains unsolved.
To this end, we first obtain the set of root nodes via computing the input degrees of CC:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|  |  | ℛ={j∣j∈𝒱∧(∑i=1kci​j′=0)∧(∑j=1kci​j′≠0)},\\displaystyle\\mathcal{R}=\\Big\\{j\\mid j\\in\\mathcal{V}\\land(\\sum\_{i=1}^{k}c^{\\prime}\_{ij}=0)\\land(\\sum\_{j=1}^{k}c^{\\prime}\_{ij}\\neq 0)\\Big\\}, |  | (6) |

where ℛ\\mathcal{R} recodes the indices of root nodes, 𝒱\\mathcal{V} denotes the set of token nodes, and \|𝒱\|=k=T×N′\|\\mathcal{V}\|=k=T\\times N^{\\prime}.

Afterwards, we collect the child nodes for each root one. In particular, although CC reflect the feasible connections between nodes, but they are still likely linked to different trees (root nodes). To avoid this case, we build another ranking matrix PP based on AA and DD:

|     |     |     |     |
| --- | --- | --- | --- |
|  | P=C⊙(A−λ​D),P=C\ \\odot\ \\big(A-\\lambda\\,D\\big), |  | (7) |

where A−λ​DA-\\lambda D is used to consider both semantic and spatial distances between nodes, their values are larger than 0. λ\\lambda is a hyper-parameter that controls the trade-off.

PP can be used to identify the belonging of child nodes via ranking their scores to root ones.
Then, we identify the nodes for each root jj in ℛ\\mathcal{R} based on PP and CC, and obtain the tree nodes 𝒱j\\mathcal{V}\_{j}:

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝒱j={i∣arg⁡maxi∈𝒱⁡pi​j∧(∑i=1kpi​j≠0)}.\\mathcal{V}\_{j}=\\Big\\{i\\mid\\arg\\max\_{i\\in\\mathcal{V}}p\_{ij}\\land(\\sum\_{i=1}^{k}p\_{ij}\\neq 0)\\Big\\}. |  | (8) |

Given the nodes of a tree 𝒱j\\mathcal{V}\_{j}, we use a _LinkNode_ function to obtain its connections EE and the tree depth dd:

|     |     |     |     |
| --- | --- | --- | --- |
|  | L​i​n​k​N​o​d​e​(rj,𝒱j,T,C)→E,d.LinkNode(r\_{j},\\mathcal{V}\_{j},T,C)\\rightarrow E,d. |  | (9) |

Afterwards we can obtain the tree as well as its connections 𝒯j=⟨Vj,Ej⟩\\mathcal{T}\_{j}=\\langle V\_{j},E\_{j}\\rangle. The detailed process of LinkNode is given in Algorithm [1](https://arxiv.org/html/2603.22911v2#alg1 "Algorithm 1 ‣ 3.2 Spatial-Temporal Forest Construction ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"), which well considers the temporal information of all nodes.

Algorithm 1 LinkNode(⋅)(\\cdot)

1:rjr\_{j}, 𝒱j\\mathcal{V}\_{j}, TT, CC

2:EE, dd

3:fort=1t=1toT−1T-1do

4:𝒱t′={nit∣ni∈𝒱j∧Ti=t}\\mathcal{V}^{\\prime}\_{t}=\\Big\\{n\_{i}^{t}\\mid n\_{i}\\in\\mathcal{V}\_{j}\\land T\_{i}=t\\Big\\}

5:if𝒱t′=∅\\mathcal{V}^{\\prime}\_{t}=\\varnothingthen

6:continue

7:foreachnit∈𝒱t′n\_{i}^{t}\\in\\mathcal{V}^{\\prime}\_{t}do

8:ifnit=rjn\_{i}^{t}=r\_{j}then

9:d=0d=0; continue

10:else

11:E=E+⟨nit,njt′⟩​s.t.ci​j=1, 1≤t′<tE=E+\\langle n\_{i}^{t},n\_{j}^{t^{\\prime}}\\rangle\ s.t.\ c\_{ij}=1,\ 1\\leq t^{\\prime}<t

12:d=d+1d=d+1

13:returnEE, dd

In particular, when the number of root nodes are much larger than that of the retained tokens, _i.e._, \|ℛ\|>>K\|\\mathcal{R}\|>>K, we will combine trees based on the root similarities, and then update the new trees.

### 3.3 Token Pruning

After the construction of spatial-temporal forest, _i.e._, Sec. [3.2](https://arxiv.org/html/2603.22911v2#S3.SS2 "3.2 Spatial-Temporal Forest Construction ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"), we then conduct the token pruning based on the depth of trees and the role of nodes.

Specifically, given the depths of all trees in the forest, d={d1,d2,…,d\|ℛ\|}d=\\Big\\{d\_{1},d\_{2},...,d\_{\|\\mathcal{R}\|}\\Big\\}, we first sort the trees based on their depth, and then remove the leaf nodes from the trees in descending order of depth. When only root and trunk nodes remain in all trees, but the pruning budget is still not met. We will progressively remove the nodes at the ends of trees.

For instance, given a tree denoted as 𝒯j=⟨Vj,Ej⟩\\mathcal{T}\_{j}=\\langle V\_{j},E\_{j}\\rangle with a depth of djd\_{j}, the leaf nodes Vj′V\_{j}^{\\prime} can be obtained by

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝒱j′={i∣i∈𝒱j∧(∑j=1kci​j=0)},\\mathcal{V}^{\\prime}\_{j}=\\Big\\{i\\mid i\\in\\mathcal{V}\_{j}\\land(\\sum\_{j=1}^{k}c\_{ij}=0)\\Big\\}, |  | (10) |

and we discard the leaf nodes by 𝒱k=𝒱j−𝒱j′\\mathcal{V}\_{k}=\\mathcal{V}\_{j}-\\mathcal{V}^{\\prime}\_{j}.

And for the tail nodes of the pruned tree, we can remove them via

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝒱t​a​i​l=maxj∈𝒱j⁡Tj,𝒱k=𝒱j−𝒱t​a​i​l.\\mathcal{V}\_{tail}=\\max\_{j\\in\\mathcal{V}\_{j}}T\_{j},\ \\mathcal{V}\_{k}=\\mathcal{V}\_{j}-\\mathcal{V}\_{tail}. |  | (11) |

This process will be progressively conducted until reaching the pruning budget. Besides, under high-ratio pruning setting, if only the root nodes are kept, we will select the ones with default earlier timesteps as the remaining nodes for the budget. Finally, we obtain the pruned node set 𝒱K⊂𝒱\\mathcal{V}\_{K}\\subset\\mathcal{V} and the pruned feature 𝐅v′∈ℝK×d\\mathbf{F}\_{v}^{\\prime}\\in\\mathbb{R}^{K\\times d}.

## 4 Experiments

Table 1:
Comparison between ForestPrune and existing compression methods on LLaVA-Video-7B and LLaVA-OV 7B. Compression Ratio denotes the target reduction of visual tokens. Retain reflects the degree to which MLLM retains performance.

|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CompressionRatio | Method | NExT-QA | VideoMME | MLVU | LongVideoBench | MVBench | Avg |
| Acc↑\\uparrow | Retain↑\\uparrow | Acc↑\\uparrow | Retain↑\\uparrow | Acc↑\\uparrow | Retain↑\\uparrow | Acc↑\\uparrow | Retain↑\\uparrow | Acc↑\\uparrow | Retain↑\\uparrow | Retain↑\\uparrow |
| - | LLaVA-Video 7B | 82.9 | 100.0% | 62.8 | 100.0% | 71.3 | 100.0% | 60.4 | 100.0% | 61.2 | 100.0% | - |
| 70% | FastV \[ [6](https://arxiv.org/html/2603.22911v2#bib.bib1 "")\] | 81.3 | 98.1% | 60.0 | 95.5% | 64.2 | 90.0% | 56.8 | 94.0% | 57.5 | 94.0% | 94.5% |
| VisionZip \[ [60](https://arxiv.org/html/2603.22911v2#bib.bib44 "")\] | 82.3 | 99.3% | 61.3 | 97.6% | 69.8 | 97.9% | 58.8 | 97.4% | 57.7 | 94.3% | 97.4% |
| G-Prune \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] | 82.2 | 99.2% | 61.7 | 98.2% | 67.2 | 94.2% | 57.8 | 95.7% | 58.6 | 95.8% | 96.7% |
| STTM \[ [18](https://arxiv.org/html/2603.22911v2#bib.bib55 "")\] | 81.2 | 98.0% | 62.0 | 98.7% | 68.8 | 96.5% | 57.7 | 95.5% | - | - | 97.2% |
| FrameFusion \[ [13](https://arxiv.org/html/2603.22911v2#bib.bib54 "")\] | 81.1 | 97.8% | 60.8 | 96.8% | 67.3 | 94.4% | 59.3 | 98.2% | 60.3 | 98.5% | 97.1% |
| ForestPrune | 82.8 | 99.9% | 62.3 | 99.2% | 69.3 | 97.2% | 59.5 | 98.5% | 59.8 | 97.7% | 98.6% |
| 80% | FastV \[ [6](https://arxiv.org/html/2603.22911v2#bib.bib1 "")\] | 80.9 | 97.6% | 57.7 | 91.9% | 66.8 | 93.7% | 55.6 | 92.1% | 58.3 | 95.3% | 94.3% |
| VisionZip \[ [60](https://arxiv.org/html/2603.22911v2#bib.bib44 "")\] | 81.9 | 98.8% | 60.0 | 95.5% | 67.8 | 95.1% | 57.5 | 95.2% | 59.9 | 97.9% | 96.6% |
| G-Prune \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] | 81.3 | 98.1% | 60.0 | 95.5% | 65.5 | 91.9% | 56.5 | 93.5% | 59.8 | 97.7% | 95.4% |
| STTM \[ [18](https://arxiv.org/html/2603.22911v2#bib.bib55 "")\] | 80.9 | 97.6% | 59.8 | 95.2% | 67.1 | 94.1% | 55.9 | 92.6% | - | - | 95.1% |
| FrameFusion \[ [13](https://arxiv.org/html/2603.22911v2#bib.bib54 "")\] | 81.5 | 98.3% | 59.9 | 95.4% | 66.5 | 93.3% | 56.9 | 94.2% | 59.6 | 97.4% | 95.8% |
| ForestPrune | 82.4 | 99.4% | 60.5 | 96.3% | 68.5 | 96.1% | 57.6 | 95.4% | 59.9 | 97.9% | 97.1% |
| 90% | FastV \[ [6](https://arxiv.org/html/2603.22911v2#bib.bib1 "")\] | 73.2 | 88.3% | 53.4 | 85.0% | 58.5 | 82.1% | 52.6 | 87.1% | 51.3 | 83.8% | 85.4% |
| VisionZip \[ [60](https://arxiv.org/html/2603.22911v2#bib.bib44 "")\] | 79.6 | 96.0% | 57.0 | 90.8% | 64.5 | 90.5% | 51.9 | 85.9% | 51.7 | 84.5% | 90.0% |
| G-Prune \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] | 78.4 | 94.6% | 57.7 | 91.9% | 59.9 | 84.0% | 52.1 | 86.3% | 52.5 | 85.8% | 88.8% |
| STTM \[ [18](https://arxiv.org/html/2603.22911v2#bib.bib55 "")\] | 65.0 | 78.4% | 56.0 | 89.2% | 64.8 | 90.9% | 54.5 | 90.2% | - | - | 86.6% |
| FrameFusion \[ [13](https://arxiv.org/html/2603.22911v2#bib.bib54 "")\] | 78.9 | 95.2% | 55.4 | 88.2% | 60.3 | 84.6% | 54.7 | 90.6% | 57.2 | 93.5% | 90.5% |
| ForestPrune | 81.0 | 97.7% | 59.1 | 94.1% | 66.4 | 93.1% | 55.9 | 92.6% | 57.8 | 94.4% | 94.6% |
| - | LLaVA-OV 7B | 80.1 | 100.0% | 58.7 | 100.0% | 64.4 | 100.0% | 56.8 | 100.0% | 58.2 | 100.0% | - |
| 70% | FastV \[ [6](https://arxiv.org/html/2603.22911v2#bib.bib1 "")\] | 78.8 | 98.4% | 55.7 | 94.9% | 61.9 | 96.1% | 55.5 | 97.7% | 55.5 | 95.4% | 96.6% |
| VisionZip \[ [60](https://arxiv.org/html/2603.22911v2#bib.bib44 "")\] | 79.1 | 98.8% | 57.2 | 97.4% | 64.2 | 99.7% | 55.9 | 98.4% | 56.2 | 96.6% | 98.2% |
| G-Prune \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] | 79.3 | 99.0% | 57.4 | 97.8% | 63.2 | 98.1% | 56.8 | 100.0% | 56.1 | 96.4% | 98.3% |
| STTM \[ [18](https://arxiv.org/html/2603.22911v2#bib.bib55 "")\] | 79.9 | 99.8% | 58.7 | 100% | 63.7 | 98.9% | 54.6 | 96.1% | - | - | 98.8% |
| FrameFusion \[ [13](https://arxiv.org/html/2603.22911v2#bib.bib54 "")\] | 80.3 | 100.2% | 57.2 | 97.4% | 63.9 | 99.2% | 55.1 | 97.0% | 57.6 | 99.0% | 98.7% |
| ForestPrune | 79.8 | 99.6% | 57.7 | 98.3% | 64.4 | 100.0% | 56.3 | 99.1% | 57.3 | 98.5% | 99.2% |
| 80% | FastV \[ [6](https://arxiv.org/html/2603.22911v2#bib.bib1 "")\] | 77.6 | 96.9% | 52.9 | 90.1% | 59.5 | 92.4% | 52.7 | 92.8% | 53.7 | 92.3% | 93.1% |
| VisionZip \[ [60](https://arxiv.org/html/2603.22911v2#bib.bib44 "")\] | 78.6 | 98.1% | 56.3 | 95.9% | 62.5 | 97.1% | 53.7 | 94.5% | 56.2 | 96.6% | 96.6% |
| G-Prune \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] | 78.4 | 97.9% | 55.8 | 95.1% | 61.7 | 95.8% | 52.5 | 92.4% | 55.5 | 95.4% | 95.5% |
| STTM \[ [18](https://arxiv.org/html/2603.22911v2#bib.bib55 "")\] | 78.8 | 98.4% | 56.1 | 95.6% | 63.7 | 98.9% | 52.3 | 92.1% | - | - | 96.5% |
| FrameFusion \[ [13](https://arxiv.org/html/2603.22911v2#bib.bib54 "")\] | 79.6 | 99.4% | 56.3 | 95.9% | 61.7 | 95.8% | 54.4 | 95.8% | 57.4 | 98.6% | 97.2% |
| ForestPrune | 79.2 | 98.9% | 56.8 | 96.8% | 64.1 | 99.5% | 56.2 | 98.9% | 57.6 | 99.0% | 98.6% |
| 90% | FastV \[ [6](https://arxiv.org/html/2603.22911v2#bib.bib1 "")\] | 76.4 | 95.4% | 50.9 | 86.7% | 57.4 | 89.1% | 51.2 | 90.1% | 53.0 | 91.1% | 90.8% |
| VisionZip \[ [60](https://arxiv.org/html/2603.22911v2#bib.bib44 "")\] | 74.4 | 92.9% | 50.8 | 86.5% | 58.7 | 91.2% | 47.7 | 84.0% | 52.0 | 89.4% | 89.1% |
| G-Prune \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] | 73.1 | 91.8% | 53.1 | 90.5% | 53.1 | 82.5% | 50.1 | 88.2% | 52.3 | 89.9% | 88.5% |
| STTM \[ [18](https://arxiv.org/html/2603.22911v2#bib.bib55 "")\] | 72.4 | 90.4% | 49.8 | 84.8% | 60.2 | 93.5% | 50.1 | 88.2% | - | - | 89.4% |
| FrameFusion \[ [13](https://arxiv.org/html/2603.22911v2#bib.bib54 "")\] | 77.9 | 97.3% | 51.8 | 88.2% | 57.5 | 89.3% | 51.1 | 90.0% | 55.5 | 95.4% | 92.3% |
| ForestPrune | 77.2 | 96.4% | 55.8 | 95.1% | 61.3 | 95.2% | 55 | 96.8% | 55.6 | 95.5% | 95.8% |

Table 2: Comparison between LLaVA-Video using ForestPrune and existing SOTA MLLMs.
Keeping the same amount of input tokens, we use ForestPrune to scale up the input video frames, and achieve obvious performance gains.

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| Model | Size | Frames | Input tokens | VideoMME | MLVU |
| Acc↑\\uparrow | Acc↑\\uparrow |
| GPT-4V/4T  \[ [1](https://arxiv.org/html/2603.22911v2#bib.bib31 "")\] | - | 10 | - | 59.9 | 49.2 |
| Qwen2.5-VL  \[ [3](https://arxiv.org/html/2603.22911v2#bib.bib15 "")\] | 7B | 64 | >12544>12544 | 65.1 | 69.6 |
| Qwen3-VL  \[ [47](https://arxiv.org/html/2603.22911v2#bib.bib68 "")\] | 8B | 2fps | >12544>12544 | 71.4 | 78.1 |
| GLM-4.1V  \[ [14](https://arxiv.org/html/2603.22911v2#bib.bib67 "")\] | 9B | 64 | 16384 | 68.2 | 71.5 |
| InternVL3  \[ [70](https://arxiv.org/html/2603.22911v2#bib.bib66 "")\] | 8B | 64 | 16384 | 66.3 | 71.4 |
| InternVL3.5  \[ [50](https://arxiv.org/html/2603.22911v2#bib.bib13 "")\] | 8B | 64 | 16384 | 66.0 | 70.2 |
| LLaVA-Video \[ [66](https://arxiv.org/html/2603.22911v2#bib.bib16 "")\] | 7B | 64 | 10816 | 62.8 | 71.3 |
| \+ ForestPrune50%\\text{ForestPrune}\_{\\textbf{50\\%}} | 7B | 128 | 10816 | 63.7 | 70.5 |
| \+ ForestPrune75%\\text{ForestPrune}\_{\\textbf{75\\%}} | 7B | 256 | 10816 | 64.2 | 72.5 |
| \+ ForestPrune87.5%\\text{ForestPrune}\_{\\textbf{87.5\\%}} | 7B | 512 | 10816 | 66.5 | 72.2 |

Table 3: Ablation study of the construction manners and numbers of the potential tree nodes 𝐅n​o​d\\mathbf{F}\_{nod} for ForestPrune on LLaVA-Video.

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Node | FPrune | NExT-QA | VideoMME | MLVU |
| Acc↑\\uparrow | Retain↑\\uparrow | Acc↑\\uparrow | Retain↑\\uparrow | Acc↑\\uparrow | Retain↑\\uparrow |
| G-Prune | ×\\times | 74.7 | 91.0% | 57.7 | 91.9% | 59.9 | 84.0% |
| VisionZip | ×\\times | 76.5 | 91.7% | 57.0 | 90.8% | 64.5 | 90.5% |
| ×\\times | ✓\\checkmark | 80.1 | 96.0% | 58.9 | 93.8% | 63.9 | 89.6% |
| G-Prune | ✓\\checkmark | 81.0 | 97.1% | 59.1 | 94.1% | 66.4 | 93.1% |
| VisionZip | ✓\\checkmark | 80.6 | 96.6% | 58.4 | 93.0% | 66.7 | 93.5% |
| Random | ✓\\checkmark | 80.1 | 96.0% | 58.2 | 92.7% | 65.6 | 92.0% |
| The keep ratio of tree nodes for each frame |
| 100% | 80.1 | 96.0% | 58.9 | 93.8% | 63.9 | 89.6% |
| 70% | 80.6 | 97.2% | 58.9 | 93.8% | 66.4 | 93.1% |
| 60% | 80.7 | 97.3% | 58.9 | 93.8% | 66.4 | 93.1% |
| 50% | 80.8 | 97.5% | 58.8 | 93.6% | 66.4 | 93.1% |

### 4.1 Implement Detail

We apply our ForestPrune to two representative video MLLMs, namely LLaVA-Video-7B \[ [66](https://arxiv.org/html/2603.22911v2#bib.bib16 "")\] and LLaVA-OneVision-7B \[ [22](https://arxiv.org/html/2603.22911v2#bib.bib17 "")\].
Following their default settings, we input 64 frames with a 13×1313\\times 13 patch tokens on LLaVA-Video, and input 32 frames with a 14×1414\\times 14 tokens on LLaVA-OneVision.
We primarily set the semantic thresholds τs\\tau\_{s} to 0.9 and spatial thresholds τp\\tau\_{p} to 0.8, and their best settings are defined based on MLLM.
By default, we keep the number of nodes at 50% of the original number.
And we compare ForestPrune with other image and video pruning methods.
For image based method, we compare the pruning based methods of FastV \[ [6](https://arxiv.org/html/2603.22911v2#bib.bib1 "")\] and G-Prune \[ [20](https://arxiv.org/html/2603.22911v2#bib.bib46 "")\] and the hybrid method of VisionZip \[ [60](https://arxiv.org/html/2603.22911v2#bib.bib44 "")\] that adopts both token pruning and merging.
For video based methods, we compare two token merging methods, namely STTM \[ [18](https://arxiv.org/html/2603.22911v2#bib.bib55 "")\] and FrameFusion \[ [13](https://arxiv.org/html/2603.22911v2#bib.bib54 "")\].
Considering the differences in base MLLMs, experimental settings and the lack of results, we follow previous works \[ [18](https://arxiv.org/html/2603.22911v2#bib.bib55 ""), [13](https://arxiv.org/html/2603.22911v2#bib.bib54 "")\] to faithfully reproduce their performance in our experiments using their default code projects.

### 4.2 Benchmarks and Metrics

To validate ForestPrune, we conduct extensive experiments on five public video understanding benchmarks: NExT-QA \[ [56](https://arxiv.org/html/2603.22911v2#bib.bib20 "")\], MVBench \[ [26](https://arxiv.org/html/2603.22911v2#bib.bib18 "")\], VideoMME \[ [12](https://arxiv.org/html/2603.22911v2#bib.bib22 "")\], MLVU \[ [68](https://arxiv.org/html/2603.22911v2#bib.bib21 "")\], and LongVideoBench \[ [52](https://arxiv.org/html/2603.22911v2#bib.bib19 "")\].
NExT-QA is a multiple-choice video QA benchmark with short clips averaging about 44 seconds.
MVBench assesses multi-skill short-video understanding with clips averaging roughly 16 seconds.
VideoMME is a comprehensive benchmark, spanning short, medium and long videos.
MLVU targets at long videos ranging from 3 minutes to 2 hours, with an average around 15 minutes.
LongVideoBench covers diverse video pieces with four groups, which are 8–15 seconds, 15–60 seconds, 3–10 minutes, and 15–60 minutes, respectively.

### 4.3 Quantitative Analysis

Performance Comparison with SOTA methods.
We first compare ForestPrune to existing visual compression methods on LLaVA-Video and LLaVA-OV in Tab [1](https://arxiv.org/html/2603.22911v2#S4.T1 "Table 1 ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").
The performance of these base MLLMs without token compression are used as reference.
From these results, we can first observe that image-centric methods can still performs well in these video tasks.
For instance, VisionZip can outperform other video-based methods under the setting of LLaVA-Video-70%.
And G-Prune also performs well on LLaVA-OV, _e.g.,_ 98.3% for 70% pruning ratio.
However, under the extremely high pruning ratio, their retained performance still drop greatly, _e.g._, -9.1% and -7.4% by FastV and VisionZip from 70% to 90% ratios.
Besides, it can be also seen that the video-oriented methods, such as STTM and FrameFusion, are also inferior in high-ratio settings, _e.g.,_ 90%.
In stark contrast, our ForestPrune not only shows better performance than the compared methods, but also retain high accuracies under the high-ratio compression cases, _e.g._, 94.6% and 95.8% for LLaVA-Video and LLaVA-OV under the 90% setting.
These results well confirm the effectiveness of ForestPrune towards high-ratio video compression for MLLMs.

In addition, we also use ForestPrune to scale up the input frames of LLaVA-Video and compare it with existing SOTA MLLMs on VideoMME and MLVU, as reported in Tab [2](https://arxiv.org/html/2603.22911v2#S4.T2 "Table 2 ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").
From the table, we can first observe that ForestPrune can scale up the input frames while maintaining the same number of input tokens.
On both the VideoMME and MLVU benchmarks, ForestPrune significantly improves LLaVA-Video’s performance by processing more frames.
More importantly, we help LLaVA-Video outperform the most advanced video MLLMs such as InternVL3 and InternVL3.5 \[ [70](https://arxiv.org/html/2603.22911v2#bib.bib66 ""), [50](https://arxiv.org/html/2603.22911v2#bib.bib13 "")\].
Overall, ForestPrune not only maintains the model’s performance well under high pruning rates, but also improves model performance by scaling up the input frames.

Efficiency Comparison with SOTA methods.
We make efficiency comparisons between ForestPrune and a bunch of image and video pruning methods under the ratio of 90%, as shown in Fig [4](https://arxiv.org/html/2603.22911v2#S4.F4 "Figure 4 ‣ 4.3 Quantitative Analysis ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").
From these charts, we can first observe that all methods can well shorten the prefilling time of LLaVA-Video via reducing the amount of video tokens.
In particular, the prefilling efficiency of the pre-compression methods, such as G-Prune and our ForestPrune, is more obvious, since they compress tokens before MLLM’s encoding.
Similarly, these methods are also superior in the reductions of computation complexity and GPU memory overhead.
For the post-compression methods, _i.e._, compressing tokens in MLLMs due to their token evaluations in MLLMs, _e.g._, FrameFusion.
In particular, our ForestPrune is not only one of the most efficient approaches, but also, as mentioned in the previous paragraph, keeps the highest accuracies.
These results well confirm the efficiency of ForestPrune.

Figure 4: Efficiency comparison between ForestPrune and three existing methods. It is using LLaVA-Video with 90% compression ratio. _GPU memory_ records the peak usage.

Ablation Study.
In Tab [3](https://arxiv.org/html/2603.22911v2#S4.T3 "Table 3 ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"), we first ablate the collection and number of candidate tree nodes, _i.e._, 𝐅n​o​d\\mathbf{F}\_{nod} in Sec [3.1](https://arxiv.org/html/2603.22911v2#S3.SS1 "3.1 Overview ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").
Here, the performance of G-Prune and VisionZip are used as reference.
From the first block of the table, we can observe that the selection of tree nodes from each frame has a certain impact on ForestPrune.
For instance, using all frame tokens will be more difficult to construct the spatial-temporal trees, resulting in sub-optimal performance, _i.e._, ×\\times in _Image_.
A better selection of tree nodes can help to improve performance, _e.g._, ⟨G-Prune,✓⟩\\langle\\text{G-Prune},\\checkmark\\rangle, but it has not great difference in methodologies, _e.g._, _Random_ is also feasible.
Similarly, from the second block, we can also see that keeping a smaller number of frame tokens are beneficial in tree construction.
But it does not much matters the results.

Table 4: Ablation of the semantic and spatial hyper-parameters of ForestPrune on LLaVA-Video-7B, _i.e._, τs\\tau\_{s} and τp\\tau\_{p}.

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| τs\\tau\_{s} | τp\\tau\_{p} | NExT-QA | VideoMME | MLVU |
| Acc↑\\uparrow | Retain↑\\uparrow | Acc↑\\uparrow | Retain↑\\uparrow | Acc↑\\uparrow | Retain↑\\uparrow |
| 0.95 | 0.80 | 80.7 | 97.3% | 58.8 | 93.6% | 66.4 | 93.1% |
| 0.90 | 0.80 | 80.9 | 97.6% | 58.8 | 93.6% | 66.4 | 93.1% |
| 0.80 | 0.80 | 79.8 | 96.3% | 58.8 | 93.6% | 66.4 | 93.1% |
| 0.80 | 0.50 | 79.4 | 95.8% | 58.5 | 93.2% | 65.8 | 92.3% |
| 0.80 | 0.60 | 79.5 | 95.9% | 58.5 | 93.2% | 65.3 | 91.6% |
| 0.80 | 0.90 | 80.2 | 96.7% | 58.9 | 93.8% | 66.4 | 93.1% |
| 0.80 | 0.95 | 81.0 | 97.7% | 58.8 | 93.6% | 66.1 | 92.7% |

In Tab [4](https://arxiv.org/html/2603.22911v2#S4.T4 "Table 4 ‣ 4.3 Quantitative Analysis ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"), we ablate the two hyper-parameters τs,τp\\tau\_{s},\\tau\_{p} of ForestPrune, _i.e._, the semantic and spatial constraints, respectively.
These two hyper-parameters also affect the qualities of constructed trees.
We can see that via using a large threshold values, ForestPrune can construct better token trees with fewer noisy connections, thereby facilitating the final token pruning.
We can also see that using a smaller spatial threshold increases noisy connections in the token tree, leading to slight drops in performance.
Similar to Tab [3](https://arxiv.org/html/2603.22911v2#S4.T3 "Table 3 ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"), when the thresholds reach a certain value, ForestPrune is not sensitive to their slight changes, _e.g._, the performance of 60% and 50% are almost the same.
Overall, these results well confirm the effectiveness and robustness of our ForestPrune towards its designs and settings.

![Refer to caption](https://arxiv.org/html/2603.22911v2/forest_v16.png)Figure 5: Visualized results of ForestPrune.
Subfigure-(a) shows the spatial-temporal tree built by ForestPrune and the compression results, which show ForestPrune’s global spatial-temporal modeling capabilities.
Subfigure-(b) shows the compression results of ForestPrune, G-Prune, and VisionZip, showcasing ForestPrune’s ability to reduce temporal redundancy compared to image compression methods.
The ORANGE and BLUE trees are the spatial-temporal trees.
Frames with scene changes occur are shown with GREEN boxes.

### 4.4 Qualitative Analysis

To gain deeper insight into ForestPrune’s process of building a spatial-temporal forest, we visualize its forest construction and pruning results, as shown in Fig [5](https://arxiv.org/html/2603.22911v2#S4.F5 "Figure 5 ‣ 4.3 Quantitative Analysis ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling")(a).
As observed, the spatial-temporal tree can span multiple frames, allowing each tree to represent global temporal information.
And we can see that the nodes in a same tree are similar, _e.g._, the orange tree in the Exp.1 which capture human’s face.
This proves that the spatial-temporal trees can capture similar semantic information across video.
In addition, it can be seen that due to the spatial constraint of the spatial-temporal trees, the trees can only be constructed within a limited area, _e.g._, the orange and blue trees in the Exp.3.
This reduces noisy in the tree, making the spatial-temporal tree more accurate.

In the Fig [5](https://arxiv.org/html/2603.22911v2#S4.F5 "Figure 5 ‣ 4.3 Quantitative Analysis ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling")(b), we visualize the compression results of ForestPrune, G-Prune, and VisionZip on different video examples.
First, ForestPrune gradually reduces the number of tokens per frame when consecutive scenes are similar.
Afterward, when the scene changes, the number of tokens retained by ForestPrune increases rapidly.
In addition, if a scene reappear, the number of tokens retained by ForestPrune increased slightly.
These phenomena indicate that ForestPrune effectively preserves diversity information in the video.
In contrast, G-Prune and VisionZip exhibit substantial temporal redundancy in the retained tokens.
For instance, in the Exp.1 and Exp.2, ForestPrune retains a more diverse range of tokens, while G-Prune and VisionZip repeatedly retain nearly the same tokens across similar frames. Overall, these results well confirm the merits of ForestPrune in spatial-temporal modeling.

## 5 Conclusion

In this paper, we introduce ForestPrune, a novel and training-free high-ratio compression method for video MLLMs.
ForestPrune constructs token forests across video frames based on the semantic, spatial and temporal constraints.
Extensive comparisons with existing compression methods across various benchmarks demonstrate that ForestPrune well retain the video MLLMs performance while reducing a large number of redundant tokens, fully validating its designs and our motivations.

## 6 Acknowledgments

This work was supported by the National Key Research and Development Program of China (No.2025YFE0113500), the National Science Fund for Distinguished Young Scholars (No.62525605), the National Natural Science Foundation of China (No.U25B2066, No.U22B2051, No.62572407) , Fujian Province Special Science and Technology Program (No.2025H0041).

## References

- \[1\]J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al. (2023)Gpt-4 technical report.
arXiv preprint arXiv:2303.08774.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 2](https://arxiv.org/html/2603.22911v2#S4.T2.7.1.3.1.1.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[2\]S. R. Alvar, G. Singh, M. Akbari, and Y. Zhang (2025)Divprune: diversity-based visual token pruning for large multimodal models.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 9392–9401.
Cited by: [§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[3\]S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, et al. (2025)Qwen2. 5-vl technical report.
arXiv preprint arXiv:2502.13923.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 2](https://arxiv.org/html/2603.22911v2#S4.T2.7.1.4.1.1.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[4\]D. Bolya, C. Fu, X. Dai, P. Zhang, C. Feichtenhofer, and J. Hoffman (2022)Token merging: your vit but faster.
arXiv preprint arXiv:2210.09461.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§3.2](https://arxiv.org/html/2603.22911v2#S3.SS2.p1.1 "3.2 Spatial-Temporal Forest Construction ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[5\]W. Chai, E. Song, Y. Du, C. Meng, V. Madhavan, O. Bar-Tal, J. Hwang, S. Xie, and C. D. Manning (2024)Auroracap: efficient, performant video detailed captioning and a new benchmark.
arXiv preprint arXiv:2410.03051.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[6\]L. Chen, H. Zhao, T. Liu, S. Bai, J. Lin, C. Zhou, and B. Chang (2024)An image is worth 1/2 tokens after layer 2: plug-and-play inference acceleration for large vision-language models.
In European Conference on Computer Vision,
pp. 19–35.
Cited by: [Figure 1](https://arxiv.org/html/2603.22911v2#S0.F1 "In ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Figure 1](https://arxiv.org/html/2603.22911v2#S0.F1.5 "In ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.1](https://arxiv.org/html/2603.22911v2#S4.SS1.p1.1 "4.1 Implement Detail ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.10.2 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.16.2 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.23.2 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.29.2 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.35.2 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.4.2 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[7\]Z. Chen, W. Wang, Y. Cao, Y. Liu, Z. Gao, E. Cui, J. Zhu, S. Ye, H. Tian, Z. Liu, et al. (2024)Expanding performance boundaries of open-source multimodal models with model, data, and test-time scaling.
arXiv preprint arXiv:2412.05271.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[8\]Z. Chen, W. Wang, H. Tian, S. Ye, Z. Gao, E. Cui, W. Tong, K. Hu, J. Luo, Z. Ma, J. Ma, J. Wang, X. Dong, H. Yan, H. Guo, C. He, B. Shi, Z. Jin, C. Xu, B. Wang, X. Wei, W. Li, W. Zhang, B. Zhang, P. Cai, L. Wen, X. Yan, M. Dou, L. Lu, X. Zhu, T. Lu, D. Lin, Y. Qiao, J. Dai, and W. Wang (2024)How far are we to gpt-4v? closing the gap to commercial multimodal models with open-source suites.
arXiv Preprint.
Note: [https://arxiv.org/abs/2404.16821](https://arxiv.org/abs/2404.16821 "")Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[9\]Z. Cheng, S. Leng, H. Zhang, Y. Xin, X. Li, G. Chen, Y. Zhu, W. Zhang, Z. Luo, D. Zhao, and L. Bing (2024)VideoLLaMA 2: advancing spatial-temporal modeling and audio understanding in video-llms.
arXiv preprint arXiv:2406.07476.
External Links: [Link](https://arxiv.org/abs/2406.07476 "")Cited by: [§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[10\]W. Dai, J. Li, D. Li, A. M. H. Tiong, J. Zhao, W. Wang, B. Li, P. Fung, and S. Hoi (2023)InstructBLIP: towards general-purpose vision-language models with instruction tuning.
External Links: 2305.06500,
[Link](https://arxiv.org/abs/2305.06500 "")Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[11\]M. Dhouib, D. Buscaldi, S. Vanier, and A. Shabou (2025)Pact: pruning and clustering-based token reduction for faster visual language models.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 14582–14592.
Cited by: [§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[12\]C. Fu, Y. Dai, Y. Luo, L. Li, S. Ren, R. Zhang, Z. Wang, C. Zhou, Y. Shen, M. Zhang, et al. (2025)Video-mme: the first-ever comprehensive evaluation benchmark of multi-modal llms in video analysis.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 24108–24118.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p3.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p5.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.2](https://arxiv.org/html/2603.22911v2#S4.SS2.p1.1 "4.2 Benchmarks and Metrics ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[13\]T. Fu, T. Liu, Q. Han, G. Dai, S. Yan, H. Yang, X. Ning, and Y. Wang (2024)Framefusion: combining similarity and importance for video token reduction on large visual language models.
arXiv preprint arXiv:2501.01986.
Cited by: [Figure 1](https://arxiv.org/html/2603.22911v2#S0.F1 "In ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Figure 1](https://arxiv.org/html/2603.22911v2#S0.F1.5 "In ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p5.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.1](https://arxiv.org/html/2603.22911v2#S4.SS1.p1.1 "4.1 Implement Detail ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.14.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.20.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.27.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.33.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.39.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.8.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[14\]GLM-V Team (2025)GLM-4.5v and GLM-4.1v-thinking: towards versatile multimodal reasoning with scalable reinforcement learning.
arXiv preprint arXiv:2507.01006.
Note: v5, 15 Aug 2025. Zhipu AI & Tsinghua UniversityExternal Links: 2507.01006,
[Link](https://arxiv.org/abs/2507.01006 "")Cited by: [Table 2](https://arxiv.org/html/2603.22911v2#S4.T2.7.1.6.1.1.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[15\]Y. Goyal, T. Khot, D. Summers-Stay, D. Batra, and D. Parikh (2017)Making the v in vqa matter: elevating the role of image understanding in visual question answering.
In Proceedings of the IEEE conference on computer vision and pattern recognition,
pp. 6904–6913.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p3.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[16\]X. Huang, H. Zhou, and K. Han (2025)Prunevid: visual token pruning for efficient video large language models.
In Findings of the Association for Computational Linguistics: ACL 2025,
pp. 19959–19973.
Cited by: [§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[17\]D. A. Hudson and C. D. Manning (2019)Gqa: a new dataset for real-world visual reasoning and compositional question answering.
In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition,
pp. 6700–6709.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p3.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[18\]J. Hyun, S. Hwang, S. H. Han, T. Kim, I. Lee, D. Wee, J. Lee, S. J. Kim, and M. Shim (2025)Multi-granular spatio-temporal token merging for training-free acceleration of video llms.
In Proceedings of the IEEE/CVF International Conference on Computer Vision,
pp. 23990–24000.
Cited by: [§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.1](https://arxiv.org/html/2603.22911v2#S4.SS1.p1.1 "4.1 Implement Detail ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.13.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.19.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.26.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.32.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.38.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.7.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[19\]H. Jiang, I. Misra, M. Rohrbach, E. Learned-Miller, and X. Chen (2020)In defense of grid features for visual question answering.
In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition,
pp. 10267–10276.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[20\]Y. Jiang, Q. Wu, W. Lin, W. Yu, and Y. Zhou (2025)What kind of visual tokens do we need? training-free visual token pruning for multi-modal large language models from the perspective of graph.
In Proceedings of the AAAI Conference on Artificial Intelligence,
Vol. 39, pp. 4075–4083.
Cited by: [Figure 1](https://arxiv.org/html/2603.22911v2#S0.F1 "In ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Figure 1](https://arxiv.org/html/2603.22911v2#S0.F1.5 "In ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Figure 2](https://arxiv.org/html/2603.22911v2#S1.F2 "In 1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Figure 2](https://arxiv.org/html/2603.22911v2#S1.F2.4 "In 1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p3.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§3.1](https://arxiv.org/html/2603.22911v2#S3.SS1.p3.2 "3.1 Overview ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§3.1](https://arxiv.org/html/2603.22911v2#S3.SS1.p4.1 "3.1 Overview ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§3.1](https://arxiv.org/html/2603.22911v2#S3.SS1.p5.1 "3.1 Overview ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.1](https://arxiv.org/html/2603.22911v2#S4.SS1.p1.1 "4.1 Implement Detail ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.12.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.18.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.25.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.31.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.37.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.6.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[21\]Z. Kong, Y. Li, F. Zeng, L. Xin, S. Messica, X. Lin, P. Zhao, M. Kellis, H. Tang, and M. Zitnik (2026)Token reduction should go beyond efficiency in generative models – from vision, language to multimodality.
External Links: 2505.18227,
[Link](https://arxiv.org/abs/2505.18227 "")Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[22\]B. Li, Y. Zhang, D. Guo, R. Zhang, F. Li, H. Zhang, K. Zhang, P. Zhang, Y. Li, Z. Liu, et al. (2024)Llava-onevision: easy visual task transfer.
arXiv preprint arXiv:2408.03326.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p5.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.1](https://arxiv.org/html/2603.22911v2#S4.SS1.p1.1 "4.1 Implement Detail ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[23\]J. Li, D. Li, S. Savarese, and S. C. H. Hoi (2023)BLIP-2: bootstrapping language-image pre-training with frozen image encoders and large language models.
In ICML,
Proceedings of Machine Learning Research, Vol. 202, pp. 19730–19742.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[24\]J. Li, D. Li, S. Savarese, and S. Hoi (2023)Blip-2: bootstrapping language-image pre-training with frozen image encoders and large language models.
In International conference on machine learning,
pp. 19730–19742.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[25\]K. Li, Y. He, Y. Wang, Y. Li, W. Wang, P. Luo, Y. Wang, L. Wang, and Y. Qiao (2023)VideoChat: chat-centric video understanding.
arXiv Preprint.
Note: [https://arxiv.org/abs/2305.06355](https://arxiv.org/abs/2305.06355 "")Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[26\]K. Li, Y. Wang, Y. He, Y. Li, Y. Wang, Y. Liu, Z. Wang, J. Xu, G. Chen, P. Luo, et al. (2024)Mvbench: a comprehensive multi-modal video understanding benchmark.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 22195–22206.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p5.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.2](https://arxiv.org/html/2603.22911v2#S4.SS2.p1.1 "4.2 Benchmarks and Metrics ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[27\]Y. Li, C. Wang, and J. Jia (2024)Llama-vid: an image is worth 2 tokens in large language models.
In European Conference on Computer Vision,
pp. 323–340.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[28\]J. Liang, X. Meng, Y. Wang, C. Liu, Q. Liu, and D. Zhao (2024)End-to-end video question answering with frame scoring mechanisms and adaptive sampling.
arXiv Preprint.
Note: [https://arxiv.org/abs/2407.15047](https://arxiv.org/abs/2407.15047 "")Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[29\]B. Lin, B. Zhu, Y. Ye, M. Ning, P. Jin, and L. Yuan (2023)Video-llava: learning united visual representation by alignment before projection.
arXiv preprint arXiv:2311.10122.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[30\]H. Liu, C. Li, Y. Li, and Y. J. Lee (2024)Improved baselines with visual instruction tuning.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 26296–26306.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[31\]H. Liu, C. Li, Y. Li, B. Li, Y. Zhang, S. Shen, and Y. J. Lee (2024)Llava-next: improved reasoning, ocr, and world knowledge.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[32\]H. Liu, C. Li, Q. Wu, and Y. J. Lee (2024)Visual instruction tuning.
Advances in neural information processing systems36.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[33\]Y. Liu, H. Duan, Y. Zhang, B. Li, S. Zhang, W. Zhao, Y. Yuan, J. Wang, C. He, Z. Liu, et al. (2024)Mmbench: is your multi-modal model an all-around player?.
In European conference on computer vision,
pp. 216–233.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p3.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[34\]Z. Liu, L. Zhu, B. Shi, Z. Zhang, Y. Lou, S. Yang, H. Xi, S. Cao, Y. Gu, D. Li, et al. (2025)Nvila: efficient frontier visual language models.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 4122–4134.
Cited by: [§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[35\]G. Luo, Y. Zhou, M. Huang, T. Ren, X. Sun, and R. Ji (2024)MoIL: momentum imitation learning for efficient vision-language adaptation.
IEEE Transactions on Pattern Analysis and Machine Intelligence.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[36\]G. Luo, Y. Zhou, X. Sun, Y. Wang, L. Cao, Y. Wu, F. Huang, and R. Ji (2022)Towards lightweight transformer via group-wise transformation for vision-and-language tasks.
IEEE Transactions on Image Processing31, pp. 3386–3398.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[37\]G. Luo, Y. Zhou, X. Sun, Y. Wu, Y. Gao, and R. Ji (2024)Towards language-guided visual recognition via dynamic convolutions.
International Journal of Computer Vision132 (1), pp. 1–19.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[38\]G. Luo, Y. Zhou, Y. Zhang, X. Zheng, X. Sun, and R. Ji (2024)Feast your eyes: mixture-of-resolution adaptation for multimodal large language models.
arXiv preprint arXiv:2403.03003.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[39\]M. Maaz, H. A. Rasheed, S. Khan, and F. Khan (2024)Video-chatgpt: towards detailed video understanding via large vision and language models.
In ACL,
pp. 12585–12602.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[40\]Y. Man, Y. Huang, C. Zhang, B. Li, W. Niu, and M. Yin (2025)AdaCMˆ 2: on understanding extremely long-term video with adaptive cross-modality memory reduction.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 8534–8544.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[41\]OpenAI (2024)GPT-4O.
Note: [https://openai.com/index/hello-gpt-4o/](https://openai.com/index/hello-gpt-4o/ "")Cited by: [§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[42\]F. Radenovic, A. Dubey, A. Kadian, T. Mihaylov, S. Vandenhende, Y. Patel, Y. Wen, V. Ramanathan, and D. Mahajan (2023)Filtering, distillation, and hard negatives for vision-language pre-training.
In CVPR,
pp. 6967–6977.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[43\]A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, G. Krueger, and I. Sutskever (2021)Learning transferable visual models from natural language supervision.
External Links: 2103.00020,
[Link](https://arxiv.org/abs/2103.00020 "")Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[44\]Y. Shang, M. Cai, B. Xu, Y. J. Lee, and Y. Yan (2025)Llava-prumerge: adaptive token reduction for efficient large multimodal models.
In Proceedings of the IEEE/CVF International Conference on Computer Vision,
pp. 22857–22867.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[45\]K. Shao, K. Tao, C. Qin, H. You, Y. Sui, and H. Wang (2025)HoliTom: holistic token merging for fast video large language models.
arXiv preprint arXiv:2505.21334.
Cited by: [§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[46\]K. Tao, C. Qin, H. You, Y. Sui, and H. Wang (2025)DyCoke: dynamic compression of tokens for fast video large language models.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 18992–19001.
Cited by: [§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[47\]Q. Team (2025)Qwen3 technical report.
External Links: 2505.09388,
[Link](https://arxiv.org/abs/2505.09388 "")Cited by: [Table 2](https://arxiv.org/html/2603.22911v2#S4.T2.7.1.5.1.1.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[48\]H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale, et al. (2023)Llama 2: open foundation and fine-tuned chat models.
arXiv preprint arXiv:2307.09288.
Cited by: [§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[49\]P. Wang, S. Bai, S. Tan, S. Wang, Z. Fan, J. Bai, K. Chen, X. Liu, J. Wang, W. Ge, Y. Fan, K. Dang, M. Du, X. Ren, R. Men, D. Liu, C. Zhou, J. Zhou, and J. Lin (2024)Qwen2-vl: enhancing vision-language model’s perception of the world at any resolution.
arXiv Preprint.
Note: [https://arxiv.org/abs/2409.12191](https://arxiv.org/abs/2409.12191 "")Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[50\]W. Wang, Z. Gao, L. Gu, H. Pu, L. Cui, X. Wei, Z. Liu, L. Jing, S. Ye, J. Shao, et al. (2025)Internvl3.5: advancing open-source multimodal models in versatility, reasoning, and efficiency.
arXiv preprint arXiv:2508.18265.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.3](https://arxiv.org/html/2603.22911v2#S4.SS3.p2.1 "4.3 Quantitative Analysis ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 2](https://arxiv.org/html/2603.22911v2#S4.T2.7.1.8.1.1.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[51\]Y. Weng, M. Han, H. He, X. Chang, and B. Zhuang (2024)Longvlm: efficient long video understanding via large language models.
In European Conference on Computer Vision,
pp. 453–470.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[52\]H. Wu, D. Li, B. Chen, and J. Li (2024)LongVideoBench: A benchmark for long-context interleaved video-language understanding.
arXiv Preprint.
Note: [https://arxiv.org/abs/2407.15754](https://arxiv.org/abs/2407.15754 "")Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p5.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.2](https://arxiv.org/html/2603.22911v2#S4.SS2.p1.1 "4.2 Benchmarks and Metrics ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[53\]Q. Wu, Z. Ke, Y. Zhou, X. Sun, and R. Ji (2025)Routing experts: learning to route dynamic experts in existing multi-modal large language models.
In The Thirteenth International Conference on Learning Representations,
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[54\]Q. Wu, W. Lin, Y. Zhou, W. Ye, Z. Zen, X. Sun, and R. Ji (2024)Accelerating multimodal large language models via dynamic visual-token exit and the empirical findings.
arXiv preprint arXiv:2411.19628.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[55\]Q. Wu, Y. Zhou, W. Ye, X. Sun, and R. Ji (2026)Not all attention is needed: parameter and computation efficient tuning for multi-modal large language models via effective attention skipping.
International Journal of Computer Vision134 (3), pp. 128.
Cited by: [§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[56\]J. Xiao, X. Shang, A. Yao, and T. Chua (2021)NExT-qa: next phase of question-answering to explaining temporal actions.
In CVPR,
pp. 9777–9786.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p5.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.2](https://arxiv.org/html/2603.22911v2#S4.SS2.p1.1 "4.2 Benchmarks and Metrics ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[57\]L. Xing, Q. Huang, X. Dong, J. Lu, P. Zhang, Y. Zang, Y. Cao, C. He, J. Wang, F. Wu, et al. (2024)Pyramiddrop: accelerating your large vision-language models via pyramid visual redundancy reduction.
arXiv preprint arXiv:2410.17247.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[58\]C. Yang, Y. Sui, J. Xiao, L. Huang, Y. Gong, C. Li, J. Yan, Y. Bai, P. Sadayappan, X. Hu, et al. (2025)Topv: compatible token pruning with inference time optimization for fast and low-memory multimodal vision language model.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 19803–19813.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[59\]C. Yang, X. Dong, X. Zhu, W. Su, J. Wang, H. Tian, Z. Chen, W. Wang, L. Lu, and J. Dai (2025)PVC: progressive visual token compression for unified image and video processing in large vision-language models.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 24939–24949.
Cited by: [§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[60\]S. Yang, Y. Chen, Z. Tian, C. Wang, J. Li, B. Yu, and J. Jia (2025)Visionzip: longer is better but not necessary in vision language models.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 19792–19802.
Cited by: [Figure 1](https://arxiv.org/html/2603.22911v2#S0.F1 "In ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Figure 1](https://arxiv.org/html/2603.22911v2#S0.F1.5 "In ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p3.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§3.1](https://arxiv.org/html/2603.22911v2#S3.SS1.p3.2 "3.1 Overview ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§3.1](https://arxiv.org/html/2603.22911v2#S3.SS1.p4.1 "3.1 Overview ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§3.1](https://arxiv.org/html/2603.22911v2#S3.SS1.p5.1 "3.1 Overview ‣ 3 Method ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.1](https://arxiv.org/html/2603.22911v2#S4.SS1.p1.1 "4.1 Implement Detail ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.11.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.17.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.24.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.30.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.36.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 1](https://arxiv.org/html/2603.22911v2#S4.T1.11.1.5.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[61\]W. Ye, Q. Wu, W. Lin, and Y. Zhou (2024)Fit and prune: fast and training-free visual token pruning for multi-modal large language models.
arXiv preprint arXiv:2409.10197.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[62\]X. Ye, Y. Gan, Y. Ge, X. Zhang, and Y. Tang (2025)Atp-llava: adaptive token pruning for large vision language models.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 24972–24982.
Cited by: [§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[63\]H. Zhang, X. Li, and L. Bing (2023)Video-llama: an instruction-tuned audio-visual language model for video understanding.
In EMNLP,
pp. 543–553.
Cited by: [§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[64\]Y. Zhang, C. Fan, J. Ma, W. Zheng, T. Huang, K. Cheng, D. Gudovskiy, T. Okuno, Y. Nakata, K. Keutzer, et al. (2024)Sparsevlm: visual token sparsification for efficient vision-language model inference.
arXiv preprint arXiv:2410.04417.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[65\]Y. Zhang, B. Li, h. Liu, Y. j. Lee, L. Gui, D. Fu, J. Feng, Z. Liu, and C. Li (2024)LLaVA-next: a strong zero-shot video understanding model.
External Links: [Link](https://llava-vl.github.io/blog/2024-04-30-llava-next-video/ "")Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[66\]Y. Zhang, J. Wu, W. Li, B. Li, Z. Ma, Z. Liu, and C. Li (2024)Video instruction tuning with synthetic data.
arXiv preprint arXiv:2410.02713.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p1.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§1](https://arxiv.org/html/2603.22911v2#S1.p5.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.1](https://arxiv.org/html/2603.22911v2#S2.SS1.p1.1 "2.1 Video LLMs ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.1](https://arxiv.org/html/2603.22911v2#S4.SS1.p1.1 "4.1 Implement Detail ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 2](https://arxiv.org/html/2603.22911v2#S4.T2.7.1.9.1.1.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[67\]S. Zhao, Z. Wang, F. Juefei-Xu, X. Xia, M. Liu, X. Wang, M. Liang, N. Zhang, D. N. Metaxas, and L. Yu (2025)Accelerating multimodal large language models by searching optimal vision token reduction.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 29869–29879.
Cited by: [§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[68\]J. Zhou, Y. Shu, B. Zhao, B. Wu, S. Xiao, X. Yang, Y. Xiong, B. Zhang, T. Huang, and Z. Liu (2024)MLVU: A comprehensive benchmark for multi-task long video understanding.
arXiv Preprint.
Note: [https://arxiv.org/abs/2406.04264](https://arxiv.org/abs/2406.04264 "")Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p5.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§4.2](https://arxiv.org/html/2603.22911v2#S4.SS2.p1.1 "4.2 Benchmarks and Metrics ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[69\]Y. Zhou, R. Ji, X. Sun, J. Su, D. Meng, Y. Gao, and C. Shen (2019)Plenty is plague: fine-grained learning for visual question answering.
IEEE transactions on pattern analysis and machine intelligence44 (2), pp. 697–709.
Cited by: [§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[70\]J. Zhu, W. Wang, Z. Chen, Z. Liu, S. Ye, L. Gu, H. Tian, Y. Duan, W. Su, J. Shao, et al. (2025)Internvl3: exploring advanced training and test-time recipes for open-source multimodal models.
arXiv preprint arXiv:2504.10479.
Cited by: [§4.3](https://arxiv.org/html/2603.22911v2#S4.SS3.p2.1 "4.3 Quantitative Analysis ‣ 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[Table 2](https://arxiv.org/html/2603.22911v2#S4.T2.7.1.7.1.1.1 "In 4 Experiments ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").

- \[71\]X. Zou, D. Lu, Y. Wang, Y. Yan, Y. Lyu, X. Zheng, L. Zhang, and X. Hu (2025)Don’t just chase” highlighted tokens” in mllms: revisiting visual holistic context retention.
arXiv preprint arXiv:2510.02912.
Cited by: [§1](https://arxiv.org/html/2603.22911v2#S1.p2.1 "1 Introduction ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling"),
[§2.2](https://arxiv.org/html/2603.22911v2#S2.SS2.p1.1 "2.2 Visual Token Compression Methods ‣ 2 Related Work ‣ ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling").