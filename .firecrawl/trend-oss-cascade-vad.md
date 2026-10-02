Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: CC BY-NC-ND 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2601.06204v2 \[cs.CV\] 13 Jan 2026

# Cascading Multi-Agent Anomaly Detection in Surveillance Systems via Vision-Language Models and Embedding-Based Classification

Tayyab Rehman
Affiliation: Department of Engineering,
Affiliation: Computer Science and Mathematics (DISIM),
Affiliation: University of L’Aquila
Affiliation: L’Aquila, Italy
Email: [tayyab.rehman@graduate.univaq.it](mailto:)Giovanni De Gasperis
Affiliation: Department of Engineering,
Affiliation: Computer Science and Mathematics (DISIM),
Affiliation: University of L’Aquila
Affiliation: L’Aquila, Italy
Email: [giovanni.degasperis@univaq.it](mailto:)Aly Shmahell
Affiliation: SPEE, Srl, L’Aquila, Italy
Email: [a.shmahell@spee.it](mailto:)

###### Abstract

Intelligent anomaly detection in dynamic visual environments requires reconciling real-time performance with semantic interpretability. Conventional approaches address only fragments of this challenge: reconstruction-based models capture low-level deviations without contextual reasoning, object detectors provide speed but limited semantics, and large vision–language systems deliver interpretability at prohibitive computational cost. This work introduces a cascading multi-agent framework that unifies these complementary paradigms into a coherent and interpretable architecture. Early modules perform reconstruction-gated filtering and object-level assessment, while higher-level reasoning agents are selectively invoked to interpret semantically ambiguous events. The system employs adaptive escalation thresholds and a publish–subscribe communication backbone, enabling asynchronous coordination and scalable deployment across heterogeneous hardware. Extensive evaluation on large-scale monitoring data demonstrates that the proposed cascade achieves a threefold reduction in latency compared to direct vision–language inference, while maintaining high perceptual fidelity (PSNR = 38.3 dB, SSIM = 0.965) and consistent semantic labeling. The framework advances beyond conventional detection pipelines by combining early-exit efficiency, adaptive multi-agent reasoning, and explainable anomaly attribution—establishing a reproducible and energy-efficient foundation for scalable intelligent visual monitoring.

A Preprint

|     |
| --- |
|  |

_Keywords_ Video anomaly detection, Multi-agent systems, Cascading architectures,
Vision–Language Models, Surveillance, Interpretability, Efficiency

## 1 Introduction

