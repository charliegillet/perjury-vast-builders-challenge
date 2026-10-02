[Back to Articles](https://huggingface.co/blog)

# Welcome NVIDIA Cosmos 3: The First Open Omni-model for Physical AI Reasoning and Action

[Community Article](https://huggingface.co/blog/community)

Published
June 1, 2026

[Upvote \\
\\
90](https://huggingface.co/login?next=%2Fblog%2Fnvidia%2Fcosmos-3-for-physical-ai)

- [![](https://huggingface.co/avatars/dcf870695fd56b06ca03d82f831e9019.svg)](https://huggingface.co/luotto "luotto")
- [![](https://cdn-avatars.huggingface.co/v1/production/uploads/no-auth/bXjlRMppUn4uOwKSE8jmM.png)](https://huggingface.co/dwjoeikr "dwjoeikr")
- [![](https://huggingface.co/avatars/d92eb2dedaa6a93abca22533d7fca37e.svg)](https://huggingface.co/adiasg "adiasg")
- [![](https://huggingface.co/avatars/f8ec95d43353cadcd78b4a713918364b.svg)](https://huggingface.co/rakeshtanwar "rakeshtanwar")
- [![](https://huggingface.co/avatars/9a4f6a5a7c26c9cfcc9521fe43699eca.svg)](https://huggingface.co/ch-min "ch-min")
- [![](https://cdn-avatars.huggingface.co/v1/production/uploads/1605114051380-noauth.jpeg)](https://huggingface.co/jeffboudier "jeffboudier")
- +84

[![Asawaree's avatar](https://huggingface.co/avatars/c1eb1024a4c6bd1296884ff17b0e0cbf.svg)](https://huggingface.co/asawareeb)

[Asawaree\\
asawareeb\\
\\
Follow](https://huggingface.co/asawareeb)

[![NVIDIA's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/65df9200dc3292a8983e5017/Vs5FPVCH-VZBipV3qKTuy.png)](https://huggingface.co/nvidia "NVIDIA")[nvidia](https://huggingface.co/nvidia)

[![Atharva Joshi's avatar](https://huggingface.co/avatars/f9457fe82d4eb589c317bc855a5c2c68.svg)](https://huggingface.co/atharvajoshi10)

[Atharva Joshi\\
atharvajoshi10\\
\\
Follow](https://huggingface.co/atharvajoshi10)

[![NVIDIA's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/65df9200dc3292a8983e5017/Vs5FPVCH-VZBipV3qKTuy.png)](https://huggingface.co/nvidia "NVIDIA")[nvidia](https://huggingface.co/nvidia)

[NVIDIA Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) is here - and it's available on [Hugging Face](https://huggingface.co/collections/nvidia/cosmos3) today. Cosmos 3 represents a major leap forward in [world foundation models](https://www.nvidia.com/en-us/glossary/world-models/) (WFMs) for physical AI: a single, unified omni-model that combines world generation, physical reasoning, and action generation in one model. No more juggling between different models and inference pipelines - Cosmos 3 does it all.

Whether you're building for robotics, autonomous vehicles, or smart spaces, Cosmos 3 gives you the foundation to simulate and understand the physical world.

Here's what's shipping with this release:

- Cosmos 3 Super and Cosmos 3 Nano on Hugging Face with model cards and licensing
- Cosmos 3 Diffusers integration for generation pipelines
- Post-training scripts for training Cosmos 3 on your own data (on GitHub)
- Open synthetic data generation (SDG) datasets for physical AI

**TABLE OF CONTENTS**

1. [What's new with Cosmos 3?](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai#section-1-whats-new-with-cosmos-3)
2. [Cosmos 3 Capabilities](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai#section-2-cosmos-3-capabilities)
3. [Using Cosmos 3 with Diffusers](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai#section-3-using-cosmos-3-with-diffusers)
4. [Datasets for physical AI](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai#section-4-datasets-for-physical-ai)
5. [Cosmos Framework](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai#section-5-cosmos-framework)
6. [Resources](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai#section-6-resources)

### SECTION 1: What's new with Cosmos 3?

The biggest change in Cosmos 3 compared to previous Cosmos releases is that it's an omni-model, built on a Mixture-of-Transformers (MoT) architecture. Previously, developers had to work with separate models for different capabilities like world generation (Cosmos Predict), controlled generation (Cosmos Transfer), scene understanding (Cosmos Reason) and policy generation (Cosmos Policy). Cosmos 3 enables all of this in a single model that can reason and generate different modalities in one unified forward pass.

This means you can now do all this from one model:

- Generate realistic and physically plausible video worlds from text, images, videos or action inputs
- Reason about physical properties like motion, causality, and spatial relationships
- Predict future video and action sequences based on the current state

**Why this matters for physical AI**

Cosmos 3 helps build physical AI systems capable of understanding the real world. Not just pixels and tokens, but motion, causality, physics, and action. If you're training a robot to fold laundry, building an autonomous driving simulation, or generating synthetic training data for warehouse safety scenarios, Cosmos 3 is the foundation model designed for exactly these use-cases.

![](https://cdn-uploads.huggingface.co/production/uploads/6799309995f2227228bc38f3/Wcx8G3cD6e3tib-Zj4Ryw.gif)
Video generated by Cosmos 3 for robotics pick and place use-cases.

![](https://cdn-uploads.huggingface.co/production/uploads/6799309995f2227228bc38f3/FP6Mh3FqTyThuZ_RN4mt4.gif)
Video generated by Cosmos 3 for long tail driving scenarios.

![](https://cdn-uploads.huggingface.co/production/uploads/6799309995f2227228bc38f3/WgIJWLbDhavkxYV8mBYjh.gif)
Image-to-video generation using Cosmos 3 for warehouse safety data.

![](https://cdn-uploads.huggingface.co/production/uploads/6799309995f2227228bc38f3/g06bFosM9Br-cwgfmt7cl.png)
Cosmos 3 chain-of-thought reasoning in an autonomous driving application.

**Architecture**

Cosmos 3 is built on an MoT backbone that processes all modalities - text, image, video, audio, and action - within a single unified architecture. Each modality is first encoded by a dedicated encoder (a ViT for visual understanding, a VAE for visual/audio generation, and domain-aware vectors for actions), then projected into a shared representation space.

![cosmos3-architecture-diagram](https://cdn-uploads.huggingface.co/production/uploads/6799309995f2227228bc38f3/IBreD1akJz8T47xKva3_B.png)

The input sequence is split into two subsequences: an autoregressive (AR) subsequence that handles reasoning and understanding via next-token prediction, and a diffusion (DM) subsequence that handles generation via iterative denoising. AR and DM tokens use separate parameter sets within each transformer layer but interact through joint attention - this is what lets a single model seamlessly switch between acting as a VLM, a video generator, a forward/inverse dynamics model, or a robot policy without any architectural changes.

**Model Versions**

This release of Cosmos 3 includes two model sizes, optimized for different deployment scenarios:

- **Cosmos 3 Nano** \- This is the 16B parameter model (8B reasoner and 8B generator), optimized for efficient inference. Cosmos 3 Nano is designed to run on workstation-grade compute like the RTX PRO 6000 GPU, and is available on Hugging Face at [nvidia/Cosmos3-Nano](http://huggingface.co/nvidia/Cosmos3-Nano).
- **Cosmos 3 Super** \- This is the 64B parameter model (32B reasoner and 32B generator) designed for large-scale synthetic data generation (SDG) and research, and runs on NVIDIA Hopper and Blackwell GPUs. Cosmos 3 Super is available on Hugging Face at [nvidia/Cosmos3-Super](http://huggingface.co/nvidia/Cosmos3-Super).

### SECTION 2: Cosmos 3 Capabilities

Cosmos 3 supports multiple input and generation modalities through a single unified model:

| **Input Modality** | **Output Modality** | **Application** |
| :-: | :-: | :-: |
| Text \| Image \| Video | Video | Video Model |
| Text \| Video | Text | Vision Language Model (VLM) |
| Action \| Image \| Text | Video | Forward Dynamics Model |
| Text \| Video | Action | Inverse Dynamics Model |
| Image \| Text | Video & Action | Policy Model |

**Prompt Guide**

For video generation, we recommend using detailed prompts in the form of narrative paragraphs. For example:

> The video begins with a view from inside a vehicle traveling on a multi-lane highway under a clear blue sky. The road is bordered by dense green trees on both sides, creating a tranquil environment. Several vehicles, including a prominent white semi-truck and various cars, are visible ahead, maintaining a steady pace. The highway features multiple lanes separated by concrete barriers, and the scene is bathed in bright sunlight, indicating a clear day. As the video progresses, a large amount of debris suddenly appears on the lane ahead. With little time to avoid it, the ego vehicle has to drive over the debris and continue moving forward. A noticeable jolt occurs as the ego vehicle passes over the scattered objects. A point-of-view shot from inside the vehicle, capturing the road ahead and the surrounding environment.

For action generation, prompts should be concise and provide spatial references. For example:

> Put the pot to the left of the purple item. This video is captured from a first-person perspective looking at the scene.

Find the prompt upsampling template, and best practices for writing high-quality prompts in the prompting guide on GitHub.

### SECTION 3: Using Cosmos 3 with Diffusers

Cosmos 3 is integrated with the Hugging Face Diffusers library, making it easy to use world generation pipelines with just a few lines of code. You can run Cosmos 3 through the familiar DiffusionPipeline via _Cosmos3OmniPipeline_. With this, the goal is enabling frictionless adoption of Cosmos 3 and integration with your existing pipelines.

Let's see a Text-to-Image example for single frame generation using the Cosmos 3 Nano model:

```python
import torch
from diffusers import Cosmos3OmniPipeline

pipe = Cosmos3OmniPipeline.from_pretrained(
    "nvidia/Cosmos3-Nano", torch_dtype=torch.bfloat16, device_map="cuda"
)

prompt = (
    "A medium shot of a modern robotics research laboratory with white walls and a gray floor. "
    "A robotic arm with a metallic finish is mounted on a clean white workbench, its gripper positioned "
    "above a row of small colored objects. A laptop and neatly arranged tools sit beside the robot. "
    "A large monitor on the wall behind displays a software interface. The scene is brightly lit by "
    "overhead fluorescent lights."
)

result = pipe(prompt=prompt, num_frames=1, height=720, width=1280)
result.video[0].save("cosmos3_t2i.jpg", format="JPEG", quality=85)
```

Here's the image generated by the Cosmos 3 Nano model and given prompt:

![](https://cdn-uploads.huggingface.co/production/uploads/6799309995f2227228bc38f3/J7F5Kov02E21Tx1A21ZcB.jpeg)

The documentation also has examples on Text-to-Video, Image-to-Video and more. Find information and API usage in the [Cosmos 3 Diffusers documentation](https://huggingface.co/docs/diffusers/main/en/api/pipelines/cosmos3).

### SECTION 4: Datasets for physical AI

As part of the Cosmos 3 launch, NVIDIA is releasing a set of Synthetic Data Generation (SDG) datasets to help the physical AI community train and evaluate world foundation models. These datasets were generated by various NVIDIA teams and are available on Hugging Face.

| **Dataset** | **Domain** | **Description** |
| :-: | :-: | :-: |
| [Embodied-Robot-Scenes](http://huggingface.co/datasets/nvidia/PhysicalAI-SDG-RobotSim) | Robotics | Synthetic robot simulation data |
| [Physical-Interaction-Scenes](http://huggingface.co/datasets/nvidia/PhysicalAI-SDG-PhysxSim) | Physics | Isaac Sim physics simulation data |
| [Digital-Human-Scenes](http://huggingface.co/datasets/nvidia/PhysicalAI-SDG-SynHuman) | Human motion | Synthetic human motion data |
| [Autonomous-Driving-Scenarios](http://huggingface.co/datasets/nvidia/PhysicalAI-SDG-DriveSim) | Driving | Driving simulation data |
| [Warehouse-Operations-Scenes](http://huggingface.co/datasets/nvidia/PhysicalAI-SDG-WareHouse) | Warehouse safety | Warehouse environment data |

### Section 5: Cosmos Framework

[Cosmos Framework](https://github.com/NVIDIA/Cosmos-Framework) is an end-to-end framework for training and serving WFMs like Cosmos 3. This is where you'll find inference and post-training scripts, and agent skills for development.

**Post-training Cosmos 3**

Cosmos 3 understands and generates world videos and actions for robotics, autonomous vehicles, and smart spaces out of the box, but some applications may require further post-training on specific datasets to get the best results. We encourage post-training Cosmos 3 for different robots, environments, and tasks - check out the post-training guide in the repo.

**Agent Skills**

The repo also comes with agent skills to make development fast and easy. These skills help validate requirements, and set up the environment with dependencies. You can also use them for learning about the repo structure and examples, drafting good prompts, or running the inference and post-training scripts.

### SECTION 6: Resources

Read the [Cosmos 3 technical blog](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3) to learn about Cosmos 3 capabilities, performance, post-training, and deployment with NIM microservices.

- [Cosmos 3 GitHub](https://github.com/nvidia/Cosmos)
- [Cosmos 3 NIM microservices](https://build.nvidia.com/models?q=cosmos)
- [Cosmos Cookbook](https://nvidia-cosmos.github.io/cosmos-cookbook/)
- [Cosmos Page](https://www.nvidia.com/en-us/ai/cosmos/)
- [Cosmos 3 Technical Paper](https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf)
- [Diffusers Cosmos Documentation](https://huggingface.co/docs/diffusers/main/en/api/pipelines/cosmos3)

### Acknowledgments

Cosmos 3 is the result of amazing collaboration between many teams and people across NVIDIA, including -

Aditi, Niket Agarwal, Arslan Ali, Jon Allen, Martin Antolini, Adeline Aubame, Alisson Azzolini, Junjie Bai, Maciej Bala, Yogesh Balaji, Josh Bapst, Aarti Basant, Mukesh Beladiya, Mohammad Qazim Bhat, Zaid Pervaiz Bhat, Dan Blick, Vanni Brighella, Han Cai, Tiffany Cai, Eric Cameracci, Jiaxin Cao, Yulong Cao, Mark Carlson, Carlos Casanova, Ting-Yun Chang, Yan Chang, Yu-Wei Chao, Prithvijit Chattopadhyay, Roshan Chaudhari, Chieh-Yun Chen, Junyu Chen, Ke Chen, Qizhi Chen, Wenkai Chen, Xiaotong Chen, Yu Chen, An-Chieh Cheng, Click Cheng, Xiu Chia, Jeana Choi, Chaeyeon Chung, Wenyan Cong, Yin Cui, Magdalena Dadela, Nalin Dadhich, Wenliang Dai, Joyjit Daw, Alperen Degirmenci, Rodrigo Vieira Del Monte, Robert Denomme, Sameer Dharur, Marco Di Lucca, Ke Ding, Wenhao Ding, Yifan Ding, Yuzhu Dong, Nicole Drumheller, Yilun Du, Aigul Dzhumamuratova, Aleksandr Efitorov, Hamid Eghbalzadeh, Naomi Eigbe, Imad El Hanafi, Hassan Eslami, Benedikt Falk, Jiaojiao Fan, Jim Fan, Amol Fasale, Sergiy Fefilatyev, Liang Feng, Francesco Ferroni, Sanja Fidler, Xiao Fu, Vikram Fugro, Prashant Gaikwad, TJ Galda, Katelyn Gao, Yihuai Gao, Wenhang Ge, Sreyan Ghosh, Arushi Goel, Vivek Goel, Akash Gokul, Rama Govindaraju, Jinwei Gu, Miguel Guerrero, Elfie Guo, Aryaman Gupta, Siddharth Gururani, Hugo Hadfield, Song Han, Ankur Handa, Zekun Hao, Mohammad Harrim, Ali Hassani, Nathan Hayes-Roth, Yufan He, Chris Helvig, Cyrus Hogg, Madison Huang, Michael Huang, Sophia Huang, Yufan Huang, Jacob Huffman, DeLesley Hutchins, Suneel Indupuru, Boris Ivanovic, Arihant Jain, Joel Jang, Ryan Ji, Yanan Jian, Dongfu Jiang, Jingyi Jin, Atharva Joshi, Nikhilesh Joshi, Pranjali Joshi, Jaehun Jung, Weiwei Kang, Scott Kassekert, Jan Kautz, Ashna Khetan, Julia Kiczka, Slawek Kierat, Gwanghyun Kim, Kuno Kim, Sunny Kim, Kezhi Kong, Xin Kong, Zhifeng Kong, Tomasz Kornuta, Egor Krivov, Hui Kuang, Saurav Kumar, Chia-Wen Kuo, George Kurian, Wojciech Kutak, JF Lafleche, Himangshu Lahkar, Omar Laymoun, Jayjun Lee, Sanggil Lee, Gabriele Leone, Boyi Li, Freya Li, Jiajun Li, Jinfeng Li, Ling Li, Pengcheng Li, Shangru Li, Tingle Li, Xiaolong Li, Xuan Li, Zhaoshuo Li, Zhiqi Li, Hao Liang, Maosheng Liao, Chen-Hsuan Lin, Tsung-Yi Lin, Ming-Yu Liu, Sifei Liu, Zihan Liu, Hai Loc Lu, Xiangyu Lu, Alice Luo, Ruipu Luo, Wenjie Luo, Jiangran Lyu, Martin Ding Ma, Nic Ma, Qianli Ma, Dawid Majchrowski, Louis Marcoux, Miguel Martin, Qing Miao, Ashkan Mirzaei, Shreyas Misra, Kaichun Mo, Durra Mohsin, Hyejin Moon, Pawel Morkisz, Saeid Motiian, Kirill Motkov, Seungjun Nah, Yashraj Narang, Deepak Narayanan, Thabang Ngazimbi, Julian Ouyang, David Page, Yatian Pang, Sehwi Park, Mahesh Patekar, Mostofa Patwary, Marco Pavone, Trung Pham, Wei Ping, Soha Pouya, Shrimai Prabhumoye, Varun Praveen, Delin Qu, Hesam Rabeti, Morteza Ramezanali, Marilyn Reeb, Xuanchi Ren, Kristen Rumley, Wojciech Rymer, Jun Saito, Yeongho Seol, John Shao, Piyush Shekdar, Tianwei Shen, Humphrey Shi, Min Shi, Stella Shi, Kevin Shih, Mohammad Shoeybi, Mateusz Sieniawski, Shuran Song, Alex Sotelo, Amir Sotoodeh, Sunil Srinivasa, Vignesh Srinivasakumar, Bartosz Stefaniak, Rahul Heinrich Steiger, Shangkun Sun, Jiaxiang Tang, Shitao Tang, Yangyang Tang, Yue Tang, Tolou Tavakkoli, Kayley Ting, Krzysztof Tomala, Wei-Cheng Tseng, Jibin Varghese, Sergei Vasilev, Thomas Volk, Raju Wagwani, Roger Waleffe, Andrew Z. Wang, Boxiang Wang, Haoxiang Wang, Qiao Wang, Shihao Wang, Shijie Wang, Ting-Chun Wang, Yan Wang, Yu Wang, David Wehr, Fangyin Wei, Xinshuo Weng, Jay Zhangjie Wu, Kedi Wu, Hongchi Xia, Summer Xiao, Tianjun Xiao, Kevin Xie, Daguang Xu, Jiashu Xu, Mengyao Xu, Ruqing Xu, Xingqian Xu, Yao Xu, Dinghao Yang, Dong Yang, Hans Yang, Xiaodong Yang, Xuning Yang, Yichu Yang, Yurong You, Zhiding Yu, Hao Yuan, Simon Yuen, Xiaohui Zeng, Pengcuo Zeren, Cindy Zha, Haotian Zhang, Jenny Zhang, Jing Zhang, Liangkai Zhang, Paris Zhang, Shun Zhang, Xuanmeng Zhang, Zhizheng Zhang, Ann Zhao, Yilin Zhao, Yuliya Zhautouskaya, Charles Zhou, Fengzhe Zhou, Shilin Zhu, Yuke Zhu, Dima Zhylko, Artur Zolkowski.

## Models mentioned in this article 2

## Collections mentioned in this article 1

More from this author

[![](https://cdn-uploads.huggingface.co/production/uploads/684040a5de1ad7f4fcec9508/HyVlq-3d7EVj_M-m_TfHJ.png)\\
\\
**NVIDIA Kumo Tabular Sets a New Accuracy-Efficiency Frontier for Tabular Prediction**\\
\\
- ![](https://cdn-avatars.huggingface.co/v1/production/uploads/65df9200dc3292a8983e5017/Vs5FPVCH-VZBipV3qKTuy.png)\\
\\
46\\
\\
September 29, 2026\\
\\
nvidia](https://huggingface.co/blog/nvidia/kumo-tabular)

[![](https://cdn-uploads.huggingface.co/production/uploads/6994dc99f850a10f03fd0b21/rQ6tGCJEaH16bQQ8X4M8b.png)\\
\\
**How to Use NVIDIA Warp and MjWarp to Accelerate Robotics Simulation and Learning Workflows**\\
\\
- ![](https://cdn-avatars.huggingface.co/v1/production/uploads/65df9200dc3292a8983e5017/Vs5FPVCH-VZBipV3qKTuy.png)\\
\\
50\\
\\
September 23, 2026\\
\\
nvidia](https://huggingface.co/blog/nvidia/how-to-use-nvidia-warp-and-mjwarp)

### Community

EditPreview

Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.

Tap or paste here to upload images

Comment

· [Sign up](https://huggingface.co/join?next=%2Fblog%2Fnvidia%2Fcosmos-3-for-physical-ai) or [log in](https://huggingface.co/login?next=%2Fblog%2Fnvidia%2Fcosmos-3-for-physical-ai) to comment

[Upvote \\
\\
90](https://huggingface.co/login?next=%2Fblog%2Fnvidia%2Fcosmos-3-for-physical-ai)

- [![](https://huggingface.co/avatars/dcf870695fd56b06ca03d82f831e9019.svg)](https://huggingface.co/luotto "luotto")
- [![](https://cdn-avatars.huggingface.co/v1/production/uploads/no-auth/bXjlRMppUn4uOwKSE8jmM.png)](https://huggingface.co/dwjoeikr "dwjoeikr")
- [![](https://huggingface.co/avatars/d92eb2dedaa6a93abca22533d7fca37e.svg)](https://huggingface.co/adiasg "adiasg")
- [![](https://huggingface.co/avatars/f8ec95d43353cadcd78b4a713918364b.svg)](https://huggingface.co/rakeshtanwar "rakeshtanwar")
- [![](https://huggingface.co/avatars/9a4f6a5a7c26c9cfcc9521fe43699eca.svg)](https://huggingface.co/ch-min "ch-min")
- [![](https://cdn-avatars.huggingface.co/v1/production/uploads/1605114051380-noauth.jpeg)](https://huggingface.co/jeffboudier "jeffboudier")
- [![](https://huggingface.co/avatars/100f5ae3cf3c52faaecdaecd5d8f2881.svg)](https://huggingface.co/haotiz "haotiz")
- [![](https://cdn-avatars.huggingface.co/v1/production/uploads/6141a88b3a0ec78603c9e784/DJsxSmWV39M33JFheLobC.jpeg)](https://huggingface.co/merve "merve")
- [![](https://cdn-avatars.huggingface.co/v1/production/uploads/1673909278097-noauth.png)](https://huggingface.co/xziayro "xziayro")
- [![](https://huggingface.co/avatars/183456c0fa0d5e21c27813ce48d3bad2.svg)](https://huggingface.co/Sentinel7 "Sentinel7")
- [![](https://cdn-avatars.huggingface.co/v1/production/uploads/63c1699e40a26dd2db32400d/3N0-Zp8igv8-52mXAdiiq.jpeg)](https://huggingface.co/Chroma111 "Chroma111")
- [![](https://huggingface.co/avatars/5e8a4e7f3e9dfcba25f6fa3c35c6f2a5.svg)](https://huggingface.co/pipizich "pipizich")
- +78

## Models mentioned in this article 2

## Collections mentioned in this article 1