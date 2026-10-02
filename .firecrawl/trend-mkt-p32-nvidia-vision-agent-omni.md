![country_code](https://www.nvidia.com/content/dam/1x1-00000000.png)

[Skip to content](https://blogs.nvidia.com/blog/vision-ai-agent-skills-omniverse-metropolis/#primary)

_Editor’s note: This post is part of_ [_Into the Omniverse_](https://www.nvidia.com/en-us/omniverse/news/) _, a series focused on how developers, 3D practitioners, and enterprises can transform their workflows using the latest advances in_ [_OpenUSD_](https://www.nvidia.com/en-us/omniverse/usd/) _and_ [_NVIDIA Omniverse_](https://www.nvidia.com/en-us/omniverse/) _._

[Vision AI agents](https://www.nvidia.com/en-us/use-cases/video-analytics-ai-agents/) are becoming a practical way to automatically turn video data from the physical world into operational intelligence in factories, cities, warehouses and transportation systems.

That shift is accelerating as more AI workloads move closer to where data is generated. Gartner projects that more than two-thirds of enterprise-managed data will be created and processed outside the data center or cloud by 2028, and that over two-thirds of all enterprises globally will deploy edge AI by 2029, up from 10% in 2025 (1).

But more edge data doesn’t automatically create more intelligence. As much as 90% of existing edge data goes unprocessed, according to the same Gartner report.

Turning that data into useful action requires vision AI agents that can understand video, adapt to real-world conditions and connect insights to operational workflows. These agents often run near cameras, machines and sensors, where models must meet latency, power, cost and connectivity requirements while adapting to site-specific conditions.

To build those agents, developers need repeatable ways to generate training data, fine-tune models and deploy agentic video applications across edge and cloud environments.

[NVIDIA Metropolis](https://developer.nvidia.com/metropolis) agent skills and blueprints give developers reusable workflows to build, operate and optimize vision AI agents across that lifecycle.

For the simulation and [synthetic data](https://www.nvidia.com/en-us/glossary/synthetic-data-generation/) side of that work, Universal Scene Description, or [OpenUSD](https://www.nvidia.com/en-us/glossary/openusd/), provides a common framework for describing, composing and reusing 3D worlds. Built on OpenUSD, [NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/) libraries help teams build simulation, synthetic data generation and digital twin workflows that model real-world environments and expand scenario coverage across conditions such as lighting, weather, traffic patterns, camera angles, occlusion and rare events.

## **Where Vision AI Agent Projects Can Get Stuck**

As organizations move toward autonomous vision agents, three challenges often come up:

- **Accuracy Plateaus With Data Gaps:** Vision AI agents need to spot rare defects, abnormal events and changing environments. In manufacturing, for example, an inspection model may perform well on common scratches or dents but struggle with a new hairline crack not represented in the training data.
- **Lack of Fine-Tuning Expertise:** Once teams identify a performance gap, improving the model is rarely a simple handoff. Fine-tuning requires labeled datasets, training configuration, experiment tracking, evaluation and decisions about whether there’s improvement for the target use case. Many organizations building vision AI agents don’t have large in-house machine learning teams to manage that process quickly, especially across many sites, products or camera views.
- **Complex, Time-Consuming Agent Assembly Workflows:** Deploying a vision AI agent requires more than running inference. Developers have to stitch together video pipelines, AI models, metadata, embeddings, indexing, search, alerts, reporting and system integrations. Customizing that workflow for a specific environment adds significant time and requires specialized expertise. Without OpenUSD’s shared scene description layer, teams often rebuild 3D environments from scratch each time conditions or deployment sites change.

## **A Full-Lifecycle Approach to Vision AI Agents**

NVIDIA agent skills and blueprints — used alongside NVIDIA Omniverse for OpenUSD-based simulation and synthetic data generation, NVIDIA Metropolis for model development and video AI deployment — give developers reusable starting points for key parts of those workflows:

- The [Defect Image Generation skill](https://github.com/NVIDIA/skills/tree/main/skills/physical-ai-defect-image-generation) helps create synthetic defect data.
- The [Video Data Augmentation skill](https://github.com/NVIDIA/skills/tree/main/skills/physical-ai-video-data-augmentation) helps expand scenario coverage.
- [NVIDIA TAO skills](https://github.com/NVIDIA-TAO/tao-skills-bank) enable model fine-tuning.
- [NVIDIA video search and summarization (VSS) skills](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization/tree/main/skills) help turn video understanding into deployable workflows for alerts, reporting, stream management and more.

Instead of rebuilding every step from scratch, developers can use these reusable workflows to generate data, improve models and deploy vision AI agents faster.

## **Visual Inspection: Generating the Data That Production Lines Don’t Have**

In manufacturing, the more successful a factory is at preventing defects, the harder it becomes to collect enough defect examples to train the next inspection model.

[Roboflow](https://blog.roboflow.com/synthetic-data-generation-manufacturing-nvidia/) is integrating the NVIDIA Defect Image Generation skill and [NVIDIA Cosmos world foundation models](https://www.nvidia.com/en-us/ai/cosmos/) into its vision AI platform to generate synthetic defect images for customers like Corning when real training data is scarce, enabling near-perfect detection performance while significantly reducing the need for daily manual image review.

In a benchmark conducted with Corning’s optical fiber manufacturing engineering team, a model trained on just eight real defect images — augmented with synthetic data generated by the NVIDIA Defect Image Generation skill — reached an average precision of 95% and perfect recall on the most challenging defect class. This performance surpassed a baseline model trained solely on real data, effectively compressing a multi-quarter inspection project into just a few days.

Watch how synthetic data generation workflows help developers create the data needed to train and improve physical AI models:

Generate Synthetic Data for Physical AI With NVIDIA Brev Launchables and Agent Skills - YouTube

Tap to unmute

[Generate Synthetic Data for Physical AI With NVIDIA Brev Launchables and Agent Skills](https://www.youtube.com/watch?v=rJCSWE9XhE0) [NVIDIA Developer](https://www.youtube.com/channel/UCBHcMCGaiJhv-ESTcWGJPcw)

NVIDIA Developer225K subscribers

[Watch on](https://www.youtube.com/watch?v=rJCSWE9XhE0)

## **Smart Cities: From Video Analytics to Autonomous Operations**

Large-scale city operations show why vision AI agents need connected workflows, not just inference.

[Linker Vision](https://www.nvidia.com/en-us/case-studies/linker-vision-ai-smart-city-solutions/) is building smart city AI systems with the [NVIDIA Metropolis Blueprint for VSS](https://build.nvidia.com/nvidia/video-search-and-summarization) to accelerate the deployment of video reasoning agents across city infrastructure. In this workflow, VSS skills can help package common video AI tasks such as search, summarization, alerts, reporting and stream management into reusable agent-executable workflows.

OpenUSD-based NVIDIA Omniverse digital twins help model city environments and test how vision AI systems respond to varied traffic patterns, weather conditions, emergency events and infrastructure changes. Linker Vision uses NVIDIA Cosmos for [video data augmentation](https://github.com/NVIDIA/skills/tree/main/skills/physical-ai-video-data-augmentation) and [NVIDIA TAO](https://developer.nvidia.com/tao-toolkit) for Cosmos model fine-tuning.

In Kaohsiung, Linker Vision reduced development effort by 85% using the VSS blueprint and reduced incident response times by up to 80%. Its newer AI-GRID expansion builds on this approach with [NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/) blueprints for secure agentic AI, supporting autonomous video reasoning across city and transportation environments.

Smart Kaohsiung: How the City AI Platform Manages Floods, Traffic & Waste in Real Time - YouTube

Tap to unmute

[Smart Kaohsiung: How the City AI Platform Manages Floods, Traffic & Waste in Real Time](https://www.youtube.com/watch?v=-T6jB_CKIcg) [Linker Vision - Large-Scale AI Innovation](https://www.youtube.com/channel/UCslkLHjBF61Imqw9Pepp9hQ)

![thumbnail-image](https://yt3.ggpht.com/GqpxRB5j5e7rH0CqJgmgmB9lfa23RjRUxzlE7LK_vAbGtC1tTiUa5rc38iIhZSrMaKR8yXBJZHs=s68-c-k-c0x00ffffff-no-rj)

Linker Vision - Large-Scale AI Innovation117 subscribers

[Watch on](https://www.youtube.com/watch?v=-T6jB_CKIcg)

## **Industrial Operations: Reasoning Over Work as It Happens**

In industrial environments, the challenge isn’t just detecting what appears in a video frame. Teams need agents that can:

- Understand whether work is being performed correctly
- Compare execution against standard operating procedures
- Produce insights before defects move downstream.

At Foxconn, [DeepHow’s Live Standard Operating Procedure](https://deephow.com/blog/foxconn-boosts-production-throughput-with-deephow-live-sop-verification-powered-by-nvidia) (SOP) Verification agent uses the NVIDIA Metropolis VSS blueprint as the agentic video workflow layer for search, summarization and analysis across operational environments. NVIDIA Cosmos provides the reasoning capability that helps the agent interpret complex human activity and work sequences in context, such as whether assembly steps are performed correctly and in the expected order.

The solution has been used on the NVIDIA GB300 server production lines to improve first-pass yield by 3%, achieve 99% task-level accuracy in micro-action understanding of critical SOP steps and reduce redundant work by helping teams catch problems earlier.

_To see how developers can build and deploy video analytics AI agents, watch this technical walkthrough on using_ [_NVIDIA VSS skills with coding agents_](https://www.youtube.com/watch?v=U1D4ZhSHHd0) _._

_Explore NVIDIA agent skills and blueprints to build, operate and optimize_ [_video analytics AI agents_](https://www.nvidia.com/en-us/use-cases/video-analytics-ai-agents/) _._

_Source: Gartner, Predicts 2026: Physical AI Pushes I&O to the Edge, 3 March 2026._ _Gartner is a trademark of Gartner, Inc. and/or its affiliates._

- Categories:
- [AI](https://blogs.nvidia.com/blog/category/generative-ai/)
- [Robotics](https://blogs.nvidia.com/blog/category/robotics/)

- Tags:
- [Agentic AI](https://blogs.nvidia.com/blog/tag/agentic-ai/)
- [Cosmos](https://blogs.nvidia.com/blog/tag/cosmos/)
- [Industrial and Manufacturing](https://blogs.nvidia.com/blog/tag/industrial-manufacturing/)
- [Into the Omniverse](https://blogs.nvidia.com/blog/tag/into-the-omniverse/)
- [Metropolis](https://blogs.nvidia.com/blog/tag/metropolis/)
- [Omniverse](https://blogs.nvidia.com/blog/tag/omniverse/)
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