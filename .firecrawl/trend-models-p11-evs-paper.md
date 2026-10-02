[Abstract](https://www.alphaxiv.org/abs/2510.14624) [Paper](https://www.alphaxiv.org/pdf/2510.14624)

## Abstract

Vision-language models (VLMs) have recently expanded from static image understanding to video reasoning, but their scalability is fundamentally limited by the quadratic cost of processing dense frame sequences. Long videos often exceed the token budget of modern language models, leading to severe context limitations and latency issues. We introduce Efficient Video Sampling (EVS), a simple, plug-and-play method for reducing token redundancy in videos by identifying and pruning temporally static patches -- spatial regions that remain unchanged across consecutive frames. EVS preserves positional identity, requires no architectural changes or retraining. We show that EVS substantially reduces token count while maintaining semantic fidelity, enabling faster inference and longer input sequences. Applied at inference time, EVS reduces large language model (LLM) time-to-first-token (TTFT) by up to 4x with minimal accuracy loss. When combined with an uptraining phase using stochastic pruning rates, EVS yields models that are robust to varying compression levels and retain full performance under aggressive pruning. Extensive experiments demonstrate that EVS consistently improves efficiency-accuracy trade-offs, unlocking scalable video-language understanding without sacrificing quality.

View more

[View Paper](https://www.alphaxiv.org/pdf/2510.14624)

16

Save

[Comments](https://www.alphaxiv.org/abs/2510.14624#discussion)

Cite

## AI Overview

Copy

Our new overview generator adds more detail and page citations

Generate overview

## Introduction

![Efficient Video Sampling visualization showing original video frames, patches identified as temporally static (white areas), and resulting sparse token retention across consecutive frames](https://paper-assets.alphaxiv.org/figures/2510.14624v1/img-0.jpeg)

Vision-Language Models (VLMs) have made remarkable progress in understanding static images, but scaling these models to process video data presents significant computational challenges. Videos generate enormous numbers of visual tokens - a typical two-minute video can produce over two million vision tokens, far exceeding the context length limitations of most Large Language Models. This token explosion creates a scalability bottleneck that severely limits the ability of VLMs to process long-form video content.

Researchers from NVIDIA have developed Efficient Video Sampling (EVS), a training-free method that addresses this fundamental challenge by intelligently pruning temporally redundant tokens. EVS operates on a simple yet effective principle: real-world videos contain substantial temporal redundancy, with many patches remaining static across consecutive frames. By identifying and aggregating these temporally static regions, EVS can dramatically reduce the computational burden while preserving the essential dynamic content needed for video understanding.

## Problem Statement and Current Limitations

The core challenge in video VLM inference stems from the quadratic computational complexity of transformer architectures. When processing video sequences, the number of visual tokens grows linearly with video length, but the computational cost of the attention mechanism scales quadratically. This creates several critical limitations:

**Token Budget Constraints**: Modern LLMs typically support context windows of 4K to 128K tokens. A video sampled at standard frame rates quickly exhausts these limits, forcing practitioners to either process very short clips or use extremely sparse temporal sampling that loses important temporal information.

**Inference Latency**: High token counts directly translate to increased Time-To-First-Token (TTFT), making real-time video understanding applications impractical. The memory requirements for storing Key-Value (KV) cache states also grow linearly with sequence length, further constraining deployment scenarios.

**Computational Inefficiency**: Processing every pixel and patch across all frames treats dynamic and static regions equally, wasting computational resources on redundant information that doesn't contribute to understanding.

Existing approaches to this problem fall into several categories, each with distinct limitations. Learned keyframe selection methods like LongVU and VilaMP require additional training and architectural modifications. Spatial token merging approaches like Token Merging (ToMe) focus on within-frame redundancy but don't exploit temporal patterns. Text-guided sparsification methods require access to attention maps and add computational overhead.

## Core Methodology

EVS distinguishes itself through its simplicity and plug-and-play compatibility. The method can operate in two spaces: RGB pixel space for low-latency applications, or embedding space for potentially better accuracy.

**RGB Space Operation**: The algorithm divides each frame into non-overlapping square patches of a defined size. For every patch at time ttt, it computes the L1 norm difference against the corresponding patch in the previous frame:

Dp,t=∣∣pt−pt−1∣∣1D\_{p,t} = \|\|p\_t - p\_{t-1}\|\|\_1Dp,t​=∣∣pt​−pt−1​∣∣1​

A sequence-level threshold ddd is determined as the qqq-th percentile of all patch differences across frames, where qqq represents the desired pruning rate. Patches in the first frame are always retained to provide temporal anchoring. For subsequent frames, only patches where Dp,t≥dD\_{p,t} \\geq dDp,t​≥d are kept, creating a binary retention mask.

**Embedding Space Operation**: Alternatively, frames can first pass through the vision encoder to generate feature embeddings. The algorithm then computes frame-wise cosine dissimilarity along the feature dimension for patches in consecutive frames. The same percentile-based thresholding approach determines which embeddings to retain.

**Position-Preserving Encoding**: A critical design choice in EVS is maintaining the original positional encodings for retained tokens. Rather than re-indexing positions sequentially after pruning, EVS preserves the sparse positional indices from the original dense sequence. This allows the LLM backbone to interpret the pruned input as if it were a naturally sparse sampling, maintaining spatial-temporal relationships that are crucial for video understanding.

The method requires no architectural changes and adds minimal computational overhead - primarily two efficient `gather` operations during token selection.

## Training and Optimization

While EVS works effectively as a plug-and-play solution, the authors introduce an optional "uptraining" phase that significantly enhances performance and robustness.

**Stochastic Pruning During Training**: Instead of using a fixed pruning rate during fine-tuning, EVS samples the pruning rate qqq from a Beta distribution for each mini-batch. This exposes the model to a continuum of compression ratios, teaching it to maintain performance across varying levels of sparsity.

**Robustness Benefits**: This stochastic approach produces models that can dynamically adapt to different pruning rates at inference time without requiring separate checkpoints. The model learns to be invariant to the specific level of temporal sparsity, making it suitable for deployment scenarios where computational budgets may vary.

The uptraining phase can replace standard supervised fine-tuning, producing a single model capable of handling both dense and sparse vision inputs effectively.

## Experimental Results and Performance

The authors conducted extensive experiments across multiple video understanding benchmarks including VideoMME, MVBench, TempCompass, and an internal nv-Metropolis dataset. The results demonstrate EVS's effectiveness across different model sizes and pruning rates.

![Performance comparison showing accuracy vs. percentage of tokens dropped for different video benchmarks, with both plug-in and uptrained variants](https://paper-assets.alphaxiv.org/figures/2510.14624v1/img-1.jpeg)

**Token Reduction and Speedup**: With a pruning rate of q=0.75q=0.75q=0.75 (removing 75% of tokens), EVS achieves up to 4x reduction in LLM Time-To-First-Token. The speedup is more pronounced for larger models, where the LLM component represents a larger fraction of total computation time.

![Time-to-First-Token speedup comparisons showing both LLM-only and full VLM performance improvements](https://paper-assets.alphaxiv.org/figures/2510.14624v1/img-3.jpeg)

**Memory Efficiency**: EVS provides linear reduction in KV-cache memory proportional to the pruning rate, enabling processing of longer sequences or larger batch sizes within the same memory constraints.

![KV-cache memory reduction showing linear decrease with pruning percentage](https://paper-assets.alphaxiv.org/figures/2510.14624v1/img-4.jpeg)

**Accuracy Preservation**: In plug-and-play mode, EVS maintains reasonable accuracy even with aggressive pruning. At q=0.75q=0.75q=0.75, accuracy drops are typically within a few percentage points across benchmarks. With uptraining, models can recover most of their original accuracy while maintaining the efficiency benefits.

The experiments also reveal that embedding-space pruning generally outperforms RGB-space pruning, and position-preserving encoding is crucial for uptrained models to achieve optimal performance.

## Technical Innovation and Distinctions

EVS's primary innovation lies in its combination of simplicity, effectiveness, and broad compatibility. Unlike learned approaches that require architectural modifications or additional parameters, EVS can be immediately applied to any existing VLM. The position-preserving encoding strategy is particularly clever, allowing the LLM to maintain its understanding of spatial-temporal relationships even when processing sparse inputs.

![Illustration of different positional encoding strategies during token pruning](https://paper-assets.alphaxiv.org/figures/2510.14624v1/img-2.jpeg)

The stochastic uptraining approach represents another significant contribution, creating models that can dynamically adapt to varying computational budgets without requiring multiple checkpoints or complex scheduling mechanisms.

## Significance and Future Directions

EVS addresses a fundamental scalability challenge in video understanding, making long-form video processing feasible for practical applications. The method's plug-and-play nature significantly lowers the barrier to adoption, allowing existing deployments to immediately benefit from improved efficiency.

The work opens several promising research directions. Online streaming applications could benefit from EVS's low-latency token selection, particularly when combined with KV-cache reuse strategies. Query-aware pruning could further improve efficiency by focusing computation on regions relevant to specific user questions. Integration with emerging long-context LLMs could enable processing of extremely long video sequences spanning hours rather than minutes.

The fundamental insight that temporal redundancy in video can be efficiently exploited without complex learned mechanisms provides a foundation for future work in efficient multimodal processing. As video content continues to grow in importance across AI applications, methods like EVS that can scale these systems while maintaining quality will become increasingly valuable for practical deployment.

Token merging: Your vit but faster

This paper introduces ToMe, a method for merging similar tokens based on embedding similarity to reduce computational load. The EVS paper contrasts its temporal-focused pruning against ToMe's purely spatial approach and includes it as a key baseline in experimental comparisons.

Daniel Bolya, Cheng-Yang Fu, Xiaoliang Dai, Peizhao Zhang, Christoph Feichtenhofer, and Judy Hoffman. Token merging: Your vit but faster, 2023.

Don’t look twice: Faster video transformers with run-length tokenization

This work is highly relevant as it also addresses temporal redundancy in videos by compressing consecutive duplicate tokens. The main paper differentiates EVS by highlighting its patch-level approach, which is potentially more robust to noise than RLT's pixel-level similarity metric.

Rohan Choudhury, Guanglei Zhu, Sihan Liu, Koichiro Niinuma, Kris M. Kitani, and L´aszl´o Jeni. Don’t look twice: Faster video transformers with run-length tokenization, 2024.

Longvu: Spatiotemporal adaptive compression for long video-language understanding

LongVU represents a common alternative strategy for reducing video tokens by selecting or skipping entire keyframes. The EVS paper presents its patch-level pruning as a more granular and flexible approach that can retain information from all frames, avoiding the potential information loss of whole-frame dropping.

Xiaoqian Shen, Yunyang Xiong, Changsheng Zhao, Lemeng Wu, Jun Chen, Chenchen Zhu, Zechun Liu, Fanyi Xiao, Balakrishnan Varadarajan, Florian Bordes, Zhuang Liu, Hu Xu, Hyunwoo J. Kim, Bilge Soran, Raghuraman Krishnamoorthi, Mohamed Elhoseiny, and Vikas Chandra. Longvu: Spatiotemporal adaptive compression for long video-language understanding, 2024.

Sparsevlm: Visual token sparsification for efficient vision-language model inference

This paper proposes another training-free method for token reduction that uses text-guidance to sparsify visual tokens. The main paper contrasts EVS with SparseVLM by emphasizing its own simplicity, as EVS does not require access to internal model states like attention matrices for its pruning decisions.

Yuan Zhang, Chun-Kai Fan, Junpeng Ma, Wenzhao Zheng, Tao Huang, Kuan Cheng, Denis Gudovskiy, Tomoyuki Okuno, Yohei Nakata, Kurt Keutzer, and Shanghang Zhang. Sparsevlm: Visual token sparsification for efficient vision-language model inference, 2025.

## Audio

Audio summaryTwo hosts talking through the paper's ideas, methods and results.

Generate

## Similar papers

[![](https://thumbnails.assets.alphaxiv.org/512/0196fc9e-d998-798c-bd55-fd4b7d09641f.png)MMInference: Accelerating Pre-filling for Long-Context VLMs via Modality-Aware Permutation Sparse Attention23 May 2025](https://www.alphaxiv.org/abs/2504.16083) [![](https://thumbnails.assets.alphaxiv.org/512/019733fd-5590-7388-bfd2-592da950a0b0.png)SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference03 Jun 2025](https://www.alphaxiv.org/abs/2410.04417) [![](https://thumbnails.assets.alphaxiv.org/512/019ab4b9-b068-72cf-8505-52a60edd01b5.png)Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models18 Nov 2025](https://www.alphaxiv.org/abs/2505.14454) [![](https://thumbnails.assets.alphaxiv.org/512/0195a214-1138-760d-8f44-d118b5150407.png)VideoScan: Enabling Efficient Streaming Video Understanding via Frame-level Semantic Carriers17 Mar 2025](https://www.alphaxiv.org/abs/2503.09387) [![](https://thumbnails.assets.alphaxiv.org/512/019d5daf-9962-733e-ba8c-95c62d3d3fc2.png)CoPE-VideoLM: Leveraging Codec Primitives For Efficient Video Language Modeling30 Mar 2026](https://www.alphaxiv.org/abs/2602.13191)

Show moreShow less

[![](https://thumbnails.assets.alphaxiv.org/512/0199e1a2-fab8-7e52-b803-1a0d0c90aec7.png)HoliTom: Holistic Token Merging for Fast Video Large Language Models10 Oct 2025](https://www.alphaxiv.org/abs/2505.21334) [![](https://thumbnails.assets.alphaxiv.org/512/019b44d8-a9ec-7fc0-9867-4bf39df32856.png)FastVID: Dynamic Density Pruning for Fast Video Large Language Models14 Dec 2025](https://www.alphaxiv.org/abs/2503.11187) [![](https://thumbnails.assets.alphaxiv.org/512/0196684a-8788-7a83-855b-e0f535988ffc.png)Keyframe-oriented Vision Token Pruning: Enhancing Efficiency of Large Vision Language Models on Long-Form Video Processing24 Apr 2025](https://www.alphaxiv.org/abs/2503.10742) [![](https://thumbnails.assets.alphaxiv.org/512/019c45fe-fc84-7423-a5d0-ae44e3dd0dbe.png)FlashVID: Efficient Video Large Language Models via Training-free Tree-based Spatiotemporal Token Merging08 Feb 2026](https://www.alphaxiv.org/abs/2602.08024) [![](https://thumbnails.assets.alphaxiv.org/512/0195dd18-11a8-7ca9-88cc-8e3b29bba336.png)DyCoke: Dynamic Compression of Tokens for Fast Video Large Language Models28 Mar 2025](https://www.alphaxiv.org/abs/2411.15024)

## Discussion

Leave a comment

Comment

Smart

Write notes about this paper...

Sign in to save