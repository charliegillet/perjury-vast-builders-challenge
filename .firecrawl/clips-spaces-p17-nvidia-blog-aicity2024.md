![country_code](https://www.nvidia.com/content/dam/1x1-00000000.png)

[Skip to content](https://blogs.nvidia.com/blog/ai-city-challenge-omniverse-cvpr/#primary)

NVIDIA contributed the largest ever indoor synthetic dataset to the [Computer Vision and Pattern Recognition (CVPR)](https://www.nvidia.com/en-us/events/cvpr/) conference’s annual [AI City Challenge](https://www.aicitychallenge.org/) — helping researchers and developers advance the development of solutions for smart cities and industrial automation.

The challenge, garnering over 700 teams from nearly 50 countries, tasks participants to develop AI models to enhance operational efficiency in physical settings, such as retail and warehouse environments, and intelligent traffic systems.

Teams tested their models on the datasets that were generated using [NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/), a platform of application programming interfaces (APIs), software development kits (SDKs) and services that enable developers to build [Universal Scene Description (OpenUSD)](https://www.nvidia.com/en-us/omniverse/usd/)-based applications and workflows.

## **Creating and Simulating Digital Twins for Large Spaces**

In large indoor spaces like factories and warehouses, daily activities involve a steady stream of people, small vehicles and future autonomous robots. Developers need solutions that can observe and measure activities, optimize operational efficiency, and prioritize human safety in complex, large-scale settings.

Researchers are addressing that need with computer vision models that can perceive and understand the physical world. It can be used in applications like [multi-camera tracking](https://www.youtube.com/watch?v=l5M4sqaRd6w), in which a model tracks multiple entities within a given environment.

To ensure their accuracy, the models must be trained on large, ground-truth datasets for a variety of real-world scenarios. But collecting that data can be a challenging, time-consuming and costly process.

AI researchers are turning to physically based simulations — such as [digital twins](https://www.nvidia.com/en-us/glossary/digital-twin/) of the physical world — to enhance AI simulation and training. These virtual environments can help generate [synthetic data](https://www.nvidia.com/en-us/use-cases/synthetic-data/) used to train AI models. Simulation also provides a way to run a multitude of “what-if” scenarios in a safe environment while addressing privacy and AI bias issues.

Creating synthetic data is important for AI training because it offers a large, scalable, and expandable amount of data. Teams can generate a diverse set of training data by changing many parameters including lighting, object locations, textures and colors.

## **Building Synthetic Datasets for the AI City Challenge**

This year’s AI City Challenge consists of five computer vision challenge tracks that span traffic management to worker safety.

NVIDIA contributed datasets for the first track, Multi-Camera Person Tracking, which saw the highest participation, with over 400 teams. The challenge used a benchmark and the largest synthetic dataset of its kind — comprising 212 hours of 1080p videos at 30 frames per second spanning 90 scenes across six virtual environments, including a warehouse, retail store and hospital.

Created in Omniverse, these scenes simulated nearly 1,000 cameras and featured around 2,500 digital human characters. It also provided a way for the researchers to generate data of the right size and fidelity to achieve the desired outcomes.

The benchmarks were created using Omniverse Replicator in [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim), a reference application that enables developers to design, simulate and train AI for robots, smart spaces or autonomous machines in physically based virtual environments built on NVIDIA Omniverse.

[Omniverse Replicator](https://docs.omniverse.nvidia.com/isaacsim/latest/replicator_tutorials/tutorial_replicator_omni_replicator_agent.html), an SDK for building synthetic data generation pipelines, automated many manual tasks involved in generating quality synthetic data, including domain randomization, camera placement and calibration, character movement, and semantic labeling of data and ground-truth for benchmarking.

Ten institutions and organizations are collaborating with NVIDIA for the AI City Challenge:

- Australian National University, Australia
- Emirates Center for Mobility Research, UAE
- Indian Institute of Technology Kanpur, India
- Iowa State University, U.S.
- Johns Hopkins University, U.S.
- National Yung-Ming Chiao-Tung University, Taiwan
- Santa Clara University, U.S.
- The United Arab Emirates University, UAE
- University at Albany – SUNY, U.S.
- Woven by Toyota, Japan

## **Driving the Future of Generative Physical AI**

Researchers and companies around the world are developing infrastructure automation and robots powered by physical AI — which are models that can understand instructions and autonomously perform complex tasks in the real world.

[Generative physical AI](https://www.youtube.com/watch?v=AYSfcgVv9-U) uses reinforcement learning in simulated environments, where it perceives the world using accurately simulated sensors, performs actions grounded by laws of physics, and receives feedback to reason about the next set of actions.

Developers can tap into developer SDKs and APIs, such as the NVIDIA Metropolis developer stack — which includes a [multi-camera tracking reference workflow](https://developer.nvidia.com/blog/optimize-processes-for-large-spaces-with-the-multi-camera-tracking-workflow/) — to add enhanced perception capabilities for factories, warehouses and retail operations. And with [the latest release of NVIDIA Isaac Sim](https://developer.nvidia.com/blog/supercharge-robotics-workflows-with-ai-and-simulation-using-nvidia-isaac-sim-4-0-and-nvidia-isaac-lab/), developers can supercharge robotics workflows by simulating and training AI-based robots in physically based virtual spaces before real-world deployment.

Researchers and developers are also combining high-fidelity, physics-based simulation with advanced AI to bridge the gap between [simulated training and real-world application](https://developer.nvidia.com/blog/closing-the-sim-to-real-gap-training-spot-quadruped-locomotion-with-nvidia-isaac-lab/). This helps ensure that synthetic training environments closely mimic real-world conditions for more seamless robot deployment.

NVIDIA is taking the accuracy and scale of simulations further with the recently [announced NVIDIA Omniverse Cloud Sensor RTX](https://nvidianews.nvidia.com/news/omniverse-microservices-physical-ai), a set of microservices that enable physically accurate sensor simulation to accelerate the development of fully autonomous machines.

This technology will allow autonomous systems, whether a factory, vehicle or robot, to gather essential data to effectively perceive, navigate and interact with the real world. Using these microservices, developers can run large-scale tests on sensor perception within realistic, virtual environments, significantly reducing the time and cost associated with real-world testing.

Omniverse Cloud Sensor RTX microservices will be available later this year. [Sign up](https://developer.nvidia.com/omniverse/join) for early access.

## **Showcasing Advanced AI With Research**

Participants submitted research papers for the AI City Challenge and a few achieved top rankings, including:

- [Overlap Suppression Clustering for Offline Multi-Camera People Tracking](https://openaccess.thecvf.com/content/CVPR2024W/AICity/papers/Yoshida_Overlap_Suppression_Clustering__for_Offline_Multi-Camera_People_Tracking_CVPRW_2024_paper.pdf): This paper introduces a tracking method that includes identifying individuals within a single camera’s view, selecting clear images for easier recognition, grouping similar appearances, and helping to clarify identities in challenging situations.
- [A Robust Online Multi-Camera People Tracking System With Geometric Consistency and State-aware Re-ID Correction](https://openaccess.thecvf.com/content/CVPR2024W/AICity/papers/Xie_A_Robust_Online_Multi-Camera_People_Tracking_System_With_Geometric_Consistency_CVPRW_2024_paper.pdf): This research presents a new system that uses geometric and appearance data to improve tracking accuracy, and includes a mechanism that adjusts identification features to fix tracking errors.
- [Cluster Self-Refinement for Enhanced Online Multi-Camera People Tracking](https://openaccess.thecvf.com/content/CVPR2024W/AICity/papers/Kim_Cluster_Self-Refinement_for_Enhanced_Online_Multi-Camera_People_Tracking_CVPRW_2024_paper.pdf): This research paper addresses specific challenges faced in online tracking, such as the storage of poor-quality data and errors in identity assignment.

All accepted papers will be presented at the [AI City Challenge 2024 Workshop](https://cvpr.thecvf.com/virtual/2024/workshop/23656), taking place on June 17.

At CVPR 2024, NVIDIA Research will present over 50 papers, introducing generative physical AI breakthroughs with potential applications in areas like autonomous vehicle development and robotics.

Papers that used NVIDIA Omniverse to generate synthetic data or digital twins of environments for model simulation, testing and validation include:

- [FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects](https://arxiv.org/abs/2312.08344): FoundationPose is a versatile model for estimating and tracking the 3D position and orientation of objects. The model operates by using a few reference images or a 3D representation to accurately understand an object’s shape.
- [Neural Implicit Representation for Building Digital Twins of Unknown Articulated Objects](https://arxiv.org/abs/2404.01440): This research paper presents a method for creating digital models of objects from two 3D scans, improving accuracy by analyzing how movable parts connect and move between positions.
- [BEHAVIOR Vision Suite: Customizable Dataset Generation via Simulation](https://arxiv.org/abs/2405.09546): The BEHAVIOR Vision Suite generates customizable synthetic data for computer vision research, allowing researchers to adjust settings like lighting and object placement.

Read more about NVIDIA Research at [CVPR](https://www.nvidia.com/en-us/events/cvpr/), and learn more about the [AI City Challenge](https://www.aicitychallenge.org/).

_Get started with NVIDIA Omniverse by downloading the standard license_ [_free_](https://www.nvidia.com/en-us/omniverse/download/) _, access_ [_OpenUSD_](https://developer.nvidia.com/usd) _resources and learn how_ [_Omniverse Enterprise can connect teams_](https://www.nvidia.com/en-us/omniverse/enterprise/) _. Follow Omniverse on_ [_Instagram_](https://www.instagram.com/nvidiaomniverse/) _,_ [_Medium_](https://medium.com/@nvidiaomniverse) _,_ [_LinkedIn_](https://www.linkedin.com/showcase/nvidia-omniverse/) _and_ [_X_](https://twitter.com/nvidiaomniverse) _. For more, join the_ [_Omniverse community_](https://www.nvidia.com/en-us/omniverse/community/) _on the_ [_forums_](https://forums.developer.nvidia.com/c/omniverse/300) _,_ [_Discord server_](https://discord.com/invite/XWQNJDNuaC) _,_ [_Twitch_](https://www.twitch.tv/nvidiaomniverse) _and_ [_YouTube_](https://www.youtube.com/channel/UCSKUoczbGAcMld7HjpCR8OA) _channels._

- Categories:
- [Pro Graphics](https://blogs.nvidia.com/blog/category/pro-graphics/)
- [Research](https://blogs.nvidia.com/blog/category/nvidia-research/)

- Tags:
- [Artificial Intelligence](https://blogs.nvidia.com/blog/tag/artificial-intelligence/)
- [NVIDIA Isaac Sim](https://blogs.nvidia.com/blog/tag/nvidia-isaac-sim/)
- [NVIDIA Research](https://blogs.nvidia.com/blog/tag/nvidia-research/)
- [Omniverse](https://blogs.nvidia.com/blog/tag/omniverse/)
- [Physical AI](https://blogs.nvidia.com/blog/tag/physical-ai/)
- [Retail and Consumer Packaged Goods](https://blogs.nvidia.com/blog/tag/retail/)
- [Simulation and Design](https://blogs.nvidia.com/blog/tag/simulation-and-design/)
- [Synthetic Data Generation](https://blogs.nvidia.com/blog/tag/synthetic-data-generation/)

### Related News

[![How NVIDIA GPUs Help Accelerate OpenAI’s GPT-6 Astra Ultrafast](https://blogs.nvidia.com/wp-content/uploads/2026/09/twitter-gif-2104993966043320759-v5-300x169.png)](https://blogs.nvidia.com/blog/gpus-openai-gpt-6-astra-ultrafast/)

[AI Infrastructure](https://blogs.nvidia.com/blog/category/enterprise/)

### [How NVIDIA GPUs Help Accelerate OpenAI’s GPT-6 Astra Ultrafast](https://blogs.nvidia.com/blog/gpus-openai-gpt-6-astra-ultrafast/)

Oct 1, 2026

[![How Open Science Can Help Researchers Prepare for the Next Pandemic](https://blogs.nvidia.com/wp-content/uploads/2026/09/AF-0000000212056767-master-black-background-300x169.png)](https://blogs.nvidia.com/blog/open-protein-dataset/)

[AI](https://blogs.nvidia.com/blog/category/generative-ai/)

### [How Open Science Can Help Researchers Prepare for the Next Pandemic](https://blogs.nvidia.com/blog/open-protein-dataset/)

Sep 24, 2026

[![At AI Day Singapore, NVIDIA and Partners Showcase AI Advancements Across Southeast Asia](https://blogs.nvidia.com/wp-content/uploads/2026/09/ai-day-singapore-key-visul-1920x1080-1-300x169.jpg)](https://blogs.nvidia.com/blog/ai-day-singapore/)

[AI](https://blogs.nvidia.com/blog/category/generative-ai/)

### [At AI Day Singapore, NVIDIA and Partners Showcase AI Advancements Across Southeast Asia](https://blogs.nvidia.com/blog/ai-day-singapore/)

Sep 22, 2026

[![From Enablement to Execution, Egypt’s AI Ecosystem Reaches Production Scale](https://blogs.nvidia.com/wp-content/uploads/2026/09/5723250-ent-dig-egypt-ecosystem-reception-blog-1920x1080-1-300x169.jpg)](https://blogs.nvidia.com/blog/egypt-africa-ai-ecosystem/)

[AI](https://blogs.nvidia.com/blog/category/generative-ai/)

### [From Enablement to Execution, Egypt’s AI Ecosystem Reaches Production Scale](https://blogs.nvidia.com/blog/egypt-africa-ai-ecosystem/)

Sep 21, 2026

Follow Us

![](data:image/svg+xml,%3csvg id='Logo' xmlns='http://www.w3.org/2000/svg' width='108.472' height='20' viewBox='0 0 108.472 20'%3e %3cpath id='Reg' d='M1072.628,253.918v-.3h.192c.105,0,.248.008.248.136s-.073.163-.2.163h-.243m0,.211h.129l.3.524h.327l-.33-.545a.3.3,0,0,0,.311-.323c0-.285-.2-.377-.53-.377h-.482v1.245h.276v-.524m1.4-.1a1.2,1.2,0,1,0-1.2,1.157,1.14,1.14,0,0,0,1.2-1.157m-.347,0a.854.854,0,0,1-.855.891v0a.889.889,0,1,1,.855-.887Z' transform='translate(-965.557 -237.878)'/%3e %3cpath id='NVIDIA' d='M463.9,151.934v13.127h3.707V151.934Zm-29.164-.018v13.145h3.74v-10.2l2.918.01a2.674,2.674,0,0,1,2.086.724c.586.625.826,1.632.826,3.476v5.995h3.624V157.8c0-5.183-3.3-5.882-6.536-5.882Zm35.134.018v13.127h6.013c3.2,0,4.249-.533,5.38-1.727a7.352,7.352,0,0,0,1.316-4.692,7.789,7.789,0,0,0-1.2-4.516c-1.373-1.833-3.352-2.191-6.306-2.191Zm3.677,2.858h1.594c2.312,0,3.808,1.039,3.808,3.733s-1.5,3.734-3.808,3.734h-1.594Zm-14.992-2.858-3.094,10.4-2.965-10.4h-4l4.234,13.127h5.343l4.267-13.127Zm25.749,13.127h3.708V151.935h-3.709ZM494.7,151.939l-5.177,13.117h3.656l.819-2.318h6.126l.775,2.318h3.969l-5.216-13.118Zm2.407,2.393,2.246,6.145h-4.562Z' transform='translate(-399.551 -148.155)'/%3e %3cpath id='Eye_Mark' data-name='Eye Mark' d='M129.832,124.085v-1.807c.175-.013.353-.022.533-.028,4.941-.155,8.183,4.246,8.183,4.246s-3.5,4.863-7.255,4.863a4.553,4.553,0,0,1-1.461-.234v-5.478c1.924.232,2.31,1.082,3.467,3.01l2.572-2.169a6.81,6.81,0,0,0-5.042-2.462,9.328,9.328,0,0,0-1,.059m0-5.968v2.7c.177-.014.355-.025.533-.032,6.871-.232,11.348,5.635,11.348,5.635s-5.142,6.253-10.5,6.253a7.906,7.906,0,0,1-1.383-.122v1.668a9.1,9.1,0,0,0,1.151.075c4.985,0,8.59-2.546,12.081-5.559.578.463,2.948,1.591,3.435,2.085-3.319,2.778-11.055,5.018-15.44,5.018-.423,0-.829-.026-1.228-.064v2.344h18.947v-20Zm0,13.009v1.424c-4.611-.822-5.89-5.615-5.89-5.615a9.967,9.967,0,0,1,5.89-2.85v1.563h-.007a4.424,4.424,0,0,0-3.437,1.571s.845,3.035,3.444,3.908m-8.189-4.4a11.419,11.419,0,0,1,8.189-4.449v-1.463c-6.043.485-11.277,5.6-11.277,5.6s2.964,8.569,11.277,9.354v-1.555C123.731,133.451,121.643,126.728,121.643,126.728Z' transform='translate(-118.555 -118.117)' fill='%23000000'/%3e %3c/svg%3e)[United States](https://www.nvidia.com/en-us/location-selector/)

- [Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/)
- [Your Privacy Choices](https://www.nvidia.com/en-us/about-nvidia/privacy-center/)
- [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/)
- [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/)
- [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/)
- [Product Security](https://www.nvidia.com/en-us/product-security/)
- [Contact](https://www.nvidia.com/en-us/contact/)

Copyright © 2026 NVIDIA Corporation

[Share This](https://x.com/intent/tweet?via=%username%&url=%url%&text=%prefix%%text%%suffix%&hashtags=%hashtags%)

[Facebook](https://www.facebook.com/sharer/sharer.php?u=%url%&t=%title%)

[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?mini=true&url=%url%&title=%title%)

### Share on Mastodon

Enter your Mastodon instance URL (optional)Share