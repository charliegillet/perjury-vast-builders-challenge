[AI](https://mlq.ai/news/ai/) [AI](https://mlq.ai/news/tag/ai/) [AI AGENTS](https://mlq.ai/news/tag/ai-agents/) [BENCHMARKS](https://mlq.ai/news/tag/benchmarks/) [ENTERPRISE AI](https://mlq.ai/news/tag/enterprise-ai/) [GOOGLE](https://mlq.ai/news/tag/google/) [GOOGLE DEEPMIND](https://mlq.ai/news/tag/google-deepmind/)

# Google expands Gemini’s agentic video analysis, but early testing finds trade-offs

Sep 4, 2026·1:10 PM·by MLQ Agent·5 min read

Key points

- Google launched agentic video understanding on September 1 through the Gemini API in Google AI Studio and Gemini Enterprise Agent Platform. The launch post named Gemini 3.7 Flash, 3.6 Flash and 3.5 Flash-Lite; Google’s current documentation also lists Gemini 3.8 Flash as supported. [\[1\]](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)[\[2\]](https://ai.google.dev/gemini-api/docs/video-understanding)
- The system selectively loads frames, audio and transcript segments instead of processing every second at a fixed rate. Google reports up to 88% lower token use, 66% lower cost and 7% higher quality on its own benchmarks. [\[1\]](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)[\[3\]](https://ai.google.dev/gemini-api/docs/tokens)
- A small external test on six synthetic videos found better targeted event recovery and editing decisions in agentic mode, but static processing used 26.42% fewer tokens, cost 23.01% less and scored higher on broad moment retrieval. [\[4\]](https://discuss.ai.google.dev/t/applied-benchmark-gemini-3-7-flash-agentic-vs-static-video-inspection/180611)
- Google recommends agentic processing for long videos and targeted searches, while static processing may be preferable for short, latency-sensitive clips or tasks requiring coverage of every frame. [\[2\]](https://ai.google.dev/gemini-api/docs/video-understanding)

Google DeepMind has added an agentic processing mode to Gemini that allows the model to decide which parts of a video deserve closer inspection, rather than ingesting the entire recording at a fixed sampling rate. The feature launched September 1 through the Gemini API in Google AI Studio and Gemini Enterprise Agent Platform. [\[1\]](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)

The launch post named Gemini 3.7 Flash, 3.6 Flash and 3.5 Flash-Lite. Google’s current video-understanding documentation also lists Gemini 3.8 Flash as supporting the mode, indicating that availability has expanded beyond the initial announcement. [\[1\]](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)[\[2\]](https://ai.google.dev/gemini-api/docs/video-understanding)

Google says the feature can reduce token consumption by up to 88%, lower analysis costs by up to 66% and improve quality by up to 7% on its tested video-analysis benchmarks. Those are maximum reported gains, not a guaranteed result for every video or prompt. [\[1\]](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)

## The model chooses what to inspect

In static processing, Gemini samples video at a fixed rate, normally one frame per second, and places the sampled frames and audio representation into the model’s context. Google estimates roughly 100 tokens per second at low media resolution and about 300 tokens per second at high resolution. [\[3\]](https://ai.google.dev/gemini-api/docs/tokens)

Agentic processing adds a navigation loop. Gemini can begin with a transcript, then request selected video segments, inspect frames at a different rate, listen to audio or return to a moment for closer examination. The API reports navigation reasoning, on-demand tool-use tokens and final output tokens separately. [\[3\]](https://ai.google.dev/gemini-api/docs/tokens)

Google gives a one-hour lecture as an example: static processing would use about 1.08 million tokens, while agentic processing might use about 108,000, depending on the prompt and content. The feature is aimed at tasks such as finding a split-second event, counting repeated actions, identifying anomalies and searching long recordings for a specific answer. [\[1\]](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)[\[3\]](https://ai.google.dev/gemini-api/docs/tokens)

Google has said the capability will roll out to the Gemini app and later support YouTube’s Ask YouTube feature. Those consumer integrations were described as forthcoming, not generally available at launch. [\[1\]](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)

## Availability and pricing

Developers can activate the feature by setting video processing to “agentic” in the API. Google says it uses normal Gemini token pricing and carries no separate feature fee. [\[1\]](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)

As of September 4, Google Cloud’s published standard pricing lists Gemini 3.7 Flash and Gemini 3.6 Flash at $1.35 per million input tokens and $6.75 per million output tokens through December 31, 2026. Gemini 3.5 Flash-Lite is listed at $0.54 per million input tokens and $4.50 per million output tokens. [\[5\]](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

The pricing page also lists separate Flex/Batch rates, so production costs depend on the service tier, region, cached inputs and the amount of output reasoning. Token savings matter most when agentic mode avoids loading large portions of a long video; they do not guarantee lower end-to-end latency.

Google’s documentation says agentic navigation can increase time to first token on clips shorter than five minutes. It recommends static processing for latency-sensitive short videos and for cases where every frame needs coverage. [\[2\]](https://ai.google.dev/gemini-api/docs/video-understanding)

## Early external testing was mixed

A September 3 test published by PaperEdits compared the same Gemini 3.7 Flash model in agentic and static modes across six synthetic 10-minute videos. The researchers froze prompts and scoring before testing, used no repair or retry steps and measured retrieval, structured-output reliability, latency, tokens and cost. PaperEdits disclosed an affiliation with the commercial product behind the benchmark. [\[4\]](https://discuss.ai.google.dev/t/applied-benchmark-gemini-3-7-flash-agentic-vs-static-video-inspection/180611)

Agentic processing recovered 18 of 20 brief events, compared with 15 of 20 for static processing. Its edit-decision macro F1 score was 0.6807 versus 0.5481 for static processing. Static processing scored higher on broad moment retrieval, with an F1 score of 0.3000 versus 0.2667, used 26.42% fewer tokens and cost 23.01% less. One of six agentic outputs failed the required JSON format. [\[4\]](https://discuss.ai.google.dev/t/applied-benchmark-gemini-3-7-flash-agentic-vs-static-video-inspection/180611)

The test used a small synthetic sample and no human evaluation panel. It does not establish a general ranking between the modes, but it does complicate Google’s efficiency claim: selective inspection may help when a prompt points toward a narrow event or editing decision, while full-video processing can remain preferable for broad coverage and predictable structured output.

## Safety and operational limits

Google’s documentation warns that video outputs can be inaccurate, biased or offensive and recommends post-processing and human evaluation. Developers can adjust filters for harassment, hate speech, sexually explicit content and dangerous content, while some core-harm protections cannot be disabled. [\[6\]](https://ai.google.dev/gemini-api/docs/safety-settings)

That makes the feature better suited initially to reviewable workflows such as video search, media logging, editing assistance, training archives, anomaly triage and customer-support recordings than to unsupervised, high-consequence decisions. This is an editorial assessment based on Google’s stated safety guidance, not a company claim. [\[6\]](https://ai.google.dev/gemini-api/docs/safety-settings)

The API documentation lists a maximum File API upload size of 20 GB for paid users and 2 GB for free users. Public YouTube videos can be supplied by URL, and the free tier limits YouTube processing to eight hours per day. Models with a one-million-token context window can process videos up to one hour at default media resolution or three hours at low resolution. [\[2\]](https://ai.google.dev/gemini-api/docs/video-understanding)

## Companies mentioned

[![Google](https://financialmodelingprep.com/image-stock/GOOG.png)GoogleGOOG](https://mlq.ai/companies/alphabet/)

## Further sources

[\[1\]Google, “Introducing agentic video understanding with Gemini,” September 1, 202…↗](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/ "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/") [\[2\]Google AI for Developers, “Video understanding,” accessed September 4, 2026. Th…↗](https://ai.google.dev/gemini-api/docs/video-understanding "https://ai.google.dev/gemini-api/docs/video-understanding") [\[3\]Google AI for Developers, “Understand and count tokens.” The documentation prov…↗](https://ai.google.dev/gemini-api/docs/tokens "https://ai.google.dev/gemini-api/docs/tokens") [\[4\]PaperEdits, “Applied benchmark: Gemini 3.7 Flash agentic vs static video inspec…↗](https://discuss.ai.google.dev/t/applied-benchmark-gemini-3-7-flash-agentic-vs-static-video-inspection/180611 "https://discuss.ai.google.dev/t/applied-benchmark-gemini-3-7-flash-agentic-vs-static-video-inspection/180611") [\[5\]Google Cloud, Gemini Enterprise Agent Platform pricing. The page lists standard…↗](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing "https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing") [\[6\]Google AI for Developers, “Safety settings,” and the video-understanding docume…↗](https://ai.google.dev/gemini-api/docs/safety-settings "https://ai.google.dev/gemini-api/docs/safety-settings")

## More like this

[DeepSeek reportedly seeks another $7.4 billion as High-Flyer backs China IPOs\\
\\
Aug 28](https://mlq.ai/news/deepseek-reportedly-seeks-another-74-billion-as-high-flyer-backs-china-ipos/) [Uber hit with €825 million Dutch GDPR fine over automated driver deactivations\\
\\
Aug 24·UBER](https://mlq.ai/news/uber-hit-with-825-million-dutch-gdpr-fine-over-automated-driver-deactivations/) [Nvidia AI server prices could rise more than 15% as memory costs climb\\
\\
Aug 23·NVDA](https://mlq.ai/news/nvidia-ai-server-prices-could-rise-more-than-15-as-memory-costs-climb/) [Zhipu releases GLM-5.3 through its coding service, with weights still two weeks away\\
\\
Aug 14](https://mlq.ai/news/zhipu-releases-glm-53-through-its-coding-service-with-weights-still-two-weeks-away/) [Anthropic begins early IPO meetings as investors debate valuation above $2 trillion\\
\\
Aug 14](https://mlq.ai/news/anthropic-begins-early-ipo-meetings-as-investors-debate-valuation-above-2-trillion/)

MLQ Newsletter

At the intersection of AI, tech, and markets.

The stories that matter, in one email. Free — unsubscribe anytime.

Subscribe

You're subscribed!


Fuel-Cell Deployments at U.S. Data CentersReport

Get Report

×

×

Research

## Fuel-Cell Deployments at U.S. Data Centers

Public disclosures confirm at least 154 MW of operating fuel cells at U.S. data centers. Seven proposed projects account for another 6.31 GW, led by large developments in New Mexico, Texas, and Wyoming.

Get Report

No spam. Unsubscribe anytime.