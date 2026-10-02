Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2412.01095v1 \[cs.AI\] 02 Dec 2024

# VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models

Muchao Ye     Weiyang Liu     Pan He
The University of Iowa   Max Planck Institute for Intelligent Systems – Tübingen   Auburn UniversityProject Page: [https://vera-framework.github.io](https://vera-framework.github.io/ "")

###### Abstract

The rapid advancement of vision-language models (VLMs) has established a new paradigm in video anomaly detection (VAD): leveraging VLMs to simultaneously detect anomalies and provide comprehendible explanations for the decisions. Existing work in this direction often assumes the complex reasoning required for VAD exceeds the capabilities of pretrained VLMs. Consequently, these approaches either incorporate specialized reasoning modules during inference or rely on instruction tuning datasets through additional training to adapt VLMs for VAD. However, such strategies often incur substantial computational costs or data annotation overhead. To address these challenges in explainable VAD, we introduce a verbalized learning framework named VERA that enables VLMs to perform VAD without model parameter modifications. Specifically, VERA automatically decomposes the complex reasoning required for VAD into reflections on simpler, more focused guiding questions capturing distinct abnormal patterns. It treats these reflective questions as learnable parameters and optimizes them through data-driven verbal interactions between learner and optimizer VLMs, using coarsely labeled training data. During inference, VERA embeds the learned questions into model prompts to guide VLMs in generating segment-level anomaly scores, which are then refined into frame-level scores via the fusion of scene and temporal contexts. Experimental results on challenging benchmarks demonstrate that the learned questions of VERA are highly adaptable, significantly improving both detection performance and explainability of VLMs for VAD.

### 1 Introduction

![Refer to caption](https://arxiv.org/html/2412.01095v1/fig1.png)Figure 1: VERA renders frozen VLMs to describe and reason with learnable guiding questions learned from coarsely labeled data.

Video anomaly detection (VAD) aims to automatically identify unexpected and abnormal events in video sequences, with broad applications ranging from autonomous driving \[ [2](https://arxiv.org/html/2412.01095v1#bib.bib2 "")\] to industrial manufacturing \[ [34](https://arxiv.org/html/2412.01095v1#bib.bib34 "")\]. While achieving good performance in VAD is essential, providing clear explanations for detected anomalies is even more crucial.

To this end, our work primarily focuses on explainable VAD, which requires both comprehensive visual understanding and the ability to generate human-interpretable predictions. The rapid advancement of vision language models (VLMs) \[ [20](https://arxiv.org/html/2412.01095v1#bib.bib20 ""), [8](https://arxiv.org/html/2412.01095v1#bib.bib8 ""), [61](https://arxiv.org/html/2412.01095v1#bib.bib61 ""), [23](https://arxiv.org/html/2412.01095v1#bib.bib23 "")\] enables us to address both requirements through their strong visual reasoning and language interaction capabilities. As multi-modal architectures that effectively combine the reasoning capabilities from large language models (LLMs) \[ [4](https://arxiv.org/html/2412.01095v1#bib.bib4 "")\] and the visual understanding capabilities from pretrained vision encoders \[ [9](https://arxiv.org/html/2412.01095v1#bib.bib9 "")\], VLMs are particularly well-suited for VAD for they can offer explainable predictions that clearly illustrate the rationale behind specific anomalies, making the results more interpretable to users. Recent research on VAD has consequently focused on how to effectively leverage the power of pretrained VLM. As shown in Fig. [1](https://arxiv.org/html/2412.01095v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), existing approaches aim to address the misalignment problem between VLMs’ pretraining tasks and the VAD requirements through either additional reasoning modules or instruction tuning (IT):

- •


One line of research _introduces external LLMs to assist frozen VLMs to reason in VAD_\[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 ""), [49](https://arxiv.org/html/2412.01095v1#bib.bib49 "")\].
It uses VLMs to caption what they see given a video, and the descriptions are then passed to an external LLM, _e.g_., GPT-4 \[ [1](https://arxiv.org/html/2412.01095v1#bib.bib1 "")\], to reason whether an anomaly occurs.

- •


Another line of research, instead, _expands VLMs to generate explainable prediction via IT_\[ [29](https://arxiv.org/html/2412.01095v1#bib.bib29 ""), [58](https://arxiv.org/html/2412.01095v1#bib.bib58 "")\].
This research line creates additional VAD datasets with frame-level annotations and leverages exemplary instructions to fine-tune the VLM, enabling it to detect anomalies and generate human-interpretable explanations.


Key Observations and Research Question. While prior research demonstrates the potential of applying VLMs to VAD, we identify that this new paradigm is hindered by a shared critical issue: the use of additional reasoning modules or fine-grained labeled datasets incurs significant computational cost either in the inference or training phases. First, decoupling a VAD system into a frozen VLM and an extra LLM introduces more overhead in inference, because it separates the description generation and reasoning processes. Secondly, although IT-based methods enable VLMs to effectively integrate description and reasoning for VAD, they require additional manpower and computational resources for annotating and finetuning on fine-grained labeled instruction datasets, which is time-consuming and not scalable for large-scale datasets. In light of this, we investigate the following unexplored yet important question:

_Can we enable a frozen VLM to integrate description and reasoning for VAD without instruction tuning?_

Our Approach. This research question is nontrivial because the reasoning ability of a frozen VLM is limited in general visual tasks, and it struggles to handle complex reasoning tasks like VAD, which requires the understanding of subtle, context-dependent outliers. To illustrate, Table [1](https://arxiv.org/html/2412.01095v1#S1.T1 "Table 1 ‣ 1 Introduction ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") shows that prompting frozen VLMs with simple VAD questions used in existing works leads to unsatisfactory results. Thus, instruction-tuning a VLM seems necessary to make it responsive to specific instructional cues and capture delicate visual variations. In this paper, we question the necessity of such an operation and propose a principled approach to tailor frozen VLMs for VAD.

Specifically, our solution is guided by the intuition that the reasoning ability of VLMs for VAD will improve if we find questions with suitable and concrete description of abnormal patterns rather than with abstract and general words like “anomaly” to prompt them. Our idea is to iteratively refine anomaly descriptions from abstract ones ( _e.g_., “is there any anomaly?”) to detailed, specific characterizations.

Driven by such insight, we propose a framework, termed VERA, to explore verbalized learning for VAD. This framework considers the practical constraint that it is suboptimal to manually write down VAD guiding questions across VLMs, so it introduces a data-driven learning task to identify suitable anomaly-characterization questions containing concrete abnormal patterns for the frozen VLM using coarsely labeled datasets, eliminating the need for IT. Specifically, in the training phase, VERA treats the questions guiding the reasoning of VLMs in VAD as learnable parameters, improving them based on the verbal feedback from an optimizer VLM on the performance of a learner VLM on an intermediate VAD subtask—binary video classification for each video in the VAD training set. This design is both efficient and appropriate for VAD, as it accounts for video-specific properties like temporality while relying solely on provided coarse video-level labels.
After that, considering the large scale of video frames, VERA assigns a fine-grained anomaly score for each frame in a coarse-to-fine manner in the inference phase. First, VERA generates segment-level anomaly scores by querying VLMs with the learned guiding questions. Next, VERA improves the initial score by incorporating scene context into each segment score via ensembling. Finally, VERA outputs frame-level scores by fusing temporal context via Gaussian smoothing and frame-level position weighting.

| VAD Question for InternVL2-8B | AUC (%) |
| --- | --- |
| “Describe the video and is there any anomaly?” \[ [29](https://arxiv.org/html/2412.01095v1#bib.bib29 "")\] | 53.05 |
| “Are there any abnormal events in the video?” \[ [58](https://arxiv.org/html/2412.01095v1#bib.bib58 "")\] | 65.03 |

Table 1: Instructing a frozen VLM (InternVL2-8B \[ [8](https://arxiv.org/html/2412.01095v1#bib.bib8 "")\]) with simple questions to perform VAD yields poor AUC on UCF-Crime \[ [35](https://arxiv.org/html/2412.01095v1#bib.bib35 "")\] dataset.

Contributions. To sum up, our contributions are:

- •


To our knowledge, we present the first approach, that is, VERA, to adapt frozen VLMs as an integrated system for VAD by learning detailed anomaly-characterization questions in prompts that decompose anomalies into concrete and recognizable patterns. VERA learns them directly from coarsely labeled datasets, eliminating the need for IT or external reasoning modules.

- •


We introduce an effective verbalized learning-based algorithm for VLMs in VAD, allowing direct adaptation without modifying model parameters. With coarse labeled VAD datasets only, our approach obtains good guiding questions in VAD by relying on the verbal interaction between learner and optimizer VLMs in verbalized training. Additionally, we design a coarse-to-fine strategy to derive frame-level anomaly scores from verbally learned guiding questions in VAD, integrating both scene and temporal contexts for better VAD performance and reasoning.

- •


The learned guiding questions from VERA are expressed in natural languages, providing a unified method to encode and transfer prior VAD knowledge seamlessly to other datasets or VLMs. In challenging VAD datasets like UCF-Crime \[ [35](https://arxiv.org/html/2412.01095v1#bib.bib35 "")\] and XD-Violence \[ [45](https://arxiv.org/html/2412.01095v1#bib.bib45 "")\], VERA achieves state-of-the-art explainable VAD performance and enjoys good generalization ability across models and datasets.


### 2 Related Work

Video Anomaly Detection. VAD is the task of localizing frames that contain abnormal events in a given video. This task is challenging for anomalies cover a broad scope of events like accidents and criminal activities while training sets only offer coarse annotations. Modern VAD methods are based on deep neural networks (DNNs) for their superiority and are going through a paradigm shift in using VLMs: (1) Early DNNs for VAD are task-specific, which often employ unsupervised (including one-class) or weakly supervised (WS) learning techniques for training. Most unsupervised learning methods \[ [25](https://arxiv.org/html/2412.01095v1#bib.bib25 ""), [51](https://arxiv.org/html/2412.01095v1#bib.bib51 ""), [59](https://arxiv.org/html/2412.01095v1#bib.bib59 ""), [41](https://arxiv.org/html/2412.01095v1#bib.bib41 ""), [28](https://arxiv.org/html/2412.01095v1#bib.bib28 ""), [40](https://arxiv.org/html/2412.01095v1#bib.bib40 "")\] train DNNs on frame reconstruction/prediction tasks to establish representation spaces for normal/abnormal videos. WS learning methods \[ [35](https://arxiv.org/html/2412.01095v1#bib.bib35 ""), [6](https://arxiv.org/html/2412.01095v1#bib.bib6 ""), [50](https://arxiv.org/html/2412.01095v1#bib.bib50 ""), [56](https://arxiv.org/html/2412.01095v1#bib.bib56 ""), [30](https://arxiv.org/html/2412.01095v1#bib.bib30 "")\] leverage both normal and abnormal videos to train a feature extractor that distinguishes anomalies from normalcy, typically using multiple instance learning \[ [35](https://arxiv.org/html/2412.01095v1#bib.bib35 "")\] objectives. (2) Recent VAD methods adopt VLMs due to their remarkable success across core vision tasks \[ [31](https://arxiv.org/html/2412.01095v1#bib.bib31 ""), [23](https://arxiv.org/html/2412.01095v1#bib.bib23 ""), [13](https://arxiv.org/html/2412.01095v1#bib.bib13 "")\]. Early research \[ [58](https://arxiv.org/html/2412.01095v1#bib.bib58 ""), [55](https://arxiv.org/html/2412.01095v1#bib.bib55 ""), [49](https://arxiv.org/html/2412.01095v1#bib.bib49 ""), [29](https://arxiv.org/html/2412.01095v1#bib.bib29 "")\] has leveraged VLMs to generate textual descriptions of detected anomalies to enhance prediction explainability for VAD. However, current approaches incur high processing demands from external LLMs or require substantial effort and cost for fine-tuning on additional datasets, which are computationally inefficient in training or inference. Our work reduces the processing overhead by adapting frozen VLMs for VAD without model parameter modification or extra reasoning modules via learnable guiding questions, which elicit superior reasoning from frozen VLMs and significantly boost their performance in VAD.

Verbalized Learning for VLMs. The designed verbalized learning framework is inspired by a recent technique called verbalized machine learning (VML) \[ [47](https://arxiv.org/html/2412.01095v1#bib.bib47 "")\]. The main idea of VML is to use LLMs to approximate functions and learn the verbal rules and descriptions of performing specific tasks, which casts traditional machine learning tasks such as regression and classification as language-based learning tasks. This approach regards the language expressions that define classification rules and other task-specific criteria as learned parameters, and optimize them in a data-driven fashion through interactions between a learner and an optimizer modeled by LLMs or VLMs. However, the VML framework is limited to tasks involving regression on scalar values or classification for static images. Later, another concurrent method, TextGrad \[ [52](https://arxiv.org/html/2412.01095v1#bib.bib52 "")\], is proposed under a similar idea, which integrates the process of incorporating textual feedback from LLMs for improving prompts in PyTorch and further proves its effectiveness in coding, question answering, and optimization in chemistry and medicine.
Compared to existing works, our work pioneers verbalized learning for the VAD task and video data, which remains unsolved for previous verbalized learning frameworks focus on tasks with static input data and cannot handle the challenges of temporality and scene dynamics in the input for a complex visual reasoning task like VAD. Specifically, VERA introduces a new learning paradigm for VAD: generating effective questions that encapsulate key abnormal patterns in videos to elicit the reasoning ability from VLMs for explainable VAD. Additionally, VERA works for any VAD dataset and supports WS learning. Unlike previous WS methods, VERA only needs to learn concise text but not millions of parameters, so the training is lightweight.

### 3 The VERA Framework

![Refer to caption](https://arxiv.org/html/2412.01095v1/fig2.png)Figure 2: The overall training pipeline in VERA aims to optimize VAD guiding questions iteratively. In each iteration, the optimization is verbalized by providing verbal instructions for the learner and optimizer to follow. They will generate predictions and new guiding questions, respectively.

Our approach adapts VLMs to detect video anomalies without additional reasoning modules or instruction tuning. We now formulate the VAD task and detail the design of VERA.

#### 3.1 Problem Formulation

Video Anomaly Detection. Let VV be a video with FF frames, represented as V={Ii}i=1FV=\\{I\_{i}\\}\_{i=1}^{F}, where IiI\_{i} is the ii-th frame (1≤i≤F)(1\\leq i\\leq F). Our objective is to locate and detect the start and end of anomalous events within VV. In standard labeling, any frame associated with an anomaly is labeled as 1, and normal frames are labeled as 0. Therefore, the ground truth label sequence for VV is Y=\[y1,…,yF\]Y=\[y\_{1},\\dots,y\_{F}\], where yi∈{0,1}y\_{i}\\in\\{0,1\\} represents the fine-grained label for IiI\_{i}. We aim to use a frozen VLM, fVLMf\_{\\text{VLM}}, to generate anomaly score predictions across all frames, Y^=\[y^1,…,y^F\]\\hat{Y}=\[\\hat{y}\_{1},\\dots,\\hat{y}\_{F}\], where y^i∈\[0,1\]\\hat{y}\_{i}\\in\[0,1\] is a continuous anomaly score for IiI\_{i}.

Available Training Data for VAD. Typically, VAD datasets only provide coarsely labeled training sets \[ [35](https://arxiv.org/html/2412.01095v1#bib.bib35 ""), [45](https://arxiv.org/html/2412.01095v1#bib.bib45 ""), [25](https://arxiv.org/html/2412.01095v1#bib.bib25 ""), [28](https://arxiv.org/html/2412.01095v1#bib.bib28 "")\]. We denote a VAD training set as 𝒟={(V(j),Y(j))}j=1N\\mathcal{D}=\\{(V^{(j)},Y^{(j)})\\}\_{j=1}^{N}, where NN is the total number of training videos, V(j)V^{(j)} represents the jj-th video (1≤j≤N)(1\\leq j\\leq N) and Y(j)Y^{(j)} is the corresponding video-level label. Y(j)=1Y^{(j)}=1 if V(j)V^{(j)} contains any anomaly defined by the dataset annotators, _e.g_., abuse or arson activities, and Y(j)=0Y^{(j)}=0 if V(j)V^{(j)} has no anomalies. For V(j)V^{(j)}, we suppose it contains FjF\_{j} frames and denote the frames sequence as V(j)={Ii(j)}i=1FjV^{(j)}=\\{I\_{i}^{(j)}\\}\_{i=1}^{F\_{j}}, where Ii(j)I\_{i}^{(j)} is the ii-th frame (1≤i≤Fj1\\leq i\\leq F\_{j}) in V(j)V^{(j)}.

#### 3.2 Training in VERA: Finding Guiding Questions for VAD via Verbalized Learning

Training Objective. We aim to learn guiding questions that break down a complex and ambiguous concept ( _i.e_., what is an “anomaly”) into a set of identifiable anomalous patterns to unlock reasoning capabilities within frozen VLMs for VAD tasks. Those patterns vary among datasets, making manually designed descriptions ineffective for generalization. To address this, we propose a general verbalized learning framework shown in Fig. [2](https://arxiv.org/html/2412.01095v1#S3.F2 "Figure 2 ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") to generate the desired guiding questions. We denote the guiding question set as 𝐐={q1,…,qm}\\mathbf{Q}=\\{q\_{1},\\dots,q\_{m}\\}, where qiq\_{i} is the ii-th question (1≤i≤m1\\leq i\\leq m) and mm is the number of questions. The training framework considers 𝐐\\mathbf{Q} as the learnable parameters, which are optimized through verbal interaction between a learner and an optimizer, modeled by VLMs through leveraging their ability to follow instructions with given prompts.

Training Data. The training data for learning 𝐐\\mathbf{Q} consist of paired sampled video frames and video-level labels. Sampling is necessary because the amount of video frames is so huge that we cannot compute with every frame. We explore three types of sampling strategies and find that uniform sampling \[ [57](https://arxiv.org/html/2412.01095v1#bib.bib57 "")\] yields the best results. We will use it for illustration here, and please refer to the experiment section for details on other sampling methods. To illustrate, with any video V(j)∈𝒟V^{(j)}\\in\\mathcal{D}, we first calculate the interval between sampled frames as l=floor​(Fj/S)l=\\text{floor}(F\_{j}/S), where SS is the number of sampled frames, and floor denotes rounding down to the nearest integer. Given ll, the uniformly sampled frames from V(j)V^{(j)} are represented by V~(j)=\[I1(j),Il+1(j),…,I(S−1)⋅l+1(j)\]\\tilde{V}^{(j)}=\[I\_{1}^{(j)},I\_{l+1}^{(j)},\\dots,I\_{(S-1)\\cdot l+1}^{(j)}\]. The label used for training is Y(j)Y^{(j)} only, resulting in training data pairs {(V~(j),Y(j))}j=1N\\{(\\tilde{V}^{(j)},Y^{(j)})\\}\_{j=1}^{N} for VERA.

Updating 𝐐\\mathbf{Q} via Learner and Optimizer. Since 𝐐\\mathbf{Q} are verbal expressions for specific anomaly patterns, VERA inherits the idea of VML \[ [47](https://arxiv.org/html/2412.01095v1#bib.bib47 "")\] in training: optimizing language-based parameters by verbal communication between a learner agent flearnerf\_{\\rm learner} and an optimizer agent foptf\_{\\rm opt}, rather than by numerical optimization algorithms like Adam \[ [18](https://arxiv.org/html/2412.01095v1#bib.bib18 "")\]. We take an arbitrary iteration tt for illustration in this section. Please refer to Algorithm [1](https://arxiv.org/html/2412.01095v1#algorithm1 "Algorithm 1 ‣ A.1 Algorithm ‣ Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") in Sec. [A](https://arxiv.org/html/2412.01095v1#A1 "Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") for the complete iterative training in VERA.

Learner and Optimizer. We denote any LLM-based model as f⁡(x,ϕ)f(x;\\phi) where xx represents the input data, and ϕ\\phi denotes the natural language instructions for ff to follow, which is considered as learnable parameters in our verbalized learning framework. Specifically, 𝐐\\mathbf{Q} contains parameters to be learned in VERA. As depicted in Fig. [2](https://arxiv.org/html/2412.01095v1#S3.F2 "Figure 2 ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), in each iteration tt, the learner agent flearner(t)f\_{\\text{learner}}^{(t)} is modeled by the frozen VLM fVLM​(⋅)f\_{\\text{VLM}}(\\cdot) used for VAD with a specific prompt template θ\\theta that guide fVLM​(⋅)f\_{\\text{VLM}}(\\cdot) to conduct a learning task by pondering on current guiding questions 𝐐t\\mathbf{Q}\_{t}. We denote the learner agent as
flearner(t)​(x)=fVLM​(x,(θ,𝐐t))f\_{\\text{learner}}^{(t)}(x)=f\_{\\text{VLM}}(x;(\\theta,\\mathbf{Q}\_{t})), where xx is the input in a learning task, and 𝐐t\\mathbf{Q}\_{t}, the learnable guiding questions applied in each iteration tt, constitutes the core parameters that distinguish the learner between iterations. Meanwhile, we introduce an optimizer fopt(t)f\_{\\text{opt}}^{(t)} to assess the quality of the predictions of the learner and to optimize 𝐐t\\mathbf{Q}\_{t}. W.l.o.g., we use the same frozen VLM fVLMf\_{\\rm VLM} to model the optimizer. As demonstrated in Fig. [2](https://arxiv.org/html/2412.01095v1#S3.F2 "Figure 2 ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), we provide another specific prompt template ψ\\psi for the learner to follow to optimize 𝐐t\\mathbf{Q}\_{t}, so we denote the optimizer agent as fopt(t)​(z)=fVLM​(z,(ψ,𝐐t))f\_{\\text{opt}}^{(t)}(z)=f\_{\\text{VLM}}(z;(\\psi,\\mathbf{Q}\_{t})), where zz is its input and ψ\\psi is the instruction to improve 𝐐t\\mathbf{Q}\_{t}.
It is important to note that flearner(t)≠fopt(t)f\_{\\text{learner}}^{(t)}\\neq f\_{\\text{opt}}^{(t)} because flearner(t)f\_{\\text{learner}}^{(t)} follows (θ,𝐐t)(\\theta,\\mathbf{Q}\_{t}) to conduct a learning task, while fopt(t)f\_{\\text{opt}}^{(t)} follows (ψ,𝐐t)(\\psi,\\mathbf{Q}\_{t}) to refine 𝐐t\\mathbf{Q}\_{t}.

_Learning Task for flearnerf\_{\\rm learner}_. The learner executes the “forward pass” and outputs a prediction. Recall that we only use the original coarsely labeled information for training. Thus, we design a binary classification task for flearnerf\_{\\rm learner}, which accounts for the temporal nature of video data, the sparsity of anomalies, and the weak supervision in VAD datasets. In this task, the job of the learner flearnerf\_{\\rm learner} is to produce a binary classification prediction Y^(j)\\hat{Y}^{(j)} to determine whether there is an anomaly in the video based on the sampled frames V~(j)\\tilde{V}^{(j)}. As shown in Fig. [2](https://arxiv.org/html/2412.01095v1#S3.F2 "Figure 2 ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), we explain the task in natural language in the “Model Description” section in θ\\theta. Guiding questions 𝐐t\\mathbf{Q}\_{t} are inserted in the “Prompt Questions” section in θ\\theta to elicit reasoning of the VLM. This template design is based on the prompt structures used in VML, with targeted modifications to help the learner effectively address this WS learning task. Due to the space limit, please refer to the Appendix for detailed information on θ\\theta. Given θ\\theta and a sampled frame set V~(j)\\tilde{V}^{(j)}, the learner will output a prediction as

|     |     |     |     |
| --- | --- | --- | --- |
|  | Y^(j)=flearner(t)​(V~(j)),\\hat{Y}^{(j)}=f\_{\\rm learner}^{(t)}(\\tilde{V}^{(j)}), |  | (1) |

where Y^(j)=1\\hat{Y}^{(j)}=1 if the learner thinks there is an anomaly after skimming across the sampled frames V~(j)\\tilde{V}^{(j)} and reasoning through the guiding questions 𝐐t\\mathbf{Q}\_{t}, and otherwise, Y^i=0\\hat{Y}\_{i}=0.

_Optimization Step in foptf\_{\\rm opt}_. The optimizer executes the “backward pass” to update the questions 𝐐t\\mathbf{Q}\_{t} via a mini-batch (batch size is nn). Suppose the visual input in a batch is Vbatch=\[V~batch(1),⋯,V~batch(n)\]V\_{\\rm batch}=\[\\tilde{V}^{(1)}\_{\\rm batch},\\cdots,\\tilde{V}^{(n)}\_{\\rm batch}\] and the corresponding ground truths are Ybatch=\[Ybatch(1),⋯,Ybatch(n)\]Y\_{\\rm batch}=\[Y^{(1)}\_{\\rm batch},\\cdots,Y^{(n)}\_{\\rm batch}\]. The learner generates prediction as Y^batch=\[Y^batch(1),⋯,Y^batch(n)\]\\hat{Y}\_{\\rm batch}=\[\\hat{Y}^{(1)}\_{\\rm batch},\\cdots,\\hat{Y}^{(n)}\_{\\rm batch}\] with the current questions 𝐐t\\mathbf{Q}\_{t} by Eq. ( [1](https://arxiv.org/html/2412.01095v1#S3.E1 "Equation 1 ‣ 3.2 Training in VERA: Finding Guiding Questions for VAD via Verbalized Learning ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")). The optimizer will output a new set of questions 𝐐t+1\\mathbf{Q}\_{t+1} by following the prompt ψ\\psi with batched data. We denote the optimization step as

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝐐t+1=fopt(t)​(Vbatch,Y^batch,Ybatch),\\mathbf{Q}\_{t+1}=f\_{\\rm opt}^{(t)}(V\_{\\rm batch},\\hat{Y}\_{\\rm batch},Y\_{\\rm batch}), |  | (2) |

where 𝐐t+1\\mathbf{Q}\_{t+1} is a new set of guiding questions constructed from fopt(t)f\_{\\rm opt}^{(t)} owing to its text generation and instruction following abilities after reading ψ\\psi. Due to space constraints, please refer to the Appendix for information about ψ\\psi. As shown in Algorithm [1](https://arxiv.org/html/2412.01095v1#algorithm1 "Algorithm 1 ‣ A.1 Algorithm ‣ Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") in the Appendix, we will repeat Eq. ( [1](https://arxiv.org/html/2412.01095v1#S3.E1 "Equation 1 ‣ 3.2 Training in VERA: Finding Guiding Questions for VAD via Verbalized Learning ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) and Eq. ( [2](https://arxiv.org/html/2412.01095v1#S3.E2 "Equation 2 ‣ 3.2 Training in VERA: Finding Guiding Questions for VAD via Verbalized Learning ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) for PP iterations to optimize 𝐐\\mathbf{Q}. We denote the one with the largest validation accuracy as 𝐐∗\\mathbf{Q^{\*}}.

#### 3.3 Inference in VERA: Coarse-to-Fine Anomaly Scoring by Guiding Questions and Contexts

Given 𝐐∗\\mathbf{Q}^{\*}, VERA yields fine-grained anomaly score Y^\\hat{Y} for a test video VV via a coarse-to-fine process shown in Fig. [3](https://arxiv.org/html/2412.01095v1#S3.F3 "Figure 3 ‣ 3.3 Inference in VERA: Coarse-to-Fine Anomaly Scoring by Guiding Questions and Contexts ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models").

Step 1: Initial Anomaly Scores via Learned Guiding Questions. We divide the video into segments and analyze each segment independently first. Following \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\], we perform equidistant frame sampling within VV to obtain the set of each segment center 𝒞\\mathcal{C}, resulting in 𝒞={I1,Id+1,⋯,I(h−1)⋅d+1}\\mathcal{C}=\\{I\_{1},I\_{d+1},\\cdots,I\_{(h-1)\\cdot d+1}\\}, where dd is the interval between centers and h=floor⁡(F/d)h={\\rm floor}(F/d) is the total number of segments. For each center frame I(u−1)⋅d+1I\_{(u-1)\\cdot d+1} (1≤u≤h1\\leq u\\leq h), we define a 10-second window around it as the uu-th segment, within which we uniformly sample 8 frames. We denote the sampled frame set in the uu-th segment as VuV\_{u}. Next, we input VuV\_{u} in fVLMf\_{\\rm VLM} with the prompt (θ,𝐐∗)(\\theta,\\mathbf{Q}^{\*}) to get the initial score

|     |     |     |     |
| --- | --- | --- | --- |
|  | y~u=fVLM​(Vu,(θ,𝐐∗)),\\tilde{y}\_{u}=f\_{\\rm VLM}(V\_{u};(\\theta,\\mathbf{Q}^{\*})), |  | (3) |

where y~u=1\\tilde{y}\_{u}=1 if fVLMf\_{\\rm VLM} thinks the segment contains an anomaly after reasoning via 𝐐∗\\mathbf{Q}^{\*} with VuV\_{u}, and otherwise, y~u=0\\tilde{y}\_{u}=0. By repeating Eq. ( [3](https://arxiv.org/html/2412.01095v1#S3.E3 "Equation 3 ‣ 3.3 Inference in VERA: Coarse-to-Fine Anomaly Scoring by Guiding Questions and Contexts ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) for each segment, we have a segment-level initial anomaly score set Y~=\[y~1,⋯,y~h\]\\tilde{Y}=\[\\tilde{y}\_{1},\\cdots,\\tilde{y}\_{h}\].

Step 2: Ensemble Segment-Level Anomaly Scores with Scene Context. Note that the scores derived above only examine a short moment in a long video without considering any context. To resolve it, we refine the initial segment-level score by incorporating scene context—defined as preceding and following segments that contain similar elements, such as actors and background, to those in the current segment.

![Refer to caption](https://arxiv.org/html/2412.01095v1/fig3.png)Figure 3: VERA computes anomaly scores with 𝐐∗\\mathbf{Q}^{\*} in three steps.

We measure the relevance between different video segments by the cosine similarity of their feature representations \[ [24](https://arxiv.org/html/2412.01095v1#bib.bib24 "")\], extracted by a pretrained vision feature extractor gg, _e.g_., ImageBind \[ [11](https://arxiv.org/html/2412.01095v1#bib.bib11 "")\]. For the uu-th segment VuV\_{u}, its similarity with any segment VwV\_{w} (OPEN1≤w≤h)1\\leq w\\leq h) is sim⁡(u,w)=cos⁡(eu⋅ew‖eu‖⋅‖ew‖){\\rm sim}(u,w)={\\rm cos}\\left(\\frac{e\_{u}\\cdot e\_{w}}{\|\|e\_{u}\|\|\\cdot\|\|e\_{w}\|\|}\\right), where cos{\\rm cos} denotes the cosine function, and eu=g⁡(Vu)e\_{u}=g(V\_{u}) and ew=g⁡(Vw)e\_{w}=g(V\_{w}) represent their features. Let κu=\[κu(1),…,κu(K)\]\\kappa\_{u}=\[\\kappa\_{u}^{(1)},\\dots,\\kappa\_{u}^{(K)}\] denote the indices of the top-KK segments similar to VuV\_{u}. We refine the anomaly score by

|     |     |     |     |
| --- | --- | --- | --- |
|  | y¯u=∑i=1Ky~κu(i)⋅exp⁡(sim⁡(u,κu(i))/τ)∑j=1Kexp⁡(sim⁡(u,κu(j))/τ),\\bar{y}\_{u}=\\sum\_{i=1}^{K}\\tilde{y}\_{\\kappa\_{u}^{(i)}}\\cdot\\frac{{\\rm exp}({\\rm sim}(u,\\kappa\_{u}^{(i)})/\\tau)}{\\sum\_{j=1}^{K}{\\rm exp}({\\rm sim}(u,\\kappa\_{u}^{(j)})/\\tau)}, |  | (4) |

where y¯u\\bar{y}\_{u} is an ensemble of initial scores of top-KK video segments relevant to VuV\_{u}. Here, the initial score of each retrieved segment is weighted by a factor derived from the cosine similarity and normalized by the Softmax function (with τ\\tau as the temperature hyperparameter). Accordingly, scenes with greater similarity are assigned higher weights, making the ensemble score a more comprehensive reflection of anomalies with the video context. By applying Eq. ( [4](https://arxiv.org/html/2412.01095v1#S3.E4 "Equation 4 ‣ 3.3 Inference in VERA: Coarse-to-Fine Anomaly Scoring by Guiding Questions and Contexts ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) for all segments, we obtain
Y¯=\[y¯1,…,y¯h\]\\bar{Y}=\[\\bar{y}\_{1},\\dots,\\bar{y}\_{h}\].

Step 3: Frame-level Anomaly Scoring with Temporal Context. Given Y¯\\bar{Y}, we aim to incorporate temporal context to capture how events evolve over time when computing frame-level anomaly scores, for the abnormality of an event often depends on the timing and progression of observed activities. To detail, we first apply Gaussian smoothing \[ [12](https://arxiv.org/html/2412.01095v1#bib.bib12 "")\] to aggregate local temporal context into the segment-level anomaly scores. We denote the Gaussian kernel (suppose the filter size is ω\\omega) as G⁡(p)=exp⁡(−p22​σ12)G(p)={\\rm exp}(\\frac{-p^{2}}{2\\sigma\_{1}^{2}}) where pp is the distance from the kernel center and σ1\\sigma\_{1} is the variance. We update segment-level scores as Γ¯=Y¯∗G=\[γ¯1,⋯,γ¯h\]\\bar{\\Gamma}=\\bar{Y}\*G=\[\\bar{\\gamma}\_{1},\\cdots,\\bar{\\gamma}\_{h}\], where ∗\* is the convolution operation. Next, we integrate global temporal context by position weighting. With Γ¯\\bar{\\Gamma}, we flatten it into frame-level scores by assigning the score γ¯u\\bar{\\gamma}\_{u} to each frame in the uu-th segment, _i.e_., \[I(u−1)⋅d+1,⋯,Iu⋅d\]\[I\_{(u-1)\\cdot d+1},\\cdots,I\_{u\\cdot d}\]. We denote the frame-level score sequence after flattening as \[ρ1,⋯,ρF\]\[\\rho\_{1},\\cdots,\\rho\_{F}\]. We then apply the Gaussian function to encode position weights as w⁡(i)=exp⁡(−(i−c)22​σ22)w(i)=\\exp\\left(\\frac{-(i-c)^{2}}{2\\sigma\_{2}^{2}}\\right), where ii(1≤i≤F)(1\\leq i\\leq F) is any frame index, c=floor​(F/2)c=\\text{floor}(F/2) is the center frame index, and σ2\\sigma\_{2} is the variance. The anomaly score for the ii-th frame is:

|     |     |     |     |
| --- | --- | --- | --- |
|  | y^i=w⁡(i)⋅ρi.\\hat{y}\_{i}=w(i)\\cdot\\rho\_{i}. |  | (5) |

This operation scales the score ρi\\rho\_{i}, diminishing the anomaly score for frames near the beginning and end of the event. This helps better capture the temporal progression of anomalies: the score gradually increases as the anomaly reaches its peak and decreases afterward. The final scores is denoted as Y^=\[y^1,…,y^F\]\\hat{Y}=\[\\hat{y}\_{1},\\dots,\\hat{y}\_{F}\] after applying Eq. ( [5](https://arxiv.org/html/2412.01095v1#S3.E5 "Equation 5 ‣ 3.3 Inference in VERA: Coarse-to-Fine Anomaly Scoring by Guiding Questions and Contexts ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")).

Explainable VAD by VERA. When using template θ\\theta embedded with 𝐐∗\\mathbf{Q}^{\*} to compute Y^\\hat{Y}, we ask the VLM to “provide an explanation in one sentence” when reasoning, and VLM will explain the anomaly score it assigns afterward based on 𝐐∗\\mathbf{Q}^{\*}. Please refer to Sec. [4.4](https://arxiv.org/html/2412.01095v1#S4.SS4 "4.4 Qualitative Results and Case Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") and Sec. [B.4](https://arxiv.org/html/2412.01095v1#A2.SS4 "B.4 Additional Qualitative Results & Case Studies ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") in the Appendix for the demonstration of explainable VAD by VERA.

### 4 Experiments and Results

In this section, we present an evaluation of VERA as follows, addressing key questions of interest including: (Q1) Does it enhance the effectiveness of frozen VLMs in VAD? (Q2) Is its design reasonable and well-structured? (Q3) How well does it generalize across different scenarios?

#### 4.1 Experimental Settings

Datasets. We conduct experiments on two large-scale VAD datasets: (1) UCF-Crime \[ [35](https://arxiv.org/html/2412.01095v1#bib.bib35 "")\] and (2) XD-Violence \[ [45](https://arxiv.org/html/2412.01095v1#bib.bib45 "")\]. The details are as follows:

- •


UCF-Crime dataset is collected from real-world surveillance videos (128-hour long in total), covering crime-related anomalies including abuse, arrest, arson, assault, burglary, explosion, fighting, road accident, robbery, shoplifting, shooting, stealing, and vandalism. The training set has 1610 videos (810 abnormal ones and 800 normal ones), while the test set has 290 videos (140 abnormal ones and 150 normal ones). The total number of test frames is over 1 million (1,111,808), and abnormal frames account for 7.92%. The average duration of a test video is 2.13 minutes, which is relatively long compared to common video datasets and serves as a benchmark.

- •


XD-Violence is another representative large-scale (217-hour long in total) VAD dataset with 6 anomaly categories, _i.e_., abuse, car accident, explosion, fighting, riot, and shooting, which defines anomalous events as the ones related to violence. This dataset is collected from movies and YouTube videos. It has 3954 training videos and 800 test videos (500 abnormal ones and 300 normal ones). The total number of test frames is over 2 million (2,335,801), and abnormal frames account for 23.07%. The average duration of a test video is 1.62 minutes.


Metrics. Following approaches in \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 ""), [58](https://arxiv.org/html/2412.01095v1#bib.bib58 "")\], we evaluate VAD performance using the Area Under the Curve (AUC) of the frame-level Receiver Operating Characteristic (ROC) curve, as it provides a comprehensive measure of model performance across all thresholds. It is a comprehensive representation for evaluating the ability of a method to distinguish between anomaly and normality across different thresholds in VAD. As for average precision (AP), the area under the frame-level precision-recall curve, it is another VAD performance metric mostly used for the XD-Violence dataset. Compared to AUC, this metric mainly focuses on the performance of VAD method in identifying anomalous events. In other words, AP pays attention to classifying the anomaly correctly rather than the overall separation. We report AP results for XD-Violence in the Appendix.

Baselines. We categorize baselines into non-explainable approaches and explainable ones as \[ [58](https://arxiv.org/html/2412.01095v1#bib.bib58 "")\] does. Non-explainable ones are obtained by WS learning \[ [45](https://arxiv.org/html/2412.01095v1#bib.bib45 ""), [46](https://arxiv.org/html/2412.01095v1#bib.bib46 ""), [44](https://arxiv.org/html/2412.01095v1#bib.bib44 ""), [38](https://arxiv.org/html/2412.01095v1#bib.bib38 ""), [21](https://arxiv.org/html/2412.01095v1#bib.bib21 ""), [7](https://arxiv.org/html/2412.01095v1#bib.bib7 ""), [17](https://arxiv.org/html/2412.01095v1#bib.bib17 ""), [35](https://arxiv.org/html/2412.01095v1#bib.bib35 ""), [54](https://arxiv.org/html/2412.01095v1#bib.bib54 ""), [60](https://arxiv.org/html/2412.01095v1#bib.bib60 ""), [10](https://arxiv.org/html/2412.01095v1#bib.bib10 ""), [53](https://arxiv.org/html/2412.01095v1#bib.bib53 ""), [19](https://arxiv.org/html/2412.01095v1#bib.bib19 "")\] and unsupervised learning \[ [37](https://arxiv.org/html/2412.01095v1#bib.bib37 ""), [40](https://arxiv.org/html/2412.01095v1#bib.bib40 ""), [36](https://arxiv.org/html/2412.01095v1#bib.bib36 ""), [41](https://arxiv.org/html/2412.01095v1#bib.bib41 ""), [14](https://arxiv.org/html/2412.01095v1#bib.bib14 ""), [28](https://arxiv.org/html/2412.01095v1#bib.bib28 "")\]. These non-explainable approaches cannot provide language-based explanations for VAD and have following characteristics:

- •


WS learning methods \[ [45](https://arxiv.org/html/2412.01095v1#bib.bib45 ""), [46](https://arxiv.org/html/2412.01095v1#bib.bib46 ""), [44](https://arxiv.org/html/2412.01095v1#bib.bib44 ""), [38](https://arxiv.org/html/2412.01095v1#bib.bib38 ""), [21](https://arxiv.org/html/2412.01095v1#bib.bib21 ""), [7](https://arxiv.org/html/2412.01095v1#bib.bib7 ""), [17](https://arxiv.org/html/2412.01095v1#bib.bib17 ""), [35](https://arxiv.org/html/2412.01095v1#bib.bib35 ""), [54](https://arxiv.org/html/2412.01095v1#bib.bib54 ""), [60](https://arxiv.org/html/2412.01095v1#bib.bib60 ""), [10](https://arxiv.org/html/2412.01095v1#bib.bib10 ""), [53](https://arxiv.org/html/2412.01095v1#bib.bib53 ""), [19](https://arxiv.org/html/2412.01095v1#bib.bib19 "")\] usually use task-specific learning models with pretrained weights such as C3D \[ [39](https://arxiv.org/html/2412.01095v1#bib.bib39 "")\], I3D \[ [5](https://arxiv.org/html/2412.01095v1#bib.bib5 "")\], VideoSwin \[ [27](https://arxiv.org/html/2412.01095v1#bib.bib27 "")\], ResNet \[ [15](https://arxiv.org/html/2412.01095v1#bib.bib15 "")\], and ResNext \[ [48](https://arxiv.org/html/2412.01095v1#bib.bib48 "")\]
to extract feature for each video segment. Based on that, they form the training of classifiers, which output predictions after the feature extractors, as a multiple instance learning task, regarding the segments containing anomaly scenes as positive bags and the others as negative bags to handle the lack of frame-level annotations and the uncertainty of the anomaly locations in the video. Such learning objectives can fully use the only available video-level label information and effectively improve the discriminative ability of the classifiers in the network. However, the trained neural networks from these methods operate on highly abstract features that are hard for humans to interpret.

- •


Unsupervised learning methods \[ [37](https://arxiv.org/html/2412.01095v1#bib.bib37 ""), [40](https://arxiv.org/html/2412.01095v1#bib.bib40 ""), [36](https://arxiv.org/html/2412.01095v1#bib.bib36 ""), [41](https://arxiv.org/html/2412.01095v1#bib.bib41 ""), [14](https://arxiv.org/html/2412.01095v1#bib.bib14 ""), [28](https://arxiv.org/html/2412.01095v1#bib.bib28 "")\] improve the discriminative ability of the models regarding anomalies and normality without any knowledge of the video label. Note that we include one-class learning \[ [14](https://arxiv.org/html/2412.01095v1#bib.bib14 ""), [28](https://arxiv.org/html/2412.01095v1#bib.bib28 ""), [41](https://arxiv.org/html/2412.01095v1#bib.bib41 ""), [40](https://arxiv.org/html/2412.01095v1#bib.bib40 "")\] methods in this category. Unsupervised methods mostly learn reconstruction models from unlabeled data and use reconstruction errors to distinguish normal and abnormal video frames. Another common strategy \[ [37](https://arxiv.org/html/2412.01095v1#bib.bib37 ""), [36](https://arxiv.org/html/2412.01095v1#bib.bib36 "")\] is introducing pseudo-labels for unlabeled data and using this information to train discriminative models for VAD. Still, these methods cannot produce explainable results for VAD due to the structure gap.


For explainable approaches, we use LAVAD \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\], Holmes-VAD \[ [58](https://arxiv.org/html/2412.01095v1#bib.bib58 "")\], and VADor \[ [29](https://arxiv.org/html/2412.01095v1#bib.bib29 "")\] as representatives of Pipeline 1 and Pipeline 2 shown in Fig. [1](https://arxiv.org/html/2412.01095v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). It should be noted that \[ [49](https://arxiv.org/html/2412.01095v1#bib.bib49 "")\] does not report performance on UCF-Crime and XD-Violence. Additionally, we include zero-shot (ZS) VAD by frozen VLMs designed by  \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] as baselines.

Implementation of VERA. In our experiments, we choose a small VLM, InternVL2-8B \[ [8](https://arxiv.org/html/2412.01095v1#bib.bib8 "")\], as the backbone fVLMf\_{\\rm VLM} for building VERA by default, if not otherwise specified. With this choice, we implement VERA on an NVIDIA RTX A6000 GPU. We also explore other backbones, such as Qwen2-VL-7B \[ [43](https://arxiv.org/html/2412.01095v1#bib.bib43 "")\] and larger model variants of InternVL2 \[ [8](https://arxiv.org/html/2412.01095v1#bib.bib8 "")\] for ablation. In principle, VERA works well with different backbones. We train 𝐐\\mathbf{Q} for no more than 10 epochs, with a validation accuracy calculated every 100 iterations to determine the optimal 𝐐∗\\mathbf{Q}^{\*}. The used 𝐐∗\\mathbf{Q}^{\*} is given in Fig. [5](https://arxiv.org/html/2412.01095v1#S4.F5 "Figure 5 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). We set nn as 2, SS as 8, and mm as 5 for training and include the discussion in Sec. [4.3](https://arxiv.org/html/2412.01095v1#S4.SS3 "4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). Refer to the Appendix for more details on the hyperparameters in inference.

#### 4.2 Comparison to State-of-the-art Methods

| Method | AUC |
| _Non-explainable VAD Methods_ |
| Wu et al. \[ [45](https://arxiv.org/html/2412.01095v1#bib.bib45 "")\] | 82.44 |
| OVVAD \[ [46](https://arxiv.org/html/2412.01095v1#bib.bib46 "")\] | 86.40 |
| S3R \[ [44](https://arxiv.org/html/2412.01095v1#bib.bib44 "")\] | 85.99 |
| RTFM \[ [38](https://arxiv.org/html/2412.01095v1#bib.bib38 "")\] | 84.30 |
| MSL \[ [21](https://arxiv.org/html/2412.01095v1#bib.bib21 "")\] | 85.62 |
| MGFN \[ [7](https://arxiv.org/html/2412.01095v1#bib.bib7 "")\] | 86.98 |
| SSRL \[ [19](https://arxiv.org/html/2412.01095v1#bib.bib19 "")\] | 87.43 |
| CLIP-TSA \[ [17](https://arxiv.org/html/2412.01095v1#bib.bib17 "")\] | 87.58 |
| Sultani et al. \[ [35](https://arxiv.org/html/2412.01095v1#bib.bib35 "")\] | 77.92 |
| GCL \[ [54](https://arxiv.org/html/2412.01095v1#bib.bib54 "")\] | 79.84 |
| GCN \[ [60](https://arxiv.org/html/2412.01095v1#bib.bib60 "")\] | 82.12 |
| MIST \[ [10](https://arxiv.org/html/2412.01095v1#bib.bib10 "")\] | 82.30 |
| CLAWS \[ [53](https://arxiv.org/html/2412.01095v1#bib.bib53 "")\] | 83.03 |
| DYANNET \[ [37](https://arxiv.org/html/2412.01095v1#bib.bib37 "")\] | 84.50 |
| Tur el al. \[ [40](https://arxiv.org/html/2412.01095v1#bib.bib40 "")\] | 66.85 |
| GODS \[ [41](https://arxiv.org/html/2412.01095v1#bib.bib41 "")\] | 70.46 |
| _Explainable VAD Methods_ |
| LAVAD \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 80.28 |
| Holmes-VAD \[ [58](https://arxiv.org/html/2412.01095v1#bib.bib58 "")\] | 84.61 |
| VADor \[ [29](https://arxiv.org/html/2412.01095v1#bib.bib29 "")\] | 85.90 |
| ZS CLIP \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 53.16 |
| ZS IMAGEBIND-I\[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 53.65 |
| ZS IMAGEBIND-V\[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 55.78 |
| LLAVA-1.5 \[ [22](https://arxiv.org/html/2412.01095v1#bib.bib22 "")\] | 72.84 |
| VERA | 86.55 |

Table 2: AUC (%) on UCF-Crime. No instruction tuning is used for Holmes-VAD and VADor.

We address Q1 by empirically comparing VERA to existing VAD methods. First, in Table [2](https://arxiv.org/html/2412.01095v1#S4.T2 "Table 2 ‣ 4.2 Comparison to State-of-the-art Methods ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), VERA achieves the highest AUC among explainable VAD methods on UCF-Crime, outperforming Holmes-VAD and VADor (without instruction tuning, as reported in their papers) in a fair comparison. Importantly, unlike these methods, VERA does not need to modify the model parameters, demonstrating its suitability to directly adapt VLM to the VAD task with minimal training requirements. Moreover, VERA surpasses LAVAD by 6%6\\% in AUC on UCF-Crime, uniquely integrating both description and reasoning capabilities in VAD. Compared to non-explainable methods, VERA achieves AUC performance that is comparable to one of the top-performing methods, CLIP-TSA, on UCF-Crime, while offering the additional advantage of explainable predictions.

| Method | AUC |
| _Non-Explainable VAD Methods_ |
| Hasan et al. \[ [14](https://arxiv.org/html/2412.01095v1#bib.bib14 "")\] | 50.32 |
| Lu et al. \[ [28](https://arxiv.org/html/2412.01095v1#bib.bib28 "")\] | 53.56 |
| BODS \[ [41](https://arxiv.org/html/2412.01095v1#bib.bib41 "")\] | 57.32 |
| GODS \[ [41](https://arxiv.org/html/2412.01095v1#bib.bib41 "")\] | 61.56 |
| RareAnom \[ [36](https://arxiv.org/html/2412.01095v1#bib.bib36 "")\] | 68.33 |
| _Explainable VAD Methods_ |
| LAVAD \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 85.36 |
| ZS CLIP \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 38.21 |
| ZS IMAGEBIND-I\[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 58.81 |
| ZS IMAGEBIND-V\[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 55.06 |
| LLAVA-1.5 \[ [22](https://arxiv.org/html/2412.01095v1#bib.bib22 "")\] | 79.62 |
| VERA | 88.26 |

Table 3: AUC (%) on XD-Violence.

Similar advantages are also observed in Table [3](https://arxiv.org/html/2412.01095v1#S4.T3 "Table 3 ‣ 4.2 Comparison to State-of-the-art Methods ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") for XD-Violence. Considering multiple factors, including performance, training efficiency, system integration, and explainability, VERA stands out as a promising pipeline for VLMs in VAD.

#### 4.3 Ablation Studies

We perform necessary ablation studies on UCF-Crime to answer both Q2 and Q3 for a comprehensive evaluation.

| Strategy | AUC (%) |
| --- | --- |
| Random \[ [3](https://arxiv.org/html/2412.01095v1#bib.bib3 "")\] | 83.63 |
| TSN \[ [42](https://arxiv.org/html/2412.01095v1#bib.bib42 "")\] | 82.63 |
| Uniform \[ [57](https://arxiv.org/html/2412.01095v1#bib.bib57 "")\] | 86.55 |

Table 4: Sampling strategies explored in VERA training.

Training Frame Sampling Strategy. We compare three frame sampling strategies for obtaining each V~(j)\\tilde{V}^{(j)} in training: uniform sampling, random sampling, and TSN sampling (random sampling from equally divided segments). Table [4](https://arxiv.org/html/2412.01095v1#S4.T4 "Table 4 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") shows that uniform sampling performs the best (with batch size n=n= 2 and S=S= 8). This is because uniform sampling preserves the temporal structure and maintains consistent motion patterns throughout the long video, making it easier for VLMs to understand the video and update 𝐐\\mathbf{Q}.

Batch Size and Sampled Frame Number. Key hyperparameters that need to be set in training are the batch size nn and the number of sampled frames SS for each video V(j)V^{(j)} in the verbalized learning framework. The selection of SS and nn are correlated because they determine the total number of frames for the optimizer to skim and provide feedback as S⋅nS\\cdot n. In implementation, we will face memory constraints when implementing VLMs on GPUs. In our training, we find in the general case fVLMf\_{\\rm VLM} used for training can handle at most 16 frames when we implement VERA on an NVIDIA RTX A6000 GPU, so we set S⋅n=16S\\cdot n=16 in training. We further explore the trade-off between SS and nn given the constraints for input frames to decide SS and nn.

| Batch Size | Sampled Frames | AUC (%) |
| --- | --- | --- |
| nn = 1 | SS = 16 | 81.53 |
| nn = 2 | SS = 8 | 86.55 |
| nn = 4 | SS = 4 | 83.19 |
| nn = 8 | SS = 2 | 79.91 |

Table 5: The choice of batch size and sampling frames affects the effectiveness of the learned guiding questions in VAD. The results are obtained by InternVL2-8B as VERA’s backbone.

The results are shown in Table [5](https://arxiv.org/html/2412.01095v1#S4.T5 "Table 5 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). If the batch size nn is 1 with S=S= 16, the learned questions cannot be generalized due to the limited video sample in the batch which leads to a suboptimal AUC, and it takes longer to train for VERA. Meanwhile, if we set nn as large numbers like 4 or 8 (with S=S= 4 or S=S= 2), the learned questions are suboptimal too because relatively few sampled frames generally lack the temporality for the optimizer to look into the details and conceive good questions. Thus, setting nn to 2 and SS to 8 is in default in this paper, which strikes the balance between training efficiency and effectiveness.

| Question Type | AUC (%) |
| --- | --- |
| No questions | 78.81 |
| Manually written questions by human | 81.15 |
| Learned questions w/o iteratively inputting VbatchV\_{\\rm batch} in Eq. ( [2](https://arxiv.org/html/2412.01095v1#S3.E2 "Equation 2 ‣ 3.2 Training in VERA: Finding Guiding Questions for VAD via Verbalized Learning ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) | 78.06 |
| Iteratively learned questions (used in VERA) | 86.55 |

Table 6: The way we obtain guiding questions affects AUC substantially.

How to Obtain Guiding Questions 𝐐\\mathbf{Q} for VLM. As seen in Table [6](https://arxiv.org/html/2412.01095v1#S4.T6 "Table 6 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), if the guiding questions are not incorporated into the VLM prompt, the AUC will drop largely to 78.81%, confirming the need to use simpler and more focused questions to provoke reasoning in the VLMs for VAD. Meanwhile, if we use manually written questions (detailed in the Appendix), the performance is suboptimal with an 81.15% AUC, which shows the need to use verbalized learning to find guiding questions. Lastly, if we only input batched predictions Y^b​a​t​c​h\\hat{Y}\_{batch} and ground truths Yb​a​t​c​hY\_{batch} without inputting VbatchV\_{\\rm batch} in the optimizer, the 𝐐\\mathbf{Q} updated in this way will dumb the VLMs and make it have a low AUC. Thus, inputting video frames as Eq. ( [2](https://arxiv.org/html/2412.01095v1#S3.E2 "Equation 2 ‣ 3.2 Training in VERA: Finding Guiding Questions for VAD via Verbalized Learning ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) does is necessary to learn good 𝐐\\mathbf{Q}.

Figure 4: Effect of the number of guiding questions on AUC.

Number of Questions mm.
As shown in Fig. [4](https://arxiv.org/html/2412.01095v1#S4.F4 "Figure 4 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), when mm is set to 1, the reasoning is limited to a single perspective, resulting in a lower AUC. As mm increases up to 5, the model captures more comprehensive anomaly patterns, leading to improved AUC. However, increasing mm beyond 5 yields no significant gains. Therefore, we set mm to 5 by default in VERA, if not otherwise specified.

| Operation | AUC (%) |
| --- | --- |
| Initial (Step 1) | 76.10 |
| Initial + Retrieval (Step 2) | 84.53 (+8.43) |
| Initial + Retrieval + Smoothing (Step 3) | 85.48 (+0.95) |
| Initial + Retrieval + Smoothing + Weighting (Step 3) | 86.55 (+1.07) |

Table 7: Ablation study of each step in VERA inference.

Coarse-to-Fine Anomaly Score Computation. We also validate the anomaly score computation by VERA. Table [7](https://arxiv.org/html/2412.01095v1#S4.T7 "Table 7 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") shows the AUC is 76.10% when using the flattened initial score obtained in Step 1, and leveraging retrieved segments in Step 2 significantly boosts the AUC to 84.53%, highlighting the effectiveness of incorporating ensemble scores based on scene context. Meanwhile, smoothing and weighting in Step 3 further improves the AUC by around 1% each, verifying the benefit of integrating temporal context.

![Refer to caption](https://arxiv.org/html/2412.01095v1/fig5.png)Figure 5: Given 𝐐∗\\mathbf{Q}^{\*} by VERA, the frozen VLM (InternVL2-8B) will reason and explain the scene based on it. For illustration, we take as an example the video “Arrest007\_x264” from UCF-Crime and include 6 scenes here. The complete anomaly scores are shown in Fig. [6](https://arxiv.org/html/2412.01095v1#S4.F6 "Figure 6 ‣ 4.4 Qualitative Results and Case Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models").

Generalizability Test. We further examine the generalizability of VERA across different model sizes, VLM architectures, and datasets to address Q3.

| fVLMf\_{\\rm VLM} | Source of 𝐐\\mathbf{Q} |
| --- | --- |
| InternVL2-8B | InternVL2-40B |
| --- | --- |
| InternVL2-8B | 86.55 | 80.43 |
| InternVL2-40B | 85.24 | 86.72 |

Table 8: AUC (%) across model sizes .

| fVLMf\_{\\rm VLM} | Source of 𝐐\\mathbf{Q} |
| --- | --- |
| InternVL2-8B | Qwen2-VL-7B |
| --- | --- |
| InternVL2-8B | 86.55 | 81.37 |
| Qwen2-VL-7B | 79.60 | 82.64 |

Table 9: AUC (%) across architectures.

| Dataset | Source of 𝐐\\mathbf{Q} |
| --- | --- |
| UCF-Crime | XD-Violence |
| --- | --- |
| UCF-Crime | 86.55 | 80.42 |
| XD-Violence | 86.26 | 88.26 |

Table 10: AUC (%) across datasets.

First, we apply VERA to InternVL2-40B, a larger model in the InternVL2 family compared to InternVL2-8B. As shown in Table [10](https://arxiv.org/html/2412.01095v1#S4.T10 "Table 10 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), InternVL2-40B achieves effective AUC performance, slightly exceeding that of InternVL2-8B, indicating that verbalized learning in VERA enables models of various scales to identify a 𝐐\\mathbf{Q} suitable for their reasoning capabilities. Additionally, We also evaluate the transferability of 𝐐\\mathbf{Q} across different scales and and observe an interesting phenomenon: the 𝐐\\mathbf{Q} learned by InternVL2-8B remains effective for InternVL2-40B, but not vice versa. This is likely because the 𝐐\\mathbf{Q} learned by the smaller model is readily interpretable by the larger model, whereas the 𝐐\\mathbf{Q} derived from the larger model is more complex in syntactic structure and does not align well with the reasoning framework of the smaller model. Secondly, we select a different VLM, Qwen2-VL-7B \[ [43](https://arxiv.org/html/2412.01095v1#bib.bib43 "")\], as the backbone for VERA. As shown in Table [10](https://arxiv.org/html/2412.01095v1#S4.T10 "Table 10 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), while the AUC achieved with Qwen2-VL-7B is lower than that with InternVL2-8B, the verbalized learning in VERA remains effective, allowing it to outperform notable baselines such as LAVAD \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\]. However, a notable gap exists when transferring 𝐐\\mathbf{Q} across different model architectures in Table [10](https://arxiv.org/html/2412.01095v1#S4.T10 "Table 10 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). Developing a universal 𝐐\\mathbf{Q} that can effectively elicit reasoning capabilities across various VLM structures would be an promising direction for future research. Lastly, we observe that the transferability of 𝐐\\mathbf{Q} depends on the training dataset. From Table [10](https://arxiv.org/html/2412.01095v1#S4.T10 "Table 10 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), we observe that transferring 𝐐\\mathbf{Q} learned from UCF-Crime to XD-Violence results in a smaller performance drop compared to the reverse case. This suggests the source dataset is crucial to the transferability of 𝐐\\mathbf{Q} across datasets.

#### 4.4 Qualitative Results and Case Studies

To illustrate how VERA performs video anomaly detection, we take one video for a qualitative demonstration of the explainability brought by the learned 𝐐\\mathbf{Q}, as shown in Fig. [5](https://arxiv.org/html/2412.01095v1#S4.F5 "Figure 5 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). Please refer to the Appendix for more qualitative examples if interested. The main anomaly in this video is that a man tries to steal money from the washing machines in a laundromat and is arrested after being found by the police. In Fig. [5](https://arxiv.org/html/2412.01095v1#S4.F5 "Figure 5 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), we provide the guiding questions learned by VERA and take 6 main video segments (each with 2 sampled frames and their time indices are given in Fig. [6](https://arxiv.org/html/2412.01095v1#S4.F6 "Figure 6 ‣ 4.4 Qualitative Results and Case Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) as examples to demonstrate the explanation produced by VERA. From every given answer, the frozen VLM with VERA-learned questions is able to explain the scene by closely following the detailed anomaly characterization of the five learned guiding questions. For example, in the second scene, one question in 𝐐∗\\mathbf{Q}^{\*} states that “Are there any people in the video who are not in their typical positions or engaging in activities that are not consistent with their usual behavior”, and it successfully triggers the reasoning abilities from the frozen VLM. The VLM then accurately describes the abnormal event and explains why it is regarded as an anomaly under the cue from the question.

Figure 6: Anomaly scores generated by VERA (with InternVL2-8B) in “Arrest007\_x264” from UCF-Crime.

Moreover, owing to the proposed coarse-to-fine detection strategy in testing, the anomaly score dynamics shown in Fig. [6](https://arxiv.org/html/2412.01095v1#S4.F6 "Figure 6 ‣ 4.4 Qualitative Results and Case Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") well represents the actual real-time anomaly level in this video and gradually increases to nearly 1 when the man is being arrested. This result verifies that VERA allows VLMs to effectively identify anomalies with a holistic model, reducing the manpower and computational overhead for explainable VAD.

More interestingly, we want to highlight one more advantage of VERA. That is, VERA allows humans to further interact with VLMs because it retains the general question-answering ability of pretrained VLMs. This is because VERA does not require finetuning of the VLM backbone weights. Although finetuning VLMs with parameter-efficient methods like \[ [16](https://arxiv.org/html/2412.01095v1#bib.bib16 ""), [32](https://arxiv.org/html/2412.01095v1#bib.bib32 ""), [26](https://arxiv.org/html/2412.01095v1#bib.bib26 "")\] is easy and computationally tractable, instruction-tuned models still inevitably lose the flexibility to handle general questions (due to catastrophic forgetting), as they are trained to respond to certain queries with fixed answer styles. In contrast, as shown in Fig. [7](https://arxiv.org/html/2412.01095v1#S4.F7 "Figure 7 ‣ 4.4 Qualitative Results and Case Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), the learned 𝐐∗\\mathbf{Q}^{\*} can steer reasoning in a frozen VLM while still being able to allow the VLM to answer open-ended (like follow-up or counterfactual) questions, which is an important ability lost in instruction tuning-based models.

![Refer to caption](https://arxiv.org/html/2412.01095v1/fig7.png)Figure 7: Humans can further interact with VERA (Backbone: InternVL2-8B) and ask open-ended questions.

### 5 Concluding Remarks and Limitations

We propose a novel pipeline, VERA, which can effectively elicit the reasoning ability from VLMs to perform explainable VAD without additional computation overhead. This is done through an effective and novel application of verbalized machine learning \[ [47](https://arxiv.org/html/2412.01095v1#bib.bib47 "")\] to VLM. In training, VERA obtains the guiding questions detailing anomaly patterns through the verbal interaction between the learner and the optimizer agents. In inference, VERA uses them to enhance VLMs for identifying anomalies and compute frame-level anomaly scores in a coarse-to-fine process. Experimental results validate the effectiveness of the VERA framework in achieving state-of-the-art explainable VAD performance.

Like existing VLM-based VAD methods, VERA’s performance relies heavily on the visual perception capabilities of VLMs. Most VLMs employ the CLIP vision encoder \[ [33](https://arxiv.org/html/2412.01095v1#bib.bib33 "")\], which has limitations in capturing fine-grained visual details. This limitation can impair precise anomaly detection. If important visual features are missing during the visual encoding process, then it is unlikely for VERA to perform meaningful verbalized learning.
Therefore, a fundamental challenge for VLM-based VAD is to ensure sufficient visual and temporal features are encoded. Having verified this capability, VERA can perform verbalized learning to extract crucial cues that guide video anomaly reasoning.

### References

- \[1\]
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya,
Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al.
Gpt-4 technical report.
_arXiv preprint arXiv:2303.08774_, 2023.

- \[2\]
Daniel Bogdoll, Maximilian Nitsche, and J Marius Zöllner.
Anomaly detection in autonomous driving: A survey.
In _CVPR Workshops_, 2022.

- \[3\]
Meinardus Boris, Batra Anil, Rohrbach Anna, and Rohrbach Marcus.
The surprising effectiveness of multimodal large language models for
video moment retrieval.
_arXiv preprint arXiv:2406.18113_, 2024.

- \[4\]
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan,
Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom
Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens
Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott
Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec
Radford, Ilya Sutskever, and Dario Amodei.
Language models are few-shot learners.
In _NeurIPS_, 2020.

- \[5\]
Joao Carreira and Andrew Zisserman.
Quo vadis, action recognition? a new model and the kinetics dataset.
In _CVPR_, 2017.

- \[6\]
Junxi Chen, Liang Li, Li Su, Zheng-jun Zha, and Qingming Huang.
Prompt-enhanced multiple instance learning for weakly supervised
video anomaly detection.
In _CVPR_, 2024a.

- \[7\]
Yingxian Chen, Zhengzhe Liu, Baoheng Zhang, Wilton Fok, Xiaojuan Qi, and
Yik-Chung Wu.
Mgfn: Magnitude-contrastive glance-and-focus network for
weakly-supervised video anomaly detection.
In _AAAI_, 2023.

- \[8\]
Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Muyan Zhong,
Qinglong Zhang, Xizhou Zhu, Lewei Lu, et al.
Internvl: Scaling up vision foundation models and aligning for
generic visual-linguistic tasks.
In _CVPR_, 2024b.

- \[9\]
Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn,
Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg
Heigold, Sylvain Gelly, Jakob Uszkoreit, and Neil Houlsby.
An image is worth 16x16 words: Transformers for image recognition at
scale.
In _ICLR_, 2021.

- \[10\]
Jia-Chang Feng, Fa-Ting Hong, and Wei-Shi Zheng.
Mist: Multiple instance self-training framework for video anomaly
detection.
In _CVPR_, 2021.

- \[11\]
Rohit Girdhar, Alaaeldin El-Nouby, Zhuang Liu, Mannat Singh, Kalyan Vasudev
Alwala, Armand Joulin, and Ishan Misra.
Imagebind: One embedding space to bind them all.
In _CVPR_, 2023.

- \[12\]
Rafael C Gonzalez.
_Digital image processing_.
Pearson education india, 2009.

- \[13\]
Qiushan Guo, Shalini De Mello, Hongxu Yin, Wonmin Byeon, Ka Chun Cheung, Yizhou
Yu, Ping Luo, and Sifei Liu.
Regiongpt: Towards region understanding vision language model.
In _CVPR_, 2024.

- \[14\]
Mahmudul Hasan, Jonghyun Choi, Jan Neumann, Amit K Roy-Chowdhury, and Larry S
Davis.
Learning temporal regularity in video sequences.
In _CVPR_, 2016.

- \[15\]
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
Deep residual learning for image recognition.
In _CVPR_, 2016.

- \[16\]
Edward J Hu, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,
Weizhu Chen, et al.
Lora: Low-rank adaptation of large language models.
In _ICLR_, 2021.

- \[17\]
Hyekang Kevin Joo, Khoa Vo, Kashu Yamazaki, and Ngan Le.
Clip-tsa: Clip-assisted temporal self-attention for weakly-supervised
video anomaly detection.
In _ICIP_, 2023.

- \[18\]
Diederik P Kingma.
Adam: A method for stochastic optimization.
_arXiv preprint arXiv:1412.6980_, 2014.

- \[19\]
Guoqiu Li, Guanxiong Cai, Xingyu Zeng, and Rui Zhao.
Scale-aware spatio-temporal relation learning for video anomaly
detection.
In _ECCV_, 2022a.

- \[20\]
Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi.
Blip-2: Bootstrapping language-image pre-training with frozen image
encoders and large language models.
In _ICML_, 2023.

- \[21\]
Shuo Li, Fang Liu, and Licheng Jiao.
Self-training multi-sequence learning with transformer for weakly
supervised video anomaly detection.
In _AAAI_, 2022b.

- \[22\]
Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee.
Improved baselines with visual instruction tuning.
In _CVPR_, 2024a.

- \[23\]
Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee.
Visual instruction tuning.
In _NeurIPS_, 2024b.

- \[24\]
Weiyang Liu, Yan-Ming Zhang, Xingguo Li, Zhiding Yu, Bo Dai, Tuo Zhao, and Le
Song.
Deep hyperspherical learning.
In _NeurIPS_, 2017.

- \[25\]
Wen Liu, Weixin Luo, Dongze Lian, and Shenghua Gao.
Future frame prediction for anomaly detection–a new baseline.
In _CVPR_, 2018.

- \[26\]
Weiyang Liu, Zeju Qiu, Yao Feng, Yuliang Xiu, Yuxuan Xue, Longhui Yu, Haiwen
Feng, Zhen Liu, Juyeon Heo, Songyou Peng, et al.
Parameter-efficient orthogonal finetuning via butterfly
factorization.
In _ICLR_, 2024c.

- \[27\]
Ze Liu, Jia Ning, Yue Cao, Yixuan Wei, Zheng Zhang, Stephen Lin, and Han Hu.
Video swin transformer.
In _CVPR_, 2022.

- \[28\]
Cewu Lu, Jianping Shi, and Jiaya Jia.
Abnormal event detection at 150 fps in matlab.
In _ICCV_, 2013.

- \[29\]
Hui Lv and Qianru Sun.
Video anomaly detection and explanation via large language models.
_arXiv preprint arXiv:2401.05702_, 2024.

- \[30\]
Hui Lv, Zhongqi Yue, Qianru Sun, Bin Luo, Zhen Cui, and Hanwang Zhang.
Unbiased multiple instance learning for weakly supervised video
anomaly detection.
In _CVPR_, 2023.

- \[31\]
Sarah Pratt, Ian Covert, Rosanne Liu, and Ali Farhadi.
What does a platypus look like? generating customized prompts for
zero-shot image classification.
In _ICCV_, 2023.

- \[32\]
Zeju Qiu, Weiyang Liu, Haiwen Feng, Yuxuan Xue, Yao Feng, Zhen Liu, Dan Zhang,
Adrian Weller, and Bernhard Schölkopf.
Controlling text-to-image diffusion by orthogonal finetuning.
In _NeurIPS_, 2023.

- \[33\]
Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh,
Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark,
et al.
Learning transferable visual models from natural language
supervision.
In _ICML_, 2021.

- \[34\]
Karsten Roth, Latha Pemula, Joaquin Zepeda, Bernhard Schölkopf, Thomas
Brox, and Peter Gehler.
Towards total recall in industrial anomaly detection.
In _CVPR_, 2022.

- \[35\]
Waqas Sultani, Chen Chen, and Mubarak Shah.
Real-world anomaly detection in surveillance videos.
In _CVPR_, 2018.

- \[36\]
Kamalakar Vijay Thakare, Debi Prosad Dogra, Heeseung Choi, Haksub Kim, and
Ig-Jae Kim.
Rareanom: A benchmark video dataset for rare type anomalies.
_Pattern Recognition_, 140:109567, 2023a.

- \[37\]
Kamalakar Vijay Thakare, Yash Raghuwanshi, Debi Prosad Dogra, Heeseung Choi,
and Ig-Jae Kim.
Dyannet: A scene dynamicity guided self-trained video anomaly
detection network.
In _WACV_, 2023b.

- \[38\]
Yu Tian, Guansong Pang, Yuanhong Chen, Rajvinder Singh, Johan W Verjans, and
Gustavo Carneiro.
Weakly-supervised video anomaly detection with robust temporal
feature magnitude learning.
In _ICCV_, 2021.

- \[39\]
Du Tran, Lubomir Bourdev, Rob Fergus, Lorenzo Torresani, and Manohar Paluri.
Learning spatiotemporal features with 3d convolutional networks.
In _ICCV_, 2015.

- \[40\]
Anil Osman Tur, Nicola Dall’Asen, Cigdem Beyan, and Elisa Ricci.
Unsupervised video anomaly detection with diffusion models
conditioned on compact motion representations.
In _International Conference on Image Analysis and Processing_,
2023.

- \[41\]
Jue Wang and Anoop Cherian.
Gods: Generalized one-class discriminative subspaces for anomaly
detection.
In _ICCV_, 2019.

- \[42\]
Limin Wang, Yuanjun Xiong, Zhe Wang, Yu Qiao, Dahua Lin, Xiaoou Tang, and Luc
Van Gool.
Temporal segment networks: Towards good practices for deep action
recognition.
In _ECCV_, 2016.

- \[43\]
Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin
Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Yang Fan, Kai Dang, Mengfei Du,
Xuancheng Ren, Rui Men, Dayiheng Liu, Chang Zhou, Jingren Zhou, and Junyang
Lin.
Qwen2-vl: Enhancing vision-language model’s perception of the world
at any resolution.
_arXiv preprint arXiv:2409.12191_, 2024.

- \[44\]
Jhih-Ciang Wu, He-Yen Hsieh, Ding-Jie Chen, Chiou-Shann Fuh, and Tyng-Luh Liu.
Self-supervised sparse representation for video anomaly detection.
In _ECCV_, 2022.

- \[45\]
Peng Wu, Jing Liu, Yujia Shi, Yujia Sun, Fangtao Shao, Zhaoyang Wu, and Zhiwei
Yang.
Not only look, but also listen: Learning multimodal violence
detection under weak supervision.
In _ECCV_, 2020.

- \[46\]
Peng Wu, Xuerong Zhou, Guansong Pang, Yujia Sun, Jing Liu, Peng Wang, and
Yanning Zhang.
Open-vocabulary video anomaly detection.
In _CVPR_, pages 18297–18307, 2024.

- \[47\]
Tim Z Xiao, Robert Bamler, Bernhard Schölkopf, and Weiyang Liu.
Verbalized machine learning: Revisiting machine learning with
language models.
_arXiv preprint arXiv:2406.04344_, 2024.

- \[48\]
Saining Xie, Ross Girshick, Piotr Dollár, Zhuowen Tu, and Kaiming He.
Aggregated residual transformations for deep neural networks.
In _CVPR_, 2017.

- \[49\]
Yuchen Yang, Kwonjoon Lee, Behzad Dariush, Yinzhi Cao, and Shao-Yuan Lo.
Follow the rules: reasoning for video anomaly detection with large
language models.
_arXiv preprint arXiv:2407.10299_, 2024a.

- \[50\]
Zhiwei Yang, Jing Liu, and Peng Wu.
Text prompt with normality guidance for weakly supervised video
anomaly detection.
In _CVPR_, 2024b.

- \[51\]
Muchao Ye, Xiaojiang Peng, Weihao Gan, Wei Wu, and Yu Qiao.
Anopcn: Video anomaly detection via deep predictive coding network.
In _ACM international conference on multimedia_, 2019.

- \[52\]
Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos
Guestrin, and James Zou.
Textgrad: Automatic “differentiation” via text.
_arXiv preprint arXiv:2406.07496_, 2024.

- \[53\]
Muhammad Zaigham Zaheer, Arif Mahmood, Marcella Astrid, and Seung-Ik Lee.
Claws: Clustering assisted weakly supervised learning with normalcy
suppression for anomalous event detection.
In _ECCV_, 2020.

- \[54\]
M Zaigham Zaheer, Arif Mahmood, M Haris Khan, Mattia Segu, Fisher Yu, and
Seung-Ik Lee.
Generative cooperative learning for unsupervised video anomaly
detection.
In _CVPR_, 2022.

- \[55\]
Luca Zanella, Willi Menapace, Massimiliano Mancini, Yiming Wang, and Elisa
Ricci.
Harnessing large language models for training-free video anomaly
detection.
In _CVPR_, 2024.

- \[56\]
Chen Zhang, Guorong Li, Yuankai Qi, Shuhui Wang, Laiyun Qing, Qingming Huang,
and Ming-Hsuan Yang.
Exploiting completeness and uncertainty of pseudo labels for weakly
supervised video anomaly detection.
In _CVPR_, 2023a.

- \[57\]
Hang Zhang, Xin Li, and Lidong Bing.
Video-llama: An instruction-tuned audio-visual language model for
video understanding.
In _EMNLP_, 2023b.

- \[58\]
Huaxin Zhang, Xiaohao Xu, Xiang Wang, Jialong Zuo, Chuchu Han, Xiaonan Huang,
Changxin Gao, Yuehuan Wang, and Nong Sang.
Holmes-vad: Towards unbiased and explainable video anomaly detection
via multi-modal llm.
_arXiv preprint arXiv:2406.12235_, 2024a.

- \[59\]
Menghao Zhang, Jingyu Wang, Qi Qi, Haifeng Sun, Zirui Zhuang, Pengfei Ren,
Ruilong Ma, and Jianxin Liao.
Multi-scale video anomaly detection by multi-grained spatio-temporal
representation learning.
In _CVPR_, 2024b.

- \[60\]
Jia-Xing Zhong, Nannan Li, Weijie Kong, Shan Liu, Thomas H Li, and Ge Li.
Graph convolutional label noise cleaner: Train a plug-and-play action
classifier for anomaly detection.
In _CVPR_, 2019.

- \[61\]
Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mohamed Elhoseiny.
Minigpt-4: Enhancing vision-language understanding with advanced
large language models.
In _ICLR_, 2024.


## Appendix

We include more details on training in VERA (Sec. [A](https://arxiv.org/html/2412.01095v1#A1 "Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) and additional experimental results (Sec. [B](https://arxiv.org/html/2412.01095v1#A2 "Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")). To specify:

- •


In Sec. [A](https://arxiv.org/html/2412.01095v1#A1 "Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), we provide the pseudocodes and details on the initialization, the learner prompt template, and the optimizer prompt template for the training process in Sec. [A.1](https://arxiv.org/html/2412.01095v1#A1.SS1 "A.1 Algorithm ‣ Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). After that, we discuss the optimization process of the learned questions by the optimizer in Sec. [A.2](https://arxiv.org/html/2412.01095v1#A1.SS2 "A.2 Details for Iterative Update by the Optimizer ‣ Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models").

- •


In Sec. [B](https://arxiv.org/html/2412.01095v1#A2 "Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), we first include comparison results with the state-of-the-art methods on XD-Violence measured by AP in Sec. [B.1](https://arxiv.org/html/2412.01095v1#A2.SS1 "B.1 Comparison to the State-of-the-art Methods on XD-Violence Measured by AP ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). We also discuss other good properties of VERA, including the good generalizability of the learned questions for different scenarios and the insensitivity of VERA regarding hyperparameters in Sec. [B.2](https://arxiv.org/html/2412.01095v1#A2.SS2 "B.2 Discussion on Generalizability of Used Questions ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") and Sec. [B.3](https://arxiv.org/html/2412.01095v1#A2.SS3 "B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), respectively. Finally, we include additional case studies with normal and abnormal videos in Sec. [B.4](https://arxiv.org/html/2412.01095v1#A2.SS4 "B.4 Additional Qualitative Results & Case Studies ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models").


### Appendix A Training in VERA

#### A.1 Algorithm

We show the complete iterative training process of VERA in pseudocodes in Algorithm [1](https://arxiv.org/html/2412.01095v1#algorithm1 "Algorithm 1 ‣ A.1 Algorithm ‣ Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). It is an iterative process of using the learner to output binary prediction for each sample in a mini-batch and asking the optimizer to update the guiding questions after collecting the batched data. Meanwhile, we have a small validation set (10% samples randomly drawn from the original training set) for deciding the 𝐐∗\\mathbf{Q}^{\*} used for testing. We want to further detail on certain elements in Algorithm [1](https://arxiv.org/html/2412.01095v1#algorithm1 "Algorithm 1 ‣ A.1 Algorithm ‣ Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") as follows.

Algorithm 1Optimizing Guiding Questions in VAD by VERA during Training

Inputs: Training data pairs Dtrain={(V~(j),Y(j))}j=1ND\_{\\rm train}=\\{(\\tilde{V}^{(j)},Y^{(j)})\\}\_{j=1}^{N}, iteration number PP, initial guiding questions 𝐐0\\mathbf{Q}\_{0}, learner flearnerf\_{\\rm learner}, optimizer foptf\_{\\rm opt}, learner prompt template θ\\theta, optimizer prompt template ψ\\psi, validation set Dval={(V~val(j),Yval(j))}j=1ηD\_{\\rm val}=\\{(\\tilde{V}\_{\\rm val}^{(j)},Y\_{\\rm val}^{(j)})\\}\_{j=1}^{\\eta}, period for validation μ\\mu, batch size nn.

Output: Optimal guiding questions 𝐐∗\\mathbf{Q}^{\*}.

Set iteration counter t←1t\\leftarrow 1;

Set 𝐐∗←𝐐0\\mathbf{Q}^{\*}\\leftarrow\\mathbf{Q}\_{0}, test 𝐐0\\mathbf{Q}\_{0} on validation set DvalD\_{\\rm val} and compute its validation accuracy as Acc∗{\\rm Acc}^{\*};

while _t ≤\\leq P_ do

\# _Conduct the learning task with a mini-batch by the learner_

Randomly sample a batch without repetition from DtrainD\_{\\rm train} with a visual input batch Vbatch=\[V~batch(1),⋯,V~batch(n)\]V\_{\\rm batch}=\[\\tilde{V}\_{\\rm batch}^{(1)},\\cdots,\\tilde{V}\_{\\rm batch}^{(n)}\] and ground truths Ybatch=\[Ybatch(1),⋯,Ybatch(n)\]Y\_{\\rm batch}=\[Y\_{\\rm batch}^{(1)},\\cdots,Y\_{\\rm batch}^{(n)}\];

for _1≤j≤n1\\leq j\\leq n_ do

Obtain a prediction Y^batch(j)\\hat{Y}\_{\\rm batch}^{(j)} for V~batch(j)\\tilde{V}\_{\\rm batch}^{(j)} from flearnerf\_{\\rm learner} with prompt (θ,𝐐t)(\\theta,\\mathbf{Q}\_{t}) by Eq. ( [1](https://arxiv.org/html/2412.01095v1#S3.E1 "Equation 1 ‣ 3.2 Training in VERA: Finding Guiding Questions for VAD via Verbalized Learning ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) as
Y^batch(j)=flearner(t)​(V~batch(j))\\hat{Y}\_{\\rm batch}^{(j)}=f\_{\\rm learner}^{(t)}(\\tilde{V}\_{\\rm batch}^{(j)});

end for

\# _Update the guiding questions with the batched data by the optimizer_

Input the batched prediction Y^batch=\[Y^batch(1),⋯,Y^batch(n)\]\\hat{Y}\_{\\rm batch}=\[\\hat{Y}\_{\\rm batch}^{(1)},\\cdots,\\hat{Y}\_{\\rm batch}^{(n)}\] with VbatchV\_{\\rm batch} and YbatchY\_{\\rm batch} into the optimizer for obtaining a new set of guiding questions by Eq. ( [2](https://arxiv.org/html/2412.01095v1#S3.E2 "Equation 2 ‣ 3.2 Training in VERA: Finding Guiding Questions for VAD via Verbalized Learning ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) as:
𝐐t+1=fopt(t)​(Vbatch,Y^batch,Ybatch)\\mathbf{Q}\_{t+1}=f\_{\\rm opt}^{(t)}(V\_{\\rm batch},\\hat{Y}\_{\\rm batch},Y\_{\\rm batch});

\# _Compute the validation accuracy with the learned guiding questions periodically_

t←t+1t\\leftarrow t+1;

if _t​mod​μ=0t\ {\\rm mod}\ \\mu=0_ then

Test 𝐐t\\mathbf{Q}\_{t} on the validation set DvalD\_{\\rm val} and compute the validation accuracy Acct{\\rm Acc}\_{t};

if _Acct>Acc∗{\\rm Acc}\_{t}>{\\rm Acc}^{\*}_ then

Update 𝐐∗←𝐐t\\mathbf{Q}^{\*}\\leftarrow\\mathbf{Q}\_{t};

Update ACC∗←ACCt{\\rm ACC}^{\*}\\leftarrow{\\rm ACC}\_{t};

end if

end if

end while

Return𝐐∗\\mathbf{Q}^{\*};

Initial 𝐐0\\mathbf{Q}\_{0}. The initial guiding questions 𝐐0\\mathbf{Q}\_{0} are “ _1\. Is there any suspicious person or object that looks unusual in this scene? 2. Is there any behavior that looks unusual in this scene?_”. These two questions are manually written and inspired by previous VAD methods, which assume anomaly as something or somebody with unusual appearance or motions \[ [46](https://arxiv.org/html/2412.01095v1#bib.bib46 ""), [14](https://arxiv.org/html/2412.01095v1#bib.bib14 "")\]. This set of questions is also the “manually written questions by human” in Table [6](https://arxiv.org/html/2412.01095v1#S4.T6 "Table 6 ‣ 4.3 Ablation Studies ‣ 4 Experiments and Results ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), which is suboptimal in guiding frozen VLMs to detect anomalies. The key idea of training is to use verbalized learning to iteratively update 𝐐\\mathbf{Q} given a suboptimal 𝐐0\\mathbf{Q}\_{0}.

Learner Prompt Template θ\\theta.
We detail the design of θ\\theta as follows. As shown in Fig. [2](https://arxiv.org/html/2412.01095v1#S3.F2 "Figure 2 ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), the learner prompt template θ\\theta includes four sections, _i.e_., Model Description, Prompt Questions, Input, and Output Formatting. To specify:

- •


Model Description: This section introduces the learning task, providing the learner with the necessary background knowledge to understand the objective. It clarifies what the learner is expected to predict based on the given visual input data.

- •


Prompt Questions: This section presents a general prompt to guide the learner’s reasoning process. Specific prompts, denoted as 𝐐t\\mathbf{Q}\_{t}, will be inserted here to facilitate reasoning within a frozen VLM.

- •


Input: This section simply stores the visual tokens. When the VLM reads this, it will correlate the read text with the visual inputs.

- •


Output Formatting: The last section in θ\\theta mainly provides information on output formats to ensure that VLMs think through the given questions 𝐐t\\mathbf{Q}\_{t} and output a prediction in a format easy for post-processing in computers.


Optimizer Prompt Template ψ\\psi. As shown in Fig. [2](https://arxiv.org/html/2412.01095v1#S3.F2 "Figure 2 ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), the optimizer prompt template includes seven sections, _i.e_., Instruction, Inputs, Model Description, Current Prompt Questions, Model Predictions & Targets, and Optimization Instruction:

- •


Instruction: The prompt template begins with an introduction outlining the responsibilities of the optimizer, clearly stating that its primary task is to optimize the guiding questions provided.

- •


Inputs: This section is used to attach the batched visual data for the reference of the optimizer.

- •


Model Description: The learning task of the learner is reiterated here for the information of the optimizer.

- •


Current Prompt Questions: The guiding questions used by the learner in the current iteration are shown here for the reference of the optimizer.

- •


Model Predictions & Targets: The batched numerical predictions and the ground truths are shown here for foptf\_{\\rm opt}. These two inputs can tell the optimizer how well the learner does in the learning task on the mini-batch data.

- •


Optimization Instruction: The final section includes the instruction to ask the optimizer to think step by step with all the information above and output a new set of prompt questions with the required format.


Figure 8: The validation accuracy given different learned guiding questions from each iteration. The graph is smoothed with moving average (window size 5) for better readability.

#### A.2 Details for Iterative Update by the Optimizer

In training, we assess the quality of the learned guiding questions by the accuracy of the validation set. We show the validation accuracy from different questions 𝐐t\\mathbf{Q}\_{t} obtained every 100 iterations (mini-batches) in Fig. [8](https://arxiv.org/html/2412.01095v1#A1.F8 "Figure 8 ‣ A.1 Algorithm ‣ Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). In the duration of up to 5000 iterations in training, the observed plot in Fig. [8](https://arxiv.org/html/2412.01095v1#A1.F8 "Figure 8 ‣ A.1 Algorithm ‣ Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") contains three oscillations, each consisting of an increase in validation accuracy followed by a decrease. The increase represents that the optimizer VLM gradually finds better questions for the binary classification learning task when it sees more batched data, which shows the optimizer can understand its responsibility well and find better questions effectively. Meanwhile, we note that verbal optimization may not always lead to an increase. This is probably because the optimization is completely verbalized, and the VLM will have an inertial thinking behavior like humans, which gets the optimizer stuck in the wrong direction and makes it continue the optimization in a direction that is not beneficial. As a result, this causes the validation accuracy to decrease sometimes. Despite that, because of the guidance provided by the optimizer prompt template ψ\\psi, the optimizer can overcome its pitfalls in thinking and find good guiding questions in a new direction, which leads to an increase in validation accuracy afterward. This is an interesting phenomenon due to the distinction between verbal learning and traditional numerical optimization algorithms, and it will be a promising future direction to reduce the time in overcoming pitfalls in thinking for VLMs during verbalized learning.

Figure 9: We take the guiding questions 𝐐\\mathbf{Q} learned from the 100th iteration to the 700th iteration for illustration purpose. During the updating process, the optimizer gradually concretizes anomaly patterns that can be applied to different scenarios in a concise expression.

In addition, w.l.og., we take learned questions from the 100th iteration to the 700th iteration (which are within the first epoch) for illustration to show the process of updating 𝐐\\mathbf{Q} by the optimizer in Fig. [9](https://arxiv.org/html/2412.01095v1#A1.F9 "Figure 9 ‣ A.2 Details for Iterative Update by the Optimizer ‣ Appendix A Training in VERA ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). First, as the optimizer sees more videos, it tries to make the questions focus on a more general setting. For example, the questions in the 100th iteration focus on “street” and “store” scenes. After more iterations, the questions become more generalizable for a general environment and focus on the elements that cause anomalies. Additionally, the anomalous pattern descriptions become more diverse as the optimization continues. To illustrate, in the beginning, the questions mostly pay attention to the humans, objects, and their interaction. In later iterations, the optimizers gradually summarize some previous questions into one and raise questions considering the overall environment (Q5 from the 700th iteration). Therefore, the verbalized learning framework proposed in this paper is effective in finding a diverse set of guiding questions for VAD that apply to general cases, which can elicit the reasoning of a frozen VLM in VAD.

### Appendix B Additional Experiments and Results

#### B.1 Comparison to the State-of-the-art Methods on XD-Violence Measured by AP

| Method | AP |
| _Non-Explainable VAD Methods_ |
| Wu et al.†\[ [45](https://arxiv.org/html/2412.01095v1#bib.bib45 "")\] | 78.64 |
| OVVAD \[ [46](https://arxiv.org/html/2412.01095v1#bib.bib46 "")\] | 66.53 |
| S3R†\[ [44](https://arxiv.org/html/2412.01095v1#bib.bib44 "")\] | 80.26 |
| RTFM†\[ [38](https://arxiv.org/html/2412.01095v1#bib.bib38 "")\] | 77.81 |
| MSL†\[ [21](https://arxiv.org/html/2412.01095v1#bib.bib21 "")\] | 78.58 |
| MGFN†\[ [7](https://arxiv.org/html/2412.01095v1#bib.bib7 "")\] | 80.11 |
| CLIP-TSA†\[ [17](https://arxiv.org/html/2412.01095v1#bib.bib17 "")\] | 82.19 |
| _Explainable VAD Methods_ |
| Holmes-VAD†\[ [58](https://arxiv.org/html/2412.01095v1#bib.bib58 "")\] | 84.96 |
| LAVAD \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 62.01 |
| ZS CLIP \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 17.83 |
| ZS IMAGEBIND-I\[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 27.25 |
| ZS IMAGEBIND-V\[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] | 25.36 |
| LLAVA-1.5 \[ [22](https://arxiv.org/html/2412.01095v1#bib.bib22 "")\] | 50.26 |
| VERA | 70.54 |

Table 11: AP (%) on XD-Violence. †\\dagger indicates VAD methods are trained on entire training frames. No instruction tuning is used for Holmes-VAD.

The comparison results regrading average precision (AP), _i.e_., the area under the frame-level precision-recall curve, on XD-Violence are shown in Table [11](https://arxiv.org/html/2412.01095v1#A2.T11 "Table 11 ‣ B.1 Comparison to the State-of-the-art Methods on XD-Violence Measured by AP ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). Compared to AUC, AP focuses on measuring the ability to identify the positive class (anomaly), while AUC measures how well a method separates anomaly and normalcy in general. We provide the analysis of the results as follows.

Firstly, under such a distinct property of AP, as pointed out by \[ [46](https://arxiv.org/html/2412.01095v1#bib.bib46 "")\], methods trained on the whole training set and utilizing all frames will enjoy advantages when measuring VAD performance by AP. As a result, CLIP-TSA and Holmes-VAD, two methods using the whole training frames, attain the highest AP in the category of non-explainable and explainable VAD, respectively. We acknowledge there is a gap between VERA and these two methods under AP on XD-Violence, which is understandable because they use the whole training frames to improve the ability to find anomalies of classifiers. To illustrate, in training VERA only samples 8 frames for each video and only uses 0.19% total frames (31,632 out of 16,378,527) for training on XD-Violence. Thus, our training is dramatically light compared to the methods like CLIP-TSA and Holmes-VAD in Table [11](https://arxiv.org/html/2412.01095v1#A2.T11 "Table 11 ‣ B.1 Comparison to the State-of-the-art Methods on XD-Violence Measured by AP ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). With fewer frames used for training, VERA unavoidably achieve lower AP (which only considers positive cases) compared to those that have more, for it relies on fewer training data. In addition, we want to point out that judging the VAD performance solely by AP on XD-Violence can be biased. This is because the ratio of positive frames in XD-Violence (23.07%) in test videos is overly higher than other datasets like UCF-Crime (7.92%), which is unrealistic because the anomaly is sparse in the real world \[ [35](https://arxiv.org/html/2412.01095v1#bib.bib35 "")\]. Given that, only focusing on the comparison in AP on XD-Violence would amplify the bias in VAD performance evaluation, and we recommend taking into consideration other factors like training costs and the comprehensive ability of distinguishing anomaly and normality by the methods in evaluation.

Secondly, among the methods (OVVAD, LAVAD, ZS CLIP, ZS IMAGEBIND, and LLAVA-1.5) that does not use full frames for training, VERA achieves the best AP in this fair comparison, surpassing the second best method in the Explainable VAD category (LAVAD) over 8.53%, which showcases the effectiveness of using learned guiding question to prompt frozen VLMs for VAD.

To conclude, it is unfair to only judge VAD performance by AP on XD-Violence without considering the training costs and the relatively imbalanced frame distribution in test videos. Considering all factors into consideration, VERA is a favorable method used for VAD in detecting anomalies.

#### B.2 Discussion on Generalizability of Used Questions

During the optimization of 𝐐\\mathbf{Q}, because of the randomness involved in this process, the optimizer may output certain guiding questions that only focus on one specific surrounding. We find an interesting phenomenon on VLMs in VAD that guiding questions related to a specific scenario yield inferior VAD performance compared to the general questions in both general cases and specific cases.

To illustrate, we take two sets of specific questions for analysis. The first example is a set of guiding questions 𝐐traffic\\mathbf{Q}\_{\\rm traffic} that only ask the VLM to consider anomalies related to the traffic as follows:

1. 1.


_Are there any vehicles or people violating traffic rules?_

2. 2.


_Are there any accidents or near-accidents occurring?_

3. 3.


_Are there any objects or people obstructing the normal flow of traffic?_

4. 4.


_Are there any unusual or unexpected behaviors from pedestrians or drivers?_

5. 5.


_Are there any emergency vehicles or personnel present?_


The second example is another set of guiding questions 𝐐store\\mathbf{Q}\_{\\rm store} that only ask the VLM to identify anomalies in a store setting, which includes questions like:

1. 1.


_Are there any individuals loitering or behaving suspiciously inside the store?_

2. 2.


_Is there any unusual activity inside the store, such as tampering with items or attempting to enter restricted areas?_

3. 3.


_Are there any signs of forced entry or damage to the store’s entrance?_

4. 4.


_Are there any individuals present who seem to be watching or waiting for something specific inside the store?_

5. 5.


_Are there any interactions between individuals inside the store that appear suspicious or out of the ordinary?_


Thus, 𝐐traffic\\mathbf{Q}\_{\\rm traffic} and 𝐐store\\mathbf{Q}\_{\\rm store} focuses on the specific anomalies of traffic accidents and shoplifting, respectively, while the 𝐐∗\\mathbf{Q}^{\*} that we find focuses on general cases and includes the following questions:

1. 1.


_Are there any people in the video who are not in their typical positions or engaging in activities that are not consistent with their usual behavior?_

2. 2.


_Are there any vehicles in the video that are not in their typical positions or being used in a way that is not consistent with their usual function?_

3. 3.


_Are there any objects in the video that are not in their typical positions or being used in a way that is not consistent with their usual function?_

4. 4.


_Is there any visible damage or unusual movement in the video that indicates an anomaly?_

5. 5.


_Are there any unusual sounds or noises in the video that suggest an anomaly?_


The comparison results of 𝐐∗\\mathbf{Q}^{\*}, 𝐐traffic\\mathbf{Q}\_{\\rm traffic}, and 𝐐store\\mathbf{Q}\_{\\rm store} in detecting anomalies in general cases (all testing videos on UCF-Crime), traffic scenes (testing videos from the Traffic Accident category on UCF-Crime), and the store scenes (testing videos from the Shoplifting category on UCF-Crime) are shown in Table [12](https://arxiv.org/html/2412.01095v1#A2.T12 "Table 12 ‣ B.2 Discussion on Generalizability of Used Questions ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). It indicates that 𝐐∗\\mathbf{Q}^{\*} performs the best in both general cases and two specific cases like in traffic and store scenes. This is because the overly specific definition of anomalies like 𝐐traffic\\mathbf{Q}\_{\\rm traffic} and 𝐐store\\mathbf{Q}\_{\\rm store} makes it harder for a VLM to classify one clip into an anomaly and leads to more false negatives in its prediction given those specific questions, which degrades the performance. Therefore, we recommend using general questions like the ones shown in 𝐐∗\\mathbf{Q}^{\*} in frozen VLMs for VAD.

| Questions | Scenario |
| --- | --- |
| All | Traffic | Store |
| --- | --- | --- |
| 𝐐∗\\mathbf{Q}^{\*} | 86.55 | 70.43 | 72.58 |
| 𝐐traffic\\mathbf{Q}\_{\\rm traffic} | 82.59 | 67.53 | / |
| 𝐐store\\mathbf{Q}\_{\\rm store} | 76.67 | / | 44.84 |

Table 12: General guiding questions outperform specific ones measured by AUC (%) on UCF-Crime. Specific questions are not tested on other specific scenarios, which is indicated by a slash (/).

#### B.3 Hyperparameters in Inference and Sensitivity Test

Hyperparameters in Inference
During inference, in Step 1, following \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\], the interval between each segment center dd is 16 frames. In Step 2, we use ImageBind \[ [11](https://arxiv.org/html/2412.01095v1#bib.bib11 "")\] as the feature extractor in computing segment similarity as  \[ [55](https://arxiv.org/html/2412.01095v1#bib.bib55 "")\] does, and the number of retrieved segments KK depends on the total number of segments hh in each test video VV. Setting KK to (0.1⋅h)(0.1\\cdot h) to (0.15⋅h)(0.15\\cdot h) is generally good. We set KK to (0.1⋅h)(0.1\\cdot h) for UCF-Crime and to (0.15⋅h)(0.15\\cdot h) for XD-Violence. The temperature τ\\tau in the Softmax function is set to 10 for both datasets in Eq. ( [4](https://arxiv.org/html/2412.01095v1#S3.E4 "Equation 4 ‣ 3.3 Inference in VERA: Coarse-to-Fine Anomaly Scoring by Guiding Questions and Contexts ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")). In Step 3, due to the properties of datasets, we set the filter size ω\\omega of G⁡(p)G(p) to 15 and σ1\\sigma\_{1} to 10 for UCF-Crime, while setting ω\\omega to 30 and σ1\\sigma\_{1} to 30 for XD-Violence. For position weighting, we set c=floor⁡(F/2)c={\\rm floor}(F/2) and σ2=floor⁡(F/2)\\sigma\_{2}={\\rm floor}(F/2) for both datasets to make sure the position weight covers the whole video sequence.

W.l.o.g, we test the sensitivity of the VAD performance of VERA regarding hyperparameters on UCF-Crime.

Sensitivity Test for KK. As shown in Table [13](https://arxiv.org/html/2412.01095v1#A2.T13 "Table 13 ‣ B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), as the number of retrieved segments increases from 0 to 0.15⋅h0.15\\cdot h, the AUC gradually increases from to 85.21% to 86.61%. Meanwhile, if we randomly select 0.1⋅h0.1\\cdot h segments for retrieval, the AUC is even lower than the performance without retrieval. Thus, using Eq. ( [4](https://arxiv.org/html/2412.01095v1#S3.E4 "Equation 4 ‣ 3.3 Inference in VERA: Coarse-to-Fine Anomaly Scoring by Guiding Questions and Contexts ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) for retrieval is necessary. Meanwhile, having a large KK greater than 0.15⋅h0.15\\cdot h will introduce some noise in Eq. ( [4](https://arxiv.org/html/2412.01095v1#S3.E4 "Equation 4 ‣ 3.3 Inference in VERA: Coarse-to-Fine Anomaly Scoring by Guiding Questions and Contexts ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) and downgrade the AUC slightly. Thus, selecting 0.1⋅h0.1\\cdot h or 0.15⋅h0.15\\cdot h for KK is generally good choice.

| Ratio (%) | 0 | 5 | 10 | 15 | 20 | 25 |
| --- | --- | --- | --- | --- | --- | --- |
| AUC (%) | 85.21 | 86.48 | 86.55 | 86.61 | 86.42 | 86.19 |

Table 13: Influence of the number of retrieved segments on AUC. The AUC of not using retrieval (Ratio == 0%) and randomly selecting 10% segments for Eq. ( [4](https://arxiv.org/html/2412.01095v1#S3.E4 "Equation 4 ‣ 3.3 Inference in VERA: Coarse-to-Fine Anomaly Scoring by Guiding Questions and Contexts ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) is 85.21% and 84.55%, respectively.

Sensitivity Test for ω\\omega. The filter size decides how many local segments are incorporated for the current segment for Gaussian smoothing. From Table [14](https://arxiv.org/html/2412.01095v1#A2.T14 "Table 14 ‣ B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), we find that AUC converges when the filter size increases to 15. Meanwhile, the VAD performance measured AUC is insensitive to ω\\omega and does not fluctuate much. Thus, we can set the filter size with a medium number like 15.

| ω\\omega | 5 | 10 | 15 | 20 | 25 |
| --- | --- | --- | --- | --- | --- |
| AUC (%) | 86.25 | 86.43 | 86.55 | 86.61 | 86.60 |

Table 14: Influence of filter size ω\\omega in Gaussian Smoothing on AUC.

Sensitivity Test for σ1\\sigma\_{1}. The AUC performance is also robust on the choice of σ1\\sigma\_{1}. As, shown in Fig. [15](https://arxiv.org/html/2412.01095v1#A2.T15 "Table 15 ‣ B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), when we set σ1\\sigma\_{1} greater than 1, the AUC generally remains around 86.50%, which again shows the robustness of the design of anomaly scoring in VERA. We can set σ1\\sigma\_{1} as 10 for VERA.

| σ1\\sigma\_{1} | 1 | 5 | 10 | 15 | 20 |
| --- | --- | --- | --- | --- | --- |
| AUC (%) | 86.17 | 86.49 | 86.55 | 86.49 | 86.54 |

Table 15: Influence of σ1\\sigma\_{1} in Gaussian Smoothing on AUC.

Sensitivity Test for τ\\tau. The temperature hyperparameter τ\\tau in Eq. ( [4](https://arxiv.org/html/2412.01095v1#S3.E4 "Equation 4 ‣ 3.3 Inference in VERA: Coarse-to-Fine Anomaly Scoring by Guiding Questions and Contexts ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) controls the entropy of the distribution obtained from the Softmax function while preserving the rank of each element. As demonstrated in Table [16](https://arxiv.org/html/2412.01095v1#A2.T16 "Table 16 ‣ B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), when τ\\tau is a small number like 10e-8 that is close to 0, the distributions tend to become a trivial distribution with all mass concentrated on the highest-probability class (corresponding to the segment itself), and the result is the same as the one by not using retrieval. As we gradually increase τ\\tau to a reasonably large number (from 0.01 to 1), the AUC value converges around 86.55% with no obvious fluctuation, again proving the robustness of anomaly scoring in VERA regarding hyperparameter selection. Note that when τ\\tau approaches +∞+\\infty, the distribution tends to become a uniform distribution, which yields an AUC of 86.59%. From the discussion above, we can generally choose τ\\tau to be an number in \[0.01, 1\] in implementation.

| τ\\tau | 10e-8 | 0.01 | 0.1 | 1 | +∞+\\infty |
| --- | --- | --- | --- | --- | --- |
| AUC (%) | 85.21 | 86.31 | 86.55 | 86.58 | 86.59 |

Table 16: Influence of τ\\tau in Eq. ( [4](https://arxiv.org/html/2412.01095v1#S3.E4 "Equation 4 ‣ 3.3 Inference in VERA: Coarse-to-Fine Anomaly Scoring by Guiding Questions and Contexts ‣ 3 The VERA Framework ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) on AUC.

Sensitivity Test for σ2\\sigma\_{2}. From Table [17](https://arxiv.org/html/2412.01095v1#A2.T17 "Table 17 ‣ B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), we find that setting σ2=0.5​F\\sigma\_{2}=0.5F encodes the position information best in the anomaly score. A drop is noticeable if we choose σ2\\sigma\_{2} less than 0.5​F0.5F for it will not cover the whole sequence, which is reasonable, while choosing a σ2\\sigma\_{2} great than 0.5​F0.5F does not change much. Thus, based on the physical meaning of σ2\\sigma\_{2}, which controls the width of the distribution, we should make σ2\\sigma\_{2} equal to 0.5​F0.5F in anomaly scoring.

| σ2\\sigma\_{2} | w/o Weighting | 0.25 | 0.5 | 0.75 |
| --- | --- | --- | --- | --- |
| AUC (%) | 85.48 | 85.43 | 86.55 | 86.27 |

Table 17: Influence of σ2\\sigma\_{2} in Position Weighting on AUC.![Refer to caption](https://arxiv.org/html/2412.01095v1/fig10.png)Figure 10: Given the normal video “Normal\_Videos\_018\_x264”, the frozen VLM (InternVL2-8B) can conclude that no anomaly happens in the video under the guidance of 𝐐∗\\mathbf{Q}^{\*}, which is aligned with the ground truth. Since the anomaly scores for all scenes are zeros by VERA, we do not show the complete anomaly scores with an additional figure.![Refer to caption](https://arxiv.org/html/2412.01095v1/fig11.png)Figure 11: Given the abnormal video “RoadAccidents127\_x264”, the frozen VLM (InternVL2-8B) can generate reasonable explanations aligned with the semantic change observed in each scene under the guidance of 𝐐∗\\mathbf{Q}^{\*}. The complete anomaly scores are shown in Fig. [12](https://arxiv.org/html/2412.01095v1#A2.F12 "Figure 12 ‣ B.4 Additional Qualitative Results & Case Studies ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models").

#### B.4 Additional Qualitative Results & Case Studies

W.l.o.g., we take one normal video (“Normal\_Videos\_018\_x264”) and another abnormal video (“RoadAccidents127\_x264”) from the UCF-Crime dataset to demonstrate the explanations provided by a frozen VLM (InternVL2-8B) achieved by using the learned guiding questions 𝐐∗\\mathbf{Q}^{\*}.

First, in Fig. [10](https://arxiv.org/html/2412.01095v1#A2.F10 "Figure 10 ‣ B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models") we showcase the explanation of anomaly scoring by VERA regarding a normal video “Normal\_Videos\_018\_x264” in UCF-Crime, which is taken in an airport hallway where no anomaly happens. For this video, VERA assigns a 0 score to each frame. As shown in Fig. [10](https://arxiv.org/html/2412.01095v1#A2.F10 "Figure 10 ‣ B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"), for the selected scenes in this video, VERA explains that this is because there are no events that conform to the anomaly descriptions in 𝐐∗\\mathbf{Q}^{\*}. Such explanations are consistent with the recording and again manifest the effectiveness of eliciting the reasoning ability in a frozen VLM for VAD by using learned guiding questions. Note that we do not have an additional figure illustrating the anomaly score dynamic for this video because all scenes are assigned 0 scores by VERA.

Figure 12: Anomaly scores generated by VERA (with InternVL2-8B) in “RoadAccidents127\_x264” from UCF-Crime.

Next, we select 6 representative scenes in the abnormal video (“RoadAccidents127\_x264”) and show the corresponding explanation provided by the frozen VLM in Fig. [11](https://arxiv.org/html/2412.01095v1#A2.F11 "Figure 11 ‣ B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). The main anomaly that happens in this video is a traffic accident where a truck crashes into a train from Frame 2160 to Frame 2299, which corresponds to the 5th scene in Fig. [11](https://arxiv.org/html/2412.01095v1#A2.F11 "Figure 11 ‣ B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). In particular, the figure shows that the learned question “Is there any visible damage or unusual movement in the video that indicates an anomaly?” in 𝐐∗\\mathbf{Q}^{\*} makes the frozen VLM find a good way to express what it sees in the 5th scene and understand this is an anomaly because the crash is unusual and dangerous. The other scenes are also well explained by the frozen VLM under 𝐐∗\\mathbf{Q}^{\*}. Thus, this again verifies that the learned guiding questions can successfully trigger reasonable explanations in the adopted frozen VLM for VAD.

Meanwhile, we also include the anomaly scores generated by VERA for the abnormal video in Fig. [12](https://arxiv.org/html/2412.01095v1#A2.F12 "Figure 12 ‣ B.4 Additional Qualitative Results & Case Studies ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models"). Most frames are assigned to zero except the scenes when someone crosses the road at an unusual speed (the 2nd scene in Fig. [11](https://arxiv.org/html/2412.01095v1#A2.F11 "Figure 11 ‣ B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")) and the truck-train crash happens (the 5th scene in Fig. [11](https://arxiv.org/html/2412.01095v1#A2.F11 "Figure 11 ‣ B.3 Hyperparameters in Inference and Sensitivity Test ‣ Appendix B Additional Experiments and Results ‣ Appendix ‣ VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models")). This fluctuation is aligned with the ground truth annotation and common sense about an anomaly, which shows that the anomaly scoring proposed in VERA is reasonable.