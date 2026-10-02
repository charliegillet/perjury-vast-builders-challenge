# StreamingVLM: Real-Time Understanding for Infinite Video Streams

Ruyi Xu¹\*, Guangxuan Xiao¹\*, Yukang Chen¹, Liuning He¹, Yao Lu², Song Han¹,²

¹MIT, ²NVIDIA

(\\* indicates equal contribution)

[Demo](https://streamingvlm.hanlab.ai/)

[Paper](https://arxiv.org/abs/2510.09608)

[Code](https://github.com/mit-han-lab/streaming-vlm)

[Slides](https://github.com/mit-han-lab/streaming-vlm/blob/main/assets/StreamingVLM_slides.pdf)

[Poster](https://hanlab.mit.edu/projects/streamingvlm#)

## News

## Awards

No items found.

## Competition Awards

No items found.

## Abstract

Vision-language models (VLMs) could power real-time assistants and autonomous agents, but they face a critical challenge: understanding near-infinite video streams without escalating latency and memory usage. Processing entire videos with full attention leads to quadratic computational costs and poor performance on long videos. Meanwhile, simple sliding window methods are also flawed, as they either break coherence or suffer from high latency due to redundant recomputation. In this paper, we introduce StreamingVLM, a model designed for real-time, stable understanding of infinite visual input. Our approach is a unified framework that aligns training with streaming inference. During inference, we maintain a compact KV cache by reusing states of attention sinks, a short window of recent vision tokens, and a long window of recent text tokens. This streaming ability is instilled via a simple supervised fine-tuning (SFT) strategy that applies full attention on short, overlapped video chunks, which effectively mimics the inference-time attention pattern without training on prohibitively long contexts. For evaluation, we build Inf-Streams-Eval, a new benchmark with videos averaging over two hours that requires dense, per-second alignment between frames and text. On Inf-Streams-Eval, StreamingVLM achieves a 66.18% win rate against GPT-4o mini and maintains stable, real-time performance at up to 8 FPS on a single NVIDIA H100.

### **The Challenge: Infinite Video Overwhelms Existing VLMs**

Current VLMs are not designed for continuous, real-time video streams. Their core attention mechanisms break down when faced with long-running inputs, making them impractical for real-world applications.

![](https://cdn.prod.website-files.com/64f4e81394e25710d22d042e/68f2ebf02e97ef6e1a30bfa2_streamingvlm.png)

- **(a) Full Attention:** The computational cost grows quadratically ($O(T^2)$) with video length, quickly leading to out-of-memory (OOM) errors and unacceptable latency.
- **(b) Sliding Window (No Overlap):** To manage memory, the context is frequently reset. This breaks temporal coherence, causing the model to lose track of what happened moments ago.
- **(c) Sliding Window (With Overlap):** This preserves some recent context but is highly inefficient. Attention is recomputed over the overlapping tokens in every single step, leading to high latency that prevents real-time performance.

### **Our Solution: A Unified Framework for Streaming Perception**

StreamingVLM introduces a unified training and inference framework that enables efficient and coherent understanding of infinite video streams.

#### **1\. Efficient Inference with a Streaming-Aware KV Cache**

At the core of our inference strategy is a compact, fixed-size KV cache that intelligently manages context. Instead of letting the cache grow indefinitely, we reuse the states of:

- **Attention Sinks:** A small set of initial tokens that anchor the attention mechanism and stabilize performance over long sequences.
- **A Short Vision Window:** The most recent video frames (e.g., 16 seconds) to track immediate, ongoing actions.
- **A Long Text Window:** A longer history of recent text tokens to maintain conversational context and long-term memory.

This asymmetric design keeps latency low while preserving all the necessary context for coherent, long-horizon reasoning. To prevent positional drift when old tokens are evicted, we use **Contiguous RoPE**, which shifts positional indices to keep them in-distribution and stable.

![](https://cdn.prod.website-files.com/64f4e81394e25710d22d042e/68f2ec012e97ef6e1a30c5ac_inference.png)

Our inference scheme maintains a stable KV cache by retaining attention sinks, a long window of recent text, and a short window of recent vision, while evicting older tokens.

#### **2\. Aligned Training on Overlapped Chunks**

How do we teach the model this streaming behavior without training on prohibitively long videos? We use a simple but powerful SFT strategy: the model is trained with **full attention on short, temporally-overlapped video chunks** (e.g., training on 24-second clips that overlap by 12 seconds). This design naturally forces the model to learn the desired attention pattern—relying on initial tokens (sinks) and a sliding window of recent context—perfectly aligning the training process with our efficient inference scheme.

![](https://cdn.prod.website-files.com/64f4e81394e25710d22d042e/68f2ec0d9d5600c7e45857f8_training.png)

Our training strategy (right) uses full attention on overlapped chunks to mimic the effective attention pattern of our streaming inference method (left), bridging the train-inference gap.

### **Performance Highlights**

#### **Real-Time Speed and Stability**

StreamingVLM is not just accurate; it's truly real-time. It maintains a low and stable per-token latency, processing video at up to **8 FPS on a single NVIDIA H100 GPU**. Unlike other methods, its performance does not degrade as the video gets longer.

![](https://cdn.prod.website-files.com/64f4e81394e25710d22d042e/68f2ec36048bef5077299244_efficiency.png)

Latency comparison of different methods. StreamingVLM (purple line) stays consistently low and stable, well below the real-time threshold, while others eventually fail or become too slow.

#### **State-of-the-Art Long-Video Understanding**

On our challenging **Inf-Streams-Eval** benchmark, which features videos averaging over two hours, StreamingVLM significantly outperforms strong baselines.

- Achieves a **66.18% win rate** against GPT-40 mini.
- Our SFT strategy boosts performance on general VQA tasks without any VQA-specific training, improving scores on **LongVideoBench by +4.30** and **OVOBench Realtime by +5.96**.

![](https://cdn.prod.website-files.com/64f4e81394e25710d22d042e/68f2ec42af49b73061da1af2_example.png)

StreamingVLM provides coherent, real-time commentary with long-term memory, addressing the failures of other models which suffer from incoherence, high latency, or memory loss.

### **Inf-Streams: A New Benchmark for Infinite Video**

To spur research in this area, we introduce a new suite of data and evaluation tools. The process involves collecting over 6,000 hours of sports footage, performing ASR, and using a GPT-5-based pipeline for cleaning and annotation.

- **Inf-Streams-Train:** A 4000+ hour SFT dataset for training streaming VLMs.
- **Inf-Streams-Eval:** A new benchmark with videos averaging over 2 hours to test dense, per-second, long-horizon understanding.

![](https://cdn.prod.website-files.com/64f4e81394e25710d22d042e/68f2ec4caf49b73061da1b11_data.png)

Our pipeline for creating the Inf-Streams dataset, from video collection and ASR to LLM-based cleaning and segmentation.

‍

## Video

YouTube

Tap to unmute

Video unavailable

[Visit YouTube to search for more videos](https://www.youtube.com/)

Video unavailable

This video contains content from NFL, who has blocked it from display on this website or application
<a href='http://www.youtube.com/watch?v=9f4mZ1GbUoU&feature=emb\_err\_woyt' target='\_blank'>Watch on YouTube</a>

[Watch on YouTube](http://www.youtube.com/watch?v=9f4mZ1GbUoU)

## Citation

@misc{xu2025streamingvlmrealtimeunderstandinginfinite,

title={StreamingVLM: Real-Time Understanding for Infinite Video Streams},

author={Ruyi Xu and Guangxuan Xiao and Yukang Chen and Liuning He and Kelly Peng and Yao Lu and Song Han},

year={2025},

eprint={2510.09608},

archivePrefix={arXiv},

primaryClass={cs.CV},

url={https://arxiv.org/abs/2510.09608}

}

## Media

No media articles found.

#### Acknowledgment

#### Team Members

[Guangxuan Xiao](https://hanlab.mit.edu/team/guangxuan-xiao)

[Song Han](https://hanlab.mit.edu/team/song-han)

[Yukang Chen](https://hanlab.mit.edu/team/yukang-chen)

Categories

[Efficient AI Algorithm](https://hanlab.mit.edu/categories/algorithm)

Topics

[Large Language Models (LLMs)](https://hanlab.mit.edu/topics/llm)

[Generative AI](https://hanlab.mit.edu/topics/generative-ai)

Techniques

[New Architecture](https://hanlab.mit.edu/techniques/new-architecture)