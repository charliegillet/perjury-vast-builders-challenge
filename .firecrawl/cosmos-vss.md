[Skip to content](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#video-search-and-summarization-with-cosmos-reason)

[Cosmos Cookbook](https://nvidia-cosmos.github.io/cosmos-cookbook/ "Cosmos Cookbook")

[Cosmos Cookbook](https://nvidia-cosmos.github.io/cosmos-cookbook/)


Video Search and Summarization with Cosmos Reason



Initializing search


[nvidia-cosmos/cosmos-cookbook\\
\\
\\
- 477\\
- 110](https://github.com/nvidia-cosmos/cosmos-cookbook "Go to repository")

[Cosmos Cookbook](https://nvidia-cosmos.github.io/cosmos-cookbook/index.html "Cosmos Cookbook")
Cosmos Cookbook


[nvidia-cosmos/cosmos-cookbook\\
\\
\\
- 477\\
- 110](https://github.com/nvidia-cosmos/cosmos-cookbook "Go to repository")

- [Overview](https://nvidia-cosmos.github.io/cosmos-cookbook/index.html)
- [ ]
Getting Started


Getting Started


  - [Setup](https://nvidia-cosmos.github.io/cosmos-cookbook/getting_started/setup.html)
  - [Cloud Deployments](https://nvidia-cosmos.github.io/cosmos-cookbook/getting_started/cloud_platform.html)
  - [Prompt Guide](https://nvidia-cosmos.github.io/cosmos-cookbook/getting_started/prompt_guide/overview.html)

- [ ]
Gallery


Gallery


  - [Robotics](https://nvidia-cosmos.github.io/cosmos-cookbook/gallery/robotics_inference.html)
  - [Autonomous Driving](https://nvidia-cosmos.github.io/cosmos-cookbook/gallery/av_inference.html)
  - [Vision AI](https://nvidia-cosmos.github.io/cosmos-cookbook/gallery/vision_ai_inference.html)

- [ ]
Recipes


Recipes


  - [All recipes](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/all_recipes.html)
  - [Additional examples](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/additional_examples.html)

- [ ]
Core Concepts


Core Concepts


  - [ ]
     Control Modalities


     Control Modalities


    - [Overview](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/control_modalities/overview.html)

  - [ ]
     Data Curation


     Data Curation


    - [Overview](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/data_curation/overview.html)
    - [Core Curation](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/data_curation/core_curation.html)

  - [ ]
     Post-Training


     Post-Training


    - [Overview](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/post_training/overview.html)

  - [ ]
     Evaluation


     Evaluation


    - [Overview](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/evaluation/overview.html)
    - [Evaluate Predict](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/evaluation/evaluation_predict.html)
    - [Evaluate Transfer](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/evaluation/evaluation_transfer.html)
    - [Cosmos Reason as Reward](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/evaluation/reason_as_reward.html)
    - [Evaluate Reason](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/evaluation/evaluation_reason.html)

  - [ ]
     Distillation


     Distillation


    - [Overview](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/distillation/overview.html)
    - [Case Study: Distill Cosmos Transfer 1](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/distillation/distilling_transfer1.html)
    - [Case Study: Distill Cosmos Predict 2.5](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/distillation/distilling_predict2.5.html)

- [Glossary](https://nvidia-cosmos.github.io/cosmos-cookbook/glossary.html)
- [FAQ](https://nvidia-cosmos.github.io/cosmos-cookbook/faq.html)
- [CONTRIBUTING](https://nvidia-cosmos.github.io/cosmos-cookbook/contributing_doc.html)

Table of contents


- [Overview](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#overview)
- [Key Features](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#key-features)
- [VSS Blueprint Architecture](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#vss-blueprint-architecture)

  - [Ingestion Pipeline](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#ingestion-pipeline)
  - [Retrieval Pipeline](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#retrieval-pipeline)

- [Getting Started](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#getting-started)

  - [Cloud Deployment](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#cloud-deployment)
  - [Local Deployment](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#local-deployment)
  - [Example Code Walkthrough](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#example-code-walkthrough)

- [Conclusion](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#conclusion)
- [Resources](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#resources)
- [Document Information](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#document-information)

  - [Citation](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html#citation)

# Video Search and Summarization with Cosmos Reason

> **Authors:** [Sammy Ochoa](https://www.linkedin.com/in/sammy-ochoa/) **Organization:** NVIDIA

## Overview

| **Model** | **Workload** | **Use Case** |
| --- | --- | --- |
| [Cosmos Reason 2 8B](https://huggingface.co/nvidia/Cosmos-Reason2-8B) | Inference | Large scale video search and summarization. |

Large volumes of video data contain critical information for understanding and optimizing operations in warehouses, factories, retail stores, cities and more. Both archived video files and live streaming camera feeds require time-consuming manual review to extract valuable insights from the videos.

The [Video Search and Summarization Blueprint](https://build.nvidia.com/nvidia/video-search-and-summarization) (VSS) from NVIDIA is a reference architecture for combining vision language models, computer vision models and large language models to analyze and understand large volumes of video data. VSS is easily configured through various prompts to tune the model responses based on the target use case.

![VSS UI Example](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/assets/warehouse_summary_example.png)

VSS allows the user to upload video files or connect live streaming camera feeds to generate summaries, answer questions or send alerts when events of interest occur.

Cosmos Reason is used as the default vision language model in VSS to produce high quality captions across the input videos. VSS first breaks the input video into small chunks (10s-30s) then provides them to Cosmos Reason as a part of a GPU optimized inference pipeline to rapidly caption the video chunks in parallel.

In addition to the captions from Cosmos Reason, extra data sources such as detection data and audio transcription are combined with the video captions. This data is stored in vector and graph database, then retrieved by an LLM to generate summaries, answer questions and trigger alerts based on user prompts.

The NVIDIA Brev Launchable is a quick way to launch a pre-configured environment for VSS testing.

- [VSS Brev Launchable](https://docs.nvidia.com/vss/latest/content/cloud_brev.html)

For Nebius deployment, an 8xH100 GPU instance is recommended using the local deployment profile. Alternatively, a single 1xH100 instance can be used with smaller models by following the single GPU deployment profile.

- [Multi-GPU local deployment profile](https://docs.nvidia.com/vss/latest/content/vss_dep_docker_compose_x86.html#local-deployment)
- [Single-GPU local deployment profile](https://docs.nvidia.com/vss/latest/content/vss_dep_docker_compose_x86.html#fully-local-deployment-single-gpu)

For custom deployments on local systems or other cloud instances, the VSS documentation provides several deployment profiles for various hardware configurations.

- [Setup and System Requirements](https://docs.nvidia.com/vss/latest/content/prereqs_x86.html#)

## Key Features

- **Video Summarization**: Generate custom video summaries based on user prompts.
- **Video Q&A**: Answer questions using advanced Graph-RAG techniques on video files and streams.
- **Livestream Alerts**: Receive alerts on live streaming video when events of interest occur.

## VSS Blueprint Architecture

![VSS Architecture](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/assets/vss_architecture.jpg)

VSS is composed of two main parts:

- **Ingestion Pipeline**: Extract visual insights from the input video in the
form of captions and scene descriptions.
- **Retrieval Pipeline**: Visual insights from the ingestion pipeline are further
processed, indexed, and used in retrieval tasks like summarization, Q&A and alerts.

### Ingestion Pipeline

The ingestion pipeline supports offline and batch processing of video and image files as well
as online processing of live streams from cameras.

- Video files are divided into smaller segments—typically 10 to 30 seconds, depending on the model and application. Processing of individual chunks is distributed across the GPUs in parallel for better performance.

- For each video chunk, a set number of frames are sampled. For example 10 frames from a 10 second video chunk will be provided to Cosmos Reason to produce a caption. These values are configurable based on the use case and model context length.

- Audio transcription using Riva ASR can optionally be enabled to generate audio transcripts of each video chunk.

- A Grounding Dino based detection and tracking pipeline can be enabled to gain extra insight into specific objects in the video. The detection and tracking data is overlaid onto the video then provided to Cosmos Reason to produce more detailed captions.

- The VLM captions, audio transcripts, CV metadata and timestamp information for each chunk are sent to the retrieval pipeline for further processing and indexing.


### Retrieval Pipeline

The retrieval pipeline, implemented in the [CA-RAG library](https://github.com/NVIDIA/context-aware-rag), is responsible for processing the output of the ingestion pipeline and using it for various retrieval tasks like summarization of long video files, live streams, and Q&A on the indexed data.

- VLM captions, audio transcripts and associated metadata are processed and indexed and stored in vector and graph databases.

- The accelerated NeMo Retriever Embedding NIM is used for high throughput text embedding of the VLM captions. These text embeddings, along with associated metadata, are inserted in the vector database.

- LLMs like Llama 3.1 70B are used for tool calling, parsing the VLM captions, and generating the insertion API calls for the graph database to build a knowledge graph of the video.

- For summarization, the VLM captions and audio transcripts are summarized together to get a final aggregated summary using an LLM.

- For Q&A, with the help of LLM tool calling, information relevant to your query is extracted from the knowledge graph and the vector database. The retrieved information is passed to the NeMo reranking service and the output is used as context by the LLM for generating the answer to your question.


## Getting Started

To use VSS with Cosmos Reason, you must first deploy it either to a cloud instance or to your local GPUs. After deployment, VSS offers a reference front-end interface for quick video summarization and a REST API backend for seamless integration with your custom applications.

### Cloud Deployment

- [VSS Brev Launchable](https://docs.nvidia.com/vss/latest/content/cloud_brev.html)

### Local Deployment

- [Setup and System Requirements](https://docs.nvidia.com/vss/latest/content/prereqs_x86.html#)

Once deployed, you can follow the [UI documentation page](https://docs.nvidia.com/vss/latest/content/ui_app.html) to learn how to use the reference UI for quickly testing your own videos and live streams.

### Example Code Walkthrough

Once you are ready build a custom application around VSS, you can directly access the back end REST APIs instead of using the UI.

1. Once deployed, VSS will provide a backend port by default at port 8100. This is where the REST APIs are available.

2. Import the requests library and setup the REST API paths. The full REST API documentation can be found [here](https://docs.nvidia.com/vss/latest/content/API_doc.html).



```
import requests

vss_host = "http://localhost:8100"
files_endpoint = vss_host + "/files" #upload and manage files
summarize_endpoint = vss_host + "/summarize" #summarize uploaded content
qna_endpoint = vss_host + "/chat/completions" #ask questions for ingested video
```

3. Upload a video file to VSS and receive a video ID



```
video_file_path = "/path/to/your/video.mp4"

with open(video_file_path, "rb") as file:
       files = {"file": ("video_file", file)} #provide the file content along with a file name
       data = {"purpose":"vision", "media_type":"video"}
       response = requests.post(files_endpoint, data=data, files=files) #post file upload request
       response = response.json()

video_id = response["id"] #save file ID for summarization request
```

4. With the video id, a summarization request can be sent along with prompts to control the VLM captioning and output summary.



```
body = {
       "id": video_id, #id of file returned after upload
       "prompt": "Write a detailed caption based on the video clip.",
       "caption_summarization_prompt": "Combine sequential captions to create more concise descriptions.",
       "summary_aggregation_prompt": "Write a detailed and well formatted summary of the video captions.",
       "model": "cosmos-reason2",
       "max_tokens": 1024,
       "temperature": 0.3,
       "top_p": 0.3,
       "chunk_duration": 20,
}

response = requests.post(summarize_endpoint, json=body)
response = response.json()
summary = response["choices"][0]["message"]["content"]
print(summary)
```

5. Once the video has been ingested, additional Q&A requests can be sent to ask questions about the video.



```
question = "What did you see in the video?"

payload = {
           "id": video_id,
           "messages": [{"content": question, "role": "user"}],
           "model": "cosmos-reason2"
       }

response = requests.post(qna_endpoint, json=payload)
response_data = response.json()
answer = response_data["choices"][0]["message"]["content"]
print(answer)
```


## Conclusion

Cosmos Reason is used in VSS to generate high-quality video captions through an optimized GPU accelerated inference pipeline. The captions are analyzed and indexed using a combination of embedding and large language models to store key information in vector and graph databases to power long video summarization, Q&A and live stream alerts.

VSS can easily be deployed through the [Brev Launchable](https://docs.nvidia.com/vss/latest/content/cloud_brev.html) or by following the local deployment guide. Once deployed, the reference web UI can be used to quickly test custom videos and prompts. To integrate with your own application, the [VSS REST APIs](https://docs.nvidia.com/vss/latest/content/API_doc.html) can be used programmatically to access all VSS features.

## Resources

- **[VSS Documentation](https://docs.nvidia.com/vss/latest/index.html)** \- Primary documentation for VSS
- **[VSS Github Repository](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization)** \- Open Source GitHub Repository for VSS

* * *

## Document Information

**Publication Date:** January 29, 2026

### Citation

If you use this recipe or reference this work, please cite it as:

```
@misc{cosmos_cookbook_video_search_and_2026,
  title={Video Search and Summarization with Cosmos Reason},
  author={Ochoa, Sammy},
  organization={NVIDIA},
  year={2026},
  month={January},
  howpublished={\url{https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html}},
  note={NVIDIA Cosmos Cookbook}
}
```

**Suggested text citation:**

> Sammy Ochoa (2026). Video Search and Summarization with Cosmos Reason. In _NVIDIA Cosmos Cookbook_. NVIDIA. Accessible at [https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/vss/inference.html)

[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) \|
[Your Privacy Choices](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) \|
[Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) \|
[Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) \|
[Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) \|
[Product Security](https://www.nvidia.com/en-us/product-security/) \|
[Contact](https://www.nvidia.com/en-us/contact/)

© Copyright 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.