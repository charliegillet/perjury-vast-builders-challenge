# 01 — Fast / Real-Time Video Understanding: Models & Techniques (sweep as of 2026-10-02)

> **Cleanup note (2026-10-02):** some raw captures and docs cited below were moved to [`unwanted/`](../../unwanted/README.md) with their paths preserved (e.g. `docs/sources/x.md` is now `unwanted/docs/sources/x.md`). See `unwanted/MANIFEST.tsv`.

**Purpose:** pick what makes UNWATCHED's 5 s CCTV verify step **faster and more accurate on one GPU today**.
**Method:** 35 firecrawl searches + 35 page scrapes, saved under `.firecrawl/trend-models-*` (search JSON = `s*`, page captures = `p*`). Each number below cites the page it came from. **[UNVERIFIED]** means the figure only appeared in a search snippet or on a secondary/vendor page, and we did not confirm it on the primary source.

---

## TL;DR for the team

1. **Swap verifier → Cosmos3-Nano (Reasoner) if the venue serves it.** On VANTAGE-Bench Event Verification it scores **68.88** macro-F1 vs **64.09** for Cosmos-Reason2-8B. Cosmos3-Super reaches 71.28 with balanced sensitivity/specificity (72.1/72.9). Reason2-8B's specificity is only **57.6**: it accepts events that didn't happen. Cosmos3-Edge (4B) gets 63.36, which is Reason2-8B accuracy at half the size. ([vantage-bench.org](https://vantage-bench.org/), [arXiv 2609.09396](https://arxiv.org/html/2609.09396))
2. **Output length matters more than model choice for latency.** NVIDIA's own numbers for CR2-8B FP8 on H100: a 10 s chunk takes **0.58 s with a 1-token Yes/No answer** and **1.23 s with a 100-token caption**. Our verifier asks for `<think>` CoT with `max_tokens=1024` (`src/verifier_backends.py:112-118`), so it pays for roughly 10× the decode. Make the gate a short-answer call and generate CoT only for clips that pass. ([VSS RT-VLM perf](https://docs.nvidia.com/vss/3.2.0/performance-rt-vlm.html))
3. **Turn on EVS in vLLM:** `--video-pruning-rate 0.5..0.75`. It prunes temporally static patches, and a fixed CCTV camera is almost entirely static patches. The paper reports up to 4× lower LLM TTFT at q=0.75. NVIDIA says the Cosmos Reason NIM already uses EVS. ([vLLM engine args](https://docs.vllm.ai/en/stable/configuration/engine_args/), [EVS paper](https://www.alphaxiv.org/abs/2510.14624), [Cosmos 3 blog](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/))
4. **Embedder gotcha:** `Cosmos-Embed1-448p-anomaly-detection` outputs **768-d** vectors. Our pipeline assumes **256-d**, which is the 224p variant. Switching means re-indexing and rebuilding the centroids. The model is tuned for **8 frames at 1–2 fps**, and it was fine-tuned on **5 s chunks**, which matches our segment length exactly. ([HF card](https://huggingface.co/nvidia/Cosmos-Embed1-448p-anomaly-detection), [VSS docs](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html))

---

## 1. Model landscape, ranked for *our* job (5 s fixed-camera clip → "did event X really happen?")

Ranking order: accuracy on fixed-camera event verification first, then latency on one GPU, then whether we can deploy it today.

| # | Model | Params | License | Video latency / throughput (reported) | Streaming? | Notes for UNWATCHED | Link |
|---|---|---|---|---|---|---|---|
| 1 | **Cosmos3-Super (Reasoner)** | 64B (32B reasoner + 32B gen) | OpenMDW-1.1 | RTX PRO 6000: **535 ms** (1-tok out, 1 fps video, c=1); **5.2 s** at 100-tok out. H100 NVL: 522 ms (1-tok) | No (clip) | Best open model on VANTAGE (63.62 overall, EV 71.28, spec 72.9). Too slow for every clip; fine as a 3% verify tier. | [HF blog](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai), [benchmarks](https://github.com/NVIDIA/cosmos/blob/main/inference_benchmarks.md) |
| 2 | **Cosmos3-Nano (Reasoner)** | 16B (8B reasoner + 8B gen) | OpenMDW-1.1 | RTX PRO 6000: **146 ms** (1-tok, 1 fps), **866 ms** (100-tok); 2 fps ≈ 229 ms / 967 ms | No | **Our pick.** EV 68.88, overall 60.67 (#5 overall, #2 open). 4 fps video recommended, 256K context. NIM: `nvcr.io/nim/nvidia/cosmos3-reasoner`, `NIM_MODEL_SIZE=nano`. | [model card](https://huggingface.co/nvidia/Cosmos3-Nano), [blog](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/) |
| 3 | **Cosmos-Reason2-8B** | 8B | NVIDIA Open Model License [UNVERIFIED for R2] | H100 FP8, 10 s chunk (80 frames @448², 7,840 vis tokens): **0.58 s** (1-tok), **1.23 s** (100-tok); 51 alert streams/H100; RTX Pro 6000 0.73 s / 2.23 s | Via VSS RT-VLM | Our current baseline. EV 64.09, sensitivity 71.15, **specificity 57.63** (cries wolf). FP8 weights ~17 GB. | [VSS RT-VLM perf](https://docs.nvidia.com/vss/3.2.0/performance-rt-vlm.html), [Jetson](https://www.jetson-ai-lab.com/tutorials/cosmos-reason2-vlm/) |
| 4 | **Cosmos3-Edge** | 4B | OpenMDW-1.1 | RTX PRO 6000: **142 ms** (1-tok), **503 ms** (100-tok); ~18 req/s at c=64 (1-tok) | Built for real-time / on-device | EV 63.36 at half Reason2-8B's size. Good fast pre-filter. Released Jul 2026. | [cosmos GitHub](https://github.com/nvidia/cosmos), [benchmarks](https://github.com/NVIDIA/cosmos/blob/main/inference_benchmarks.md) |
| 5 | Qwen3-VL (2B/4B/8B/32B; 30B-A3B, 235B-A22B MoE) | 2B–235B | Apache-2.0 | No first-party latency; SGLang/vLLM supported, FP8 ckpts; vLLM EVS works with Qwen3-VL (bug noted in vLLM #30847) | No | VANTAGE: 8B EV 59.39 (spec 74.6 but sensitivity only 51.0, which the paper calls "causal blindness"); 32B overall 55.38. OVO-S-Bench #2 (235B). | [tech report](https://arxiv.org/abs/2511.21631), [SGLang cookbook](https://lmsysorg.mintlify.app/cookbook/autoregressive/Qwen/Qwen3-VL) |
| 6 | Nemotron 3 Nano Omni | 30B total / 3B active (MoE) | NVIDIA Open Model [UNVERIFIED] | "9× higher throughput than other open omni models at same interactivity"; EVS (q=0.5) + Conv3D halves vision tokens; BF16/FP8/NVFP4 | No | Strong throughput option if Cosmos is unavailable. Not domain-tuned for CCTV. | [vLLM blog](https://vllm.ai/blog/2026-04-28-nemotron-omni), [arXiv 2604.24954](https://arxiv.org/html/2604.24954v1) |
| 7 | Qwen3.5 / Qwen3.5-Omni (30B-A3B) | 4B–397B | Apache-2.0 [UNVERIFIED for Omni] | Omni: 400 s of 720p video at 1 fps | Omni = real-time dialogue | VANTAGE: Qwen3.5-9B EV only 46.78. Not better than Cosmos on our task. | [Qwen3.5-Omni report](https://arxiv.org/html/2604.15804v1) |
| 8 | MiniCPM-V 4.5 | 8B (Qwen3-8B + SigLIP2-400M) | MiniCPM Model License [UNVERIFIED] | 3D-Resampler: **6 frames → 64 tokens (96× compression)**, up to 10 fps video; int4/GGUF/ollama | No | Cheapest tokens per frame among open VLMs. Possible high-fps fallback. | [GitHub doc](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/minicpm_v4dot5_en.md) |
| 9 | Molmo 2 (4B / 8B / 7B-O) | 4–8B (Qwen3-based) | Apache-2.0 (weights) | n/a | No | Best open **video tracking/pointing**: could ground "where" in the digest. Dec 2025. | [Ai2 blog](https://allenai.org/blog/molmo2) |
| 10 | InternVL3.5 (1B–241B) | 1B–241B | Apache-2.0 [UNVERIFIED per size] | ViR + decoupled ViT/LLM deploy: **up to 4.05× inference speedup** | No | OVO-S-Bench 241B #6. Mid-pack on CCTV. | [blog](https://internvl.github.io/blog/2025-08-26-InternVL-3.5/) |
| 11 | Moondream 3.1 | 9B MoE / 2B active | BSL-style [UNVERIFIED] | **59 ms P50 on H100**, 33 ms on RTX 6000 (single direct-answer *image* query) | Real-time on video streams (per keyframe) | Very fast per-frame QA. Image-centric, so it can't handle temporal events. | [moondream.ai](https://moondream.ai/) |
| 12 | Gemma 4 (E2B, E4B, 26B-A4B, 31B) | 2.3B–31B | **Apache-2.0** (first Gemma to use it) | Video ≤60 s at 1 fps; E2B runs 7.6 tok/s on Raspberry Pi 5 | No | Weak here: E2B VANTAGE overall 21.28, EV 27.65. | [datature](https://datature.io/blog/gemma-4-what-computer-vision-engineers-actually-need-to-know), [HF](https://huggingface.co/blog/gemma4) |
| 13 | StreamingVLM (MIT Han Lab) | 7B (Qwen2.5-VL base) | MIT [UNVERIFIED] | **Up to 8 fps on one H100**, flat latency over infinite stream (attention sinks + short vision window + long text window KV) | **Yes** | Good for live commentary. On OVO-S-Bench it scores 43.0, which is *below* general VLMs. Not needed for 5 s clips. | [project](https://hanlab.mit.edu/projects/streamingvlm), [GitHub](https://github.com/mit-han-lab/streaming-vlm) |
| 14 | Apple FastVLM (0.5B/1.5B/7B) | 0.5–7B | Apple research license [UNVERIFIED] | **85× faster TTFT** (0.5B vs LLaVA-OneVision-0.5B) [UNVERIFIED headline]; 3.2× TTFT vs prior works | Image-first; WebGPU real-time demo | On-device keyframe captioning. | [Apple ML](https://machinelearning.apple.com/research/fast-vision-language-models) |
| 15 | SmolVLM2 (256M/500M/2.2B) | 0.26–2.2B | Apache-2.0 | "Smallest video LMs ever"; best 2B on Video-MME at release | No | Edge toy. Too weak for verification. | [HF blog](https://huggingface.co/blog/smolvlm2) |
| — | Eagle 2.5-8B (NVIDIA) | 8B | NVIDIA non-commercial [UNVERIFIED] | 512-frame long video; Video-MME 72.4 | No | Built for long video, which isn't our setting. | [HF](https://huggingface.co/nvidia/Eagle2.5-8B) |
| — | LLaVA-OneVision-1.5 → **-2** (May 2026), Perception LM | 8B-ish | Apache-2.0 / FAIR | n/a | No | Fully open training stacks. Not useful at the hackathon. | [OV-2](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-2), [PE/PLM](https://github.com/facebookresearch/perception_models) |
| — | Dispider, Flash-VStream, VideoLLM-online, StreamBridge (Apple), LiveCC, VideoChat-Online | 7B-class | research | Proactive "when to speak" heads, memory banks | **Yes** | Research streaming stacks. **SimpleStream (Apr 2026) shows that feeding just the last 4 frames to an off-the-shelf VLM hits 67.7% on OVO-Bench / 80.59% on StreamingBench**, matching these complex memory systems. | [SimpleStream](https://arxiv.org/html/2604.02317v1), [StreamBridge](https://machinelearning.apple.com/research/proactive-streaming-assistant), [LiveCC](https://arxiv.org/abs/2504.16030) |

**Proprietary reference points (fallback only):** Gemini 3.6 Flash leads VANTAGE (69.52 overall; EV 82.00, sensitivity 87.5, spec 76.3), and GPT-5.6 Sol is close behind (68.04). ([vantage-bench.org](https://vantage-bench.org/))

### VANTAGE-Bench Event Verification breakdown (n=163; 104 positive / 59 negative)
| Model | Macro-F1 | Sensitivity (true-event recall) | Specificity (true-negative recall) |
|---|---|---|---|
| Gemini 3.6 Flash | 82.00 | 87.50 | 76.27 |
| GPT-5.6 Sol | 76.14 | 77.88 | 76.27 |
| Cosmos-Reason2-32B | 73.58 | 83.65 | 62.71 |
| **Cosmos3-Super** | 71.28 | 72.12 | **72.88** |
| Gemini 3.1 Pro | 68.57 | 71.15 | 67.80 |
| **Cosmos-Reason2-8B** | 64.09 | 71.15 | **57.63** |
| Qwen3-VL-8B | 59.39 | 50.96 | 74.58 |

Source: Table 7, [arXiv 2609.09396](https://arxiv.org/html/2609.09396). Cosmos3-Nano EV = 68.88 and Cosmos3-Edge EV = 63.36 come from Table 1. Nano and Edge have no published sensitivity/specificity split, so **measure it on our 60 clips**. The benchmark ran zero-shot with greedy decoding and **no chain-of-thought**.

---

## 2. Speed techniques: what they claim, and whether we can use them today

| Technique | What it does | Reported speedup / retention | Usable today? | Source |
|---|---|---|---|---|
| **Short output (OSL=1 Yes/No)** | Ask for a 1-token verdict instead of a caption or CoT | CR2-8B H100: 0.58 s vs 1.23 s (100 tok); Cosmos3-Super RTX6000: 0.53 s vs 5.2 s | **Yes, prompt change only** | [VSS perf](https://docs.nvidia.com/vss/3.2.0/performance-rt-vlm.html), [Cosmos bench](https://github.com/NVIDIA/cosmos/blob/main/inference_benchmarks.md) |
| **Lower video fps** | Fewer frames → fewer vision tokens | Cosmos3-Nano 1 fps vs 2 fps: 146 → 229 ms (1-tok); throughput 17.4 → 8.4 req/s at c=64 | **Yes** (`COSMOS_FPS` env already exists) | same |
| **EVS (Efficient Video Sampling)** | Drops temporally static patches before the LLM, training-free | Up to **4× lower LLM TTFT** at q=0.75; Nemotron Omni uses q=0.5 | **Yes**: `vllm serve ... --video-pruning-rate 0.6 --video-pruning-method evs` (alt: `vidcom2`) | [vLLM args](https://docs.vllm.ai/en/stable/configuration/engine_args/), [EVS](https://www.alphaxiv.org/abs/2510.14624) |
| **Skip CoT / "reason-when-necessary"** | Direct answer first, reason only if unsure | VideoAuto-R1 (CVPR 2026): direct answers often match or beat CoT at far fewer tokens | **Yes**: two-stage prompt | [efficient-video-2026](https://v-chandra.github.io/efficient-video-intelligence/) |
| FP8 / NVFP4 quantization | Smaller weights and activations | vLLM FP8: up to 2× latency reduction; NVFP4 LLM + BF16 ViT raises EPD goodput 1.78× → 2.64× | Yes if FP8 checkpoint/NIM is served (CR2 FP8 exists) | [Red Hat](https://developers.redhat.com/articles/2024/07/15/vllm-brings-fp8-inference-open-source-community), [Dynamo EPD](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/) |
| `--mm-encoder-tp-mode data`, `--async-scheduling` | ViT data-parallel; overlapped scheduling | Part of NVIDIA's recommended Cosmos3-Nano launch | Yes (self-host) | [Cosmos3-Nano card](https://huggingface.co/nvidia/Cosmos3-Nano) |
| `--mm-processor-cache-gb` | Avoids reprocessing repeated media | Qualitative | Yes (helps when the same clip goes through gate then CoT) | [vLLM args](https://docs.vllm.ai/en/stable/configuration/engine_args/) |
| Dynamo EPD disaggregation | Vision encoder on its own worker | Up to **5× TTFT, 7× E2E**; benefit shrinks when decode dominates | **No** (multi-worker; overkill for one GPU) | [NVIDIA blog](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/) |
| FastV / VisionZip / DyCoke / PruneVid / FrameFusion / ForestPrune / LLaVA-Scissor | In-LLM or pre-LLM visual token pruning/merging | ForestPrune keeps 95.8% accuracy at 90% pruning (LLaVA-OV); FastV/VisionZip drop −9.1/−7.4% at extreme ratios; DyToK 2.5× on top of VisionZip/FastV; ShaRP 5.1× fewer TFLOPs at 97.2% retention | Research code, no serving flag. **Use EVS instead.** | [ForestPrune](https://arxiv.org/html/2603.22911v2), [DyCoke](http://openaccess.thecvf.com/content/CVPR2025/papers/Tao_DyCoke_Dynamic_Compression_of_Tokens_for_Fast_Video_Large_Language_CVPR_2025_paper.pdf), [ShaRP](https://arxiv.org/html/2512.05385v2), [awesome list](https://github.com/daixiangzi/awesome-token-compress) |
| Keyframe / redundancy gating | Drop near-duplicate frames or segments before the VLM | LongVU: DINOv2 redundancy filter keeps ~45.9% of frames; LVNet >10× lower LLM cost | **Yes**: our embedding-distance scorer already does this at the segment level | [efficient-video-2026](https://v-chandra.github.io/efficient-video-intelligence/), [LVNet](https://github.com/jongwoopark7978/LVNet) |
| Streaming KV reuse (attention sinks + windows) | Fixed-size KV cache for infinite streams | StreamingVLM: 8 fps on H100, flat latency | Not needed for 5 s clips | [StreamingVLM](https://hanlab.mit.edu/projects/streamingvlm) |
| Speculative decoding for VLMs (SpecVLM, ViSpec, ParallelVLM) | Draft model proposes tokens | SpecVLM 1.5–2.3× E2E; ParallelVLM lossless for Video-LLMs (CVPR 2026) | No (helps long outputs only; we want short outputs anyway) | [SpecVLM](https://arxiv.org/html/2509.11815v1), [ParallelVLM](https://openaccess.thecvf.com/content/CVPR2026/papers/Kong_ParallelVLM_Lossless_Video-LLM_Acceleration_with_Visual_Alignment_Aware_Parallel_Speculative_CVPR_2026_paper.pdf) |
| Event cameras | Per-pixel async brightness events | µs latency | No (needs different hardware) | [UZH RPG](https://rpg.ifi.uzh.ch/research_dvs.html) |
| SGLang for Qwen3-VL | `SGLANG_USE_CUDA_IPC_TRANSPORT=1`, `--mm-feature-transport=cuda_ipc` | "Significantly improves TTFT" (qualitative) | Only if we self-host Qwen | [SGLang cookbook](https://lmsysorg.mintlify.app/cookbook/autoregressive/Qwen/Qwen3-VL) |

---

## 3. Fast video embeddings / retrieval & training-free VAD

| Embedder | Dim | Input | Latency | License | Fit for UNWATCHED baseline | Source |
|---|---|---|---|---|---|---|
| **Cosmos-Embed1-224p** (current) | **256** | 8 frames @224² | fast (local GPU; no published ms) | NVIDIA Open Model License (commercial OK) | What VSS ships by default | [VSS docs](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html) |
| **Cosmos-Embed1-448p-anomaly-detection** | **768** | 8 frames @448², 1–2 fps; LoRA on Vad-Reasoning **5 s chunks** (UCF-Crime, XD-Violence, TAD, ShanghaiTech, UBnormal, ECVA) | slower than 224p (4× pixels) [UNVERIFIED ms] | NVIDIA Open Model License | **Best-matched to our task.** Re-index required (256→768). | [HF card](https://huggingface.co/nvidia/Cosmos-Embed1-448p-anomaly-detection) |
| Twelve Labs Marengo 3.0 | 512 | any-to-any | ~0.05 s per second of video (vendor claim); ~10 s for a ≤60 s clip | API | Too slow per call for 5 s segments; vendor numbers | [Twelve Labs](https://www.twelvelabs.io/blog/marengo-3-0) |
| Gemini Embedding 2 | 3072 | video | 2.1 s | API | Top text→video NDCG@10 (0.764) in Mixpeek benchmark | [mixpeek bench](https://github.com/mixpeek/video-embedding-benchmark) |
| X-CLIP Base | 512 | temporal | 192 ms local | MIT | Best open model in that benchmark (NDCG@10 0.470) | same |
| SigLIP 2 SO400M (frame-avg) | 1152 | frames | 636 ms | Apache-2.0 | Frame averaging loses temporal information (NDCG@10 0.325) | same; [HF](https://huggingface.co/blog/siglip2) |
| InternVideo2-6B | 768 | video | 24.8 s | — | Slow, weak zero-shot | same |
| Meta Perception Encoder (PE-core) | — | image/video (8 uniform frames) | — | FAIR license | "Outperforms SigLIP2"; no video-native temporal module | [GitHub](https://github.com/facebookresearch/perception_models) |
| VideoPrism (Google) | — | video | — | — | Research only | [Google](https://research.google/blog/videoprism-a-foundational-visual-encoder-for-video-understanding/) |

**Training-free VLM VAD, 2026 state of the art:** LAVAD (caption → LLM scoring) is still the reference design. 2026 follow-ups include PRISM (OpenReview), CoReVAD ([arXiv 2605.23116](https://arxiv.org/html/2605.23116v1)), ReCI (retrieval-guided; [ACM](https://dl.acm.org/doi/10.1145/3805622.3810823)), and ASK-Hint (fine-grained prompting, WACV 2026; [PDF](https://openaccess.thecvf.com/content/WACV2026/papers/Zou_Unlocking_Vision-Language_Models_for_Video_Anomaly_Detection_via_Fine-Grained_Prompting_WACV_2026_paper.pdf)). All report SOTA among training-free methods on UCF-Crime / XD-Violence. The common thread is **context and retrieval of "normal" plus class-specific prompts**, which supports our per-camera centroid design plus class-specific verify prompts. An MDPI CCTV study shows prompting alone moves compact VLMs a lot: InternVL3-2B F1 went 0.49 → 0.90 with better prompts, and Qwen2.5-VL-7B reached F1 0.90 at 3.7 s per clip. ([PMC12653427](https://pmc.ncbi.nlm.nih.gov/articles/PMC12653427/))

---

## 4. Streaming / real-time benchmarks: who leads

| Benchmark | Leader (as captured) | Notable | Source |
|---|---|---|---|
| **VANTAGE-Bench** (fixed infra cameras; NVIDIA + Clemson, leaderboard live 2026-05-27) | Gemini 3.6 Flash 69.52 → GPT-5.6 Sol 68.04 → **Cosmos3-Super 63.62** (best open) → Gemini 3.1 Pro 62.66 → Cosmos3-Nano 60.67 | Event Verification drops 9–24 pts vs consumer benchmarks at every scale | [site](https://vantage-bench.org/), [paper](https://arxiv.org/html/2609.09396) |
| **OVO-S-Bench** (InternLM, EMNLP 2026) | Gemini-3.1-Pro 59.2 → Qwen3-VL-235B 53.6 → Qwen3.5-397B 52.1 | **Dedicated streaming models (StreamForest 44.1, StreamingVLM 43.0) trail general VLMs**; humans 86.6 | [GitHub](https://github.com/InternLM/OVO-S-Bench) |
| OVO-Bench | ByteDance Seed 2.1 Pro 0.807 (LLM-Stats, 4 models tracked) [UNVERIFIED aggregator] | SimpleStream (4 recent frames) 67.7% | [LLM-Stats](https://llm-stats.com/benchmarks/ovobench), [SimpleStream](https://arxiv.org/html/2604.02317v1) |
| OVBench | Seed 2.1 Pro (LLM-Stats) [UNVERIFIED] | — | [LLM-Stats](https://llm-stats.com/benchmarks/ovbench) |
| StreamingBench | Official page still shows 2024–25 entries (Gemini 1.5 Pro 70.26, MiniCPM-o 2.6 66.01); SimpleStream reports 80.59% | Leaderboard looks stale | [site](https://streamingbench.github.io/) |
| AI City Challenge 2026 Track 3 (Traffic Anomaly Reasoning) | New leaderboard cited by NVIDIA for Cosmos 3 | Not scraped [UNVERIFIED] | [leaderboard](https://eval.aicitychallenge.org/aicity2026/submission/leaderboard?trackId=3&type=general) |

**Takeaway:** for 5 s clips, "streaming" architectures don't help. Use the strongest clip model with a short output. SimpleStream and OVO-S-Bench both show that recent-frame plus general VLM is as good as or better than the streaming stacks.

---

## 5. What we can use TODAY at the hackathon (concrete, in priority order)

1. **Ask the venue at 10:00 which Cosmos is served.** Preference order for the verify tier: **Cosmos3-Super > Cosmos3-Nano > Reason2-8B**. If self-hosting on one GPU: Nano fits on RTX PRO 6000 / H100 (≈30 GB est. [UNVERIFIED, classmethod](https://dev.classmethod.jp/en/articles/dgx-spark-cosmos3-family-usecase-map/)). NIM: `docker run --gpus=all -e NGC_API_KEY -e NIM_MODEL_SIZE=nano -p 8000:8000 nvcr.io/nim/nvidia/cosmos3-reasoner:latest`.
2. **Two-stage verify prompt (biggest latency win, zero infra).**
   - *Stage A (gate):* class-specific question, answer `YES`/`NO` only, `max_tokens≈4`, no `<think>`, `temperature=0`. Expected cost per clip: ~0.15 s (Nano) to ~0.6 s (R2-8B / Super).
   - *Stage B (only on YES):* the current CoT + JSON prompt at `max_tokens=1024`, to produce the on-screen explanation.
   - VANTAGE scores were all produced *without* CoT. Measure A-only vs A+B specificity on our ~60 labeled clips in Weave before we claim anything.
3. **Set `COSMOS_FPS=2`** (env already supported in `src/verifier_backends.py:104`) instead of the NIM default of 4 fps. A 5 s clip becomes 10 frames. Nano numbers show 1→2 fps roughly halves throughput, so 4 fps costs about double again. A/B test 2 vs 4 fps on the labeled set.
4. **If we self-host vLLM, add** `--video-pruning-rate 0.6 --mm-encoder-tp-mode data --async-scheduling --mm-processor-cache-gb 4`. Fixed cameras have mostly static patches, which is the ideal case for EVS. Watch vLLM issue [#30847](https://github.com/vllm-project/vllm/issues/30847) (EVS + Qwen3-VL bug) and check that output is sane on Cosmos.
5. **Embedder:** try `Cosmos-Embed1-448p-anomaly-detection` (8 frames, 1–2 fps, trained on 5 s chunks). **Vectors become 768-d, so rebuild the VastDB column, centroids, and the all-zero-vector filter.** If GPU time is tight, keep 224p (256-d) for the baseline and use the AD variant only to re-score the top outliers.
6. **Optional fast pre-filter:** Cosmos3-Edge (4B, ~142 ms 1-token on RTX PRO 6000, EV 63.4) can run on *all* outliers, leaving Nano/Super for the rest. Only worth it if we see GPU contention.
7. **Do NOT spend time on:** streaming VLMs (StreamingVLM, Dispider, VideoLLM-online), Dynamo EPD, speculative decoding, or research token-pruning repos. None of them pays off within one day on 5 s clips.

### Numbers to say on stage (all sourced)
- "Cosmos-Reason2-8B accepts ~42% of events that never happened on NVIDIA's own fixed-camera benchmark (specificity 57.6). Cosmos3-Super gets that to 72.9." ([arXiv 2609.09396](https://arxiv.org/html/2609.09396))
- "A yes/no verify on a 10 s chunk takes 0.58 s on an H100. We only spend the full reasoning budget on clips that pass." ([VSS perf](https://docs.nvidia.com/vss/3.2.0/performance-rt-vlm.html))

---

## Capture index
Searches: `.firecrawl/trend-models-s01…s35-*.json` (streaming VLMs, Cosmos 3, Qwen3-VL, VANTAGE, OVO/StreamingBench, Cosmos-Embed, token pruning, vLLM EVS, VAD, FastVLM, Nemotron, MiniCPM, InternVL3.5, Molmo 2, SmolVLM/Moondream, Eagle 2.5, StreamBridge et al., news, Marengo, PE, SigLIP2/VideoPrism, keyframes, SGLang/TRT, Qwen3.5, Gemma 4, Reason2 NIM, Reason 3, Dynamo, spec-dec, LiveCC, LLaVA-OV, event cameras, StreamingBench, VSS perf).
Scrapes: `.firecrawl/trend-models-p01…p35-*.md`.
Caveats: Cosmos reasoner benchmark pages don't state clip duration (so ms figures are per request at the given fps) [UNVERIFIED clip length]. The "Cosmos Reason 3 Nano is the VSS 3.2.1 default" claim in FINAL-IDEA was not confirmed in this sweep; NVIDIA's public naming is "Cosmos 3 Nano Reasoner".