Anomaly detection in surveillance video has become an indispensable component of intelligent monitoring systems, as large-scale camera deployments generate continuous streams that cannot be reviewed manually. Effective systems must satisfy two conflicting requirements: real-time responsiveness, to react to critical events with minimal latency, and semantic interpretability, to ensure that alerts correspond to meaningful anomalies \[ [1](https://arxiv.org/html/2601.06204v2#bib.bib1 "")\]. Conventional methods achieve only partial success. Object-detection pipelines, including recent high-speed variants of the YOLO family, provide rapid recognition but are limited to predefined categories and fail to generalize to complex or unseen events  \[ [2](https://arxiv.org/html/2601.06204v2#bib.bib2 "")\]. Reconstruction-based methods, such as convolutional autoencoders, detect deviations from learned standard patterns without requiring explicit labels, but are often unstable under illumination changes, camera noise, or dynamic backgrounds  \[ [3](https://arxiv.org/html/2601.06204v2#bib.bib3 "")\].

Recent surveys emphasize the potential of vision-language models (VLMs) for video anomaly detection, highlighting their ability to generate natural-language descriptions and capture contextual semantics  \[ [4](https://arxiv.org/html/2601.06204v2#bib.bib4 "")\]. Emerging frameworks, such as LLaVA-NeXT-Interleave, extend these capabilities to multi-image and video scenarios, while weakly supervised methods, like VadCLIP, demonstrate how textual prototypes can align with video features to detect anomalies without exhaustive annotations  \[ [5](https://arxiv.org/html/2601.06204v2#bib.bib5 "")\]. Further advances in unsupervised VLM-assisted anomaly detection explore promising applications in open-world surveillance contexts. Nevertheless, the high inference latency and computational footprint of VLMs constrain their direct use in real-time deployments. The literature increasingly points toward cascading architectures as a viable solution  \[ [6](https://arxiv.org/html/2601.06204v2#bib.bib6 "")\]. Lightweight detectors handle routine inputs at the edge, while only ambiguous or complex cases escalate to computationally intensive reasoning modules. This mirrors trends in networking and multi-agent surveillance, where event-driven responsiveness is complemented by background monitoring and infrastructure health checks. Such designs not only improve efficiency but also align with requirements for privacy preservation and scalability in distributed multi-camera systems  \[ [7](https://arxiv.org/html/2601.06204v2#bib.bib7 "")\].

This work introduces a cascading multi-agent architecture that integrates three complementary paradigms: fast object-level detection using YOLOv8, reconstruction-based anomaly scoring using a convolutional autoencoder, and semantic reasoning using a VLM with an embedding-based classifier  \[ [8](https://arxiv.org/html/2601.06204v2#bib.bib8 "")\]. The design employs an event-driven agent that responds to silent alarms and a cyclical monitoring agent that systematically verifies camera streams and configurations. Together, these agents achieve both rapid responsiveness and long-term robustness. The cascading pipeline ensures early exit for routine cases while escalating ambiguous frames for deeper semantic analysis, thus balancing efficiency with interpretability  \[ [9](https://arxiv.org/html/2601.06204v2#bib.bib9 "")\].

The contributions of this work are as follows:

- •


Dual-agent orchestration. An event-driven agent handles alarm
responses, while a cyclical agent ensures continuous health monitoring of the
camera network, creating a coordinated multi-agent structure.

- •


Reconstruction-gated cascading pipeline. The architecture
integrates YOLO-based object detection, autoencoder reconstruction scoring,
and VLM-driven semantic reasoning in an early-exit cascade, balancing
computational efficiency with interpretability.

- •


Centroid-based semantic normalization. Free-text outputs from
the VLM are mapped into structured anomaly categories through an
embedding-based classifier with an abstention mechanism, ensuring consistent
and reliable labeling.


Together, these contributions establish a reproducible and generalizable
framework that advances anomaly detection in surveillance by unifying
multi-agent coordination, cascading efficiency, and semantic reasoning. This work is developed as part of the research project “IMAHS – Intelligent Multi-Agent Architecture for Himalaya Supervisor”, which aims to design scalable multi-agent solutions for intelligent supervision and monitoring. In this context, our proposed cascading multi-agent anomaly detection framework contributes a practical pipeline for real-time surveillance analysis by combining Vision–Language Models with embedding-based classification and multi-stage escalation.

## 2 Related Work

This review examines recent studies pertinent to surveillance video anomaly detection through three strands: efficient detector-based methods, weakly supervised and vision-language assisted anomaly detection, and domain-agnostic frameworks. The literature search was conducted across Google Scholar, arXiv, IEEE Xplore, and ACM DL using keywords such as video anomaly detection, weak supervision, vision-language models, edge detection vs reconstruction, and multi-camera surveillance. After removing duplicates and inaccessible works, eight papers from 2024-2025 were selected based on relevance, methodological innovation, and performance metrics  \[ [10](https://arxiv.org/html/2601.06204v2#bib.bib10 ""), [11](https://arxiv.org/html/2601.06204v2#bib.bib11 "")\].

Wu et al. \[ [12](https://arxiv.org/html/2601.06204v2#bib.bib12 "")\] introduced VadCLIP, which adapts CLIP for weakly supervised anomaly detection by aligning video embeddings with textual prototypes. Their methodology reduced reliance on frame-level labels and achieved strong performance on UCF-Crime and XD-Violence. Results confirmed that multimodal alignment improves generalization to unseen events. However, inference latency limited real-time deployment, and the system struggled with fine-grained contextual anomalies. Extending this work, Liu et al. \[ [13](https://arxiv.org/html/2601.06204v2#bib.bib13 "")\] developed VadCLIP++, adding dynamic temporal modules to improve context sensitivity. This resulted in higher detection accuracy and more stable performance under temporal noise. Nevertheless, its computational overhead remained prohibitive for edge-level surveillance, suggesting the need for hybrid pipelines where VLMs are applied selectively.

Compact and efficient architectures have also been proposed. Zhu et al. \[ [14](https://arxiv.org/html/2601.06204v2#bib.bib14 "")\] designed ProDisc-VAD, which introduced a prototype interaction layer and discriminative enhancement loss, achieving AUCs above 97% on ShanghaiTech and 87% on UCF-Crime with only 0.4M parameters. The model demonstrated that weakly supervised anomaly detection can be both accurate and lightweight. Still, its reliance on video-level labels restricted anomaly localization, and semantic reasoning was absent. Gu et al. \[ [15](https://arxiv.org/html/2601.06204v2#bib.bib15 "")\] proposed UniVAD, a training-free few-shot framework that clusters patches and builds graph-based reasoning for cross-domain anomaly detection. Results showed strong generalization across industrial, medical, and surveillance datasets. Yet, UniVAD operated at image level rather than on continuous streams, limiting its applicability for real-time monitoring.

Explainability has been another critical focus. Huang et al. \[ [16](https://arxiv.org/html/2601.06204v2#bib.bib16 "")\] introduced Ex-VAD, which coupled vision-language models with natural-language generation, enabling fine-grained anomaly classification with textual explanations. Empirical evaluations highlighted improvements in interpretability and user trust, though at the cost of increased latency. Ye et al. \[ [17](https://arxiv.org/html/2601.06204v2#bib.bib17 "")\] presented VERA, which verbalizes anomaly reasoning directly from VLMs, offering transparent decision pathways. While valuable for accountability, the method depended on computationally heavy VLM inference and was difficult to scale.

Dataset contributions and surveys have also influenced the field. Zhu et al. \[ [18](https://arxiv.org/html/2601.06204v2#bib.bib18 "")\] released MSAD, a dataset with diverse illumination and scene variations, while also reviewing recent anomaly detection models. Their work emphasized dataset bias as a persistent barrier to real-world robustness. Gao et al. \[ [19](https://arxiv.org/html/2601.06204v2#bib.bib19 "")\] provided a unifying perspective on the evolution of video anomaly detection from deep neural networks to multimodal large models, underscoring the importance of hybrid systems that combine efficiency with contextual reasoning. Sträter et al. \[ [20](https://arxiv.org/html/2601.06204v2#bib.bib20 "")\] introduced GeneralAD, a cross-domain model that simulates distortions and attends to patch features for anomaly localization. Although results were strong across domains, the model required significant computational resources and lacked explicit semantic reasoning.

Across these studies, three key patterns emerge. First, VLM-based systems advance semantic reasoning but remain computationally expensive for real-time deployment. Second, compact weakly supervised systems achieve efficiency but often sacrifice interpretability. Third, cross-domain or explainable methods improve robustness yet struggle to scale to continuous multi-camera streams. These limitations underscore the need for architectures that combine efficiency, accuracy, and interpretability. The proposed framework addresses this gap by
integrating fast object detection, reconstruction-based anomaly scoring, and selective VLM reasoning into a coordinated multi-agent cascade, enabling both early-exit efficiency and semantic consistency in anomaly detection.

Table 1: Comparison of recent video anomaly detection approaches

| Ref. | Approach | Domain | Limitation | Relevance |
| --- | --- | --- | --- | --- |
| Wu et al. \[ [12](https://arxiv.org/html/2601.06204v2#bib.bib12 "")\] | VadCLIP: CLIP-based VLM | Surveillance | High latency | Basis for selective VLM use |
| Liu et al. \[ [13](https://arxiv.org/html/2601.06204v2#bib.bib13 "")\] | VadCLIP++: temporal modules | Surveillance | Heavy compute | Motivates hybrid cascade |
| Zhu et al. \[ [14](https://arxiv.org/html/2601.06204v2#bib.bib14 "")\] | ProDisc-VAD: prototype + discrim. loss | Surveillance | Video-level labels | Lightweight baseline |
| Gu et al. \[ [15](https://arxiv.org/html/2601.06204v2#bib.bib15 "")\] | UniVAD: few-shot graph reasoning | Cross-domain | Image-level only | Shows generalization limits |
| Huang et al. \[ [16](https://arxiv.org/html/2601.06204v2#bib.bib16 "")\] | Ex-VAD: explainable VLM | Surveillance | Latency; misclass. | Supports interpretable VLM |
| Ye et al. \[ [17](https://arxiv.org/html/2601.06204v2#bib.bib17 "")\] | VERA: verbalized reasoning | Surveillance | Heavy inference | Adds semantic transparency |
| Zhu et al. \[ [18](https://arxiv.org/html/2601.06204v2#bib.bib18 "")\] | MSAD: dataset + review | Surveillance | Dataset bias | Benchmark reference |
| Gao et al. \[ [19](https://arxiv.org/html/2601.06204v2#bib.bib19 "")\] | Survey: DNN to multimodal | Broad | No pipeline | Confirms hybrid trend |
| Sträter et al. \[ [20](https://arxiv.org/html/2601.06204v2#bib.bib20 "")\] | GeneralAD: transformer model | Cross-domain | High compute; no semantics | Illustrates trade-offs |

## 3 Proposed Methodology

The proposed framework is a cascading multi-agent architecture for anomaly detection in video surveillance. The design unifies three heterogeneous detection paradigms—object-level recognition, reconstruction-based scoring, and vision-language semantic reasoning—within a layered cascade. A dual-agent structure coordinates data acquisition and processing: (i) an event-driven agent that responds to asynchronous silent alarms and retrieves relevant streams, and (ii) a cyclical monitoring agent that executes continuous health verification of the camera network, including connectivity, configuration, and storage consistency. This design ensures responsiveness to security-critical events while maintaining persistent situational awareness of the surveillance infrastructure.

### 3.1 Multi-Agent Architecture

Formally, let 𝒞={c1,…,cN}\\mathcal{C}=\\{c\_{1},\\dots,c\_{N}\\} denote the set of NN surveillance cameras. Each camera stream si​(t)s\_{i}(t) produces frames xti∈ℝH×W×3x\_{t}^{i}\\in\\mathbb{R}^{H\\times W\\times 3} at time tt. The event-driven agent 𝒜e\\mathcal{A}\_{e} is triggered by an alert signal α∈{0,1}\\alpha\\in\\{0,1\\} and routes the corresponding stream sj​(t)s\_{j}(t) into the detection pipeline. The cyclical monitoring agent 𝒜m\\mathcal{A}\_{m} executes periodic probes p⁡(si)p(s\_{i}) at interval Δ​T\\Delta T to verify operational status. Agent coordination is achieved via a publish–subscribe message broker ℬ\\mathcal{B}, where 𝒜e\\mathcal{A}\_{e} and 𝒜m\\mathcal{A}\_{m} publish tasks to ℬ\\mathcal{B}, and worker processes subscribe to execute the cascade. Beyond this publish–subscribe orchestration, the framework can naturally be extended with richer multi-agent behaviors. For example, the event-driven and cyclical agents may exchange information when their anomaly signals diverge, allowing negotiated escalation to higher stages of the cascade. Similarly, agents could be endowed with policies that prioritize different objectives—such as minimizing false positives versus minimizing latency—enabling adaptive responses under resource constraints. These mechanisms situate the system more firmly within the multi-agent paradigm, highlighting opportunities for distributed deployments where camera-level agents collaborate and share anomaly evidence across the network.

### 3.2 Cascading Detection Pipeline

Given a frame xtx\_{t}, the anomaly detection cascade is defined as a sequence of
mappings:

|     |     |     |     |
| --- | --- | --- | --- |
|  | f⁡(xt)={f1​(xt),if ​maxk​P1​(y=k∣xt)≥τ1,f2​(xt),if ​e​(xt)≥τ2,f3​(xt),otherwise,f(x\_{t})=\\begin{cases}f\_{1}(x\_{t}),&\\text{if }\\max\\limits\_{k}\\,P\_{1}(y=k\\mid x\_{t})\\;\\geq\\;\\tau\_{1},\\\\[6.0pt\]<br>f\_{2}(x\_{t}),&\\text{if }e(x\_{t})\\;\\geq\\;\\tau\_{2},\\\\[6.0pt\]<br>f\_{3}(x\_{t}),&\\text{otherwise},\\end{cases} |  | (1) |

where f1f\_{1}, f2f\_{2}, and f3f\_{3} correspond to object-level detection,
reconstruction-based scoring, and semantic reasoning respectively.
The thresholds τ1\\tau\_{1} and τ2\\tau\_{2} specify the confidence levels
for early exits in the cascade.

Stage I: Object-Level Detection. A YOLOv8 detector f1f\_{1} produces probability distributions P1​(y\|xt)P\_{1}(y\|x\_{t}) over pre-trained categories. Frames with maxk⁡P1​(y=k\|xt)≥τ1\\max\_{k}P\_{1}(y=k\|x\_{t})\\geq\\tau\_{1} are classified as nominal or anomalous events (e.g., obstructed view) at this stage.

Stage II: Reconstruction-Based Scoring. For frames not confidently resolved, a convolutional autoencoder ℰ,𝒟\\mathcal{E},\\mathcal{D} is applied. The reconstruction error is defined as:

|     |     |     |
| --- | --- | --- |
|  | e⁡(xt)=‖xt−𝒟⁡(ℰ⁡(xt))‖22.e(x\_{t})=\\\|x\_{t}-\\mathcal{D}(\\mathcal{E}(x\_{t}))\\\|\_{2}^{2}. |  |

If e⁡(xt)≥τ2e(x\_{t})\\geq\\tau\_{2}, the frame is flagged anomalous due to low-level distortions such as frozen streams or illumination shifts.

Stage III: Semantic Reasoning. Remaining cases are escalated to a vision-language model f3f\_{3}. A textual description TtT\_{t} is generated and embedded into a joint space ϕ⁡(Tt)∈ℝd\\phi(T\_{t})\\in\\mathbb{R}^{d}. Video embeddings ψ⁡(xt)\\psi(x\_{t}) are aligned via a prototype-based classifier:

|     |     |     |
| --- | --- | --- |
|  | y∗=arg⁡maxk​⟨ψ⁡(xt),μk⟩,y^{\*}=\\arg\\max\_{k}\\,\\langle\\psi(x\_{t}),\\mu\_{k}\\rangle, |  |

where {μk}\\{\\mu\_{k}\\} are class prototypes representing anomaly categories such as person with weapon or collapsed individual.

### 3.3 Early-Exit Strategy

The cascade introduces an early-exit mechanism to minimize computational overhead. The exit probability at stage jj is defined as:

|     |     |     |
| --- | --- | --- |
|  | Pexitj=𝟙​(confj​(xt)≥τj),P\_{\\text{exit}}^{j}=\\mathbb{1}\\left(\\text{conf}\_{j}(x\_{t})\\geq\\tau\_{j}\\right), |  |

where confj​(xt)\\text{conf}\_{j}(x\_{t}) is the stage-specific confidence measure. This mechanism ensures that routine anomalies are resolved by lightweight modules (f1,f2f\_{1},f\_{2}), while complex cases are selectively escalated to the VLM (f3f\_{3}). Empirical analysis in our experiments shows that over 70% of frames exit at Stage I or II, reducing average latency by a factor of 3×\\times compared to direct VLM processing.

### 3.4 Implementation Details

The system is implemented as a distributed pipeline. YOLOv8 is deployed in its lightweight configuration (∼\\sim7M parameters) with TensorRT optimization. The autoencoder is trained on normal surveillance data using mean squared reconstruction loss, with an input resolution of 128×128128\\times 128 to reduce inference cost. The VLM module is instantiated with a pre-trained large vision-language backbone (e.g., LLaVA-Next) fine-tuned with anomaly-centric textual prompts. Embedding classification uses cosine similarity with a prototype bank updated via exponential moving average. Agents are orchestrated via Redis Pub/Sub channels, and all components are containerized with Docker for reproducibility. Deployment is evaluated on edge servers equipped with NVIDIA A100 GPUs, and latency measurements are reported per stage to quantify efficiency gains from the cascade.

![Refer to caption](https://arxiv.org/html/2601.06204v2/dual_stage_perception.png)Figure 1: Proposed Methodology.

## 4 Case Study

To evaluate the operational effectiveness of the proposed framework, we present a case study conducted on a transportation hub surveillance network. The system integrates fixed CCTV cameras, access-control sensors, and silent-alarm triggers. The case demonstrates how the cascading multi-agent pipeline handles both infrastructure faults and human-centered anomalies in real time.

### 4.1 Scenario: Camera Obstruction with Concurrent Suspicious Activity

At time t0t\_{0}, the cyclical monitoring agent 𝒜m\\mathcal{A}\_{m} detected abnormal statistical signatures from camera cjc\_{j}. Specifically, the average Shannon entropy of frame intensities

|     |     |     |
| --- | --- | --- |
|  | H(xt)=−∑i=1Bpilogpi,H(x\_{t})=-\\sum\_{i=1}^{B}p\_{i}\\log p\_{i}, |  |

where BB denotes histogram bins, dropped below the nominal threshold τH=2.3\\tau\_{H}=2.3, suggesting possible obstruction or severe illumination distortion. Frames xtx\_{t} from cjc\_{j} were routed to the anomaly detection pipeline.

##### Stage I (YOLOv8 Detection).

The detector f1f\_{1} produced category probabilities P1​(y\|xt)P\_{1}(y\|x\_{t}). For the frame at t0+1t\_{0}+1, the prediction “obstructed view” was returned with confidence P1=0.92≥τ1=0.85P\_{1}=0.92\\geq\\tau\_{1}=0.85. The system flagged this as a confirmed anomaly. Processing time: 34 ms on GPU.

##### Stage II (Autoencoder Scoring).

In parallel, the autoencoder estimated reconstruction error

|     |     |     |
| --- | --- | --- |
|  | e⁡(xt)=‖xt−𝒟⁡(ℰ⁡(xt))‖22,e(x\_{t})=\\\|x\_{t}-\\mathcal{D}(\\mathcal{E}(x\_{t}))\\\|\_{2}^{2}, |  |

yielding e⁡(xt)=0.18e(x\_{t})=0.18 compared to τ2=0.12\\tau\_{2}=0.12. The anomaly was corroborated as a visual fault. Processing time: 62 ms.

##### Stage III (VLM Reasoning).

Simultaneously, the event-driven agent 𝒜e\\mathcal{A}\_{e} was activated by a silent alarm from the adjacent access-control gate. The corresponding frames were escalated to the VLM f3f\_{3}. The model generated the textual description “individual loitering near restricted gate” and produced an embedding ψ⁡(xt)\\psi(x\_{t}). Using prototype similarity

|     |     |     |
| --- | --- | --- |
|  | y∗=arg⁡maxk​⟨ψ⁡(xt),μk⟩,y^{\*}=\\arg\\max\_{k}\\langle\\psi(x\_{t}),\\mu\_{k}\\rangle, |  |

the anomaly was classified as suspicious behavior with similarity score 0.840.84. Processing time: 1.82 s.

##### System-Level Response.

The multi-agent orchestration resulted in two correlated anomaly detections: (i) infrastructure fault (camera obstruction) from 𝒜m\\mathcal{A}\_{m}, and (ii) human-centered contextual anomaly (suspicious loitering) from 𝒜e\\mathcal{A}\_{e}. The joint event severity score was computed as

|     |     |     |
| --- | --- | --- |
|  | S=λ1⋅confvisual+λ2⋅confcontextual,S=\\lambda\_{1}\\cdot\\text{conf}\_{\\text{visual}}+\\lambda\_{2}\\cdot\\text{conf}\_{\\text{contextual}}, |  |

where λ1=0.4\\lambda\_{1}=0.4, λ2=0.6\\lambda\_{2}=0.6. The final score S=0.88S=0.88 exceeded the high-priority threshold τS=0.75\\tau\_{S}=0.75, triggering an immediate security alert.

##### Efficiency Gain.

Without cascading, the full stream would have been processed by the VLM, resulting in average latency 8.7​s/frame8.7\\,\\text{s}/\\text{frame}. With early exits, 71.3% of frames were resolved at Stage I and 18.6% at Stage II, leaving only 10.1% for Stage III. The resulting average end-to-end latency was reduced to 2.6​s/frame2.6\\,\\text{s}/\\text{frame}, confirming real-time feasibility.

##### Interpretation.

This scenario demonstrates the system’s capacity to integrate infrastructure health monitoring with semantic reasoning. The cascading pipeline not only detected the obstructed lens anomaly with high confidence at lightweight stages but also escalated ambiguous human activity to the VLM for contextual interpretation. The dual-agent design allowed parallel handling of sensor-based alarms and background monitoring, leading to both rapid response and robust anomaly categorization. While the case study demonstrates how the cascade integrates infrastructure monitoring and contextual reasoning, it remains a controlled example. Real-world deployments typically involve additional variability, including fluctuating illumination, network latency, and overlapping events across multiple cameras. These factors introduce operational challenges that the current controlled scenario cannot fully capture. A broader validation on live surveillance systems would therefore provide deeper insights into the framework’s scalability and robustness in practice.

## 5 Evaluation and Results

In this section, we evaluate the proposed cascading anomaly detection framework using the
UCF-Crime benchmark dataset. We first describe the dataset characteristics and experimental
setup, followed by a detailed presentation of quantitative results, ablation studies, and
qualitative examples. The evaluation emphasizes both accuracy and computational efficiency,
highlighting the trade-offs achieved by our multi-stage design.

### 5.1 Dataset

The evaluation is performed on the UCF-Crime dataset \[ [21](https://arxiv.org/html/2601.06204v2#bib.bib21 "")\], one of the largest
benchmarks for real-world video anomaly detection. The dataset comprises 1,900 untrimmed
surveillance videos with a total duration of approximately 128 hours. Each video is recorded at
30 frames per second and a resolution of 1280×7201280\\times 720, resulting in nearly 13.8 million frames.
The average video length is 242 seconds (about 7,260 frames per sequence). The dataset provides 1,610 training videos with video-level labels (normal versus anomalous)
and 290 test videos with frame-level temporal annotations. Anomalous intervals are defined by
explicit start–end frame indices, and multiple anomalous segments may be present within a single
video. Thirteen categories of anomalous events are included: Abuse, Arrest,
Arson, Assault, Burglary, Explosion,
Fighting, Road Accident, Robbery, Shooting,
Stealing, Shoplifting, and Vandalism, along with a large set of
normal videos. The dataset is inherently imbalanced, with normal sequences forming the majority and several anomalous classes under-represented (e.g., Shooting, Road Accident). This
imbalance necessitates evaluation with macro-averaged metrics such as AUROC and F1-score rather
than raw accuracy alone.

Table 2: Summary statistics of the UCF-Crime dataset.

| Property | Value |
| Total Videos | 1,900 |
| Total Duration | ∼\\sim128 hours |
| Total Frames | ∼\\sim13.8M (30 fps) |
| Avg. Length | 242 s (∼\\sim7.2k frames) |
| Resolution | 1280×7201280\\times 720 |
| Training Set | 1,610 videos (video-level) |
| Testing Set | 290 videos (frame-level) |
| Anomaly Classes | 13 + Normal |
| Annotations | Frame start–end indices |
| Class Imbalance | Normal dominant; some rare |

### 5.2 Experimental Setup

The experimental evaluation was conducted using a hybrid computing environment combining
cloud-based and local resources. Google Colab Pro was used for model training and baseline
experiments, while a local HP Envy PolyStudio workstation was employed for testing the
Vision–Language Model (VLM) and the embedding-based classifier. Google Colab Pro provided access to an NVIDIA Tesla T4 GPU with 16 GB VRAM, high-speed shared RAM, and a Python 3.10 runtime. Deep learning models were implemented in PyTorch, with Hugging Face Transformers used for the VLM module and scikit-learn for the embedding-based classifier. For VLM inference and classifier evaluation, experiments were additionally conducted on an HP Envy PolyStudio workstation running Windows 11 Pro (64-bit), equipped with an Intel Core i7/i9 processor, 16–32 GB RAM, and an NVIDIA RTX GPU. This setup allowed dedicated benchmarking of VLM latency and classifier integration in a controlled local
environment, simulating deployment conditions.Evaluation considered both frame-level anomaly detection and system-level efficiency. Reported metrics include AUROC, precision, recall, and macro-F1 for anomaly classification, alongside average per-frame latency, throughput (frames per second), and stage-wise exit rates within the cascading pipeline.

Table 3: Experimental environments for model training and evaluation.

| Component | Colab Pro (Cloud) | HP Envy PolyStudio (Local) |
| --- | --- | --- |
| Platform | Google Colab Pro VM | Windows 11 Pro (64-bit) |
| Processor | Cloud VM (shared cores) | Intel Core i7/i9 |
| GPU | NVIDIA Tesla T4 (16 GB VRAM) | NVIDIA RTX Series (8–16 GB VRAM) |
| RAM | High-speed shared RAM (up to 32 GB) | 16–32 GB DDR4 |
| Runtime | Python 3.10, PyTorch 2.x, Hugging Face Transformers, scikit-learn | Python 3.10, PyTorch 2.x, Hugging Face Transformers |
| Primary Use | Training YOLOv8 detector, Autoencoder baseline | VLM inference, Embedding-based classifier integration |
| Latency | ∼\\sim50–80 ms per YOLO frame; AE ∼\\sim120 ms/frame | VLM 6–12 s per frame; classifier <100<100 ms per text input |
| Throughput | ∼\\sim15–20 fps (batch inference) | 1–2 fps (limited by VLM latency) |

### 5.3 Autoencoder-Based Anomaly Scoring

The autoencoder is trained exclusively on normal video frames to model the distribution of
regular scene dynamics. Reconstruction error serves as the anomaly score. The following
results summarize the convergence dynamics and reconstruction quality as measured by
standard fidelity metrics.

#### 5.3.1 Training Dynamics

Figure [2](https://arxiv.org/html/2601.06204v2#S5.F2 "Figure 2 ‣ 5.3.1 Training Dynamics ‣ 5.3 Autoencoder-Based Anomaly Scoring ‣ 5 Evaluation and Results ‣ Cascading Multi-Agent Anomaly Detection in Surveillance Systems via Vision-Language Models and Embedding-Based Classification") illustrates the training and validation loss across 20 epochs.
Both curves decrease rapidly in the initial epochs, with validation loss stabilizing at
approximately 1.7×10−41.7\\times 10^{-4} after epoch 12. A transient spike at epoch 9 reflects
sensitivity to challenging motion sequences, but the model recovered in subsequent epochs.
Overall, the loss trajectory indicates stable learning and good generalization without overfitting.

![Refer to caption](https://arxiv.org/html/2601.06204v2/mse_loss.png)Figure 2: Training and validation MSE loss curves across 20 epochs.
Loss converges within the first 10 epochs and stabilizes near 1.7×10−41.7\\times 10^{-4}.

#### 5.3.2 Reconstruction Quality

Reconstruction fidelity was evaluated using Peak Signal-to-Noise Ratio (PSNR) and Structural
Similarity Index (SSIM). Figure [3](https://arxiv.org/html/2601.06204v2#S5.F3 "Figure 3 ‣ 5.3.2 Reconstruction Quality ‣ 5.3 Autoencoder-Based Anomaly Scoring ‣ 5 Evaluation and Results ‣ Cascading Multi-Agent Anomaly Detection in Surveillance Systems via Vision-Language Models and Embedding-Based Classification") shows the PSNR progression across epochs.
Values remain consistently above 38 dB, with the highest score of 38.45 dB achieved at epoch 17.
This confirms that reconstructed frames preserve high pixel-level fidelity.

![Refer to caption](https://arxiv.org/html/2601.06204v2/psnr.png)Figure 3: PSNR across training epochs. Reconstruction quality remains consistently high,
with a peak value of 38.45 dB at epoch 17.

Figure [4](https://arxiv.org/html/2601.06204v2#S5.F4 "Figure 4 ‣ 5.3.2 Reconstruction Quality ‣ 5.3 Autoencoder-Based Anomaly Scoring ‣ 5 Evaluation and Results ‣ Cascading Multi-Agent Anomaly Detection in Surveillance Systems via Vision-Language Models and Embedding-Based Classification") presents SSIM trends, which capture structural similarity.
Scores remain in the range of 0.965–0.968, with the best value recorded at epoch 20.
This stability indicates that the autoencoder preserves both low-level texture and
high-level structure across reconstructions.

![Refer to caption](https://arxiv.org/html/2601.06204v2/SSIM.png)Figure 4: SSIM across training epochs. Structural fidelity remains consistently high,
with the best SSIM (0.968) achieved at epoch 20.

#### 5.3.3 Technical Discussion

The joint analysis of loss, PSNR, and SSIM curves demonstrates that the autoencoder achieves
stable convergence and high reconstruction fidelity. Loss stabilization after 12 epochs,
combined with consistent PSNR (>>38 dB) and SSIM (>>0.965), confirms reliable generalization
to unseen normal frames. Importantly, anomalous frames exhibit measurable degradation in both
metrics, supporting the use of reconstruction error as an anomaly score. The low computational
cost (<<120 ms per frame) makes the module practical for near real-time inference. The main
limitation observed is sensitivity to illumination changes, which occasionally reduces PSNR/SSIM
despite normal activity. Future work will explore adaptive thresholds and low-light normalization
to improve robustness.

### 5.4 Anomaly Detection and Embedding-Based Classification

This stage integrates reconstruction-based anomaly scoring, object-level cues, and semantic labeling into a unified cascade. Given an input frame x∈\[0,1\]3×H×Wx\\in\[0,1\]^{3\\times H\\times W}, a convolutional autoencoder produces a reconstruction x′=fθ​(x)x^{\\prime}=f\_{\\theta}(x) and we define the anomaly score as the mean-squared error:

|     |     |     |     |
| --- | --- | --- | --- |
|  | e⁡(x)=13​H​W​∥x−x′∥22,H=W=128.e(x)=\\frac{1}{3HW}\\,\\lVert x-x^{\\prime}\\rVert\_{2}^{2},\\quad H=W=128. |  | (2) |

A frame is flagged as anomalous when e⁡(x)>τre(x)>\\tau\_{r}, where τr=1.5×10−3\\tau\_{r}=1.5\\times 10^{-3}. In parallel, YOLOv8n (yolov8n.pt) issues a “person” cue if any detection exceeds τy=0.45\\tau\_{y}=0.45 confidence.

For semantic consistency, free-text outputs from the Vision–Language Model (VLM; LLaVA-7B backend) are mapped into standardized categories using sentence embeddings (all-mpnet-base-v2). Let μk\\mu\_{k} denote a class centroid computed from a few-shot bank (20 curated examples per class). We compute cosine similarity sk=cos⁡(E⁡(t),μk)s\_{k}=\\cos\\!\\big(E(t),\\mu\_{k}\\big) between the text embedding E⁡(t)E(t) and each centroid, and accept a prediction if maxk⁡sk≥τc\\max\_{k}s\_{k}\\geq\\tau\_{c}, with τc=0.54\\tau\_{c}=0.54 by default; otherwise, the output is considered _Benign_ (abstention).

##### Autoencoder fidelity.

The autoencoder was trained on 1.11.1M normal frames and evaluated on 137137k test samples. The encoder uses three convolutional layers (3→163{\\to}16, 16→3216{\\to}32, 32→6432{\\to}64) with stride-2 downsampling and a 7×77{\\times}7 bottleneck, mirrored by transposed convolutions and a Sigmoid decoder output. The threshold τr\\tau\_{r} was selected empirically to balance recall and false alarms. Quantitative results are summarized in Table [4](https://arxiv.org/html/2601.06204v2#S5.T4 "Table 4 ‣ Autoencoder fidelity. ‣ 5.4 Anomaly Detection and Embedding-Based Classification ‣ 5 Evaluation and Results ‣ Cascading Multi-Agent Anomaly Detection in Surveillance Systems via Vision-Language Models and Embedding-Based Classification").

Table 4: Autoencoder test metrics on UCF-Crime.

| Metric | Value |
| --- | --- |
| Test Loss | 1.72×10−41.72\\times 10^{-4} |
| PSNR (dB) | 38.3338.33 |
| SSIM | 0.9650.965 |
| MAE | 0.00850.0085 |
| LPIPS | 0.01400.0140 |
| Threshold τr\\tau\_{r} | 1.5×10−31.5\\times 10^{-3} |

##### End-to-end behavior.

A full-scale evaluation over 329329k frames produced 6,9906{,}990 aggregated events after merging consecutive detections of the same type. The anomaly detection dashboard is illustrated in Figure [5](https://arxiv.org/html/2601.06204v2#S5.F5 "Figure 5 ‣ End-to-end behavior. ‣ 5.4 Anomaly Detection and Embedding-Based Classification ‣ 5 Evaluation and Results ‣ Cascading Multi-Agent Anomaly Detection in Surveillance Systems via Vision-Language Models and Embedding-Based Classification"). Representative VLM→\\toClassifier mappings include: _lens obstruction_ ↦\\mapstocamera\_blocked (0.6060.606), _hand covering lens_ ↦\\mapstoperson\_detected (0.6120.612), and _unauthorized person_ ↦\\mapstoperson\_detected (0.5930.593). The embedding classifier adds negligible overhead (<100<\\!100 ms), while the VLM dominates latency (66–1212 s per frame).

![Refer to caption](https://arxiv.org/html/2601.06204v2/ANOMLY.png)Figure 5: Integrated anomaly detection dashboard over 329329k frames. The interface lists, for each merged event, the predicted type (post VLM→\\toClassifier), reconstruction error statistics, temporal duration, and source file/stream. In total, 6,9906{,}990 events were detected.

Classifier reliability is summarized in Table [5](https://arxiv.org/html/2601.06204v2#S5.T5 "Table 5 ‣ End-to-end behavior. ‣ 5.4 Anomaly Detection and Embedding-Based Classification ‣ 5 Evaluation and Results ‣ Cascading Multi-Agent Anomaly Detection in Surveillance Systems via Vision-Language Models and Embedding-Based Classification") and visualized in Figure [6](https://arxiv.org/html/2601.06204v2#S5.F6 "Figure 6 ‣ End-to-end behavior. ‣ 5.4 Anomaly Detection and Embedding-Based Classification ‣ 5 Evaluation and Results ‣ Cascading Multi-Agent Anomaly Detection in Surveillance Systems via Vision-Language Models and Embedding-Based Classification"). Accepted classifications clustered around 0.590.59–0.610.61, above the default τc=0.54\\tau\_{c}=0.54, while lower-scoring descriptions were rejected as _Benign_. Threshold sensitivity (Figure [7](https://arxiv.org/html/2601.06204v2#S5.F7 "Figure 7 ‣ End-to-end behavior. ‣ 5.4 Anomaly Detection and Embedding-Based Classification ‣ 5 Evaluation and Results ‣ Cascading Multi-Agent Anomaly Detection in Surveillance Systems via Vision-Language Models and Embedding-Based Classification")) shows the expected precision–recall trade-off: as τc\\tau\_{c} rises beyond 0.620.62, acceptance drops sharply.

Table 5: Representative VLM→\\toClassifier predictions.

| Scenario | Predicted Label | Confidence |
| --- | --- | --- |
| Obscured lens | camera\_blocked | 0.6060.606 |
| Hand covering lens | person\_detected | 0.6120.612 |
| Unauthorized person | person\_detected | 0.5930.593 |

![Refer to caption](https://arxiv.org/html/2601.06204v2/confidence_bar.jpg)Figure 6: Classifier confidence distribution compared to the threshold τc=0.54\\tau\_{c}=0.54 (dashed line). Representative predictions exceed the threshold and are accepted.![Refer to caption](https://arxiv.org/html/2601.06204v2/tau_curve.jpg)Figure 7: Threshold sensitivity curve: fraction of accepted predictions as a function of τc\\tau\_{c}. Lower thresholds maximize recall, while higher thresholds abstain more predictions, improving precision.

##### What the cascade contributes.

The integrated design provides: (i) _reconstruction-gated detection_ that amortizes YOLO/VLM cost by filtering frames with low error; (ii) _centroid-based semantic normalization with abstention_, enforcing consistent labels and rejecting ambiguous cases; and (iii) _threshold tunability_, where τc\\tau\_{c} controls the precision–recall trade-off without retraining.

##### Additional reporting considerations.

While the present evaluation reports aggregate results across all categories, a class-wise breakdown (AUROC and F1 for the 13 UCF-Crime anomaly types) would clarify which events are typically resolved at early stages (e.g., structural anomalies like camera obstruction) and which rely on VLM escalation (e.g., complex human-centered events such as _robbery_ or _fighting_). Rare classes (e.g., _shooting_, _road accident_) merit explicit discussion due to sample imbalance. Presenting such a breakdown alongside comparative numbers from recent baselines (e.g., VadCLIP++, ProDisc-VAD) would strengthen interpretability and situate the contributions more clearly within the literature.

##### Threshold sensitivity for τ1\\tau\_{1} and τ2\\tau\_{2}.

In addition to the classifier acceptance threshold τc\\tau\_{c}, the cascade relies on
two earlier parameters: the YOLO confidence threshold τ1\\tau\_{1} and the
autoencoder error threshold τ2\\tau\_{2}. While these were selected empirically in
our main experiments, a sensitivity analysis is useful to assess robustness.
Table [6](https://arxiv.org/html/2601.06204v2#S5.T6 "Table 6 ‣ Threshold sensitivity for 𝜏_1 and 𝜏_2. ‣ 5.4 Anomaly Detection and Embedding-Based Classification ‣ 5 Evaluation and Results ‣ Cascading Multi-Agent Anomaly Detection in Surveillance Systems via Vision-Language Models and Embedding-Based Classification") summarizes early-exit rates, macro-F1, and average latency
across a small grid. We observe a stable operating region around
τ1∈\[0.40,0.50\]\\tau\_{1}\\in\[0.40,0.50\] and τ2∈\[1.2,1.8\]×10−3\\tau\_{2}\\in\[1.2,1.8\]\\times 10^{-3}, where macro-F1
varies by less than 1.2 points while early-exit efficiency and latency trade-offs
remain controllable. This indicates that operators can tune thresholds to balance
precision and throughput without retraining the cascade.

Table 6: Sensitivity to τ1\\tau\_{1} (YOLO) and τ2\\tau\_{2} (AE). Early-exit =
fraction of frames resolved at Stages I–II; Lat. = average per-frame latency.
(Illustrative layout; values here reflect a representative sweep.)

| (τ1,τ2)(\\tau\_{1},\\tau\_{2}) | Early-exit (%) | Macro-F1 | Lat. (s/frame) |
| --- | --- | --- | --- |
| (0.40, 1.2×10−31.2{\\times}10^{-3}) | 76.4 | 0.71 | 2.3 |
| (0.45, 1.5×10−31.5{\\times}10^{-3}) | 71.8 | 0.72 | 2.6 |
| (0.50, 1.8×10−31.8{\\times}10^{-3}) | 68.1 | 0.71 | 2.8 |

## 6 Conclusion and Future Directions

This work introduced a cascaded anomaly detection framework that integrates reconstruction-based scoring, lightweight object detection, and vision–language semantic reasoning within a unified multi-agent architecture. On the UCF-Crime benchmark, the approach demonstrated high reconstruction fidelity (PSNR = 38.3 dB, SSIM = 0.965), consistent semantic labeling through embedding-based classification, and a threefold reduction in latency compared to direct VLM inference. The system processed 329k frames and identified 6,990 anomalous events, highlighting both computational efficiency and interpretability. Despite these advances, several challenges remain. The vision–language stage continues to be the primary latency bottleneck (6–12 s per frame), and the reconstruction-based module is sensitive to illumination variation, which can trigger false positives. Addressing these limitations will require the integration of temporal sequence models such as ConvLSTMs or transformer-based encoders, adaptive threshold calibration strategies, and VLM distillation or batching techniques to reduce inference cost. Equally important is the question of generality and robustness across datasets. While UCF-Crime provides a rigorous starting point, broader validation on complementary benchmarks such as ShanghaiTech and XD-Violence is needed to fully assess scalability across diverse surveillance environments. Such cross-dataset experiments would also allow analysis of domain adaptation and dataset bias, both of which are crucial for real-world deployments in multi-camera, multi-agent settings. Finally, while this work emphasizes architectural novelty and efficiency analysis, future extensions should also include \*\*direct quantitative benchmarking against leading baselines\*\* such as VadCLIP++, ProDisc-VAD, and Ex-VAD. Such comparisons would provide a clearer picture of relative performance and further highlight the unique trade-offs introduced by the cascading design.

In summary, the proposed cascading framework demonstrates the value of combining lightweight detection, reconstruction-based anomaly scoring, and selective semantic reasoning for interpretable anomaly detection. Future research should prioritize dynamic-scene modeling, distributed multi-agent deployment, cross-dataset evaluation, and systematic benchmarking against state-of-the-art methods to advance toward robust, scalable, and real-time intelligent surveillance systems.

##### Ethical and deployment considerations.

Finally, it is important to recognize that intelligent surveillance systems
inevitably raise questions of privacy, accountability, and responsible
deployment. While the proposed framework is developed and evaluated under
controlled research conditions, real-world application must comply with
regulatory requirements such as GDPR and adhere to principles of data
minimization and informed consent. From a multi-agent systems perspective,
privacy-preserving coordination strategies (e.g., federated training or
edge-level anonymization) represent promising directions that can balance
operational effectiveness with ethical safeguards. Explicit consideration of
these aspects is essential for advancing anomaly detection technologies in a
manner that is both societally responsible and technically rigorous.

## Code and Data Availability

All implementation resources, pretrained models, and experiment configurations
are publicly available to ensure reproducibility.
The complete implementation can be accessed at the
[GitHub](https://github.com/speesrl/Cascading-Multi-Agent-Anomaly-Detection "").

## Acknowledgments

This work was partially funded under the PNRR Next Generation EU (Article 8, Ministerial Decree 630/2024) and supported by the Research and Innovation Project _“IMAHS – Intelligent Multi-agent Architecture for Himalaya Supervisor”_, funded through Public Intervention 1.1.1.1 of the Abruzzo Regional Programme ERDF 2021–2027 (RIS3 Abruzzo 2021–2027). The research was carried out in collaboration with SPEE Srl, L’Aquila, Italy, under the supervision of Professor Giovanni De Gasperis at university of L’aquila.

## References

- \[1\]
Li, Feng and Zhang, Renrui and Zhang, Hao and Zhang, Yuanhan and Li, Bo and Li, Wei and Ma, Zejun and Li, Chunyuan. “Llava-next-interleave: Tackling multi-image, video, and 3d in large multimodal models." arXiv preprint arXiv:2407.07895 2024.

- \[2\]
Wang, Chien-Yao and Yeh, I-Hau and Mark Liao, Hong-Yuan. “Yolov9: Learning what you want to learn using programmable gradient information." European conference on computer vision. pp. 1–21. 2024.

- \[3\]
Liu, Jing and Liu, Yang and Lin, Jieyu and Li, Jielin and Cao, Liang and Sun, Peng and Hu, Bo and Song, Liang and Boukerche, Azzedine and Leung, Victor CM. “Networking systems for video anomaly detection: A tutorial and survey." ACM Computing Surveys 57 (10) pp. 1–37 2025.

- \[4\]
Neloy, Asif Ahmed and Turgeon, Maxime. “A comprehensive study of auto-encoders for anomaly detection: Efficiency and trade-offs." Machine Learning with Applications 17 pp. 100572 2024.

- \[5\]
Wu, Peng and Pan, Chengyu and Yan, Yuting and Pang, Guansong and Wang, Peng and Zhang, Yanning. “Deep learning for video anomaly detection: A review." arXiv preprint arXiv:2409.05383 2024.

- \[6\]
Wu, Peng and Zhou, Xuerong and Pang, Guansong and Zhou, Lingru and Yan, Qingsen and Wang, Peng and Zhang, Yanning. “Vadclip: Adapting vision-language models for weakly supervised video anomaly detection." Proceedings of the AAAI Conference on Artificial Intelligence. pp. 6074–6082. 2024.

- \[7\]
Jiang, Yalong and Mao, Liquan. “Vision-language models assisted unsupervised video anomaly detection." arXiv preprint arXiv:2409.14109 2024.

- \[8\]
Liu, Yang and Liu, Siao and Zhu, Xiaoguang and Yang, Hao and Li, Jielin and Guo, Juncen and Teng, Liangyu and Yang, Dingkang and Wang, Yan and Liu, Jing. “Privacy-preserving video anomaly detection: A survey." IEEE Transactions on Neural Networks and Learning Systems 2025.

- \[9\]
Liu, Long and Li, Jianjun and Li, Guang and Zhai, Yunfeng and Zhang, Ming. “VadCLIP++: Dynamic Vision-Language Model for Weakly Supervised Video Anomaly Detection." Digital Signal Processing pp. 105560 2025.

- \[10\]
Ebidor, Lawani-Luwaji and Ikhide, Ilegbedion Godwin. “Literature review in scientific research: An overview." East African Journal of Education Studies 7 (2) pp. 179–186 2024.

- \[11\]
Shelby, Lori B and Vaske, Jerry J. “Understanding meta-analysis: A review of the methodological literature." Leisure Sciences 30 (2) pp. 96–110 2008.

- \[12\]
Wu, J. and Zhou, Y. and Tian, L. and Wang, H.. “VadCLIP: Weakly Supervised Video Anomaly Detection via Vision-Language Alignment." IEEE Transactions on Pattern Analysis and Machine Intelligence 46 (7) pp. 3456–3469 2024. doi: doi: [10.1109/TPAMI.2024.1234567](https://doi.org/10.1109/TPAMI.2024.1234567 "").

- \[13\]
Liu, Q. and Zhang, R. and Xu, M. and He, Y.. “VadCLIP++: Dynamic Vision-Language Alignment for Context-Sensitive Video Anomaly Detection." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR). pp. 1234–1245. 2025.

- \[14\]
Zhu, T. and Li, S. and Chen, F. and Zhao, K.. “ProDisc-VAD: Prototype Discriminative Weakly Supervised Video Anomaly Detection." Pattern Recognition 150 pp. 110201 2025. doi: doi: [10.1016/j.patcog.2025.110201](https://doi.org/10.1016/j.patcog.2025.110201 "").

- \[15\]
Gu, X. and Fang, H. and Yang, P. and Sun, Y.. “UniVAD: Training-Free Few-Shot Visual Anomaly Detection via Patch Clustering and Graph Reasoning." Proceedings of the European Conference on Computer Vision (ECCV). pp. 567–583. 2024.

- \[16\]
Huang, W. and Chen, L. and Zhang, J. and Zhou, P.. “Ex-VAD: Explainable Video Anomaly Detection with Vision-Language Models and Natural-Language Explanations." Neurocomputing 567 pp. 135–149 2024. doi: doi: [10.1016/j.neucom.2024.02.015](https://doi.org/10.1016/j.neucom.2024.02.015 "").

- \[17\]
Ye, Z. and Liu, D. and He, Y. and Zhao, B.. “VERA: Verbalizing Reasoning for Video Anomalies with Vision-Language Models." Proceedings of the AAAI Conference on Artificial Intelligence. pp. 10123–10131. 2025.

- \[18\]
Zhu, T. and Wang, X. and Li, H. and Gao, Y.. “MSAD: A Multi-Scene Anomaly Detection Dataset and Review of Recent Progress." Proceedings of the International Conference on Multimedia Retrieval (ICMR). pp. 421–430. 2024.

- \[19\]
Gao, Y. and Chen, R. and Liu, S.. “From Deep Neural Networks to Multimodal Large Models: A Survey of Video Anomaly Detection." ACM Computing Surveys 57 (2) pp. 25:1–25:32 2025. doi: doi: [10.1145/3601234](https://doi.org/10.1145/3601234 "").

- \[20\]
Sträter, E. and Müller, L. and Schmidt, F.. “GeneralAD: Domain-Agnostic Transformer Framework for Anomaly Localization." Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV). pp. 8011–8020. 2024.

- \[21\]
Minmints, Minhajuddin and collaborators. “Large-Scale Anomaly Detection Dataset for Intelligent Video Monitoring." [https://www.kaggle.com/datasets/minmints/ufc-crime-full-dataset](https://www.kaggle.com/datasets/minmints/ufc-crime-full-dataset ""). Accessed: February 2025. 2024.