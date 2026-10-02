[Skip to content](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md) to refresh your session.Dismiss alert

{{ message }}

[OpenBMB](https://github.com/OpenBMB)/ **[MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V)** Public

- [Notifications](https://github.com/login?return_to=%2FOpenBMB%2FMiniCPM-V) You must be signed in to change notification settings
- [Fork\\
2.1k](https://github.com/login?return_to=%2FOpenBMB%2FMiniCPM-V)
- [Star\\
26.5k](https://github.com/login?return_to=%2FOpenBMB%2FMiniCPM-V)


## Collapse file tree

## Files

main

Search this repository(forward slash)` forward slash/`

/

# minicpm\_v4dot5\_en.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

[![BingH225](https://avatars.githubusercontent.com/u/155717179?v=4&size=40)](https://github.com/BingH225)[BingH225](https://github.com/OpenBMB/MiniCPM-V/commits?author=BingH225)

[docs: fix architecture spelling](https://github.com/OpenBMB/MiniCPM-V/commit/76092d9e1564a4c7d531a0f68f91cd5f1a739764)

2 months agoAug 29, 2026

[76092d9](https://github.com/OpenBMB/MiniCPM-V/commit/76092d9e1564a4c7d531a0f68f91cd5f1a739764) · 2 months agoAug 29, 2026

## History

[History](https://github.com/OpenBMB/MiniCPM-V/commits/main/docs/minicpm_v4dot5_en.md)

Open commit details

[View commit history for this file.](https://github.com/OpenBMB/MiniCPM-V/commits/main/docs/minicpm_v4dot5_en.md) History

158 lines (125 loc) · 9.66 KB

/

# minicpm\_v4dot5\_en.md

Copy path

Top

## File metadata and controls

- Preview

- Code

- Blame


158 lines (125 loc) · 9.66 KB

[Raw](https://github.com/OpenBMB/MiniCPM-V/raw/refs/heads/main/docs/minicpm_v4dot5_en.md)

Copy raw file

Download raw file

You must be signed in to make or propose changes

More edit options

Outline

Edit and raw actions

## MiniCPM-V 4.5

[Permalink: MiniCPM-V 4.5](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md#minicpm-v-45)

> Archieve at: 2026-02-03

**MiniCPM-V 4.5** is the latest and most capable model in the MiniCPM-V series. The model is built on Qwen3-8B and SigLIP2-400M with a total of 8B parameters. It exhibits a significant performance improvement over previous MiniCPM-V and MiniCPM-o models, and introduces new useful features. Notable features of MiniCPM-V 4.5 include:

- 🔥 **State-of-the-art Vision-Language Capability.**
MiniCPM-V 4.5 achieves an average score of 77.0 on OpenCompass, a comprehensive evaluation of 8 popular benchmarks. **With only 8B parameters, it surpasses widely used proprietary models like GPT-4o-latest, Gemini-2.0 Pro, and strong open-source models like Qwen2.5-VL 72B** for vision-language capabilities, making it the most performant MLLM under 30B parameters.

- 🎬 **Efficient High-FPS and Long Video Understanding.** Powered by a new unified 3D-Resampler over images and videos, MiniCPM-V 4.5 can now achieve 96x compression rate for video tokens, where 6 448x448 video frames can be jointly compressed into 64 video tokens (normally 1,536 tokens for most MLLMs). This means that the model can perceive significantly more video frames without increasing the LLM inference cost. This brings state-of-the-art high-FPS (up to 10FPS) video understanding and long video understanding capabilities on Video-MME, LVBench, MLVU, MotionBench, FavorBench, etc., efficiently.

- ⚙️ **Controllable Hybrid Fast/Deep Thinking.** MiniCPM-V 4.5 supports both fast thinking for efficient frequent usage with competitive performance, and deep thinking for more complex problem solving. To cover efficiency and performance trade-offs in different user scenarios, this fast/deep thinking mode can be switched in a highly controlled fashion.

- 💪 **Strong OCR, Document Parsing and Others.**
Based on [LLaVA-UHD](https://arxiv.org/pdf/2403.11703) architecture, MiniCPM-V 4.5 can process high-resolution images with any aspect ratio and up to 1.8 million pixels (e.g., 1344x1344), using 4x fewer visual tokens than most MLLMs. The model achieves **leading performance on OCRBench, surpassing proprietary models such as GPT-4o-latest and Gemini 2.5**. It also achieves state-of-the-art performance for PDF document parsing capability on OmniDocBench among general MLLMs. Based on the latest [RLAIF-V](https://github.com/RLHF-V/RLAIF-V/) and [VisCPM](https://github.com/OpenBMB/VisCPM) techniques, it features **trustworthy behaviors**, outperforming GPT-4o-latest on MMHal-Bench, and supports **multilingual capabilities** in more than 30 languages.

- 💫 **Easy Usage.**
MiniCPM-V 4.5 can be easily used in various ways: (1) [llama.cpp](https://github.com/tc-mb/llama.cpp/blob/Support-MiniCPM-V-4.5/docs/multimodal/minicpmv4.5.md) and [ollama](https://github.com/tc-mb/ollama/tree/MIniCPM-V) support for efficient CPU inference on local devices, (2) [int4](https://huggingface.co/openbmb/MiniCPM-V-4_5-int4), [GGUF](https://huggingface.co/openbmb/MiniCPM-V-4_5-gguf) and [AWQ](https://github.com/tc-mb/AutoAWQ) format quantized models in 16 sizes, (3) [SGLang](https://github.com/tc-mb/sglang/tree/main) and [vLLM](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md#efficient-inference-with-llamacpp-ollama-vllm) support for high-throughput and memory-efficient inference, (4) fine-tuning on new domains and tasks with [Transformers](https://github.com/tc-mb/transformers/tree/main) and [LLaMA-Factory](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/llamafactory_train_and_infer.md), (5) quick [local WebUI demo](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md#chat-with-our-demo-on-gradio), (6) optimized [local iOS app](https://github.com/OpenBMB/MiniCPM-V-Apps) on iPhone and iPad, and (7) online web demo on [server](https://huggingface.co/spaces/openbmb/MiniCPM-V-4_5-Demo). See our [Cookbook](https://github.com/OpenSQZ/MiniCPM-V-CookBook) for full usage!


### Key Techniques

[Permalink: Key Techniques ](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md#key-techniques-)

[![](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpm-v-4dot5-framework.png)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpm-v-4dot5-framework.png)

- **Architecture: Unified 3D-Resampler for High-density Video Compression.** MiniCPM-V 4.5 introduces a 3D-Resampler that overcomes the performance-efficiency trade-off in video understanding. By grouping and jointly compressing up to 6 consecutive video frames into just 64 tokens (the same token count used for a single image in MiniCPM-V series), MiniCPM-V 4.5 achieves a 96× compression rate for video tokens. This allows the model to process more video frames without additional LLM computational cost, enabling high-FPS video and long video understanding. The architecture supports unified encoding for images, multi-image inputs, and videos, ensuring seamless capability and knowledge transfer.

- **Pre-training: Unified Learning for OCR and Knowledge from Documents.** Existing MLLMs learn OCR capability and knowledge from documents in isolated training approaches. We observe that the essential difference between these two training approaches is the visibility of the text in images. By dynamically corrupting text regions in documents with varying noise levels and asking the model to reconstruct the text, the model learns to adaptively and properly switch between accurate text recognition (when text is visible) and multimodal context-based knowledge reasoning (when text is heavily obscured). This eliminates reliance on error-prone document parsers in knowledge learning from documents, and prevents hallucinations from over-augmented OCR data, resulting in top-tier OCR and multimodal knowledge performance with minimal engineering overhead.

- **Post-training: Hybrid Fast/Deep Thinking with Multimodal RL.** MiniCPM-V 4.5 offers a balanced reasoning experience through two switchable modes: fast thinking for efficient daily use and deep thinking for complex tasks. Using a new hybrid reinforcement learning method, the model jointly optimizes both modes, significantly enhancing fast-mode performance without compromising deep-mode capability. Incorporated with [RLPR](https://github.com/OpenBMB/RLPR) and [RLAIF-V](https://github.com/RLHF-V/RLAIF-V), it generalizes robust reasoning skills from broad multimodal data while effectively reducing hallucinations.


### Evaluation

[Permalink: Evaluation  ](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md#evaluation--)

[![](https://github.com/OpenBMB/MiniCPM-V/raw/main/docs/assets/radar_minicpm_v45.png)](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/assets/radar_minicpm_v45.png)

[![](https://github.com/OpenBMB/MiniCPM-V/raw/main/docs/assets/minicpmv_4_5_evaluation_result.png)](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/assets/minicpmv_4_5_evaluation_result.png)

### Inference Efficiency

[Permalink: Inference Efficiency](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md#inference-efficiency)

**OpenCompass**

| Model | Size | Avg Score ↑ | Total Inference Time ↓ |
| :-- | --- | --- | --- |
| GLM-4.1V-9B-Thinking | 10.3B | 76.6 | 17.5h |
| MiMo-VL-7B-RL | 8.3B | 76.4 | 11h |
| MiniCPM-V 4.5 | 8.7B | **77.0** | **7.5h** |

**Video-MME**

| Model | Size | Avg Score ↑ | Total Inference Time ↓ | GPU Mem ↓ |
| :-- | --- | --- | --- | --- |
| Qwen2.5-VL-7B-Instruct | 8.3B | 71.6 | 3h | 60G |
| GLM-4.1V-9B-Thinking | 10.3B | **73.6** | 2.63h | 32G |
| MiniCPM-V 4.5 | 8.7B | 73.5 | **0.26h** | **28G** |

Both Video-MME and OpenCompass were evaluated using 8×A100 GPUs for inference. The reported inference time of Video-MME includes full model-side computation, and excludes the external cost of video frame extraction (dependent on specific frame extraction tools) for fair comparison.

### Examples

[Permalink: Examples  ](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md#examples--)

[![](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/MiniCPM-V%204.5-8.26_img.jpeg)](https://www.youtube.com/watch?v=Cn23FujYMMU)

[![en_case1](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/en_case1.png)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/en_case1.png)[![en_case2](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/en_case2.png)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/en_case2.png)[![en_case3](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/en_case3.jpeg)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/en_case3.jpeg)

Click to view more cases.

[![zh_extra](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/zh_extra.jpeg)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/zh_extra.jpeg)

We deploy MiniCPM-V 4.5 on iPad M4 with [iOS demo](https://github.com/OpenBMB/MiniCPM-V-Apps). The demo video is the raw screen recording without edition.

[![](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/v45_en_handwriting.gif)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_en_handwriting.gif)[![v45_en_handwriting.gif](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/v45_en_handwriting.gif)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_en_handwriting.gif)[Open v45_en_handwriting.gif in new window](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_en_handwriting.gif)[![](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/v45_en_cot.gif)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_en_cot.gif)[![v45_en_cot.gif](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/v45_en_cot.gif)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_en_cot.gif)[Open v45_en_cot.gif in new window](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_en_cot.gif)

[![](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/v45_cn_handwriting.gif)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_cn_handwriting.gif)[![v45_cn_handwriting.gif](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/v45_cn_handwriting.gif)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_cn_handwriting.gif)[Open v45_cn_handwriting.gif in new window](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_cn_handwriting.gif)[![](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/v45_cn_travel.gif)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_cn_travel.gif)[![v45_cn_travel.gif](https://github.com/OpenBMB/MiniCPM-V/raw/main/assets/minicpmv4_5/v45_cn_travel.gif)](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_cn_travel.gif)[Open v45_cn_travel.gif in new window](https://github.com/OpenBMB/MiniCPM-V/blob/main/assets/minicpmv4_5/v45_cn_travel.gif)

|
|

You can’t perform that action at this time.