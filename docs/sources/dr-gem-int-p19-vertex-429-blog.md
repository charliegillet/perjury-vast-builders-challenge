AI & Machine Learning

# Build Resilient LLM Applications on Vertex AI and Reduce 429 Errors

March 12, 2026

##### Richard Liu

Senior Product Manager, Google Cloud

##### Pedro Melendez

Cloud AI Technical Evangelist

##### Try Gemini Enterprise today

The front door to AI in the workplace

[Try now](https://business.gemini.google/?utm_source=cloud.google.com/blog&utm_medium=et&utm_campaign=FY26-Q2-GLOBAL-GLO27877-physicalevent-er-next26-mc-105752)

Building applications powered by Large Language Models (LLMs) on Vertex AI is exciting, but hitting a [429 error](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/error-code-429) can be a frustrating roadblock. These errors signal that your requests are coming in faster than the service can handle them at that moment.

Last year, we [published a guide](https://cloud.google.com/blog/products/ai-machine-learning/learn-how-to-handle-429-resource-exhaustion-errors-in-your-llms?e=48754805) to handling these 429 errors. In this article, we’ll dig deeper into Vertex AI’s consumption models and dives into architectural best practices for managing request flows. This way, you can build smooth, resilient, and truly scalable AI applications.

### Choosing the right consumption option

Vertex AI provides a range of consumption models designed to accommodate various API traffic types and volumes. Your primary strategy for minimizing 429 errors is selecting the consumption model that best aligns with your application’s unique traffic patterns.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Build_Resilient_LLM_Applications_on_Vertex.max-2200x2200.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Build_Resilient_LLM_Applications_on_Vertex.max-2200x2200.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Build_Resilient_LLM_Applications_on_Vertex.max-2200x2200.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Build_Resilient_LLM_Applications_on_Vertex.max-2200x2200.jpg)

**Default options:** The default option with Gemini on Vertex AI is Standard Pay-as-you-go (Paygo). For [Standard Pay-as-you-go](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/standard-paygo) (Paygo) traffic, Vertex AI uses a system with Usage Tiers. This dynamic approach allocates resources from a shared pool, where your organization’s historical spend determines your Usage Tier and baseline throughput (TPM). This baseline provides a predictable performance floor for typical workloads, while still allowing your application to burst beyond it on a best-effort basis.

If your application generates critical, user-facing traffic that can be unpredictable and require higher reliability than Standard Paygo, [Priority Paygo](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/priority-paygo) is designed for you. By adding the priority header to your requests, you signal that this traffic should be prioritized, reducing the likelihood of being throttled.

For applications with consistently high volumes of real-time traffic, [Provisioned Throughput](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/overview) (PT) is the only consumption option that provides isolation from the shared PayGo pool, offering a stable experience even during heavy contention on PayGo. With PT, you reserve and pay for a guaranteed throughput, ensuring your important traffic flows smoothly. [To learn more about PT on Vertex AI, visit our guide here.](https://cloud.google.com/blog/products/ai-machine-learning/provisioned-throughput-on-vertex-ai?e=48754805)

**Cost-effective options:** For traffic that isn't latency sensitive, Vertex AI offers more cost-effective options. The [Flex PayGo](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/flex-paygo) is suited for latency-tolerant traffic, processing requests at a lower price. Large-scale, asynchronous jobs, such as offline analysis or bulk data enrichment, are best handled by [Batch](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-gemini). This service manages the entire workflow, including scaling and retries, over a longer period (around 24 hours), insulating your main application from this heavy load.

**Complex applications and hybrid approaches:** Complex applications often leverage a hybrid approach: PT for essential real-time traffic, Priority Paygo for fluctuating traffic, Standard Paygo for general requests, and Batch/Flex for latency-tolerant and offline request flows.

### Five ways to reduce 429 errors on Vertex AI

**1\. Implement smart retries**

When your application encounters a temporary overload error like a 429 (Resource Exhausted) or 503 (Service Unavailable), an immediate retry is not recommended. The best practice is to implement a retry strategy called Exponential Backoff with Jitter. Exponential backoff means that the delay between retry attempts increases exponentially usually up to a predefined maximum delay. This gives the service time to recover from the overload condition.

- **SDK & libraries:** The [Google Gen AI SDK](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/retry-strategy#configuring-retries)  includes native retry behavior that can be configured via HttpRetryOptions in client parameters. However, you can also leverage specialized libraries like [Tenacity](https://github.com/jd/tenacity) (for Python) or build a custom solution. For a deeper dive, refer to this [blog post](https://cloud.google.com/blog/products/ai-machine-learning/learn-how-to-handle-429-resource-exhaustion-errors-in-your-llms).

- **Agentic workflows:** For developing agents, the [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) offers a [Reflect and Retry plugin](https://google.github.io/adk-docs/integrations/reflect-and-retry/) that builds resilience into AI workflows by automatically intercepting 429 errors.

- **Infrastructure & Gateway:** Another robust option for building resilience is [circuit breaking with Apigee](https://github.com/GoogleCloudPlatform/apigee-samples/tree/main/llm-circuit-breaking), which enables you to manage traffic distribution and implement graceful failure handling.


**2\. Leverage global model routing**

Vertex AI's infrastructure is distributed across multiple regions. By default, if you target a specific regional endpoint, your request is served from that region. This means your application's availability is tied to the capacity of that single region. This is where the global endpoint becomes an effective tool for enhancing availability and resilience. Instead of being locked into one region, the global endpoint routes your traffic across a fleet of regions where there may be more availability, reducing the potential error rate.

**3\. Reduce payload via context caching**

An effective way to reduce the load on Vertex AI is to avoid making calls for repetitive queries. Many production applications, especially chatbots and support systems, see similar questions asked frequently. Instead of re-processing these, you can implement [context caching](https://cloud.google.com/blog/products/ai-machine-learning/vertex-ai-context-caching?e=48754805). With Context Caching, Gemini reuses precomputed cached tokens, allowing you to reduce your API traffic and throughput. This not only saves costs but also reduces latency for repeated content within your prompts.

**4\. Optimize prompts**

Reducing the token count in each request directly lowers your TPM consumption and costs.

- **Summarization with Flash-Lite:** Before sending a long conversation history to a model like Gemini Pro, use a lightweight model like [Gemini 2.5 Flash-Lite](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-lite) to summarize the context.
- **Agent memory optimization:** ForAgentic workloads you can leverage Vertex AI [Agent Engine Memory Bank](https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/overview). Features like Memory Extraction and Consolidation allow you to distill meaningful facts from a conversation, ensuring your agent remains context-aware without raw chat history.
- **Prompt hygiene:** Review your prompts and reduce overly verbose JSON schema descriptions (if the model is already familiar) and stripping excessive whitespace or redundant formatting.

**5\. Shape traffic**

Sudden bursts of requests are a primary cause of 429 errors. Even if your average traffic rate is low, sharp spikes can strain resources. The goal is to smoothen traffic, spreading requests out over time.

### Get started

Ready to put these patterns into practice? Explore the [Vertex AI samples on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/), or jumpstart your next project with the [Google Cloud Beginner’s Guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview), [Vertex AI quickstart](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start) or start building your next AI agent with the  [Agent Development Kit (ADK)](https://google.github.io/adk-docs/)

Posted in

- [AI & Machine Learning](https://cloud.google.com/blog/products/ai-machine-learning)
- [Developers & Practitioners](https://cloud.google.com/blog/topics/developers-practitioners)

##### Related articles

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/Whats_new_in_AI_infrastructure.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Whats_new_in_AI_infrastructure.max-700x700.jpg)\\
\\
AI infrastructure\\
\\
**What’s new in AI infrastructure and orchestration in September** \\
\\
By Alex Barrett • 19-minute read](https://cloud.google.com/blog/topics/ai-infrastructure/whats-new-in-ai-infrastructure-this-month)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/01_-_AI__Machine_Learning_H1ZyZG8.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/01_-_AI__Machine_Learning_H1ZyZG8.max-700x700.jpg)\\
\\
AI & Machine Learning\\
\\
**Empower your agents with the Google Cloud CLI remote MCP server** \\
\\
By Prosper Nwankpa • 6-minute read](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-cli-remote-mcp-server-in-preview)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/open-models-for-startups-gemma-header.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/open-models-for-startups-gemma-header.max-700x700.png)\\
\\
Startups\\
\\
**Why your startup needs open models alongside frontier APIs** \\
\\
By Darren Mowry • 7-minute read](https://cloud.google.com/blog/topics/startups/why-your-startup-needs-open-models-alongside-frontier-apis)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/11_-_Developers__Practitioners_a4Y5EGr.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/11_-_Developers__Practitioners_a4Y5EGr.max-700x700.jpg)\\
\\
Developers & Practitioners\\
\\
**Best practices guide for customizing Gemini models via Reinforcement Learning (RL)** \\
\\
By Jiaqi Pan • 6-minute read](https://cloud.google.com/blog/topics/developers-practitioners/best-practices-guide-for-customizing-gemini-models)