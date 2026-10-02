[Home](https://pecollective.com/) › [Tools](https://pecollective.com/tools/) › Gemini Free Tier Guide

# Gemini API Free Tier (September 2026): Every Rate Limit, Quota, and Gotcha

Google gives away more free LLM compute than any other major provider. No credit card. No expiration. Access to their best models. This page is the Gemini-specific deep dive. For how Gemini's free tier stacks up against ChatGPT, Claude, Copilot, and Pinecone, see [AI Free Tiers Compared](https://pecollective.com/blog/ai-free-tiers-compared/).

## Two Ways to Access Gemini for Free

Google offers Gemini through two platforms, each with different free tier mechanics. Understanding the distinction is important because they serve different use cases, and mixing them up leads to unexpected bills or unnecessary limitations.

### Google AI Studio (aistudio.google.com)

This is the primary free tier path. You get an API key with zero configuration. No Google Cloud project. No billing account. It works immediately after signing in with a Google account.

AI Studio gives you access to the current free lineup: Gemini 3 Flash, Gemini 3.1 Flash-Lite, and the older 2.5 and 2.0 Flash models. The Pro models moved behind billing in May 2026, so the free tier is a Flash-only tier now. Each model has different rate limits, and we cover those in detail below. The key advantage here is simplicity. You get a key, you make API calls, and you pay nothing until you choose to upgrade.

The tradeoff: Google may use your free-tier inputs and outputs to improve their models. If you are building something with sensitive data, this matters.

### Vertex AI ($300 Credit for New Accounts)

Vertex AI is Google Cloud's full ML platform. New GCP accounts get $300 in free credits valid for 90 days. That covers Gemini API calls, but also any other Google Cloud service you use during that window.

After the credits expire, you pay standard rates. There is no ongoing free tier for Vertex AI. The advantage over AI Studio is higher rate limits, no data-sharing clause, enterprise features (grounding, custom fine-tuning, data residency), and SLAs. For most developers starting out, AI Studio is the right choice. Vertex AI makes sense when you need production guarantees or are already in the Google Cloud ecosystem.

## Free Tier Rate Limits by Model

These are the limits that actually matter day-to-day. Every model has three constraints: requests per minute (RPM), tokens per minute (TPM), and requests per day (RPD). You will hit the RPM limit long before TPM in most use cases.

| Model | RPM | TPM | RPD | Context |
| --- | --- | --- | --- | --- |
| **Gemini 3 Flash** | 10 | 250,000 | 1,500 | 1M tokens |
| **Gemini 3.1 Flash-Lite** | 15 | 250,000 | 1,000 | 1M tokens |
| **Gemini 2.5 Flash** | 10 | 250,000 | 1,500 | 1M tokens |
| **Gemini 2.5 Pro** | 5 | 150,000 | 50 | 1M tokens |
| **Gemini 2.0 Flash** | 15 | 1,000,000 | 1,500 | 1M tokens |
| **Gemini 1.5 Pro** | 2 | 32,000 | 50 | 2M tokens |
| **Gemini 1.5 Flash** | 15 | 1,000,000 | 1,500 | 1M tokens |
| **Gemma 2 (27B)** | 15 | 1,000,000 | 1,500 | 8K tokens |

A few things stand out. Gemini 2.5 Pro is capped at 50 requests per day on the free tier. That is enough to test and prototype but not enough for any real workload. Gemini 2.0 Flash and the newer Gemini 3.1 Flash-Lite are the most generous on requests per minute. As of May 2026, Google's free tier covers only Flash and Flash-Lite models. The Pro models moved behind billing. So if your project runs on the free tier, you are running on Flash.

## Gemini 3 Flash Free Tier Limits

Gemini 3 Flash arrived in early 2026 as Google's recommended free-tier model, and it replaced 2.5 Flash as the default for most new projects. On the free tier it runs 10 requests per minute, 250,000 tokens per minute, and 1,500 requests per day. The 1M-token context window carries over from the 2.5 generation, so you can still feed it long documents without paying.

Two numbers matter here. The 10 RPM ceiling is the one most people hit first. The 1,500 RPD cap is the one that ends a busy day early. At a steady 1 request per minute you run for 25 hours of clock time before the daily cap resets, which means a low-traffic app fits comfortably. A burst-heavy app does not.

Gemini 3.1 Flash-Lite sits below 3 Flash on quality but gives you 15 RPM. If your task is classification, extraction, or routing rather than long-form reasoning, Flash-Lite buys you 50% more throughput on the same free tier. People building automation agents often run Flash-Lite for the cheap, high-volume steps and call 3 Flash only when a step needs the stronger model.

One caveat worth repeating: the limits Google publishes are starting points. AI Studio shows the live cap for your specific project, and it varies by region, account age, and whether billing is attached. Spinning up extra API keys under the same project does not add quota. The limit is per project, not per key.

## Running PicoClaw and Other Automation Agents on the Free Tier

The query that brings most people to this page in 2026 is some version of "can I run my agent on Gemini for free, all day, without a bill." The short answer: yes, within the daily cap, and Gemini's free tier is the most agent-friendly of the major providers.

PicoClaw is the tool that made this popular. It is a tiny CLI agent (under 10MB of RAM, sub-second startup) that runs file operations, code execution, scheduling, and web search, and you point it at any LLM by dropping a key into `~/.picoclaw/config.json`. People deploy it on a Raspberry Pi or a cheap VPS and let it run 24/7 against the Gemini free tier. The same pattern works for OpenClaw, Aider in unattended mode, and homegrown cron-driven scripts.

What you can actually do for free with an always-on agent:

- **Scheduled jobs.** A cron task that runs every 10 minutes makes 144 calls a day. That leaves you over 1,300 calls of headroom under the 1,500 RPD cap on Gemini 3 Flash. Summarizing an inbox, watching a folder, or checking a feed all fit easily.
- **A personal coding agent.** Interactive coding sessions burn requests in bursts. You will hit the 10 RPM wall during heavy editing, not the daily cap. Exponential backoff turns that wall into a 1-2 second pause instead of a failed run.
- **A Telegram or Discord bot.** PicoClaw's gateway mode connects to chat platforms. For a bot serving you and a few friends, free-tier limits are invisible. For a public bot, you will blow past 1,500 RPD fast.
- **Multi-step pipelines.** Here is the trap. A single "task" in an agent can fan out into 8 or 10 model calls (plan, search, read, reason, act, verify). Ten tasks an hour at 8 calls each is 80 RPM of demand against a 10 RPM ceiling. You need queuing.

The honest limit for automation: the daily cap is your real budget, not the per-minute one. Picture an agent that averages 4 model calls per task. The 1,500 RPD ceiling on Gemini 3 Flash gives you about 375 agent tasks a day before the free tier cuts you off. That is plenty for a personal assistant, a monitoring job, or a side project. It is not enough for an agent serving real users.

Three tactics keep a free-tier agent alive longer. Route cheap steps (classification, routing, short extraction) to Gemini 3.1 Flash-Lite to spread load across two separate quotas. Cache anything deterministic so repeat questions never hit the API. And queue agent steps so a burst of fan-out calls drains under 10 RPM instead of slamming the limit and triggering 429s. For where the free tier stops making sense, see our breakdown of [LLM pricing per million tokens](https://pecollective.com/tools/llm-pricing-per-million-tokens/) and how Gemini compares to [Claude API pricing](https://pecollective.com/tools/anthropic-api-pricing/) once you go paid.

## What the Free Tier Includes Beyond Text

Gemini is multimodal, and the free tier includes all modalities. This is a significant differentiator from OpenAI and Anthropic, where vision capabilities are often limited or cost extra.

- **Image understanding:** Send images alongside text prompts. Useful for OCR, chart reading, visual Q&A, and image classification. No separate image API needed.
- **Video understanding:** Upload video clips up to 2 hours in length (with Gemini 1.5 Pro or newer). The model can answer questions about video content, extract information from frames, and summarize visual sequences.
- **Audio processing:** Send audio files for transcription, translation, and content understanding. Supports common formats including MP3, WAV, and FLAC.
- **Document analysis:** Upload PDFs directly. The model processes text and images within the document without needing a separate parsing step.
- **Code execution:** Gemini 2.0 Flash and 2.5 models can execute Python code in a sandboxed environment and return results. This runs inside Google's infrastructure at no additional cost on the free tier.

The rate limits above apply across all modalities. A multimodal request (text + image) counts as one request toward your RPM and RPD limits. Token counts for images and video are calculated based on resolution and duration, which can consume your TPM faster than text-only requests.

## Gemini App vs. Gemini API: Different Products

This is where people get confused. The Gemini app (gemini.google.com) and the Gemini API are separate products with separate free tiers.

**Gemini app (free):** Unlimited text conversations with Gemini. Includes image generation (via Imagen 3). No API access. Think of this as Google's equivalent to free ChatGPT. It uses Gemini 2.0 Flash by default.

**Gemini Advanced ($19.99/month via Google One AI Premium):** Access to Gemini 2.5 Pro in the app. 2TB Google storage. Gemini in Gmail, Docs, Sheets, and other Workspace apps. NotebookLM Plus. Still no API access included.

**Gemini API (Google AI Studio free tier):** What this guide covers. Programmatic access to all Gemini models. Completely separate from the Gemini app subscription. You can use both the free app and the free API simultaneously.

A common mistake: people pay for Gemini Advanced thinking it gives them API access. It does not. The API free tier through Google AI Studio is separate and does not require any subscription.

### When the Free Tier Breaks Down

The 10 RPM limit on Gemini 3 Flash means you can process roughly 600 requests per hour. For a chatbot serving a handful of users, that is fine. For batch processing (analyzing a thousand documents, for example), you will need the paid tier or creative rate-limit management. At 1,500 requests per day, you run out by early afternoon if your app has steady traffic. The inflection point for most developers: once you are building something other people use, you will need to upgrade.

## Free Tier vs. Pay-as-You-Go Pricing

When you do outgrow the free tier, here is what you will pay. These rates apply through Google AI Studio with a billing account enabled.

| Model | Input / 1M Tokens | Output / 1M Tokens | Paid RPM |
| --- | --- | --- | --- |
| **Gemini 2.5 Flash** | $0.15 | $0.60 | 2,000 |
| **Gemini 2.5 Pro** | $1.25 | $10.00 | 1,000 |
| **Gemini 2.0 Flash** | $0.075 | $0.30 | 2,000 |
| **Gemini 1.5 Pro** | $1.25 | $5.00 | 1,000 |

Gemini 2.0 Flash at $0.075 per million input tokens is the cheapest major LLM API on the market. For comparison, GPT-4o mini costs $0.15/$0.60 (twice the input price) and Claude Haiku 4.5 costs $1/$5 (over 13x the input price). If cost is your primary concern and you need a capable model, Gemini 2.0 Flash is difficult to beat even after you leave the free tier.

The jump from free to paid also increases your RPM by 100-200x. That alone justifies upgrading for any production workload.

## Practical Tips for Maximizing the Free Tier

If you want to stay on the free tier as long as possible, here are strategies that work.

1. **Use Gemini 3 Flash for most tasks, Flash-Lite for the cheap ones.** 3 Flash is the recommended free model (10 RPM, 250K TPM, 1,500 RPD). Flash-Lite runs at 15 RPM with its own daily bucket, so routing classification and extraction there stretches your quota.
2. **Cache results aggressively.** If your app asks the same types of questions repeatedly, cache the API responses locally. A simple key-value cache (Redis, SQLite, even a dictionary) can eliminate 30-60% of redundant calls.
3. **Batch your requests within rate windows.** Instead of making calls as they come in, queue requests and send them in controlled bursts that stay under 15 RPM.
4. **Use the Gemini app for manual testing.** The web app has no rate limits for conversational use. Use it for prompt development and iteration, then switch to the API for production calls.
5. **Implement exponential backoff.** When you hit rate limits, the API returns 429 errors. A simple retry with exponential backoff (1s, 2s, 4s, 8s) handles transient limit hits gracefully without losing requests.

## How Gemini Free Tier Compares to Other Providers

Here is an honest comparison of what you get for free across the major AI API providers as of September 2026.

| Provider | Free Access | Expiration | Best Free Model |
| --- | --- | --- | --- |
| **Google (Gemini)** | Ongoing free tier, no card needed | Never | Gemini 2.0 Flash |
| **OpenAI** | Free daily tokens if you share API traffic for training | Ongoing (30-day notice) | GPT-5 family |
| **Anthropic** | Small console trial credit, no standing free tier | Limited | Claude Haiku 4.5 |
| **Mistral** | Free tier, API key only | Never | Mistral Small |
| **Groq** | Free tier with rate limits | Never | Llama 3.3 70B |
| **Cohere** | Trial key, 1,000 calls/month | Never | Command R+ |

Google's position is clear: they want developers building on Gemini, and they are willing to subsidize the onboarding. The combination of no expiration, no credit card, multimodal support, and access to competitive models makes the Gemini free tier the strongest starting point for developers in 2026.

For a detailed breakdown of all providers, see our [complete AI API free tier comparison](https://pecollective.com/tools/ai-api-free-tiers/).

## Common Mistakes to Avoid

After tracking developer experience with Gemini's free tier, these are the mistakes we see most often.

- **Confusing AI Studio with Vertex AI.** They have different URLs, different authentication, different rate limits, and different billing. Pick one and stick with it.
- **Not handling 429 errors.** The free tier will rate-limit you. If your code does not have retry logic, requests will silently fail during traffic spikes.
- **Sending unnecessarily large prompts.** Long system prompts eat into your TPM budget. Keep prompts concise. Use few-shot examples only when they measurably improve output quality.
- **Ignoring the data-sharing clause.** If you send customer data, PII, or proprietary information through the free tier, Google can use it for training. For production apps with real user data, upgrade to paid or use Vertex AI.
- **Using 2.5 Pro when 2.0 Flash would work.** The Pro model has a 50 RPD limit on free tier. Most tasks that developers throw at Pro can be handled by Flash with a better prompt. Test with Flash first.

## Related Resources

[**AI API Free Tiers Compared** Complete free tier breakdown for OpenAI, Anthropic, Google, Mistral, Cohere, and more.](https://pecollective.com/tools/ai-api-free-tiers/) [**LLM Pricing Per Million Tokens** Side-by-side token costs for every major model when you outgrow free tiers.](https://pecollective.com/tools/llm-pricing-per-million-tokens/) [**OpenAI API Pricing Guide** GPT-4.1, GPT-5, and the full OpenAI model lineup with current costs.](https://pecollective.com/tools/openai-api-pricing/) [**Claude API Pricing Guide** Anthropic's model pricing including batch and caching discounts.](https://pecollective.com/tools/anthropic-api-pricing/) [**ChatGPT Free Tier Guide** What you get with free ChatGPT vs. Plus vs. Pro, including API differences.](https://pecollective.com/tools/chatgpt-free-tier-guide/) [**AI Free Tiers in 2026** Analysis of which free tiers are actually worth building on this year.](https://pecollective.com/blog/ai-free-tiers-2026/)

## Frequently Asked Questions

### Is the Gemini API free to use in 2026?

Yes. Google AI Studio offers a free tier for Gemini models with no credit card required. You get access to Gemini 3 Flash, Gemini 3.1 Flash-Lite, and the older Flash models, with rate limits of 10-15 requests per minute depending on the model. The free tier is generous enough for prototyping, personal projects, and low-volume production apps.

### What are the rate limits on Gemini's free tier?

Gemini 3 Flash gets 10 RPM, 250,000 tokens per minute, and 1,500 requests per day. Gemini 3.1 Flash-Lite gets 15 RPM with a 1,000 RPD cap. The older 2.5 Flash matches 3 Flash at 10 RPM and 1,500 RPD. Pro models are no longer on the free tier.

### What is the difference between Google AI Studio and Vertex AI?

Google AI Studio is the free, developer-friendly way to access Gemini with an API key. No GCP project needed. Vertex AI is Google Cloud's enterprise ML platform, which requires a GCP project and billing account. Vertex AI offers $300 in free credits for new accounts, higher rate limits, SLAs, and features like grounding with Google Search. For individual developers, AI Studio's free tier is the better starting point.

### Does the Gemini free tier include image and video understanding?

Yes. All Gemini models on the free tier support multimodal inputs including images, audio, video, and documents. Multimodal requests count toward the same rate limits as text requests. Token counts for images and video are calculated based on resolution and duration.

### When should I upgrade from Gemini's free tier?

Upgrade when you consistently hit rate limits (more than 10-15 RPM), need guaranteed uptime for production apps, want higher throughput for batch processing, or need enterprise features like data residency. Pay-as-you-go starts at $0.075 per 1M input tokens for Gemini 2.0 Flash.

### How does Gemini's free tier compare to OpenAI and Anthropic?

Google is the most generous for no-strings access. OpenAI discontinued signup credits; its free option now grants daily tokens only if you opt in to share your API traffic for training. Anthropic has no standing free API tier. Google AI Studio has no expiration and no credit card requirement, making it the only major provider with an indefinite free API tier that costs you nothing but rate limits.

### Can I use the Gemini free tier for commercial applications?

Yes, with a caveat. Google AI Studio's free tier allows commercial use, but Google may use free-tier inputs and outputs to improve its models. If data privacy matters for your application, upgrade to paid or use Vertex AI, which does not use your data for model training.

### Does Google Gemini 2.5 Pro have a free tier in 2026?

Not anymore. Pro models moved behind billing in May 2026, so 2.5 Pro now requires a paid account. Earlier in the year the free tier allowed 5 requests per minute and 50 per day, which is the number many older guides still quote. The paid rate runs $1.25 per million input tokens and $10 per million output tokens. If you are on the free tier, your reasoning model is Gemini 3 Flash.

### What changed with Gemini free tier limits in early 2026?

Google raised rate limits for Gemini 2.0 Flash in early 2026, going from 15 RPM to rates that better support production workloads. The 1M token context window became standard across Flash models. Gemini 3 Flash launched as the new recommended model for most tasks, with better reasoning than 2.5 Flash at similar cost. The Pro models moved behind billing, so the free tier now covers Flash and Flash-Lite only.

### What are the Gemini 3 Flash free tier limits?

Gemini 3 Flash on the free tier runs 10 requests per minute, 250,000 tokens per minute, and 1,500 requests per day, with the 1M-token context window. Gemini 3.1 Flash-Lite gives you 15 RPM if you need more throughput on lighter tasks. The exact cap shown in AI Studio varies by region and account, and adding extra API keys to one project does not raise it.

### Can I run PicoClaw or another automation agent on the Gemini free tier?

Yes. PicoClaw is a lightweight CLI agent people run 24/7 against Gemini's free tier on a Raspberry Pi or cheap VPS. Drop a Google AI Studio key into the config and you are running for free. The real budget is the 1,500 requests-per-day cap, not the per-minute one. If your agent averages 4 model calls per task, that is roughly 375 tasks a day before the free tier stops you. Route light steps to Flash-Lite, cache deterministic calls, and queue requests under 10 RPM to stretch it further.

### How many requests per day does a free Gemini agent get?

Gemini 3 Flash allows 1,500 requests per day on the free tier. A cron job firing every 10 minutes uses 144 of those. An interactive coding agent burns them in bursts and tends to hit the 10 RPM wall before the daily cap. Running cheap steps on Gemini 3.1 Flash-Lite gives you a second 1,000 RPD bucket, so splitting work across both models roughly doubles your free daily ceiling.

## Gemini Free Tier vs. Building with Context Caching

One feature worth knowing on the paid tier: context caching. If your application sends the same system prompt or large document with every request, caching lets you pay for that context once and reuse it across requests. Cached tokens cost 75% less than regular input tokens on Gemini 2.5 Flash.

On the free tier, context caching is not available. Every request sends the full context. For prototyping, that's fine. Once you're running real workloads where the same instructions repeat across hundreds of calls, caching pays for the upgrade quickly. A 10K-token system prompt repeated 1,000 times costs $0.38 uncached versus $0.09 cached on Gemini 2.0 Flash. At scale, the math tilts hard toward paid.

The other paid-tier feature worth knowing: batch requests. Gemini supports asynchronous batch processing for non-time-sensitive workloads at a 50% discount on token costs. If you're processing thousands of documents overnight, the combination of batch pricing and context caching makes Gemini the cheapest capable LLM API by a significant margin. This does not exist on the free tier. Free tier requests are synchronous only.

For reference: our [LLM pricing comparison](https://pecollective.com/tools/llm-pricing-per-million-tokens/) tracks current costs across all major providers. And for developers choosing between the free tier and the API: the decision usually comes down to whether you hit the RPM limits before you hit your budget limits.

## Getting Started: Practical First Steps

If you haven't used the Gemini free tier yet, here's the fastest path to your first API call.

1. **Go to aistudio.google.com.** Sign in with any Google account. No special access needed.
2. **Click "Get API Key."** You can create a key attached to an existing Google Cloud project or create a new one. For free tier use, the project setup is automatic.
3. **Make your first call.** The API follows the same general pattern as OpenAI's SDK. The quickest way to start is with the Python SDK: `pip install google-generativeai`. The Google AI Studio interface also has a code export button that generates the equivalent API call for whatever you test in the UI.
4. **Pick the right model.** Start with Gemini 3 Flash. It is the model Google recommends for the free tier, it carries the 1M-token context window, and its 1,500 RPD cap is the most generous of the current lineup. Drop to Gemini 3.1 Flash-Lite when you need more requests per minute on lighter tasks.
5. **Add exponential backoff immediately.** Even in development, you'll hit rate limits when you're testing quickly. Build retry logic before you need it, not after a confusing string of 429 errors.

Related: [ChatGPT free tier guide](https://pecollective.com/tools/chatgpt-free-tier-guide/) and [which AI free tiers are worth building on in 2026](https://pecollective.com/blog/ai-free-tiers-2026/).

## AI API pricing changes weekly. We track all of it.

Weekly data from 22,000+ job postings. Free.

Get the Data

2,700+ subscribers. Unsubscribe anytime.