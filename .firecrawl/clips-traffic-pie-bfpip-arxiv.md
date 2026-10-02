Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2507.21161v1 \[cs.CV\] 25 Jul 2025

# Seeing Beyond Frames: Zero-Shot Pedestrian Intention Prediction with Raw Temporal Video and Multimodal Cues \*Thanks:

1stPallavi Zambare
Affiliation: Departmrnt of computer science

Texas Tech University

Lubbock, USA

pzambare@ttu.edu
2ndVenkata Nikhil Thanikella
Affiliation: Departmrnt of computer science

Texas Tech University

Lubbock, USA

vthanike@ttu.edu
3rd Ying Liu
Affiliation: Departmrnt of computer science

Texas Tech University

Lubbock, USA

Y.Liu@ttu.edu

###### Abstract

Pedestrian intention prediction is essential for autonomous driving in complex urban environments. Conventional approaches depend on supervised learning over frame sequences and require extensive retraining to adapt to new scenarios. Here, we introduce BF PIP (Beyond Frames Pedestrian Intention Prediction), a zero-shot approach built upon Gemini 2.5 Pro. It infers crossing intentions directly from short, continuous video clips enriched with structured JAAD metadata. In contrast to GPT-4V–based methods that operate on discrete frames, BF-PIP processes uninterrupted temporal clips. It also incorporates bounding-box annotations and ego-vehicle speed via specialized multimodal prompts. Without any additional training, BF-PIP achieves 73% prediction accuracy, outperforming a GPT-4V baseline by 18 %. These findings illustrate that combining temporal video inputs with contextual cues enhances spatiotemporal perception and improves intent inference under ambiguous conditions. This approach paves the way for agile, retraining-free perception module in intelligent transportation system.

###### Index Terms:

Pedestrian Behavior Prediction, Multimodal Large Language Models
(MLLM), Zero-shot Learning, Video Understanding.

## I Introduction

