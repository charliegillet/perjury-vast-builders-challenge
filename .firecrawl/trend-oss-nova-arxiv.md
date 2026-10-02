Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2609.06360v1 \[cs.CV\] 06 Sep 2026

# NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection

Wei-Chih Yin
Yun-Ching Kao
Cheng-Kuan Lin
Yu-Chee Tseng
Affiliation: Department of Computer Science, National Yang Ming Chiao Tung University, Hsinchu, Taiwan
Affiliation: eric123602@gmail.com, yunching.cs14@nycu.edu.tw, cklin@cs.nycu.edu.tw, yctseng@cs.nycu.edu.tw

###### Abstract

Training-free zero-shot video anomaly detection (ZS-VAD) leverages vision-language models (VLMs) to localize anomaly instances from a predefined anomaly vocabulary, without providing any video.
Existing CLIP-based methods often emphasize anomaly-side semantics, while the competing normality side remains less carefully formulated. We identify two key limitations in existing solutions: (i) blurred decision boundary: normal prompts may contain ambiguous verbs, such as “running”, that are semantically close to anomalies, reducing normal and abnormal separation in the VLM embedding space; and (ii) modality gap: poor alignment between features of textual normal anchors and visual frames.
We propose NOVA, a training-free ZS-VAD framework that strengthens the normal side at both linguistic and visual levels. NOVA introduces Normality-Aware Prompt Construction (NA), which excludes anomaly-adjacent verbs and biases normal descriptions toward static, low-motion scenes. To overcome the text-vision modality gap, NOVA constructs a Visual Normality Anchor (VNA) , which creates a weighted visual normal anchor from the initial frames of each test video, providing a video-specific normal reference without task-specific training or annotations.
NOVA achieves 89.86% AUC on UCF-Crime and 95.07% AUC and 84.82% AP on XD-Violence, reaching state-of-the-art performance among comparable training-free zero-shot methods.

## 1 Introduction

