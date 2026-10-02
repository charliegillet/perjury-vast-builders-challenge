[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fgoogle-cloud%2Fvideo-understanding-with-gemini-notes-from-the-field-82dd0cd130ea&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-------------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav--------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fgoogle-cloud%2Fvideo-understanding-with-gemini-notes-from-the-field-82dd0cd130ea&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

[**Google Cloud - Community**](https://medium.com/google-cloud?source=post_page---publication_nav-e52cf94d98af-82dd0cd130ea-----------------------------------------)

·

Follow publication

[![Google Cloud - Community](https://miro.medium.com/v2/resize:fill:38:38/1*FUjLiCANvATKeaJEeg20Rw.png)](https://medium.com/google-cloud?source=post_page---post_publication_sidebar-e52cf94d98af-82dd0cd130ea-----------------------------------------)

A collection of technical articles and blogs published or curated by Google Cloud Developer Advocates. The views expressed are those of the authors and don't necessarily reflect those of Google.

Follow publication

[Video Analytics](https://medium.com/tag/video-analytics?source=post_page---header_tags--82dd0cd130ea-----------------------------------------)

[Gemini](https://medium.com/tag/gemini?source=post_page---header_tags--82dd0cd130ea-----------------------------------------)

[Google Cloud Platform](https://medium.com/tag/google-cloud-platform?source=post_page---header_tags--82dd0cd130ea-----------------------------------------)

[Google](https://medium.com/tag/google?source=post_page---header_tags--82dd0cd130ea-----------------------------------------)

[Data](https://medium.com/tag/data?source=post_page---header_tags--82dd0cd130ea-----------------------------------------)

# **Video Understanding with Gemini: Notes From the Field**

[![Sveta Morag](https://miro.medium.com/v2/resize:fill:32:32/1*w7chfWPHnoYRYcZCZeUsrw.png)](https://medium.com/@svetamorag?source=post_page---byline--82dd0cd130ea-----------------------------------------)

[Sveta Morag](https://medium.com/@svetamorag?source=post_page---byline--82dd0cd130ea-----------------------------------------)

Follow

6 min read

·

Mar 16, 2026

58

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D82dd0cd130ea&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fgoogle-cloud%2Fvideo-understanding-with-gemini-notes-from-the-field-82dd0cd130ea&source=---header_actions--82dd0cd130ea---------------------post_audio_button--------------------)

Share

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*1e08Sb_dFeOnBSpuxb7ihg.png)

Video Understanding with Gemini

After shipping several video analysis pipelines, I can tell you that teaching an AI to actually _watch_ a video is a deceptively complex engineering problem. Whether you’re working on cinematic productions or professional archives, the goal is always the same: getting high-quality results while keeping costs down.

To do this, I’ve centered my builds on five core architectural pillars:

- **Multi-Stage Agentic Chains:** Breaking analysis into “Triage” and “Deep Dive” phases.
- **Audio-First Contextualization:** Grounding visual interpretation with audio tracks.
- **Adaptive Temporal Sampling:** Balancing frame rates and reasoning budgets for precision.
- **Prompt Objectivity & The Context Trap:** Mitigating hallucination through objective instruction.
- **Context Barrier Management:** Handling extreme video lengths through chunking and hybrid context.

## The Multi-Stage Agentic Chain: Triage vs. Deep Dive

One of the most common pitfalls is the “single-request” approach — throwing a 60-minute file at a model and asking for everything at once. This often leads to reasoning truncation or missed nuances.

Instead, adopt a multi-stage workflow:

- **Initial Triage:** Use a high-efficiency model like **Gemini 3 Flash** to index the video at a low resolution. This “first pass” identifies major events, shifts in scene, and key timestamps, acting as a high-level map.
- **Audio-First Transcription (if you have audio in your video file):** Run a transcription pass before visual reasoning to create a “script”. This provides a semantic anchor that improves quality and minimizes temporal hallucinations.
- **Deep Analysis:** Once specific intervals are identified, we trigger a targeted request using a high-insight model like **Gemini 3.1 Pro**.
- **With Audio Transcript (Temporal Anchor Pattern):** If an audio transcript is available from the previous step, use it as a ‘temporal anchor’ to ground visual analysis and solve synchronization issues. The text prompt should treat the video as a referential timeline, providing a map instead of asking a vague question.

```
Example Prompt Structure (with Transcript):

"I have provided a video. Below is the synchronized audio transcript.
Use these timestamps to ground your visual analysis:
Task:
Identify if the visual 'blue spark' at 00:16 matches the audio description,
or if it is a lens flare."

+ Video content
```

## Solving “Visual Dominance” with Audio-First Context

Some studies suggest that current MLLMs often suffer from [**Visual Dominance bias**](https://www.researchgate.net/publication/397596158_When_Eyes_and_Ears_Disagree_Can_MLLMs_Discern_Audio-Visual_Confusion). In simple terms: if the model sees a piano on screen but hears a bird chirping, it is statistically likely to “hallucinate” that the piano is playing. However, I sometimes see the opposite picture — especially with low-resolution video — where the model may prioritize auditory information as the visual signal becomes less distinct.

Because of this variability, **I strongly recommend implementing an audio-first transcription layer**. By providing the audio transcript as a “pre-context layer,” you give the visual model a script to follow. This is a technique I’ve found essential; it prevents the model from “force-aligning” sounds with visual artifacts that happen to be present at the same timestamp, effectively keeping the narrative in sync and significantly boosting overall reliability.

## **Precision Timing: The FPS & Reasoning Balance**

True video understanding requires “temporal sensitivity” — knowing not just what happened, but exactly when and why.

- **The Sampling Sweet Spot:** For standard indexing and triage, **1 FPS** (frame per second) is [typically sufficient](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#videometadata). However, for long videos that are mostly static (e.g., lectures), you can set a **lower FPS (<1)** to significantly reduce token count and processing time without losing the core message.
- **High-Resolution Sampling:** For tasks requiring fine-grained OCR, reading numeric strings, or action recognition, you should increase the sampling rate for those specific segments to capture higher visual fidelity.
- **Thinking Budgets:** For complex spatiotemporal reasoning, the [**thinking**](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking) is our best friend. This allows the model to reason through its “thoughts” before providing a final response. Ensure you adjust your thinking\_budget (thinking\_level for latest Gemini models) and [max\_output\_tokens](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters) to allow the model to build an extensive internal reasoning chain before it commits to an answer. This is critical for preventing responses from cutting off during intensive analysis.

## The Context Trap: Understanding vs. Hallucination

In video analysis, context is a double-edged sword. While providing the model with background information or specific goals is essential for accuracy, it can also become a primary source of hallucinations (Object Presence Bias, etc.).

## Get Sveta Morag’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

MLLMs are highly suggestible. If the prompt explicitly states that the model “should see” a specific event or object, it will often “see” it — even if it’s not actually in the video. This “Confirmation Bias” in prompts can lead the model to ignore the visual evidence in favor of satisfying the instructions.

To avoid this, keep the initial prompts objective and use the multi-stage approach to verify findings rather than assuming they exist from the start.

## Handling the Context Barrier: Extreme Video Lengths

“How do I handle videos longer than the context window?” is a question I get often. When a video exceeds the million-token mark, the multi-stage triage **must happen on chunks** rather than the whole file.

Here are the two techniques I use to break through the context barrier:

- **Temporal Chunking & Anchor Mapping:** Programmatically split the video into manageable chunks (e.g., 20–30 minutes). I run the initial triage on each chunk independently. To maintain accuracy across boundaries, I apply the **Temporal Anchor Pattern** to each chunk’s prompt, ensuring the model’s “lookup table” stays synced with the specific chunk’s timestamps.
- **The Partial-Visual/Full-Audio Pivot:** Depending on the use case, you can often provide the **full audio transcript** paired with only a **partial visual context**. By using the Temporal Anchor pattern for the segments where visual data _is_ provided, the model can bridge the gaps using the transcript, maintaining the narrative arc without overflowing the context window.

Please check [this paper](https://arxiv.org/abs/2504.02259) for more insights.

## **Cost Optimization**

Scaling to millions of videos daily necessitates aggressive financial management. Here are four ways to optimize the “token burn” without sacrificing accuracy:

### 1\. Leverage Media Resolution (LOW)

The most significant lever in our cost-control arsenal is the [media resolution parameter.](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#adjust-media-resolution) You can lower video token usage from roughly 258 to only 66 per second for Gemini 2 and 2.5 models by adjusting the media resolution to “ **low”**. Note that for Gemini 3, a “ **medium”** resolution setting of 70 tokens per frame has become the standard. Before a full rollout, I recommend a POC across diverse sample files to confirm that quality remains acceptable for your needs.

### 2\. Implement Explicit Caching

If my workflow involves querying the same video multiple times — perhaps for different metadata extractions — **Context Caching** is non-negotiable. By caching the global context of the video, we avoid paying to re-index the file for every subsequent request.

### 3\. Picking the Right Model for the Job

Not every task requires a powerhouse model. I find it most effective to use a tiered approach:

- Use **Gemini 3 Flash or Gemini 3.1 Flash Lite** for 90% of the heavy lifting. They are incredibly fast and efficient for routine summaries, indexing, and basic validation.
- Save **Gemini 3.1 Pro** for the tricky parts. It’s the perfect partner for complex edge cases or deep reasoning where you really need that extra layer of insight.

### 4\. The Power of Batch Jobs

For high-throughput pipelines that don’t require millisecond latency, [**Batch API**](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-gemini) jobs are the ultimate goal. Moving from Online to Batch processing typically offers significant discounts on token pricing.

The trajectory of video understanding is moving toward models that can truly “understand” intent and subtle nuances. By combining a multi-stage agentic workflow with smart cost-saving parameters, we can turn a mountain of video data into a library of actionable insights today.

[Video Analytics](https://medium.com/tag/video-analytics?source=post_page---footer_tags--82dd0cd130ea-----------------------------------------)

[Gemini](https://medium.com/tag/gemini?source=post_page---footer_tags--82dd0cd130ea-----------------------------------------)

[Google Cloud Platform](https://medium.com/tag/google-cloud-platform?source=post_page---footer_tags--82dd0cd130ea-----------------------------------------)

[Google](https://medium.com/tag/google?source=post_page---footer_tags--82dd0cd130ea-----------------------------------------)

[Data](https://medium.com/tag/data?source=post_page---footer_tags--82dd0cd130ea-----------------------------------------)

[![Sveta Morag](https://miro.medium.com/v2/resize:fill:48:48/1*w7chfWPHnoYRYcZCZeUsrw.png)](https://medium.com/@svetamorag?source=post_page---post_author_info--82dd0cd130ea-----------------------------------------)

[![Sveta Morag](https://miro.medium.com/v2/resize:fill:64:64/1*w7chfWPHnoYRYcZCZeUsrw.png)](https://medium.com/@svetamorag?source=post_page---post_author_info--82dd0cd130ea-----------------------------------------)

Follow

[**Written by Sveta Morag**](https://medium.com/@svetamorag?source=post_page---post_author_info--82dd0cd130ea-----------------------------------------)

[29 followers](https://medium.com/@svetamorag/followers?source=post_page---post_author_info--82dd0cd130ea-----------------------------------------)

· [3 following](https://medium.com/@svetamorag/following?source=post_page---post_author_info--82dd0cd130ea-----------------------------------------)

AI Solution Architect at Google Cloud

Follow

[![Google Cloud - Community](https://miro.medium.com/v2/resize:fill:48:48/1*FUjLiCANvATKeaJEeg20Rw.png)](https://medium.com/google-cloud?source=post_page---post_publication_info--82dd0cd130ea-----------------------------------------)

[![Google Cloud - Community](https://miro.medium.com/v2/resize:fill:64:64/1*FUjLiCANvATKeaJEeg20Rw.png)](https://medium.com/google-cloud?source=post_page---post_publication_info--82dd0cd130ea-----------------------------------------)

Follow

[**Published in Google Cloud - Community**](https://medium.com/google-cloud?source=post_page---post_publication_info--82dd0cd130ea-----------------------------------------)

[78K followers](https://medium.com/google-cloud/followers?source=post_page---post_publication_info--82dd0cd130ea-----------------------------------------)

· [Last published 20 hours ago](https://medium.com/google-cloud/flink-sql-and-apache-iceberg-on-google-cloud-streaming-and-batch-into-one-open-lakehouse-5521296f627c?source=post_page---post_publication_info--82dd0cd130ea-----------------------------------------)

A collection of technical articles and blogs published or curated by Google Cloud Developer Advocates. The views expressed are those of the authors and don't necessarily reflect those of Google.

Follow

[Help](https://help.medium.com/hc/en-us?source=post_page-----82dd0cd130ea-----------------------------------------)

[Status](https://status.medium.com/?source=post_page-----82dd0cd130ea-----------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----82dd0cd130ea-----------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----82dd0cd130ea-----------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----82dd0cd130ea-----------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----82dd0cd130ea-----------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----82dd0cd130ea-----------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----82dd0cd130ea-----------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----82dd0cd130ea-----------------------------------------)