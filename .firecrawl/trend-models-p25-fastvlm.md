[content type highlight](https://machinelearning.apple.com/highlights)published July 23, 2025

[research area Computer Vision](https://machinelearning.apple.com/highlights?domain=Computer%20Vision)

# FastVLM: Efficient Vision Encoding for Vision Language Models

Vision Language Models (VLMs) enable visual understanding alongside textual inputs. They are typically built by passing visual tokens from a pretrained vision encoder to a pretrained Large Language Model (LLM) through a projection layer. By leveraging the rich visual representations of the vision encoder and the world knowledge and reasoning capabilities of the LLM, VLMs can be useful for a wide range of applications, including accessibility assistants, UI navigation, robotics, and gaming.

**Update** _\- September 22, 2025:_

- _FastVLM models, including checkpoints for MLX and CoreML, are available on HuggingFace [here](https://huggingface.co/collections/apple/fastvlm-68ac97b9cd5cacefdd04872e)._
- _HuggingFace has also shared a FastVLM demo that works in real-time directly in the browser, powered by transformers.js and WebGPU, available [here](https://huggingface.co/spaces/apple/fastvlm-webgpu). Videos of the demo in action are available in [this thread](https://x.com/xenovacom/status/1961454543503344036)._
- _MobileCLIP2 is now also available on HuggingFace, [here](https://huggingface.co/collections/apple/mobileclip2-68ac947dcb035c54bcd20c47). MobileCLIP2 models are a family of image-text models that can be used as the image encoder in fast VLM models such as FastVLM. For more detail, please see the paper: [MobileCLIP2: Improving Multi-Modal Reinforced Training](https://machinelearning.apple.com/research/mobileclip2), which has been accepted to [Transactions on Machine Learning Research](https://jmlr.org/tmlr/papers/#) with Featured certification._

VLM accuracy generally improves with higher input image resolution, creating a tradeoff between accuracy and efficiency. For many production use-cases, VLMs need to be both accurate and efficient to meet the low-latency demands of real-time applications and run on-device for privacy-preserving AI experiences.

In a [paper](https://machinelearning.apple.com/research/fastvlm-efficient-vision-encoding) accepted to CVPR 2025, Apple ML researchers recently shared a new technique to address this challenge: FastVLM, a new type of VLM that significantly improves accuracy-latency trade-offs with a simple design. Leveraging a hybrid architecture visual encoder designed for high-resolution images, FastVLM delivers accurate, fast, and efficient visual query processing, making it suitable for powering real-time applications on-device. The inference code, model checkpoints, and an iOS/macOS demo app based on [MLX](https://opensource.apple.com/projects/mlx/) are available [here](https://github.com/apple/ml-fastvlm/).

## [Image Resolution and the Accuracy-Latency Tradeoff](https://machinelearning.apple.com/research/fast-vision-language-models\#image-resolution-and-the-accuracy-latency-tradeoff)

Generally, VLM accuracy improves with higher image resolution, especially for tasks needing detailed understanding, such as document analysis, UI recognition, or answering natural language queries about images. For example, in [Figure 1](https://machinelearning.apple.com/research/fast-vision-language-models#figure1) below, we ask our VLM about the street sign visible in the image. On the left, the model receives a low-resolution image and cannot respond correctly. On the right, the VLM receives a high-resolution image and correctly identifies the traffic sign which is a “Do Not Enter”.

### Question

What does the street sign mention?

### Low Res Model

![Low resolution image of New York street with skyscrapers, train bridge, vehicles, and road signs.](https://mlr.cdn-apple.com/media/fast_vlm_fig1_lowres_76be49e44a.jpg)

Answer

The Street sign in the image mentions "bus stop". hidden placeholder text

Incorrect

### High Res Model

![High resolution image of New York street with skyscrapers, train bridge, vehicles, and road signs.](https://mlr.cdn-apple.com/media/fast_vlm_fig1_hires_f00f1c98cb.jpg)

Answer

The street sign in the image is red and white, and it says "Do Not Enter".

Correct

Figure 1: Comparison of VLM performance with a low-resolution (left) and high-resolution (right) input image.

High resolution significantly increases time-to-first-token in VLMs. While using high-resolution images improves accuracy, it also reduces efficiency in two ways: 1) higher resolution images take longer for the vision encoder to process, and 2) the encoder creates more visual tokens, which increases the pre-filling time for the LLM. Both factors increase the time-to-first-token (TTFT), which is the sum of vision encoding time and LLM pre-filling time. As shown in [Figure 2](https://machinelearning.apple.com/research/fast-vision-language-models#figure2) below, both vision encoding and LLM pre-filling times grow as image resolution increases, and at high resolutions, vision encoder latency becomes the dominant bottleneck. To address this, our research introduces FastVLM, a new vision language model that significantly improves efficiency without sacrificing accuracy.

### Latency Breakdown

#### For 1.5B VLM (fp16)

Figure 2: Vision latency dominates at high resolution. Breakdown of FastVLM’s time to the first token for different image resolutions. The vision encoder is FastViT-HD, and the LLM has 1.5B parameters.

## [Hybrid Vision Encoders Deliver the Best Accuracy-Latency Tradeoff](https://machinelearning.apple.com/research/fast-vision-language-models\#hybrid-vision-encoders-deliver-the-best-accuracy-latency-tradeoff)

To identify which architecture delivers the best accuracy-latency tradeoff, we systematically compared existing pre-trained vision encoders with an experiment in which everything (training data, recipe, LLM, etc.) was kept the same, and only the vision encoder was changed. In [Figure 3](https://machinelearning.apple.com/research/fast-vision-language-models#figure3) below, the x-axis shows TTFT, and the y-axis shows the average accuracy across different VLM tasks. We show two points for popular transformer-based encoders, [ViT-L/14](https://arxiv.org/abs/2103.00020) and [SigLIP-SO400](https://arxiv.org/abs/2303.15343), pre-trained on image-text data at their native resolutions. We also show curves for [ConvNeXT](https://arxiv.org/abs/2405.15738)(fully convolutional encoder) and FastViT (a hybrid encoder combining convolutional and transformer blocks) at various resolutions. FastViT, which is based on two of our previous works ( [FastViT](https://machinelearning.apple.com/research/fastvit), ICCV 2023; and [MobileCLIP](https://machinelearning.apple.com/research/mobileclip), CVPR 2024), achieves the best accuracy-latency trade-off compared to other vision encoders—about 8 times smaller and 20 times faster than ViT-L/14.

### Performance Comparison to FastViT

ViT-L/14SigLIP-SO400ConvNeXT-L

Figure 3: Comparison of different vision architectures for visual encoding in VLMs. All vision
encoders are pre-trained with CLIP and trained using the same setup (dataset, recipe, LLM size).
The FastViT hybrid architecture achieves the best accuracy-latency trade-off. Avg-5 is the average
performance of the model on [GQA](https://arxiv.org/abs/1902.09506),
[TextVQA](https://arxiv.org/abs/1904.08920), [DocVQA](https://arxiv.org/abs/2007.00398),
[SeedBench](https://arxiv.org/abs/2307.16125) and [POPE](https://arxiv.org/abs/2305.10355)
benchmarks.

## [FastViTHD: An Optimal Vision Encoder for VLMs](https://machinelearning.apple.com/research/fast-vision-language-models\#fastvithd-an-optimal-vision-encoder-for-vlms)

While the FastViT hybrid backbone is a great choice for efficient VLMs, larger vision encoders are needed for improved accuracy on challenging tasks. Initially, we simply increased the size of each FastViT layer. However, this naive scaling made FastViT even less efficient than fully convolutional encoders at higher resolutions. To address this, we designed a new backbone, FastViTHD, specifically for high-resolution images. FastViTHD includes an extra stage compared to FastViT and is pre-trained using the MobileCLIP recipe to produce fewer but higher-quality visual tokens.

FastViTHD has better latency at high resolution images compared to FastViT, but to evaluate which is best in a VLM, we compared their performance when combined with LLMs of various sizes. We evaluated different pairs of (image resolution, LLM size), and three LLMs with 0.5B, 1.5B, and 7B parameters (corresponding to each curve in [Figure 4](https://machinelearning.apple.com/research/fast-vision-language-models#figure4) below) and pair it with vision backbone running at different resolutions.

As shown in [Figure 4](https://machinelearning.apple.com/research/fast-vision-language-models#figure4), using very high resolution images with a small LLM is not always the optimal choice; sometimes it is better to switch the LLM to a larger one instead of increasing the resolution. For each case, we show the Pareto-optimal curve with dashed lines, which shows the optimal (image resolution, LLM size) for a given runtime budget (TTFT here). Comparing Pareto-optimal curves, FastVLM (based on FastViTHD) offers a much better accuracy-latency trade-off than the FastViT-based model. It can be up to 3x faster for the same accuracy. Note that we had already shown that FastViT is significantly better than purely transformer-based or convolutional-based encoders.

### Pareto-Optimal Curve by Model Size

0.5B1.5B7B

Figure 4: Comparison of FastViT and FastViT-HD backbones paired with LLMs of varying sizes and different image resolutions. Dashed lines show Pareto-optimal curve for both vision backbones. Note that the x-axis is in log scale. Avg-5 is the average performance of the model on GQA, TextVQA, DocVQA, SeedBench and POPE benchmarks.

## [FastVLM: a New VLM Based on FastViTHD](https://machinelearning.apple.com/research/fast-vision-language-models\#fastvlm-a-new-vlm-based-on-fastvithd)

FastViTHD is a hybrid convolutional-transformer architecture comprising a convolutional stem, three convolutional stages, and two subsequent stages of transformer blocks. Each stage is preceded by a patch embedding layer that reduces the spatial dimensions of the input tensor by a factor of two. Using FastViTHD as the vision encoder, we built FastVLM, with a simple Multi-Layer Perceptron (MLP) module to project visual tokens to the embedding space of LLM, as shown in [Figure 5](https://machinelearning.apple.com/research/fast-vision-language-models#figure5).

![Figure 5: Overview of the FastVLM architecture.](https://mlr.cdn-apple.com/media/fast_vlm_fig5_cd0aa7ebc1.png)

Figure 5: Overview of the FastVLM architecture. FastVLM features our novel vision encoder, FastViT-HD, which incorporates multi-scale pooling, additional self-attention layers, and downsampling to generate 4× fewer tokens than FastViT and 16× fewer tokens than ViT-L/14 at a resolution of 336.

## [FastVLM Outperforms Token Pruning and Merging Methods](https://machinelearning.apple.com/research/fast-vision-language-models\#fastvlm-outperforms-token-pruning-and-merging-methods)

Prior research works in accelerating VLMs have employed complex merging or pruning techniques to reduce visual token counts to speed up LLM prefilling (and thus reduce the time to first token). As shown in [Figure 6](https://machinelearning.apple.com/research/fast-vision-language-models#figure6) below, FastVLM achieves higher overall accuracy across different visual token counts (corresponding to different input resolutions) compared to these approaches. This is due to the high-quality visual tokens from its FastViTHD encoder, and because FastVLM does not require complicated token pruning or merging, it is simpler to deploy.

### Performance Comparison

Figure 6: Comparison of FastVLM’s average performance at different input image resolutions, corresponding to varying numbers of visual tokens, and different token pruning and merging methods. Y-axis is the average performance of the model on GQA, TextVQA, ScienceQA, SeedBench and POPE benchmarks.

## [FastVLM and Dynamic Tiling](https://machinelearning.apple.com/research/fast-vision-language-models\#fastvlm-and-dynamic-tiling)

As noted earlier, VLM accuracy increases with input resolution, particularly for tasks requiring understanding fine-grain details. Dynamic tiling (for example, in [AnyRes](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Improved_Baselines_with_Visual_Instruction_Tuning_CVPR_2024_paper.html)) is a popular way to handle very high-resolution images. This approach divides an image into smaller tiles, processes each tile separately through the vision encoder, and then sends all tokens to the LLM, as in [Figure 7](https://machinelearning.apple.com/research/fast-vision-language-models#figure7) shown below.

![Figure 7: Dynamic tiling approach.](https://mlr.cdn-apple.com/media/fast_vlm_fig7_530b99fbfc.png)

Figure 7: AnyRes tiling encodes different sub-regions of the image (tiles) separately, along with a lower-resolution version of the full image, passing all tokens to the LLM.

Since FastVLM naturally handles high-resolution images, we explored if combining FastVLM with dynamic tiling improves its accuracy-latency tradeoff. [Figure 8](https://machinelearning.apple.com/research/fast-vision-language-models#figure8) below shows that FastVLM without tiling (blue curve) achieves a better accuracy-latency trade-off compared to dynamic tiling (pink points), up to very high image resolutions, at which point combing FastVLM and AnyRes can be beneficial.

### Tiling Effect on Performance

2x23x34x4

Figure 8: Dynamic tiling (AnyRes) for FastVLM is only optimal at the highest resolution and when using fewer tiles (2×2). The tile grid size is specified in parentheses. Note that the x-axis is in log scale. Avg-5 is the average performance of the model on GQA, TextVQA, DocVQA, SeedBench and POPE benchmarks.

## [FastVLM is Faster and More Accurate Than Popular VLMs of the Same Size](https://machinelearning.apple.com/research/fast-vision-language-models\#fastvlm-is-faster-and-more-accurate-than-popular-vlms-of-the-same-size)

Finally, we compared FastVLM with other popular VLMs. In [Figure 9](https://machinelearning.apple.com/research/fast-vision-language-models#figure9) below, we show two curves for FastVLM: one with AnyRes (to achieve the highest accuracy) and one without tiling (for the best accuracy-latency tradeoff), each tested with three different LLM sizes. FastVLM is significantly faster and more accurate than popular models of the same size as indicated by the arrows: it is 85x faster than [LLava-OneVision](https://arxiv.org/abs/2408.03326)(0.5B LLM), 5.2x faster than [SmolVLM](https://arxiv.org/abs/2504.05299v1)(~0.5B LLM), and 21x faster than [Cambrian-1](https://arxiv.org/abs/2406.16860)(7B LLM).

### Performance Comparison by Model Size

Figure 9: Comparison of FastVLM with popular VLMs. Arrows indicate comparisons with similarly sized VLMs, highlighting FastVLM’s superior accuracy and significantly faster performance. Y-axis is the average performance of the model on ChartQA, TextVQA, DocVQA, OCRBench, AI2D, MMMU and ScienceQA benchmarks.

To further show the on-device efficiency of FastVLM, we released an [iOS/macOS demo app](https://github.com/apple/ml-fastvlm/tree/main/app) based on MLX. [Figure 10](https://machinelearning.apple.com/research/fast-vision-language-models#figure10) shows examples of FastVLM running locally on an iPhone GPU. FastVLM’s near real-time performance can enable new on-device features and experiences.

Figure 10: Demo app running FastVLM 0.5B model on iPhone 16 Pro. Time to first token is shown on the screen, highlighting near real-time performance.

## [Conclusion](https://machinelearning.apple.com/research/fast-vision-language-models\#conclusion)

By combining visual and textual understanding, VLMs can power a range of useful applications. Because the accuracy of these models generally corresponds to the resolution of input images, there has often been a performance tradeoff between accuracy and efficiency, which has limited the value of VLMs for applications that require both high accuracy and great efficiency.

FastVLM addresses this tradeoff by leveraging a hybrid-architecture vision encoder built for high-resolution images, FastViTHD. With a simple design, FastVLM outperforms prior approaches in both accuracy and efficiency, enabling on-device visual query processing suitable for real-time on-device applications.

April 18, 2025 [research area Computer Vision](https://machinelearning.apple.com/research/?domain=Computer%20Vision) [conference CVPR](https://machinelearning.apple.com/research/?event=CVPR)

Scaling the input image resolution is essential for enhancing the performance of Vision Language Models (VLMs), particularly in text-rich image understanding tasks. However, popular visual encoders such as ViTs become inefficient at high resolutions due to the large number of tokens and high encoding latency. At different operational resolutions, the vision encoder of a VLM can be optimized along two axes: reducing encoding latency and minimizing…

[Read more](https://machinelearning.apple.com/research/fastvlm-efficient-vision-encoding)

June 7, 2022 [research area Computer Vision](https://machinelearning.apple.com/highlights?domain=Computer%20Vision), [research area Methods and Algorithms](https://machinelearning.apple.com/highlights?domain=Methods%20and%20Algorithms)

Scene analysis is an integral core technology that powers many features and experiences in the Apple ecosystem. From visual content search to powerful memories marking special occasions in one’s life, outputs (or “signals”) produced by scene analysis are critical to how users interface with the photos on their devices. Deploying dedicated models for each of these individual features is inefficient as many of these models can benefit from sharing resources. We present how we developed Apple Neural Scene Analyzer (ANSA), a unified backbone to build and maintain scene analysis workflows in production. This was an important step towards enabling Apple to be among the first in the industry to deploy fully client-side scene analysis in 2016.

[Read more](https://machinelearning.apple.com/research/on-device-scene-analysis)

![Bottom banner](https://mlr.cdn-apple.com/media/Discover_1440x420_2x_9c465d585e.jpg)

## Discover opportunities in Machine Learning.

Our research in machine learning breaks new ground every day.

[Work with us](https://machinelearning.apple.com/work-with-us)