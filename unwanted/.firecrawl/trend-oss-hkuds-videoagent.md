[Skip to content](https://github.com/HKUDS/VideoAgent#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/HKUDS/VideoAgent) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/HKUDS/VideoAgent) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/HKUDS/VideoAgent) to refresh your session.Dismiss alert

{{ message }}

[HKUDS](https://github.com/HKUDS)/ **[VideoAgent](https://github.com/HKUDS/VideoAgent)** Public

- [Notifications](https://github.com/login?return_to=%2FHKUDS%2FVideoAgent) You must be signed in to change notification settings
- [Fork\\
243](https://github.com/login?return_to=%2FHKUDS%2FVideoAgent)
- [Star\\
1.9k](https://github.com/login?return_to=%2FHKUDS%2FVideoAgent)


main

[**1** Branch](https://github.com/HKUDS/VideoAgent/branches) [**0** Tags](https://github.com/HKUDS/VideoAgent/tags)

[Go to Branches page](https://github.com/HKUDS/VideoAgent/branches)[Go to Tags page](https://github.com/HKUDS/VideoAgent/tags)

Go to file

Code

Open more actions menu

## Latest commit

[![Hengji-cs](https://avatars.githubusercontent.com/u/177777906?v=4&size=40)](https://github.com/Hengji-cs)[Hengji-cs](https://github.com/HKUDS/VideoAgent/commits?author=Hengji-cs)

[Add files via upload](https://github.com/HKUDS/VideoAgent/commit/f207987e3cffb554aaa6ffdbe733efb30f4b51ed)

3 months agoJul 22, 2026

[f207987](https://github.com/HKUDS/VideoAgent/commit/f207987e3cffb554aaa6ffdbe733efb30f4b51ed) · 3 months agoJul 22, 2026

## History

[265 Commits](https://github.com/HKUDS/VideoAgent/commits/main/)

Open commit details

[View commit history for this file.](https://github.com/HKUDS/VideoAgent/commits/main/) 265 Commits

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| [VideoEdit](https://github.com/HKUDS/VideoAgent/tree/main/VideoEdit "VideoEdit") | [VideoEdit](https://github.com/HKUDS/VideoAgent/tree/main/VideoEdit "VideoEdit") | [Add files via upload](https://github.com/HKUDS/VideoAgent/commit/f207987e3cffb554aaa6ffdbe733efb30f4b51ed "Add files via upload") | 3 months agoJul 22, 2026 |
| [assets](https://github.com/HKUDS/VideoAgent/tree/main/assets "assets") | [assets](https://github.com/HKUDS/VideoAgent/tree/main/assets "assets") | [Add files via upload](https://github.com/HKUDS/VideoAgent/commit/6e7f46397d82d40c1f4a89040ff82cd5706f6f6f "Add files via upload") | last yearOct 11, 2025 |
| [dataset](https://github.com/HKUDS/VideoAgent/tree/main/dataset "dataset") | [dataset](https://github.com/HKUDS/VideoAgent/tree/main/dataset "dataset") | [update](https://github.com/HKUDS/VideoAgent/commit/26d7b2e83dbac0f10f3f0942e535c54b92a757ee "update  Agentic Video Intelligence") | last yearJul 17, 2025 |
| [environment](https://github.com/HKUDS/VideoAgent/tree/main/environment "environment") | [environment](https://github.com/HKUDS/VideoAgent/tree/main/environment "environment") | [Fix orchestrator crashes and unsafe eval in MultiAgent](https://github.com/HKUDS/VideoAgent/commit/5e81d5d8f82c01370c5ecea9c4f708be869774c8 "Fix orchestrator crashes and unsafe eval in MultiAgent  Several bugs in environment/agents/multi.py cause the CLI to crash or behave incorrectly during normal operation:  1. run() subscripted the return of process_requirement without guarding    the failure path. process_requirement returns the int 1 (in 4 places)    when intent analysis, graph generation, or graph judgment fails to    converge, so run() then raised    `TypeError: 'int' object is not subscriptable` on `result[\"Agent Graph\"]`.    Since the surrounding LLM-driven pipeline can legitimately fail to    converge, this crashed the program on otherwise-recoverable failures.    Guard with an isinstance(result, dict) check and exit cleanly.  2. intents_analysis() used eval() on a string parsed from raw LLM output.    This executes arbitrary Python and is an injection risk. Replace with    ast.literal_eval, which parses the list literal identically while    refusing anything other than literals. Malformed output still raises    (caught by the existing handler) so retry behavior is unchanged.  3. The intent-analysis retry loop checked `attempt == MAX_Retries`, which    is never true for range(MAX_Retries) (0..MAX_Retries-1). The \"reached    max retries\" branch was dead code. Fix the comparison to    MAX_Retries - 1, matching the graph-generation loop.  4. In the graph-generation loop, agent_data was indexed    ([\"Agent Graph\"], etc.) before the `if agent_data:` check, so a None    return from generate_agent_graph raised TypeError instead of taking    the intended empty-value branch. Move the None-check before indexing.  Co-Authored-By: Claude <noreply@anthropic.com>") | 3 months agoJul 3, 2026 |
| [tools](https://github.com/HKUDS/VideoAgent/tree/main/tools "tools") | [tools](https://github.com/HKUDS/VideoAgent/tree/main/tools "tools") | [Update caption.py with frames insert](https://github.com/HKUDS/VideoAgent/commit/e275a8713ab4fcf93010e3d2b070b105059a8d72 "Update caption.py with frames insert") | last yearSep 1, 2025 |
| [.DS\_Store](https://github.com/HKUDS/VideoAgent/blob/main/.DS_Store ".DS_Store") | [.DS\_Store](https://github.com/HKUDS/VideoAgent/blob/main/.DS_Store ".DS_Store") | [update why](https://github.com/HKUDS/VideoAgent/commit/2a20f66b1ff4a09e8af1d57e58949a8f4e2433d5 "update why") | last yearJul 19, 2025 |
| [Communication.md](https://github.com/HKUDS/VideoAgent/blob/main/Communication.md "Communication.md") | [Communication.md](https://github.com/HKUDS/VideoAgent/blob/main/Communication.md "Communication.md") | [Update Communication.md](https://github.com/HKUDS/VideoAgent/commit/aee9dedbb5e8dd0b8aaddb54375557ce14dc507c "Update Communication.md") | last yearOct 16, 2025 |
| [LICENSE](https://github.com/HKUDS/VideoAgent/blob/main/LICENSE "LICENSE") | [LICENSE](https://github.com/HKUDS/VideoAgent/blob/main/LICENSE "LICENSE") | [Create LICENSE](https://github.com/HKUDS/VideoAgent/commit/e0fcf075df93fde973fe38f2f72f8de608bfd09a "Create LICENSE") | last yearJul 23, 2025 |
| [demos\_documents.md](https://github.com/HKUDS/VideoAgent/blob/main/demos_documents.md "demos_documents.md") | [demos\_documents.md](https://github.com/HKUDS/VideoAgent/blob/main/demos_documents.md "demos_documents.md") | [Update demos\_documents.md](https://github.com/HKUDS/VideoAgent/commit/0d37e148a29341b517601a872838fd56847f3542 "Update demos_documents.md") | last yearJul 19, 2025 |
| [main.py](https://github.com/HKUDS/VideoAgent/blob/main/main.py "main.py") | [main.py](https://github.com/HKUDS/VideoAgent/blob/main/main.py "main.py") | [Update main.py with banner](https://github.com/HKUDS/VideoAgent/commit/313a6c1c7ecdff07e16a7b566d5e9f24ecea24b4 "Update main.py with banner") | last yearJul 20, 2025 |
| [pyproject.toml](https://github.com/HKUDS/VideoAgent/blob/main/pyproject.toml "pyproject.toml") | [pyproject.toml](https://github.com/HKUDS/VideoAgent/blob/main/pyproject.toml "pyproject.toml") | [Update pyproject.toml](https://github.com/HKUDS/VideoAgent/commit/1af1a1cf5ae66b87e3b161b9450fcca7569c5978 "Update pyproject.toml") | last yearAug 27, 2025 |
| [readme.md](https://github.com/HKUDS/VideoAgent/blob/main/readme.md "readme.md") | [readme.md](https://github.com/HKUDS/VideoAgent/blob/main/readme.md "readme.md") | [Enhance README](https://github.com/HKUDS/VideoAgent/commit/331b3582aaf0d60e65130c4193fc77cfdd99ec14 "Enhance README") | 4 months agoJul 1, 2026 |
| [readme\_zh.md](https://github.com/HKUDS/VideoAgent/blob/main/readme_zh.md "readme_zh.md") | [readme\_zh.md](https://github.com/HKUDS/VideoAgent/blob/main/readme_zh.md "readme_zh.md") | [Update readme\_zh.md](https://github.com/HKUDS/VideoAgent/commit/6e0ddb4f8043c98d05e0a0c7d17e02662997371b "Update readme_zh.md  Modify from novel to screen to commentary video/解说视频") | last yearJul 19, 2025 |
| [requirements.txt](https://github.com/HKUDS/VideoAgent/blob/main/requirements.txt "requirements.txt") | [requirements.txt](https://github.com/HKUDS/VideoAgent/blob/main/requirements.txt "requirements.txt") | [update](https://github.com/HKUDS/VideoAgent/commit/26d7b2e83dbac0f10f3f0942e535c54b92a757ee "update  Agentic Video Intelligence") | last yearJul 17, 2025 |
| View all files |

## Repository files navigation

[![](https://github.com/HKUDS/VideoAgent/raw/main/assets/logo_new.png)](https://github.com/HKUDS/VideoAgent/blob/main/assets/logo_new.png)

**🌟 Comprehensive Video Intelligence:**

**An All-in-One Framework for Understanding, Editing, and Generation**

[![](https://camo.githubusercontent.com/8a8fdf2fa9b4951262e11345ce95cd215fa5d69c903837e9663a83504dfd2164/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f62696c6962696c692d3030413144363f7374796c653d666f722d7468652d6261646765266c6f676f3d62696c6962696c69266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)](https://space.bilibili.com/3546868449544308)[![](https://camo.githubusercontent.com/d353d03a7203fe902e90d0210eb07fee42df25a6dd2abe67a15dbd8b2e9b1cb5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f596f75547562652d4646303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d796f7574756265266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)](https://www.youtube.com/@AI-Creator-is-here)

[![](https://camo.githubusercontent.com/a41c8bd6b66ba37cc5460208a8f5a9798fe99b645d58c15516617867467246a0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652ff09f92ac4665697368752d47726f75702d3037633136303f7374796c653d666f722d7468652d6261646765266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)](https://github.com/HKUDS/VideoAgent/blob/main/Communication.md)[![](https://camo.githubusercontent.com/4273cfad6838a34696cff30ddbd0999efbe34a3fd612826c07c36262b78a4afa/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5765436861742d47726f75702d3037633136303f7374796c653d666f722d7468652d6261646765266c6f676f3d776563686174266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)](https://github.com/HKUDS/VideoAgent/blob/main/Communication.md)

[![](https://camo.githubusercontent.com/540fce265156df0bad295b05431688bc7bbfcc46bb6dcd8af22147d84790cb0b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d323630362e32333332372d6233316231623f7374796c653d666f722d7468652d6261646765266c6f676f3d6172786976266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)](https://arxiv.org/pdf/2606.23327)

[![HKUDS%2FVideoAgent | Trendshift](https://camo.githubusercontent.com/f6c23b635b569e986df2be17470aee9dff357c59179a59848f6d7c39e35a430e/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3138353438)](https://trendshift.io/repositories/18548)

[English](https://github.com/HKUDS/VideoAgent/blob/main/readme.md) \| [简体中文](https://github.com/HKUDS/VideoAgent/blob/main/readme_zh.md)

* * *

## 📹 **Demo Video**

[Permalink: 📹 Demo Video](https://github.com/HKUDS/VideoAgent#-demo-video)

[![](https://github.com/HKUDS/VideoAgent/raw/main/assets/overview.png)](https://www.youtube.com/watch?v=JZkXO1NG2Ok)

In this video, we demonstrate how to use VideoAgent to:

- Clearly articulate user requirements
- Achieve ​intent analysis and ​autonomous tool use & planning
- Create ​multi-modal products, including detailed workflows
- Fully automatic generation of video overview

## 🚀 Key Features

[Permalink: 🚀 Key Features](https://github.com/HKUDS/VideoAgent#-key-features)

🧠 \- **Understanding Video Content**

Enable in-depth analysis, summarization, and insight extraction from video media with advanced multi-modal intelligence capabilities.

✂️ \- **Editing Video Clips**

Provide intuitive tools for assembling, clipping, and reconfiguring content with seamless workflow integration.

🎨 \- **Remaking Creative Videos**

Utilize generative technologies to produce new, imaginative video content through AI-powered creative assistance.

🔧 \- **Multi-Modal Agentic Framework**

Deliver comprehensive video intelligence through an integrated framework that combines multiple AI modalities for enhanced performance.

🚀 \- **Seamless Natural Language Experience**

Transform video interaction and creation through pure conversational AI - no complex interfaces or technical expertise required, just natural dialogue with VideoAgent.

Render

🎬 VideoAgent Framework

🧠 Video Understanding & Summarization

✂️ Video Editing

🎨 VIdeo Remaking

Video Q&A

Video Summarization

Movie Edits

Commentary Video

Video Overview

Meme Videos

Music Videos

Cross-Cultural Comedy

Loading

```
graph TB
    A[🎬 VideoAgent Framework] --> B[🧠 Video Understanding & Summarization]
    A --> C[✂️ Video Editing]
    A --> D[🎨 VIdeo Remaking]

    B --> B1[Video Q&A]
    B --> B2[Video Summarization]

    C --> C1[Movie Edits]
    C --> C2[Commentary Video]
    C --> C3[Video Overview]

    D --> D1[Meme Videos]
    D --> D2[Music Videos]
    D --> D3[Cross-Cultural Comedy]
```

|  | VideoAgent | Director | Funclip | NarratoAI | NotebookLM |
| :-: | :-: | :-: | :-: | :-: | :-: |
| Beat-synced Edits | ✅ | ✅ | ✅ | — | — |
| Storytelling Video | ✅ | — | — | — | — |
| Video Overview | ✅ | ✅ | ✅ | ✅ | ✅ |
| Meme Video Remaking | ✅ | — | — | — | — |
| Song Remixes | ✅ | — | — | — | — |
| Cross-lingual Adaptations | ✅ | — | — | — | — |
| Video Q&A | ✅ | ✅ | — | — | ✅ |
| Sound Effects Tools | ✅ | — | — | — | — |

* * *

## 📑 Table of Contents

[Permalink: 📑 Table of Contents](https://github.com/HKUDS/VideoAgent#-table-of-contents)

- [🌟 System Overview](https://github.com/HKUDS/VideoAgent#system-overview)
- [🔧 Evaluation](https://github.com/HKUDS/VideoAgent#evaluation)
- [🚀 Quick Start](https://github.com/HKUDS/VideoAgent#quick-start)
- [🔮 Demos](https://github.com/HKUDS/VideoAgent#demos)
- [💖 Acknowledgments](https://github.com/HKUDS/VideoAgent#acknowledgments)

### 🔥 **Why VideoAgent?**

[Permalink: 🔥 Why VideoAgent?](https://github.com/HKUDS/VideoAgent#-why-videoagent)

| 🧠 **Easy-to-Use** | 🚀 **Boundless Creativity** | 🎨 **High-Quality** |
| :-: | :-: | :-: |
| One-Prompt Video Creation | Create From Any Ideas | Human-Quality Video Production |
| Transform your ideas into professional videos | Workflow generation for your unique ideas | Deliver videos that meet professional standards |

* * *

## 🌟System Overview

[Permalink: 🌟System Overview](https://github.com/HKUDS/VideoAgent#system-overview)

Our system introduces three key innovations for automated video processing. **Intent Analysis** captures both explicit and implicit sub-intents beyond user commands. **Autonamous Tool Use & Planning** employs graph-powered workflow generation with adaptive feedback loops for automated agent orchestration. **Multi-Modal Understanding** transforms raw input into semantically aligned visual queries for enhanced retrieval.

### 🧠 **Intent Analysis**

[Permalink: 🧠 Intent Analysis](https://github.com/HKUDS/VideoAgent#-intent-analysis)

- 🔍 VideoAgent intelligently **decomposes user instructions** into both **explicit and implicit sub-intents**, capturing nuanced requirements that users may not explicitly state. This advanced parsing ensures **comprehensive understanding** of user goals beyond surface-level commands.

- 🎯 Through an **intent-to-agent mapping mechanism**, the system identifies precisely which capabilities within the multi-agent framework are needed. This targeted approach enables **efficient activation** of relevant system components while avoiding unnecessary computational overhead for **optimal task execution**.


### 🔧 **Autonomous Tool Use & Planning**

[Permalink: 🔧 Autonomous Tool Use & Planning](https://github.com/HKUDS/VideoAgent#-autonomous-tool-use--planning)

- ⚙️ **A graph-powered framework** automatically translates user intents into **executable workflows**. The system dynamically selects appropriate agents and constructs optimal execution sequences. Nodes represent tool capabilities while edges define workflow connections for complex video tasks.

- 🔄 Adaptive feedback loops continuously refine the planning process through **two-step self-evaluation**. This ensures robust **automated decision-making** and seamless execution. The system **self-corrects** and optimizes performance throughout the entire task lifecycle.


### 🎬 **Multi-Modal Understanding**

[Permalink: 🎬 Multi-Modal Understanding](https://github.com/HKUDS/VideoAgent#-multi-modal-understanding)

- 📋 **The Storyboard Agent** transforms raw user input into **optimized visual queries**. It first analyzes pre-captioned video material banks to understand available resources. This foundational analysis ensures the system knows exactly what content is accessible for query processing.

- 💡 The agent then **decomposes user input** into **fine-grained sub-queries** that are both visually and semantically aligned. This sophisticated breakdown enables **enhanced video retrieval** by matching user intentions with the most relevant visual content in the database.


[![](https://github.com/HKUDS/VideoAgent/raw/main/assets/framework.jpg)](https://github.com/HKUDS/VideoAgent/blob/main/assets/framework.jpg)

* * *

## 🔧Evaluation

[Permalink: 🔧Evaluation](https://github.com/HKUDS/VideoAgent#evaluation)

We conduct extensive experiments across multiple dimensions to validate the effectiveness of VideoAgent in addressing key challenges.

### Boundless Creativity via Workflow Construction

[Permalink: Boundless Creativity via Workflow Construction](https://github.com/HKUDS/VideoAgent#boundless-creativity-via-workflow-construction)

To evaluate VideoAgent's **boundless creativity** through automatic workflow construction, we compared five broadly applicable agents across three backbone models. Our findings demonstrate that VideoAgent significantly outperforms other baselines on the Audio and Video datasets, showcasing its **creative workflow generation capabilities** through graph-structured guidance and self-reflection driven by dedicated self-evaluation feedback. Furthermore, we observe that VideoAgent exhibits superior and more stable **creative performance** under the Claude 3.7 backbone compared to GPT-4o and Deepseek-v3, while other baseline methods show fluctuations across different backbones. This highlights VideoAgent's ability to **unleash boundless creativity** by automatically constructing diverse and effective workflows that adapt to various user requirements, with more capable LLMs achieving deeper comprehension and providing more robust creative solutions for complex graph-based tasks.

[![](https://github.com/HKUDS/VideoAgent/raw/main/assets/eval1_audio_new.png)](https://github.com/HKUDS/VideoAgent/blob/main/assets/eval1_audio_new.png)

[![](https://github.com/HKUDS/VideoAgent/raw/main/assets/eval1_video_new.png)](https://github.com/HKUDS/VideoAgent/blob/main/assets/eval1_video_new.png)

### Superior Multimodal Understanding

[Permalink: Superior Multimodal Understanding](https://github.com/HKUDS/VideoAgent#superior-multimodal-understanding)

To validate our multimodal understanding capabilities, we conducted text-to-video retrieval experiments using shuffled caption queries. The evaluation employs three metrics to assess our model's ability to retrieve corresponding visual content: Recall measures the model's ability to correctly reorder shuffled video clips by comparing retrieved clip midpoints against ground truth positions; Embedding Matching-based score assesses coarse-grained alignment between generated videos and high-level caption summaries; and Intersection over Union quantifies temporal alignment accuracy at the clip level by computing the ratio of temporal overlap to total coverage between retrieved and ground truth intervals. The experimental results demonstrate that our approach can retrieve more accurate video segments, thereby showcasing our precise multimodal understanding capabilities.

[![](https://github.com/HKUDS/VideoAgent/raw/main/assets/eva2.png)](https://github.com/HKUDS/VideoAgent/blob/main/assets/eva2.png)

### More Iterations, Better Performance

[Permalink: More Iterations, Better Performance](https://github.com/HKUDS/VideoAgent#more-iterations-better-performance)

We investigate VideoAgent's iterative refinement capabilities by analyzing the impact of reflection rounds on performance. Through comprehensive hyperparameter experiments on workflow composition across two datasets using three LLM backbones, we demonstrate VideoAgent's **notable self-improvement ability**. The results reveal that while early iterations produce baseline results, our system's **adaptive reflection mechanism** drives significant performance gains with each subsequent round. VideoAgent achieves **consistent workflow composition success rates of 0.95** across all tested configurations, showcasing its **robust self-correction capabilities** and **reliable high-quality output** regardless of the underlying LLM backbone.

[![](https://github.com/HKUDS/VideoAgent/raw/main/assets/eva3.jpg)](https://github.com/HKUDS/VideoAgent/blob/main/assets/eva3.jpg)[![](https://github.com/HKUDS/VideoAgent/raw/main/assets/eva4.jpg)](https://github.com/HKUDS/VideoAgent/blob/main/assets/eva4.jpg)

* * *

## 🚀Quick Start

[Permalink: 🚀Quick Start](https://github.com/HKUDS/VideoAgent#quick-start)

### 🖥️ **Environment**

[Permalink: 🖥️ Environment](https://github.com/HKUDS/VideoAgent#%EF%B8%8F-environment)

```
GPU Memory: 8GB
OS: Linux, Windows
```

### 📥 **Clone and Install**

[Permalink: 📥 Clone and Install](https://github.com/HKUDS/VideoAgent#-clone-and-install)

```
git clone https://github.com/HKUDS/VideoAgent.git
conda create --name videoagent python=3.10
conda activate videoagent
conda install -y -c conda-forge pynini==2.1.5 ffmpeg
pip install -r requirements.txt
```

### 📦 **Model Download**

[Permalink: 📦 Model Download](https://github.com/HKUDS/VideoAgent#-model-download)

```
# Download CosyVoice
cd tools/CosyVoice
huggingface-cli download PillowTa1k/CosyVoice --local-dir pretrained_models
```

```
# Download fish-speech
cd tools/fish-speech
huggingface-cli download fishaudio/fish-speech-1.5 --local-dir checkpoints/fish-speech-1.5
```

```
# Download seed-vc
cd tools/seed-vc
huggingface-cli download PillowTa1k/seed-vc --local-dir checkpoints
```

```
# Download DiffSinger
cd tools/DiffSinger
huggingface-cli download PillowTa1k/DiffSinger --local-dir checkpoints
```

```
# Download Whisper
cd tools
huggingface-cli download openai/whisper-large-v3-turbo --local-dir whisper-large-v3-turbo
```

```
# Make sure git-lfs is installed (https://git-lfs.com)
git lfs install
```

```
# Download ImageBind
cd tools
mkdir .checkpoints
cd .checkpoints
wget https://dl.fbaipublicfiles.com/imagebind/imagebind_huge.pth
```

**🌟 Multiple models are available for your convenience; you may wish to download only those relevant to your project.**

| Feature Type | Video Demo | Required Models |
| :-: | :-: | :-: |
| Cross Talk | English Stand-up Comedy to Chinese Crosstalk | CosyVoice, Whisper, ImageBind |
| Talk Show | Chinese Crosstalk to English Stand-up Comedy | CosyVoice, Whisper, ImageBind |
| MAD TTS | Xiao-Ming-Jian-Mo(小明剑魔) Meme | fish-speech |
| MAD SVC | AI Music Videos | DiffSinger, seed-vc, Whisper, ImageBind |
| Rhythm | Spider-Man: Across the Spider-Verse | Whisper, ImageBind |
| Comm | Commentary Video | CosyVoice, Whisper, ImageBind |
| News | Tech News: OpenAI's GPT-4o Image Generation Release | CosyVoice, Whisper, ImageBind |
| Video QA/Summarization | Dune 2 Movie Cast Update Podcast | Whisper |

### 🤖 **LLM Configuration**

[Permalink: 🤖 LLM Configuration](https://github.com/HKUDS/VideoAgent#-llm-configuration)

```
# VideoAgent\environment\config\config.yml
# Applicable scenarios and LLM configuration
# Claude is required as it powers the Agentic Graph Router
llm:
  # Video Remixing/TTS/SVC/Stand-up/CrossTalk
  deepseek_api_key: ""
  deepseek_base_url: ""

  # Agentic Graph Router/TTS/SVC/Stand-up/CrossTalk
  claude_api_key: ""
  claude_base_url: ""

  # Video Editing/Overview/Summarization/QA/Commentary Video
  gpt_api_key: ""
  gpt_base_url: ""

  # MLLM for caption and fine-grained video understanding
  gemini_api_key: ""
  gemini_base_url: ""
```

### 🎯 **Usage**

[Permalink: 🎯 Usage](https://github.com/HKUDS/VideoAgent#-usage)

```
# With the configuration now complete, proceed to run the following instructions:
python main.py
# The console will output:
User Requirement: ...
# Requirement Example:
# 1. I need to create a reworded version of an existing video where the speech content is modified while maintaining the original speaker's voice. The video should have the same visuals as the original, but with updated dialogue that follows my specific requirements.
# 2. I have a standup comedy script that I'd like to turn into a professional-looking video. I need the script to be performed with good comedic timing and audience reactions, then matched with relevant video footage to create a complete standup comedy special. I already have a reference script and some footage I want to use for the video.
```

The current LLM selections are optimized for each function.

You can also adjust the model names in `VideoAgent\environment\config\llm.py` if needed.

* * *

## 🔮Demos

[Permalink: 🔮Demos](https://github.com/HKUDS/VideoAgent#demos)

|     |     |     |
| --- | --- | --- |
| [![](https://github.com/HKUDS/VideoAgent/raw/main/assets/spiderman_cover.png)](https://www.bilibili.com/video/BV1C9Z6Y3ESo/)<br>Movie Edits | [![](https://github.com/HKUDS/VideoAgent/raw/main/assets/masterma_cover.png)](https://www.bilibili.com/video/BV1ucZ6YmEBU/)<br>Meme Videos | [![](https://github.com/HKUDS/VideoAgent/raw/main/assets/airencuoguo_cover.png)](https://www.bilibili.com/video/BV1t8ZCYsEeA/)<br>Music Videos |
| [![](https://github.com/HKUDS/VideoAgent/raw/main/assets/adapted_crosstalk_cover.png)](https://www.bilibili.com/video/BV1ucZ6YmESg/)<br>Verbal Comedy Arts | [![](https://github.com/HKUDS/VideoAgent/raw/main/assets/joylife_cover.png)](https://www.bilibili.com/video/BV1TmZ6YjEvV/)<br>Commentary Video | [![](https://github.com/HKUDS/VideoAgent/raw/main/assets/openai_news_cover.png)](https://www.bilibili.com/video/BV12mZ6YLEqW/)<br>Video Overview |

For additional demo usage details, please refer to:

👉 [Demos Documentation](https://github.com/HKUDS/VideoAgent/blob/main/demos_documents.md)

You can find more fun videos on our Bilibili channel here:

👉 [Bilibili Homepage](https://space.bilibili.com/3546868449544308)

Feel free to check it out for more entertaining content! 😊

**Note**: All videos are used for research and demonstration purposes only. The audio and visual assets are sourced from the Internet. Please contact us if you believe any content infringes upon your intellectual property rights.

* * *

## 💖 **Acknowledgments**

[Permalink: 💖Acknowledgments](https://github.com/HKUDS/VideoAgent#acknowledgments)

We express our deepest gratitude to the numerous individuals and organizations that have made VideoAgent possible. This framework stands on the shoulders of giants, benefiting from the collective wisdom of the open-source community and the groundbreaking work of researchers worldwide.

### 🔧 **Open-Source Community and Service Providers**

[Permalink: 🔧 Open-Source Community and Service Providers](https://github.com/HKUDS/VideoAgent#-open-source-community-and-service-providers)

- [CosyVoice](https://github.com/FunAudioLLM/CosyVoice)
- [Fish Speech](https://github.com/fishaudio/fish-speech)
- [Seed-VC](https://github.com/Plachtaa/seed-vc)
- [DiffSinger](https://github.com/MoonInTheRiver/DiffSinger)
- [VideoRAG](https://github.com/HKUDS/VideoRAG)
- [ImageBind](https://github.com/facebookresearch/ImageBind)
- [Whisper](https://github.com/openai/whisper)
- [Librosa](https://github.com/librosa/librosa)

### 🎨 **Content Creators and Inspiration**

[Permalink: 🎨 Content Creators and Inspiration](https://github.com/HKUDS/VideoAgent#-content-creators-and-inspiration)

Our work has been significantly enriched by the creative contributions of content creators across various platforms. We acknowledge:

- 🎬 **Content Creators**: The talented creators behind the original video content used for testing and demonstration
- 🎭 **Comedy Artists**: Those whose work inspired our cross-cultural adaptations
- 🎥 **Filmmakers**: The production teams behind the movies and TV shows featured in our demos

**⚠️ Note**: All content used in our demonstrations is for research purposes only. We deeply respect the intellectual property rights of all content creators and welcome any concerns or feedback regarding content usage.

* * *

![Visitors](https://camo.githubusercontent.com/a817a4e1e680855aa65724ee619e2e4c3fcd685e8ee6b95dbd13d0a5a313f6ad/68747470733a2f2f76697369746f722d62616467652e6c616f62692e6963752f62616467653f706167655f69643d484b5544532e4f70656e2d4e6f7465626f6f6b4c4d267374796c653d666f722d7468652d626164676526636f6c6f723d303064346666)

## About

\[EMNLP2026\] "VideoAgent: All-in-One Agentic Framework for Video Understanding and Editing, and Remaking"

[arxiv.org/abs/2606.23327](https://arxiv.org/abs/2606.23327)

### Topics

[agents](https://github.com/topics/agents) [audio-editing](https://github.com/topics/audio-editing) [audio-understanding](https://github.com/topics/audio-understanding) [llm-agents](https://github.com/topics/llm-agents) [notebooklm](https://github.com/topics/notebooklm) [podcast](https://github.com/topics/podcast) [video-editing](https://github.com/topics/video-editing) [video-understanding](https://github.com/topics/video-understanding)

### Resources

[Readme](https://github.com/HKUDS/VideoAgent#readme-ov-file)

[MIT license](https://github.com/HKUDS/VideoAgent#MIT-1-ov-file)

[Activity](https://github.com/HKUDS/VideoAgent/activity)

[Custom properties](https://github.com/HKUDS/VideoAgent/custom-properties)

### Stars

**1.9k** stars

### Watchers

**17** watching

### Forks

[**243** forks](https://github.com/HKUDS/VideoAgent/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FHKUDS%2FVideoAgent&report=HKUDS+%28user%29)

## [Releases](https://github.com/HKUDS/VideoAgent/releases)

No releases published

## [Contributors](https://github.com/HKUDS/VideoAgent/graphs/contributors) 7 (7)

- [![@xvrrr](https://avatars.githubusercontent.com/u/83233211?s=64&v=4)](https://github.com/xvrrr)
- [![@Hengji-cs](https://avatars.githubusercontent.com/u/177777906?s=64&v=4)](https://github.com/Hengji-cs)
- [![@akaxlh](https://avatars.githubusercontent.com/u/18502814?s=64&v=4)](https://github.com/akaxlh)
- [![@chaohuang-ai](https://avatars.githubusercontent.com/u/204865953?s=64&v=4)](https://github.com/chaohuang-ai)
- [![@LarFii](https://avatars.githubusercontent.com/u/49157727?s=64&v=4)](https://github.com/LarFii)
- [![@claude](https://avatars.githubusercontent.com/u/81847?s=64&v=4)](https://github.com/claude)
- [![@hobostay](https://avatars.githubusercontent.com/u/110803307?s=64&v=4)](https://github.com/hobostay)

## Languages

- [Python98.3%](https://github.com/HKUDS/VideoAgent/search?l=python)
- [Shell0.7%](https://github.com/HKUDS/VideoAgent/search?l=shell)
- [Cuda0.4%](https://github.com/HKUDS/VideoAgent/search?l=cuda)
- [C0.3%](https://github.com/HKUDS/VideoAgent/search?l=c)
- [Jupyter Notebook0.2%](https://github.com/HKUDS/VideoAgent/search?l=jupyter-notebook)
- [Dockerfile0.1%](https://github.com/HKUDS/VideoAgent/search?l=dockerfile)

You can’t perform that action at this time.