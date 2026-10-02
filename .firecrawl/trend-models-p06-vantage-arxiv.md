Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2609.09396v1 \[cs.CV\] 08 Sep 2026

\\authornotes

∗Equal contribution. †Project lead. Correspondence: zbhat@nvidia.com.
\\paperurlhttps://vantage-bench.org/

# VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models

Zaid Pervaiz Bhat
Nimra Nayyar
Affiliation: NVIDIA  Clemson University
Arihant Jain
Lap Fung Chan
Affiliation: NVIDIA  Clemson University
John Suchanek
Affiliation: NVIDIA  Clemson University
Yu Wang
Varun Praveen
Tomasz Kornuta
Vidya Nariyambut Murali

###### Abstract

As Vision-Language Models (VLMs) rapidly advance toward physical deployment, the predominant focus has remained on action-oriented Embodied AI evaluated on subject-centric consumer video. This trajectory overlooks a pervasive class of Physical AI: _Infrastructure AI_, which relies on fixed-infrastructure cameras for open-loop insights like safety monitoring and operational logging. How well VLMs process dense, fixed-camera visual data remains insufficiently explored. We introduce VANTAGE-Bench, an evaluation benchmark that measures this “Infrastructure AI Gap,” distinguished by four features: 1) Domain Relevance, spanning three operational environments (Logistics, Transportation, and Smart Spaces); 2) Modality Breadth, unifying image and video evaluation to probe semantic, spatial, temporal, and spatio-temporal capabilities; 3) Task Format Diversity, moving beyond multiple-choice to eight task formulations spanning discriminative QA, generative dense captioning, and spatio-temporal grounding; and 4) Evaluation Novelty, a single-pass trajectory-generation protocol for Single Object Tracking and, to our knowledge, the first such evaluation on fixed-camera infrastructure video, scored against specialist trackers. Annotation spans three regimes over 3,346 expert-annotated media assets: video tasks (3,342 annotations over 854 videos), image grounding (4,281 over 1,864 images), and dense detection (27,404 boxes over 628 images).