Video Anomaly Detection (VAD) is essential in intelligent surveillance, aiming to localize rare and semantically diverse abnormal events, such as fighting, robbery, arson, and explosions, from long and untrimmed surveillance videos. Supervised and weakly supervised methods\[ [20](https://arxiv.org/html/2609.06360v1#bib.bib1 ""), [23](https://arxiv.org/html/2609.06360v1#bib.bib34 ""), [6](https://arxiv.org/html/2609.06360v1#bib.bib15 ""), [26](https://arxiv.org/html/2609.06360v1#bib.bib20 "")\] have achieved substantial progress in closed-set settings, but they rely on collecting and annotating anomalous samples from the target domain. This requirement is inherently restrictive: anomalies are rare, open-ended, and difficult to enumerate, making such methods less reliable when deployed in new scenes.

Vision-language models (VLMs), such as CLIP \[ [16](https://arxiv.org/html/2609.06360v1#bib.bib3 "")\], offer a natural basis for zero-shot VAD (ZS-VAD) by aligning visual frames and textual descriptions in a shared embedding space. By comparing frame-level visual embeddings against competing abnormal and normal text prompts, ZS-VAD can score anomalies that were never used for task-specific training. Recent methods enrich textual representations with LLM-generated descriptions, either as category-level prompts or as an offline pseudo-scene memory \[ [4](https://arxiv.org/html/2609.06360v1#bib.bib33 ""), [7](https://arxiv.org/html/2609.06360v1#bib.bib6 "")\].

Despite these advances, existing CLIP-based ZS-VAD methods often place greater emphasis on enriching anomaly-side semantics. However, anomalies are inherently open-ended and difficult to describe exhaustively. In prompt-contrastive ZS-VAD, anomaly scores are determined by the competition between anomaly and normal prompts rather than anomaly prompts alone. As a result, the normal side is not merely a background reference but directly shapes the decision boundary.
Nevertheless, normality semantics remains underexplored in existing training-free ZS-VAD methods. Normal prompts are often represented by generic descriptions, despite normal events being more constrained by scene layout, object configuration, and video-specific appearance. This mismatch motivates us to revisit the role of the normal side in training-free ZS-VAD.

We identify two key limitations of current training-free ZS-VAD frameworks from the perspective of normal-side modeling.
The first limitation is the blurred decision boundary in LLM-generated normal descriptions. Although existing methods distinguish normal and abnormal prompts using separate templates or embedding-level repulsion, semantically ambiguous verbs may still appear in normal descriptions. For example, actions such as “running” or “chasing” may describe normal activities in some contexts, yet they are also associated with violent or suspicious events. Consequently, the semantic distinction between normal and abnormal prompts becomes less clear.
The second limitation is the inherent modality gap between textual and visual embeddings, which persists even with well-designed normal prompts \[ [10](https://arxiv.org/html/2609.06360v1#bib.bib10 ""), [19](https://arxiv.org/html/2609.06360v1#bib.bib11 "")\]. A textual normal anchor does not necessarily lie closer to normal video frames than an abnormal textual description does. Furthermore, a fixed prompt bank shared across all videos cannot account for the appearance differences among individual videos. This discrepancy originates from the gap between textual and visual representations, rather than prompt wording alone.

To address these limitations, we propose NOVA (NOrmal-side Modeling for ZS-VAD), a training-free framework that explicitly models the normal side from both linguistic and visual perspectives.
On the language side, NOVA introduces Normality-Aware Prompt Construction (NA), which refines LLM-generated normal descriptions to improve the semantic distinction between normal and abnormal prompts.
On the visual side, NOVA introduces the Visual Normality Anchor (VNA), a per-test-video normal reference constructed directly in the visual embedding space. By estimating the normal reference from the test video itself, VNA alleviates the discrepancy between textual normal descriptions and visual representations while adapting to each video.
In addition, NOVA incorporates a lightweight temporal module, Motion-Aware Stabilization (MAS), to improve frame-level temporal stability. The resulting framework remains fully training-free, using a frozen vision-language encoder, a pre-constructed prompt bank, and test-time visual anchors.

Our contributions are fourfold. First, we propose NOVA, a training-free framework for zero-shot video anomaly detection that explicitly treats normality through complementary linguistic and visual modeling.
Second, NOVA introduces Normality-Aware Prompt Construction (NA) to reduce semantic ambiguity in normal descriptions and the Visual Normality Anchor (VNA) to construct a per-video visual normal reference directly from the test video, and further incorporates a lightweight Motion-Aware Stabilization (MAS) module for temporal refinement.
Third, through controlled ablation studies and embedding-space analyses, we demonstrate the importance of explicit normal-side modeling in training-free ZS-VAD and provide empirical evidence for the effectiveness of the proposed design.
Finally, in a zero-shot setting, NOVA achieves state-of-the-art performance among comparable training-free ZS-VAD methods, reaching 95.07% AUC on XD-Violence and 89.86% AUC on UCF-Crime.

## 2 Related Work

### 2.1 Video Anomaly Detection

VAD aims to localize rare abnormal events in long, untrimmed videos.
Existing VAD methods rely on frame-level annotations, video-level labels,
or unlabeled target-domain videos to learn anomaly or normality
representations \[ [17](https://arxiv.org/html/2609.06360v1#bib.bib32 ""), [20](https://arxiv.org/html/2609.06360v1#bib.bib1 ""), [23](https://arxiv.org/html/2609.06360v1#bib.bib34 ""), [6](https://arxiv.org/html/2609.06360v1#bib.bib15 ""), [26](https://arxiv.org/html/2609.06360v1#bib.bib20 ""), [30](https://arxiv.org/html/2609.06360v1#bib.bib24 "")\].
Despite their success, these approaches require task-specific data and learn dataset-specific notions of normality and abnormality.
Recent open-vocabulary methods \[ [8](https://arxiv.org/html/2609.06360v1#bib.bib35 ""), [11](https://arxiv.org/html/2609.06360v1#bib.bib36 "")\] relax the closed-set assumption but still require task-specific training or adaptation.

### 2.2 Zero-Shot Video Anomaly Detection

Training-free ZS-VAD aims to detect previously unseen anomalies at inference time using frozen VLMs or MLLMs without collecting target-domain training data \[ [31](https://arxiv.org/html/2609.06360v1#bib.bib5 ""), [7](https://arxiv.org/html/2609.06360v1#bib.bib6 ""), [36](https://arxiv.org/html/2609.06360v1#bib.bib8 ""), [18](https://arxiv.org/html/2609.06360v1#bib.bib30 ""), [1](https://arxiv.org/html/2609.06360v1#bib.bib29 "")\]. Existing methods can be categorized into prompt-contrastive and reasoning-based approaches.
Prompt-contrastive methods estimate anomaly scores by comparing visual representations against competing normal and abnormal textual descriptions.
For image anomaly detection, WinCLIP \[ [5](https://arxiv.org/html/2609.06360v1#bib.bib4 "")\] compares image embeddings with handcrafted normal and abnormal prompts for zero-shot anomaly classification and localization. It was later adopted for video anomaly detection. VadCLIP \[ [26](https://arxiv.org/html/2609.06360v1#bib.bib20 "")\] aligns textual event categories with video representations under weak supervision, while \[ [4](https://arxiv.org/html/2609.06360v1#bib.bib33 "")\] introduces LLM-generated normal and abnormal descriptions but still trains learnable prompts and temporal modules. Flashback \[ [7](https://arxiv.org/html/2609.06360v1#bib.bib6 "")\] removes task-specific training by constructing an offline pseudo-scene memory while preserving normal–abnormal prompt competition during inference. NOVA follows this prompt-contrastive formulation but differs in its treatment of normality: unlike prior approaches whose normal references remain text-derived, NOVA explicitly disambiguates normal descriptions and constructs a per-video visual normality anchor directly from the test video.

Reasoning-based training-free methods instead use frozen VLMs or MLLMs to infer anomaly scores directly. LAVAD \[ [31](https://arxiv.org/html/2609.06360v1#bib.bib5 "")\] converts VLM-generated scene descriptions into anomaly scores through LLM reasoning, while Cerberus \[ [33](https://arxiv.org/html/2609.06360v1#bib.bib7 "")\], VADTree \[ [9](https://arxiv.org/html/2609.06360v1#bib.bib17 "")\], ASK-Hint \[ [36](https://arxiv.org/html/2609.06360v1#bib.bib8 "")\], AnyAnomaly \[ [1](https://arxiv.org/html/2609.06360v1#bib.bib29 "")\], EventVAD \[ [18](https://arxiv.org/html/2609.06360v1#bib.bib30 "")\], and PANDA \[ [28](https://arxiv.org/html/2609.06360v1#bib.bib31 "")\] explore rule-based or hierarchical reasoning, structured prompting, and multimodal inference.
LAVIDA \[ [3](https://arxiv.org/html/2609.06360v1#bib.bib9 "")\] also uses an MLLM, but trains on pseudo-anomalies synthesized from external segmentation data and therefore falls outside the strictly training-free setting. Compared with these direct-reasoning approaches, NOVA retains a lightweight prompt-contrastive scorer and focuses on strengthening normal-side representations.

### 2.3 Normality Modeling

Normality plays a fundamental role in anomaly detection. In training-based VAD, normality is learned from target-domain videos. One-class VAD methods learn normality from normal-only videos and regard deviations from the learned normal patterns as anomalies \[ [24](https://arxiv.org/html/2609.06360v1#bib.bib23 "")\]. Weakly supervised VAD additionally uses video-level labels to learn normality and regularize anomaly scoring \[ [20](https://arxiv.org/html/2609.06360v1#bib.bib1 ""), [23](https://arxiv.org/html/2609.06360v1#bib.bib34 "")\].
In training-free ZS-VAD, normality is instead specified without collecting target-domain training videos, typically through textual prompts or text-only memories constructed before inference \[ [7](https://arxiv.org/html/2609.06360v1#bib.bib6 "")\]. Cerberus \[ [33](https://arxiv.org/html/2609.06360v1#bib.bib7 "")\] derives scene-specific normal behavioral rules from sample normal videos during an offline induction phase; it is thus data-adaptive rather than strictly target-data-free.
Consequently, effective normal representations must capture normality while remaining distinguishable from anomalies.
INP-Former \[ [12](https://arxiv.org/html/2609.06360v1#bib.bib12 "")\] extracts intrinsic normal prototypes directly from each test image, but requires training.
This suggests that test-instance-specific visual normality can complement text-based normal representations. NOVA similarly constructs a video-specific visual normality anchor from the test input, but requires neither normal training videos nor task-specific training.

### 2.4 Prompt Design and Modality Gap

Prompt design plays an important role in adapting vision-language models (VLMs) to downstream tasks. General prompt learning and prompt generation methods have shown that textual context can substantially influence visual recognition.
CoOp \[ [34](https://arxiv.org/html/2609.06360v1#bib.bib13 "")\] learns task-adaptive context vectors from labeled data, whereas CuPL \[ [15](https://arxiv.org/html/2609.06360v1#bib.bib16 "")\] leverages LLM-generated textual descriptions to improve zero-shot classification. In anomaly detection, prompt design is particularly important because anomaly scores are determined by the contrast between normal and abnormal descriptions rather than a single class label. Image anomaly detection methods such as WinCLIP \[ [5](https://arxiv.org/html/2609.06360v1#bib.bib4 "")\] and AnomalyCLIP \[ [35](https://arxiv.org/html/2609.06360v1#bib.bib14 "")\] represent normal and abnormal states through handcrafted or learned prompts, while video anomaly detection methods adopt related prompt-based representations for VAD \[ [4](https://arxiv.org/html/2609.06360v1#bib.bib33 ""), [7](https://arxiv.org/html/2609.06360v1#bib.bib6 "")\].

However, prompt engineering alone does not fully address the modality gap between textual and visual representations. Prior studies have shown that contrastive VLMs may embed text and image features into different regions of a shared feature space despite being trained for cross-modal alignment \[ [10](https://arxiv.org/html/2609.06360v1#bib.bib10 ""), [19](https://arxiv.org/html/2609.06360v1#bib.bib11 "")\]. For video anomaly detection, this implies that even semantically appropriate textual normal prompts need not lie close to normal video features in the shared embedding space. Consequently, a semantically reasonable prompt bank may still be suboptimal.

## 3 Method

### 3.1 Problem Definition and Framework

Let V={ft}t=1TV=\\{f\_{t}\\}\_{t=1}^{T} denote a test video with TT frames.
Given VV, a coarse footage descriptor dd (e.g., “surveillance video”),
and a predefined anomaly vocabulary 𝒞\\mathcal{C} (e.g.,
{“fighting”, “shooting”}), NOVA estimates frame-level anomaly
scores st∈\[0,1\]s\_{t}\\in\[0,1\], where higher values indicate a higher likelihood
of anomaly.
The descriptor dd and vocabulary 𝒞\\mathcal{C} are used to
construct the prompt bank before inference.
NOVA requires no task-specific training or target-domain adaptation,
and frame-level ground truth yt∈{0,1}y\_{t}\\in\\{0,1\\} remains unavailable
throughout.

As illustrated in Fig. [1](https://arxiv.org/html/2609.06360v1#S3.F1 "Figure 1 ‣ 3.1 Problem Definition and Framework ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"), NOVA comprises four
components: Normality-Aware Prompt Construction (NA)
constructs anomaly and disambiguated normal descriptions
(Sec. [3.2](https://arxiv.org/html/2609.06360v1#S3.SS2 "3.2 Normality-Aware Prompt Construction (NA) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection")); Prompt-Contrastive Anomaly Scoring
performs normal–abnormal competition using a frozen vision-language
encoder (Sec. [3.3](https://arxiv.org/html/2609.06360v1#S3.SS3 "3.3 Prompt-Contrastive Anomaly Scoring ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection")); Visual Normality Anchor (VNA)
introduces a per-video visual normal reference
(Sec. [3.4](https://arxiv.org/html/2609.06360v1#S3.SS4 "3.4 Visual Normality Anchor (VNA) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection")); and Motion-Aware Stabilization (MAS)
provides lightweight temporal refinement
(Sec. [3.5](https://arxiv.org/html/2609.06360v1#S3.SS5 "3.5 Motion-Aware Stabilization (MAS) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection")).
The entire framework is training-free and requires no parameter
optimization.

![Refer to caption](https://arxiv.org/html/2609.06360v1/pic/framework.png)Figure 1: The NOVA framework. NOVA uses a frozen vision-language encoder and a pre-constructed prompt bank, and constructs a video-specific visual normality anchor at test time. The framework comprises four key components: Normality-Aware Prompt Construction (NA), prompt-contrastive anomaly scoring, a per-video Visual Normality Anchor (VNA), and Motion-Aware Stabilization (MAS).

### 3.2 Normality-Aware Prompt Construction (NA)

All prompt banks are constructed using an LLM, but no LLM is invoked during inference.

For each anomaly category c∈𝒞c\\in\\mathcal{C}, our goal is to construct a category-conditioned prompt bank
ℬc={𝒫c={pic}i=1M,𝒩c={njc}j=1M}\\mathcal{B}\_{c}=\\left\\{\\mathcal{P}\_{c}=\\{p\_{i}^{c}\\}\_{i=1}^{M},\\mathcal{N}\_{c}=\\{n\_{j}^{c}\\}\_{j=1}^{M}\\right\\},
where 𝒫c\\mathcal{P}\_{c} contains anomaly-side descriptions, 𝒩c\\mathcal{N}\_{c} contains normal-side descriptions, and MM is their cardinality.
Each anomaly description pic∈𝒫cp\_{i}^{c}\\in\\mathcal{P}\_{c} is expected to cover a subject, an object, and an observable atomic event corresponding to cc.
Each normal description njc∈𝒩cn\_{j}^{c}\\in\\mathcal{N}\_{c}, in contrast, should provide safe, low-motion, and non-threatening counterexamples within the same context. A key requirement is that the normal side should not merely describe generic normality, but must avoid visually similar normal behaviors related to cc; otherwise, the normal descriptions may lie close to the anomaly side in the textual embedding space and weaken the subsequent competitive scoring.

For each category cc, the prompt bank ℬc\\mathcal{B}\_{c} is constructed in four steps. Step 4 is potentially repeated multiple times.

Step 1. Confusing verb mining.
Given cc and the footage descriptor dd, an LLM is invoked to mine a set of category-conditioned yet confusing normal actions,
𝒱c=LLMverb​(c,d)\\mathcal{V}\_{c}=\\mathrm{LLM}\_{\\mathrm{verb}}(c,d), where each element is a short phrase consisting of 1–3 words that describes a semantically normal action visually similar to cc. A single query asks the LLM for 5–8 such actions. For example, 𝒱fighting\\mathcal{V}\_{\\mathrm{fighting}} may include “sparring”, “play wrestling”, and “horseplay”.

Step 2. Calm-anchor generation.
Conditioned only on dd, an LLM is invoked to generate a fixed set of calm anchors,
𝒜=LLManchor​(d)={a1,…,aK}\\mathcal{A}=\\mathrm{LLM}\_{\\mathrm{anchor}}(d)=\\{a\_{1},\\dots,a\_{K}\\},
where each aka\_{k} is a low-motion, non-threatening baseline scene of the footage domain, such as “an empty corridor”. As 𝒜\\mathcal{A} does not depend on cc, it is generated once per prompt-bank run and shared across all categories, providing a stable normal reference for common background or establishing scenes in the footage domain.

Step 3. Prompt bank generation.
Using a single instruction, an LLM is invoked to produce the anomaly set and an initial normal set,
(𝒫c,𝒩c)=LLMgen​(c,𝒱c,𝒜,d)(\\mathcal{P}\_{c},\\mathcal{N}\_{c})=\\mathrm{LLM}\_{\\mathrm{gen}}(c,\\mathcal{V}\_{c},\\mathcal{A},d),
where \|𝒫c\|=\|𝒩c\|=M\|\\mathcal{P}\_{c}\|=\|\\mathcal{N}\_{c}\|=M. The anomaly set 𝒫c\\mathcal{P}\_{c} is produced once and fixed, whereas the normal set 𝒩c\\mathcal{N}\_{c} may be further revised in step 4.
Following typical anomaly-driven work, 𝒫c\\mathcal{P}\_{c} directly describes the category cc itself
(e.g., “Two people exchanging rapid punches to each other’s faces in a hallway” for category “fighting”).
Enforcing M>KM>K, 𝒩c\\mathcal{N}\_{c} consists of KK stable establishing-scene descriptions generated from the calm-anchor reference 𝒜\\mathcal{A} (e.g., “A quiet empty hallway under fluorescent lights with closed doors and no people”) and M−KM-K ordinary normal descriptions (e.g., “Two people talking calmly beside a doorway with relaxed posture”).
The generation instruction explicitly prohibits terms in the confusing set 𝒱c\\mathcal{V}\_{c} from appearing in the normal descriptions. This constraint prevents semantically ambiguous verbs, such as “sparring”, from appearing in normality descriptions.
Because the anchor set 𝒜\\mathcal{A} provides examples rather than verbatim templates, the anchor-derived descriptions differ across categories instead of repeating one fixed set of sentences.

Step 4. Geometry-gated refinement.
After step 3, some descriptions in the normal set 𝒩c\\mathcal{N}\_{c} may still lean toward the anomaly side in the textual embedding space. This step geometrically detects and rewrites such residual cases.
Assuming a pretrained text encoder ψ⁡(⋅)\\psi(\\cdot), we first compute the normalized centroid vector of the anomaly bank,

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝝁c+=Normalize⁡(1M​∑pic∈𝒫cψ⁡(T+,pic)).\\boldsymbol{\\mu}\_{c}^{+}=\\mathrm{Normalize}\\!\\left(\\frac{1}{M}\\sum\\nolimits\_{p\_{i}^{c}\\in\\mathcal{P}\_{c}}\\psi(T^{+},p\_{i}^{c})\\right). |  | (1) |

From the centroid, we compute the ambiguity score gjcg\_{j}^{c} of each normal description njc∈𝒩cn\_{j}^{c}\\in\\mathcal{N}\_{c} via cosine similarity,

|     |     |     |     |
| --- | --- | --- | --- |
|  | gjc=ψ​(T−,njc)⊤​𝝁c+,g\_{j}^{c}=\\psi(T^{-},n\_{j}^{c})^{\\top}\\boldsymbol{\\mu}\_{c}^{+}, |  | (2) |

where a higher value indicates that the normal description is closer to the anomaly side.
T+T^{+} and T−T^{-} are predefined text prefixes for embedding.
The goal of refinement is to rewrite description njcn\_{j}^{c} to remove potential ambiguity.
Specifically, njcn\_{j}^{c} is marked as an ambiguous normal if its gjc>θg\_{j}^{c}>\\theta, in which case we invoke an LLM for revision:
n^jc=LLMref​(njc,c)\\hat{n}\_{j}^{c}=\\mathrm{LLM}\_{\\mathrm{ref}}(n\_{j}^{c},c) and similarly evaluate its ambiguity score
g^jc\\hat{g}\_{j}^{c}.
The revision replaces njcn\_{j}^{c} with n^jc\\hat{n}\_{j}^{c} only if the ambiguity is reduced, i.e., g^jc<gjc\\hat{g}\_{j}^{c}<g\_{j}^{c}; otherwise the original njcn\_{j}^{c} is kept.
The above scoring, marking, and rewriting are then repeated over the current 𝒩c\\mathcal{N}\_{c}, until the ambiguity scores of all its descriptions drop below θ\\theta, until a round accepts no revision, or until a predefined number RR of rounds is reached. The resulting 𝒩c\\mathcal{N}\_{c}, together with 𝒫c\\mathcal{P}\_{c}, forms the prompt bank ℬc\\mathcal{B}\_{c}.
Values of T+T^{+}, T−T^{-}, θ\\theta, and RR are reported in Sec. [4.1](https://arxiv.org/html/2609.06360v1#S4.SS1 "4.1 Experimental Setup ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

The dataset-specific inputs include only the anomaly vocabulary 𝒞\\mathcal{C}, footage descriptor dd, and fixed domain-specific
role guidance and examples used for prompt generation.
These specifications are defined once per dataset and held fixed across categories, seeds, and prompt-generation runs.
For UCF-Crime, d=d= “surveillance footage”, whereas for XD-Violence, d=d= “movie or online video footage”.

### 3.3 Prompt-Contrastive Anomaly Scoring

Prompt-contrastive scoring adopts the Repulsive Prompting (RP) and Scaled Anomaly Penalization (SAP) principles of Flashback \[ [7](https://arxiv.org/html/2609.06360v1#bib.bib6 "")\], and applies them to category-conditioned competition between anomaly and normal prompts.
Based on the same text encoder ψ⁡(⋅)\\psi(\\cdot) and the prompt bank (𝒫c,𝒩c)(\\mathcal{P}\_{c},\\mathcal{N}\_{c}), we compute two L2-normalized textual embedding pools as
𝐞i+,c=ψ⁡(T+,pic)\\mathbf{e}\_{i}^{+,c}=\\psi(T^{+},p\_{i}^{c}) and 𝐞j−,c=ψ⁡(T−,njc)\\mathbf{e}\_{j}^{-,c}=\\psi(T^{-},n\_{j}^{c}),
where
pic∈𝒫cp\_{i}^{c}\\in\\mathcal{P}\_{c} and
njc∈𝒩cn\_{j}^{c}\\in\\mathcal{N}\_{c}.
Using the corresponding visual encoder ϕ⁡(⋅)\\phi(\\cdot) from the same frozen vision-language model, each frame is represented by the L2-normalized visual embedding
𝐱t=ϕ⁡(ft)\\mathbf{x}\_{t}=\\phi(f\_{t}).
The similarities between 𝐱t\\mathbf{x}\_{t} and the anomaly-side and normal-side embeddings are computed respectively as:

|     |     |     |     |
| --- | --- | --- | --- |
|  | ri+,c=𝐱t⊤​𝐞i+,c,rj−,c=𝐱t⊤​𝐞j−,c.r\_{i}^{+,c}=\\mathbf{x}\_{t}^{\\top}\\mathbf{e}\_{i}^{+,c},\\qquad r\_{j}^{-,c}=\\mathbf{x}\_{t}^{\\top}\\mathbf{e}\_{j}^{-,c}. |  | (3) |

To reduce the noise of individual prompts, we apply Top-50% mean aggregation to estimate the similarities of ftf\_{t} to both sides:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|  | ut+,c\\displaystyle u\_{t}^{+,c} | =TopKMean50%​({ri+,c}),\\displaystyle=\\mathrm{TopKMean}\_{50\\%}(\\{r\_{i}^{+,c}\\}), |  | (4) |
|  | ut−,c\\displaystyle u\_{t}^{-,c} | =TopKMean50%​({rj−,c}).\\displaystyle=\\mathrm{TopKMean}\_{50\\%}(\\{r\_{j}^{-,c}\\}). |  |

Following the SAP principle \[ [7](https://arxiv.org/html/2609.06360v1#bib.bib6 "")\], we compensate for the asymmetry between anomaly and normal prompts by down-weighting the anomaly similarity with a scaling factor α<1\\alpha<1.
The cc-conditioned anomaly score is computed by binary Softmax, written in the equivalent sigmoid form below:

|     |     |     |     |
| --- | --- | --- | --- |
|  | stc=sigmoid⁡(α​ut+,c−ut−,cτ).s\_{t}^{c}=\\operatorname{sigmoid}\\!\\left(\\frac{\\alpha u\_{t}^{+,c}-u\_{t}^{-,c}}{\\tau}\\right). |  | (5) |

The same α\\alpha and τ\\tau are used across all datasets without target-specific tuning. Their values are reported in Sec. [4.1](https://arxiv.org/html/2609.06360v1#S4.SS1 "4.1 Experimental Setup ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

The final frame-level anomaly score is obtained as st=maxc∈𝒞⁡stcs\_{t}=\\max\_{c\\in\\mathcal{C}}s\_{t}^{c}.
The scoring backbone above serves as the basis for the following two modules. VNA (Sec. [3.4](https://arxiv.org/html/2609.06360v1#S3.SS4 "3.4 Visual Normality Anchor (VNA) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection")) strengthens the normal-side representation, while MAS (Sec. [3.5](https://arxiv.org/html/2609.06360v1#S3.SS5 "3.5 Motion-Aware Stabilization (MAS) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection")) further improves temporal stability.

### 3.4 Visual Normality Anchor (VNA)

Textual normal prompts provide semantic guidance, but because they are fixed across videos, they cannot capture the scene-specific appearance of an individual video. Moreover, even semantically appropriate textual prompts may remain geometrically separated from visual frame embeddings because of the modality gap\[ [10](https://arxiv.org/html/2609.06360v1#bib.bib10 ""), [19](https://arxiv.org/html/2609.06360v1#bib.bib11 "")\]. To complement these textual references, VNA constructs a per-video visual normality anchor directly from the test video.

Warm-Up Normality Prior.
After temporal sampling, we use the first NwarmN\_{\\mathrm{warm}} sampled visual embeddings as a lightweight estimate of the video’s normal visual state without requiring annotations. When MAS is enabled, its windowed embedding aggregation is applied before temporal sampling and VNA estimation. Since the early-video assumption may not hold for every video, VNA incorporates a contamination-aware weighting scheme.

Anomalous Contamination Avoidance.
Directly averaging the warm-up embeddings is vulnerable to anomalous contamination: even a few anomalous embeddings can shift the visual prototype toward the anomaly side. To reduce this effect, we first compute a preliminary anomaly score s^t\\hat{s}\_{t} for each warm-up embedding using the scoring rule in Sec. [3.3](https://arxiv.org/html/2609.06360v1#S3.SS3 "3.3 Prompt-Contrastive Anomaly Scoring ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").
The resulting scores are normalized by:

|     |     |     |     |
| --- | --- | --- | --- |
|  | wt=exp(−s^t/γ)∑q=1Nwarmexp(−s^q/γ),w\_{t}=\\frac{\\exp(-\\hat{s}\_{t}/\\gamma)}{\\sum\_{q=1}^{N\_{\\mathrm{warm}}}\\exp(-\\hat{s}\_{q}/\\gamma)}, |  | (6) |

where γ\\gamma is the anchor temperature that controls how strongly the weights concentrate on the lowest-scoring frames.
The visual normality anchor is then estimated as

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝐚VNA=Normalize⁡(∑t=1Nwarmwt​𝐱t).\\mathbf{a}\_{\\mathrm{VNA}}=\\mathrm{Normalize}\\left(\\sum\\nolimits\_{t=1}^{N\_{\\mathrm{warm}}}w\_{t}\\mathbf{x}\_{t}\\right). |  | (7) |

During anomaly scoring, the normal embedding pool is extended from
{𝐞j−,c∣j=1,2,…,M}\\{\\mathbf{e}\_{j}^{-,c}\\mid j=1,2,\\ldots,M\\}
to
{𝐞j−,c∣j=1,2,…,M}∪{𝐚VNA}\\{\\mathbf{e}\_{j}^{-,c}\\mid j=1,2,\\ldots,M\\}\\cup\\{\\mathbf{a}\_{\\mathrm{VNA}}\\}.
The same visual anchor is shared across all anomaly categories, providing a video-specific normal reference in addition to the textual normal prompts.
We use the same NwarmN\_{\\mathrm{warm}} and anchor temperature γ\\gamma for both datasets (values reported in Sec. [4.1](https://arxiv.org/html/2609.06360v1#S4.SS1 "4.1 Experimental Setup ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection")).

### 3.5 Motion-Aware Stabilization (MAS)

Frame-level scoring is susceptible to fluctuations and may disrupt event continuity.
This module leverages motion information to stabilize the anomaly scores. It combines two ideas: windowed embedding and motion gate.

Windowed Embedding.
Given the visual embedding sequence
{𝐱t}t=1T\\{\\mathbf{x}\_{t}\\}\_{t=1}^{T}, we employ moving average with a sliding window of width WW (boundary cases omitted for simplicity of presentation),

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝐱~t=Normalize(1W∑k=−(W−1)/2(W−1)/2𝐱t+k).\\tilde{\\mathbf{x}}\_{t}=\\mathrm{Normalize}\\left(\\frac{1}{W}\\sum\\nolimits\_{k=-(W-1)/2}^{(W-1)/2}\\mathbf{x}\_{t+k}\\right). |  | (8) |

This windowed averaging stabilizes the frame-level embeddings. We consistently use W=5W=5 in all experiments. When this module is enabled, the visual embedding 𝐱t\\mathbf{x}\_{t} in Sec. [3.3](https://arxiv.org/html/2609.06360v1#S3.SS3 "3.3 Prompt-Contrastive Anomaly Scoring ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") is replaced by 𝐱~t\\tilde{\\mathbf{x}}\_{t} to improve anomaly scoring.

Motion Gating.
Anomalous events are often accompanied by observable motion, whereas low-motion segments are a common source of false positives. We estimate the local motion strength of frame ftf\_{t} using the cosine distance between its neighboring original frame embeddings,

|     |     |     |     |
| --- | --- | --- | --- |
|  | mt=1−𝐱t−1⊤​𝐱t+1.m\_{t}=1-\\mathbf{x}\_{t-1}^{\\top}\\mathbf{x}\_{t+1}. |  | (9) |

Note that 𝐱t−1\\mathbf{x}\_{t-1} and 𝐱t+1\\mathbf{x}\_{t+1} denote the L2-normalized frame embeddings before windowed aggregation.

A soft gate derived from the motion strength is then applied to refine the anomaly score of frame ftf\_{t}:

|     |     |     |     |
| --- | --- | --- | --- |
|  | s¯t=st⋅sig⁡(β⁡(mt−τm)),\\bar{s}\_{t}=s\_{t}\\cdot\\mathrm{sig}\\left(\\beta(m\_{t}-\\tau\_{m})\\right), |  | (10) |

where sig⁡(⋅)\\mathrm{sig}(\\cdot) denotes the logistic sigmoid, τm\\tau\_{m} is the motion threshold, and β\\beta is the gate slope; the latter two are fixed across datasets without target-specific tuning, and their values are reported in Sec. [4.1](https://arxiv.org/html/2609.06360v1#S4.SS1 "4.1 Experimental Setup ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"). Unlike a hard threshold, the soft gate does not set low-motion scores exactly to zero. It down-weights low-motion frames, while high-motion frames largely retain their pre-gate scores.
When motion gating is enabled, the anomaly score sts\_{t} in Sec. [3.3](https://arxiv.org/html/2609.06360v1#S3.SS3 "3.3 Prompt-Contrastive Anomaly Scoring ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") is replaced by s¯t\\bar{s}\_{t} before Gaussian smoothing.
The final scores are then smoothed by a Gaussian temporal filter of bandwidth σ\\sigma, a standard post-processing step separate from the embedding- and motion-level operations of MAS.

Remark. In implementation, the full-rate visual embeddings are first used to compute the motion signal, after which windowed aggregation is applied when MAS is enabled. The resulting embeddings are temporally sampled (1:16) for prompt-contrastive scoring. The sampled anomaly scores are then linearly interpolated to the original frame rate, followed by motion gating in Eq. [10](https://arxiv.org/html/2609.06360v1#S3.E10 "Equation 10 ‣ 3.5 Motion-Aware Stabilization (MAS) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") and Gaussian smoothing.

## 4 Experiments

### 4.1 Experimental Setup

Datasets.
We evaluate NOVA on two standard VAD benchmarks. UCF-Crime\[ [20](https://arxiv.org/html/2609.06360v1#bib.bib1 "")\] contains 1,900 surveillance videos, including 290 test videos with frame-level binary annotations. The dataset covers 13 anomaly categories: Abuse, Arrest, Arson, Assault, Burglary, Explosion, Fighting, Road Accident, Robbery, Shooting, Shoplifting, Stealing, and Vandalism.
XD-Violence\[ [25](https://arxiv.org/html/2609.06360v1#bib.bib2 "")\] contains videos collected from YouTube and movies, covering six anomaly categories: Abuse, Car Accident, Explosion, Fighting, Riot, and Shooting. The test set includes videos from multiple source domains and provides frame-level binary annotations.
Following \[ [31](https://arxiv.org/html/2609.06360v1#bib.bib5 ""), [29](https://arxiv.org/html/2609.06360v1#bib.bib22 ""), [7](https://arxiv.org/html/2609.06360v1#bib.bib6 "")\], we evaluate only on the official test sets to ensure fairness. Frame-level AUC-ROC is reported on UCF-Crime, while frame-level average precision (AP) and frame-level AUC-ROC are reported on XD-Violence.

Implementation Details.
We use GPT-5.4-mini-2026-03-17 \[ [14](https://arxiv.org/html/2609.06360v1#bib.bib18 "")\] (OpenAI API) to construct the prompt banks described in Sec. [3.2](https://arxiv.org/html/2609.06360v1#S3.SS2 "3.2 Normality-Aware Prompt Construction (NA) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"). The dataset-specific role guidance and examples used by the generator are fixed across categories, seeds, and NA variants; their full contents are provided in the supplementary material. We use the text prefixes T+=T^{+}=“Anomalous scene: ” and T−=T^{-}=“Normal scene: ” when embedding anomaly and normal descriptions, respectively. For each anomaly category, we generate M=20M=20 anomaly descriptions and M=20M=20 normal descriptions. Normal-prompt construction uses category-specific confusing actions together with K=4K=4 shared calm anchors, followed by geometry-guided refinement with threshold θ=0.70\\theta=0.70 for at most R=3R=3 rounds. All prompt-construction parameters (KK, MM, θ\\theta, and RR) are fixed a priori and are not calibrated on the target dataset. To evaluate prompt robustness, we independently generate five prompt banks for each category and report the average performance.
All experiments are conducted on a single NVIDIA GeForce RTX 4080 SUPER. Videos are uniformly sampled at an interval of 16 frames, and the linear interpolation described in the remark of Sec. [3.5](https://arxiv.org/html/2609.06360v1#S3.SS5 "3.5 Motion-Aware Stabilization (MAS) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") is applied to recover frame-level predictions. Following prior work, dataset-level AUC and AP are computed by pooling frame-level predictions and binary labels from all test videos.
We use PE-Core-L14-336 \[ [2](https://arxiv.org/html/2609.06360v1#bib.bib19 "")\] as the frozen vision-language backbone. Unless otherwise specified, the same hyperparameters are used for both datasets: SAP coefficient α=0.90\\alpha=0.90, temperature τ=0.03\\tau=0.03, Gaussian smoothing parameter σ=50.0\\sigma=50.0, warm-up length Nwarm=32N\_{\\mathrm{warm}}=32, VNA temperature γ=0.3\\gamma=0.3, MAS window size W=5W=5, motion threshold τm=0.02\\tau\_{m}=0.02, and gate slope β=20\\beta=20.

### 4.2 Comparison with State-of-the-Art

Table [1](https://arxiv.org/html/2609.06360v1#S4.T1 "Table 1 ‣ 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") compares NOVA with representative VAD methods under different training paradigms. Since LLM-generated prompt banks may vary across calls, NOVA’s results are reported as the mean over five independently generated prompt banks, whereas the results of competing methods are taken from their respective papers.

Among training-free zero-shot methods, NOVA achieves the best performance on all three evaluation metrics. On UCF-Crime, NOVA obtains the highest frame-level AUC. On XD-Violence, NOVA achieves the highest AUC and AP, improving AP over Flashback \[ [7](https://arxiv.org/html/2609.06360v1#bib.bib6 "")\] by 9.69 percentage points and AUC over VADTree \[ [9](https://arxiv.org/html/2609.06360v1#bib.bib17 "")\] by 4.52 percentage points.
Despite requiring no target-domain training, fine-tuning, or calibration,
NOVA remains competitive with several weakly supervised methods and
outperforms the other training-free zero-shot methods included in the comparison.

Table 1:
Comparison with VAD methods under different training paradigms.
Bold indicates the best result, while underline indicates the best result within a paradigm.
“—” denotes results not reported in the original paper.
†LAVIDA and †LaGoVAD use external segmentation data to synthesize pseudo-anomalies and are therefore not considered strictly training-free.

|  | Method | UCF-Crime | XD-Violence |
|  | AUC (%)↑\\uparrow | AP (%)↑\\uparrow | AUC (%)↑\\uparrow |
| Weaklysupervised | RareAnom \[ [21](https://arxiv.org/html/2609.06360v1#bib.bib26 "")\] | 83.56 | — | 79.89 |
| VERA \[ [29](https://arxiv.org/html/2609.06360v1#bib.bib22 "")\] | 86.55 | — | 88.26 |
| CLIP-TSA \[ [6](https://arxiv.org/html/2609.06360v1#bib.bib15 "")\] | 87.58 | 82.19 | — |
| VadCLIP \[ [26](https://arxiv.org/html/2609.06360v1#bib.bib20 "")\] | 88.02 | 84.51 | — |
| Dong \[ [4](https://arxiv.org/html/2609.06360v1#bib.bib33 "")\] | 88.52 | — | — |
| Holmes-VAD \[ [32](https://arxiv.org/html/2609.06360v1#bib.bib21 "")\] | 89.51 | 90.67 | — |
| One class | GODS \[ [24](https://arxiv.org/html/2609.06360v1#bib.bib23 "")\] | 70.46 | — | — |
| Unsupervised | GCL \[ [30](https://arxiv.org/html/2609.06360v1#bib.bib24 "")\] | 71.04 | — | — |
| FPDM \[ [27](https://arxiv.org/html/2609.06360v1#bib.bib27 "")\] | 74.70 | — | — |
| MULDE \[ [13](https://arxiv.org/html/2609.06360v1#bib.bib28 "")\] | 78.50 | — | — |
| DyAnNet \[ [22](https://arxiv.org/html/2609.06360v1#bib.bib25 "")\] | 84.50 | — | — |
| Zero shot | LaGoVAD†\[ [11](https://arxiv.org/html/2609.06360v1#bib.bib36 "")\] | 81.12 | 74.25 | — |
| LAVIDA†\[ [3](https://arxiv.org/html/2609.06360v1#bib.bib9 "")\] | 82.18 | 90.62 | — |
| Training-freezero shot | LAVAD \[ [31](https://arxiv.org/html/2609.06360v1#bib.bib5 "")\] | 80.28 | 62.01 | 85.36 |
| AnyAnomaly \[ [1](https://arxiv.org/html/2609.06360v1#bib.bib29 "")\] | 80.70 | — | — |
| EventVAD \[ [18](https://arxiv.org/html/2609.06360v1#bib.bib30 "")\] | 82.03 | 64.04 | 87.51 |
| VADTree \[ [9](https://arxiv.org/html/2609.06360v1#bib.bib17 "")\] | 84.74 | 68.85 | 90.55 |
| PANDA \[ [28](https://arxiv.org/html/2609.06360v1#bib.bib31 "")\] | 84.89 | 70.16 | — |
| Flashback \[ [7](https://arxiv.org/html/2609.06360v1#bib.bib6 "")\] | 87.29 | 75.13 | 90.54 |
| ASK-Hint \[ [36](https://arxiv.org/html/2609.06360v1#bib.bib8 "")\] | 89.83 | — | 90.31 |
| NOVA (Ours) | 89.86 | 84.82 | 95.07 |

### 4.3 Ablation Study

Table [2](https://arxiv.org/html/2609.06360v1#S4.T2 "Table 2 ‣ 4.3 Ablation Study ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") reports a full-factorial ablation of NA, VNA, and MAS. When NA is disabled, the normal prompts are generated without the normality-aware constraints introduced in Sec. [3.2](https://arxiv.org/html/2609.06360v1#S3.SS2 "3.2 Normality-Aware Prompt Construction (NA) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"). The baseline disables all three modules; NA enables normality-aware prompt construction, VNA adds the per-video visual normality anchor, and MAS introduces windowed embeddings and motion gating.

All configurations use the same PE-Core-L14-336 backbone \[ [2](https://arxiv.org/html/2609.06360v1#bib.bib19 "")\], scoring hyperparameters, and SAP scoring rule. This controlled setup isolates the effects of the enabled components.

Table 2: Full-factorial ablation of NA, VNA, and MAS. Results are reported as mean ±\\pm standard deviation over five independently generated prompt banks.

| NA | VNA | MAS | UCF AUC (%) | XD AUC (%) | XD AP (%) |
| --- | --- | --- | --- | --- | --- |
| ×\\times | ×\\times | ×\\times | 85.62±1.4185.62\\pm 1.41 | 93.51±0.4893.51\\pm 0.48 | 80.36±1.5180.36\\pm 1.51 |
| ✓ | ×\\times | ×\\times | 88.79±0.5088.79\\pm 0.50 | 94.29±0.4594.29\\pm 0.45 | 84.33±1.6084.33\\pm 1.60 |
| ×\\times | ✓ | ×\\times | 86.99±1.0386.99\\pm 1.03 | 94.08±0.4194.08\\pm 0.41 | 80.47±1.4580.47\\pm 1.45 |
| ×\\times | ×\\times | ✓ | 86.73±1.2786.73\\pm 1.27 | 91.54±0.2391.54\\pm 0.23 | 72.88±0.6472.88\\pm 0.64 |
| ✓ | ✓ | ×\\times | 89.54±0.4589.54\\pm 0.45 | 94.85±0.3094.85\\pm 0.30 | 84.65±1.3584.65\\pm 1.35 |
| ✓ | ×\\times | ✓ | 89.34±0.6189.34\\pm 0.61 | 91.07±0.3691.07\\pm 0.36 | 72.96±0.6672.96\\pm 0.66 |
| ×\\times | ✓ | ✓ | 87.54±1.0087.54\\pm 1.00 | 94.65±0.2994.65\\pm 0.29 | 82.40±0.9182.40\\pm 0.91 |
| ✓ | ✓ | ✓ | 89.86±0.43\\mathbf{89.86\\pm 0.43} | 95.07±0.33\\mathbf{95.07\\pm 0.33} | 84.82±0.56\\mathbf{84.82\\pm 0.56} |

NA provides the largest and most consistent improvement. Relative to the baseline, NA improves UCF AUC by 3.17 pp, XD AUC by 0.78 pp, and XD AP by 3.97 pp, while introducing no additional inference-time computation. VNA alone improves the same metrics by 1.37, 0.57, and 0.11 pp, respectively. In contrast, the effect of MAS is dataset-dependent: it improves UCF AUC by 1.11 pp, but decreases XD AUC and AP by 1.97 and 7.48 pp.

The factorial design also reveals clear interactions between the modules. Combining NA and VNA consistently improves over either component alone. On UCF-Crime, their joint gain is 3.92 pp, smaller than the 4.54 pp obtained by summing their individual gains, suggesting partially overlapping contributions. On XD-Violence, their gains are nearly additive: the joint improvements are 1.34 pp in AUC and 4.29 pp in AP, compared with summed individual gains of 1.35 and 4.08 pp, respectively.

VNA also changes the effect of MAS on XD-Violence. With NA enabled, adding MAS without VNA reduces XD AP from 84.33 to 72.96, whereas enabling VNA together with MAS raises it to 84.82. A similar pattern appears without NA, where VNA+MAS reaches 82.40 AP compared with 72.88 for MAS alone. Once VNA is present, however, the additional accuracy gain from MAS is modest: relative to NA+VNA, the full model improves UCF AUC, XD AUC, and XD AP by 0.32, 0.22, and 0.17 pp, respectively.

MAS nevertheless substantially reduces sensitivity to prompt-bank variation on XD-Violence. Across the four configurations without MAS, the standard deviation of XD AP ranges from 1.35 to 1.60, whereas it decreases to 0.56–0.91 when MAS is enabled. Thus, NA is the primary source of accuracy improvement, VNA provides consistent complementary gains, and MAS mainly improves robustness to prompt-bank variation once combined with VNA. Enabling all three components yields the best mean performance on all three metrics.

Additional representative PCA visualizations and qualitative frame-level anomaly score curves are provided in the supplementary material.

### 4.4 Analysis

Normal and Anomaly Prompt Analysis.
While prompts play an important role in VAD, NOVA focuses on normal-side modeling. Table [3](https://arxiv.org/html/2609.06360v1#S4.T3 "Table 3 ‣ 4.4 Analysis ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") presents a systematic analysis of different decompositions of normal and anomaly prompts.
A preliminary model uses templates containing only class names, providing weak anomaly descriptions and no normal-side reference.
Replacing the text with LLM-generated anomaly descriptions improves UCF-Crime but does not reliably improve XD-Violence AP, suggesting that enriching anomaly-side modeling alone is insufficient.
Introducing additional normal descriptions and jointly scoring anomaly and normal prompts with SAP-Softmax, even without NA, further improves performance.
Applying NA further strengthens the normal side by removing semantically ambiguous descriptions that are close to anomalies. These results highlight the importance of normal-side modeling in NOVA.

Table 3: Decomposition of normal-side and anomaly-side contributions on UCF-Crime and XD-Violence.

| Config | UCF AUC (%) | XD AUC (%) | XD AP (%) |
| Template, anomaly classes only | 66.85 | 90.99 | 77.94 |
| LLM, anomaly classes only | 72.50±2.0972.50\\pm 2.09 | 91.81±0.7191.81\\pm 0.71 | 76.44±2.3776.44\\pm 2.37 |
| LLM, normal+anomaly (no NA) | 85.62±1.4185.62\\pm 1.41 | 93.51±0.4893.51\\pm 0.48 | 80.36±1.5180.36\\pm 1.51 |
| LLM, normal+anomaly (NA) | 88.79 ±\\pm 0.50 | 94.29 ±\\pm 0.45 | 84.33 ±\\pm 1.60 |

Geometric Analysis of NA.
Fig. [2](https://arxiv.org/html/2609.06360v1#S4.F2 "Figure 2 ‣ 4.4 Analysis ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") visualizes the prompt embeddings before and after applying NA using t-SNE. Compared with unconstrained prompt generation, NA produces a clearer separation between the normal (green) and anomaly (red) prompts, with visibly less overlap. This change is also reflected quantitatively: the anomaly–normal centroid cosine similarity decreases from 0.904 to 0.844. The improved separation is consistent with the ablation results in Table [2](https://arxiv.org/html/2609.06360v1#S4.T2 "Table 2 ‣ 4.3 Ablation Study ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"), suggesting that NA strengthens prompt-contrastive scoring by making the normal side more distinguishable from the anomaly side. In contrast, prior work \[ [4](https://arxiv.org/html/2609.06360v1#bib.bib33 "")\] includes normal descriptions with ambiguous verbs such as “running” and “joggers”, which overlap semantically with anomaly-related actions.

![Refer to caption](https://arxiv.org/html/2609.06360v1/pic/fig_tsne_constraint.png)Figure 2:
t-SNE visualization of UCF-Crime prompt embeddings from five independently generated prompt banks, with and without NA. Stars denote the corresponding centroids; cosine similarities are computed in the original embedding space.

Geometric Analysis of VNA.

Fig. [3](https://arxiv.org/html/2609.06360v1#S4.F3 "Figure 3 ‣ 4.4 Analysis ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") visualizes the frame embeddings, category prompt embeddings, the visual normality anchor 𝐚VNA\\mathbf{a}\_{\\mathrm{VNA}}, and the visual normal centroid cnc\_{n} on a per-video PCA plane. Here, cnc\_{n} is computed only for post-hoc analysis by averaging the normalized embeddings of all ground-truth normal frames and is never used during VNA construction or inference. Panel (a) shows the representative UCF-Crime video _Burglary017\_x264_; panel (b) uses the same visual reference and aggregates textual centroids over all 13 anomaly categories and five independently generated prompt banks. Dataset-level statistics over all 140 anomalous test videos are reported separately below.

As illustrated in Fig. [3](https://arxiv.org/html/2609.06360v1#S4.F3 "Figure 3 ‣ 4.4 Analysis ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"), the visual anchor closely matches the visual normal centroid, whereas the textual prompt embeddings remain well separated from the visual frame distribution. Across the 65 category–bank pairs in panel (b), the mean cosine similarity to cnc\_{n} is 0.186±0.0170.186\\pm 0.017 for the textual normal centroids and 0.196±0.0330.196\\pm 0.033 for the textual anomaly centroids. In contrast, the five prompt-bank-dependent VNA anchors for this video achieve 0.989±0.0020.989\\pm 0.002.

This pattern is consistent across the dataset. Averaged over all videos, the mean cosine similarity between 𝐚VNA\\mathbf{a}\_{\\mathrm{VNA}} and cnc\_{n} is 0.969, whereas the corresponding value for the textual normal centroid is only 0.167. Furthermore, in 94.29% of the videos, the textual anomaly centroid is closer to cnc\_{n} than the textual normal centroid. These observations support the motivation of VNA: due to the cross-modal gap, textual normal prompts do not necessarily provide a visual reference close to normal frames, whereas the visual anchor constructed from the test video better captures the video’s normal appearance. Additional representative examples are provided in the supplementary material.

![Refer to caption](https://arxiv.org/html/2609.06360v1/pic/fig_pca_vna_main.png)Figure 3:
Geometric analysis of VNA on the representative UCF-Crime video _Burglary017\_x264_. (a) Per-video PCA projection of frame and prompt embeddings using the seed-10 prompt bank, together with the visual normality anchor 𝐚VNA\\mathbf{a}\_{\\mathrm{VNA}} and the ground-truth normal-frame centroid cnc\_{n} used only for post-hoc analysis.
(b) Original-space cosine similarities to cnc\_{n} for textual normal and anomaly centroids across 13 anomaly categories and five independently generated prompt banks, together with the five VNA anchors, one per prompt bank. Large markers and error bars denote mean ±\\pm standard deviation.

## 5 Conclusions

We presented NOVA, a training-free ZS-VAD framework that strengthens normal-side modeling in prompt-contrastive anomaly detection. NOVA improves normality representations at the linguistic level through Normality-Aware Prompt Construction and at the visual level through Visual Normality Anchor.
Without training, fine-tuning, or target-data calibration, NOVA achieves 89.86% AUC on UCF-Crime and 95.07% AUC / 84.82% AP on XD-Violence. Ablation and embedding-space analyses further demonstrate the importance of explicit normal-side modeling and the complementary roles of linguistic and visual normality.
These findings suggest that improving anomaly detection does not necessarily require increasingly elaborate anomaly representations; establishing a better boundary between normality and anomaly can provide a stronger basis for anomaly discrimination.

NOVA currently models visual normality from an early-video warm-up prefix and applies the resulting fixed visual anchor throughout the entire video. This design limits its applicability to long-term, open-world video anomaly detection, where normality may evolve over time. These limitations motivate online, scene-adaptive normality modeling as an important direction for future work.

## References

- \[1\]S. Ahn, Y. Jo, K. Lee, S. Kwon, I. Hong, and S. Park (2026)Anyanomaly: zero-shot customizable video anomaly detection with lvlm.
In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision,
pp. 3026–3035.
Cited by: [§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p1.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p2.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.17.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[2\]D. Bolya, P. Huang, P. Sun, J. H. Cho, A. Madotto, C. Wei, T. Ma, J. Zhi, J. Rajasegaran, H. Bangalath, et al. (2026)Perception encoder: the best visual embeddings are not at the output of the network.
Advances in Neural Information Processing Systems38, pp. 60884–60937.
Cited by: [§4.1](https://arxiv.org/html/2609.06360v1#S4.SS1.p2.1 "4.1 Experimental Setup ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§4.3](https://arxiv.org/html/2609.06360v1#S4.SS3.p2.1 "4.3 Ablation Study ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[3\]Z. Dai, K. Li, J. Liu, J. Yang, and Y. Qiao (2026)No need for real anomaly: mllm empowered zero-shot video anomaly detection.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 35648–35658.
Cited by: [§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p2.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.15.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[4\]M. Dong (2024)CLIP: assisted video anomaly detection..
In ICPRAM,
pp. 522–533.
Cited by: [§1](https://arxiv.org/html/2609.06360v1#S1.p2.1 "1 Introduction ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p1.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.4](https://arxiv.org/html/2609.06360v1#S2.SS4.p1.1 "2.4 Prompt Design and Modality Gap ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§4.4](https://arxiv.org/html/2609.06360v1#S4.SS4.p2.1 "4.4 Analysis ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.7.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[5\]J. Jeong, Y. Zou, T. Kim, D. Zhang, A. Ravichandran, and O. Dabeer (2023)Winclip: zero-/few-shot anomaly classification and segmentation.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 19606–19616.
Cited by: [§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p1.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.4](https://arxiv.org/html/2609.06360v1#S2.SS4.p1.1 "2.4 Prompt Design and Modality Gap ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[6\]H. K. Joo, K. Vo, K. Yamazaki, and N. Le (2023)Clip-tsa: clip-assisted temporal self-attention for weakly-supervised video anomaly detection.
In 2023 IEEE International Conference on Image Processing (ICIP),
pp. 3230–3234.
Cited by: [§1](https://arxiv.org/html/2609.06360v1#S1.p1.1 "1 Introduction ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.1](https://arxiv.org/html/2609.06360v1#S2.SS1.p1.1 "2.1 Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.5.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[7\]H. Lee, H. Kim, I. Kim, and Y. Choi (2025)Flashback: memory-driven zero-shot, real-time video anomaly detection.
arXiv:2505.15205.
Cited by: [§1](https://arxiv.org/html/2609.06360v1#S1.p2.1 "1 Introduction ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p1.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.3](https://arxiv.org/html/2609.06360v1#S2.SS3.p1.1 "2.3 Normality Modeling ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.4](https://arxiv.org/html/2609.06360v1#S2.SS4.p1.1 "2.4 Prompt Design and Modality Gap ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§3.3](https://arxiv.org/html/2609.06360v1#S3.SS3.p1.1 "3.3 Prompt-Contrastive Anomaly Scoring ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§3.3](https://arxiv.org/html/2609.06360v1#S3.SS3.p2.1 "3.3 Prompt-Contrastive Anomaly Scoring ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§4.1](https://arxiv.org/html/2609.06360v1#S4.SS1.p1.1 "4.1 Experimental Setup ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§4.2](https://arxiv.org/html/2609.06360v1#S4.SS2.p2.1 "4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.21.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[8\]F. Li, W. Liu, J. Chen, R. Zhang, Y. Wang, X. Zhong, and Z. Wang (2025)Anomize: better open vocabulary video anomaly detection.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 29203–29212.
Cited by: [§2.1](https://arxiv.org/html/2609.06360v1#S2.SS1.p1.1 "2.1 Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[9\]W. Li, Y. Xu, Y. Rao, Z. Wang, and S. Deng (2026)VADTree: explainable training-free video anomaly detection via hierarchical granularity-aware tree.
Advances in Neural Information Processing Systems38, pp. 148372–148404.
Cited by: [§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p2.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§4.2](https://arxiv.org/html/2609.06360v1#S4.SS2.p2.1 "4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.19.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[10\]V. W. Liang, Y. Zhang, Y. Kwon, S. Yeung, and J. Y. Zou (2022)Mind the gap: understanding the modality gap in multi-modal contrastive representation learning.
Advances in Neural Information Processing Systems35, pp. 17612–17625.
Cited by: [§1](https://arxiv.org/html/2609.06360v1#S1.p4.1 "1 Introduction ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.4](https://arxiv.org/html/2609.06360v1#S2.SS4.p2.1 "2.4 Prompt Design and Modality Gap ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§3.4](https://arxiv.org/html/2609.06360v1#S3.SS4.p1.1 "3.4 Visual Normality Anchor (VNA) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[11\]Z. Liu, X. Wu, J. Wu, X. Wang, and L. Yang (2025)Language-guided open-world video anomaly detection under weak supervision.
arXiv:2503.13160.
Cited by: [§2.1](https://arxiv.org/html/2609.06360v1#S2.SS1.p1.1 "2.1 Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.14.2.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[12\]W. Luo, Y. Cao, H. Yao, X. Zhang, J. Lou, Y. Cheng, W. Shen, and W. Yu (2025)Exploring intrinsic normal prototypes within a single image for universal anomaly detection.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 9974–9983.
Cited by: [§2.3](https://arxiv.org/html/2609.06360v1#S2.SS3.p1.1 "2.3 Normality Modeling ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[13\]J. Micorek, H. Possegger, D. Narnhofer, H. Bischof, and M. Kozinski (2024)Mulde: multiscale log-density estimation via denoising score matching for video anomaly detection.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 18868–18877.
Cited by: [Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.12.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[14\]OpenAI (2026)GPT-5.4-mini.
Note: OpenAI model documentationCited by: [§4.1](https://arxiv.org/html/2609.06360v1#S4.SS1.p2.1 "4.1 Experimental Setup ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[15\]S. Pratt, I. Covert, R. Liu, and A. Farhadi (2023)What does a platypus look like? generating customized prompts for zero-shot image classification.
In Proceedings of the IEEE/CVF International Conference on Computer Vision,
pp. 15691–15701.
Cited by: [§2.4](https://arxiv.org/html/2609.06360v1#S2.SS4.p1.1 "2.4 Prompt Design and Modality Gap ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[16\]A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. (2021)Learning transferable visual models from natural language supervision.
In International Conference on Machine Learning,
pp. 8748–8763.
Cited by: [§1](https://arxiv.org/html/2609.06360v1#S1.p2.1 "1 Introduction ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[17\]B. Ramachandra, M. J. Jones, and R. R. Vatsavai (2020)A survey of single-scene video anomaly detection.
IEEE Transactions on Pattern Analysis and Machine Intelligence44, pp. 2293–2312.
Cited by: [§2.1](https://arxiv.org/html/2609.06360v1#S2.SS1.p1.1 "2.1 Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[18\]Y. Shao, H. He, S. Li, S. Chen, X. Long, F. Zeng, Y. Fan, M. Zhang, Z. Yan, A. Ma, et al. (2025)Eventvad: training-free event-aware video anomaly detection.
In Proceedings of the 33rd ACM International Conference on Multimedia,
pp. 2586–2595.
Cited by: [§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p1.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p2.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.18.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[19\]Y. Song, W. Shen, B. Pan, Q. Wu, and D. Gu (2025)Reducing modal differences in zero-shot anomaly detection based on vision-language generation model.
Engineering Applications of Artificial Intelligence162, pp. 112541.
Cited by: [§1](https://arxiv.org/html/2609.06360v1#S1.p4.1 "1 Introduction ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.4](https://arxiv.org/html/2609.06360v1#S2.SS4.p2.1 "2.4 Prompt Design and Modality Gap ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§3.4](https://arxiv.org/html/2609.06360v1#S3.SS4.p1.1 "3.4 Visual Normality Anchor (VNA) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[20\]W. Sultani, C. Chen, and M. Shah (2018)Real-world anomaly detection in surveillance videos.
In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition,
pp. 6479–6488.
Cited by: [§1](https://arxiv.org/html/2609.06360v1#S1.p1.1 "1 Introduction ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.1](https://arxiv.org/html/2609.06360v1#S2.SS1.p1.1 "2.1 Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.3](https://arxiv.org/html/2609.06360v1#S2.SS3.p1.1 "2.3 Normality Modeling ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§4.1](https://arxiv.org/html/2609.06360v1#S4.SS1.p1.1 "4.1 Experimental Setup ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[21\]K. V. Thakare, D. P. Dogra, H. Choi, H. Kim, and I. Kim (2023)Rareanom: a benchmark video dataset for rare type anomalies.
Pattern Recognition140, pp. 109567.
Cited by: [Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.3.2.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[22\]K. V. Thakare, Y. Raghuwanshi, D. P. Dogra, H. Choi, and I. Kim (2023)Dyannet: a scene dynamicity guided self-trained video anomaly detection network.
In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision,
pp. 5541–5550.
Cited by: [Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.13.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[23\]Y. Tian, G. Pang, Y. Chen, R. Singh, J. W. Verjans, and G. Carneiro (2021)Weakly-supervised video anomaly detection with robust temporal feature magnitude learning.
In Proceedings of the IEEE/CVF International Conference on Computer Vision,
pp. 4975–4986.
Cited by: [§1](https://arxiv.org/html/2609.06360v1#S1.p1.1 "1 Introduction ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.1](https://arxiv.org/html/2609.06360v1#S2.SS1.p1.1 "2.1 Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.3](https://arxiv.org/html/2609.06360v1#S2.SS3.p1.1 "2.3 Normality Modeling ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[24\]J. Wang and A. Cherian (2019)Gods: generalized one-class discriminative subspaces for anomaly detection.
In Proceedings of the IEEE/CVF International Conference on Computer Vision,
pp. 8201–8211.
Cited by: [§2.3](https://arxiv.org/html/2609.06360v1#S2.SS3.p1.1 "2.3 Normality Modeling ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.9.2.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[25\]P. Wu, J. Liu, Y. Shi, Y. Sun, F. Shao, Z. Wu, and Z. Yang (2020)Not only look, but also listen: learning multimodal violence detection under weak supervision.
In European Conference on Computer Vision,
pp. 322–339.
Cited by: [§4.1](https://arxiv.org/html/2609.06360v1#S4.SS1.p1.1 "4.1 Experimental Setup ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[26\]P. Wu, X. Zhou, G. Pang, L. Zhou, Q. Yan, P. Wang, and Y. Zhang (2024)Vadclip: adapting vision-language models for weakly supervised video anomaly detection.
In Proceedings of the AAAI Conference on Artificial Intelligence,
Vol. 38, pp. 6074–6082.
Cited by: [§1](https://arxiv.org/html/2609.06360v1#S1.p1.1 "1 Introduction ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.1](https://arxiv.org/html/2609.06360v1#S2.SS1.p1.1 "2.1 Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p1.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.6.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[27\]C. Yan, S. Zhang, Y. Liu, G. Pang, and W. Wang (2023)Feature prediction diffusion model for video anomaly detection.
In Proceedings of the IEEE/CVF International Conference on Computer Vision,
pp. 5527–5537.
Cited by: [Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.11.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[28\]Z. Yang, C. Gao, and M. Z. Shou (2025)PANDA: towards generalist video anomaly detection via agentic AI engineer.
In Advances in Neural Information Processing Systems,
Cited by: [§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p2.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.20.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[29\]M. Ye, W. Liu, and P. He (2025)Vera: explainable video anomaly detection via verbalized learning of vision-language models.
In Proceedings of the Computer Vision and Pattern Recognition Conference,
pp. 8679–8688.
Cited by: [§4.1](https://arxiv.org/html/2609.06360v1#S4.SS1.p1.1 "4.1 Experimental Setup ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.4.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[30\]M. Z. Zaheer, A. Mahmood, M. H. Khan, M. Segu, F. Yu, and S. Lee (2022)Generative cooperative learning for unsupervised video anomaly detection.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 14744–14754.
Cited by: [§2.1](https://arxiv.org/html/2609.06360v1#S2.SS1.p1.1 "2.1 Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.10.2.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[31\]L. Zanella, W. Menapace, M. Mancini, Y. Wang, and E. Ricci (2024)Harnessing large language models for training-free video anomaly detection.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 18527–18536.
Cited by: [§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p1.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p2.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§4.1](https://arxiv.org/html/2609.06360v1#S4.SS1.p1.1 "4.1 Experimental Setup ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.16.2.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[32\]H. Zhang, X. Xu, X. Wang, J. Zuo, C. Han, X. Huang, C. Gao, Y. Wang, and N. Sang (2024)Holmes-vad: towards unbiased and explainable video anomaly detection via multi-modal llm.
arXiv:2406.12235.
Cited by: [Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.8.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[33\]Y. Zheng, X. Shi, J. Chen, and Y. Shu (2025)Cerberus: real-time video anomaly detection via cascaded vision-language models.
arXiv:2510.16290.
Cited by: [§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p2.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.3](https://arxiv.org/html/2609.06360v1#S2.SS3.p1.1 "2.3 Normality Modeling ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[34\]K. Zhou, J. Yang, C. C. Loy, and Z. Liu (2022)Learning to prompt for vision-language models.
International Journal of Computer Vision130 (9), pp. 2337–2348.
Cited by: [§2.4](https://arxiv.org/html/2609.06360v1#S2.SS4.p1.1 "2.4 Prompt Design and Modality Gap ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[35\]Q. Zhou, G. Pang, Y. Tian, S. He, and J. Chen (2024)Anomalyclip: object-agnostic prompt learning for zero-shot anomaly detection.
In International Conference on Learning Representations,
Vol. 2024, pp. 49705–49737.
Cited by: [§2.4](https://arxiv.org/html/2609.06360v1#S2.SS4.p1.1 "2.4 Prompt Design and Modality Gap ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

- \[36\]S. Zou, X. Tian, L. Wesemann, F. Waschkowski, Z. Yang, and J. Zhang (2026)Unlocking vision-language models for video anomaly detection via fine-grained prompting.
In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision,
pp. 4223–4233.
Cited by: [§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p1.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[§2.2](https://arxiv.org/html/2609.06360v1#S2.SS2.p2.1 "2.2 Zero-Shot Video Anomaly Detection ‣ 2 Related Work ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
[Table 1](https://arxiv.org/html/2609.06360v1#S4.T1.9.1.22.1.1 "In 4.2 Comparison with State-of-the-Art ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").


\\thetitle

Supplementary Material

## Appendix A Sensitivity to the Prompt-Generation LLM

Our framework utilizes an existing LLM to generate normality descriptions.
To assess sensitivity to the prompt-generation LLM, we generate the M=20M=20 prompt banks using three representative models: GPT-5.4-mini, Gemini 3.5 Flash
Lite, and Qwen-2.5-72B-Instruct. All prompt-generation roles access these models
through OpenRouter. We use the same generation seed
and keep all downstream evaluation settings fixed. For each prompt bank, we
evaluate both the NA-only configuration and the full NOVA.

Table S1: Sensitivity to the prompt-generation LLM. Each model generates M=20M=20 positive and 20 negative descriptions per anomaly category. Results are percentages from one prompt-generation seed; all downstream settings are fixed.

| Generator | Configuration | UCF AUC | XD AUC | XD AP |
| --- | --- | --- | --- | --- |
| GPT-5.4-mini | NA-only | 88.87 | 92.99 | 79.15 |
| Full NOVA | 90.09 | 94.69 | 83.21 |
| Gemini 3.5 | NA-only | 89.19 | 92.90 | 79.77 |
| Flash Lite | Full NOVA | 90.33 | 95.34 | 84.27 |
| Qwen-2.5-72B- | NA-only | 87.81 | 94.27 | 84.12 |
| Instruct | Full NOVA | 89.21 | 95.48 | 85.40 |

As shown in Table [S1](https://arxiv.org/html/2609.06360v1#A1.T1 "Table S1 ‣ Appendix A Sensitivity to the Prompt-Generation LLM ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"),
across all three generators, the full NOVA consistently improves over the
corresponding NA-only configuration. Moreover, the final results remain within
relatively narrow ranges: 89.21–90.33% AUC on UCF-Crime, 94.69–95.48% AUC
on XD-Violence, and 83.21–85.40% AP on XD-Violence. These results suggest
that NOVA’s improvements persist across the evaluated prompt-generation LLMs
and that its final performance is not strongly tied to a particular generator.

## Appendix B Sensitivity to the Number of Prompts

We further evaluate how prompt-bank size affects performance. Using the same NA
construction procedure, we generate 100 positive and 100 negative descriptions
per anomaly category. We then take the first MM descriptions from each side in
a fixed order, with M∈{10,20,40,100}M\\in\\{10,20,40,100\\}, to form prompt banks of different
sizes. Within each dataset, all prompt counts use descriptions from the same
generation run, so the observed differences more directly reflect the impact of MM.
This experiment uses one prompt-generation seed. NA is enabled, whereas VNA and
MAS are disabled.
The PE-Core encoder, frame sampling, LLM model, SAP-Softmax parameters, and
Gaussian smoothing are otherwise identical to the main evaluation protocol.

Table S2: Sensitivity to the number MM of positive and negative prompt descriptions per anomaly category. For each dataset, every row uses the same generation seed and draws MM descriptions per side from the same set of 100 positive and 100 negative descriptions. NA is enabled, whereas VNA and MAS are disabled.

| MM | UCF AUC | XD AUC | XD AP |
| --- | --- | --- | --- |
| 10 | 87.53 | 93.86 | 83.69 |
| 20 | 88.64 | 94.31 | 84.60 |
| 40 | 89.07 | 94.50 | 83.76 |
| 100 | 89.22 | 94.58 | 84.19 |

As shown in Table [S2](https://arxiv.org/html/2609.06360v1#A2.T2 "Table S2 ‣ Appendix B Sensitivity to the Number of Prompts ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"), increasing MM consistently improves AUC on both datasets. UCF-Crime AUC rises
from 87.53% to 89.22%, while XD-Violence AUC rises from 93.86% to 94.58%.
In contrast, XD-Violence AP does not follow the same trend. It reaches its
highest value of 84.60% at M=20M=20, then changes to 83.76% at M=40M=40 and
84.19% at M=100M=100. These results indicate that increasing the number of prompts
can improve AUC without consistently improving AP. The M=20M=20 setting used in
the main experiments was fixed before conducting this sensitivity analysis and
was not selected or retuned based on these results. Its performance is
consistent with the observed five-seed range of the original NA-only baseline.

![Refer to caption](https://arxiv.org/html/2609.06360v1/pic/fig_pca_vna.png)Figure S1: Per-video PCA projections of six illustrative UCF-Crime videos, including the _Burglary017\_x264_ example shown in the main paper and five additional examples. The yellow star denotes the score-weighted 𝐚VNA\\mathbf{a}\_{\\mathrm{VNA}}, and the teal cross denotes the ground-truth normal-frame centroid cnc\_{n}. Blue/red dots are normal/anomalous frames; blue/red triangles are category-specific normal/anomaly prompts; gray markers are prompts from the other categories. Annotated cosine similarities are computed in the original embedding space.

## Appendix C Sensitivity to the Warm-up Length NwarmN\_{\\text{warm}}

Table [S3](https://arxiv.org/html/2609.06360v1#A3.T3 "Table S3 ‣ Appendix C Sensitivity to the Warm-up Length 𝑁_\"warm\" ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") evaluates the sensitivity of NOVA to the warm-up window size NwarmN\_{\\text{warm}} used for constructing the visual normality anchor. Across an eightfold range from 8 to 64 sampled visual embeddings, the performance remains stable on both datasets. The maximum variation is only 0.39 pp in UCF-Crime AUC, 0.57 pp in XD-Violence AUC, and 1.67 pp in XD-Violence AP.

Although performance on XD-Violence increases slightly as NwarmN\_{\\text{warm}} becomes larger, the improvement is gradual rather than critical, indicating that VNA is not highly sensitive to the exact choice of the warm-up window. We therefore use a fixed value of Nwarm=32N\_{\\text{warm}}=32 throughout all experiments, without dataset-specific tuning.

Table S3: Sensitivity analysis of NwarmN\_{\\text{warm}}. Results are the mean and standard deviation over five prompt banks. † denotes the default used in the main experiments.

| NwarmN\_{\\text{warm}} | UCF AUC | XD AUC | XD AP |
| --- | --- | --- | --- |
| 8 | 89.76±0.4089.76\\pm 0.40 | 94.62±0.3894.62\\pm 0.38 | 83.53±0.6883.53\\pm 0.68 |
| 16 | 89.88±0.4189.88\\pm 0.41 | 94.91±0.3594.91\\pm 0.35 | 84.28±0.5984.28\\pm 0.59 |
| 24 | 89.87±0.4289.87\\pm 0.42 | 95.01±0.3395.01\\pm 0.33 | 84.60±0.5884.60\\pm 0.58 |
| 32†32^{\\dagger} | 89.86±0.4389.86\\pm 0.43 | 95.07±0.3395.07\\pm 0.33 | 84.82±0.5684.82\\pm 0.56 |
| 48 | 89.72±0.4589.72\\pm 0.45 | 95.11±0.3395.11\\pm 0.33 | 84.98±0.5484.98\\pm 0.54 |
| 64 | 89.49±0.4789.49\\pm 0.47 | 95.19±0.3395.19\\pm 0.33 | 85.20±0.5385.20\\pm 0.53 |

## Appendix D Additional Geometric Analysis

Fig. [S1](https://arxiv.org/html/2609.06360v1#A2.F1 "Figure S1 ‣ Appendix B Sensitivity to the Number of Prompts ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") reproduces the main-paper _Burglary017\_x264_ example alongside five additional illustrative UCF-Crime videos. In each example, the VNA anchor lies substantially closer to the post-hoc visual normal centroid than the category-specific textual normal centroid. These single-prompt-bank visualizations are consistent with the dataset-level statistics reported in the main paper Sec. [4.4](https://arxiv.org/html/2609.06360v1#S4.SS4 "4.4 Analysis ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection").

## Appendix E Qualitative Analysis

Fig. [S2](https://arxiv.org/html/2609.06360v1#A5.F2 "Figure S2 ‣ Appendix E Qualitative Analysis ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") shows the frame-level anomaly scores of three representative UCF-Crime videos under different configurations of NOVA. Compared with the baseline, NA generally reduces the anomaly scores assigned to normal segments while retaining clear responses around the annotated anomaly intervals. VNA further suppresses false-positive peaks outside the anomaly regions, leading to a clearer contrast between normal and anomalous frames. MAS mainly improves the temporal smoothness of the score curves by reducing short-lived fluctuations.

![Refer to caption](https://arxiv.org/html/2609.06360v1/pic/fig_per_frame_Explosion029_x264.png)

![Refer to caption](https://arxiv.org/html/2609.06360v1/pic/fig_per_frame_Explosion013_x264.png)

![Refer to caption](https://arxiv.org/html/2609.06360v1/pic/fig_per_frame_RoadAccidents016_x264.png)

Figure S2: Per-frame qualitative analysis on UCF-Crime. Pink regions denote the annotated ground-truth anomaly frames.

## Appendix F Prompt-Generation Templates and Footage Conditioning

To ensure full reproducibility, this section lists the LLM instruction templates used by each role in the
agentic multi-role pipeline described in main paper Sec. [3.2](https://arxiv.org/html/2609.06360v1#S3.SS2 "3.2 Normality-Aware Prompt Construction (NA) ‣ 3 Method ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"), and provides one
worked example showing how the dataset-level _footage description_ shapes the
generated outputs. The manually specified dataset-level context consists of a
footage description together with fixed domain-specific role guidance and examples.
These components are defined once per dataset and reused across categories, seeds,
and prompt-generation runs. The footage description is provided as context to
the prompt-generation agents:

- •


UCF-Crime:footage = "surveillance footage"

- •


XD-Violence:footage = "movie or online video footage"


The remaining placeholders are {anomaly} for the current anomaly
category, {M} for the number of descriptions per side,
{n}/{k} for the number of anchors (we use K=4K=4),
{fv} for the mined confusing actions, and {ex} for the
generated calm-anchor examples.

### F.1 Category-Conditioned Confusing Action Mining

[⬇](data:text/plain;base64,W3N5c3RlbV0KWW91IGFuYWx5emUgYSBDTElQLWJhc2VkIGFub21hbHkgZGV0ZWN0b3IgZm9yIHtmb290YWdlfS4gRm9yIGEgZ2l2ZW4gYW5vbWFseQpjYXRlZ29yeSB5b3UgaWRlbnRpZnkgQU1CSUdVT1VTIGFjdGlvbnM6IGJlbmlnbiwgbm9ybWFsIGJlaGF2aW9ycyB0aGF0IGEgcGVyc29uCm1pZ2h0IHBsYXVzaWJseSBkbyBpbiBldmVyeWRheSB7Zm9vdGFnZX0gYnV0IHRoYXQgVklTVUFMTFkgUkVTRU1CTEUgdGhlIGFub21hbHkKYW5kIHdvdWxkIGJlIGNvbmZ1c2VkIHdpdGggaXQuIFRoZXNlIGFyZSB0aGUgYWN0aW9ucyB0aGF0IG11c3QgYmUgRk9SQklEREVOIGZyb20KJ25vcm1hbCBzY2VuZScgZGVzY3JpcHRpb25zIHNvIHRoZSBub3JtYWwgc2lkZSBzdGF5cyBjbGVhcmx5IHNlcGFyYWJsZSBmcm9tIHRoZQphbm9tYWx5LgoKW3VzZXJdCkFub21hbHkgY2F0ZWdvcnk6ICJ7YW5vbWFseX0iLgpMaXN0IDUgdG8gOCBzdWNoIGFtYmlndW91cyB2ZXJicyAvIHNob3J0IGFjdGlvbiBwaHJhc2VzIChiZW5pZ24gYWN0aW9ucyB0aGF0IGxvb2sKbGlrZSAie2Fub21hbHl9IikuIEtlZXAgZWFjaCB0byAxLTMgd29yZHMsIGxvd2VyY2FzZS4KUmV0dXJuIE9OTFkgdmFsaWQgSlNPTjogeyJ2ZXJicyI6IFsiLi4uIiwgIi4uLiJdfQ==)

\[system\]

YouanalyzeaCLIP-basedanomalydetectorfor{footage}.Foragivenanomaly

categoryyouidentifyAMBIGUOUSactions:benign,normalbehaviorsthataperson

mightplausiblydoineveryday{footage}butthatVISUALLYRESEMBLEtheanomaly

andwouldbeconfusedwithit.ThesearetheactionsthatmustbeFORBIDDENfrom

’normalscene’descriptionssothenormalsidestaysclearlyseparablefromthe

anomaly.

\[user\]

Anomalycategory:"{anomaly}".

List5to8suchambiguousverbs/shortactionphrases(benignactionsthatlook

like"{anomaly}").Keepeachto1-3words,lowercase.

ReturnONLYvalidJSON:{"verbs":\["...","..."\]}

### F.2 Calm Anchor Generation

[⬇](data:text/plain;base64,W3N5c3RlbV0KWW91IHdyaXRlIHNob3J0IHZpc3VhbCBzY2VuZSBkZXNjcmlwdGlvbnMgZm9yIGEgQ0xJUC1iYXNlZCBhbm9tYWx5IGRldGVjdG9yLiBZb3UKcHJvZHVjZSBDQUxNIEFOQ0hPUiBzY2VuZXM6IG9yZGluYXJ5LCBub24tdGhyZWF0ZW5pbmcgZXN0YWJsaXNoaW5nIHNob3RzIHR5cGljYWwKb2YgdGhlIGdpdmVuIGZvb3RhZ2UgZG9tYWluLCBjb250YWluaW5nIE5PIGNvbmZsaWN0LCBOTyB3ZWFwb25zIGFuZCBsaXR0bGUgb3Igbm8KbW90aW9uIC0tIHRoZSBhYnNvbHV0ZSBiYXNlbGluZSBvZiAnbm9ybWFsJyBmb3IgdGhhdCBkb21haW4uCgpbdXNlcl0KRm9vdGFnZSBkb21haW46IHtmb290YWdlfS4KV3JpdGUgZXhhY3RseSB7bn0gZGlzdGluY3QgY2FsbSBhbmNob3Igc2NlbmUgZGVzY3JpcHRpb25zIChlYWNoIG9uZSBzaG9ydApzZW50ZW5jZSkgdHlwaWNhbCBvZiB0aGlzIGRvbWFpbi4KUmV0dXJuIE9OTFkgdmFsaWQgSlNPTjogeyJhbmNob3JzIjogWyIuLi4iXX0=)

\[system\]

YouwriteshortvisualscenedescriptionsforaCLIP-basedanomalydetector.You

produceCALMANCHORscenes:ordinary,non-threateningestablishingshotstypical

ofthegivenfootagedomain,containingNOconflict,NOweaponsandlittleorno

motion--theabsolutebaselineof’normal’forthatdomain.

\[user\]

Footagedomain:{footage}.

Writeexactly{n}distinctcalmanchorscenedescriptions(eachoneshort

sentence)typicalofthisdomain.

ReturnONLYvalidJSON:{"anchors":\["..."\]}

### F.3 Prompt-Generation Skeleton

The shared generation skeleton is shown below. The domain\_intro field
is shared across datasets, whereas positive\_roles and
examples are supplied by a fixed dataset-specific domain specification.
These fields are specified before prompt generation and then frozen: they are
reused verbatim for every category, every seed, and every run, and no video,
label, or score from the target dataset is used to adapt them.
The domain\_intro, positive\_roles, and examples
fields are identical in the constrained and unconstrained conditions reported
in Table [2](https://arxiv.org/html/2609.06360v1#S4.T2 "Table 2 ‣ 4.3 Ablation Study ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection") of the main paper. The unconstrained condition
replaces the category-specific normality-aware rules with a generic normal-prompt
instruction, while these shared fields remain unchanged. Their complete
contents are provided below.

[⬇](data:text/plain;base64,e2RvbWFpbl9pbnRyb30KCllvdXIgdGFzazogRm9yIHRoZSBhbm9tYWx5IGNhdGVnb3J5ICJ7YW5vbWFseX0iLCBnZW5lcmF0ZSBleGFjdGx5IHtNfSBQT1NJVElWRVMKYW5kIHtNfSBORUdBVElWRVMuCgotLS0gUE9TSVRJVkUgUlVMRVMgLS0tCjEuIEVhY2ggZGVzY3JpYmVzIE9ORSBzcGVjaWZpYywgdmlzdWFsbHkgb2JzZXJ2YWJsZSBhdG9taWMgYWN0aW9uIHRoYXQgc3Ryb25nbHkKICAgaW5kaWNhdGVzICJ7YW5vbWFseX0iLgp7cG9zaXRpdmVfcm9sZXN9CjMuIEluY2x1ZGUgdGhlIHNwZWNpZmljIGJvZHkgcGFydCwgb2JqZWN0LCBvciBkaXJlY3Rpb24gb2YgbW90aW9uLgo0LiBWYXJ5IHRoZSB7TX0gaXRlbXMgYWNyb3NzIGRpZmZlcmVudCBzdWJqZWN0cywgc3RhZ2VzIG9mIHRoZSBldmVudCwgYW5kIGltcGxpZWQKICAgY2FtZXJhIGFuZ2xlcy4KCi0tLSBORUdBVElWRSBSVUxFUyAtLS0Ke25lZ2F0aXZlX3J1bGVzfQoKLS0tIEhJR0gtUVVBTElUWSBFWEFNUExFUyAodXNlIGFzIHN0eWxlIHJlZmVyZW5jZSkgLS0tCntleGFtcGxlc30KCi0tLSBPVVRQVVQgRk9STUFUIC0tLQpSZXR1cm4gT05MWSB2YWxpZCBKU09OOiB7InBvc2l0aXZlcyI6IFsgLi4ue019IF0sICJuZWdhdGl2ZXMiOiBbIC4uLntNfSBdfQ==)

{domain\_intro}

Yourtask:Fortheanomalycategory"{anomaly}",generateexactly{M}POSITIVES

and{M}NEGATIVES.

\-\-\-POSITIVERULES\-\-\-

1.EachdescribesONEspecific,visuallyobservableatomicactionthatstrongly

indicates"{anomaly}".

{positive\_roles}

3.Includethespecificbodypart,object,ordirectionofmotion.

4.Varythe{M}itemsacrossdifferentsubjects,stagesoftheevent,andimplied

cameraangles.

\-\-\-NEGATIVERULES\-\-\-

{negative\_rules}

\-\-\-HIGH-QUALITYEXAMPLES(useasstylereference)\-\-\-

{examples}

\-\-\-OUTPUTFORMAT\-\-\-

ReturnONLYvalidJSON:{"positives":\[...{M}\],"negatives":\[...{M}\]}

domain\_intro is the same single sentence for both datasets: “You are a
Visual Forensic Expert designing text prompts for a CLIP-based video anomaly
detection system.” The positive\_roles field names, for a subset of the
categories in 𝒞\\mathcal{C}, the kind of subject the description should use, and
closes with the footage description:

[⬇](data:text/plain;base64,W1VDRi1DcmltZV0KMi4gVXNlIFJPTEUtU1BFQ0lGSUMgc3ViamVjdHMgdGhhdCBmaXQgdGhlIGFub21hbHk6CiAgIC0gRm9yIGFycmVzdDogIlBvbGljZSBvZmZpY2VyIiwgIk9mZmljZXIiLCAiVW5pZm9ybWVkIG9mZmljZXIiLCAiU3VzcGVjdCIKICAgLSBGb3IgZmlnaHRpbmc6ICJQZXJzb24iLCAiSW5kaXZpZHVhbCIsICJBdHRhY2tlciIsICJWaWN0aW0iLCAiVHdvIHBlb3BsZSIKICAgLSBGb3IgYXJzb246ICJQZXJzb24iLCAiSW5kaXZpZHVhbCIsICJGbGFtZXMiLCAiRmlyZSIKICAgLSBGb3Igcm9hZCBhY2NpZGVudDogIlZlaGljbGUiLCAiQ2FyIiwgIk1vdG9yY3ljbGUgcmlkZXIiLCAiUGVkZXN0cmlhbiIKICAgLSBNYXRjaCBzdWJqZWN0IHRvIHdoYXQgd291bGQgcmVhbGlzdGljYWxseSBhcHBlYXIgaW4gc3VydmVpbGxhbmNlIGZvb3RhZ2UuCgpbWEQtVmlvbGVuY2VdCjIuIFVzZSBST0xFLVNQRUNJRklDIHN1YmplY3RzIHRoYXQgZml0IHRoZSBhbm9tYWx5OgogICAtIEZvciBmaWdodGluZzogIlBlcnNvbiIsICJUd28gcGVvcGxlIiwgIkF0dGFja2VyIiwgIlZpY3RpbSIsICJCcmF3bGVycyIKICAgLSBGb3Igc2hvb3Rpbmc6ICJHdW5tYW4iLCAiU2hvb3RlciIsICJBcm1lZCBwZXJzb24iLCAiVmljdGltIgogICAtIEZvciBleHBsb3Npb246ICJGaXJlYmFsbCIsICJCbGFzdCIsICJEZWJyaXMiLCAiU2hvY2t3YXZlIgogICAtIEZvciByaW90OiAiQ3Jvd2QiLCAiUmlvdGVycyIsICJNb2IiLCAiQ2xhc2hpbmcgcHJvdGVzdGVycyIKICAgLSBGb3IgYWJ1c2U6ICJBZ2dyZXNzb3IiLCAiVmljdGltIiwgIlBlcnNvbiIKICAgLSBGb3IgY2FyIGFjY2lkZW50OiAiVmVoaWNsZSIsICJDYXIiLCAiU3BlZWRpbmcgY2FyIiwgIk1vdG9yY3ljbGUiCiAgIC0gTWF0Y2ggc3ViamVjdCB0byB3aGF0IHdvdWxkIHJlYWxpc3RpY2FsbHkgYXBwZWFyIGluIG1vdmllIG9yIG9ubGluZQogICAgIHZpZGVvIGZvb3RhZ2Ugb2YgdmlvbGVuY2Uu)

\[UCF-Crime\]

2.UseROLE-SPECIFICsubjectsthatfittheanomaly:

-Forarrest:"Policeofficer","Officer","Uniformedofficer","Suspect"

-Forfighting:"Person","Individual","Attacker","Victim","Twopeople"

-Forarson:"Person","Individual","Flames","Fire"

-Forroadaccident:"Vehicle","Car","Motorcyclerider","Pedestrian"

-Matchsubjecttowhatwouldrealisticallyappearinsurveillancefootage.

\[XD-Violence\]

2.UseROLE-SPECIFICsubjectsthatfittheanomaly:

-Forfighting:"Person","Twopeople","Attacker","Victim","Brawlers"

-Forshooting:"Gunman","Shooter","Armedperson","Victim"

-Forexplosion:"Fireball","Blast","Debris","Shockwave"

-Forriot:"Crowd","Rioters","Mob","Clashingprotesters"

-Forabuse:"Aggressor","Victim","Person"

-Forcaraccident:"Vehicle","Car","Speedingcar","Motorcycle"

-Matchsubjecttowhatwouldrealisticallyappearinmovieoronline

videofootageofviolence.

The examples field supplies a style reference drawn from two categories
of the corresponding 𝒞\\mathcal{C}; it is never used as a verbatim template:

[⬇](data:text/plain;base64,W1VDRi1DcmltZV0KRm9yICJhYnVzZSIgUE9TSVRJVkVTOgoiUGVyc29uIGZvcmNlZnVsbHkgZ3JhYmJpbmcgYW5vdGhlciBieSB0aGUgY29sbGFyIgoiQWdncmVzc29yIHR3aXN0aW5nIHZpY3RpbSdzIGFybSBiZWhpbmQgdGhlaXIgYmFjayBmb3JjZWZ1bGx5IgoiUGVyc29uIHNsYW1taW5nIGFub3RoZXIncyBoZWFkIGFnYWluc3QgYSBoYXJkIHN1cmZhY2UiCiJJbmRpdmlkdWFsIHJlc3RyYWluaW5nIHZpY3RpbSBieSBzaXR0aW5nIG9uIHRvcCBvZiB0aGVtIgoKRm9yICJhYnVzZSIgTkVHQVRJVkVTOgoiUGVyc29uIHNpdHRpbmcgcXVpZXRseSBvbiBhIGNoYWlyIHJlYWRpbmciCiJJbmRpdmlkdWFsIHN0YW5kaW5nIHN0aWxsIG5lYXIgYSB3YWxsIgoiRW1wdHkgcm9vbSB3aXRoIGZ1cm5pdHVyZSBhbmQgbm8gcGVvcGxlIiAgICAgICAgICA8LSBFbXB0eSBBbmNob3IKIkVtcHR5IGNvcnJpZG9yIHdpdGggY2xvc2VkIGRvb3JzIG9uIGJvdGggc2lkZXMiICAgPC0gRW1wdHkgQW5jaG9yCiJQZXJzb24gc2xvd2x5IHR1cm5pbmcgYXJvdW5kIGFuZCB3YWxraW5nIGF3YXkiCgpGb3IgImFycmVzdCIgUE9TSVRJVkVTOgoiUG9saWNlIG9mZmljZXIgcHJlc3Npbmcgc3VzcGVjdCBmYWNlLWRvd24gb250byB0aGUgcGF2ZW1lbnQiCiJPZmZpY2VyIHNuYXBwaW5nIGhhbmRjdWZmcyBvbnRvIGEgcGVyc29uJ3Mgd3Jpc3RzIGJlaGluZCB0aGVpciBiYWNrIgoiVW5pZm9ybWVkIG9mZmljZXIgdGFja2xpbmcgYSBmbGVlaW5nIHN1c3BlY3QgdG8gdGhlIGdyb3VuZCIKIk9mZmljZXIgcGxhY2luZyBrbmVlIG9uIHN1c3BlY3QncyBiYWNrIHdoaWxlIGN1ZmZpbmcgdGhlbSIKCltYRC1WaW9sZW5jZV0KRm9yICJzaG9vdGluZyIgUE9TSVRJVkVTOgoiR3VubWFuIGFpbWluZyBhIGhhbmRndW4gYXQgYSBmbGVlaW5nIHZpY3RpbSIKIlBlcnNvbiBmaXJpbmcgYSByaWZsZSBpbnRvIGEgcGFuaWNraW5nIGNyb3dkIgoiU2hvb3RlciBob2xkaW5nIGEgcGlzdG9sIHdpdGggYm90aCBhcm1zIGV4dGVuZGVkIgoiTXV6emxlIGZsYXNoIGZyb20gYSBndW4gZmlyZWQgaW4gYSBkYXJrIGFsbGV5IgoKRm9yICJhYnVzZSIgTkVHQVRJVkVTOgooc2FtZSBmaXZlIGl0ZW1zIGFzIHRoZSBVQ0YtQ3JpbWUgYmxvY2sgYWJvdmUp)

\[UCF-Crime\]

For"abuse"POSITIVES:

"Personforcefullygrabbinganotherbythecollar"

"Aggressortwistingvictim’sarmbehindtheirbackforcefully"

"Personslamminganother’sheadagainstahardsurface"

"Individualrestrainingvictimbysittingontopofthem"

For"abuse"NEGATIVES:

"Personsittingquietlyonachairreading"

"Individualstandingstillnearawall"

"Emptyroomwithfurnitureandnopeople"<-EmptyAnchor

"Emptycorridorwithcloseddoorsonbothsides"<-EmptyAnchor

"Personslowlyturningaroundandwalkingaway"

For"arrest"POSITIVES:

"Policeofficerpressingsuspectface-downontothepavement"

"Officersnappinghandcuffsontoaperson’swristsbehindtheirback"

"Uniformedofficertacklingafleeingsuspecttotheground"

"Officerplacingkneeonsuspect’sbackwhilecuffingthem"

\[XD-Violence\]

For"shooting"POSITIVES:

"Gunmanaimingahandgunatafleeingvictim"

"Personfiringarifleintoapanickingcrowd"

"Shooterholdingapistolwithbotharmsextended"

"Muzzleflashfromagunfiredinadarkalley"

For"abuse"NEGATIVES:

(samefiveitemsastheUCF-Crimeblockabove)

The negative\_rules block contains the confusing actions
{fv} mined by the Verb Miner and the calm-anchor examples
{ex} produced by the Anchor Generator. This block implements NA at
the language-content level:

[⬇](data:text/plain;base64,MS4gTXVzdCBkZXNjcmliZSBTQUZFLCBTVEFUSUMsIG9yIFNMT1cgYmVoYXZpb3JzIC0tIHRoZSAiYm9yaW5nIiBiYXNlbGluZSBvZgogICB7Zm9vdGFnZX0uCjIuIEZPUkJJRERFTiB2ZXJicy9hY3Rpb25zIGZvciB0aGlzIGNhdGVnb3J5IC0tIHRoZXkgdmlzdWFsbHkgcmVzZW1ibGUKICAgInthbm9tYWx5fSIgYW5kIG11c3QgTkVWRVIgYXBwZWFyIGluIGEgbm9ybWFsIGRlc2NyaXB0aW9uOiB7ZnZ9LgozLiBSRVFVSVJFRDogcHJlZmVyIHBhc3NpdmUsIGxvdy1tb3Rpb24sIHN0YXRpYyBhY3Rpb25zICh0aGUgY2FsbSBiYXNlbGluZSk7CiAgIGF2b2lkIGVuZXJnZXRpYyBvciBmYXN0IGFjdGlvbnMuCjQuIE1BTkRBVE9SWSAtLSBpbmNsdWRlIGV4YWN0bHkge2t9ICJDYWxtIEFuY2hvciIgaXRlbXM6IG9yZGluYXJ5CiAgIG5vbi10aHJlYXRlbmluZyBlc3RhYmxpc2hpbmcgc2NlbmVzIG9mIHtmb290YWdlfSB3aXRoIE5PIGNvbmZsaWN0IGFuZCBOTwogICB3ZWFwb25zLiBFeGFtcGxlczoge2V4fQo1LiBUaGUgcmVtYWluaW5nIHtNfS17a30gaXRlbXMgc2hvdWxkIHNob3cgcGVvcGxlIGluIG9yZGluYXJ5LCBub24tdGhyZWF0ZW5pbmcKICAgc2l0dWF0aW9ucy4KNi4gVmFyeSB0aGUgc3ViamVjdHMgYW5kIGltcGxpZWQgY2FtZXJhIHZpZXdwb2ludHMgYWNyb3NzIHRoZSBpdGVtcy4=)

1.MustdescribeSAFE,STATIC,orSLOWbehaviors--the"boring"baselineof

{footage}.

2.FORBIDDENverbs/actionsforthiscategory--theyvisuallyresemble

"{anomaly}"andmustNEVERappearinanormaldescription:{fv}.

3.REQUIRED:preferpassive,low-motion,staticactions(thecalmbaseline);

avoidenergeticorfastactions.

4.MANDATORY--includeexactly{k}"CalmAnchor"items:ordinary

non-threateningestablishingscenesof{footage}withNOconflictandNO

weapons.Examples:{ex}

5.Theremaining{M}-{k}itemsshouldshowpeopleinordinary,non-threatening

situations.

6.Varythesubjectsandimpliedcameraviewpointsacrosstheitems.

For the unconstrained condition, corresponding to the “LLM normal+anomaly
(no NA)” row in Table [2](https://arxiv.org/html/2609.06360v1#S4.T2 "Table 2 ‣ 4.3 Ablation Study ‣ 4 Experiments ‣ NOVA: Normal-Side Modeling for Training-Free Zero-Shot Video Anomaly Detection"), the category-specific
confusion-action list, static-action preference, and calm-anchor constraint are
omitted. The generic normal-prompt instructions used in this condition are
shown below.

[⬇](data:text/plain;base64,MS4gTXVzdCBkZXNjcmliZSBTQUZFIG9yIG5vbi10aHJlYXRlbmluZyBiZWhhdmlvcnMgLS0gdGhlIG5vcm1hbCBiYXNlbGluZSBvZgogICBzdXJ2ZWlsbGFuY2UgZm9vdGFnZS4KMi4gVGhlIHtNfSBpdGVtcyBzaG91bGQgc2hvdyBwZW9wbGUgZG9pbmcgbXVuZGFuZSwgZXZlcnlkYXkgdGhpbmdzLgozLiBTdWJqZWN0IHZhcmlldHk6ICJQZXJzb24iLCAiSW5kaXZpZHVhbCIsICJUd28gcGVvcGxlIiwgIlBlZGVzdHJpYW4iLAogICAiU2hvcHBlciIsIGV0Yy4=)

1.MustdescribeSAFEornon-threateningbehaviors--thenormalbaselineof

surveillancefootage.

2.The{M}itemsshouldshowpeopledoingmundane,everydaythings.

3.Subjectvariety:"Person","Individual","Twopeople","Pedestrian",

"Shopper",etc.

### F.4 Geometric Critic and Refinement

The Geometric Critic does not use an LLM instruction. It embeds each normal
description with the frozen PE-Core text encoder, computes its cosine similarity
gjcg\_{j}^{c} to the positive centroid, and flags descriptions with
gjc>θg\_{j}^{c}>\\theta (we use θ=0.70\\theta=0.70). Flagged descriptions are passed to the
Refiner with the system instruction below. A rewrite is accepted only if it
reduces the ambiguity score, and this procedure is repeated for at most R=3R=3
rounds:

[⬇](data:text/plain;base64,W3N5c3RlbV0KWW91IHJld3JpdGUgdGV4dCBwcm9tcHRzIGZvciBhIENMSVAtYmFzZWQgc3VydmVpbGxhbmNlIGFub21hbHkgZGV0ZWN0b3IuIEEKJ25vcm1hbCBzY2VuZScgZGVzY3JpcHRpb24gaGFzIGJlZW4gZmxhZ2dlZCBiZWNhdXNlIGl0cyB2aXN1YWwgZW1iZWRkaW5nIHNpdHMgdG9vCmNsb3NlIHRvIHRoZSBhbm9tYWx5ICd7YW5vbWFseX0nIC0tIGl0IGlzIHZpc3VhbGx5IGFtYmlndW91cyBhbmQgd291bGQgYmUKY29uZnVzZWQgd2l0aCB0aGUgYW5vbWFseS4gUmV3cml0ZSBpdCBpbnRvIGFuIFVOQU1CSUdVT1VTIG5vcm1hbCBzdXJ2ZWlsbGFuY2UKZGVzY3JpcHRpb24gb2YgdGhlIFNBTUUgc2NlbmUgdHlwZTogYSBwbGF1c2libGUgYmVuaWduIGJhc2VsaW5lLCBidXQgY2xlYXJseQpzdGF0aWMgLyBjYWxtIC8gbm9uLXRocmVhdGVuaW5nIHNvIGl0IGNhbm5vdCBiZSBjb25mdXNlZCB3aXRoICd7YW5vbWFseX0nLgpQcmVmZXIgcGFzc2l2ZSBvciBzbG93IGFjdGlvbnMgKHNpdHRpbmcsIHN0YW5kaW5nLCB3YWl0aW5nLCB3YWxraW5nIHNsb3dseSwgZW1wdHkKc2NlbmUpLiBSZXR1cm4gT05MWSB0aGUgcmV3cml0dGVuIHNlbnRlbmNlLCBubyBxdW90ZXMsIG5vIGV4cGxhbmF0aW9uLg==)

\[system\]

YourewritetextpromptsforaCLIP-basedsurveillanceanomalydetector.A

’normalscene’descriptionhasbeenflaggedbecauseitsvisualembeddingsitstoo

closetotheanomaly’{anomaly}’--itisvisuallyambiguousandwouldbe

confusedwiththeanomaly.RewriteitintoanUNAMBIGUOUSnormalsurveillance

descriptionoftheSAMEscenetype:aplausiblebenignbaseline,butclearly

static/calm/non-threateningsoitcannotbeconfusedwith’{anomaly}’.

Preferpassiveorslowactions(sitting,standing,waiting,walkingslowly,empty

scene).ReturnONLYtherewrittensentence,noquotes,noexplanation.

### F.5 Effect of Footage Conditioning

The following example shows prompts generated for the same anomaly category,
_shooting_, under seed 10, with the two datasets’ domain specifications.
The _normal_ side is conditioned by the footage description at generation
time.

#### UCF-Crime.

(footage = surveillance footage)

Positives:

- •


Person extending both arms while firing a handgun toward the left side of the frame

- •


Individual crouched behind a car door with a pistol discharging bright muzzle flashes

- •


Suspect leaning out of a vehicle window while shooting a handgun downward


Negatives:

- •


A quiet empty hallway under fluorescent lights with closed doors and no people.

- •


A static view of a lobby with a reception desk and a few chairs, everything still.

- •


A parking lot at night with parked cars and no visible movement.


#### XD-Violence.

(footage = movie or online video footage)

Positives:

- •


Gunman extending one arm forward while aiming a handgun at a victim

- •


Shooter firing a pistol from behind a car door toward the street

- •


Armed person gripping a rifle with both hands and pointing it at a doorway


Negatives:

- •


A quiet indoor shot of a person sitting on a couch watching a screen.

- •


A steady view of a desk with a laptop and a mug in a simple room.

- •


A static shot of a living room with soft lighting and a television in the background.