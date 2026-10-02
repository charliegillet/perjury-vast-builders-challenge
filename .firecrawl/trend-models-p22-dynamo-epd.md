[Technical Blog](https://developer.nvidia.com/blog)

[Subscribe](https://developer.nvidia.com/email-signup)

[Related Resources](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/#main-content-end)

[Computer Vision / Video Analytics](https://developer.nvidia.com/blog/category/computer-vision/)

English中文

# When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model Serving

![](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/multimodal-dynamo-1024x576.jpg)

Sep 09, 2026


By [Jesse Gu](https://developer.nvidia.com/blog/author/zcgu/ "Posts by Jesse Gu"), [Ryan McCormick](https://developer.nvidia.com/blog/author/rmccormick/ "Posts by Ryan McCormick") and [Akshatha Kamath](https://developer.nvidia.com/blog/author/akshathak/ "Posts by Akshatha Kamath")

+9

Like

[Discuss (0)](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/#entry-content-comments)

- [L](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fwhen-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving%2F)
- [T](https://twitter.com/intent/tweet?text=When+to+Use+Encode-Prefill-Decode+Disaggregation+to+Accelerate+Multimodal+Model+Serving+%7C+NVIDIA+Technical+Blog+https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fwhen-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving%2F)
- [F](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fwhen-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving%2F)
- [R](https://www.reddit.com/submit?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fwhen-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving%2F&title=When+to+Use+Encode-Prefill-Decode+Disaggregation+to+Accelerate+Multimodal+Model+Serving+%7C+NVIDIA+Technical+Blog)
- [E](mailto:?subject=I%27d%20like%20to%20share%20a%20link%20with%20you&body=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fwhen-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving%2F)

## AI-Generated Summary

- [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo) implements encode-prefill-decode (EPD) disaggregation to separate vision encoding from LLM prefill and decode stages for multimodal inference.
- EPD disaggregation delivers up to 5x faster time to first token and 7x faster end-to-end response time for image-heavy prompts, short-to-medium outputs, and quantized mixture-of-experts models.
- Three encoder placement topologies exist: aggregated serving, colocated encoder workers sharing GPUs with prefill-decode workers, and disaggregated encoder workers on a separate lower-cost GPU tier connected via [NVIDIA Inference Transfer Library (NIXL)](https://github.com/ai-dynamo/nixl).
- Benefits depend on input media load, output sequence length, model size and precision, and traffic mix; gains shrink when decode dominates latency or when large dense models reduce the vision encoder's share of compute.
- In mixed text and multimodal traffic, EPD reduces mean TTFT for text requests by 42.2% and for image requests by 30.8% by eliminating head-of-line blocking.
- Quantizing LLM weights to NVFP4 while keeping the vision encoder in BF16 increases colocated EPD goodput from 1.78x to 2.64x over aggregated serving.

### Next Steps

- Follow the [ai-dynamo/dynamo GitHub guide](https://github.com/ai-dynamo/dynamo/tree/release/1.5.0/benchmarks/multimodal/sweep/experiments/epd) to reproduce the EPD disaggregation experiments.
- Enable [parallel media decoding](https://docs.nvidia.com/dynamo/dev/multimodal/parallel-media-decoding) to move download and decode out of the worker and into the Dynamo front end.
- Use [embedding cache](https://docs.dynamo.nvidia.com/dynamo/dev/multimodal/embedding-cache) to store and reuse computed embeddings for repeated media content.
- Apply [multimodal KV routing](https://docs.nvidia.com/dynamo/dev/multimodal/multimodal-kv-routing) to route requests sharing media to workers already holding relevant KV blocks.

Powered by NVIDIA Nemotron. AI-generated content may summarize information incompletely. Verify important information. [Learn more](https://www.nvidia.com/en-us/agreements/trustworthy-ai/terms/)

Encode-prefill-decode (EPD) disaggregation is an inference optimization technique for multimodal models that separates the vision encoder stage from the prefill and decode stages. It is most effective for image-heavy prompts, short-to-medium outputs, and quantized [mixture-of-experts (MoE)](https://www.nvidia.com/en-us/glossary/mixture-of-experts/) models.

This post shows when and how to use EPD disaggregation with [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo) to achieve up to 5x faster time to first token (TTFT) and 7x faster end-to-end response time. The post also addresses the scenarios where EPD disaggregation is not recommended.

Dynamo is an open source inference framework for serving AI models in distributed environments. It supports EPD disaggregation, separating these phases into independently scalable stages rather than running them together with tightly coupled scheduling and scaling patterns. Dedicated encoder workers can improve batching, memory efficiency, and overall throughput.

## Why is EPD disaggregation important? [Scroll to Why is EPD disaggregation important? section](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/\#why_is_epd_disaggregation_important)

A multimodal request adds work before LLM prefill can begin. The serving stack must preprocess the media and run the vision transformer (ViT) to produce embeddings. In aggregated serving, vision encoding, LLM prefill, and decode all share one worker and one scheduling domain. This simple design works well when media processing accounts for only a small portion of the workload.

![Bar chart showing encoder work dominates TTFT for multi-image and video requests.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/ttft-multimodal-requests.webp)_Figure 1. TTFT breakdown across single-image, multi-image, and video requests, separated into media preprocessing, ViT forward and projection, and LLM prefill_

The balance changes as requests contain more images or video. Vision encoding can take hundreds of milliseconds or longer. Because encoder and LLM work share the same GPU, a media-heavy request can delay its own prefill and contend with concurrent prefill and decode work. In contrast, under mixed traffic, text-only requests may also wait behind multimodal requests even though they do not require vision encoding.

Dynamo implements EPD serving by separating the encoder and PD worker roles without fixing their hardware placement. Encoder workers produce vision embeddings, while PD workers consume those embeddings and run the LLM. This separation allows the stages to batch, schedule, and scale independently. Figure 2 compares aggregated and EPD serving, with encode workers passing embeddings to PD workers through [NVIDIA Inference Transfer Library (NIXL)](https://github.com/ai-dynamo/nixl).

![Flow diagram comparing aggregated and EPD serving, with encode workers passing embeddings to PD workers through NIXL. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/how-nvidia-dynamo-handles-multimodal-request-aggregated-versus-epd.webp)_Figure 2. Aggregated and EPD request flows in Dynamo. EPD separates encode execution from the PD workers and transfers embeddings through NIXL_

Encode disaggregation can reduce TTFT and increase same-SLO goodput only in certain scenarios. The encode work being isolated must be large enough to offset worker coordination and embedding transfer overhead. Encode workers may share the PD GPUs or run on a separate GPU tier, leading to different placement options. Here, we explore the different placement options for the encode worker and the benefits they yield under various scenarios.

## Three encode placement topologies [Scroll to Three encode placement topologies section](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/\#three_encode_placement_topologies)

Figure 3 compares aggregated serving with the two encoder disaggregated topologies, colocated and disaggregated:

- **Aggregated:** Each GPU runs a single aggregated worker whose scheduler manages vision encoding, LLM prefill, and decode as part of the same request lifecycle.
- **Colocated encoder**: Each GPU runs one or more encoder workers alongside one PD worker. This allows the workers to share GPU compute while maintaining separate request queues and batching. On a homogeneous cluster, Colocated Encoder is generally the better fit. The vision encoder is lightweight relative to the LLM, so reserving an entire same-class GPU for encoder work can leave much of that GPU underutilized. Colocation separates the workers without dedicating a GPU exclusively to the encoder.
- **Disaggregated encoder**: Disaggregated Encoder becomes attractive when the cluster includes a lower cost GPU tier better matched to encoder work while the primary GPU tier hosts the PD workers. Dynamo transfers the resulting vision embeddings to the PD tier through NIXL. In our test environment, two NVIDIA RTX 6000D GPUs ran the encoder workers, while four NVIDIA GB200 GPUs ran the PD workers. This placement keeps the lighter encoder workload on the RTX GPUs and reserves the GB200 GPUs for the more compute- and memory-intensive LLM workload. Note that this analysis does not consider the disaggregated setup with homogenous GPUs as it always underperforms the colocated encoder setup.

Hardware availability determines where the encoder can run and workload characteristics determine whether separating it pays off.

![Diagram of three encoder placements: aggregated (one worker), colocated (shared GPU through CUDA MPS), and disaggregated (RTX encoders, GB200 PD).](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/three-multimodal-encode-placement-options.webp)_Figure 3. Three encode-placement options: aggregated serving, co-located encoder and PD workers, and disaggregated encoder with a separate lower cost GPU tier for the encoder workers_

## What factors determine the benefits of EPD disaggregation? [Scroll to What factors determine the benefits of EPD disaggregation? section](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/\#what_factors_determine_the_benefits_of_epd_disaggregation)

The benefits of EPD depend on how work is divided among vision encoding, LLM prefill, and decode. EPD is most useful when vision encoding accounts for a significant share of request processing time or limits throughput. Media-heavy requests often create this condition, but media load alone does not determine the result. Output length, model size and precision, and traffic mix also change this balance.

| **Factor** | **Why it matters for EPD** | **When does EPD yield gains** |
| --- | --- | --- |
| Input media load | Heavier media load brings more visual tokens, which means more encoder work. EPD allows scaling up encoders, preventing encoding bottleneck. | Multiple images, high-resolution images, or video input that yields more visual tokens. |
| Output sequence length (OSL) | Longer OSL shifts total latency toward decode. TTFT gains from EPD hold, but end-to-end (E2E) gains shrink. | Short OSL: E2E gains hold Long OSL: E2E gains erode |
| Model size / precision | ViT compute is largely fixed, while LLM compute decreases with fewer active parameters and lower precision. Small, MoE, and quantized LLMs therefore have higher ViT-to-LLM compute ratios. | Smaller, MoE, and lower-precision models benefit more from EPD, while large dense models see less gain. |
| Mixed traffic (text + multimodal) | Mixed prefill batches can make text requests wait for ViT. EPD isolates encoder work, allowing text requests to skip waiting for encoder. | Heavy multimodal traffic mixed with latency sensitive text requests. |

_Table 1. How various factors affect EPD performance_

### Test environment [Scroll to Test environment section](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/\#test_environment)

All benchmarks were run with Qwen3.5 122B A10B NVFP4 except in the precision ablation experiments. We used four GB200 GPUs (and extra RTX 6000D GPUs in disaggregated setup):

- **Aggregated**: One TP1 aggregated worker per GB200
- **Co-located EPD**: Two encoder workers plus one PD worker per GB200
- **Disaggregated EPD**: RTX nodes as the encoder tier, GB200 as PD

We used NIXL over UCX RC/TCP Ethernet for vision embedding transfer, measured peak 20 Gbps. We used the Dynamo front end with front end parallel media decoding enabled. The goodput SLO is inter-token latency (ITL) under 100 ms.

### Image-heavy workload example [Scroll to Image-heavy workload example section](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/\#image-heavy_workload_example)

We compared the aggregated versus encoder disaggregated serving with the following request: Ten images per request (capped 256 token per image) at OSL 1024 to simulate moderately heavy visual workload with a long output sequence. Figure 4 shows the results.

![Bar charts showing ~2x TTFT reduction and ~1.5x goodput gain with EPD for 10 images/request.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/goodput-improvement-over-aggregated-setup.webp)_Figure 4. Mean TTFT and end-to-end latency across topologies for an image-heavy workload (10 images/request) (left). Goodput improvement over the aggregated setup given an SLO of ITL under 100 ms (right)_

TTFT drops 58% with colocated encoder and 50% with heterogeneous. End-to-end improvements are modest because OSL 1024 means the model generates 1024 tokens and decode time is not reduced by Encoder disaggregation. The larger signal is goodput: the heterogeneous tier serves 70% more traffic at the same latency SLO, because encoder capacity was added without touching the GB200 budget.

## How do image load and OSL impact performance gains? [Scroll to How do image load and OSL impact performance gains? section](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/\#how_do_image_load_and_osl_impact_performance_gains)

We analyzed the impact on TTFT and end-to-end latency in a range of experiments with 5-50 images, with each image using 128/256 token budget, keeping the OSL constant. The performance, both TTFT and end-to-end latency, degrades in the aggregated encoder scenario, while the performance is relatively constant for both disaggregated topologies.

![Two side-by-side line charts showing aggregated TTFT rising steeply with image count while both EPD topologies stay flat.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/mean-ttft-versus-visual-token-load.webp)_Figure 5. Mean TTFT versus visual-token load (5 to 50 images, OSL 512). Aggregated latency rises steeply with visual tokens (image count times token per image) image count; both EPD topologies stay nearly flat_

Next, we varied OSL from 128 to 2,048 while holding the image load fixed at five images. TTFT remains largely unchanged as OSL increases, but decode time increasingly dominates end-to-end latency. Consequently, heterogeneous EPD end-to-end gain over aggregated serving narrows from 20.3% to 5.2%. Co-located encoder shifts from an 11.8% gain to a 2.5% regression because its additional encoder workers share the same GPUs as the PD workers. As OSL increases and decode pressure grows, GPU contention increasingly offsets, and eventually outweighs, the benefit of encoder disaggregation.

![Line chart showing EPD end-to-end latency advantage over aggregated narrowing as OSL increases.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/mean-e2e-latency-versus-osl.webp)_Figure 6. Mean end-to-end latency versus OSL. The end-to-end gap between EPD and aggregated narrows as OSL grows because decode time increasingly dominates_

Figures 7 and 8 show percentage improvements in TTFT and end-to-end latency over the aggregated (baseline) across a range of OSL and image load. Encoder disaggregation delivers the most value with high input media load in almost all scenarios. In scenarios with high OSL and low image load, disaggregating the encoder compromises performance.

![Two heat maps showing 25–93% TTFT improvement over aggregated, with strongest gains at high image counts.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/two-heatmaps-co-located-encoder-disaggregated-encoder.webp)_Figure 7. Input image load (number of images times visual tokens). TTFT improvement over aggregated (Qwen 3.5 122B NVFP4). Colocated EPD (top) and heterogeneous EPD (bottom). Both topologies deliver 25-93% TTFT improvement across the full grid. The heaviest cell (50 x 128 images, any OSL) reaches 92-93%. Gains are consistent across the OSL dimension because TTFT is not affected by output length_

![Two heat maps showing end-to-end gains largest at high image load and short OSL, shrinking with lighter media and longer outputs. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/two-heatmaps-e2e-gains.webp)_Figure 8. End-to-end request latency improvement over aggregated (same model and hardware). Gains are strong at high image load and short OSL, shrinking toward the upper-left corner (light media, long outputs). Colocated EPD shows slight end-to-end regression at 5 x 128 images / OSL 2048 (-2.5%), where embedding transfer overhead is not recovered by encoder capacity savings_

## How do model size and precision change EPD gains? [Scroll to How do model size and precision change EPD gains? section](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/\#how_do_model_size_and_precision_change_epd_gains)

As model size grows, the LLM accounts for more of the serving workload, while the vision encoder remains roughly the same size. To quantify how this affects EPD, we ran a model-size ablation across Qwen3.5 4B, Qwen3.5 9B, and Qwen3.5 27B. The ViT parameter share decreases from 7.2% at 4B to 4.7% at 9B and 1.7% at 27B. Colocated EPD follows the same trend, delivering 2.62x, 1.50x, and 0.65x the goodput of aggregated serving, respectively.

![Bar chart showing colocated EPD goodput over aggregated declining with model size and rising with MoE/quantization. ](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/same-slo-gain-versus-aggregated-serving.webp)_Figure 9. Same-SLO goodput gain versus aggregated serving across model configurations. EPD gain decreases with model size and falls below break-even at 27B. Lower-precision and MoE models with less activated parameters show larger gains_

Parameter share is only a proxy for the more direct factor: runtime balance among ViT forward, LLM prefill, and decode. EPD provides more benefit when ViT forward accounts for a meaningful portion of request processing time. As prefill and decode become dominant, there is less encoder work to optimize. In our 27B configuration, the LM costs outweighed the benefit of separating the encoder under a colocated setup.

We measured how LLM precision affects EPD gain. When both the vision encoder and the LLM used BF16, colocated EPD delivered 1.78x the goodput of aggregated serving. Quantizing only the active LM weights to [NVFP4](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/) increased this gain to 2.64x.

![Bar chart showing co-located EPD goodput rising from 1.78x to 2.64x when LLM precision drops from BF16 to NVFP4.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/quantizing-llm-increases-epd-goodput-gain.webp)_Figure 10. Effect of LLM quantization on EPD goodput. Bars show colocated EPD goodput relative to aggregated serving. Quantizing the active LM weights from BF16 to NVFP4 increased the ratio from 1.78x to 2.64x. The vision encoder remained in BF16 in both configurations_

NVFP4 accelerates LLM prefill and decode while ViT forward remains in BF16, shifting a larger share of request time to encoder work. This provides EPD with more room to schedule encoder workload independently from PD workers.

### How EPD helps mixed modality requests [Scroll to How EPD helps mixed modality requests section](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/\#how_epd_helps_mixed_modality_requests)

Production workloads often mix text-only and multimodal requests, and the two request types may be scheduled together for prefill. With aggregated serving, one worker handles both vision encoding and LLM prefill. If a batch includes a multimodal request, the worker completes media preprocessing and ViT forward before starting prefill. Text-only requests do not need this work, but can still wait for it, increasing their TTFT.

EPD removes this dependency by running vision encoding on separate encoder workers. The front end routes both request types to a prefill worker, but only multimodal requests with missing embeddings invoke the encoder pool. Text-only requests can proceed to prefill while the encoder processes multimodal requests independently, reducing head-of-line blocking between the two request types.

To measure this, we compared aggregated serving with co-located encoder under sustained mixed text and image traffic.

![Bar chart showing co-located EPD cutting text TTFT by 42% and image TTFT by 31% under 50/50 mixed traffic.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/epd-reduces-ttft-mixed-traffic.webp)_Figure 11. Mean TTFT for text and image requests under sustained 50:50 mixed traffic at OSL 128, comparing aggregated serving with co-located encoder_

Encoder disaggregation reduced mean TTFT for text requests from 92.3 to 53.3 ms, a 42.2% reduction. Image-request TTFT fell from 289.9 to 200.6 ms, a 30.8% reduction. Image requests still incur encoder latency, whereas text requests can begin LLM prefill without waiting for vision encoding to complete. This accounts for the larger relative improvement in text-request TTFT.

## How to select the best encoder topology [Scroll to How to select the best encoder topology section](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/\#how_to_select_the_best_encoder_topology)

The best encoder placement depends on where request time is spent. EPD provides the most value when vision encoding represents a significant part of request processing, such as with media-heavy inputs, short to medium outputs, smaller or quantized models, and mixed traffics. Aggregate serving remains a good fit when media processing is light or long decode sequences dominate the latency.

Hardware also affects the placement decision. On homogeneous clusters, co-located encoder separates encoder scheduling and batching without reserving an entire GPU for the relatively lightweight vision model. A separate encoder tier is more useful with heterogeneous hardware, where lower-tier GPUs can run the encoder while higher-end GPUs remain dedicated to PD.

Note that [vLLM](https://github.com/vllm-project/vllm/issues/52409) and [SGLang](https://github.com/sgl-project/sglang/issues/24945) have roadmaps for further development of their EPD stacks.

## Get started with EPD disaggregation [Scroll to Get started with EPD disaggregation section](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/\#get_started_with_epd_disaggregation)

To reproduce the experiments featured in this post, follow the [ai-dynamo/dynamo](https://github.com/ai-dynamo/dynamo/tree/release/1.5.0/benchmarks/multimodal/sweep/experiments/epd) GitHub guide.

As shown in Figure 1, 43% of TTFT was spent before ViT even started. EPD does not help optimize those stages of the pipeline. Try the other levers listed below in Dynamo to address different stages of your stack with it.

[Parallel media decoding](https://docs.nvidia.com/dynamo/dev/multimodal/parallel-media-decoding) moves download and decode out of the worker and into the Dynamo front end, which ships decoded pixels to the backend. In an encoder-only benchmark at 30×256 on one GB200 with two encode workers, it cut mean encoder request latency 26%, from 281.3 ms to 207.0 ms, and P99 23%, from 752.1 ms to 581.7 ms, at matched throughput. Enable it with `--frontend-decoding`.

[Embedding cache](https://docs.dynamo.nvidia.com/dynamo/dev/multimodal/embedding-cache) stores and offloads computed embeddings in CPU DRAM so repeated media is not re-encoded. When the same multimodal content, such as an image or video, appears in multiple requests, the cached embedding is reused instead of running the vision encoder again.

[Multimodal KV routing](https://docs.nvidia.com/dynamo/dev/multimodal/multimodal-kv-routing) hashes media content alongside text in the Dynamo KV-aware router, so requests sharing media land on workers already holding the relevant KV blocks. Without it, every image looks like the same placeholder token to the router.

### Acknowledgments [Scroll to Acknowledgments section](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/\#acknowledgments)

_We’d like to thank Roger Wang, co-founder of Inferact, for his feedback on this post, and the NVIDIA team, Alexandre Milesi, Ayush Agarwal, Guan Luo, Indrajit Bhosale, J Wyman, Kris Hung, Krishnan Prashanth, Qi Wang, and Zhongdao Ren for their core work on multimodality support in Dynamo._

[Discuss (0)](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/#entry-content-comments)

+9

Like

## Tags

[Agentic AI / Generative AI](https://developer.nvidia.com/blog/category/generative-ai/) \| [Computer Vision / Video Analytics](https://developer.nvidia.com/blog/category/computer-vision/) \| [Developer Tools & Techniques](https://developer.nvidia.com/blog/category/development/) \| [General](https://developer.nvidia.com/blog/recent-posts/?industry=General) \| [Dynamo](https://developer.nvidia.com/blog/recent-posts/?products=Dynamo) \| [Intermediate Technical](https://developer.nvidia.com/blog/recent-posts/?learning_levels=Intermediate+Technical) \| [Deep dive](https://developer.nvidia.com/blog/recent-posts/?content_types=Deep+dive) \| [AI Agent](https://developer.nvidia.com/blog/tag/ai-agent/) \| [AI Inference](https://developer.nvidia.com/blog/tag/ai-inference-microservices/) \| [Low-Latency Inference](https://developer.nvidia.com/blog/tag/low-latency-inference/) \| [Mixture of Experts (MoE)](https://developer.nvidia.com/blog/tag/mixture-of-experts-moe/) \| [NVFP4](https://developer.nvidia.com/blog/tag/nvfp4/)

## About the Authors

![Avatar photo](https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/cropped-jesse-gu-1-262x262.webp)

**About Jesse Gu**


Jesse (Zhuangcheng) Gu is a Summer 2026 systems software engineering intern on the Dynamo team focused on multimodal inference serving optimization. He is a master’s student at Carnegie Mellon University, focusing on AI engineering and systems. Previously, he has worked on inference optimization and VLM post-training at Shanghai AI Lab on projects such as MinerU, and has also collaborated with the SGLang RL/multimodal teams on feature development and model support.




[View all posts by Jesse Gu](https://developer.nvidia.com/blog/author/zcgu/)

![Ryan McCormick](https://developer-blogs.nvidia.com/wp-content/uploads/2023/08/cropped-ryan-mccormick-262x262.png)

**About Ryan McCormick**


Ryan McCormick is an engineering manager on the NVIDIA Dynamo team, focused on high-performance distributed inference, self-hosted agents at scale, and optimizing multimodal workloads across datacenter infrastructure. He holds bachelor’s degrees in Computer Science and Mathematics from Binghamton University.




[View all posts by Ryan McCormick](https://developer.nvidia.com/blog/author/rmccormick/)

![Avatar photo](https://developer-blogs.nvidia.com/wp-content/uploads/2025/09/cropped-akshatha-kamath-262x262.jpg)

**About Akshatha Kamath**


Akshatha Kamath is a product manager at NVIDIA enabling efficient memory management for AI inference. She holds an MBA and a master’s degree in Data Science for Education from Stanford University. She brings experience developing and scaling ML/AI applications across industries, including AI-powered legal research at LawPavilion in Nigeria.




[View all posts by Akshatha Kamath](https://developer.nvidia.com/blog/author/akshathak/)

## Comments

### Start the discussion at [forums.developer.nvidia.com](https://forums.developer.nvidia.com/t/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/382831)

- [![](https://developer-blogs.nvidia.com/wp-content/uploads/2026/08/5370350-gtc26-berlin-mktg-kit-golden-ticket-email-footer-1360x180-copy.webp)](https://developer.nvidia.com/gtc-golden-ticket-contest)
- [![](https://developer-blogs.nvidia.com/wp-content/uploads/2026/08/5370463-gtc26-berlin-training-mktg-kit-email-footer-1360x180-copy.webp)](https://www.nvidia.com/gtc/)

ClosePrevious

![](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/)

![](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/)

Next

- [L](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fwhen-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving%2F)
- [T](https://twitter.com/intent/tweet?text=When+to+Use+Encode-Prefill-Decode+Disaggregation+to+Accelerate+Multimodal+Model+Serving+%7C+NVIDIA+Technical+Blog+https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fwhen-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving%2F)
- [F](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fwhen-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving%2F)
- [R](https://www.reddit.com/submit?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fwhen-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving%2F&title=When+to+Use+Encode-Prefill-Decode+Disaggregation+to+Accelerate+Multimodal+Model+Serving+%7C+NVIDIA+Technical+Blog)
- [E](mailto:?subject=I%27d%20like%20to%20share%20a%20link%20with%20you&body=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fwhen-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving%2F)

- [Join](https://developer.nvidia.com/login)