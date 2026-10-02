Solutions

Jan 5, 2026

# When the City Thinks: Real-Time Video Agents with VAST and NVIDIA Cosmos Reason 2

![When the City Thinks: Real-Time Video Agents with VAST and NVIDIA Cosmos Reason 2](https://images.ctfassets.net/2f3meiv6rg5s/6Mzeenwilq7LyHv310J6QC/e1cd80860df73159e3b3767689103b60/more-inference-less-infrastructure-vast-nvidia.webp?w=1280&fm=png&q=80)

Authored by

Sagi Grimberg, VP Architecture, VAST Data, and Lior Cohen, Senior AI Solutions Architect, NVIDIA

Share This

[![Twitter](https://images.ctfassets.net/2f3meiv6rg5s/13UM456sGH9JXUxLl81X5O/7969616967f999451929bb5be0f435cc/icon-x.svg)](https://twitter.com/share?text=When%20the%20City%20Thinks:%20Real-Time%20AI%20with%20VAST%20and%20NVIDIA%20-%20VAST%20Data&url=https://www.vastdata.com/blog/vast-nvidia-cosmos-reason-smart-cities&hashtags=vastdata)

[![LinkedIn](https://images.ctfassets.net/2f3meiv6rg5s/4JynFMRw5umhHhRleKsV9W/f2269da24d5cba265f2b443aa45aacef/blog-linkedin.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https://www.vastdata.com/blog/vast-nvidia-cosmos-reason-smart-cities&title=When%20the%20City%20Thinks:%20Real-Time%20AI%20with%20VAST%20and%20NVIDIA%20-%20VAST%20Data&source=https://www.vastdata.com/blog/vast-nvidia-cosmos-reason-smart-cities)

[![Reddit](https://images.ctfassets.net/2f3meiv6rg5s/gFi1N7KiqWuKHzDMNYwhf/720a9e9cdbc4bba4bc3c554aff3bba18/blog-reddit.svg)](https://www.reddit.com/submit?url=https://www.vastdata.com/blog/vast-nvidia-cosmos-reason-smart-cities&title=When%20the%20City%20Thinks:%20Real-Time%20AI%20with%20VAST%20and%20NVIDIA%20-%20VAST%20Data)

[![Email](https://images.ctfassets.net/2f3meiv6rg5s/30LFr1HT6NynCevNDxKd06/9f76a25c5fb820cf82f56cb2f6fe44a2/blog-email.svg)](mailto:?subject=When%20the%20City%20Thinks:%20Real-Time%20AI%20with%20VAST%20and%20NVIDIA%20-%20VAST%20Data&body=When%20the%20City%20Thinks:%20Real-Time%20AI%20with%20VAST%20and%20NVIDIA%20-%20VAST%20Data%0D%0Ahttps://www.vastdata.com/blog/vast-nvidia-cosmos-reason-smart-cities)

![Copy Link](https://images.ctfassets.net/2f3meiv6rg5s/2KGF0XrDXSq3x2jDAgneCX/b2ccf23de3c4ccc5a9fb4cc073d7a46a/blog-link.svg)

In the era of “physical AI,” smart cities are no longer just about collecting petabytes of video footage—they are understanding and reacting upon it in real-time. The challenge has shifted from _storage_ to _cognition_. That’s why we are excited to detail the integration of [NVIDIA Cosmos Reason 2](https://build.nvidia.com/nvidia/cosmos-reason2-8b) Vision Language Model (VLM) directly into the [VAST AI OS](https://www.vastdata.com/platform/ai-os).

This architecture transforms a city’s video infrastructure from a passive recording system into an agentic “thinking machine,” capable of detecting anomalies, managing traffic, and ensuring public safety with human-like reasoning and autonomous capabilities.

#### **VAST and NVIDIA: A Real-time Video Intelligence Engine for Agents**

The core limitation of traditional video intelligence systems is not model quality, but **architecture**. Most deployments are designed around **batch analytics**, with only narrow, hard-coded real-time capabilities. Video is primarily treated as data to be stored and analyzed later, not as a live signal that can drive immediate action.

This design fundamentally limits response in scenarios where **seconds matter**—traffic incidents, safety hazards, or emerging public-security events. Even when “real-time” analytics exist, they are typically constrained to isolated detectors or fixed rules, unable to reason across streams, correlate context, or adapt dynamically to unfolding situations.

These limitations stem from architectural silos. Video is written to object storage, metadata is extracted into separate systems, and analytics pipelines are bolted on downstream. Each component operates independently, making low-latency, context-aware reasoning across the entire system impractical.

The **VAST AI OS**, built with the [NVIDIA Metropolis Blueprint for video search and summarization (VSS)](https://build.nvidia.com/nvidia/video-search-and-summarization), removes these constraints by collapsing storage, metadata, and reasoning into a single, unified video intelligence engine. Among the key components are:

- [VAST DataStore](https://www.vastdata.com/platform/datastore) **:** A multiprotocol, exabyte-scale storage layer optimized for continuous high-definition video ingest, delivering sustained throughput with zero-copy efficiency.

- [VAST DataBase](https://www.vastdata.com/platform/database) **:** A built-in, high-performance transactional database that captures semantic context—timestamps, GPS coordinates, sensor readings, and vector embeddings—directly alongside the video.

- [VAST DataEngine](https://www.vastdata.com/platform/dataengine) **:** An event-driven compute layer that reacts to this metadata in real time, triggering AI reasoning functions the moment meaningful patterns emerge.


This architecture is purpose-built for time-critical intelligence, enabling cities to move beyond retrospective analysis toward continuous, real-time understanding and response.

##### NVIDIA Cosmos Reason: The core of the video agent

At the heart of this system is [NVIDIA Cosmos Reason 2](https://huggingface.co/nvidia/Cosmos-Reason2-8B), a state-of-the-art reasoning VLM purpose-built for **physical AI and video-based agents**. Traditional video analytics models focus on detection and classification—identifying objects, counting entities, or triggering alerts based on predefined rules. While useful, these approaches struggle in real-world environments where ambiguity, occlusion, and evolving context are the norm.

Cosmos Reason goes beyond recognition to **reasoning**. By applying **Chain-of-Thought (CoT)** inference, the model interprets visual scenes in terms of intent, causality, and physical context. This enables it to answer higher-level questions, such as: _Why is something happening? What is likely to happen next? Does this situation require intervention?_

For smart cities, this distinction is critical. A reasoning VLM can:

- **Reduce false positives** by understanding context rather than reacting to isolated signals.

- **Differentiate normal behavior from true anomalies**, even when both look visually similar.

- **Support safer automation**, where responses are triggered only when the model has high confidence in its interpretation.

- **Adapt to novel situations** that were never explicitly programmed or labeled.


Deployed as an [NVIDIA NIM microservice](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/), Cosmos Reason introduces true “System 2” thinking into video analytics pipelines. It deliberately pauses to <think> before responding, allowing it to solve complex visual scenarios—such as distinguishing between a vehicle stopping for a pedestrian and one disabled in traffic.

This shift from reactive detection to deliberate reasoning enables cities to move faster without acting prematurely, improving both operational efficiency and public safety.​

![When the City Thinks: Real-Time Video Agents with VAST and NVIDIA Cosmos Reason 2](https://images.ctfassets.net/2f3meiv6rg5s/2ppO37pHEkVsYNTUlMdjYH/5a1b32626edaa1dcf631194f8183c70c/more-inference-less-infrastructure-vast-nvidia-1.webp?w=2580&fm=png&q=80)

Cosmos Reason 2 offers a few key improvements over the model’s original iteration:

- **Larger context window:** Cosmos Reason 2 has a 256,000-token context window, compared with 16,000 tokens for Cosmos Reason 1. This 16x increase allows Cosmos Reason 2 to handle longer videos and richer scenes.

- **Flexible deployment options:** Cosmos Reason 2 is available in 2B and 8B parameter counts, so users can deploy the size of model that suits their accuracy requirements, latency needs, and compute budgets. The new model can also run reliably across environments ranging from edge devices to large-scale cloud devices.

- **Improved spatial reasoning:** Cosmos Reason 2 features Advanced Spatial Perception, which includes stronger 2D grounding (for locating objects in a flat image). This new capability is essential for more advanced spatial reasoning and embodied AI applications, where understanding an object’s position in space is critical.


#### **Technical Workflow: The “City Watch” Pipeline**

A modern smart city may operate tens of thousands of cameras, continuously capturing streets, buildings, transit hubs, and public spaces. When integrated with VAST AI OS and NVIDIA Cosmos Reason 2, this video fabric becomes an always-on _city watch_ pipeline—capable of detecting events, reasoning about risk, and autonomously triggering real-world response workflows within seconds.

![When the City Thinks: Real-Time Video Agents with VAST and NVIDIA Cosmos Reason 2](https://images.ctfassets.net/2f3meiv6rg5s/67jZwv8lpUcxfH1xulG17Y/e7ef2298a95cb1bb85039d8b97e90c2f/more-inference-less-infrastructure-vast-nvidia-2.webp?w=2580&fm=png&q=80)

Figure 2: video intelligence workflow diagram

Here’s how it works at each step of the pipeline.

##### Ingest, store, and catalog

Live video streams are ingested into VAST DataStore and written as time-sliced objects (for example, 5–10 second clips). These objects land in a scalable object namespace optimized for sustained, high-throughput ingest. As each clip is written:

- Object metadata (timestamps, camera ID, GPS coordinates) is automatically extracted.

- Index entries are created.

- References are recorded in the VAST DataBase, forming a searchable, transactional catalog of live video.


This ensures that video and its semantic context are immediately queryable—without waiting for offline processing.

##### Trigger pipelines

The VAST DataEngine continuously monitors the DataBase for newly ingested, unprocessed video objects. The appearance of a new catalog entry acts as a native trigger, eliminating the need for external schedulers or polling systems.

Once triggered, the pipeline:

- Performs lightweight preprocessing (frame sampling, resolution normalization)

- Constructs a structured prompt

- Invokes **Cosmos Reason 2** via its NVIDIA NIM microservice and specifies an array of possible downstream agents that may be triggered based on the events in the video.


pipeline\_clip-0 from VAST Data on Vimeo

![video thumbnail](https://i.vimeocdn.com/video/2079375438-fee93f26c5049021f0c7c287cc163d3ffb9aecc1bc5c0dc207607aa330456819-d?mw=80&q=85)

Playing in picture-in-picture

Like

Add to Watch Later

Share

Embed

Pause

00:00

00:39

Settings

Speed

Quality360p

2x

1.5x

1.25x

1x

0.75x

0.5x

Picture-in-Picture

Fullscreen

[Watch on Vimeo](https://vimeo.com/1134415380?fl=pl&fe=vl)

##### Inference (the “thinking” step)

Cosmos Reason 2 analyzes the video clip using Chain-of-Thought reasoning, explicitly ruling out benign explanations before escalating an event.

- _Prompt:_ “Analyze visual input. Is there an active fire? Estimate size and threat level.”

- _Cosmos Thought:_ <think>Thick black smoke is rising. Flashing orange flames are visible at the base of the tree line. This is not steam. Wind is blowing smoke toward the pedestrian path.</think>

- _Output:_ {"event": "fire", "confidence": "high", "severity": "critical", "recommended\_agent": "emergency\_dispatch"}


Rather than serving only as metadata, this structured output becomes a control signal for the pipeline. The reasoning model is provided, as part of its context, with knowledge of the available downstream agents and their capabilities. Based on its interpretation of the situation, Cosmos Reason 2 explicitly determines which agent should be invoked next.

This allows the system to move beyond static, prewired flows. The reasoning step dynamically selects the appropriate response path—effectively turning the VLM into an orchestration brain rather than a passive classifier.

##### Autonomous agent action

The VAST Autonomous Agent framework, operating as part of the DataEngine’s agentic execution layer, consumes the structured output and dispatches the selected agent.

The chosen agent(s):

- Validate the reasoning output

- Apply policy and safety constraints

- Execute the corresponding real-world API action


For example, an emergency dispatch agent might connect to the city’s **emergency dispatch system API**, automatically dispatching fire services and attaching:

- The relevant video clip

- GPS coordinates and camera metadata

- Severity and contextual reasoning


This design enables **reasoning-driven orchestration**, where understanding the situation determines not just _what is detected_, but _what happens next_. Crucially, it also determines **what does** _**not**_ **happen**.

By allowing Cosmos Reason 2 to select downstream agents and functions dynamically, the system avoids indiscriminately running expensive AI workloads across every video stream. In an environment where **GPU resources are scarce and valuable**, only video segments that exhibit meaningful risk or ambiguity are escalated to deeper analysis or autonomous action. Benign or low-confidence scenarios are filtered early, preventing unnecessary model invocations.

The result is a pipeline that scales economically: compute is focused where it matters most, GPU cycles are preserved for high-impact events, and city-wide video intelligence remains both **responsive and sustainable**—even at tens of thousands of concurrent streams.

agents\_clip-0 from VAST Data on Vimeo

![video thumbnail](https://i.vimeocdn.com/video/2079375055-a41ef06f2b316e53e9eafa5f47141c5adda39acb706bc7fa867eb30b9aefe831-d?mw=80&q=85)

Playing in picture-in-picture

Like

Add to Watch Later

Share

Embed

Pause

00:00

01:07

Settings

Speed

Quality360p

2x

1.5x

1.25x

1x

0.75x

0.5x

Picture-in-Picture

Fullscreen

[Watch on Vimeo](https://vimeo.com/1134415312?fl=pl&fe=vl)

Apart from real-time analysis and actions, the addition of an embedding model into the pipeline also enables real-time retrieval augmented generation (RAG) on the same videos. This would allow, for example, investigators to search footage for factors that might have contributed to an accident (like the fire example above).

rag\_clip-0 from VAST Data on Vimeo

![video thumbnail](https://i.vimeocdn.com/video/2079374953-6fa42ff9339abef8fdcd2fafe9f0435716ac955ab16e9038a91124dae6e59973-d?mw=80&q=85)

Playing in picture-in-picture

Like

Add to Watch Later

Share

Embed

Pause

00:00

00:00

Settings

Speed

Quality360p

2x

1.5x

1.25x

1x

0.75x

0.5x

Picture-in-Picture

Fullscreen

[Watch on Vimeo](https://vimeo.com/1134415209?fl=pl&fe=vl)

#### **Why an AI-Native Architecture Matters**

**For developers**, the value of combining the VAST DataEngine with Cosmos Reason 2 is that it turns “smart city AI” into a set of composable, testable building blocks instead of a fragile custom pipeline:

- **Events, not cron jobs:** Video ingest, metadata updates, and Cosmos inferences are all expressed as event-driven functions. A fire-detection flow becomes: _object written → metadata row created → trigger fires → Cosmos NIM call → result persisted → follow-up trigger for high-confidence events_. That means you can version and deploy each function independently, monitor it, and roll back without touching the storage or database layers.

- **One data substrate, many agents:** The same infrastructure used for fire detection can also be used by other agents (e.g., traffic optimization, intrusion detection, or crowd analytics) without copying data into separate “AI silos.” As a developer, you work against a consistent API and schema; you add new agents by wiring new triggers and functions to existing data, not by standing up new infrastructure.

- **Intelligent compute utilization:** An environment with many diverse agents (potentially thousands) may quickly overwhelm compute resources. Every agent may assist a VLM, a reasoning model, embedding model, or perform object tracking pipeline. Cosmos Reason 2 is used as the model router to invoke only the relevant agents based on the content of a video clip (and possibly prior clips). This allows building agentic systems that have a very rich set of capabilities, while maximizing compute resource efficiency.

- **First-class reasoning in the loop:** Cosmos Reason 2’s structured outputs (timestamps, bounding boxes, severity, confidence scores) fit naturally into VAST’s DataStore model. That gives you a clean contract: VAST handles _when_ and _what_ to process; Cosmos handles _why it matters_; and your agents implement _what to do next_ (e.g., call dispatch APIs, update a digital twin, or notify operators).


**For cities**, this approach lets teams ship **production-grade** solutions while maintaining flexibility for the next set of agents and models they want to deploy. And because new use cases don’t require new infrastructure or systems, it’s **cost-effective**—the VAST Data foundation remains constant, meaning the biggest change to roll out new applications on top of it should be choosing the right models and agentic workflows.

Video has already proven immensely valuable for solving and deterring crime, but the combination of next-generation AI models and data infrastructure helps take it to the next level. With the ability to process, analyze, and act on data in real time, cities and other government entities can now help improve public safety by taking action as soon as incidents begin to unfold.

You can access the Cosmos Reason 2 model and learn more about it [here](https://huggingface.co/nvidia/Cosmos-Reason2-8B). To learn more about deploying data pipelines, such as video-reasoning workflows, using VAST DataEngine, [read this blog post](https://www.vastdata.com/blog/vast-dataengine-bringing-compute-to-your-data). And register for our inaugural [VAST FWD user conference](https://www.vastdata.com/vast-forward) to hear experts from VAST, NVIDIA, and other leading organizations discuss the cutting edge in AI use cases.

[![VAST Forward 2026](https://images.ctfassets.net/2f3meiv6rg5s/6eFigfvnTj2Wy3RZQ2quMe/88293c9f91004586a899e36c47db39d4/vast-forward-2026-banner.webp)](https://www.vastdata.com/vast-forward)

#### More from this topic

[![Why AI Factory Workloads Outgrow the Data Center ](https://images.ctfassets.net/2f3meiv6rg5s/2kWpTSzOHsovfOb3ouIgwP/8edc252cd5ef430544ad82deee4775e7/CR-15457_BFI_SEO_Why-AI-Factory-Workloads-Outgrow_VAST-Data.webp?w=3200&fm=png)\\
\\
Why AI Factory Workloads Outgrow the Data Center \\
\\
Can a traditional data center support an AI factory? Five failure modes show where legacy data infrastructure breaks as AI moves into production.](https://www.vastdata.com/blog/ai-factory-vs-data-center)

[![NVIDIA Dynamo + VAST = Scalable, Optimized Inference](https://images.ctfassets.net/2f3meiv6rg5s/62zUKLoTZXHthlK8IoiXLi/a3bb25122b47dec5e32e2c1e39fc7ade/nvidia-dynamo-vast-scalable-optimized-inference.webp?w=3200&fm=png)\\
\\
NVIDIA Dynamo + VAST = Scalable, Optimized Inference\\
\\
Solve the GPU Memory Wall: VAST Data and NVIDIA Dynamo boost LLM inference efficiency by 90% and TTFT by 20x using KV Cache Offload.](https://www.vastdata.com/blog/nvidia-dynamo-vast-scalable-optimized-inference)

[![Introducing VAST DataEnclave: Confidential AI for Sensitive Data and Proprietary Models](https://images.ctfassets.net/2f3meiv6rg5s/4Rs0D0AuAryJBJBsEeAX9F/b9cbfb0fbd2b7d92981faa6c7360a034/CR-15082_DataEnclave_FeatureVAST-Data.webp?w=3200&fm=png)\\
\\
Introducing VAST DataEnclave: Confidential AI for Sensitive Data and Proprietary Models\\
\\
VAST DataEnclave runs AI workloads in hardware-isolated environments, so proprietary models and sensitive data can meet on untrusted infrastructure.](https://www.vastdata.com/blog/introducing-vast-dataenclave-confidential-ai-for-sensitive-data-and-proprietary-models)

Learn what VAST can do for you

Sign up for our newsletter and learn more about VAST or request a [demo](https://www.vastdata.com/demo) and see for yourself.

Country \*United StatesAfghanistanAlbaniaAlgeriaAndorraAngolaAnguillaAntigua & BarbudaArgentinaArmeniaArubaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBosnia & HerzegovinaBotswanaBrazilBritish Virgin IslandsBruneiBulgariaBurkina FasoBurundiCambodiaCameroonCanadaCape VerdeCayman IslandsChadChileChinaColombiaCongoCook IslandsCosta RicaCote D IvoireCroatiaCruise ShipCubaCyprusCzech RepublicDenmarkDjiboutiDominicaDominican RepublicEcuadorEgyptEl SalvadorEquatorial GuineaEstoniaEthiopiaFalkland IslandsFaroe IslandsFijiFinlandFranceFrench PolynesiaFrench West IndiesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuamGuatemalaGuernseyGuineaGuinea BissauGuyanaHaitiHondurasHong KongHungaryIcelandIndiaIndonesiaIraqIrelandIsle of ManIsraelItalyJamaicaJapanJerseyJordanKazakhstanKenyaKuwaitKyrgyz RepublicLaosLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgMacauMacedoniaMadagascarMalawiMalaysiaMaldivesMaliMaltaMauritaniaMauritiusMexicoMoldovaMonacoMongoliaMontenegroMontserratMoroccoMozambiqueNamibiaNepalNetherlandsNetherlands AntillesNew CaledoniaNew ZealandNicaraguaNigerNigeriaNorwayOmanPakistanPalestinePanamaPapua New GuineaParaguayPeruPhilippinesPolandPortugalPuerto RicoQatarReunionRomaniaRwandaSaint Pierre & MiquelonSamoaSan MarinoSatelliteSaudi ArabiaSenegalSerbiaSeychellesSierra LeoneSingaporeSlovakiaSloveniaSouth AfricaSouth KoreaSpainSri LankaSt Kitts & NevisSt LuciaSt VincentSt. LuciaSudanSurinameSwazilandSwedenSwitzerlandTaiwanTajikistanTanzaniaThailandTimor L'EsteTogoTongaTrinidad & TobagoTunisiaTurkeyTurkmenistanTurks & CaicosUgandaUkraineUnited Arab EmiratesUnited KingdomUruguayUzbekistanVenezuelaVietnamVirgin Islands (US)YemenZambiaZimbabwe

How much Data Capacity do you have today? \*Less than 1 Petabyte1-10 Petabytes1-100 Petabytes100+ Petabytes

Want to receive info about products and services from VAST? You may unsubscribe from these communications at anytime.

Submit

By proceeding you agree to the [VAST Data Privacy Policy](https://www.vastdata.com/legal/privacy-policy).

\\* Required field.