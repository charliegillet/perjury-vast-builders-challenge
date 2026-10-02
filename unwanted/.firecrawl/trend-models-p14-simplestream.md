Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2604.02317v1 \[cs.CV\] 02 Apr 2026

# A Simple Baseline for Streaming Video Understanding

Yujiao Shen
Affiliation: S-Lab, Nanyang Technological University
Shulin Tian
Affiliation: S-Lab, Nanyang Technological University
Jingkang Yang
Affiliation: S-Lab, Nanyang Technological University
Ziwei Liu
Affiliation: S-Lab, Nanyang Technological University

###### Abstract

Recent streaming video understanding methods increasingly rely on
complex memory mechanisms to handle long video streams. We challenge
this trend with a simple finding: a sliding-window baseline that feeds
only the most recent NN frames to an off-the-shelf VLM already matches
or surpasses published streaming models. We formalize this baseline as
SimpleStream and evaluate it against 13 major offline and
online video LLM baselines on OVO-Bench and StreamingBench. Despite its
simplicity, SimpleStream delivers consistently strong
performance. With only 4 recent frames, it reaches 67.7% average
accuracy on OVO-Bench and 80.59% on StreamingBench. Controlled
ablations further show that the value of longer context is
backbone-dependent rather than uniformly increasing with model scale,
and reveal a consistent perception-memory trade-off: adding more
historical context can improve recall, but often weakens real-time
perception. This suggests that stronger memory, retrieval, or
compression modules should not be taken as evidence of progress unless
they clearly outperform SimpleStream under the same
protocol. We therefore argue that future streaming benchmarks should
separate recent-scene perception from long-range memory, so that performance improvements
from added complexity can be evaluated more clearly.