As autonomous vehicles (AVs) increasingly become a reality in modern transportation. Consequently, the necessity for an accurate and timely understanding of pedestrian behavior has emerged as a critical safety requirement. Among the various behavioral cues, pedestrian crossing intention prediction is mainly essential for anticipating potential road conflicts and ensuring safe navigation in urban environments \[ [1](https://arxiv.org/html/2507.21161v1#bib.bib1 ""), [2](https://arxiv.org/html/2507.21161v1#bib.bib2 "")\]. Early research relied on handcrafted features such as trajectories, body orientation, and gaze, processed with RNNs or LSTMs to capture temporal dynamics \[ [3](https://arxiv.org/html/2507.21161v1#bib.bib3 ""), [4](https://arxiv.org/html/2507.21161v1#bib.bib4 "")\] Recently, approaches like Pedestrian Graph+ and STCrossingPose employed Graph Convolutional Networks (GCNs) to represent spatial relationships and enhance posebased inference \[ [5](https://arxiv.org/html/2507.21161v1#bib.bib5 ""), [6](https://arxiv.org/html/2507.21161v1#bib.bib6 "")\]. Transformer based methods like PIT-Block and IntFormer introduced enhanced spatiotemporal attention and outperformed earlier sequence models\[ [7](https://arxiv.org/html/2507.21161v1#bib.bib7 ""), [8](https://arxiv.org/html/2507.21161v1#bib.bib8 "")\].

Despite these advances, supervised methods depend on static image sequences, require extensive labeled data, and generalize poorly to novel environments \[ [2](https://arxiv.org/html/2507.21161v1#bib.bib2 ""), [9](https://arxiv.org/html/2507.21161v1#bib.bib9 ""), [10](https://arxiv.org/html/2507.21161v1#bib.bib10 "")\]. To overcome these limitations, Multimodal Large Language Models (MLLMs) such as GPT-4V, LLAVA, and GPT-4o have emerged. They offer robust zero-shot reasoning across vision and language inputs \[ [11](https://arxiv.org/html/2507.21161v1#bib.bib11 ""), [12](https://arxiv.org/html/2507.21161v1#bib.bib12 ""), [13](https://arxiv.org/html/2507.21161v1#bib.bib13 "")\]. OmniPredict \[ [14](https://arxiv.org/html/2507.21161v1#bib.bib14 "")\], a new benchmark using GPT-4o, established the probability of instruction-prompted multimodal inference. It predicted pedestrian behavior using scene images, bounding boxes, and vehicle speed. Although effective, it still processes discrete frame sequences, restraining its ability to capture motion cues like hesitation, body shifts, or gaze changes \[ [15](https://arxiv.org/html/2507.21161v1#bib.bib15 ""), [16](https://arxiv.org/html/2507.21161v1#bib.bib16 "")\].

Even at its best, OmniPredict employs static frame sequences and treats the scene as a series of discrete observations. This limits the temporal continuity that is naturally captured in video. In contrast, video-based inputs can capture motion dynamics, hesitation, gaze shifts, and interaction cues that are not easily inferred from still frames.

![Refer to caption](https://arxiv.org/html/2507.21161v1/24.png)

Fig. 1: BF-PIP Framework

In this work, we introduce BF-PIP, a zero-shot pedestrian intention prediction framework that leverages short video clips and along with structured metadata (bounding boxes and ego-vehicle speed) in a multimodal prompt to Gemini 2.5 Pro. In contrast to previous methods that relied on image sequences, our method allows for continuous motion capture, enabling spatiotemporal reasoning without the need for retraining. Evaluation was conducted using the JAADbeh\[ [19](https://arxiv.org/html/2507.21161v1#bib.bib19 "")\] dataset, a widely recognized benchmark in autonomous driving research. BF-PIP reached an impressive 73% accuracy in a zero-shot setting, representing an 18% improvement over the performance of GPT4V-PBP \[ [4](https://arxiv.org/html/2507.21161v1#bib.bib4 "")\] and outperforming OmniPredict\[ [14](https://arxiv.org/html/2507.21161v1#bib.bib14 "")\] by 6%, which is currently the leading MLLM-based approach. Without requiring additional training, BF-PIP outperforms domain-specific models in predicting pedestrian intent. Qualitative analysis confirms Gemini 2.5 Pro’s ability to interpret complex scenes using spatial and behavioral cues. An ablation study further quantifies the contribution of each input modality.

In conclusion, BF-PIP marks a significant advance beyond traditional vision-based models by directly analyzing continuous video streams with structured metadata. It operates within a prompt-driven, zero-shot framework. Results indicate that BF-PIP’s ability to process raw video input reduces the need for extensive preprocessing. This capability enables zero-shot intent prediction in unfamiliar environments, contributing to more efficient and safer autonomous driving operations.

## II Methodology

Gemini 2.5 Pro represents a significant advancement in multimodal AI, offering the ability to process and reason over rich combinations of video, image, and text data through a single prompt interface. Unlike previous models, Gemini 2.5 Pro natively supports raw video input, enabling temporally grounded understanding of pedestrian motion and scene context. In our experiments, we used the Google Gemini API to perform zero-shot pedestrian intention prediction tasks on the JAAD dataset \[ [2](https://arxiv.org/html/2507.21161v1#bib.bib2 "")\]through the Gemini 2.5 Pro model. Specifically, we focused on the JAADbeh subset \[ [2](https://arxiv.org/html/2507.21161v1#bib.bib2 "")\], which includes detailed annotations of pedestrian behavior and environmental factors.

### II-ATask Identification

Pedestrian crossing intention prediction is formulated as a binary classification task: the model must determine whether a pedestrian will cross or not cross the road within a fixed future time horizon. Given a temporal sequence of observations captured from the ego-vehicle’s front-facing camera, the goal is to anticipate the pedestrian’s crossing action 30 frames (1 second) into the future, referred to as the Time-To-Event (TTE). For each pedestrian instance, an observation window of 16 frames (approximately 0.5 seconds) immediately preceding the TTE point is defined. These frames capture the pedestrian’s motion history and environmental context leading up to the moment of prediction. This temporal segment is extracted following the JAAD benchmark protocol \[ [17](https://arxiv.org/html/2507.21161v1#bib.bib17 ""), [2](https://arxiv.org/html/2507.21161v1#bib.bib2 "")\], where t0 represents the last observed frame and prediction occurs at t0\+ TTE.

The task is defined under two input configurations: annotated and unannotated. In the annotated setting, short video clips are provided with per-frame pedestrian bounding boxes from the JAAD dataset, preserving temporal continuity and enabling precise spatial localization. In contrast, the unannotated setting involves raw video clips without bounding boxes, allowing assessment of Gemini 2.5 Pro’s ability to infer pedestrian intent solely from visual motion and contextual cues.

### II-BInput Modalities

The BF-PIP pipeline accepts three main types of input data to support pedestrian intention prediction. These modalities are incorporated either as visual embeddings within the video stream or as structured metadata attached to each instance.

- •


Short Video Clip: A temporally continuous short clip is constructed from the JAAD video sequences, capturing the target pedestrian within a 16-frame observation window. These clips maintain motion continuity and more closely resemble real-world perception compared to static image sequences.

- •


Bounding Box Coordinates: Each frame includes bounding box annotations (x, y, width, height) extracted from JAAD metadata. These are either rendered into the clip (for the annotated case) or provided as separate input (for the structured mode). They help localize the pedestrian in the scene and focus the model’s attention.

- •


Vehicle Speed: At each frame, vehicle speed is included as part of the ego-motion metadata to support contextual reasoning. For JAAD, categorical ego-speed values are used to indicate the trend of the vehicle’s motion (e.g., decelerating, maintaining constant speed, or accelerating).


This multimodal input (video, spatial annotations, and motion data) is embedded into a prompt that’s given to Gemini 2.5 Pro. The model is instructed to reason over these inputs and make a binary decision.

### II-CPrompt Construction and Inference Strategy

To enable zero-shot reasoning, a structured prompt is designed to embed the task context and input modality definitions, allowing Gemini 2.5 Pro to perform multimodal understanding directly from short video clips and associated metadata. The prompt consists of two stages:

Stage 1: Environment and Task Setup:

The first part of the prompt presents Gemini 2.5 Pro to its role as an autonomous vehicle equipped with a front-facing camera. It specifies the temporal nature of the input (a 16-frame video segment recorded at 30 FPS). It describes the metadata included per frame, including bounding boxes and ego-vehicle motion. The task is presented as a binary classification problem, requiring a decision on whether the observed pedestrian will cross the road.

![[Uncaptioned image]](https://arxiv.org/html/2507.21161v1/pro1.png)

Stage 2: Behavioral Reasoning and Output Constraints:

The second half of the prompt incorporates explicit reasoning steps to guide internal decision-making. These steps include the analysis of pedestrian posture, movement patterns, and surrounding visual cues. The classification labels are explicitly defined for the model. To ensure consistency and improve interpretability, the output is constrained to a single-word prediction.

![[Uncaptioned image]](https://arxiv.org/html/2507.21161v1/Pro2.png)

This structure for prompts was uniformly applied across all evaluation conditions, making them consistent and reproducible. The prompting logic that was built in enables Gemini 2.5 Pro to use its multimodal attention over visual and textual inputs to infer pedestrian intention without the use of fine-tuning. A strategy employing role-play prompting \[ [19](https://arxiv.org/html/2507.21161v1#bib.bib19 "")\] is used to enhance interpretability and decision-making. The role that Gemini 2.5 Pro plays is that of a situational observer, systematically analyzing such things as pedestrian motion cues, environmental conditions, and past behavioral patterns. By framing its role explicitly as an “intention predictor,” the model generates responses with more contextual awareness.

This role-play prompting strategy serves two primary objectives. First, it encourages behavioral alignment by reasoning rooted in human-like observational strategies, enabling predictions to align with real-world pedestrian behavior. Second, it enhances Contextual Fusion by multimodal integration by reinforcing attention on bounding box dynamics, trajectory shifts, and implicit social cues. Additionally, this approach complements chain-of thought prompting \[ [20](https://arxiv.org/html/2507.21161v1#bib.bib20 "")\], allowing the model to articulate stepwise decision-making before arriving at a binary prediction. By integrating role-play with structured multimodal inputs, reasoning depth and reliability are improved in zero-shot settings

By leveraging Gemini 2.5 Pro’s zero-shot multimodal reasoning capability, our method avoids task-specific training. Instead, it relies on carefully constructed prompts to guide pedestrian intention prediction. This prompt-based framework accepts both annotated and unannotated short video clips as input. It supports robust decision-making grounded in a temporally rich context. The integration of role-play framing, multimodal inputs, and structured reasoning yields a generalizable pipeline capable of handling diverse street scenes, making it well-suited for real-world autonomous driving scenarios.

In the last step of the procedure, Gemini 2.5 Pro is instructed to produce predictions in a structured JSON format to ensure consistency in output interpretation and evaluation. since Gemini 2.5 Pro is a generative model, whose outputs may vary across runs. To enhance determinism, the model is configured with a temperature of 0 and a fixed random seed of 0. Each prompt is executed five times per instance to evaluate response stability and ensure reliability.

TABLE I: Performance comparison with state-of-the-art methods from OmniPredict . The input modalities represent different data types: I: image, B: bounding box coordinates, P: skeleton-based pose, S: vehicle speed, and V: video input (short temporal clip).

| Models | Year | Model Variants | Inputs | JAAD-beh |
| --- | --- | --- | --- | --- |
|  |  |  | I | B | P | S | V | Extra Info. | ACC | AUC | F1 | P | R |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MultiRNN \[ [3](https://arxiv.org/html/2507.21161v1#bib.bib3 "")\] | 2018 | GRU | ✓ | ✓ | ✓ | ✓ | – | – | 0.61 | 0.50 | 0.74 | 0.64 | 0.86 |
| SFRNN \[ [4](https://arxiv.org/html/2507.21161v1#bib.bib4 "")\] | 2020 | GRU | ✓ | ✓ | ✓ | ✓ | – | – | 0.51 | 0.45 | 0.63 | 0.61 | 0.64 |
| SingleRNN \[ [2](https://arxiv.org/html/2507.21161v1#bib.bib2 "")\] | 2020 | GRU | ✓ | ✓ | ✓ | ✓ | – | – | 0.58 | 0.54 | 0.67 | 0.67 | 0.68 |
| PCPA \[ [17](https://arxiv.org/html/2507.21161v1#bib.bib17 "")\] | 2021 | RNN+Attention | ✓ | ✓ | ✓ | ✓ | – | – | 0.58 | 0.50 | 0.71 | – | – |
| IntFormer \[ [8](https://arxiv.org/html/2507.21161v1#bib.bib8 "")\] | 2022 | Transformer | ✓ | ✓ | ✓ | ✓ | – | – | 0.59 | 0.54 | 0.69 | – | – |
| ST CrossingPose \[ [6](https://arxiv.org/html/2507.21161v1#bib.bib6 "")\] | 2022 | Graph CNN | ✓ | ✓ | ✓ | – | – | – | 0.63 | 0.56 | 0.74 | 0.66 | 0.83 |
| FFSTP \[ [16](https://arxiv.org/html/2507.21161v1#bib.bib16 "")\] | 2022 | GRU+Attention | ✓ | ✓ | ✓ | ✓ | – | – | 0.62 | 0.54 | 0.74 | 0.65 | 0.85 |
| Pedestrian Graph+ \[ [5](https://arxiv.org/html/2507.21161v1#bib.bib5 "")\] | 2022 | Graph CNN+Attention | ✓ | ✓ | ✓ | ✓ | – | – | 0.70 | 0.70 | 0.76 | 0.77 | 0.75 |
| PIT-Block(a) \[ [7](https://arxiv.org/html/2507.21161v1#bib.bib7 "")\] | 2022 | Transformer | ✓ | ✓ | ✓ | ✓ | – | – | 0.70 | 0.65 | 0.81 | 0.71 | 0.93 |
| GPT4V-PBP \[ [15](https://arxiv.org/html/2507.21161v1#bib.bib15 "")\] | 2023 | MLLM | ✓ | ✓ | – | – | – | Text | 0.57 | 0.61 | 0.65 | 0.82 | 0.54 |
| GPT4V-PBP Skip \[ [15](https://arxiv.org/html/2507.21161v1#bib.bib15 "")\] | 2023 | MLLM | ✓ | ✓ | – | – | – | Text | 0.55 | 0.59 | 0.64 | 0.81 | 0.53 |
| OmniPredict \[ [14](https://arxiv.org/html/2507.21161v1#bib.bib14 "")\] | 2024 | MLLM | ✓ | ✓ | – | ✓ | – | Text | 0.67 | 0.65 | 0.65 | 0.66 | 0.65 |
| BF-PIP(Ours) | 2025 | MLLM | – | ✓ | – | ✓ | ✓ | Text | 0.73 | 0.77 | 0.80 | 0.96 | 0.69 |

## III Experiment and results

### III-ADataset

The experiments were conducted on the JAADbeh subset of the Joint Attention in Autonomous Driving (JAAD) dataset \[ [2](https://arxiv.org/html/2507.21161v1#bib.bib2 "")\]. It was recorded using front-facing dashboard cameras mounted on vehicles in diverse urban environments. The dataset was specifically organized to assess pedestrian intention in realistic traffic scenarios. The broader JAADall dataset includes all pedestrian instances, irrespective of crossing behavior. In contrast, JAADbeh was a focused subset containing 686 pedestrian instances who were either actively crossing or exhibiting intent to cross, each accompanied by detailed behavioral annotations.The full JAAD dataset contains 346 pedestrian video clips, divided into 188 for training, 32 for validation, and 126 for testing. For evaluation, only the 126 test clips were utilized. These test samples align with established benchmark configurations and were used for zero-shot inference. They also enable direct comparison with existing models such as PCPA and OmniPredict.

For each annotated pedestrian, a short video segment composed of 16 frames was extracted, ending 30 frames before the predicted Time-To-Event (TTE). The evaluation was conducted in two modes.

- •


Annotated mode: Bounding boxes are rendered on each frame to indicate the pedestrian of interest.

- •


Unannotated mode: The same clips are provided without any visual overlays. This allows us to assess Gemini 2.5 Pro’s capacity to infer pedestrian intent purely from raw visual input.


This dual-mode setup enables comprehensive evaluation under both structured and perceptual reasoning conditions. It also facilitates fair comparisons with both vision-based and prompt-driven models.

### III-BEvaluation metric

To evaluate how effectively pedestrian crossing intention was predicted in comparison to benchmark models, five standard classification metrics were used: Accuracy (ACC), Precision (P), Recall (R), F1 Score (F1), and Area Under the ROC Curve (AUC). These metrics provide a comprehensive assessment of overall model performance. They also capture class-wise discrimination, ensuring a balanced evaluation across varied crossing behaviors and prediction outcomes.

### III-CImplementation Setup

The Gemini 2.5 Pro–based evaluation pipeline was deployed using services provided by Google Cloud Platform (GCP). A dedicated GCP project was initialized with Vertex AI and Cloud Storage APIs enabled. A service account was configured with appropriate IAM roles (Vertex AI User and Storage Object Admin) to enable access to the Gemini API and Cloud Storage. All short video clips were uploaded to a Cloud Storage bucket and retrieved dynamically during inference.

For local execution, the environment was configured using standard GCP authentication and project variables to enable access to Vertex AI and Cloud Storage services. During each evaluation instance, Gemini 2.5 Pro received a structured prompt along with the corresponding video segment through the GenAI API. The prediction output was generated under the deterministic setup described in the methodology. It was then recorded and used for metric computation.

### III-DQuantitative results

To quantitatively assess model performance, Table 1 presents a comparative evaluation of the proposed BF-PIP model. It is compared against both classical domain-specific baselines and recent MLLM-based approaches on the JAADbeh benchmark. All models were predicting pedestrians crossing 30 frames ahead using 16 past frames. However, the GPT4V-PBP variants rely on 10-frame inputs. Conversely, the proposed BF-PIP model operates directly on short, continuous video clips to capture richer temporal context. The table also includes each model’s release year and the input modalities used for prediction. Model performance is evaluated using the five metrics introduced earlier: Accuracy (ACC), Area Under the ROC Curve (AUC), F1 Score (F1), Precision (P), and Recall (R).

Even without additional training, Gemini-based MLLM models establish competitive performance. In particular, the proposed BF-PIP model achieves the highest accuracy 0.73 and an AUC of 0.76. It also attains a strong F1 score of 0.80, which is only 0.01 lower than benchmark model PIT-Block(a). Importantly, BF-PIP records the highest precision 0.96, emphasizing its reliability in positive predictions. Additionally, it maintains a recall of 0.68, comparable to or exceeding existing Transformer-based baselines. Remarkably, BF-PIP achieves these results while relying on significantly fewer specialized features than other methods. These results demonstrate that BF-PIP’s hybrid use of bounding-box-guided attention and short-clip visual context is highly effective. It yields a new state of the art in pedestrian crossing intention prediction. It effectively balances high overall accuracy, low uncertainty, and strong reliability in positive class identification.

### III-EQualitative results

A qualitative analysis was conducted to examine how Gemini 2.5 Pro reasons interprets pedestrian behavior from video input. The study assessed the model’s attention to motion continuity, posture changes, and spatial context.

As illustrated in Fig. 2, the pedestrian in the red box was initially positioned on the sidewalk near a marked crosswalk. The model demonstrates strong contextual understanding by concurrently identifying relevant road users and analyzing traffic dynamics, such as scanning for oncoming vehicles. It also extracts environmental cues, including crosswalk markings and visual obstructions. Rather than treating all pedestrians equally, Gemini 2.5 Pro gives higher priority to individuals positioned closer to the roadway. Pedestrians standing near the curb edge receive more attention. The model also focuses on subtle behavioral cues such as leaning forward and looking toward traffic. Additionally, it considers small but decisive steps onto the crosswalk as strong indicators that the pedestrian is ready to cross. It also focuses on subtle behavioral cues, including posture shifts (a forward lean), gaze direction (observing traffic), and micro-movements (a decisive step onto the crosswalk) that indicate readiness to cross. By fusing spatial, temporal, and contextual information, the model generates robust predictions of pedestrian intention. This enables downstream planning modules to make more reliable and risk-aware decisions.

![Refer to caption](https://arxiv.org/html/2507.21161v1/22.png)

Fig. 2: Pedestrian crossing intention prediction.

### III-FAblation Study

An ablation study was conducted to isolate the impact of each input modality on BF-PIP performance. The 8 configurations were evaluated, including unannotated video (UV), annotated video (AV), bounding-box coordinates (BB), and ego-vehicle speed (S), both individually and in all pairwise combinations. All model predictions concern the crossing intent 30 frames ahead under identical conditions. Results are measured using the five metrics mentioned previously and are summarized in Table II.

TABLE II: Ablation study of input modalities. UV: unannotated video, AV: annotated video, BB: bounding box coordinates, S: ego-vehicle speed.

| Input Modality | ACC | AUC | F1 | P | R |
| --- | --- | --- | --- | --- | --- |
| UV | 0.65 | 0.62 | 0.74 | 0.96 | 0.60 |
| UV + S | 0.70 | 0.74 | 0.78 | 0.97 | 0.65 |
| UV + BB | 0.60 | 0.58 | 0.68 | 0.96 | 0.53 |
| UV + BB + S | 0.66 | 0.61 | 0.74 | 0.97 | 0.60 |
| AV | 0.64 | 0.61 | 0.73 | 0.95 | 0.59 |
| AV + S | 0.73 | 0.76 | 0.80 | 0.96 | 0.69 |
| AV + BB | 0.63 | 0.59 | 0.72 | 0.97 | 0.57 |
| AV + BB + S | 0.68 | 0.64 | 0.77 | 0.97 | 0.63 |

The base configuration using unannotated video (UV) alone achieves a strong F1 score of 0.74, demonstrating that Gemini 2.5 Pro can efficiently extract temporal features from raw visual input. When vehicle speed metadata (S) is added to the UV input, the model shows notable performance gains. Accuracy increases from 0.653 to 0.707, and AUC improves from 0.621 to 0.743. These gains highlight the importance of motion context in improving the model’s visual reasoning. Interestingly, combining unannotated video (UV) with bounding-box coordinates (BB) does not lead to significant performance gains. It lightly reduces both precision and recall. This result suggests that, in the absence of visual annotation overlays, raw coordinate inputs may be less interpretable within the video context. Conversely, configurations using annotated video (AV) consistently outperform UV-based setups. The AV-only baseline achieves 0.671 accuracy, and performance steadily improves as more modalities are added. The best performance is achieved with the AV + S configuration, reaching the highest accuracy of 0.73, an F1 score of 0.80. It also delivers strong precision and AUC values of 0.96 and 0.76, respectively.
These results confirm the importance of structured visual guidance (annotations), ego-vehicle context, and spatial grounding through bounding boxes. The observed incremental improvements in prediction accuracy validate the multimodal design of the BF-PIP model.

## IV Conclusion

The work presents BF-PIP, a zero-shot framework for predicting pedestrian crossing intent using Gemini 2.5 Pro’s multimodal reasoning. The task is framed as a binary classification problem on short video clips. These clips are either annotated or unannotated and are combined with ego-vehicle speed. Structured prompts provide scene context and behavioral cues to guide the model’s understanding. BF-PIP outperforms existing methods on the JAAD dataset. It performs well in both annotated and raw video settings and generalizes across different traffic scenes. Qualitative and ablation results highlight the value of bounding boxes, motion metadata, and temporal continuity. These results show that large multimodal models, when paired with thoughtful prompt design, can enable reliable intent prediction in autonomous driving systems.

## References

- \[1\] Amir Rasouli, Iuliia Kotseruba, Toni Kunic, and John K. Tsotsos. Pie: A large-scale dataset and models for pedestrian intention estimation and trajectory prediction. In International Conference on Computer Vision (ICCV), 2019

- \[2\] Iuliia Kotseruba, Amir Rasouli, and John K Tsotsos. Do they want to cross? understanding pedestrian intention for behavior prediction. In 2020 IEEE Intelligent Vehicles Symposium (IV), pages 1688–1693. IEEE, 2020.

- \[3\] Apratim Bhattacharyya, Mario Fritz, and Bernt Schiele. Long-term on-board prediction of people in traffic scenes under uncertainty. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 4194–4202, 2018.

- \[4\] Amir Rasouli, Iuliia Kotseruba, and John K Tsotsos. Pedestrian action anticipation using contextual feature fusion in stacked rnns. arXiv preprint arXiv:2005.06582, 2020.

- \[5\] Pablo Rodrigo Gantier Cadena, Yeqiang Qian, Chunxiang Wang, and Ming Yang. Pedestrian graph +: A fast pedestrian crossing prediction model based on graph convolutional networks. IEEE Transactions on Intelligent Transportation Systems, 23(11):21050–21061, 2022.

- \[6\] Xingchen Zhang, Panagiotis Angeloudis, and Yiannis Demiris. St crossingpose: A spatial-temporal graph convolutional network for skeleton-based pedestrian crossing intention prediction. IEEE Transactions on Intelligent Transportation Systems, 23(11):20773–20782, 2022.

- \[7\]Yuchen Zhou, Guang Tan, Rui Zhong, Yaokun Li, and Chao Gou. Pit: Progressive interaction transformer for pedestrian crossing intention prediction. IEEE Transactions on Intelligent Transportation Systems, 2023.

- \[8\]Javier Lorenzo, Ignacio Parra, and MA Sotelo. Intformer: Predicting pedestrian intention with the aid of the transformer architecture. arXiv preprint arXiv:2105.08647, 2021.

- \[9\]Ankur Singh and Upendra Suddamalla. Multi-input fusion for practical pedestrian intention prediction. In 2021 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW), pages 2304–2311, 2021.

- \[10\]Je-Seok Ham, Kangmin Bae, and Jinyoung Moon. Mcip: Multi-stream network for pedestrian crossing intention prediction. In European Conference on Computer Vision, pages 663–679. Springer, 2022

- \[11\]Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774, 2023

- \[12\]Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. Advances in neural information processing systems, 36, 2024.

- \[13\]Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023.

- \[14\]Ham, Je-Seok, Jia Huang, Peng Jiang, Jinyoung Moon, Yongjin Kwon, Srikanth Saripalli, and Changick Kim. ”OmniPredict: GPT-4o Enhanced Multi-modal Pedestrian Crossing Intention Prediction.” In Adaptive Foundation Models: Evolving AI for Personalized and Efficient Learning, NeurIPS,2024

- \[15\]Jia Huang, Peng Jiang, Alvika Gautam, and Srikanth Saripalli. Gpt-4v takes the wheel: Evaluating promise and challenges for pedestrian behavior prediction. arXiv preprint arXiv:2311.14786, 2023.

- \[16\]Dongfang Yang, Haolin Zhang, Ekim Yurtsever, Keith A Redmill, and Ümit Özgüner. Predicting pedestrian crossing intention with feature fusion and spatio-temporal attention. IEEE Transactions on Intelligent Vehicles, 7(2):221–230, 2022.

- \[17\]Iuliia Kotseruba, Amir Rasouli, and John K Tsotsos. Benchmark for evaluating pedestrian action prediction. In Proceedings of the IEEE/CVF winter conference on applications of computer vision, pages 1258–1268, 2021.

- \[18\] Google AI Studio

- \[19\] Shanahan, Murray, Kyle McDonell, and Laria Reynolds. ”Role play with large language models.” Nature 623, no. 7987 (2023): 493-498.

- \[20\]Feng, Guhao, Bohang Zhang, Yuntian Gu, Haotian Ye, Di He, and Liwei Wang. ”Towards revealing the mystery behind chain of thought: a theoretical perspective.” Advances in Neural Information Processing Systems 36 (2023): 70757-70798.