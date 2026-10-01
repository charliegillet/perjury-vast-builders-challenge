[Logo](https://www.vastdata.com/)

- Product
- Solutions
- [Customers](https://www.vastdata.com/customers)
- Resources
- Company

[Contact Sales](https://www.vastdata.com/personalized-demo) [Join a Live Demo](https://www.vastdata.com/demo)

Solutions

Jan 15, 2026

# Unlock Video Intelligence: Building Real-Time Video Search and AI Summary

![Unlock Video Intelligence: Build Real-Time Video Search and AI Summary](https://images.ctfassets.net/2f3meiv6rg5s/2X1FeSHxlX5s1LJ1DMKxO3/20d5451495e9d62888b30fa24c1450c0/unlock-video-intelligence-build-real-time-video-search-and-ai-summary.webp?w=1280&fm=png&q=80)

Authored by

Simon Golan, Senior Solutions Engineer and Ram Bansal, Developer Advocate

Share This

[![Twitter](https://images.ctfassets.net/2f3meiv6rg5s/13UM456sGH9JXUxLl81X5O/7969616967f999451929bb5be0f435cc/icon-x.svg)](https://twitter.com/share?text=Unlock%20Video%20Intelligence:%20Build%20Real-Time%20Video%20Search%20and%20AI%20Summary%20-%20VAST%20Data&url=https://www.vastdata.com/blog/unlock-video-intelligence-build-real-time-video-search-and-ai-summary&hashtags=vastdata)

[![LinkedIn](https://images.ctfassets.net/2f3meiv6rg5s/4JynFMRw5umhHhRleKsV9W/f2269da24d5cba265f2b443aa45aacef/blog-linkedin.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https://www.vastdata.com/blog/unlock-video-intelligence-build-real-time-video-search-and-ai-summary&title=Unlock%20Video%20Intelligence:%20Build%20Real-Time%20Video%20Search%20and%20AI%20Summary%20-%20VAST%20Data&source=https://www.vastdata.com/blog/unlock-video-intelligence-build-real-time-video-search-and-ai-summary)

[![Reddit](https://images.ctfassets.net/2f3meiv6rg5s/gFi1N7KiqWuKHzDMNYwhf/720a9e9cdbc4bba4bc3c554aff3bba18/blog-reddit.svg)](https://www.reddit.com/submit?url=https://www.vastdata.com/blog/unlock-video-intelligence-build-real-time-video-search-and-ai-summary&title=Unlock%20Video%20Intelligence:%20Build%20Real-Time%20Video%20Search%20and%20AI%20Summary%20-%20VAST%20Data)

[![Email](https://images.ctfassets.net/2f3meiv6rg5s/30LFr1HT6NynCevNDxKd06/9f76a25c5fb820cf82f56cb2f6fe44a2/blog-email.svg)](mailto:?subject=Unlock%20Video%20Intelligence:%20Build%20Real-Time%20Video%20Search%20and%20AI%20Summary%20-%20VAST%20Data&body=Unlock%20Video%20Intelligence:%20Build%20Real-Time%20Video%20Search%20and%20AI%20Summary%20-%20VAST%20Data%0D%0Ahttps://www.vastdata.com/blog/unlock-video-intelligence-build-real-time-video-search-and-ai-summary)

![Copy Link](https://images.ctfassets.net/2f3meiv6rg5s/2KGF0XrDXSq3x2jDAgneCX/b2ccf23de3c4ccc5a9fb4cc073d7a46a/blog-link.svg)

Reasoning with multimodal data at scale is unlocking the next wave of AI applications.

Video search powered by Vision Language Models (VLMs) enables systems to identify and act on relevant events in real-time, [transforming legacy video infrastructure](https://www.vastdata.com/blog/vast-nvidia-cosmos-reason-smart-cities) into intelligent, agentic applications for use cases like public incident detection.

The [VAST AI OS](https://www.vastdata.com/platform/ai-os) powers real-time multimodal inference applications at unprecedented scale and performance. The platform is built for data-intensive applications such as video processing to power agentic workflows:

![Video Search & Summary Reference Architecture](https://images.ctfassets.net/2f3meiv6rg5s/1fihepjOpNW9M9FiVaw3Ad/474b71d3b7d76525319c28de2dbc93ad/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-1.webp)

Let’s walk through the key steps to building a real-time video search and summarization application to create the foundation for agentic, multimodal workflows.

#### Why Developers Build on DataEngine

The VAST DataEngine runs on the [Disaggregated Shared-Everything](https://www.vastdata.com/platform/how-it-works) (DASE) architecture, leveraging the VAST Event Broker to ingest [hundreds of millions of messages per second](https://www.vastdata.com/blog/streaming-136m-messages-per-second-on-vast). The VAST AI OS is built from the ground up for AI-native applications to enable serverless functions powered by event streams and vector storage. VAST’s decoupling of compute and storage creates new opportunities for developers to run massive, real-time AI workloads without the bottlenecks of [legacy infrastructure](https://www.vastdata.com/blog/the-end-of-the-shared-nothing-era).

In this blog we’ll walk through how to use the [VAST DataEngine](https://www.vastdata.com/platform/dataengine) to build a real-time video search and summarization application. The DataEngine orchestrates video pipelines composed of serverless functions that operate directly on video stored in VAST’s S3-compatible object store. End users can search and explore video content through a client-facing Angular application, backed by a Python-based API. For a deeper overview of the VAST DataEngine, see our [previous post](https://www.vastdata.com/blog/vast-dataengine-bringing-compute-to-your-data).

#### Prerequisites

Before we dive in, you’ll want to complete the following setup steps:

- Source code:
  - The entire source code is available on [GitHub](https://github.com/vast-data/vss-blueprint)
  - All functionality is available as images via [public docker registry](https://hub.docker.com/u/vastdatasolutions)
- Access to NVIDIA Models:
  - [NVIDIA Cosmos Reason VLM](https://build.nvidia.com/nvidia/cosmos-reason1-7b)
  - [NVIDIA NIM API Endpoints](https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html) for embedding (`nvidia/nv-embedqa-e5-v5`) and reasoning (`meta/llama-3.1-8b-instruct`) models
- VAST Management System (VMS) setup by VMS admin:
  - Ensure DataEngine is enabled for the specific tenant
  - Create and share S3 and VastDB credentials for users building pipelines on DataEngine
- VAST DataEngine user:
  - Access to create and deploy DataEngine pipelines (pipelines = triggers + functions)
  - Credentials, secrets, endpoints [configuration details](https://github.com/vast-data/vss-blueprint/tree/main/deployments/dataengine-vss-ingest-pipeline#step-1-configure-secret) for VastDB, S3 buckets, and VLM are required for both pipelines and backend/frontend application
- A remote Kubernetes cluster to deploy the client application [frontend/backend](https://github.com/vast-data/vss-blueprint/tree/main/source-code/retrieval)
- Network access to VastDB and S3-compatible object storage

#### The Architecture

The frontend/backend applications are deployed on a remote Kubernetes cluster that’s accessible from your local development environment. Serverless functions are deployed to the DataEngine to orchestrate the end-to-end pipeline, from video ingestion and retrieval to multimodal inference and embedding generation.

The diagram below provides an overview of the system architecture:

![Kubernetes Cluster and VAST DataEngine (Serverless)](https://images.ctfassets.net/2f3meiv6rg5s/5SVf0Md2qCe95AvFYMWXIu/b36b12cd30d7c1a88c0eb3357765f4bf/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-2.webp)

#### Serverless Functions

Let’s walk through the serverless functions that make up the video pipelines powering search and summarization. Here we are focused on the two primary pipeline flows (stage 1 and stage 2):

![Serverless Functions](https://images.ctfassets.net/2f3meiv6rg5s/48ImFecTJ6PJPjzbN6pZUC/e96d429ddb79a3ec818c97fefedcafd1/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-3.webp)

`
Flow 1:

Trigger 1: user uploads video to S3 → Function: break video into segments

Flow 2:

Trigger 2: video segment added to S3 → Function: generate video summary w/ VLM → Function: generate summary embedding  → Function: store embeddings in VastDB
`

##### Segmenting Videos

In the first flow, once a video lands in the S3 bucket, `video-segments`, it is split into reasonably sized segments. These segments are stored in a separate S3 bucket, `video-chunks-segments`, which triggers the subsequent flow responsible for generating and storing video summaries.

By default, videos are segmented into 5-second slices, but this can be adjusted via the (`segment_duration`) environment variable.

The code snippet below handles storing the video segments:

![Segments Videos](https://images.ctfassets.net/2f3meiv6rg5s/1l56NbZf5W5toCxrNaCvZR/166b896c8d9d705ae6b858787994d9cf/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-4.webp)

Next, we’ll examine the DataEngine function that splits the video into segments and stores the results in a separate S3 bucket.

##### Generating Video Summaries

In the first flow, we retrieve videos and store segments of the video in an S3 bucket, `video-chunks-segments`. This triggers the second flow, where we generate summaries of each video segment and store them as vectors in the VAST DataBase.

We use the VLM to generate a summary for each 5-second segment. The code snippet below demonstrates how to generate a video summary, which is then returned from the function and passed to the next step in the pipeline:

![Generate Video Summaries](https://images.ctfassets.net/2f3meiv6rg5s/IGTSEoeQgpFTmX5QTzRoJ/506055b11bd300d44e34de1150ac1d02/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-5.webp)

Data returned from one function can be consumed by other functions in the DataEngine, with each function’s output triggering the next in the pipeline. At this point, we’ve covered how to generate descriptive summaries for video segments.

##### Generating Summary Embeddings

Once a video summary is generated, we use an embedding model to convert it into vectors. The pipeline produces summary embeddings for all video segments, enabling fast search and retrieval through the client-facing application. The code snippet below demonstrates how to generate these vector embeddings:

![Generate Summary Embedding](https://images.ctfassets.net/2f3meiv6rg5s/56MYBptJ4ujV9240rdcyn4/9ae344480783115d1f43f51c46ddd016/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-6.webp)

The embedding is returned from the function and consumed by the next step in the pipeline. At this point, vector embeddings for all video summaries have been successfully stored.

##### Storing Embeddings

The final function in the pipeline stores all generated embeddings. VastDB enables AI workloads and applications with native support for storing and searching vectors. Using the [VastDB SDK](https://github.com/vast-data/vastdb_sdk), we can store vectors efficiently with PyArrow:

![Store Embeddings](https://images.ctfassets.net/2f3meiv6rg5s/yI9CCd8T49Cbhp3TmeRIR/342f785d34c03b21d11cc480416d258d/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-7.webp)

Note that this is a reference architecture and that pipeline functions can be adapted to meet specific application requirements. For example, functions can be consolidated or expanded as needed.

With that, we’ve completed the second flow, generating and storing vector embeddings for all video segments.

#### Deploy the Client Application

In this section, we’ll review the frontend and backend components (Stage 3 Retrieve and Search). The full-stack code is available on [GitHub](https://github.com/vast-data/vss-blueprint/tree/main/source-code/retrieval).

Note that after deploying the client application, the DataEngine pipelines must also be deployed for users to upload and search videos.

To deploy the frontend and backend applications to the remote Kubernetes cluster, run the deployment [script](https://github.com/vast-data/vss-blueprint/blob/main/deployments/vss-k8s-application/QUICK_DEPLOY.sh) as follows:

![Deploy Client Application](https://images.ctfassets.net/2f3meiv6rg5s/4FDsuMz3SxmTrBqRNUZYJs/548ca980ac3e132bbeaab04fe0d9b2fd/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-8.webp)

After following the deployment instructions and updating your local `/etc/hosts` file, open the application in your browser (e.g., `http://video-lab.v209.vastdata.com`) to test authentication. Users are first presented with a screen to log in using their S3 credentials:

![VAST Video Reasoning Lab](https://images.ctfassets.net/2f3meiv6rg5s/2COM8TS8o4F8QXgqBdf0jr/a54265dafb0b4edf319a70accdcfa0a3/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-9.webp)

After authenticating, the user is able to access the video search and summarization UI:

![VAST DataEngine Video Reasoning Lab](https://images.ctfassets.net/2f3meiv6rg5s/XcxDCw5Y9p048EzueNTN5/6c64dd55dbc9312dbc79ed707d5abce9/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-10.webp)

In this flow, the user authenticates and gains access to the video search interface. They can upload videos to be processed by the DataEngine, enabling search once the video has passed through the processing pipeline.

When a user enters a search query and clicks “Search,” the backend performs a similarity search. The query is converted into an embedding, which is used to query the VastDB vector field and return matching video segments. The code snippet below demonstrates how the backend performs this similarity search:

![Similarity Search](https://images.ctfassets.net/2f3meiv6rg5s/4DB9SfNppDnqtULyyPpA5x/b7392e58156ebfb3054a46905243ad88/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-11.webp)

The user can continue to further prompt a specific search result of videos by toggling `Enable LLM Response`, which calls the below functionality to further prompt and reason about the videos returned in the search results:

![Synthesize Search Results](https://images.ctfassets.net/2f3meiv6rg5s/1AXSnxdoAUDnmetdimVVXR/3a80ea68641779b9c2fddad1e48376b0/unlock-video-intelligence-build-real-time-video-search-and-ai-summary-12.webp)

#### Build on VAST

Together, these steps demonstrate how to build a complete real-time video search and summarization pipeline using VAST DataEngine, serverless functions, VLMs, and VastDB to enable fast, scalable, and searchable video workflows.

#### Additional reading

- [Running Lightning-Fast Functions and AI Workloads on Kubernetes](https://www.vastdata.com/blog/kubernetes-ai-agents-pipelines)
- [Advanced AI Vision Search and Reasoning with the VAST InsightEngine with NVIDIA AI Blueprints](https://www.vastdata.com/blog/advanced-ai-vision-search-reasoning-vast-insightengine-nvidia-blueprints)
- [Video Reasoning Lab reference application](https://github.com/vast-data/vss-blueprint/tree/main)
- [VAST Cosmos Community](https://community.vastdata.com/)

#### More from this topic

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

[![Agent Sandboxes: Where Every Storage Trend Shows Up at Once](https://images.ctfassets.net/2f3meiv6rg5s/QBzHO5IDbaNO1CfX1nsr5/710d53476eca9847b994996536f4295c/CR-14557_BFI_Agent-Sandboxes_VAST-Data.webp?w=3200&fm=png)\\
\\
Agent Sandboxes: Where Every Storage Trend Shows Up at Once\\
\\
Learn why agent sandboxes are the ultimate test for AI storage, and how VAST Data solves extreme provisioning churn with isolated block and NFS.](https://www.vastdata.com/blog/agent-sandboxes-where-every-storage-trend-shows-up-at-once)

Learn what VAST can do for you

Sign up for our newsletter and learn more about VAST or request a [demo](https://www.vastdata.com/demo) and see for yourself.

Country \*United StatesAfghanistanAlbaniaAlgeriaAndorraAngolaAnguillaAntigua & BarbudaArgentinaArmeniaArubaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBosnia & HerzegovinaBotswanaBrazilBritish Virgin IslandsBruneiBulgariaBurkina FasoBurundiCambodiaCameroonCanadaCape VerdeCayman IslandsChadChileChinaColombiaCongoCook IslandsCosta RicaCote D IvoireCroatiaCruise ShipCubaCyprusCzech RepublicDenmarkDjiboutiDominicaDominican RepublicEcuadorEgyptEl SalvadorEquatorial GuineaEstoniaEthiopiaFalkland IslandsFaroe IslandsFijiFinlandFranceFrench PolynesiaFrench West IndiesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuamGuatemalaGuernseyGuineaGuinea BissauGuyanaHaitiHondurasHong KongHungaryIcelandIndiaIndonesiaIraqIrelandIsle of ManIsraelItalyJamaicaJapanJerseyJordanKazakhstanKenyaKuwaitKyrgyz RepublicLaosLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgMacauMacedoniaMadagascarMalawiMalaysiaMaldivesMaliMaltaMauritaniaMauritiusMexicoMoldovaMonacoMongoliaMontenegroMontserratMoroccoMozambiqueNamibiaNepalNetherlandsNetherlands AntillesNew CaledoniaNew ZealandNicaraguaNigerNigeriaNorwayOmanPakistanPalestinePanamaPapua New GuineaParaguayPeruPhilippinesPolandPortugalPuerto RicoQatarReunionRomaniaRwandaSaint Pierre & MiquelonSamoaSan MarinoSatelliteSaudi ArabiaSenegalSerbiaSeychellesSierra LeoneSingaporeSlovakiaSloveniaSouth AfricaSouth KoreaSpainSri LankaSt Kitts & NevisSt LuciaSt VincentSt. LuciaSudanSurinameSwazilandSwedenSwitzerlandTaiwanTajikistanTanzaniaThailandTimor L'EsteTogoTongaTrinidad & TobagoTunisiaTurkeyTurkmenistanTurks & CaicosUgandaUkraineUnited Arab EmiratesUnited KingdomUruguayUzbekistanVenezuelaVietnamVirgin Islands (US)YemenZambiaZimbabwe

How much Data Capacity do you have today? \*Less than 1 Petabyte1-10 Petabytes1-100 Petabytes100+ Petabytes

Want to receive info about products and services from VAST? You may unsubscribe from these communications at anytime.

Submit

By proceeding you agree to the [VAST Data Privacy Policy](https://www.vastdata.com/legal/privacy-policy).

\\* Required field.

### Explore the VAST Possibilities

[Talk to a Solution Engineer](https://www.vastdata.com/demo)

Get in Touch

[Email Us\\
\\
Contact hello@vastdata.com for a 24-hour response.](mailto:hello@vastdata.com "") [Call Us\\
\\
Speak with a team member today at 212-658-1753.](tel:212-658-1753 "Start Chat") [Contact Us\\
\\
Get in touch with us, and we’ll respond promptly!](https://www.vastdata.com/contact "")

Explore

Platform

- [AI Operating System](https://www.vastdata.com/platform/ai-os)
- [DASE Architecture](https://www.vastdata.com/how-it-works)

- [Gemini: Consumption Model](https://www.vastdata.com/gemini)

- [Supported Platforms](https://www.vastdata.com/supported-platforms)

- [Data Platform Services](https://www.vastdata.com/overview)

- [VAST DataStore](https://www.vastdata.com/datastore)

- [VAST DataSpace](https://www.vastdata.com/dataspace)

- [VAST DataBase](https://www.vastdata.com/database)

- [VAST DataEngine](https://www.vastdata.com/dataengine)

- [Scale-Out Solutions](https://www.vastdata.com/solutions)


Company

- [About](https://www.vastdata.com/about)

- [Customers](https://www.vastdata.com/customers)

- [Press Releases](https://www.vastdata.com/press-releases)

- [Partners](https://www.vastdata.com/partners)

- [Careers](https://www.vastdata.com/careers)

- [Contact](https://www.vastdata.com/contact)


Resources

- [Resource Library](https://www.vastdata.com/resources)

- [Blog](https://www.vastdata.com/blog)

- [Events](https://www.vastdata.com/events)

- [The VAST AI OS White Paper](https://www.vastdata.com/vast-data-platform-explained)
- [Help Center](https://www.vastdata.com/help)

- [Cosmos User Community](https://community.vastdata.com/)
- [Training & Certification](https://www.vastdata.com/training)


- [![social_icon](https://images.ctfassets.net/2f3meiv6rg5s/gmUbd6fpuNzImeOqeIhuE/ef75da10ae88fc128a9c9d35216ff682/icon-x-white.svg)](https://twitter.com/VAST_Data)
- [![social_icon](https://images.ctfassets.net/2f3meiv6rg5s/bGIsvcEKGz6oxdb6VCdQO/950221334384f172017fb850ef6aa95c/Icon-26.svg)](https://www.linkedin.com/company/vast-data)
- [![social_icon](https://images.ctfassets.net/2f3meiv6rg5s/3nESLsAkFBRjmCXyLJnz4S/d2e0260ccdcbf36d83cba696667d7bb2/Icon-28.svg)](https://www.youtube.com/vastdata)
- [![social_icon](https://images.ctfassets.net/2f3meiv6rg5s/kzta3TInGWUCtfVUh2xLl/86c81cf49557f5fb2d59dd34946bcf81/Icon-29.svg)](https://vastsupport.slack.com/)

© VAST 2026.

All rights reserved

© VAST 2026. All rights reserved

- [End User Agreement](https://www.vastdata.com/legal/end-user-services-and-license-agreement)
- [Terms of Service](https://www.vastdata.com/legal/support-services-terms)
- [Terms of Use](https://www.vastdata.com/legal/terms-of-use)
- [Privacy Policy](https://www.vastdata.com/legal/privacy-policy)
- [Cookie Policy](https://www.vastdata.com/legal/cookie-policy)
- Cookies Settings
- English