Evaluating 17 models zero-shot, we find the shortfall relative to consumer-centric benchmarks is concentrated rather than general. Event verification, referring expressions, and temporal localization fall roughly 9 to 24 points at every model scale, while video question answering stays within 5.3 points of VideoMME and 2D spatial pointing shows no shortfall against BLINK. The temporal pillar is weakest in absolute terms: no system exceeds 55.7 mIoU on temporal localization or 37.3 SODAc on dense video captioning. On tracking, frontier models come within roughly 5 points of specialist trackers over short horizons but separate as the horizon extends. Open-weight models lead 2D object localization outright, so neither parameter count nor proprietary access accounts for the pattern. The dataset is available at [https://huggingface.co/datasets/nvidia/PhysicalAI-VANTAGE-Bench](https://huggingface.co/datasets/nvidia/PhysicalAI-VANTAGE-Bench ""), and the evaluation harness and public leaderboard at [https://vantage-bench.org/](https://vantage-bench.org/ "").

\\abscontent

## 1 Introduction

As VLMs rapidly advance toward physical deployment, the prevailing research trajectory has heavily indexed on action-oriented Embodied AI and evaluations grounded in subject-centric consumer video (e.g., egocentric recordings, broadcast media). This focus overlooks a pervasive and foundational class of physical AI: _Infrastructure AI_. Relying on fixed-infrastructure cameras (e.g., CCTV, elevated sensors), Infrastructure AI provides open-loop insights for safety monitoring, operational logging, and large-scale spatial reasoning. Because frontier models are predominantly trained on internet-crawled data, they are biased toward standard photographic perspectives. Consequently, their capability to process the dense, oblique, and multi-agent visual data inherent to fixed-camera environments remains insufficiently evaluated, creating a severe implicit domain shift.

Under these conditions, the “internet-video prior” fails, and models must rely on pure spatial-temporal logic. A model can achieve state-of-the-art scores on internet video and still perform poorly in the environments where these systems are actually deployed. We term this the _Infrastructure AI Gap_: the discrepancy between a model’s performance on general video benchmarks and its reliability as an insight-generating system in dense, fixed-camera infrastructure environments. Closing this gap requires evaluation frameworks designed natively for operational reality. While comprehensive suites like VideoMME \[ [1](https://arxiv.org/html/2609.09396#bib.bib1 "")\] and MVBench \[ [2](https://arxiv.org/html/2609.09396#bib.bib2 "")\] evaluate multiple reasoning dimensions, they ultimately reduce evaluation to a single format: MCQ. MCQ evaluation provides the correct answer as an implicit prior and fails to test if a model can autonomously generate bounding box coordinates or predict explicit temporal boundaries.

To systematically measure and close this capability deficit, we introduce VANTAGE-Bench (Video Analysis Tasks Across Generalized Environments). VANTAGE-Bench is the first multi-task benchmark specifically curated for Infrastructure AI, moving beyond single-format MCQ to evaluate eight distinct task formulations across four pillars of operational visual intelligence: Semantic, Spatial, Temporal, and Spatio-Temporal Understanding.

Finding: Our zero-shot evaluation of 17 models shows that the deficit is localized rather than uniform, and the asymmetry is what makes it interpretable. Measured against the same models’ published scores on consumer-centric benchmarks, event verification, referring expressions, and temporal localization drop at every scale, while video question answering holds within 5.3 points of VideoMME \[ [1](https://arxiv.org/html/2609.09396#bib.bib1 "")\] and 2D spatial pointing shows a surplus of 8.3 points against BLINK \[ [4](https://arxiv.org/html/2609.09396#bib.bib4 "")\] at 32B. The same models therefore lose ground on some capabilities and gain it on others within one suite, which places the shortfall in specific capabilities rather than in overall difficulty. Section [4](https://arxiv.org/html/2609.09396#S4 "4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") tightens this with a prompt- and metric-matched control, and shows that models carrying more physical-AI training data gain 14 to 26 points on tracking and object localization while the two temporal tasks stay nearly untouched — an asymmetry we trace to the scarcity of densely timestamped video supervision rather than to a general weakness in video understanding. Those two tasks remain the weakest in absolute terms across the entire suite, at frontier scale as much as at 2B.

Our main contributions are:

1. 1.


VANTAGE-Bench: The first multi-task benchmark specifically curated for Infrastructure AI, spanning three deployment domains – Logistics/Warehouse, Transportation, and Smart Spaces – addressing the structural distribution shift from egocentric video.

2. 2.


Format-Diverse Evaluation: Eight task formulations spanning discriminative QA, generative dense captioning, and spatio-temporal grounding. Five of the eight require the model to emit bounding boxes, temporal boundaries, or a full trajectory with no candidate set supplied, removing the implicit answer prior that MCQ evaluation provides; only two are multiple-choice and one binary.

3. 3.


Tracking Protocol: A single-pass trajectory-generation protocol for Single Object Tracking (SOT) in VLMs and, to our knowledge, the first such evaluation on fixed-camera infrastructure video spanning open-weight and proprietary models, reported against specialist-tracker, static-box, and random baselines.

4. 4.


Expert-Annotated Dataset: 3,346 media assets across three annotation regimes: 3,342 video-task annotations over 854 videos, 4,281 image-grounding annotations over 1,864 images, and 27,404 detection boxes over 628 images. Annotation density is uneven across regimes by design, and we report the regimes separately rather than as a single aggregate.

5. 5.


Open Evaluation Ecosystem: An open-source evaluation suite and a live public leaderboard with held-out ground truth (Appendix [F.3](https://arxiv.org/html/2609.09396#A6.SS3 "F.3 Code, Data Access, and Release Strategy ‣ Appendix F Reproducibility and Experimental Configuration ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")).

6. 6.


Empirical Characterization: A 17-model zero-shot evaluation establishing that the gap is localized rather than uniform — event verification, referring expressions, and temporal localization fall roughly 9 to 24 points against the same models’ published scores, while video question answering and 2D spatial pointing do not — and that the two temporal tasks hold the lowest ceilings of the eight, unclosed at frontier scale.


## 2 Related Work

### 2.1 General Video Benchmarks and the MCQ Bottleneck

The dominant paradigm in VLM evaluation relies on general-purpose, multi-task benchmarks such as VideoMME \[ [1](https://arxiv.org/html/2609.09396#bib.bib1 "")\], MVBench \[ [2](https://arxiv.org/html/2609.09396#bib.bib2 "")\], and EgoSchema \[ [3](https://arxiv.org/html/2609.09396#bib.bib3 "")\]. While these comprehensive suites have driven substantial progress in general video understanding, their relevance to operational deployment is limited by two factors. First, they rely on a “cinematic prior”—utilizing web-sourced, broadcast, or egocentric footage characterized by high-velocity optical flow, human-centric framing, and edited temporal structures. Second, they suffer from the “MCQ Bottleneck.” By reducing complex spatio-temporal reasoning to MCQ, these benchmarks provide the correct answer as an implicit prior. This format does not test the open-ended generative capabilities—such as producing precise bounding box coordinates or explicit temporal boundaries—that autonomous Infrastructure AI requires to generate reliable downstream insights.

### 2.2 Embodied AI Datasets vs. Classical Surveillance

The physical AI community has developed extensive datasets for real-world deployment, but these efforts remain fragmented across two divides. First is the operational divide. Datasets like KITTI \[ [5](https://arxiv.org/html/2609.09396#bib.bib5 "")\], nuScenes \[ [6](https://arxiv.org/html/2609.09396#bib.bib6 "")\], and Waymo \[ [7](https://arxiv.org/html/2609.09396#bib.bib7 "")\] are optimized exclusively for Embodied AI—featuring moving cameras, low-latency requirements, and closed-loop perception. On the other side is classical surveillance, where datasets like UCF-Crime \[ [8](https://arxiv.org/html/2609.09396#bib.bib8 "")\] and VIRAT \[ [9](https://arxiv.org/html/2609.09396#bib.bib9 "")\] capture the correct fixed-infrastructure perspective, but rely on classical bounding boxes or binary anomaly labels without a natural language interface. Second is the domain divide. Existing enterprise datasets are strictly siloed—focusing solely on either transportation (e.g., AI City Challenge \[ [10](https://arxiv.org/html/2609.09396#bib.bib10 "")\]), generic crime (UCF-Crime), or robotic manipulation in logistics. VANTAGE-Bench bridges both divides simultaneously. It pairs the fixed-infrastructure perspective of classical surveillance corpora with a natural-language interface, and unifies evaluation across three distinct deployment domains: Transportation, Warehouse, and Smart Spaces. This multi-domain approach ensures models are evaluated on generalized physical reasoning rather than overfitted domain-specific priors.

### 2.3 Spatial and Temporal Grounding in Idealized Settings

Grounding language to spatial and temporal coordinates is a foundational requirement for physical AI, yet existing benchmarks evaluate these capabilities under highly idealized conditions. Spatial grounding and referring expression datasets like RefCOCO \[ [13](https://arxiv.org/html/2609.09396#bib.bib13 "")\] and BLINK utilize natural indoor and outdoor photography featuring well-lit, centered, and distinct objects. This fails to evaluate the dense, multi-instance disambiguation required when monitoring infrastructure from an elevated, oblique perspective (e.g., distinguishing between dozens of identical pallets or vehicles). Similarly, temporal grounding benchmarks like Charades-STA \[ [11](https://arxiv.org/html/2609.09396#bib.bib11 "")\] and ActivityNet Captions \[ [12](https://arxiv.org/html/2609.09396#bib.bib12 "")\] utilize scripted, continuous human actions where the event of interest dominates the video timeline. In contrast, operational video is characterized by long quiescent periods. VANTAGE-Bench forces models to search through extended periods of inactivity to localize brief, sparse, safety-critical events, which tests temporal attention and contextual recall more directly.

### 2.4 Spatio-Temporal Tracking and Grounding

Tracking objects continuously through dense scenes is among the most demanding spatio-temporal tasks. We position our Single Object Tracking track against four adjacent lines of work.

#### Classical tracking benchmarks.

LaSOT \[ [14](https://arxiv.org/html/2609.09396#bib.bib14 "")\], GOT-10k \[ [15](https://arxiv.org/html/2609.09396#bib.bib15 "")\], and MOTChallenge \[ [16](https://arxiv.org/html/2609.09396#bib.bib16 "")\] were designed to evaluate dedicated computer vision pipelines that maintain an explicit internal state (e.g., appearance models, motion priors, and frame-by-frame memory updates). We evaluate four specialist trackers—SAM 3 \[ [25](https://arxiv.org/html/2609.09396#bib.bib25 "")\], SAMURAI \[ [26](https://arxiv.org/html/2609.09396#bib.bib26 "")\], SUTrack \[ [27](https://arxiv.org/html/2609.09396#bib.bib27 "")\], and MCITrack \[ [28](https://arxiv.org/html/2609.09396#bib.bib28 "")\]—as anchors on our own tracking annotations: they reach approximately 80 Success AUC on the same tracklets and scorer, establishing the level a purpose-built system attains and giving the VLM scores a reference point (Appendix [D](https://arxiv.org/html/2609.09396#A4 "Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")).

#### Language-conditioned tracking.

TNL2K \[ [17](https://arxiv.org/html/2609.09396#bib.bib17 "")\] evaluates iterative language-conditioned tracking by dedicated architectures, whereas our protocol is single-pass trajectory generation by a general-purpose VLM from a visual first-frame box. SOT removes language in order to isolate visual correspondence over time.

#### Joint spatio-temporal grounding.

VidSTG \[ [18](https://arxiv.org/html/2609.09396#bib.bib18 "")\] and HC-STVG \[ [19](https://arxiv.org/html/2609.09396#bib.bib19 "")\] evaluate joint spatio-temporal grounding, where one score conflates language grounding, spatial localization, and temporal localization. Our pillar design decomposes exactly these: 2D Referring Expressions isolates language to space, Temporal Localization isolates language to time, and SOT removes language to isolate visual correspondence over time.

#### Tracking with multimodal language models.

Elysium \[ [20](https://arxiv.org/html/2609.09396#bib.bib20 "")\] and Merlin \[ [21](https://arxiv.org/html/2609.09396#bib.bib21 "")\] are purpose-trained tracking MLLMs. VideoChat-R1 \[ [23](https://arxiv.org/html/2609.09396#bib.bib23 "")\] and R1-Track \[ [24](https://arxiv.org/html/2609.09396#bib.bib24 "")\] address zero-shot box-initialized tracking of open VLMs. MMT-Bench \[ [22](https://arxiv.org/html/2609.09396#bib.bib22 "")\] evaluates tracking as multiple-choice box selection, the format limitation our protocol moves past.

#### Our protocol.

The model is initialized with the target object’s bounding box visually overlaid on the first frame. Through a single instruction, it then processes the subsequent multi-frame sequence and outputs a continuous coordinate trajectory, without rolling memory updates. We therefore describe our contribution as a single-pass trajectory-generation tracking protocol for VLMs and, to our knowledge, the first such evaluation on fixed-camera infrastructure video, spanning open-weight and proprietary models.

![Refer to caption](https://arxiv.org/html/2609.09396v1/dataset_overview.png)Figure 1: Taxonomy and distribution of VANTAGE-Bench. The benchmark spans three operational domains (W: Warehouse, T: Transportation, and SS: Smart Spaces), evaluating eight distinct tasks across Semantic, Spatial, Temporal, and Spatio-Temporal pillars. In total, the dataset comprises 3,346 media assets across three annotation regimes: 3,342 video-task annotations, 4,281 image-grounding annotations, and 27,404 detection boxes.

## 3 Dataset and Benchmark Construction

To construct a benchmark capable of testing the Infrastructure AI gap, we curated a multi-modal dataset combining expert-annotated real-world infrastructure footage with a limited set of high-fidelity simulated environments. The dataset is overwhelmingly human-labeled. Automated procedures are used to structure and scale one task format, 2D Spatial Pointing, where the question and its correct answer are both derived deterministically from human-labeled box coordinates (Section [3.4](https://arxiv.org/html/2609.09396#S3.SS4 "3.4 Programmatic Task Generation via Pseudo-Labeling ‣ 3 Dataset and Benchmark Construction ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). VANTAGE-Bench comprises 3,346 media assets across eight tasks (see Figure [1](https://arxiv.org/html/2609.09396#S2.F1 "Figure 1 ‣ Our protocol. ‣ 2.4 Spatio-Temporal Tracking and Grounding ‣ 2 Related Work ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). The video tasks and 2D Object Localization draw on fixed-infrastructure cameras: static, elevated, wide-angle viewpoints at mounting heights of 8 to 20 feet and viewing angles of 30 to 60 degrees from vertical, including low-light, night, and rain conditions. These are highway ITS and warehouse installations. The two remaining image tracks sample different geometries: 2D Referring Expressions uses oblique aerial views from RefDrone \[ [29](https://arxiv.org/html/2609.09396#bib.bib29 "")\], and 2D Spatial Pointing is derived from object-localization boxes over vehicle-mounted footage. Single Object Tracking uses synthetic elevated-fixed warehouse sequences from PhysicalAI-SmartSpaces \[ [30](https://arxiv.org/html/2609.09396#bib.bib30 "")\]. To support diverse physical reasoning, approximately 20% of the Video Question Answering and Temporal Localization splits feature high-fidelity synthetic simulations. VANTAGE-Bench is publicly released under the NVIDIA Evaluation Data License, which strictly restricts dataset usage to evaluation and benchmarking purposes, available at [https://huggingface.co/datasets/nvidia/PhysicalAI-VANTAGE-Bench](https://huggingface.co/datasets/nvidia/PhysicalAI-VANTAGE-Bench "").

### 3.1 Design Motivation

The architecture of VANTAGE-Bench is driven by the disconnect between how VLMs are currently evaluated and how Infrastructure AI operates in production. Existing video benchmarks inadvertently provide models with two strong priors: the “cinematic prior” of dynamic, human-centric framing, and the implicit hints embedded within MCQ formats. To evaluate physical grounding, we constructed VANTAGE-Bench around three core design principles:

- •


Ecological Validity: We strip away internet-video biases by drawing the video tasks and 2D Object Localization from static, elevated, wide-angle infrastructure cameras; the remaining image tracks sample other operational geometries. This forces models to disambiguate dense, multi-instance scenes without the aid of tracking shots or ideal lighting.

- •


Format Authenticity: By moving beyond the MCQ bottleneck, we evaluate autonomous insight generation. VANTAGE-Bench requires models to predict exact temporal boundaries, 2D coordinates, and continuous spatio-temporal trajectories.

- •


Dimensional Isolation: We design specialized task tracks to independently evaluate Semantic, Spatial, Temporal, and Spatio-Temporal intelligence, allowing researchers to isolate the exact locus of model failure.


![Refer to caption](https://arxiv.org/html/2609.09396v1/task_visualize.png)Figure 2: Visual examples of the eight evaluation tasks in VANTAGE-Bench, categorized by their primary reasoning pillar: Semantic, Spatial, Temporal, and Spatio-Temporal Understanding.

### 3.2 Task Taxonomy

We organize VANTAGE-Bench around four reasoning pillars, evaluating the distinct functional capabilities required for reliable Infrastructure AI. High-level descriptions are provided below, with formal mathematical formulations and evaluation metrics detailed in Appendix [B](https://arxiv.org/html/2609.09396#A2 "Appendix B Formal Task Formulations and Evaluation Metrics ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

#### Pillar I: Semantic Understanding.

This pillar evaluates high-level causal logic and operational reasoning via: (1) Event Verification (EV), which requires models to verify operational hypotheses against visual evidence, and (2) Video Question Answering (VQA), which tests multi-step logical reasoning over untrimmed sequences.

#### Pillar II: Spatial Understanding.

This pillar evaluates precise geometric grounding within infrastructure scenes through: (3) 2D Referring Expressions (RefEx), requiring dense semantic disambiguation to localize targets; (4) 2D Spatial Pointing, evaluating coordinate selection from positional prompts; and (5) 2D Object Localization, establishing a baseline for class-level spatial awareness.

#### Pillar III: Temporal Understanding.

This pillar focuses on perceiving action duration and sequence boundaries using: (6) Temporal Localization, requiring exact start/end timestamp prediction; and (7) Dense Video Captioning (DVC), a generative task for autonomous localization and description of chronological events.

#### Pillar IV: Spatio-Temporal Understanding.

This pillar evaluates continuous visual persistence through: (8) Single Object Tracking (SOT). Unlike standard VLM tasks, SOT requires predicting a target’s coordinate trajectory across a full sequence, testing the maintenance of spatial context over time.

### 3.3 Source Data and Expert Human Annotation

The core footage for VANTAGE-Bench was curated by NVIDIA to capture hard to source fixed-camera infrastructure perspectives. Real-world footage originates from two U.S. municipalities, San Francisco, CA and Dubuque, IA, supplemented by publicly sourced footage including European footage under license. Consent provenance and the PII obfuscation and verification pipeline are detailed in Appendix [E](https://arxiv.org/html/2609.09396#A5 "Appendix E De-identification Pipeline ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"). Annotations were generated by trained professionals—not crowdsourced—using domain-specific rulebooks. Annotators train for months, only the top 10% of the pool work on benchmark data, and per-task rulebooks are stabilized over up to two months before production. Our quality pipeline uses a multi-tier validation structure: 100% of initial annotations undergo a second-expert review, with a measured 98% first-pass acceptance (a 2% correction rate) and 99.43% acceptance after revision. A third-tier QA expert then audits a random 10% subset for consistency across spatial, temporal, and semantic boundaries.

### 3.4 Programmatic Task Generation via Pseudo-Labeling

To scale the evaluation of fine-grained spatial reasoning, the Pointing Data Engine converts human-labeled object-localization boxes over vehicle-mounted footage into 2D Spatial Pointing tasks. Both the question and its answer are generated programmatically from KITTI-style labels: the question from a template over relative distances between box coordinates, the correct option deterministically from the same geometry. A VLM is invoked only afterwards, to rewrite the templated question in more natural language; it cannot change which option is correct. Anchoring every pair to human-verified coordinates keeps the answer key tied to expert annotation at scale, and same-class distractors keep the multiple choice difficult.

### 3.5 Adaptation of Public and Synthetic Tracks

To supplement our proprietary real-world data, we selectively adapted highly relevant public and synthetic sources for specific spatial reasoning tasks. For 2D Referring Expressions (RefEx), we integrated images from the RefDrone dataset \[ [29](https://arxiv.org/html/2609.09396#bib.bib29 "")\], leveraging its dense, oblique aerial perspectives to test language-grounded object disambiguation. These queries are human-authored; the programmatic rewriting described in Section [3.4](https://arxiv.org/html/2609.09396#S3.SS4 "3.4 Programmatic Task Generation via Pseudo-Labeling ‣ 3 Dataset and Benchmark Construction ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") applies only to 2D Spatial Pointing. For SOT, we adapted high-fidelity synthetic logistics sequences from the NVIDIA PhysicalAI-SmartSpaces collection \[ [30](https://arxiv.org/html/2609.09396#bib.bib30 "")\], specifically targeting multi-camera warehouse environments. These sequences were reformatted into our VLM-native, single-pass \[x,y,w,h\]\[x,y,w,h\] coordinate prediction protocol. Full details regarding sequence filtering, data reformatting, and temporal sampling densities are provided in Appendix [C](https://arxiv.org/html/2609.09396#A3 "Appendix C Pipeline Details and Data Adaptation ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

### 3.6 Safely Simulating Severe Anomalies

A fundamental challenge in Infrastructure AI is evaluating safety-critical anomalies (e.g., collisions, industrial accidents) that are inherently rare and heavily restricted by privacy regulations. To evaluate these high-stakes scenarios without ethical compromise, approximately 20% of our VQA and Temporal splits utilize high-fidelity synthetic data generated using NVIDIA Omniverse DRIVE Sim \[ [36](https://arxiv.org/html/2609.09396#bib.bib36 "")\]. This ensures VANTAGE-Bench covers severe long-tail physical anomalies that are otherwise absent from purely real-world datasets.

Benchmark Scope.
Unlike prior datasets, which are typically restricted to a single modality or reasoning dimension, VANTAGE-Bench jointly evaluates semantic, spatial, temporal, and spatio-temporal reasoning across both image and video domains, and moves past MCQ-only evaluation to generative captioning and coordinate-based grounding. Appendix [A](https://arxiv.org/html/2609.09396#A1 "Appendix A Data Statistics and Benchmark Comparison ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") compares its scale and coverage against representative benchmarks.

## 4 Evaluation Framework and Empirical Results

To quantify the Infrastructure AI capability gap, we evaluate 17 VLMs on VANTAGE-Bench across the four pillars defined in Section [3.2](https://arxiv.org/html/2609.09396#S3.SS2 "3.2 Task Taxonomy ‣ 3 Dataset and Benchmark Construction ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

### 4.1 Experimental Setup

We evaluate 17 models spanning four vendors and 2B to frontier scale. Twelve are open-weight: Qwen3-VL at 2B, 8B, and 32B \[ [37](https://arxiv.org/html/2609.09396#bib.bib37 "")\]; Qwen3.5 at 9B and 27B \[ [43](https://arxiv.org/html/2609.09396#bib.bib43 "")\]; Cosmos-Reason2 at 2B, 8B, and 32B \[ [42](https://arxiv.org/html/2609.09396#bib.bib42 "")\]; Cosmos3 Edge, Nano, and Super \[ [38](https://arxiv.org/html/2609.09396#bib.bib38 "")\]; and Gemma-4-E2B \[ [39](https://arxiv.org/html/2609.09396#bib.bib39 "")\]. Five are proprietary: GPT-5.6 Sol \[ [40](https://arxiv.org/html/2609.09396#bib.bib40 "")\], Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, Gemini 3.1 Pro, and Gemini 3.1 Flash-Lite \[ [41](https://arxiv.org/html/2609.09396#bib.bib41 "")\]. Four of the open-weight families provide a scaling series, which we use in Section [4.4](https://arxiv.org/html/2609.09396#S4.SS4 "4.4 Returns to Scale and the Temporal Lag ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"). To test out-of-the-box physical reasoning and eliminate fine-tuning biases, all models were evaluated zero-shot. Inference and metric computation (e.g., Story-Oriented Dense Captioning (SODAc) \[ [34](https://arxiv.org/html/2609.09396#bib.bib34 "")\], temporal Intersection-over-Union (IoU), spatial trajectory parsing) were conducted using an extended version of the VLMEvalKit harness \[ [31](https://arxiv.org/html/2609.09396#bib.bib31 "")\] calibrated for VANTAGE-Bench tasks. Full details regarding our evaluation frameworks, custom metric scripts, and computational setup are provided in Appendix [F](https://arxiv.org/html/2609.09396#A6 "Appendix F Reproducibility and Experimental Configuration ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

### 4.2 Main Results

We analyze model performance across the four pillars of operational visual intelligence (Table [1](https://arxiv.org/html/2609.09396#S4.T1 "Table 1 ‣ 4.2 Main Results ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). Performance is uneven across pillars rather than uniformly low. Absolute scores are not directly comparable across tasks, since the metrics differ in what a perfect score demands; Section [4.3](https://arxiv.org/html/2609.09396#S4.SS3 "4.3 The Operational Deployment Gap (Δ) ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") therefore reads each task against an external reference measured the same way.

|  |  | Semantic | Spatial | Temporal | Sp.-Temp. |  |
| Model | Params | VQA | EV | Point. | RefEx | Obj Loc. | Temp Loc. | DVC | SOT | Overall |
|  |  | (Acc.) | (M-F1) | (Acc.) | (mIoU) | (F1@.5) | (mIoU) | (SODAc) | (AUC) |  |
| Open-weight models |
| Qwen3-VL | 2B | 63.85 | 44.73 | 53.13 | 65.12 | 47.42 | 35.21 | 19.90 | 30.38 | 41.86 |
| Qwen3-VL | 8B | 66.44 | 59.39 | 68.56 | 73.29 | 59.93 | 44.32 | 29.64 | 33.12 | 50.07 |
| Qwen3-VL | 32B | 71.30 | 60.04 | 75.62 | 72.39 | 72.67 | 46.80 | 29.40 | 44.19 | 55.38 |
| Qwen3.5 | 9B | 71.63 | 46.78 | 71.74 | 77.16 | 76.87 | 42.53 | 27.88 | 23.52 | 48.30 |
| Qwen3.5 | 27B | 67.95 | 55.34 | 75.32 | 76.35 | 85.46 | 36.88 | 26.97 | 24.40 | 49.25 |
| Cosmos-Reason2 | 2B | 64.69 | 55.27 | 59.70 | 56.33 | 73.56 | 38.95 | 28.52 | 26.85 | 45.94 |
| Cosmos-Reason2 | 8B | 67.95 | 64.09 | 68.60 | 70.26 | 83.88 | 47.30 | 32.50 | 37.69 | 54.46 |
| Cosmos-Reason2 | 32B | 70.29 | 73.58 | 74.03 | 50.04 | 4.35† | 50.47 | 30.04 | 33.12 | 47.03† |
| Cosmos3-Edge | 4B | 62.68 | 63.36 | 67.76 | 69.27 | 79.02 | 39.51 | 16.64 | 24.65 | 46.94 |
| Cosmos3-Nano | 16B | 68.95 | 68.88 | 74.83 | 75.57 | 74.11 | 48.04 | 31.42 | 59.21 | 60.67 |
| Cosmos3-Super | 64B | 69.46 | 71.28 | 72.94 | 76.23 | 86.97 | 51.90 | 29.54 | 64.66 | 63.62 |
| Gemma-4-E2B | 2B | 46.19 | 27.65 | 31.74 | 5.52 | 45.40 | 9.02 | 9.14 | 11.58 | 21.28 |
| Proprietary models |
| Gemini 3.1 Flash-Lite | — | 68.03 | 63.78 | 63.68 | 52.70 | 71.74 | 37.72 | 32.54 | 46.68 | 52.61 |
| Gemini 3.1 Pro | — | 71.46 | 68.57 | 72.04 | 67.17 | 77.21 | 45.69 | 35.55 | 67.88 | 62.66 |
| Gemini 3.5 Flash-Lite | — | 65.61 | 70.41 | 43.08 | 74.46 | 65.73 | 24.00 | 32.29 | 55.77 | 53.25 |
| Gemini 3.6 Flash | — | 76.82 | 82.00 | 79.20 | 75.78 | 81.57 | 51.50 | 36.15 | 75.99 | 69.52 |
| GPT-5.6 Sol | — | 78.08 | 76.14 | 81.90 | 69.44 | 69.30 | 55.71 | 37.28 | 75.02 | 68.04 |

Table 1: VANTAGE-Bench main results. Zero-shot performance of 17 models across the eight tasks, grouped by reasoning pillar. All metrics scaled 0–100; Overall is the macro-average of the four pillar scores, and bold denotes the best score per column. Pillar scores are in Table [11](https://arxiv.org/html/2609.09396#A4.T11 "Table 11 ‣ D.5 Pillar Scores ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") and item-level 95% bootstrap intervals in Table [13](https://arxiv.org/html/2609.09396#A7.T13 "Table 13 ‣ G.1 Item-Level Confidence Intervals ‣ Appendix G Reported Uncertainty ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"). †Output-format regression on Object Localization for this checkpoint; reported unmodified, and it propagates into the aggregates that contain it.

#### Semantic Understanding.

Semantic understanding is the strongest pillar at the top of the table, though spatial grounding has the higher aggregate across the full model set (Table [11](https://arxiv.org/html/2609.09396#A4.T11 "Table 11 ‣ D.5 Pillar Scores ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). Gemini 3.6 Flash leads Event Verification at 82.00 Macro F1 and GPT-5.6 Sol leads Video Question Answering at 78.08, with Cosmos-Reason2-32B and Cosmos3-Super leading the open-weight field on Event Verification at 73.58 and 71.28. Event Verification separates models far more sharply than VQA, spanning 27.65 to 82.00 against 46.19 to 78.08. Smaller models are conservative under uncertainty rather than uniformly weak: Qwen3-VL-8B rejects plausible negatives at a Specificity of 74.58 while reaching only 50.96 in True Event Recall, so it fails to recognize when physical interactions such as collisions or safety violations actually occur. We term this causal blindness and break it down in Appendix [D](https://arxiv.org/html/2609.09396#A4 "Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"); metric definitions are in Appendix [B](https://arxiv.org/html/2609.09396#A2 "Appendix B Formal Task Formulations and Evaluation Metrics ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

#### Spatial Understanding.

The spatial pillar is where open-weight models are most competitive. GPT-5.6 Sol leads 2D Spatial Pointing at 81.90, but open-weight models lead the other two spatial tasks outright. Cosmos3-Super leads 2D Object Localization at 86.97, ahead of the best proprietary model at 81.57, and Qwen3.5-9B leads 2D Referring Expressions at 77.16, with Qwen3.5-27B and Cosmos3-Super close behind at 76.35 and 76.23 against 75.78 for the best proprietary model. Single-frame semantic-to-spatial mapping is therefore maturing in open-weight architectures.

#### Temporal Understanding.

The temporal pillar is the weakest in absolute terms across the entire suite: the best scores on Temporal Localization and Dense Video Captioning, 55.71 mIoU and 37.28 SODAc, sit far below the leader on every other task (Section [4.4](https://arxiv.org/html/2609.09396#S4.SS4 "4.4 Returns to Scale and the Temporal Lag ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). This is not confined to open-weight models. On Temporal Localization the best proprietary and best open-weight scores are 55.71 and 51.90, a margin of 3.81 that is the narrowest frontier advantage on any task the frontier leads; on referring expressions and object localization the margin runs the other way, with open-weight models ahead. In Dense Video Captioning, models generate accurate semantic descriptions but fail to localize them in time, which depresses the joint SODAc\\text{SODA}\_{c} metric; we separate the two components in Appendix [D](https://arxiv.org/html/2609.09396#A4 "Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

#### Spatio-Temporal Understanding.

Single Object Tracking shows the widest separation between proprietary and open-weight models of any task. Gemini 3.6 Flash reaches 75.99 Success AUC and GPT-5.6 Sol 75.02, against 64.66 for the strongest open-weight model, Cosmos3-Super. The spread within the open-weight group is itself large, from 64.66 down to 11.58, and tracks training focus more closely than parameter count. Appendix [D.3](https://arxiv.org/html/2609.09396#A4.SS3 "D.3 Tracking Anchors and Horizon Analysis ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") places these numbers against specialist trackers and shows that the separation grows with the tracking horizon.

### 4.3 The Operational Deployment Gap (Δ\\Delta)

To test whether the Infrastructure AI Gap is real, we compare model performance on VANTAGE-Bench against the same models’ reported baselines on standard, consumer-focused datasets (Table [2](https://arxiv.org/html/2609.09396#S4.T2 "Table 2 ‣ The deficit is localized, not uniform. ‣ 4.3 The Operational Deployment Gap (Δ) ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). We include every model whose developer publishes reference scores: Qwen3-VL reports all five reference benchmarks at 2B, 8B, and 32B, and the Cosmos3 report publishes RefCOCO. Frontier proprietary releases and newer open-weight families increasingly report only high-level multiple-choice cognitive benchmarks and no longer publish zero-shot baselines for granular spatial and temporal grounding, which is itself symptomatic of the evaluation gap we describe.

#### The deficit is localized, not uniform.

The deltas run in both directions, and that is what makes the pattern informative. Event verification, referring expressions, and temporal localization drop roughly 9 to 24 points across every family and scale we could match. Video question answering sits within 5.3 points, and pointing is flat at the two smaller scales (−0.7-0.7 and −0.5-0.5) before turning into a surplus of +8.3+8.3 at 32B. The same models therefore lose ground on some capabilities and gain it on others within one benchmark, which locates the shortfall in specific capabilities rather than in overall difficulty.

|  |  | Qwen3-VL |
| Task | Reference benchmark | 2B | 8B | 32B |
| VQA | VideoMME \[ [1](https://arxiv.org/html/2609.09396#bib.bib1 "")\] | +2.0 | −-5.0 | −-5.3 |
| Event Verification∗ | MLVU \[ [32](https://arxiv.org/html/2609.09396#bib.bib32 "")\] | −-23.6 | −-18.7 | −-22.1 |
| 2D Spatial Pointing | BLINK \[ [4](https://arxiv.org/html/2609.09396#bib.bib4 "")\] | −-0.7 | −-0.5 | +8.3 |
| 2D Referring Expressions | RefCOCO \[ [13](https://arxiv.org/html/2609.09396#bib.bib13 "")\] | −-20.5 | −-15.8 | −-19.5 |
| Temporal Localization | Charades-STA \[ [11](https://arxiv.org/html/2609.09396#bib.bib11 "")\] | −-19.3 | −-11.7 | −-14.4 |
| Cosmos3 on RefCOCO \[ [13](https://arxiv.org/html/2609.09396#bib.bib13 "")\] (Edge / Nano / Super) |
| 2D Referring Expressions | RefCOCO \[ [13](https://arxiv.org/html/2609.09396#bib.bib13 "")\] | −-10.8  /  −-8.7  /  −-13.3 |

Table 2: The Infrastructure AI Gap (Δ\\Delta = VANTAGE −- reference), for every model whose developer publishes reference scores. Qwen3-VL reports all five reference benchmarks at each scale; the Cosmos3 report publishes RefCOCO only. ∗Loosest mapping: Macro F1 against accuracy.

#### Where the shortfall sits.

Three observations locate it. Models sharing one base diverge sharply by training focus (Section [4.4](https://arxiv.org/html/2609.09396#S4.SS4 "4.4 Returns to Scale and the Temporal Lag ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")), so the pattern moves with what a model was trained on rather than with the suite as a whole. Proprietary access is no shortcut either: two proprietary models fall below four open-weight models on the overall pillar average (Table [1](https://arxiv.org/html/2609.09396#S4.T1 "Table 1 ‣ 4.2 Main Results ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). Most directly, the split appears _within_ a single task. On dense video captioning, BERTScore-F1 spans 54.2 to 63.9 across models while temporal IoU-F1 spans 33.2 to 39.4 on the same items and the same annotations (Table [6](https://arxiv.org/html/2609.09396#A4.T6 "Table 6 ‣ Dense Video Captioning. ‣ D.1 Semantic Illusion: Fluency vs. Grounding ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")): models describe the events correctly and misplace them in time. The failure is in temporal grounding specifically, not in video understanding broadly.

#### A prompt- and metric-matched control.

Our temporal localization evaluation uses the prompt template the developer published for its own Charades-STA evaluation, so task, metric, and prompt are held constant. Qwen3-VL drops from 56.0 to 44.3 at 8B and from 61.2 to 46.8 at 32B, and the strongest frontier model reaches only 55.7, below what mid-tier open models score on Charades-STA.

#### A capability with no external baseline.

Model releases claim tracking in their demonstrations, as the Qwen3-VL release does, but none reports a quantitative tracking benchmark, and no prior VLM tracking evaluation targets fixed-camera infrastructure video. Frontier models have therefore been deployed into physical environments without a published baseline for continuous spatio-temporal attention. VANTAGE-Bench supplies one, anchored against specialist trackers in Appendix [D.3](https://arxiv.org/html/2609.09396#A4.SS3 "D.3 Tracking Anchors and Horizon Analysis ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

### 4.4 Returns to Scale and the Temporal Lag

A prevailing hypothesis is that grounding deficits will resolve through parameter scaling. The four open-weight scaling series let us test this directly (Table [3](https://arxiv.org/html/2609.09396#S4.T3 "Table 3 ‣ 4.4 Returns to Scale and the Temporal Lag ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")).

|  | Open-weight scaling series | Proprietary |
| --- | --- | --- |
| Task | Qwen3-VL | Qwen3.5 | Cosmos-Reason2 | Cosmos3 | GPT-5.6 | Gemini 3.6 |
|  | (2B→\\rightarrow32B) | (9B→\\rightarrow27B) | (2B→\\rightarrow32B) | (Edge→\\rightarrowSuper) | Sol | Flash |
| VQA | 63.9→\\rightarrow71.3 (+7.4) | 71.6→\\rightarrow68.0 (−-3.6) | 64.7→\\rightarrow70.3 (+5.6) | 62.7→\\rightarrow69.5 (+6.8) | 78.1 | 76.8 |
| Event Verif. | 44.7→\\rightarrow60.0 (+15.3) | 46.8→\\rightarrow55.3 (+8.5) | 55.3→\\rightarrow73.6 (+18.3) | 63.4→\\rightarrow71.3 (+7.9) | 76.1 | 82.0 |
| Obj. Loc. | 47.4→\\rightarrow72.7 (+25.3) | 76.9→\\rightarrow85.5 (+8.6) | 73.6→\\rightarrow4.4† (−-69.2) | 79.0→\\rightarrow87.0 (+8.0) | 69.3 | 81.6 |
| Ref. Exp. | 65.1→\\rightarrow72.4 (+7.3) | 77.2→\\rightarrow76.4 (−-0.8) | 56.3→\\rightarrow50.0 (−-6.3) | 69.3→\\rightarrow76.2 (+6.9) | 69.4 | 75.8 |
| Pointing | 53.1→\\rightarrow75.6 (+22.5) | 71.7→\\rightarrow75.3 (+3.6) | 59.7→\\rightarrow74.0 (+14.3) | 67.8→\\rightarrow72.9 (+5.1) | 81.9 | 79.2 |
| Temp. Loc. | 35.2→\\rightarrow46.8 (+11.6) | 42.5→\\rightarrow36.9 (−-5.6) | 39.0→\\rightarrow50.5 (+11.5) | 39.5→\\rightarrow51.9 (+12.4) | 55.7 | 51.5 |
| DVC | 19.9→\\rightarrow29.4 (+9.5) | 27.9→\\rightarrow27.0 (−-0.9) | 28.5→\\rightarrow30.0 (+1.5) | 16.6→\\rightarrow29.5 (+12.9) | 37.3 | 36.2 |
| SOT | 30.4→\\rightarrow44.2 (+13.8) | 23.5→\\rightarrow24.4 (+0.9) | 26.9→\\rightarrow33.1 (+6.2) | 24.7→\\rightarrow64.7 (+40.0) | 75.0 | 76.0 |

Table 3: Returns to scale, smallest to largest member of each open-weight family, with the change in parentheses, alongside the two newest proprietary models. Row-best in bold; markers as in Table [1](https://arxiv.org/html/2609.09396#S4.T1 "Table 1 ‣ 4.2 Main Results ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

#### Returns to scale are task-specific, not pillar-specific.

Scaling helps substantially on some tasks and not at all on others, and the pattern does not align with the four pillars. Temporal Localization improves by an average of 7.5 points from the smallest to the largest family member, so temporal grounding does respond to scale. Object Localization improves with scale in three of the four families; Cosmos-Reason2-32B is the exception, due to an output-format regression rather than a perception result. Qwen3.5 regresses on four of eight tasks despite tripling in size.

#### The persistent finding is an absolute temporal lag.

Across all 17 models, no system exceeds 55.71 mIoU on Temporal Localization or 37.28 SODAc on Dense Video Captioning. The same metric on consumer footage runs higher: Qwen3-VL-32B scores 61.2 mIoU on Charades-STA against 46.8 here. Temporal grounding on operational footage is therefore unsolved at present scale, though nothing in our evidence bounds what further scaling might achieve.

#### Physical-AI training data helps some tasks far more than others.

Qwen3-VL-8B, Cosmos-Reason2-8B, and Cosmos3-Nano share a common base but carry progressively more physical-AI training data. Across that sequence tracking rises 26.1 points, object localization 14.2, and event verification 9.5, while temporal localization moves 3.7 and dense captioning 1.8. All three are evaluated zero-shot. The Cosmos models add physical-AI training over the shared base \[ [42](https://arxiv.org/html/2609.09396#bib.bib42 ""), [38](https://arxiv.org/html/2609.09396#bib.bib38 "")\], though the exact composition of that mixture is not public. What the sequence shows is that such training transfers to this suite very unevenly, transforming tracking while barely moving the temporal tasks. Our working hypothesis is a training-mixture asymmetry: spatial-grounding supervision in the form of bounding-box datasets is abundant, while densely timestamped video is scarce. A targeted fine-tuning probe would distinguish a capability gap from an elicitation gap, and we leave this test to future work.

## 5 Qualitative Analysis: Failure Modes of Infrastructure AI

While Section [4](https://arxiv.org/html/2609.09396#S4 "4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") quantifies the Infrastructure AI gap, we analyze key failure modes underlying this degradation. Additional quantitative breakdowns are provided in Appendix [D](https://arxiv.org/html/2609.09396#A4 "Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

#### Semantic Illusion (Fluency vs. Grounding).

Models exhibit strong linguistic fluency but fail to anchor predictions in space and time: they recognise what happens without resolving when it occurs (Section [4.3](https://arxiv.org/html/2609.09396#S4.SS3 "4.3 The Operational Deployment Gap (Δ) ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). The effect extends to Event Verification, where smaller models exhibit causal blindness: they correctly reject negatives but fail to detect true events, defaulting to conservative predictions in dense scenes.

#### Spatial vs. Spatio-Temporal Breakdown.

Strong single-frame spatial reasoning does not translate to temporal persistence. Weaker models often initialize correctly but fail to maintain object identity as the horizon extends. Two distinct failure modes appear: predictions that stop updating (tracking freeze) and predictions that keep updating but drift off target. Appendix [D.3](https://arxiv.org/html/2609.09396#A4.SS3 "D.3 Tracking Anchors and Horizon Analysis ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") separates these using freeze rate read jointly with Success AUC.

#### Domain-Specific Vulnerabilities.

Holding the model and the annotation pipeline fixed, the two pillars degrade in different domains. For Cosmos3-Super, VQA accuracy is comparable in Warehouse and Transportation, at 75.73 and 71.51, and drops sharply only in Smart Spaces, at 55.38, where human activity is least structured and intent is hardest to read from the scene alone. Dense video captioning follows a different order: strongest in Warehouse at 40.61, lower in Smart Spaces at 30.38, and collapsing in Transportation at 8.35. No single domain is uniformly hard. Each pillar has its own worst case, and a model’s aggregate score can therefore conceal a domain in which one capability has failed almost completely (Appendix [D](https://arxiv.org/html/2609.09396#A4 "Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")).

#### Where the Frontier Leads.

Proprietary access confers no across-the-board advantage; the two newest frontier releases do lead most tasks, but by a fairly uniform margin with tracking the one large outlier. The distinctive frontier capability is temporal persistence rather than spatial grounding, which we quantify in Appendix [D.6](https://arxiv.org/html/2609.09396#A4.SS6 "D.6 Where the Frontier Advantage Actually Lies ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

## 6 Discussion and Limitations

VANTAGE-Bench establishes a baseline for Infrastructure AI evaluation.

#### Camera geometry.

Our claims are scoped to the camera configurations actually sampled: elevated fixed cameras at 8 to 20 feet and 30 to 60 degrees from vertical for the video tasks and 2D Object Localization, oblique aerial views for 2D Referring Expressions, and vehicle-mounted footage for 2D Spatial Pointing. Real-world fixed-camera deployments vary more widely than this. Eye-level retail and low-angle industrial viewpoints are not covered; the constraint is data rights, since each deployment type requires separate licensing agreements.

#### Geographic concentration.

Real-world footage comes primarily from two U.S. municipalities, supplemented by publicly sourced and licensed European footage (Section [3](https://arxiv.org/html/2609.09396#S3 "3 Dataset and Benchmark Construction ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). Coverage is therefore weighted toward North America, and broadening it is future work.

#### Annotation density.

Counts are uneven across the three annotation regimes because the tasks themselves differ in density. Infrastructure scenes contain many simultaneous objects such as people and vehicles, so a single detection image carries 43.6 boxes on average. The detection task therefore reflects deep labeling by the nature of its definition rather than broad sampling. We report the three regimes separately rather than as one aggregate: video-task annotations, image-grounding annotations, and dense detection boxes.

#### Quality assurance.

Our acceptance rates come from a sequential second-expert review pipeline, in which a reviewer corrects a prior annotation rather than labeling the item independently. They measure how often expert work passes review, not agreement between independent annotators.

#### Programmatic question generation.

For 2D Spatial Pointing, the correct answer is fixed by human-labeled geometry and cannot be altered by the rewriting stage. The rewritten question text is nonetheless not constrained to preserve the uniqueness of its spatial cue in dense scenes, and we do not currently verify that it does. A targeted uniqueness audit of the rewritten questions is planned.

#### Tracking is synthetic only.

The Single Object Tracking track is built from synthetic warehouse sequences, so its conclusions are limited to that distribution and do not yet separate tracking failure from synthetic-domain mismatch. The specialist-tracker and horizon analyses in Appendix [D.3](https://arxiv.org/html/2609.09396#A4.SS3 "D.3 Tracking Anchors and Horizon Analysis ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") establish that the task is well posed, but they do not substitute for real-data validation. Real tracking sequences are planned for a future release.

#### Model coverage and reported uncertainty.

Our evaluation is strictly zero-shot; domain-specific fine-tuning is left to future work. Extreme weather and lighting conditions are not systematically covered. Inference settings were tuned per model, following each developer’s published guidance where it exists and our own prompt-sensitivity checks otherwise; Appendix [F.2](https://arxiv.org/html/2609.09396#A6.SS2 "F.2 Task-Specific Inference Configurations ‣ Appendix F Reproducibility and Experimental Configuration ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") reports the configuration each model was finally evaluated under rather than the alternatives we tried. The intervals we report (Appendix [G.1](https://arxiv.org/html/2609.09396#A7.SS1 "G.1 Item-Level Confidence Intervals ‣ Appendix G Reported Uncertainty ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")) therefore cover item sampling only, and do not capture how far a score would move under a different prompt or decoding configuration.

#### Planned extensions.

Coverage is uneven across tasks and domains: 2D Spatial Pointing and 2D Referring Expressions are currently drawn from a single domain, and the tracking track is synthetic. We are extending every task with additional real-world footage spanning all three deployment domains rather than a subset, and we are broadening the camera configurations sampled within each. We also plan a human performance baseline on a representative subset of each task, which would calibrate task difficulty independently of annotation quality. Beyond the current suite, we plan to add task tracks that operational deployments require and this release does not cover, including multi-object tracking and 3D grounding.

#### Ethical considerations.

The automation of fixed-camera monitoring carries privacy implications. All raw assets underwent a de-identification pipeline combining automated obfuscation with human verification, documented in Appendix [E](https://arxiv.org/html/2609.09396#A5 "Appendix E De-identification Pipeline ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"). VANTAGE-Bench is released under a license prohibiting biometric identification and demographic profiling. We emphasize that the benchmark evaluates physical and causal reasoning rather than identity recognition, and we advocate for human-in-the-loop oversight in downstream operational deployments.

## 7 Conclusion

We introduced VANTAGE-Bench, an evaluation suite for VLMs in open-loop Infrastructure AI settings. Moving beyond the priors of internet video and single-format MCQ evaluation, we built an 8-task taxonomy spanning semantic, spatial, temporal, and spatio-temporal reasoning over 3,346 expert-annotated media assets, and evaluated 17 models zero-shot.

The resulting picture is uneven rather than uniformly poor. Open-weight models lead 2D Object Localization outright, and they edge ahead on 2D Referring Expressions by a margin comparable to its confidence interval. The deficit against consumer-centric benchmarks concentrates in event verification, referring expressions, and temporal grounding, while pointing is flat at smaller scales and turns into a surplus at 32B. Returns to scale are task-specific rather than pillar-specific. What persists across all 17 models is an absolute lag on the two temporal tasks, which no system has yet closed, and a widening separation on tracking as the horizon extends. We hope VANTAGE-Bench provides a useful framework for evaluating physical reasoning in operational settings, and that its open leaderboard makes progress on these specific deficits measurable.

## Acknowledgements

We thank Paris Zhang, Yilin Zhao and Zheng Liu for developing portions of several task tracks, including Event Verification; Chintan Shah, Sumeeth Nagaraja and Ratnesh Kumar for data sourcing, discussions and evaluation feedback; and Yao Xu and the NVIDIA Data Factory team for video sourcing and human annotation. Tsung-Yi Lin, Ke Ding and Ming-Yu Liu provided evaluation infrastructure and model access. We thank Professor Carrie Russell of Clemson University for collaboration throughout, and Ahmet Dokmeci for the leaderboard evaluation pipeline. This research used in part resources on the Palmetto 2 cluster at Clemson University under National Science Foundation awards MRI 1228312, II NEW 1405767, MRI 1725573, and MRI 2018069. The views expressed in this article do not necessarily represent the views of NSF or the United States government.

## Appendix A Data Statistics and Benchmark Comparison

This appendix places VANTAGE-Bench alongside the benchmarks it is most often compared against and records how its annotations are distributed. Table [4](https://arxiv.org/html/2609.09396#A1.T4 "Table 4 ‣ Appendix A Data Statistics and Benchmark Comparison ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") reports scale, modality, and pillar coverage for each.

BenchmarkModality\# Media\# Annot.PillarsAnnotation SourceVideoMMEVideo9002,700SemanticHumanBLINKImage3,6831,906SpatialHuman, ExistingRefCOCO\_avgImage3,98230,969SpatialHuman, ExistingODinW13 \[ [33](https://arxiv.org/html/2609.09396#bib.bib33 "")\]Image4,60810,966SpatialHuman, ExistingCharadesSTAVideo1,3343,720TemporalHuman, PLActivityNet Cap.Video5,04417,750TemporalHumanVANTAGE-BenchImage + Video3,34635,027†All fourHuman, Simulated, PL, Existing

Table 4: Cross-benchmark comparison. All statistics reflect available evaluation test sets. Pillars is the reasoning taxonomy each benchmark covers. †Shown as a single total for comparability with the other rows; we report our annotations by regime elsewhere.

Each of the three annotation regimes listed in Section [3](https://arxiv.org/html/2609.09396#S3 "3 Dataset and Benchmark Construction ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") is comparable to or larger than its established counterpart in Table [4](https://arxiv.org/html/2609.09396#A1.T4 "Table 4 ‣ Appendix A Data Statistics and Benchmark Comparison ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"): the video tasks carry more annotations than VideoMME (3,342 against 2,700), though over slightly fewer videos (854 against 900), and image grounding exceeds BLINK’s test set (4,281 against 1,906). Tracking is the one smaller track. Detection dominates the aggregate because infrastructure scenes are dense, at 43.6 boxes per image against ODinW-13’s 2.4, which reflects scene density rather than broad sampling.

## Appendix B Formal Task Formulations and Evaluation Metrics

In this section, we provide the rigorous definitions for the mappings and evaluation protocols used in VANTAGE-Bench.

### B.1 Notation and Definitions

Each task is stated in Table [5](https://arxiv.org/html/2609.09396#A2.T5 "Table 5 ‣ B.1 Notation and Definitions ‣ Appendix B Formal Task Formulations and Evaluation Metrics ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") as a function from inputs to a structured output, with its primary metric. We define the following input and output spaces to standardize the task formulations:

- •


Inputs:ℐ\\mathcal{I} (Image); 𝒱\\mathcal{V} (Video); 𝒬\\mathcal{Q} (Query); Bt=0B\_{t=0} (Initial Box).

- •


Outputs:τ\\tau (Temporal segment \[ts​t​a​r​t,te​n​d\]\[t\_{start},t\_{end}\]); CC (Caption); aa (Selection from candidates); {B}\\{B\\} (Set of coordinates).


|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Pillar | Task | Mathematical Formulation | Primary Metric | Additional |
| Semantic | EV | f⁡(𝒱,𝒬h​y​p)→{0,1}f(\\mathcal{V},\\mathcal{Q}\_{hyp})\\rightarrow\\{0,1\\} | Macro F1 | Sens., Spec. |
| VQA | f⁡(𝒱,𝒬,{A,B,C,D})→a∈{A,B,C,D}f(\\mathcal{V},\\mathcal{Q},\\{A,B,C,D\\})\\rightarrow a\\in\\{A,B,C,D\\} | Accuracy | — |
| Spatial | RefEx | f⁡(ℐ,𝒬)→\[x,y,w,h\]f(\\mathcal{I},\\mathcal{Q})\\rightarrow\[x,y,w,h\] | mIoU | Precision@0.5 |
| Pointing | f⁡(ℐ,𝒬,{A,B,C,D})→a∈{A,B,C,D}f(\\mathcal{I},\\mathcal{Q},\\{A,B,C,D\\})\\rightarrow a\\in\\{A,B,C,D\\} | Accuracy | — |
| Obj Loc. | f⁡(ℐ,𝒬c)→{Bk}k=1Mf(\\mathcal{I},\\mathcal{Q}\_{c})\\rightarrow\\{B\_{k}\\}\_{k=1}^{M} | F1@0.5 | COCO mAP |
| Temporal | Temp Loc. | f⁡(𝒱,𝒬)→\[ts​t​a​r​t,te​n​d\]f(\\mathcal{V},\\mathcal{Q})\\rightarrow\[t\_{start},t\_{end}\] | mIoU | Recall@0.5 |
| DVC | f⁡(𝒱)→{(τi,Ci)}i=1Nf(\\mathcal{V})\\rightarrow\\{(\\tau\_{i},C\_{i})\\}\_{i=1}^{N} | SODAc | BERTScore-F1, IoU-F1 |
| Spatio-Temp. | SOT | f⁡(𝒱,Bt=0)→{Bt}t=1Tf(\\mathcal{V},B\_{t=0})\\rightarrow\\{B\_{t}\\}\_{t=1}^{T} | Success AUC | Mean IoU |

Table 5: Formal task definitions for VANTAGE-Bench. The primary metric is the one reported in Table [1](https://arxiv.org/html/2609.09396#S4.T1 "Table 1 ‣ 4.2 Main Results ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") and on the public leaderboard.

### B.2 Metric Clarifications

- •


SODAc: Evaluates narrative quality by matching predicted event sequences to ground truth based on temporal overlap and BERTScore-based \[ [35](https://arxiv.org/html/2609.09396#bib.bib35 "")\] linguistic similarity.

- •


Success AUC: For SOT, the Success Plot counts frames where predicted IoU exceeds threshold σ\\sigma, calculated by varying σ∈\[0,1\]\\sigma\\in\[0,1\].

- •


Macro F1: Penalizes models that exploit majority-class bias in binary Event Verification.


## Appendix C Pipeline Details and Data Adaptation

### C.1 Data Adaptation for SOT and RefEx

2D Referring Expressions: We utilized RefDrone because its elevated perspective mimics infrastructure cameras. We ported prompts requiring dense disambiguation between identically colored vehicles based on relative spatial relationships.

Single Object Tracking: Adapted from the MTMC 2025 subset of PhysicalAI-SmartSpaces. We filtered 17 warehouse scenes featuring workers and robotic profiles (e.g., Nova Carter). Sequences include an initial “visual anchor” followed by a sequence of frames sampled at densities of 8, 16, and 32 frames.

## Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap

This section provides detailed quantitative and qualitative analysis of the failure modes summarized in Section [5](https://arxiv.org/html/2609.09396#S5 "5 Qualitative Analysis: Failure Modes of Infrastructure AI ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"). While Section [4](https://arxiv.org/html/2609.09396#S4 "4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") establishes the magnitude of the Infrastructure AI gap, the analyses below isolate the underlying mechanisms responsible for model failure.

### D.1 Semantic Illusion: Fluency vs. Grounding

We observe a systemic disconnect between linguistic fluency and physical grounding, which we term the Semantic Illusion.

#### Dense Video Captioning.

Models generate semantically coherent descriptions (high BERTScore-F1) but fail to temporally localize events, resulting in low joint performance (SODAc\\text{SODA}\_{c}). This indicates that models capture what happens but fail to resolve when it occurs, leading to temporal smearing across events. Table [6](https://arxiv.org/html/2609.09396#A4.T6 "Table 6 ‣ Dense Video Captioning. ‣ D.1 Semantic Illusion: Fluency vs. Grounding ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") separates the two components.

| Model | Semantic Fluency | Discrete Loc. | Joint Metric |
| --- | --- | --- | --- |
|  | (BERTScore-F1) | (IoU-F1) | (SODAc) |
| --- | --- | --- | --- |
| Gemini 3.1 Pro | 63.86 | 39.44 | 35.55 |
| Cosmos-Reason2-8B | 58.08 | 36.70 | 32.50 |
| Qwen3-VL-8B | 58.66 | 33.24 | 29.64 |
| Cosmos-Reason2-32B | 54.74 | 33.95 | 30.04 |
| Cosmos3-Super | 54.24 | 33.39 | 29.54 |

Table 6: Dense Video Captioning decomposed into its semantic and temporal components, with the joint metric for reference. Scaled 0–100.

#### Event Verification: Causal Blindness.

The same disconnect appears in Event Verification, though the direction of the imbalance depends on the model rather than on scale alone (Table [7](https://arxiv.org/html/2609.09396#A4.T7 "Table 7 ‣ Event Verification: Causal Blindness. ‣ D.1 Semantic Illusion: Fluency vs. Grounding ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). Qwen3-VL-8B fails to detect true events while maintaining strong specificity, at 50.96 against 74.58, a bias toward conservative predictions under uncertainty rather than an inability to reason about the scene. Cosmos-Reason2-8B shows the opposite profile, at 71.15 sensitivity against 57.63 specificity, accepting events that did not occur. Macro F1 conceals both, which is why we report the two components separately.

| Model | Macro F1 | True Event Recall | True Negative Recall |
| --- | --- | --- | --- |
|  |  | (Sensitivity) | (Specificity) |
| --- | --- | --- | --- |
| Gemini 3.6 Flash | 82.00 | 87.50 | 76.27 |
| GPT-5.6 Sol | 76.14 | 77.88 | 76.27 |
| Cosmos-Reason2-32B | 73.58 | 83.65 | 62.71 |
| Cosmos3-Super | 71.28 | 72.12 | 72.88 |
| Gemini 3.1 Pro | 68.57 | 71.15 | 67.80 |
| Cosmos-Reason2-8B | 64.09 | 71.15 | 57.63 |
| Qwen3-VL-8B | 59.39 | 50.96 | 74.58 |

Table 7: Event Verification causal breakdown (n=163n=163; 104 positive, 59 negative). Sensitivity and specificity are reported separately, since Macro F1 alone conceals the asymmetry.

### D.2 Spatial vs. Spatio-Temporal Breakdown

We identify a key architectural limitation: static spatial grounding does not imply temporal persistence. Table [8](https://arxiv.org/html/2609.09396#A4.T8 "Table 8 ‣ D.2 Spatial vs. Spatio-Temporal Breakdown ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") contrasts the two for six representative models.

The dissociation is sharpest in the open-weight group. Qwen3.5-27B reaches 85.46 on 2D Object Localization and 76.35 on 2D Referring Expressions, among the strongest spatial results in the suite, yet scores 24.40 on tracking. Cosmos3-Super posts comparable spatial numbers and reaches 64.66. Spatial grounding is therefore not sufficient for temporal persistence, and the two are not acquired together.

| Model | Spatial | Spatio-Temporal |
| Pointing | RefEx | Object Loc. | SOT |
|  | (Accuracy) | (mIoU) | (F1@0.5) | (AUC) |
| GPT-5.6 Sol | 81.90 | 69.44 | 69.30 | 75.02 |
| Gemini 3.6 Flash | 79.20 | 75.78 | 81.57 | 75.99 |
| Cosmos3-Super | 72.94 | 76.23 | 86.97 | 64.66 |
| Qwen3.5-27B | 75.32 | 76.35 | 85.46 | 24.40 |
| Cosmos-Reason2-8B | 68.60 | 70.26 | 83.88 | 37.69 |
| Qwen3-VL-8B | 68.56 | 73.29 | 59.93 | 33.12 |

Table 8: Single-frame spatial scores against Single Object Tracking, for six representative models. Metrics scaled 0–100.

### D.3 Tracking Anchors and Horizon Analysis

Every system is reported at all three horizons in Table [9](https://arxiv.org/html/2609.09396#A4.T9 "Table 9 ‣ Baselines. ‣ D.3 Tracking Anchors and Horizon Analysis ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

#### Protocol.

All evaluations are performed on the same underlying object tracklets (200 sequences); the 8-frame, 16-frame, and 32-frame benchmarks differ only in the temporal sampling and clip length. The 8f and 16f datasets share an identical frame-level prefix (stride 15), with the 16f clips extending the 8f sequences by eight additional sampled frames. The 32f benchmark is independently resampled from the same tracklets using a stride of 14, resulting in a longer temporal window rather than a strict continuation of the 16f clips. At the default sampling rate (30 FPS), the three settings correspond to approximately 3.5 s (8f), 7.5 s (16f), and 14.5 s (32f) of video. We additionally report a _freeze rate_: the fraction of predicted boxes that are nearly identical (IoU ≥0.95\\geq 0.95) to the box predicted on the previous frame.

#### Baselines.

We evaluate four specialist trackers, a static-box floor, and a random floor on the same 200 tracklets and the exact frames the VLMs see, using the identical Success-AUC scorer. We did not add classical trackers (e.g., KCF, CSRT): on standard benchmarks they are bounded above by the modern trackers and below by these floors, so they would not change where the VLM scores sit.

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Success AUC↑\\uparrow | Freeze rate↓\\downarrow |  |
| Model | 8f | 16f | 32f | 8f | 16f | 32f | Δ\\Delta AUC |
| Floors |
| Random | 6.55 | 6.27 | 6.12 | 0.00 | 0.00 | 0.00 | −0.43-0.43 |
| Static box | 24.64 | 18.28 | 13.75 | 99.08 | 99.35 | 99.20 | −10.89-10.89 |
| Specialist trackers |
| SAM 3 | 79.92 | 82.25 | 80.47 | 17.58 | 30.66 | 29.83 | +0.55+0.55 |
| SAMURAI | 80.91 | 81.16 | 79.85 | 18.00 | 30.23 | 30.01 | −1.06-1.06 |
| SUTrack | 79.12 | 81.30 | 78.50 | 16.33 | 28.43 | 27.77 | −0.62-0.62 |
| MCITrack | 77.74 | 79.44 | 76.61 | 16.67 | 27.53 | 27.29 | −1.13-1.13 |
| Vision-language models |
| Gemini 3.6 Flash | 75.99 | 70.77 | 66.25 | 23.75 | 36.46 | 36.66 | −9.74-9.74 |
| GPT-5.6 Sol | 75.02 | 74.75 | 70.91 | 22.75 | 37.32 | 34.96 | −4.11-4.11 |
| Cosmos3-Super | 64.66 | 61.32 | 45.32 | 32.08 | 48.74 | 58.99 | −19.34-19.34 |
| Cosmos-Reason2-8B | 37.69 | 30.64 | 17.98 | 77.67 | 84.57 | 92.96 | −19.71-19.71 |
| Qwen3-VL-8B | 33.12 | 23.27 | 15.67 | 38.42 | 47.20 | 48.50 | −17.45-17.45 |

Table 9: Tracking anchors and horizon analysis. Success AUC and freeze rate at three horizons, scaled 0–100. The 8-frame column is the Success AUC reported on the public leaderboard.

#### Reading the anchors.

The specialist trackers reach approximately 80 Success AUC and hold steady as the horizon grows, establishing the level a purpose-built system reaches on these annotations. Frontier VLMs come within roughly 5 points of them at 8 frames but degrade with horizon (GPT-5.6 Sol −4.1-4.1, Gemini 3.6 Flash −9.7-9.7 from 8f to 32f). Open-weight behavior is heterogeneous. Cosmos3-Super remains well above the static floor at 32 frames (45.3 versus 13.8 AUC), although it drops 19.3 points as the horizon increases. Cosmos-Reason2-8B and Qwen3-VL-8B finish much closer to the static floor, at 18.0 and 15.7 versus 13.8. Long-horizon degradation is therefore broadly observed, while convergence toward the static baseline is confined to the weaker open-weight models. The tier ordering—specialists, frontier VLMs, strongest open-weight, then 8B-class—is unchanged across all three horizons.

#### Reading the freeze rate.

Freeze rate must be interpreted jointly with AUC, since a nearly unchanged box can be correct when the target is stationary; freeze rate alone is not an error rate. The specialist trackers provide an empirical reference that itself rises with horizon: 16–18% at 8 frames against 27–31% at 16 and 32 frames. The static-box floor, which by construction never updates, sits at 99% throughout, so the metric is bracketed at both ends. Cosmos-Reason2-8B has a much higher freeze rate of 93% together with only 18.0 AUC at 32 frames, consistent with a failure to update its prediction. Qwen3-VL-8B has a lower freeze rate of 49% but only 15.7 AUC, consistent with continued box updates that drift off target. We therefore use freeze rate to distinguish these two failure modes, without interpreting the specialist rate as the true fraction of stationary targets.

The track covers 200 objects across 102 videos, in line with established tracking test sets (GOT-10k validation: 180 videos; LaSOT: 280). What separates VLMs from purpose-built trackers on this track is persistence over time rather than box regression: at short horizons the frontier models are close to the specialists, and the gap opens as the horizon extends.

### D.4 Domain-Specific Vulnerabilities

Model performance varies significantly across operational domains, revealing sensitivity to environmental priors (Table [10](https://arxiv.org/html/2609.09396#A4.T10 "Table 10 ‣ D.4 Domain-Specific Vulnerabilities ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")).

| Domain | VQA (Acc %) | DVC (SODAc\\text{SODA}\_{c}) |
| --- | --- | --- |
| Warehouse | 75.73 | 40.61 |
| Smart Spaces | 55.38 | 30.38 |
| Transportation | 71.51 | 8.35 |
| Overall | 69.46 | 29.54 |

Table 10: Cosmos3-Super by operational domain, holding model and annotation pipeline fixed.

#### Unstructured Intent.

Semantic reasoning is weakest in Smart Spaces, at 55.38 VQA accuracy against 75.73 in Warehouse, which we attribute to ambiguous human behaviour and the absence of structured, task-driven interactions.

#### Egocentric Bias is Temporal, not Semantic.

Transportation leaves VQA accuracy nearly intact at 71.51 but reduces dense video captioning to 8.35 from 40.61 in Warehouse. The model still recognises what is in the scene; it loses the ability to say when events begin and end. We attribute this to the mismatch between ego-centric training footage and fixed-camera evaluation perspectives, which is most disruptive to the continuous-motion cues temporal grounding depends on. The domain effect is therefore larger than previously reported, but it falls on the temporal pillar.

### D.5 Pillar Scores

The main results table reports the eight task scores and the
Overall column, but not the intermediate pillar scores from which
Overall is computed. Table [11](https://arxiv.org/html/2609.09396#A4.T11 "Table 11 ‣ D.5 Pillar Scores ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") supplies them. Each
pillar score is the unweighted mean of its constituent task scores, and
Overall is the unweighted mean of the four pillar scores, so a
pillar containing one task carries the same weight as a pillar containing
three. This equal weighting is deliberate: it prevents the spatial pillar,
which has the most tasks, from dominating the aggregate. It does mean the
Spatio-Temporal pillar is identical to the Single Object Tracking column of
Table [1](https://arxiv.org/html/2609.09396#S4.T1 "Table 1 ‣ 4.2 Main Results ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"), since tracking is its only task, and that
tracking therefore carries a quarter of the Overall score.
Readers who prefer a task-weighted aggregate can compute one from
Table [1](https://arxiv.org/html/2609.09396#S4.T1 "Table 1 ‣ 4.2 Main Results ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"); it would raise the relative weight of the
spatial pillar, where open-weight models are strongest.

ModelParamsSemanticSpatialTemporalSp.-Temp.Overall(2 tasks)(3 tasks)(2 tasks)(1 task)Open-weight modelsQwen3-VL2B54.2955.2227.5530.3841.86Qwen3-VL8B62.9167.2636.9833.1250.07Qwen3-VL32B65.6773.5638.1044.1955.38Qwen3.59B59.2075.2635.2023.5248.30Qwen3.527B61.6579.0431.9324.4049.25Cosmos-Reason22B59.9863.2033.7326.8545.94Cosmos-Reason28B66.0274.2539.9037.6954.46Cosmos-Reason232B71.9442.81†40.2533.1247.03†Cosmos3-Edge4B63.0272.0228.0724.6546.94Cosmos3-Nano16B68.9174.8439.7359.2160.67Cosmos3-Super64B70.3778.7140.7264.6663.62Gemma-4-E2B2B36.9227.559.0811.5821.28Proprietary modelsGemini 3.1 Flash-Lite—65.9162.7135.1346.6852.61Gemini 3.1 Pro—70.0172.1440.6267.8862.66Gemini 3.5 Flash-Lite—68.0161.0928.1455.7753.25Gemini 3.6 Flash—79.4178.8543.8375.9969.52GPT-5.6 Sol—77.1173.5546.5075.0268.04

Table 11: Pillar scores and their aggregate. Each pillar is the unweighted
mean of its tasks; Overall is the unweighted mean of the four
pillars. The Spatio-Temporal pillar consists of Single Object Tracking
alone. All values scaled 0–100; bold denotes the best score per column. Markers as in Table [1](https://arxiv.org/html/2609.09396#S4.T1 "Table 1 ‣ 4.2 Main Results ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

### D.6 Where the Frontier Advantage Actually Lies

The frontier advantage is concentrated in tracking rather than spread across spatial grounding, and this section sets out the evidence for that.

#### There is no across-the-board proprietary advantage.

Open-weight models lead 2D Object Localization outright (86.97 against 81.57) and lead 2D Referring Expressions by 1.38 points (77.16 against 75.78), and two proprietary models fall below four open-weight models on the overall pillar average (Table [1](https://arxiv.org/html/2609.09396#S4.T1 "Table 1 ‣ 4.2 Main Results ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). Proprietary access alone does not confer an edge.

#### The advantage belongs to the two newest releases, and it is mostly uniform.

GPT-5.6 Sol and Gemini 3.6 Flash lead the best open-weight model on six of eight tasks, by a fairly uniform margin of 3.8 to 8.4 points across spatial, semantic, and temporal tasks alike. Three tasks depart from that band. Two are exceptions in the open-weight direction: Cosmos3-Super leads object localization by 5.4 points, and Qwen3.5-9B leads referring expressions by 1.4. Single Object Tracking is the exception in the other direction, where the frontier lead is 11.3 points, roughly double the typical margin.

#### The distinctive frontier capability is temporal persistence.

The tracking gap is where the frontier separates, not spatial grounding, where open-weight models in fact lead two of the three tasks, and not temporal localization, where the edge is smallest at 3.8 points because no model of either kind exceeds 55.71 mIoU (Section [4.4](https://arxiv.org/html/2609.09396#S4.SS4 "4.4 Returns to Scale and the Temporal Lag ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). The horizon analysis in Appendix [D.3](https://arxiv.org/html/2609.09396#A4.SS3 "D.3 Tracking Anchors and Horizon Analysis ‣ Appendix D Extended Analysis: Deconstructing the Infrastructure AI Gap ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") is consistent with this reading: frontier models degrade least as the tracking horizon extends, while weaker open-weight models converge toward the static-box floor.

## Appendix E De-identification Pipeline

#### What counts as PII.

We treat as personally identifiable any information that can identify or locate a person: names, recognizable faces, license plates, addresses, and GPS or location data.

#### Detection and obfuscation.

Faces, license plates, and video locations were obfuscated using a proprietary detector. Detector output was then verified and corrected by human annotators, so that the released media reflect a human-in-the-loop pass rather than automated obfuscation alone.

#### Licensing safeguards.

Beyond obfuscation, the NVIDIA Evaluation Data License prohibits biometric identification and demographic profiling, restricting the released data to evaluation and benchmarking use.

#### Consent.

70% of footage was provided by vendors who obtained explicit informed consent from recorded individuals for research and redistribution. A smaller portion was captured in limited spaces with posted notice of camera operation, where individuals incidentally captured consented to fixed-camera monitoring as a condition of site access.

## Appendix F Reproducibility and Experimental Configuration

### F.1 Compute Resources and Frameworks

Evaluations for open-weight models (Cosmos-Reason2, Qwen3-VL, Qwen3.5, Cosmos3, Gemma-4) were conducted on the Palmetto 2 cluster at Clemson University, using 7 nodes of 8×\\times NVIDIA H100 (80GB) GPUs, as well as additional cloud compute instances. Proprietary models (GPT-5.6 Sol and the Gemini family) were accessed via public APIs. We build our evaluation harness on top of VLMEvalKit \[ [31](https://arxiv.org/html/2609.09396#bib.bib31 "")\], extending it with custom metric scripts for automated SODAc computation, temporal IoU evaluation, and spatial trajectory parsing.

### F.2 Task-Specific Inference Configurations

All evaluations used greedy decoding (temperature = 0) with
chain-of-thought disabled (enable\_thinking = False).
The sampling and pixel budgets used to manage visual granularity and
token limits are given in Table [12](https://arxiv.org/html/2609.09396#A6.T12 "Table 12 ‣ F.2 Task-Specific Inference Configurations ‣ Appendix F Reproducibility and Experimental Configuration ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"). FPS
ranges reflect model-specific sampling rates.

| Pillar | Task | FPS | Max Frames | Max Total Pixels |
| --- | --- | --- | --- | --- |
| Semantic | EV / VQA | 1.0 – 4.0 | 256 | 16.7×10616.7\\times 10^{6} |
| Spatial | Pointing / RefEx | — | 1 | 1.5×1061.5\\times 10^{6} |
| Temporal | Temporal Localization | 2.0 – 10.0 | 256 | 16.7×10616.7\\times 10^{6} |
| Temporal | DVC | 1.0 – 4.0 | 128 | 8.4×1068.4\\times 10^{6} |
| Spatio-Temp. | SOT | — | 8 / 16 / 32 | 0.9×1060.9\\times 10^{6} |
| Spatial | 2D Object Localization | — | 1 | 1.5×1061.5\\times 10^{6} |

Table 12: VANTAGE-Bench Task Inference Parameters.

### F.3 Code, Data Access, and Release Strategy

To support reproducibility, we provide the VANTAGE-Bench dataset at [huggingface.co/datasets/nvidia/PhysicalAI-VANTAGE-Bench](https://huggingface.co/datasets/nvidia/PhysicalAI-VANTAGE-Bench "")
the evaluation code at [github.com/Clemson-Capstone/VANTAGE-Bench](https://github.com/Clemson-Capstone/VANTAGE-Bench ""), and the public leaderboard at [huggingface.co/spaces/clemson-computing/VANTAGE-Bench-Leaderboard](https://huggingface.co/spaces/clemson-computing/VANTAGE-Bench-Leaderboard ""). Project information is collected at [vantage-bench.org](https://vantage-bench.org/ ""). To preserve long-term integrity against training-data contamination, we adopt a held-out evaluation protocol. We publicly release (i) all input media, (ii) all prompts and questions, and (iii) the evaluation harness. Ground-truth annotations are held-out to be used by the official leaderboard server. The leaderboard is live and open for submissions, which are uploaded as JSON in LLaVA format.

## Appendix G Reported Uncertainty

We report two kinds of variability, which answer different questions: how
precisely a score is estimated from the items in the test set, and how
reproducible it is across runs.

### G.1 Item-Level Confidence Intervals

Because all evaluation uses greedy decoding at temperature 0, run-to-run
variance is small (Section [G.2](https://arxiv.org/html/2609.09396#A7.SS2 "G.2 Seed Variance ‣ Appendix G Reported Uncertainty ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"), below); the dominant source of
uncertainty is which items happen to be in the test set. We therefore
report 95% percentile bootstrap confidence intervals over test items,
resampling items with replacement 10,000 times per model–task cell and
recomputing the metric on each resample. For Single Object Tracking the
resampling unit is the object tracklet (n=200n=200) rather than the
individual frame, since frames within a tracklet are strongly correlated.

The half-width of each interval is given in Table [13](https://arxiv.org/html/2609.09396#A7.T13 "Table 13 ‣ G.1 Item-Level Confidence Intervals ‣ Appendix G Reported Uncertainty ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"). Interval width
is governed by the number of scored items, so it varies far more across
tasks than across models. Referring expressions and object localization
are the tightest (median ±\\pm1.00 and ±\\pm1.27 respectively), while event
verification is the widest by a wide margin (median ±\\pm7.47), reflecting
its smaller item pool and binary scoring. The practical consequence is
that the comparisons we draw in Section [4](https://arxiv.org/html/2609.09396#S4 "4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models") should be read
against very different resolutions: a two-point difference is meaningful
on referring expressions and is not meaningful on event verification.

SemanticSpatialTemporalSp.-Temp.ModelParamsVQAEVPoint.RefExObj Loc.Temp Loc.DVCSOTOpen-weight modelsQwen3-VL2B63.85 ±\\pm2.7644.73 ±\\pm7.5653.13 ±\\pm3.0865.12 ±\\pm1.1047.42 ±\\pm2.6835.21 ±\\pm2.2319.90 ±\\pm1.7730.38 ±\\pm2.83Qwen3-VL8B66.44 ±\\pm2.6859.39 ±\\pm7.6468.56 ±\\pm2.9473.29 ±\\pm1.0159.93 ±\\pm3.1144.32 ±\\pm2.4929.64 ±\\pm2.2633.12 ±\\pm2.90Qwen3-VL32B71.30 ±\\pm2.5560.04 ±\\pm7.6675.62 ±\\pm2.6472.39 ±\\pm1.0072.67 ±\\pm2.5146.80 ±\\pm2.4029.40 ±\\pm2.8744.19 ±\\pm2.98Qwen3.59B71.63 ±\\pm2.5146.78 ±\\pm7.6171.74 ±\\pm2.7977.16 ±\\pm0.9076.87 ±\\pm1.8142.53 ±\\pm2.4927.88 ±\\pm2.8723.52 ±\\pm2.47Qwen3.527B67.95 ±\\pm2.6855.34 ±\\pm7.7375.32 ±\\pm2.6476.35 ±\\pm0.8985.46 ±\\pm0.6436.88 ±\\pm2.2226.97 ±\\pm2.5324.40 ±\\pm2.35Cosmos-Reason22B64.69 ±\\pm2.7255.27 ±\\pm7.9759.70 ±\\pm3.0856.33 ±\\pm1.2473.56 ±\\pm1.6238.95 ±\\pm2.5328.52 ±\\pm3.1226.85 ±\\pm2.71Cosmos-Reason28B67.95 ±\\pm2.7264.09 ±\\pm7.7068.60 ±\\pm2.8970.26 ±\\pm1.0283.88 ±\\pm0.8947.30 ±\\pm2.5332.50 ±\\pm3.5037.69 ±\\pm3.12Cosmos-Reason232B70.29 ±\\pm2.5973.58 ±\\pm7.0074.03 ±\\pm2.7450.04 ±\\pm1.054.35†±\\pm0.9150.47 ±\\pm2.6530.04 ±\\pm3.1833.12 ±\\pm3.02Cosmos3-Edge4B62.68 ±\\pm2.7663.36 ±\\pm7.5167.76 ±\\pm2.8469.27 ±\\pm1.0979.02 ±\\pm0.7039.51 ±\\pm2.5716.64 ±\\pm2.8524.65 ±\\pm2.81Cosmos3-Nano16B68.95 ±\\pm2.6868.88 ±\\pm7.1674.83 ±\\pm2.6975.57 ±\\pm0.9974.11 ±\\pm1.7448.04 ±\\pm2.6131.42 ±\\pm3.8159.21 ±\\pm3.75Cosmos3-Super64B69.46 ±\\pm2.5971.28 ±\\pm7.1272.94 ±\\pm2.7476.23 ±\\pm0.9886.97 ±\\pm0.7051.90 ±\\pm2.5729.54 ±\\pm3.3164.66 ±\\pm3.67Gemma-4-E2B2B46.19 ±\\pm2.8527.65 ±\\pm4.5231.74 ±\\pm2.945.52 ±\\pm0.4045.40 ±\\pm0.749.02 ±\\pm1.109.14 ±\\pm1.8311.58 ±\\pm1.31Proprietary modelsGemini 3.1 Flash-Lite—68.03 ±\\pm2.7263.78 ±\\pm7.4763.68 ±\\pm2.9952.70 ±\\pm1.4171.74 ±\\pm1.3437.72 ±\\pm2.3632.54 ±\\pm2.4646.68 ±\\pm3.89Gemini 3.1 Pro—71.46 ±\\pm2.5568.57 ±\\pm7.2372.04 ±\\pm2.7967.17 ±\\pm1.2777.21 ±\\pm1.7345.69 ±\\pm2.3635.55 ±\\pm2.8267.88 ±\\pm3.98Gemini 3.5 Flash-Lite—65.61 ±\\pm2.6870.41 ±\\pm7.0643.08 ±\\pm3.0374.46 ±\\pm0.9765.73 ±\\pm1.2724.00 ±\\pm2.6732.29 ±\\pm2.3955.77 ±\\pm4.56Gemini 3.6 Flash—76.82 ±\\pm2.3882.00 ±\\pm6.2679.20 ±\\pm2.5475.78 ±\\pm0.8781.57 ±\\pm0.6151.50 ±\\pm2.6736.15 ±\\pm3.1675.99 ±\\pm3.44GPT-5.6 Sol—78.08 ±\\pm2.3876.14 ±\\pm6.7281.90 ±\\pm2.3969.44 ±\\pm0.9169.30 ±\\pm0.7255.71 ±\\pm2.6537.28 ±\\pm2.8875.02 ±\\pm3.34

Table 13: Scores with 95% item-level bootstrap confidence-interval half-widths (±\\pm), for
every cell of Table [1](https://arxiv.org/html/2609.09396#S4.T1 "Table 1 ‣ 4.2 Main Results ‣ 4 Evaluation Framework and Empirical Results ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models"), in points on the 0–100 scale
(10,000 resamples; tracking resampled at the tracklet level) \[ [44](https://arxiv.org/html/2609.09396#bib.bib44 "")\]. Scored
items per task: VQA 1195; EV 163; Point. 1005; RefEx 3276; Obj Loc. 628; Temp Loc. 203; DVC 104; SOT 200.

### G.2 Seed Variance

To confirm that reported differences are not seed-driven, we ran Qwen3-VL-8B three times with different random seeds (Table [14](https://arxiv.org/html/2609.09396#A7.T14 "Table 14 ‣ G.2 Seed Variance ‣ Appendix G Reported Uncertainty ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models")). Because decoding is greedy at temperature 0, this variance is expected to be small, and it is. All five tasks measured show a standard deviation below 0.5 points, with 2D Spatial Pointing and Single Object Tracking the largest at 0.42 and 0.40. This establishes that individual cells are reproducible across runs. It is not a basis for judging whether two models differ: seed variance holds the item set fixed and therefore omits the dominant source of uncertainty in benchmark scores, which is item sampling \[ [44](https://arxiv.org/html/2609.09396#bib.bib44 "")\]. For model comparisons, the item-level intervals above are the relevant quantity.

The dominant source of uncertainty is item sampling, which seed runs cannot measure. The variance reported here should therefore not be read as a confidence interval on the scores themselves; item-level bootstrap intervals for every model and task are reported separately in Appendix [G.1](https://arxiv.org/html/2609.09396#A7.SS1 "G.1 Item-Level Confidence Intervals ‣ Appendix G Reported Uncertainty ‣ VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models").

| Pillar | Task (metric) | Std. dev. across 3 seeds |
| --- | --- | --- |
| Semantic | Event Verification (Macro F1) | 0.310.31 |
| Semantic | Video Question Answering (Accuracy) | 0.090.09 |
| Spatial | 2D Spatial Pointing (Accuracy) | 0.420.42 |
| Temporal | Dense Video Captioning (SODAc) | 0.320.32 |
| Spatio-Temp. | Single Object Tracking (AUC) | 0.400.40 |

Table 14: Seed variance on VANTAGE-Bench (Qwen3-VL-8B), standard deviation across three random seeds, scaled 0–100. This reflects decoding randomness only, not item sampling.

## References

- \[1\]
Chaoyou Fu, Yuhan Dai, Yondong Luo, Lei Li, Shuhuai Ren, Renrui Zhang, Zihan Wang, Chenyu Zhou, Yunhang Shen, Mengdan Zhang, et al.

Video-MME: The first-ever comprehensive evaluation benchmark of multi-modal LLMs in video analysis.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2025.

- \[2\]
Kunchang Li, Yali Wang, Yinan He, Yizhuo Li, Yi Wang, Yi Liu, Zun Wang, Jilan Xu, Guo Chen, Ping Luo, Limin Wang, and Yu Qiao.

MVBench: A comprehensive multi-modal video understanding benchmark.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2024.

- \[3\]
Karttikeya Mangalam, Raiymbek Akshulakov, and Jitendra Malik.

EgoSchema: A diagnostic benchmark for very long-form video language understanding.

In _Advances in Neural Information Processing Systems (NeurIPS)_, 2023.

- \[4\]
Xingyu Fu, Yushi Hu, Bangzheng Li, Yu Feng, Haoyu Wang, Xudong Lin, Dan Roth, Noah A. Smith, Wei-Chiu Ma, and Ranjay Krishna.

BLINK: Multimodal large language models can see but not perceive.

In _Proceedings of the European Conference on Computer Vision (ECCV)_, 2024.

- \[5\]
Andreas Geiger, Philip Lenz, and Raquel Urtasun.

Are we ready for autonomous driving? The KITTI vision benchmark suite.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2012.

- \[6\]
Holger Caesar, Varun Bankiti, Alex H. Lang, Sourabh Vora, Venice Erin Liong, Qiang Xu, Anush Krishnan, Yuxin Pan, Giancarlo Baldan, and Oscar Beijbom.

nuScenes: A multimodal dataset for autonomous driving.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2020.

- \[7\]
Pei Sun, Henrik Kretzschmar, Xerxes Dotiwalla, Aurelien Chouard, Vijaysai Patnaik, Paul Tsui, James Guo, Yin Zhou, Yuning Chai, Benjamin Caine, et al.

Scalability in perception for autonomous driving: Waymo Open Dataset.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2020.

- \[8\]
Waqas Sultani, Chen Chen, and Mubarak Shah.

Real-world anomaly detection in surveillance videos.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2018.

- \[9\]
Sangmin Oh, Anthony Hoogs, Amitha Perera, Naresh Cuntoor, Chia-Chih Chen, Jong Taek Lee, Saurajit Mukherjee, J.K. Aggarwal, Hyungtae Lee, Larry Davis, et al.

A large-scale benchmark dataset for event recognition in surveillance video.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2011.

- \[10\]
Zheng Tang, Shuo Wang, David C. Anastasiu, Ming-Ching Chang, Anuj Sharma, Quan Kong, Munkhjargal Gochoo, Jun-Wei Hsieh, Tomasz Kornuta, et al.

The 10th AI City Challenge.

In _Proceedings of the European Conference on Computer Vision (ECCV) Workshops_, 2026.

- \[11\]
Jiyang Gao, Chen Sun, Zhenheng Yang, and Ram Nevatia.

TALL: Temporal activity localization via language query.

In _Proceedings of the IEEE International Conference on Computer Vision (ICCV)_, 2017.

- \[12\]
Ranjay Krishna, Kenji Hata, Frederic Ren, Li Fei-Fei, and Juan Carlos Niebles.

Dense-captioning events in videos.

In _Proceedings of the IEEE International Conference on Computer Vision (ICCV)_, 2017.

- \[13\]
Licheng Yu, Patrick Poirson, Shan Yang, Alexander C. Berg, and Tamara L. Berg.

Modeling context in referring expressions.

In _Proceedings of the European Conference on Computer Vision (ECCV)_, 2016.

- \[14\]
Heng Fan, Liting Lin, Fan Yang, Peng Chu, Ge Deng, Sijia Yu, Hexin Bai, Yong Xu, Chunyuan Liao, and Haibin Ling.

LaSOT: A high-quality benchmark for large-scale single object tracking.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2019.

- \[15\]
Lianghua Huang, Xin Zhao, and Kaiqi Huang.

GOT-10k: A large high-diversity benchmark for generic object tracking in the wild.

_IEEE Transactions on Pattern Analysis and Machine Intelligence_, 43(5):1562–1577, 2021.

- \[16\]
Anton Milan, Laura Leal-Taixé, Ian Reid, Stefan Roth, and Konrad Schindler.

MOT16: A benchmark for multi-object tracking.

_arXiv preprint arXiv:1603.00831_, 2016.

- \[17\]
Xiao Wang, Xiujun Shu, Zhipeng Zhang, Bo Jiang, Yaowei Wang, Yonghong Tian, and Feng Wu.

Towards more flexible and accurate object tracking with natural language: Algorithms and benchmark.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2021.

- \[18\]
Zhu Zhang, Zhou Zhao, Yang Zhao, Qi Wang, Huasheng Liu, and Lianli Gao.

Where does it exist: Spatio-temporal video grounding for multi-form sentences.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2020.

- \[19\]
Zongheng Tang, Yue Liao, Si Liu, Guanbin Li, Xiaojie Jin, Hongxu Jiang, Qian Yu, and Dong Xu.

Human-centric spatio-temporal video grounding with visual transformers.

_IEEE Transactions on Circuits and Systems for Video Technology_, 2021.

- \[20\]
Han Wang, Yanjie Wang, Yongjie Ye, Yuxiang Nie, and Can Huang.

Elysium: Exploring object-level perception in videos via MLLM.

In _Proceedings of the European Conference on Computer Vision (ECCV)_, 2024.

- \[21\]
En Yu, Liang Zhao, Yana Wei, Jinrong Yang, Dongming Wu, Lingyu Kong, Haoran Wei, Tiancai Wang, Zheng Ge, Xiangyu Zhang, and Wenbing Tao.

Merlin: Empowering multimodal LLMs with foresight minds.

In _Proceedings of the European Conference on Computer Vision (ECCV)_, 2024.

- \[22\]
Kaining Ying, Fanqing Meng, Jin Wang, Zhiqian Li, Han Lin, Yue Yang, Hao Zhang, Wenbo Zhang, Yuqi Lin, Shuo Liu, et al.

MMT-Bench: A comprehensive multimodal benchmark for evaluating large vision-language models towards multitask AGI.

In _Proceedings of the International Conference on Machine Learning (ICML)_, 2024.

- \[23\]
Xinhao Li, Ziang Yan, Desen Meng, Lu Dong, Xiangyu Zeng, Yinan He, Yali Wang, Yu Qiao, Yi Wang, and Limin Wang.

VideoChat-R1: Enhancing spatio-temporal perception via reinforcement fine-tuning.

_arXiv preprint arXiv:2504.06958_, 2025.

- \[24\]
Biao Wang, Wenwen Li, and Jiawei Ge.

R1-Track: Direct application of MLLMs to visual object tracking via reinforcement learning.

_arXiv preprint arXiv:2506.21980_, 2025.

- \[25\]
Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, et al.

SAM 3: Segment anything with concepts.

In _International Conference on Learning Representations (ICLR)_, 2026.

- \[26\]
Cheng-Yen Yang, Hsiang-Wei Huang, Wenhao Chai, Zhongyu Jiang, and Jenq-Neng Hwang.

SAMURAI: Motion-aware memory for training-free visual object tracking with SAM 2.

_IEEE Transactions on Image Processing_, 35:970–982, 2026.

- \[27\]
Xin Chen, Ben Kang, Wanting Geng, Jiawen Zhu, Yi Liu, Dong Wang, and Huchuan Lu.

SUTrack: Towards simple and unified single object tracking.

In _Proceedings of the AAAI Conference on Artificial Intelligence_, 2025.

- \[28\]
Ben Kang, Xin Chen, Simiao Lai, Yang Liu, Yi Liu, and Dong Wang.

Exploring enhanced contextual information for video-level object tracking.

In _Proceedings of the AAAI Conference on Artificial Intelligence_, 2025.

- \[29\]
Zhichao Sun, Yepeng Liu, Zhiling Su, Huachao Zhu, Yuliang Gu, Yuda Zou, Zelong Liu, Gui-Song Xia, Bo Du, and Yongchao Xu.

RefDrone: A challenging benchmark for referring expression comprehension in drone scenes.

_arXiv preprint arXiv:2502.00392_, 2025.

- \[30\]
NVIDIA.

PhysicalAI-SmartSpaces: A multi-camera 3D perception dataset for smart spaces.

[https://huggingface.co/datasets/nvidia/PhysicalAI-SmartSpaces](https://huggingface.co/datasets/nvidia/PhysicalAI-SmartSpaces ""), 2025.

- \[31\]
Haodong Duan, Junming Yang, Yuxuan Qiao, Xinyu Fang, Lin Chen, Yuan Liu, Xiaoyi Dong, Yuhang Zang, Pan Zhang, Jiaqi Wang, Dahua Lin, and Kai Chen.

VLMEvalKit: An open-source toolkit for evaluating large multi-modality models.

In _Proceedings of the 32nd ACM International Conference on Multimedia (ACM MM)_, pages 11198–11201, 2024.

- \[32\]
Junjie Zhou, Yan Shu, Bo Zhao, Boya Wu, Zhengyang Liang, Shitao Xiao, Minghao Qin, Xi Yang, Yongping Xiong, Bo Zhang, Tiejun Huang, and Zheng Liu.

MLVU: Benchmarking multi-task long video understanding.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2025.

- \[33\]
Liunian Harold Li, Pengchuan Zhang, Haotian Zhang, Jianwei Yang, Chunyuan Li, Yiwu Zhong, Lijuan Wang, Lu Yuan, Lei Zhang, Jenq-Neng Hwang, Kai-Wei Chang, and Jianfeng Gao.

Grounded language-image pre-training.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, 2022.

- \[34\]
Soichiro Fujita, Tsutomu Hirao, Hidetaka Kamigaito, Manabu Okumura, and Masaaki Nagata.

SODA: Story oriented dense video captioning evaluation framework.

In _Proceedings of the European Conference on Computer Vision (ECCV)_, 2020.

- \[35\]
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, and Yoav Artzi.

BERTScore: Evaluating text generation with BERT.

In _International Conference on Learning Representations (ICLR)_, 2020.

- \[36\]
NVIDIA.

NVIDIA Omniverse DRIVE Sim.

[https://developer.nvidia.com/drive/simulation](https://developer.nvidia.com/drive/simulation ""), 2025.

- \[37\]
Qwen Team.

Qwen3-VL technical report.

_arXiv preprint arXiv:2511.21631_, 2025.

- \[38\]
NVIDIA.

Cosmos3: Reasoning vision-language models for physical AI.

[https://huggingface.co/nvidia/Cosmos3-Super](https://huggingface.co/nvidia/Cosmos3-Super ""), 2026.

- \[39\]
Google DeepMind.

Gemma 4 model card.

[https://huggingface.co/google/gemma-4-e2b-it](https://huggingface.co/google/gemma-4-e2b-it ""), 2026.

- \[40\]
OpenAI.

GPT-5.6 Sol.

[https://openai.com/index/gpt-5-6/](https://openai.com/index/gpt-5-6/ ""), 2026.

- \[41\]
Google DeepMind.

Gemini 3.1 Pro model card.

[https://deepmind.google/models/model-cards/gemini-3-1-pro/](https://deepmind.google/models/model-cards/gemini-3-1-pro/ ""), 2026.

- \[42\]
NVIDIA.

Cosmos-Reason2: An open reasoning vision-language model for physical AI and robotics.

[https://docs.nvidia.com/cosmos/latest/reason2/index.html](https://docs.nvidia.com/cosmos/latest/reason2/index.html ""), 2026.

- \[43\]
Qwen Team.

Qwen3.5 model release.

[https://huggingface.co/Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B ""), 2026.

- \[44\]
Evan Miller.

Adding error bars to evals: A statistical approach to language model evaluations.

_arXiv preprint arXiv:2411.00640_, 2024.