††date: April 1, 2026††Codebase: [https://github.com/EvolvingLMMs-Lab/SimpleStream](https://github.com/EvolvingLMMs-Lab/SimpleStream "")††Project Page: [https://simple-stream.github.io/](https://simple-stream.github.io/ "")

## 1 Introduction

Streaming video understanding increasingly relies on complex
memory-centric designs to handle long streams under causal
constraints ( [Qian et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib10 ""); [Qian et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib11 ""); [Di et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib2 ""); [Chen et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib1 ""); [Yao et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib25 ""); [Zhang et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib28 ""); [Zeng et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib26 ""); [Zhang et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib29 "")).
Across these methods, the complexity typically lies in how past
context is managed, for example through explicit memory banks,
retrieval over prior observations, or compression of visual and
latent representations under bounded budgets. This trend reflects a common assumption: strong streaming
performance requires increasingly complex memory mechanisms.

![Refer to caption](https://arxiv.org/html/2604.02317v1/figures/baseline_teaser.png)Figure 1: A Strong Simple Baseline for Streaming Video Understanding. (a) Overview of SimpleStream: given a streaming video and a query, only the most recent NN frames are fed to an off-the-shelf VLM. (b) Perception-memory comparison on OVO-Bench, where SimpleStream consistently lies on the upper-right frontier across backbone families and window sizes.

However, these increasingly elaborate designs have often delivered
modest or uneven gains, leaving a more fundamental question
underexplored: is such memory complexity actually necessary for
strong streaming video understanding? We show that a very simple
baseline can already outperform published streaming methods.
Figure [1](https://arxiv.org/html/2604.02317v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ A Simple Baseline for Streaming Video Understanding") previews this result, where a minimal
recent-context method lies on the upper-right frontier of both
perception and memory performance.

Motivated by this observation, we introduce SimpleStream, an
intentionally simple baseline for streaming video understanding.
Given a query at time tt, SimpleStream feeds the last NN
observed frames and the query text directly to the base VLM.
The design is minimal by construction: preserve only a short recent
window and let a strong backbone operate on clear, uncompressed recent
evidence.

Despite its minimal design, SimpleStream achieves state-of-the-art performance on both OVO-Bench ( [Li et al., 2025b](https://arxiv.org/html/2604.02317v1#bib.bib7 "")) and
StreamingBench ( [Lin et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib8 "")), while also maintaining
the lowest peak GPU memory and competitive latency among all compared
streaming methods. Therefore, a strong backbone plus uncompressed recent
visual context is already a highly competitive streaming solution.
It also exposes two broader issues: injecting additional memory can
degrade real-time perception, and longer context is not uniformly
rewarded even across model scales and backbone families.
These observations make it necessary to report strong simple baselines before
claiming gains from additional streaming complexity.

Our analyses and discussion show that this pattern is systematic rather
than incidental. Across controlled recency-window, model-scaling, and
Visual-RAG ablations, adding more historical context is not uniformly
beneficial. A modest increase in recent context can help, but the
preferred window size depends on model scale and backbone family rather
than increasing monotonically with parameter count. More broadly, extra
historical context can improve memory-oriented behavior, but often at a
cost to present-scene perception. We further show that current benchmark
design can amplify this tension, making aggregate gains difficult to
interpret without separating perception-oriented and memory-oriented
behavior.

These findings motivate a practical evaluation standard for streaming
video understanding: under matched backbones and protocols, reported
gains should be assessed against strong recency baselines and
disaggregated perception-versus-memory metrics, so that the benefit of
added complexity is identifiable rather than assumed.

Our contributions are as follows:

- •


We introduce SimpleStream, a deliberately minimal
streaming baseline that answers each query using only the last NN
frames from the causal prefix with an off-the-shelf VLM, without
additional memory, retrieval, compression, or training.

- •


Through comprehensive evaluation on OVO-Bench and StreamingBench, we show that
a simple recent-context baseline is sufficient to outperform prior
streaming methods while maintaining favorable peak GPU memory and
latency.

- •


We provide controlled analyses of recent-window size, model
scale, Visual-RAG augmentation, and benchmark structure, showing that
the utility of longer context is backbone-dependent rather than
monotonically improved by larger models, and that memory-side gains
often come with perception costs.

- •


We argue that future streaming video understanding work should adopt strong recency baselines and disaggregated reporting as default evaluation practice, so that gains from added streaming complexity are demonstrated rather than assumed.


## 2 Related Work

Streaming video understanding.
Recent streaming video understanding research can be broadly organized into three directions: proactive response and interaction, streaming-oriented training, and memory-centric context management. These directions address different challenges in online video understanding, including when a model should respond, how it can align perception with generation under causal constraints, and how it can preserve useful past information under limited compute and memory budgets. Proactive systems concentrate on response timing and interaction policy, for example by predicting answer readiness ( [Azad et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib30 ""); [Liu et al., 2026b](https://arxiv.org/html/2604.02317v1#bib.bib32 ""); [Xia et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib19 ""); [Yang et al., 2025c](https://arxiv.org/html/2604.02317v1#bib.bib23 "")), decoupling decision from
perception ( [Qian et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib11 "")), or using an external trigger for response generation ( [Wang et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib15 "")).
Training-oriented approaches instead make online generation feasible
through supervision, positional design, and temporal alignment, as in
LiveCC and Streamo ( [Chen et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib1 ""); [Xia et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib19 "")), without
making memory design the primary object of study.

Memory and context management remain a central concern in streaming video understanding. What differs across methods is not whether history matters, but how explicitly it is modeled and through which mechanism.
Some methods compress or prune redundant tokens or KV states ( [Yao et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib25 ""); [Chen et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib49 ""); [Jin et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib5 ""); [Zhang et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib29 ""); [Wang et al., 2025c](https://arxiv.org/html/2604.02317v1#bib.bib17 "")).
Others make past information query-addressable through retrieval or adaptive KV
selection ( [Ning et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib48 ""); [Di et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib2 ""); [Yang et al., 2025b](https://arxiv.org/html/2604.02317v1#bib.bib24 "")).
Another line introduces explicit external or hierarchical memory
structures ( [Xiong et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib20 ""); [Azad et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib30 ""); [Guo et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib31 ""); [Zhang et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib28 ""); [Zhou et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib36 ""); [Liu et al., 2026b](https://arxiv.org/html/2604.02317v1#bib.bib32 "")),
including StreamForest and FluxMem ( [Zeng et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib26 ""); [Xie et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib22 "")). Some approaches instead summarize long streams through learned latent or
recurrent state, _e.g._, VideoStreaming ( [Qian et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib10 ""))
and Dispider ( [Qian et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib11 "")). Although these methods differ in implementation, they are often motivated by the view that strong streaming performance benefits from complex memory
mechanisms for preserving history. SimpleStream makes the
recent-context baseline the primary reference point. This reframing turns what is usually a peripheral ablation into a direct test of when
additional memory mechanisms deliver meaningful gains.

Streaming video benchmarks.
Evaluating streaming video understanding requires benchmarks that
distinguish among causal online reasoning, proactive interaction, and
retrospective video comprehension. OVO-Bench ( [Li et al., 2025b](https://arxiv.org/html/2604.02317v1#bib.bib7 "")),
StreamingBench ( [Lin et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib8 "")), and other causal
benchmarks ( [Huang et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib4 ""); [Liu et al., 2026a](https://arxiv.org/html/2604.02317v1#bib.bib33 ""); [Xu et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib21 ""); [Xia et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib19 ""); [Zeng et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib26 ""); [Jin et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib5 ""); [Chen et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib1 ""))
evaluate models under
observed-only constraints, requiring both current-scene perception and
the use of prior context. Benchmarks such as
OmniMMI ( [Wang et al., 2025f](https://arxiv.org/html/2604.02317v1#bib.bib13 "")) and
ProactiveVideoQA ( [Wang et al., 2025d](https://arxiv.org/html/2604.02317v1#bib.bib14 "")) instead emphasize
initiative, assistance, and turn-taking, a direction further developed
by RIVER, LiViBench, and
PhoStream ( [Shi et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib35 ""); [Wang et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib18 ""); [Lu et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib34 "")), with
additional benchmark formulations ( [Azad et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib30 ""); [Wang et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib15 ""); [Zhang et al., 2025c](https://arxiv.org/html/2604.02317v1#bib.bib27 "")). By
contrast, retrospective or offline video understanding benchmarks such
as LVBench ( [Wang et al., 2025b](https://arxiv.org/html/2604.02317v1#bib.bib12 "")), MLVU ( [Zhou et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib39 "")), and
EgoLifeQA ( [Yang et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib38 "")) target long-range temporal reasoning
and event understanding over full videos, but do not impose the same
causal streaming constraint ( [Fu et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib3 ""); [Li et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib6 ""); [Mangalam et al., 2023](https://arxiv.org/html/2604.02317v1#bib.bib9 "")).
To enable a
cleaner comparison between a strong simple baseline and more elaborate
streaming designs, we thus focus primarily on OVO-Bench and use
StreamingBench as a complementary evaluation.

![Refer to caption](https://arxiv.org/html/2604.02317v1/figures/landscape.png)Figure 2: A landscape of streaming video understanding methods. Most existing approaches differ mainly in how they preserve and reuse historical information under bounded budgets, while SimpleStream keeps only a small recent frame window.

## 3 From Complex Streaming Methods to SimpleStream

### 3.1 A Landscape of Streaming Video Understanding Methods

We study streaming video understanding under a causal observation protocol, where the model must answer each query using only past observations. At query time tt, the model must answer a text question
qtq\_{t} using only the observed prefix of the video stream up to tt,
without access to future frames or side information. Although the
visible prefix may grow arbitrarily long, the model can condition only
on a bounded representation at inference time under realistic limits on
memory, attention tokens, and per-step computation. We therefore view
streaming inference as a context-management problem: at each query, the
system must construct a bounded working context CtC\_{t} from the observed
history. This context must keep the answer grounded in what has been
seen while respecting a fixed streaming budget. Under this formulation, streaming
QA is not simply sequential decoding over a video prefix, but causal,
budgeted context management.

Figure [2](https://arxiv.org/html/2604.02317v1#S2.F2 "Figure 2 ‣ 2 Related Work ‣ A Simple Baseline for Streaming Video Understanding") groups prior methods by the mechanism
that expands CtC\_{t} beyond a short recency window. External-memory
systems maintain structured history online: StreamForest ( [Zeng et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib26 ""))
maintains an event-level tree whose insertion rule balances an explicit
penalty with temporal distance, content similarity, and merge
frequency, while Flash-VStream ( [Zhang et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib28 "")) uses fixed-size
Flash Memory with slots reserved for global summaries and salient frame
details. Retrieval-based methods retain past representations so they can be selected at query time. ReKV ( [Di et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib2 "")) stores a disk-backed historical
KV cache and loads query-conditioned KV states when a question arrives.
Compression targets the KV and attention budget directly;
HERMES ( [Zhang et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib29 "")) maintains a hierarchical memory view over
the KV state by reusing a compact cached representation. Latent-memory approaches learn a
constant-length state for the prefix: VideoStreaming ( [Qian et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib10 ""))
and Dispider ( [Qian et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib11 "")) use a compact LLM decoder to
compress the observed stream into fixed-size memory features, relying on
learned implicit memory and substantial supervised fine-tuning. Despite their differences, these methods share the goal of expanding or restructuring CtC\_{t} under a fixed streaming budget. This framing motivates a minimal baseline that constructs CtC\_{t} only from the most recent observations.

### 3.2 SimpleStream: A Simple Recent-N-Frames Baseline

Unlike prior streaming systems, we do not introduce an additional mechanism for managing long-range history. Instead, we introduce SimpleStream, a deliberately simple
baseline that isolates what current off-the-shelf VLMs can achieve using only recent visual context. Let the video stream be
represented as a sequence of frames, where fif\_{i} denotes the visual
frame at time step ii. Given a question qtq\_{t} at time tt, we feed the
base VLM only the most recent NN frames and the text query:

|     |     |     |
| --- | --- | --- |
|  | SimpleStream​(t)=VLM⁡({ft−N+1,…,ft},qt)\\textsc{SimpleStream}(t)=\\mathrm{VLM}\\bigl(\\{f\_{t-N+1},\\ldots,f\_{t}\\},\\,q\_{t}\\bigr) |  |

By construction, SimpleStream omits the additional memory mechanisms used in prior streaming systems. Frames outside the sliding window are discarded, so the per-query memory
and computation remain bounded by NN and do not grow with stream
length. SimpleStream introduces no architectural modification,
memory module, or additional training; it is an inference-time input
policy applied to an off-the-shelf VLM. We use it as a controlled
reference baseline to isolate how much streaming performance can be
obtained from recent visual context alone, while minimizing confounding
effects from additional training, module design, or system-level
engineering.

Table 1: Main results on OVO-Bench ( [Li et al., 2025b](https://arxiv.org/html/2604.02317v1#bib.bib7 "")) and
StreamingBench ( [Lin et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib8 "")).
Per-task accuracy on OVO-Bench under its Real-Time Visual Perception and
Backward Tracing tracks.
“StreamingBench” denotes RTVU accuracy.
“–” indicates unreported results.
†\\dagger: Qwen2.5-VL-7B + HERMES (4K tokens).
Task abbreviations follow OVO-Bench: OCR, ACR, ATR, STU, FPD, and OJR denote Optical Character Recognition, Action Recognition, Attribute Recognition, Spatial Understanding, Future Prediction, and Object Recognition; EPM, ASI, and HLD denote Episodic Memory, Action Sequence Identification, and Hallucination Detection.
“Avg.” is the mean of Real-Time and Backward category averages.
For a fair comparison with most baselines, we sample at 1 fps in SimpleStream and cap maximum frames at 2, 4, or 8.

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | #Frames | StreamingBench | OVO-Bench |
| Real-Time Visual Perception | Backward Tracing | Avg. |
| OCR | ACR | ATR | STU | FPD | OJR | Avg. | EPM | ASI | HLD | Avg. |
| Human | – | 91.46 | 94.0 | 92.6 | 94.8 | 92.7 | 91.1 | 94.0 | 93.2 | 92.6 | 93.0 | 91.4 | 92.3 | 92.77 |
| Offline Video LLMs |
| Qwen2.5-VL-7B ( [Bai et al., 2025b](https://arxiv.org/html/2604.02317v1#bib.bib41 "")) | 1 fps | 73.31 | 67.8 | 55.1 | 67.2 | 42.1 | 66.3 | 60.9 | 59.9 | 51.5 | 58.8 | 23.7 | 44.7 | 52.28 |
| LLaVA-OneVision-7B ( [Li et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib44 "")) | 32 | 71.12 | 66.4 | 57.8 | 73.3 | 53.4 | 71.3 | 62.0 | 64.0 | 54.2 | 55.4 | 21.5 | 43.7 | 53.85 |
| InternVL2-8B ( [Chen et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib40 "")) | 16 | 63.72 | 67.1 | 60.6 | 63.8 | 46.1 | 68.3 | 56.5 | 60.4 | 48.2 | 57.4 | 24.7 | 43.4 | 51.90 |
| LLaVA-Video-7B ( [Zhang et al., 2025b](https://arxiv.org/html/2604.02317v1#bib.bib43 "")) | 64 | – | 69.1 | 58.7 | 68.8 | 49.4 | 74.3 | 59.8 | 63.5 | 56.2 | 57.4 | 7.5 | 40.4 | 51.95 |
| Qwen2-VL-7B ( [Wang et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib42 "")) | 64 | 69.04 | 69.1 | 53.2 | 63.8 | 50.6 | 66.3 | 60.9 | 60.7 | 44.4 | 66.9 | 34.4 | 48.6 | 54.62 |
| LongVU-7B ( [Shen et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib45 "")) | 1 fps | – | 55.7 | 49.5 | 59.5 | 48.3 | 68.3 | 63.0 | 57.4 | 43.1 | 66.2 | 9.1 | 39.5 | 48.45 |
| Online / Streaming Video LLMs |
| VideoLLM-online-8B ( [Wang et al., 2025e](https://arxiv.org/html/2604.02317v1#bib.bib16 "")) | 2 fps | 35.99 | 8.1 | 23.9 | 12.1 | 14.0 | 45.5 | 21.2 | 20.8 | 22.2 | 18.8 | 12.2 | 17.7 | 19.26 |
| Flash-VStream-7B ( [Zhang et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib28 "")) | 1 fps | 23.23 | 24.2 | 29.4 | 28.5 | 33.7 | 25.7 | 28.8 | 28.4 | 39.1 | 37.2 | 5.9 | 27.4 | 27.90 |
| Dispider-7B ( [Qian et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib11 "")) | 1 fps | 67.63 | 57.7 | 49.5 | 62.1 | 44.9 | 61.4 | 51.6 | 54.6 | 48.5 | 55.4 | 4.3 | 36.1 | 45.35 |
| TimeChat-Online-7B ( [Yao et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib25 "")) | 1 fps | 75.28 | 75.2 | 46.8 | 70.7 | 47.8 | 69.3 | 61.4 | 61.9 | 55.9 | 59.5 | 9.7 | 41.7 | 51.80 |
| StreamForest-7B ( [Zeng et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib26 "")) | 1 fps | 77.26 | 68.5 | 53.2 | 71.6 | 47.8 | 65.4 | 60.9 | 61.2 | 58.9 | 64.9 | 32.3 | 52.0 | 56.60 |
| Streamo-7B ( [Xia et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib19 "")) | 1 fps | – | 79.2 | 57.8 | 75.0 | 49.4 | 64.4 | 70.1 | 66.0 | 54.6 | 52.0 | 31.7 | 46.1 | 56.05 |
| HERMES-7B†( [Zhang et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib29 "")) | 1 fps | 79.44 | 85.2 | 64.2 | 71.6 | 53.4 | 74.3 | 65.2 | 69.0 | 48.5 | 62.2 | 37.6 | 49.4 | 59.20 |
| SimpleStream (Ours) |
| Qwen2.5-VL-7B + 2f | 2 | 76.39 | 88.6 | 67.0 | 81.0 | 64.6 | 69.3 | 79.3 | 75.0 | 49.2 | 56.8 | 42.5 | 49.5 | 62.22 |
| Qwen2.5-VL-7B + 4f | 4 | 78.47 | 94.0 | 72.5 | 80.2 | 68.0 | 76.2 | 79.3 | 78.4 | 54.5 | 60.8 | 40.3 | 51.9 | 65.13 |
| Qwen2.5-VL-7B + 8f | 8 | 79.11 | 95.3 | 67.9 | 79.3 | 61.2 | 74.3 | 81.5 | 76.6 | 52.2 | 63.5 | 36.6 | 50.8 | 63.70 |
| Qwen3-VL-8B + 2f | 2 | 78.31 | 89.3 | 77.1 | 83.6 | 68.5 | 76.2 | 81.0 | 79.3 | 49.5 | 56.1 | 54.8 | 53.5 | 66.38 |
| Qwen3-VL-8B + 4f | 4 | 80.59 | 94.0 | 85.3 | 82.8 | 65.7 | 77.2 | 83.2 | 81.4 | 51.9 | 58.1 | 52.1 | 54.0 | 67.70 |
| Qwen3-VL-8B + 8f | 8 | 78.83 | 94.0 | 84.4 | 80.2 | 64.0 | 75.3 | 81.5 | 79.9 | 53.2 | 60.8 | 50.5 | 54.9 | 67.37 |

## 4 Experiments

### 4.1 Experimental Setup

#### Benchmarks.

We evaluate all models on OVO-Bench ( [Li et al., 2025b](https://arxiv.org/html/2604.02317v1#bib.bib7 "")) and
StreamingBench ( [Lin et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib8 "")).
OVO-Bench contains 1,640 questions over 12 tasks spanning memory recall,
real-time perception, and future-oriented reasoning. We evaluate the
Backward Tracing and Real-Time Visual Perception categories, which directly test the trade-off between
memory and real-time perception. Under the official evaluation protocol,
each question is answered using only the video prefix available up to the
query time, and we report scores with the official scorer. Offline and
online baselines therefore share the same visible prefix at query time,
while retaining their own model-specific inference pipelines, prompts,
and frame budgets or frame rates as specified in the original papers or
official implementations. For StreamingBench, we use the official
real-time visual understanding subset, which contains 2,500 questions
across ten task types. This setting complements OVO-Bench with broader
real-time coverage and tests whether the same trends transfer across
benchmarks.

#### Compared Models.

We compare against six offline video LLMs ( [Bai et al., 2025b](https://arxiv.org/html/2604.02317v1#bib.bib41 ""); [Li et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib44 ""); [Chen et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib40 ""); [Zhang et al., 2025b](https://arxiv.org/html/2604.02317v1#bib.bib43 ""); [Wang et al., 2024](https://arxiv.org/html/2604.02317v1#bib.bib42 ""); [Shen et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib45 ""))
and seven representative streaming video LLMs ( [Wang et al., 2025e](https://arxiv.org/html/2604.02317v1#bib.bib16 ""); [Zhang et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib28 ""); [Qian et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib11 ""); [Yao et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib25 ""); [Zeng et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib26 ""); [Xia et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib19 ""); [Zhang et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib29 "")),
covering the main design paradigms in recent streaming video understanding; the full model list is reported in Table [1](https://arxiv.org/html/2604.02317v1#S3.T1 "Table 1 ‣ 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"). Unless otherwise noted, we use the best inference settings reported in the original papers or official implementations, and summarize each model’s frame budget or sampling setting in the #Frames column. For special cases, we follow the table notes, e.g., HERMES† denotes the Qwen2.5-VL-7B variant with a 4K-token memory budget.

#### Our SimpleStream.

We instantiate SimpleStream with two open-source VLM backbones,
Qwen2.5-VL-7B-Instruct ( [Bai et al., 2025b](https://arxiv.org/html/2604.02317v1#bib.bib41 "")) and
Qwen3-VL-8B-Instruct ( [Bai et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib47 "")). At each query, we sample the
visible stream at 1 fps and feed the model only the last
N∈{2,4,8}N\\in\\{2,4,8\\} frames. By default, SimpleStream uses no
separate memory bank, retrieval, or vision/KV compression beyond this
recent window.

### 4.2 Benchmark Performance

Table [1](https://arxiv.org/html/2604.02317v1#S3.T1 "Table 1 ‣ 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding") reports our main results on OVO-Bench and
StreamingBench, comparing offline VLMs, online/streaming VLMs, and
SimpleStream under a unified protocol.

On OVO-Bench, the best SimpleStream configuration (Qwen3-VL, 4
frames) reaches 67.7%, exceeding the strongest published streaming method,
HERMES ( [Zhang et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib29 "")), by 8.5 pp (59.2%). The gain is largest on Real-Time Visual
Perception, where SimpleStream achieves 81.4% versus 69.0% for
HERMES, with especially large margins on the OCR, ACR, and OJR tracks. On Backward
Tracing, SimpleStream remains competitive: the 8-frame variant
reaches 54.9%, compared with 52.0% for StreamForest ( [Zeng et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib26 "")) and 49.4% for HERMES. The same pattern appears on StreamingBench. SimpleStream with
Qwen3-VL and 4 frames reaches 80.59%, surpassing HERMES
(79.44%), while five of the six SimpleStream configurations
outperform StreamForest, and all six outperform the remaining streaming
baselines other than HERMES.

Table 2: Model scale effects under a fixed recent-window evaluation
protocol on OVO-Bench.
We vary model scale within each backbone family while keeping all other
evaluation settings unchanged. For each recent window, we report Backward
Tracing accuracy, Real-Time Visual Perception accuracy, and their mean
(“Avg.”). The 7B and 8B rows reuse the corresponding 2-frame, 4-frame, and
8-frame runs from the main experiment under the same protocol. “–”
indicates unavailable or incomplete runs.

|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | 2 Frames | 4 Frames | 8 Frames | 16 Frames |
| Bwd. | Real-Time | Avg. | Bwd. | Real-Time | Avg. | Bwd. | Real-Time | Avg. | Bwd. | Real-Time | Avg. |
| Qwen2.5-VL |
| Qwen2.5-VL-3B | 42.09 | 70.87 | 56.48 | 42.89 | 73.47 | 58.18 | 40.98 | 72.07 | 56.52 | 45.75 | 70.60 | 58.17 |
| Qwen2.5-VL-7B | 49.50 | 75.00 | 62.22 | 51.90 | 78.40 | 65.13 | 50.80 | 76.60 | 63.70 | 48.87 | 74.45 | 61.66 |
| Qwen2.5-VL-32B | 45.87 | 78.80 | 62.33 | 48.64 | 83.03 | 65.84 | 49.43 | 81.70 | 65.56 | 49.97 | 80.69 | 65.33 |
| Qwen2.5-VL-72B | 57.65 | 77.63 | 67.64 | 58.71 | 80.36 | 69.53 | 56.75 | 81.25 | 69.00 | 60.61 | 80.91 | 70.76 |
| Qwen3-VL |
| Qwen3-VL-2B | 43.92 | 73.17 | 58.55 | 45.00 | 76.07 | 60.53 | 45.00 | 75.25 | 60.12 | 47.41 | 73.29 | 60.35 |
| Qwen3-VL-4B | 52.01 | 76.04 | 64.03 | 52.37 | 79.25 | 65.81 | 53.28 | 78.67 | 65.97 | 54.63 | 77.48 | 66.06 |
| Qwen3-VL-8B | 53.50 | 79.30 | 66.38 | 54.00 | 81.40 | 67.70 | 54.90 | 79.90 | 67.37 | 56.41 | 77.88 | 67.15 |
| Qwen3-VL-32B | 63.21 | 81.65 | 72.43 | 63.41 | 83.57 | 73.49 | 65.39 | 82.78 | 74.09 | 66.93 | 80.69 | 73.81 |
| Qwen3-VL-30B-A3B | 58.59 | 82.69 | 70.64 | 61.00 | 85.56 | 73.28 | 61.11 | 84.59 | 72.85 | 64.08 | 81.85 | 72.97 |

|     |     |     |     |
| --- | --- | --- | --- |
| Method | 16 Frames | 64 Frames | 256 Frames |
| Dispider ( [Qian et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib11 "")) | 490 | 1460 | 3810 |
| ReKV ( [Di et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib2 "")) | 250 | 380 | 740 |
| LiveVLM ( [Ning et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib48 "")) | 240 | 310 | 600 |
| StreamForest ( [Zeng et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib26 "")) | 221 | 560 | 834 |
| StreamingTOM ( [Chen et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib49 "")) | 180 | 180 | 280 |
| TimeChat-Online ( [Yao et al., 2025](https://arxiv.org/html/2604.02317v1#bib.bib25 "")) | 156 | 607 | 3072 |
| Flash-VStream ( [Zhang et al., 2025a](https://arxiv.org/html/2604.02317v1#bib.bib28 "")) | 36 | 63 | 67 |
| HERMES ( [Zhang et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib29 "")) | 27 | 29 | 29 |
| Our Method |
| SimpleStream-4f | 35 | 33 | 38 |

Figure 3: Peak GPU memory vs. observed frames.SimpleStream-4f maintains the lowest and flattest memory curve because it retains only a fixed recent frame window.

Table 3: Latency-efficient streaming inference (TTFT).
TTFT (ms) for streaming baselines at 16, 64, and 256 observed frames.
SimpleStream-4f uses a Qwen2.5-VL-7B backbone and remains close to the fastest method.

### 4.3 Model Scale Effects

In the main experiment, increasing the recent window from 4 to 8 frames does
not consistently improve performance, even though the longer window strictly
contains the shorter one. To examine whether this non-monotonic behavior
depends on model scale, we extend the study under the same OVO-Bench protocol
to multiple sizes of Qwen2.5-VL and Qwen3-VL, evaluating SimpleStream
with recent windows N∈{2,4,8,16}N\\in\\{2,4,8,16\\} across all publicly available
Qwen2.5-VL checkpoints up to 72B and all publicly available Qwen3-VL
checkpoints up to 32B, plus an additional Qwen3-VL-30B-A3B checkpoint, while
keeping all other settings fixed.

Table [2](https://arxiv.org/html/2604.02317v1#S4.T2 "Table 2 ‣ 4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding") reports the detailed results. Across both
backbone families, moving from 2 to 4 frames usually improves average
accuracy. For many small and mid-sized checkpoints, performance then plateaus
or slightly declines as the window expands further. Larger windows can become
more favorable for some higher-capacity checkpoints, but the preferred window
size varies across scales and backbone families. Overall, these results show
that model scale affects the optimal recent-window size, without changing the
main conclusion that longer context is not uniformly better.

### 4.4 Efficiency Observations

We also evaluated and compared the efficiency of the models, including time to
first token (TTFT) and peak GPU memory.
Table [3](https://arxiv.org/html/2604.02317v1#S4.T3 "Table 3 ‣ 4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding") shows that SimpleStream-4f remains
latency-competitive despite using no explicit memory module. Across
increasing observed-frame budgets, it achieves lower TTFT than most published
streaming baselines. HERMES ( [Zhang et al., 2026](https://arxiv.org/html/2604.02317v1#bib.bib29 "")) is the only method that is
consistently faster. The remaining gap is modest despite
SimpleStream-4f using no dedicated memory module. This pattern
suggests that low startup latency does not require persistent historical
state. SimpleStream-4f attains the second-lowest TTFT at 16, 64, and
256 observed frames. Figure [3](https://arxiv.org/html/2604.02317v1#S4.F3 "Figure 3 ‣ 4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding") complements the
latency comparison by showing that SimpleStream-4f also has the
lowest peak GPU memory usage. Unlike external-memory streaming systems, its
state size does not accumulate with the observed stream. This behavior follows
directly from the minimalist design in Section [3](https://arxiv.org/html/2604.02317v1#S3 "3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"): the model
preserves only a fixed recent frame window, so memory usage remains nearly
flat as the stream grows.

![[Uncaptioned image]](https://arxiv.org/html/2604.02317v1/figures/window_size_accuracy.png)

|     |     |     |     |
| --- | --- | --- | --- |
| Track | Base | +V-RAG | Δ\\Delta Acc. |
| Backward Tracing |
| EPM (Episodic Memory) | 52.5 | 59.6 | +7.1+7.1 |
| ASI (Action Sequence Identification) | 58.8 | 64.9 | +6.1+6.1 |
| HLD (Hallucination Detection) | 45.7 | 33.3 | −12.4-12.4 |
| Real-Time Visual Perception |
| OJR (Object Recognition) | 81.5 | 72.3 | −9.2-9.2 |
| ATR (Attribute Recognition) | 81.9 | 81.9 | 0.00.0 |
| ACR (Action Recognition) | 78.9 | 71.6 | −7.3-7.3 |
| OCR (Optical Character Recognition) | 94.0 | 85.9 | −8.1-8.1 |
| FPD (Future Prediction) | 77.2 | 74.3 | −2.9-2.9 |
| STU (Spatial Understanding) | 64.0 | 62.4 | −1.6-1.6 |
| Acc. | 66.0 | 63.7 | −2.3-2.3 |

Figure 4: Window-size ablation. Under this controlled setting, SimpleStream reaches its highest Real-Time accuracy with 4 recent frames, while overall accuracy does not improve monotonically as the window widens.

Table 4: Per-track Visual-RAG analysis on OVO-Bench.
Base: matched recent-window baseline; +V-RAG: 5 retrieved chunks appended.
Acc. =(RT+Bwd)/2=(\\mathrm{RT}+\\mathrm{Bwd})/2.

## 5 Analysis

### 5.1 Longer Context Is Not Always Better

A common assumption in streaming video understanding is that giving the model
more past visual evidence should improve answers, because many decisions depend
on continuity across time and earlier observations.
We test that assumption with three complementary probes.
First, we enlarge the recent-frame window fed to the VLM to measure the basic
effect of exposing more contiguous visual context.
Second, we analyze model scaling to test whether the utility of longer visual
context depends on backbone capacity.
Third, we append retrieved historical chunks with Visual-RAG to examine whether
selectively re-injecting distant frames changes the conclusion.
Taken together, these analyses turn a narrow ablation result into a broader
practical question: more context is not free, and whether it helps depends on
whether the backbone can actually absorb and use it.

#### Recency-window ablation.

The simplest way to extend context is to widen the recent-frame window itself.
Holding retrieval, prompting, and decoding otherwise fixed, we vary only the
number of consecutive frames shown to the VLM.
Figure [4](https://arxiv.org/html/2604.02317v1#S4.F4 "Figure 4 ‣ 4.4 Efficiency Observations ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding") reports a controlled ablation over
N∈{2,4,8,16}N\\in\\{2,4,8,16\\} recent frames.
Moving from 2 to 4 frames improves both Overall accuracy (66.4 →\\rightarrow 67.7)
and Real-Time accuracy (79.3 →\\rightarrow 81.4), which indicates that a modestly
wider recent view still supplies useful temporal cues.
Beyond this point, however, performance does not keep rising: at 8 frames,
Overall falls to 67.4 and Real-Time accuracy to 79.9, and at 16 frames they decline further
to 67.1 and 77.9.
Taken together, accuracy is non-monotonic in window size: a modest expansion
helps, but further growth yields flat or declining scores, inconsistent with
the expectation that simply stacking more recent frames should monotonically
improve answers.

\\FloatBarrier

Figure 5: Model-scaling ablation on OVO-Bench.
Average accuracy versus recent-window size for Qwen2.5-VL (left) and
Qwen3-VL (right) checkpoints. Stars mark the best window for each
checkpoint. Many checkpoints peak at 4f, but several prefer longer
windows, including Qwen3-VL-4B at 16f and larger checkpoints at 8f or
16f.

#### Model-scaling ablation.

Table [2](https://arxiv.org/html/2604.02317v1#S4.T2 "Table 2 ‣ 4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding") and
Figure [5](https://arxiv.org/html/2604.02317v1#S5.F5 "Figure 5 ‣ Recency-window ablation. ‣ 5.1 Longer Context Is Not Always Better ‣ 5 Analysis ‣ A Simple Baseline for Streaming Video Understanding") suggest that this trend is better
understood as a model-scale effect than a clean scaling law, since the performance is non-monotonic in window size and varies across checkpoints. Larger models
sometimes benefit more from wider recent windows, but the optimal window does
not increase uniformly with parameter count. One plausible explanation is that whether a model benefits from additional context depends on its capacity to process it. Longer
windows add potentially useful evidence, but they also introduce more
redundancy. Smaller
models therefore saturate earlier, with a short recent window already capturing
most of the usable signal. Larger models can absorb more of this added context,
which explains why 8f or 16f becomes competitive, and occasionally optimal, only for some higher-capacity checkpoints.

Model scale alone, however, does not determine the optimum. For example, Qwen2.5-VL-72B prefers 16 frames, whereas Qwen2.5-VL-32B
peaks at 4 frames; similarly, Qwen3-VL-32B prefers 8 frames, while
Qwen3-VL-30B-A3B peaks at 4 frames. In addition, OVO-Bench does not uniformly reward wider
recent windows, because many questions are still dominated by
present-scene perception. Taken
together, these results suggest that the effective context range is not
a universally increasing function of model scale, but a quantity shaped
by backbone family and by how the benchmark balances present-scene
perception against the use of historical context.

\\FloatBarrier

#### Visual-RAG ablation.

Rather than widening the contiguous window, Visual-RAG ( [Lewis et al., 2020](https://arxiv.org/html/2604.02317v1#bib.bib37 "")) probes the same
“more history helps” premise through targeted retrieval.
A CLIP-based ( [Radford et al., 2021](https://arxiv.org/html/2604.02317v1#bib.bib46 "")) index over historical chunks is built offline; at inference time,
the top-5 most similar past chunks are appended to the recent-frame input
before the VLM generates an answer.
Table [4](https://arxiv.org/html/2604.02317v1#S4.T4 "Table 4 ‣ 4.4 Efficiency Observations ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding") shows that this enrichment is again not uniformly
beneficial. We therefore focus on the within-table deltas between the
matched base and +V-RAG conditions, rather than direct row-by-row
comparison to Table [1](https://arxiv.org/html/2604.02317v1#S3.T1 "Table 1 ‣ 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding").
Visual-RAG improves some Backward tracks, especially EPM (+7.1) and ASI (+6.1),
which confirms that retrieval can recover useful historical evidence, but those
gains coincide with clear degradations on Real-Time tracks, including OJR
(-9.2), OCR (-8.1), and ACR (-7.3), and overall accuracy drops from 66.0 to 63.7.
The outcome is again mixed rather than uniformly positive: selected Backward
tracks rise, yet multiple Real-Time tracks fall and overall accuracy drops, so
richer historical evidence does not translate into reliable aggregate gains
under this setup.

These three probes tell a consistent story.
A slightly longer recent window helps, but gains saturate quickly; beyond that
point, longer context helps only when the backbone has enough capacity to use
it, and even targeted retrieval fails to deliver uniform gains.
Benefits appear task-local, whereas costs often surface on
perception-oriented evaluation slices, which is especially consequential when
aggregate scores overweight Real-Time-style tracks.
This observation motivates the next subsection, where we quantify the trade-off
between historical gains and real-time perception loss.

### 5.2 Perception-Memory Trade-off

The preceding results reveal an asymmetric pattern: adding historical context
often hurts current-scene perception, while its benefits on memory are narrower
and task-dependent. Raw OVO-Bench category averages do not expose this pattern
cleanly because they mix the effect of the streaming mechanism with backbone
strength and input budget. In addition, the Backward split is not a pure memory
measure, since HLD primarily reflects hallucination robustness rather than
episodic event recall. We therefore separate the two sides of the trade-off.

For any streaming method, we measure the change in real-time perception as

|     |     |     |     |
| --- | --- | --- | --- |
|  | Δ​P=RTmethod−RTSimpleStream\\Delta P=\\mathrm{RT}\_{\\text{method}}-\\mathrm{RT}\_{\\textsc{SimpleStream}} |  | (1) |

where RT\\mathrm{RT} is the OVO-Bench Real-Time category average. To quantify the
memory side, we define _Memory Gain_ as the change in the mean of EPM and
ASI, the two Backward tracks most directly tied to recalling previously
observed events:

|     |     |     |     |
| --- | --- | --- | --- |
|  | Δ​M=ERmethod−ERSimpleStream\\Delta M=\\mathrm{ER}\_{\\text{method}}-\\mathrm{ER}\_{\\textsc{SimpleStream}} |  | (2) |

where ER=(EPM+ASI)/2\\mathrm{ER}=(\\mathrm{EPM}+\\mathrm{ASI})/2.
These two quantities make the trade-off explicit: Δ​M>0\\Delta M>0 indicates
memory gain, while Δ​P<0\\Delta P<0 indicates a perception cost. For
descriptive cross-method visualization, Figure [6](https://arxiv.org/html/2604.02317v1#S6.F6 "Figure 6 ‣ 6 Why Does a Simple Baseline Win? ‣ A Simple Baseline for Streaming Video Understanding")
uses the SimpleStream Qwen2.5-VL + 2f configuration as a common
reference under the unified protocol.

Figure [6](https://arxiv.org/html/2604.02317v1#S6.F6 "Figure 6 ‣ 6 Why Does a Simple Baseline Win? ‣ A Simple Baseline for Streaming Video Understanding") shows that the dominant pattern is still
perception loss: every evaluated external baseline falls below SimpleStream
on Δ​P\\Delta P. This holds across memory-bank methods, retrieval-based
augmentation, and offline long-context baselines, suggesting that the
perception cost is broad rather than architecture-specific. In contrast,
positive memory gain becomes common once memory is measured on EPM and ASI.
Among published streaming systems, StreamForest shows the clearest
memory-side gain (Δ​M=+8.9\\Delta M=+8.9), but it pays a much larger perception
penalty (Δ​P=−13.8\\Delta P=-13.8). HERMES also gains on memory
(Δ​M=+2.4\\Delta M=+2.4), yet still incurs a substantial perception cost
(Δ​P=−6.0\\Delta P=-6.0).

Our controlled Visual-RAG ablation shows the same asymmetry even more directly.
Retrieving historical chunks improves EPM and ASI by 6.6 points on average,
but reduces real-time perception by 4.9 points relative to the matched recent
window. Taken together, these results support a perception-memory trade-off
under a cleaner definition of memory: current mechanisms can improve
memory-oriented behavior, but these gains are typically purchased with a
broader and more consistent loss in present-scene perception. The central
challenge is therefore not simply to preserve more history, but to recover
useful past evidence without corrupting the model’s perception of the present.

### 5.3 Benchmark Limitations

#### HLD is not a memory task.

We argue that HLD is conceptually misaligned with long-term memory evaluation.
Hallucination detection primarily measures whether the model resists misleading
prompts, unsupported claims, or semantically inconsistent options. This ability
is related to robustness and grounded verification, but it is not equivalent to
recalling previously observed events from a long video stream. A model can fail
HLD without forgetting the past, just as it can succeed on HLD without
demonstrating strong episodic memory. Placing HLD under Backward Tracing
therefore conflates two distinct abilities: memory recall and hallucination
robustness. In our Visual-RAG study, for example, HLD drops by 12.4 points even
when memory-oriented tracks such as EPM and ASI improve. We therefore caution
against interpreting HLD as a direct measure of long-range memory.

#### Macro-average favors perception-heavy gains.

OVO-Bench reports a macro-average over 12 tracks, but these tracks are not
balanced across capability types. Real-Time Visual Perception occupies 6 tracks,
Backward Tracing occupies 3, and Forward Active Responding occupies 3. As a
result, equal weighting at the track level does not produce balanced weighting
at the capability level. Aggregate scores are therefore more sensitive to
changes on perception-oriented tracks than to comparable changes on
memory-oriented ones. This matters when evaluating streaming methods that trade
stronger access to history for weaker present-scene perception, because even
modest degradation on Real-Time tracks can dominate the final score. We
therefore interpret the macro-average together with per-track results rather
than treating it as a neutral summary of overall streaming ability.

\\FloatBarrier

## 6 Why Does a Simple Baseline Win?

Figure 6: Perception cost (Δ​P\\Delta P) and Memory Gain
(Δ​M\\Delta M) relative to the SimpleStream Qwen2.5-VL + 2f
configuration. Green bars show changes in OVO-Bench Real-Time average. Blue bars
show changes on the mean of EPM and ASI. Relative to this short-window
reference, many methods improve memory, but external baselines still
incur a substantial perception cost.

#### Recent context matters most.

Our results suggest that the main strength of current streaming VLMs does not
come from increasingly elaborate memory mechanisms, but from their already
strong short-horizon perception. Modern VLM backbones can read text, recognize
objects, track local actions, and answer query-conditioned questions well when
the recent visual evidence remains clear. In this regime, preserving an
undiluted view of the latest frames is often more valuable than injecting
additional historical summaries whose relevance is uncertain. Model scale does
affect how much recent context a backbone can use effectively: stronger models
can sometimes benefit from somewhat wider recent windows. But this is still a
recent-context effect rather than evidence that complex memory is necessary.
This perspective helps explain why SimpleStream is competitive: it
protects the signal that current backbones use best, namely dense and reliable
recent visual evidence.

#### Complex memory can hurt present perception.

The converse is equally important: memory is not free. Compression, retrieval
noise, abstract latent states, or large memory injection can all interfere with
the model’s understanding of the current scene, even when they are intended to
help long-range reasoning. In other words, adding more history can reduce the
effective clarity of the present input. One plausible mechanism is attention
dilution: when too much retrieved or summarized context is injected, the model
may allocate capacity away from the most relevant recent evidence. We do not
claim this mechanism as an established empirical fact here, but it offers a
useful hypothesis for why stronger memory modules can still degrade real-time
perception.
This does not argue against memory-centric designs in principle;
rather, it argues for evaluation that reveals when they improve
recall-oriented behavior without imposing unacceptable costs on
present-scene perception.

#### Benchmark design further amplifies this advantage.

This advantage is also partly structural. Current benchmarks do not purely
measure long-term memory; instead, their aggregate scores still place heavy
weight on recent perception. As a result, methods that preserve clear recent visual evidence can gain twice: they align with the strongest capability of today’s
backbones, and they are rewarded by evaluation protocols that overweight that
capability in the final score. From this perspective, SimpleStream
wins not only because it is strong, but also because the benchmark favors the
kind of strength it preserves. This does not invalidate the result, but it does
change its interpretation: benchmark leadership is not the same thing as
solving long-horizon memory.

#### Implications for future research.

These observations suggest two concrete directions. For future _models_, a
promising principle is _recent-first, history-on-demand_: preserve the
recent context by default, and access historical memory only when the current
evidence is insufficient. More broadly, memory modules should be evaluated not
only by recall gains, but also by whether they damage real-time perception. For
future _benchmarks_, evaluation should explicitly separate perception,
memory recall, and hallucination robustness rather than collapsing them into a
single macro-average. More transparent reporting of the
accuracy-efficiency trade-off would make it easier to distinguish genuinely
better long-context reasoning from methods that simply preserve the benchmark’s
most rewarded capability.

## 7 Conclusion

We show that SimpleStream, a simple baseline, is already strong enough to exceed
recently published complex-memory streaming systems on both OVO-Bench and
StreamingBench while remaining latency-competitive.
Our results show that additional memory, retrieval, or compression
should be justified by clear gains over SimpleStream on the
relevant capability slices.
Our analyses show why this baseline is so competitive. Current memory
injection techniques often improve recall-oriented cases at the cost of
current-scene perception, producing a consistent perception-memory
trade-off that we quantify with real-time perception change (Δ​P\\Delta P).
Moreover, performance often saturates with a small recent window.
Although some higher-capacity backbones benefit from longer recent
context, the optimal window does not grow monotonically with model
scale, reinforcing that more history is not always better and that
current benchmarks may not faithfully reward long-term memory as
intended.
We therefore recommend that future work report strong simple baselines,
disaggregated perception-versus-memory metrics, and transparent
efficiency statistics before claiming progress.
The central open problem is not how to add more memory, but how to use
history without degrading current-scene understanding.

## 8 Limitations

#### Dependence on strong backbone families.

SimpleStream is evaluated on top of strong modern VLM backbones,
specifically Qwen2.5-VL and Qwen3-VL. As a result, our conclusions are coupled
to the capabilities of this backbone family: strong recent-context performance
may partly reflect the fact that these models already provide robust short-range
perception, OCR, and query-conditioned reasoning. We therefore do not claim
that the same degree of competitiveness will automatically transfer to broader
model families with different pretraining data, visual encoders, or temporal
reasoning characteristics. Extending the comparison to a wider range of
backbones is an important direction for future work.

#### Scope as a strong-baseline paper.

This paper is deliberately positioned as a _strong baseline_ study rather
than a proposal of a new streaming video understanding architecture. Our main
contributions are to establish SimpleStream as a strong baseline,
clarify how results on memory-heavy benchmarks should be interpreted, and analyze the
accuracy-efficiency and perception-memory trade-offs. Accordingly,
SimpleStream does not introduce a new memory-centric architecture, a
new long-term memory mechanism, or a new retrieval/compression design. The
paper therefore should not be read as solving long-horizon video understanding;
rather, it clarifies what current benchmarks already reward and what future
memory-centric methods must surpass under stronger controls.

## References

- Azad et al. (2026)S. Azad, V. Vineet, and Y. S. RawatStreamReady: Learning What to Answer and When in Long Streaming Videos.
arXiv preprint arXiv:2603.08620.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2603.08620 ""),
2603.08620Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p1.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Bai et al. (2025a)S. Bai, Y. Cai, R. Chen, K. Chen, X. Chen, Z. Cheng, L. Deng, W. Ding, C. Gao, C. Ge, W. Ge, Z. Guo, Q. Huang, J. Huang, F. Huang, B. Hui, S. Jiang, Z. Li, M. Li, M. Li, K. Li, Z. Lin, J. Lin, X. Liu, J. Liu, C. Liu, Y. Liu, D. Liu, S. Liu, D. Lu, R. Luo, C. Lv, R. Men, L. Meng, X. Ren, X. Ren, S. Song, Y. Sun, J. Tang, J. Tu, J. Wan, P. Wang, P. Wang, Q. Wang, Y. Wang, T. Xie, Y. Xu, H. Xu, J. Xu, Z. Yang, M. Yang, J. Yang, A. Yang, B. Yu, F. Zhang, H. Zhang, X. Zhang, B. Zheng, H. Zhong, J. Zhou, F. Zhou, J. Zhou, Y. Zhu, and K. ZhuQwen3-VL technical report.
arXiv preprint arXiv:2511.21631.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2511.21631 ""),
2511.21631Cited by: [§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px3.p1.1 "Our SimpleStream. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Bai et al. (2025b)S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, et al.Qwen2.5-VL technical report.
arXiv preprint arXiv:2502.13923.
External Links: 2502.13923Cited by: [Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.6.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px3.p1.1 "Our SimpleStream. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Chen et al. (2025)J. Chen, Z. Zeng, Y. Lin, W. Li, Z. Ma, and M. Z. ShouLiveCC: Learning Video LLM with Streaming Speech Transcription at Scale.
In CVPR,
External Links: 2504.16030Cited by: [§1](https://arxiv.org/html/2604.02317v1#S1.p1.1 "1 Introduction ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p1.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Chen et al. (2026)X. Chen, K. Tao, K. Shao, and H. WangStreamingTOM: Streaming Token Compression for Efficient Video Understanding.
In CVPR,
Note: To appearExternal Links: 2510.18269Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.2](https://arxiv.org/html/2604.02317v1#S4.SS2.fig1.2.1.6.1 "4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Chen et al. (2024)Z. Chen, W. Wang, H. Tian, S. Ye, Z. Gao, E. Cui, W. Tong, K. Hu, J. Luo, Z. Ma, J. Ma, J. Wang, X. Dong, H. Yan, H. Guo, C. He, B. Shi, Z. Jin, C. Xu, B. Wang, X. Wei, W. Li, W. Zhang, B. Zhang, P. Cai, L. Wen, X. Yan, M. Dou, L. Lu, X. Zhu, T. Lu, D. Lin, Y. Qiao, J. Dai, and W. WangHow far are we to GPT-4V? closing the gap to commercial multimodal models with open-source suites.
arXiv preprint arXiv:2404.16821.
External Links: 2404.16821Cited by: [Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.8.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Di et al. (2025)S. Di, Z. Yu, G. Zhang, H. Li, T. Zhong, H. Cheng, B. Li, W. He, F. Shu, and H. JiangStreaming Video Question-Answering with In-context Video KV-Cache Retrieval.
In ICLR,
External Links: 2503.00540Cited by: [§1](https://arxiv.org/html/2604.02317v1#S1.p1.1 "1 Introduction ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§3.1](https://arxiv.org/html/2604.02317v1#S3.SS1.p2.1 "3.1 A Landscape of Streaming Video Understanding Methods ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.2](https://arxiv.org/html/2604.02317v1#S4.SS2.fig1.2.1.3.1 "4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Fu et al. (2025)C. Fu, Y. Dai, Y. Luo, L. Li, S. Ren, R. Zhang, Z. Wang, C. Zhou, Y. Shen, M. Zhang, P. Chen, Y. Li, S. Lin, S. Zhao, K. Li, T. Xu, X. Zheng, E. Chen, C. Shan, R. He, and X. SunVideo-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis.
In CVPR,
External Links: 2405.21075Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Guo et al. (2026)Z. Guo, Y. Man, J. Sheng, B. Lin, A. Ahmed, B. Jiang, B. Zhang, M. Yin, S. Jin, O. Gnawal, and C. ZhangEvent-VStream: Event-Driven Real-Time Understanding for Long Video Streams.
arXiv preprint arXiv:2601.15655.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2601.15655 ""),
2601.15655Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Huang et al. (2025)Z. Huang, X. Li, J. Li, J. Wang, X. Zeng, C. Liang, T. Wu, X. Chen, L. Li, and L. WangOnline Video Understanding: OVBench and VideoChat-Online.
In CVPR,
External Links: 2501.00584Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Jin et al. (2025)X. Jin, H. Yu, B. Yu, K. Liu, J. Liu, K. Tao, Y. Pei, H. Wang, F. Dang, J. Liu, and W. WangStreamingAssistant: Efficient Visual Token Pruning for Accelerating Online Video Understanding.
arXiv preprint arXiv:2512.12560.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2512.12560 ""),
2512.12560Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Lewis et al. (2020)P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rocktäschel, S. Riedel, and D. KielaRetrieval-augmented generation for knowledge-intensive NLP tasks.
In NeurIPS,
External Links: 2005.11401,
[Document](https://dx.doi.org/10.48550/arXiv.2005.11401 "")Cited by: [§5.1](https://arxiv.org/html/2604.02317v1#S5.SS1.SSS0.Px3.p1.1 "Visual-RAG ablation. ‣ 5.1 Longer Context Is Not Always Better ‣ 5 Analysis ‣ A Simple Baseline for Streaming Video Understanding").

- Li et al. (2025a)B. Li, Y. Zhang, D. Guo, R. Zhang, F. Li, H. Zhang, K. Zhang, Y. Li, Z. Liu, and C. LiLLaVA-OneVision: easy visual task transfer.
TMLR.
External Links: 2408.03326Cited by: [Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.7.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Li et al. (2024)K. Li, Y. Wang, Y. He, Y. Li, Y. Wang, Y. Liu, Z. Wang, J. Xu, G. Chen, P. Luo, L. Wang, and Y. QiaoMVBench: A Comprehensive Multi-modal Video Understanding Benchmark.
In CVPR,
External Links: 2311.17005Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Li et al. (2025b)Y. Li, J. Niu, Z. Miao, C. Ge, Y. Zhou, Q. He, X. Dong, H. Duan, S. Ding, R. Qian, P. Zhang, Y. Zang, Y. Cao, C. He, and J. WangOVO-Bench: How Far is Your Video-LLMs from Real-World Online Video Understanding?.
In CVPR,
External Links: 2501.05510Cited by: [§1](https://arxiv.org/html/2604.02317v1#S1.p4.1 "1 Introduction ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.3 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.6 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px1.p1.1 "Benchmarks. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Lin et al. (2024)J. Lin, Z. Fang, C. Chen, Z. Wan, F. Luo, P. Li, Y. Liu, and M. SunStreamingBench: Assessing the Gap for MLLMs to Achieve Streaming Video Understanding.
arXiv preprint arXiv:2411.03628.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2411.03628 ""),
2411.03628Cited by: [§1](https://arxiv.org/html/2604.02317v1#S1.p4.1 "1 Introduction ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.3 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.6 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px1.p1.1 "Benchmarks. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Liu et al. (2026a)P. Liu, Z. Shi, H. Hao, Q. Fu, X. Bi, S. Zhang, X. Hu, Z. Wang, L. Huang, and S. LiuVCBench: A Streaming Counting Benchmark for Spatial-Temporal State Maintenance in Long Videos.
arXiv preprint arXiv:2603.12703.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2603.12703 ""),
2603.12703Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Liu et al. (2026b)Z. Liu, L. Guo, H. Li, R. Zhen, X. He, R. Ji, X. Ren, Y. Zhang, H. Lu, and J. LiuThinking in Streaming Video.
arXiv preprint arXiv:2603.12938.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2603.12938 ""),
2603.12938Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p1.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Lu et al. (2026)X. Lu, H. Guan, Y. Bo, J. Chen, X. Guo, S. Li, F. Liu, P. Sun, X. Li, W. Zhang, X. Yang, R. Liu, and H. LiPhoStream: Benchmarking Real-World Streaming for Omnimodal Assistants in Mobile Scenarios.
arXiv preprint arXiv:2601.22575.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2601.22575 ""),
2601.22575Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Mangalam et al. (2023)K. Mangalam, R. Akshulakov, and J. MalikEgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding.
In NeurIPS,
External Links: 2308.09126Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Ning et al. (2025)Z. Ning, G. Liu, Q. Jin, W. Ding, M. Guo, and J. ZhaoLiveVLM: Efficient Online Video Understanding via Streaming-Oriented KV Cache and Retrieval.
arXiv preprint arXiv:2505.15269.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2505.15269 ""),
2505.15269Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.2](https://arxiv.org/html/2604.02317v1#S4.SS2.fig1.2.1.4.1 "4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Qian et al. (2025)R. Qian, S. Ding, X. Dong, P. Zhang, Y. Zang, Y. Cao, D. Lin, and J. WangDispider: Enabling Video LLMs with Active Real-Time Interaction via Disentangled Perception, Decision, and Reaction.
In CVPR,
External Links: 2501.03218Cited by: [§1](https://arxiv.org/html/2604.02317v1#S1.p1.1 "1 Introduction ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p1.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§3.1](https://arxiv.org/html/2604.02317v1#S3.SS1.p2.1 "3.1 A Landscape of Streaming Video Understanding Methods ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.15.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.2](https://arxiv.org/html/2604.02317v1#S4.SS2.fig1.2.1.2.1 "4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Qian et al. (2024)R. Qian, X. Dong, P. Zhang, Y. Zang, S. Ding, D. Lin, and J. WangStreaming Long Video Understanding with Large Language Models.
In NeurIPS,
External Links: 2405.16009Cited by: [§1](https://arxiv.org/html/2604.02317v1#S1.p1.1 "1 Introduction ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§3.1](https://arxiv.org/html/2604.02317v1#S3.SS1.p2.1 "3.1 A Landscape of Streaming Video Understanding Methods ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding").

- Radford et al. (2021)A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, G. Krueger, and I. SutskeverLearning transferable visual models from natural language supervision.
In International conference on machine learning,
pp. 8748–8763.
Cited by: [§5.1](https://arxiv.org/html/2604.02317v1#S5.SS1.SSS0.Px3.p1.1 "Visual-RAG ablation. ‣ 5.1 Longer Context Is Not Always Better ‣ 5 Analysis ‣ A Simple Baseline for Streaming Video Understanding").

- Shen et al. (2025)X. Shen, Y. Xiong, C. Zhao, L. Wu, J. Chen, C. Zhu, Z. Liu, F. Xiao, B. Varadarajan, F. Borber, et al.LongVU: spatiotemporal adaptive compression for long video-language understanding.
In ICML,
External Links: 2410.17434Cited by: [Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.11.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Shi et al. (2026)Y. Shi, Q. Zhao, T. Jiang, X. Zeng, Y. Wang, and L. WangRIVER: A Real-Time Interaction Benchmark for Video LLMs.
arXiv preprint arXiv:2603.03985.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2603.03985 ""),
2603.03985Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Wang et al. (2025a)H. Wang, B. Feng, Z. Lai, M. Xu, S. Li, W. Ge, A. Dehghan, M. Cao, and P. HuangStreamBridge: Turning Your Offline Video Large Language Model into a Proactive Streaming Assistant.
In NeurIPS,
External Links: 2505.05467Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p1.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Wang et al. (2024)P. Wang, S. Bai, S. Tan, S. Wang, Z. Fan, J. Bai, K. Chen, X. Liu, J. Wang, W. Ge, et al.Qwen2-VL: enhancing vision-language model’s perception of the world at any resolution.
arXiv preprint arXiv:2409.12191.
External Links: 2409.12191Cited by: [Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.10.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Wang et al. (2025b)W. Wang, Z. He, W. Hong, Y. Cheng, X. Zhang, J. Qi, X. Gu, S. Huang, B. Xu, Y. Dong, M. Ding, and J. TangLVBench: An Extreme Long Video Understanding Benchmark.
In ICCV,
External Links: 2406.08035Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Wang et al. (2026)X. Wang, L. Huang, Z. Wu, X. Zhao, T. Xu, X. Xia, and P. PengLiViBench: an Omnimodal Benchmark for Interactive Livestream Video Understanding.
arXiv preprint arXiv:2601.15016.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2601.15016 ""),
2601.15016Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Wang et al. (2025c)Y. Wang, X. Liu, X. Gui, X. Lin, B. Yang, C. Liao, T. Chen, and L. ZhangAccelerating streaming video large language models via hierarchical token compression.
arXiv preprint arXiv:2512.00891.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2512.00891 ""),
2512.00891Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Wang et al. (2025d)Y. Wang, X. Meng, Y. Wang, H. Zhang, and D. ZhaoProactiveVideoQA: A Comprehensive Benchmark Evaluating Proactive Interactions in Video Large Language Models.
arXiv preprint arXiv:2507.09313.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2507.09313 ""),
2507.09313Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Wang et al. (2025e)Y. Wang, X. Meng, Y. Wang, J. Liang, J. Wei, H. Zhang, and D. ZhaoVideoLLM Knows When to Speak: Enhancing Time-Sensitive Video Comprehension with Video-Text Duet Interaction Format.
In Findings of EMNLP,
External Links: 2411.17991Cited by: [Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.13.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Wang et al. (2025f)Y. Wang, Y. Wang, B. Chen, T. Wu, D. Zhao, and Z. ZhengOmniMMI: A Comprehensive Multi-modal Interaction Benchmark in Streaming Video Contexts.
In CVPR,
External Links: 2503.22952Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Xia et al. (2025)J. Xia, P. Chen, M. Zhang, X. Sun, and K. ZhouStreaming Video Instruction Tuning.
arXiv preprint arXiv:2512.21334.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2512.21334 ""),
2512.21334Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p1.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.18.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Xie et al. (2026)Y. Xie, B. He, J. Wang, X. Zheng, Z. Ye, and Z. WuFluxMem: Adaptive Hierarchical Memory for Streaming Video Understanding.
arXiv preprint arXiv:2603.02096.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2603.02096 ""),
2603.02096Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Xiong et al. (2025)H. Xiong, Z. Yang, J. Yu, Y. Zhuge, L. Zhang, J. Zhu, and H. LuStreaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge.
In ICLR,
External Links: 2501.13468Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Xu et al. (2026)R. Xu, G. Xiao, Y. Chen, L. He, K. Peng, Y. Lu, and S. HanStreamingVLM: Real-Time Understanding for Infinite Video Streams.
In ICLR,
External Links: 2510.09608Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Yang et al. (2025a)J. Yang, S. Liu, H. Guo, Y. Dong, X. Zhang, S. Zhang, P. Wang, Z. Zhou, B. Xie, Z. Wang, B. Ouyang, Z. Lin, M. Cominelli, Z. Cai, Y. Zhang, P. Zhang, F. Hong, J. Widmer, F. Gringoli, L. Yang, B. Li, and Z. LiuEgoLife: towards egocentric life assistant.
In CVPR,
External Links: 2503.03803,
[Document](https://dx.doi.org/10.48550/arXiv.2503.03803 "")Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Yang et al. (2025b)Y. Yang, Z. Zhao, S. N. Shukla, A. Singh, S. K. Mishra, L. Zhang, and M. RenStreamMem: Query-Agnostic KV Cache Memory for Streaming Video Understanding.
arXiv preprint arXiv:2508.15717.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2508.15717 ""),
2508.15717Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Yang et al. (2025c)Z. Yang, K. Zhang, Y. Hu, B. Wang, S. Qian, B. Wen, F. Yang, T. Gao, W. Dong, and C. XuLiveStar: Live Streaming Assistant for Real-World Online Video Understanding.
In NeurIPS,
External Links: 2511.05299Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p1.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Yao et al. (2025)L. Yao, Y. Li, Y. Wei, L. Li, S. Ren, Y. Liu, K. Ouyang, L. Wang, S. Li, S. Li, L. Kong, Q. Liu, Y. Zhang, and X. SunTimeChat-Online: 80% Visual Tokens are Naturally Redundant in Streaming Videos.
In ACM MM,
External Links: 2504.17343Cited by: [§1](https://arxiv.org/html/2604.02317v1#S1.p1.1 "1 Introduction ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.16.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.2](https://arxiv.org/html/2604.02317v1#S4.SS2.fig1.2.1.7.1 "4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Zeng et al. (2025)X. Zeng, K. Qiu, Q. Zhang, X. Li, J. Wang, J. Li, Z. Yan, K. Tian, M. Tian, X. Zhao, Y. Wang, and L. WangStreamForest: Efficient Online Video Understanding with Persistent Event Memory.
arXiv preprint arXiv:2509.24871.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2509.24871 ""),
2509.24871Cited by: [§1](https://arxiv.org/html/2604.02317v1#S1.p1.1 "1 Introduction ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§3.1](https://arxiv.org/html/2604.02317v1#S3.SS1.p2.1 "3.1 A Landscape of Streaming Video Understanding Methods ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.17.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.2](https://arxiv.org/html/2604.02317v1#S4.SS2.fig1.2.1.5.1 "4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.2](https://arxiv.org/html/2604.02317v1#S4.SS2.p2.1 "4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Zhang et al. (2025a)H. Zhang, Y. Wang, Y. Tang, Y. Liu, J. Feng, and X. JinFlash-VStream: Efficient Real-Time Understanding for Long Video Streams.
In ICCV,
External Links: 2506.23825Cited by: [§1](https://arxiv.org/html/2604.02317v1#S1.p1.1 "1 Introduction ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§3.1](https://arxiv.org/html/2604.02317v1#S3.SS1.p2.1 "3.1 A Landscape of Streaming Video Understanding Methods ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.14.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.2](https://arxiv.org/html/2604.02317v1#S4.SS2.fig1.2.1.8.1 "4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Zhang et al. (2026)H. Zhang, S. Yang, J. Fu, S. Ng, and X. QiuHERMES: KV Cache as Hierarchical Memory for Efficient Streaming Video Understanding.
arXiv preprint arXiv:2601.14724.
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2601.14724 ""),
2601.14724Cited by: [§1](https://arxiv.org/html/2604.02317v1#S1.p1.1 "1 Introduction ‣ A Simple Baseline for Streaming Video Understanding"),
[§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding"),
[§3.1](https://arxiv.org/html/2604.02317v1#S3.SS1.p2.1 "3.1 A Landscape of Streaming Video Understanding Methods ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.19.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.2](https://arxiv.org/html/2604.02317v1#S4.SS2.fig1.2.1.9.1 "4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.2](https://arxiv.org/html/2604.02317v1#S4.SS2.p2.1 "4.2 Benchmark Performance ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.4](https://arxiv.org/html/2604.02317v1#S4.SS4.p1.1 "4.4 Efficiency Observations ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Zhang et al. (2025b)Y. Zhang, B. Li, h. Liu, Y. J. Lee, L. Gui, D. Fu, J. Feng, Z. Liu, and C. LiVideo instruction tuning with synthetic data.
TMLR.
External Links: 2410.02713Cited by: [Table 1](https://arxiv.org/html/2604.02317v1#S3.T1.7.1.9.1 "In 3.2 SimpleStream: A Simple Recent-N-Frames Baseline ‣ 3 From Complex Streaming Methods to SimpleStream ‣ A Simple Baseline for Streaming Video Understanding"),
[§4.1](https://arxiv.org/html/2604.02317v1#S4.SS1.SSS0.Px2.p1.1 "Compared Models. ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ A Simple Baseline for Streaming Video Understanding").

- Zhang et al. (2025c)Y. Zhang, C. Shi, Y. Wang, and S. YangEyes Wide Open: Ego Proactive Video-LLM for Streaming Video.
In NeurIPS,
External Links: [Document](https://dx.doi.org/10.48550/arXiv.2510.14560 ""),
2510.14560Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Zhou et al. (2025)J. Zhou, Y. Shu, B. Zhao, B. Wu, Z. Liang, S. Xiao, M. Qin, X. Yang, Y. Xiong, B. Zhang, T. Huang, and Z. LiuMLVU: Benchmarking Multi-task Long Video Understanding.
In CVPR,
External Links: 2406.04264Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p3.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").

- Zhou et al. (2024)X. Zhou, A. Arnab, S. Buch, S. Yan, A. Myers, X. Xiong, A. Nagrani, and C. SchmidStreaming Dense Video Captioning.
In CVPR,
External Links: 2404.01297Cited by: [§2](https://arxiv.org/html/2604.02317v1#S2.p2.1 "2 Related Work ‣ A Simple Baseline for Streaming Video Understanding").