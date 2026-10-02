Product

Feb 25, 2026

# Inside the Next Release of the VAST AI OS: New Capabilities for Real-Time AI at Scale

![Inside the Next Release of the VAST AI OS: New Capabilities for Real-Time AI at Scale](https://images.ctfassets.net/2f3meiv6rg5s/5LJnBHCxe8FF1J24AqzuUO/e20d51181392caa9b29b23862c30544a/inside-the-next-release-of-the-vast-ai-os.webp?w=1280&fm=png&q=80)

Authored by

Colleen Quinn, Product Marketing Director

Share This

[![Twitter](https://images.ctfassets.net/2f3meiv6rg5s/13UM456sGH9JXUxLl81X5O/7969616967f999451929bb5be0f435cc/icon-x.svg)](https://twitter.com/share?text=Inside%20the%20Next%20VAST%20AI%20OS%20Release:%20Real-Time%20AI%20at%20Scale%20-%20VAST%20Data&url=https://www.vastdata.com/blog/inside-the-next-release-of-the-vast-ai-os&hashtags=vastdata)

[![LinkedIn](https://images.ctfassets.net/2f3meiv6rg5s/4JynFMRw5umhHhRleKsV9W/f2269da24d5cba265f2b443aa45aacef/blog-linkedin.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https://www.vastdata.com/blog/inside-the-next-release-of-the-vast-ai-os&title=Inside%20the%20Next%20VAST%20AI%20OS%20Release:%20Real-Time%20AI%20at%20Scale%20-%20VAST%20Data&source=https://www.vastdata.com/blog/inside-the-next-release-of-the-vast-ai-os)

[![Reddit](https://images.ctfassets.net/2f3meiv6rg5s/gFi1N7KiqWuKHzDMNYwhf/720a9e9cdbc4bba4bc3c554aff3bba18/blog-reddit.svg)](https://www.reddit.com/submit?url=https://www.vastdata.com/blog/inside-the-next-release-of-the-vast-ai-os&title=Inside%20the%20Next%20VAST%20AI%20OS%20Release:%20Real-Time%20AI%20at%20Scale%20-%20VAST%20Data)

[![Email](https://images.ctfassets.net/2f3meiv6rg5s/30LFr1HT6NynCevNDxKd06/9f76a25c5fb820cf82f56cb2f6fe44a2/blog-email.svg)](mailto:?subject=Inside%20the%20Next%20VAST%20AI%20OS%20Release:%20Real-Time%20AI%20at%20Scale%20-%20VAST%20Data&body=Inside%20the%20Next%20VAST%20AI%20OS%20Release:%20Real-Time%20AI%20at%20Scale%20-%20VAST%20Data%0D%0Ahttps://www.vastdata.com/blog/inside-the-next-release-of-the-vast-ai-os)

![Copy Link](https://images.ctfassets.net/2f3meiv6rg5s/2KGF0XrDXSq3x2jDAgneCX/b2ccf23de3c4ccc5a9fb4cc073d7a46a/blog-link.svg)

#### Why the AI Stack Is Breaking and What Comes Next

An era does not end when a new technology appears. It ends when the assumptions that shaped the old one stop holding up.

For the last decade, enterprises have built AI, analytics, and event-driven systems as separate stacks. Data lives in one place. Analytics runs somewhere else. Vector databases sit off to the side. Event streams flow through their own infrastructure. Kubernetes clusters sprawl across teams. Each layer solves a real problem, but together they form architectures that are fragmented, expensive, and increasingly fragile at scale.

The premise has been simple: specialized systems deliver the best performance. In practice, this has produced pipelines where data is constantly copied, indexed, reshaped, and moved just to stay operational. Performance gains in one layer introduce bottlenecks in another. Governance becomes inconsistent. As systems scale, real-time guarantees are often weakened by batch-oriented processing and delayed execution paths.

As AI workloads become more demanding and more operational, real-time intelligence requires more than faster components. It requires a platform where data, vectors, events, and execution operate as one system.

That is the foundation VAST has built.

With this release, we are extending that foundation across four core dimensions of the [VAST AI Operating System](https://www.vastdata.com/platform/ai-os): hyperscale vector retrieval, native analytical execution, managed Kubernetes compute inside the cluster, and high-performance data movement for modern inference workloads.

Today, we are introducing a set of platform capabilities that strengthen each of these dimensions and move AI infrastructure closer to a unified, production-ready model.

#### **Introducing the VAST Hyperscale Vector Index**

Today, we are introducing the [VAST Hyperscale Vector Index](https://www.vastdata.com/features/ai-ready), a new indexing architecture that expands the performance and scale limits of the VAST vector store. Designed for real-time ingestion and search at trillion-vector scale, it is built directly into the VAST DataBase and eliminates the memory, sharding, and operational constraints that limit existing vector systems as workloads grow.

Vector databases promise semantic search, recommendations, multimodal retrieval, and large-scale reasoning. The prevailing assumption has been that vector search must run in a separate system built around in-memory structures and sharded indexes. That model works at modest scale. It begins to fracture at tens or hundreds of billions of vectors. Memory-resident indexes become prohibitively expensive. Sharding adds operational complexity and unpredictable performance. Hybrid search requires stitching together results across systems, introducing latency and governance gaps.

This strain is especially visible in large-scale video AI workloads. Organizations continuously ingest video streams, generate embeddings for frames and transcripts, and retrieve relevant segments in real time using both similarity and metadata. Embeddings quickly exceed memory budgets. Metadata resides elsewhere. What should be real time becomes brittle.

The VAST Hyperscale Vector Index takes a different approach.

At its core is new hierarchical clustering. Instead of maintaining a flat, largely memory-resident graph, VAST organizes vectors into a multi-level hierarchy of distance-based clusters. Coarse clusters at the top represent broad regions of vector space. Each successive level refines those regions into increasingly granular neighborhoods where nearest neighbors are most likely to reside.

![Inside the Next Release of the VAST AI OS: New Capabilities for Real-Time AI at Scale](https://images.ctfassets.net/2f3meiv6rg5s/7noYvPsULNwoMhuV2FvIe9/c1d88ef64fb170e860ddfe22f211f819/inside-the-next-release-of-the-vast-ai-os-1.webp?w=2580&fm=png&q=80)

Search follows the hierarchy. A query evaluates a bounded number of clusters at each level and descends only into the most promising candidates. Because traversal work is controlled and fanout is bounded, the cost per query depends on search effort rather than total corpus size. As datasets grow, hierarchy depth increases — but the number of clusters explored per query remains constrained. Query latency plateaus instead of rising linearly with scale.

In benchmarking with 1 billion 128-dimensional vectors, this architecture delivered approximately 1,000 queries per second, compared to roughly 89 queries per second on a widely used open-source vector database with a disk-based backend, a performance gap of more than 11× **.** A deeper technical analysis of that benchmark is available [here](https://www.vastdata.com/blog/architecture-behind-our-11x-vector-benchmark).

At 50 billion vectors on the same 8-node footprint, this architectural efficiency translated into approximately 91% lower cost per 1,000 searches compared to the same open-source vector configuration.

Implementation is integrated, not bolted on. The hierarchy is embedded directly into the VAST DataBase table layout and execution model. Vectors and metadata reside together under unified governance. Quantized vector representations enable memory-efficient traversal, and only the targeted cluster fragments required for a given query are read at execution time. Final scoring is applied to a reduced candidate set using higher-fidelity data.

Vector and index structures are stored persistently inside the [VAST DataBase](https://www.vastdata.com/platform/database) on the VAST [DASE architecture](https://www.vastdata.com/platform/how-it-works). Compute nodes pull only the necessary fragments, execute in parallel, and return results without relying on external vector services or memory-heavy replicas. Larger namespaces do not require proportionally larger DRAM pools simply to remain searchable.

Because vectors live alongside structured and semi-structured data, similarity search can be combined natively with SQL filters, joins, and metadata predicates. In a video RAG workflow, semantically relevant clips can be retrieved while filtering by time range, camera ID, location, or policy within a single execution path. Multi-modal retrieval becomes a first-class capability rather than an integration exercise.

![Inside the Next Release of the VAST AI OS: New Capabilities for Real-Time AI at Scale](https://images.ctfassets.net/2f3meiv6rg5s/6E52kG0wju6CMx7amOdEuB/7d6b587165c4aed79f138f158379e5db/inside-the-next-release-of-the-vast-ai-os-2.webp?w=2580&fm=png&q=80)

Most importantly, this occurs without sacrificing governance. Vectors inherit the same permissions and access controls as their underlying data throughout ingestion, indexing, and retrieval.

This is how vector search moves from experimental infrastructure to a production foundation for real-time AI at hyperscale.

#### **Expanding the VAST Native Query Engine**

TheVAST Native Query Engine is not new. It has powered vector retrieval inside the platform since we introduced our vector store earlier this year. What we are announcing now is the next phase of that engine’s evolution: full SQL-native aggregation and statistical support, expanding the engine from vector execution into broader analytical workloads.

With this release, the engine now supports more than 50 additional aggregation functions, including advanced statistical measures, quantiles and percentiles, correlation, and full regression analysis. Analytical queries that previously required external engines can now execute directly inside the VAST platform.

The underlying premise has been that analytics engines must sit outside the storage platform in order to scale. In practice, this separation creates unnecessary data movement, higher latency, and architectural sprawl.

We are taking a different path.

The VAST Native Query Engine runs directly inside the platform and was designed from the start to take advantage of the VAST DASE architecture. It already serves as a high-performance vector execution engine, combining similarity search and filtering within a single execution path while respecting governance and access controls at the data layer. With native SQL aggregations and statistical functions now integrated into that same execution framework, vector search and analytical processing operate without exporting data to external systems.

Analytical logic executes where the data lives. Vector similarity, SQL aggregation, and governed access operate within a unified execution model rather than across loosely connected components.

In practice, this enables workflows such as interactive analytics on operational data, AI-assisted investigations that combine similarity search with structured metrics, and real-time dashboards operating directly on continuously ingested data without pre-aggregation pipelines. Analysts can correlate events, metadata, and embeddings in a single query flow instead of stitching together results across multiple systems.

#### Improving Analytical Performance for Large Tables

High-performance analytics is not only a function of execution. It also depends on how efficiently data can be organized, pruned, and accessed at query time.

To improve analytical performance for large-scale workloads, the VAST DataBase introduces new partitioning optimization for large tables that reduce unnecessary scanning and improve execution locality.

For organizations that choose to use it, VAST now supports logical, SQL-native partitioning as a declarative performance optimization rather than a sharding or data placement strategy. Users express high-level intent, such as partitioning by time or category, and the platform automatically applies partition pruning, join optimization, and efficient deletes during query execution.

![Inside the Next Release of the VAST AI OS: New Capabilities for Real-Time AI at Scale](https://images.ctfassets.net/2f3meiv6rg5s/RKQ0h8pODNPLCczKgMQcq/1230f9cd6a624bbae035b7cf2a22ad6a/inside-the-next-release-of-the-vast-ai-os-3__1_.webp?w=2580&fm=png&q=80)

This is not traditional database partitioning. Customers do not manage shards, rebalance data, or reason about node ownership. There is no manual data routing or operational overhead. The system handles execution details transparently.

In a customer-driven case study, VAST showed consistently faster query execution for workloads aligned with logical partitioning and sort keys, with aggregate runtime improvements of roughly 20% compared to Iceberg-based tables. While results will vary by workload, the findings suggest that engine-managed pruning and locality optimizations can deliver meaningful analytical performance gains without introducing operational complexity.

#### **From Data Platform to Execution Platform**

Modern AI pipelines are not just about storing data and running queries. They require continuous execution. Data must be ingested, chunked, embedded, enriched, and indexed. Models must be deployed, invoked, monitored, and updated. Events must trigger processing in real time. In most environments, this requires operating separate Kubernetes clusters alongside the data platform.

That separation introduces latency, increases cost, and creates operational friction. Data moves between storage, vector systems, and external compute environments simply to keep pipelines running.

With this release, we are introducing **VAST Compute for Kubernetes** in the [VAST DataEngine](https://www.vastdata.com/platform/dataengine), bringing container orchestration and serverless execution directly into the VAST AI Operating System.

Administrators can provision up to 32 physical Kubernetes clusters on selected CNodes within a VAST cluster, allocating dedicated compute capacity for containerized workloads. Clusters may be assigned to individual tenants for strict physical isolation, or shared across tenants using namespace segmentation and enforced network policies for logical isolation.

![Inside the Next Release of the VAST AI OS: New Capabilities for Real-Time AI at Scale](https://images.ctfassets.net/2f3meiv6rg5s/4ygPiXlQbU9AZISYfXpm2i/4383057915bb5c57119f9d58a35dd6d2/inside-the-next-release-of-the-vast-ai-os-3.webp?w=2580&fm=png&q=80)

These clusters are fully managed by VAST. Provisioning, scaling, upgrades, and lifecycle operations are handled by the platform. Kubernetes runs as a hardened RKE2 distribution in FIPS mode. Control-plane state is backed up automatically, and access to the Kubernetes API and metrics endpoints is protected by mutual TLS. External control-plane exposure is not permitted.

GPU-enabled nodes are supported and automatically detected, allowing AI workloads to execute adjacent to the data they operate on with direct, high-performance access to VAST file, object, database, and event services.

![Inside the Next Release of the VAST AI OS: New Capabilities for Real-Time AI at Scale](https://images.ctfassets.net/2f3meiv6rg5s/78MphBaZIrzjMboEBZsvg3/375868399d62365c8b82a1b5e30f29f3/inside-the-next-release-of-the-vast-ai-os-4.webp?w=2580&fm=png&q=80)

In practice, this enables end-to-end AI pipelines to run entirely on VAST. Vectorization jobs, document and video chunking, embedding generation, and inference services execute next to the data. In a RAG workflow, embeddings are generated and indexed in place, retrieval operates on live vectors and metadata, and inference consumes results without exporting data to external compute tiers.

The result is a unified execution model in which data, vectors, events, and compute operate within a single system rather than across loosely coupled infrastructure layers.

Over time, these native compute clusters will serve as the foundation for higher-level managed services within the VAST AI Operating System, including pre-built data pipelines, inference services, and AI agents that run directly inside the platform.

#### **Bringing RDMA Performance to S3**

Performance at scale is not achieved through isolated optimizations. It is the result of architectural choices that eliminate unnecessary work.

Modern AI inference makes this clear. Large language models rely on a Key-Value (KV) cache to retain conversational context. As context windows expand toward 1 million tokens and beyond, the KV cache for a single session can exceed the capacity of GPU memory. What was once temporary data becomes a persistent working set that must move efficiently between compute and storage tiers.

To address this shift, NVIDIA introduced the Inference Context Management Service (ICMS), part of its CMS/CMX architecture, which sits between local SSDs and traditional network storage. ICMS enables KV cache data to be staged outside GPU memory while remaining accessible at high speed. But for this model to function at scale, the storage layer must operate as part of the inference data plane. Traditional HTTP-based S3 calls introduce CPU overhead, latency variability, and tail effects that are incompatible with high-concurrency serving.

We are [previewing S3 over RDMA](https://www.vastdata.com/blog/s3-over-rdma-scaling-the-kv-cache-data-plane), an upcoming capability that extends VAST’s RDMA-native architecture to object storage and allows S3-compatible workflows to operate directly on an RDMA transport.

VAST has always been built around a multi-protocol, RDMA-native data plane. Many customers already access file data over RDMA through NFS. With [S3 over RDMA](https://www.vastdata.com/blog/the-rise-of-s3-rdma), we extend this same foundation to object storage without introducing a new data path or siloed interface.

RDMA-based data movement is integrated into the existing S3 API while preserving standard S3 semantics. Control-plane operations continue over HTTP and TCP, while object payloads are transferred directly via RDMA. This enables architectures such as [NVIDIA ICMS](https://www.vastdata.com/blog/more-inference-less-infrastructure-vast-nvidia) to use S3-compatible storage while allowing the [BlueField-4 DPU](https://www.vastdata.com/press-releases/vast-data-brings-context-memory-to-agentic-ai-bluefield-4) to move KV data directly from flash into GPU HBM, bypassing host CPU bottlenecks.

Because this is a transport-level extension of the platform, data written through S3 over RDMA remains immediately accessible through NFS, SMB, analytics engines, vector workflows, and event-driven pipelines. Customers who already use RDMA-enabled file access can enable S3 over RDMA through simple configuration and immediately benefit from higher throughput and lower latency.

On the event side, native file triggers extend VAST’s event-driven automation beyond object storage to support [NFS-based workflows](https://www.vastdata.com/blog/meet-your-need-for-speed-with-nfs). File system events can trigger pipelines directly, allowing traditional file-centric environments to participate in real-time data processing without re-architecting ingestion flows.

These capabilities reinforce a single principle. Performance should emerge naturally when data, protocols, and execution share the same foundation.

#### **A Unified Foundation for Real-Time Intelligence**

These new capabilities reflect a continued evolution in how the VAST AI Operating System is designed and operated. Together, these capabilities strengthen four core dimensions of the VAST AI OS: retrieval, analytics, execution, and data movement.

Hyperscale vector indexing, native analytical query execution, managed Kubernetes compute, and high-performance data movement work together to support real-time AI and analytics without introducing additional operational complexity. Data remains governed, execution stays close to the data, and performance scales as workloads grow.

All of the capabilities described here will be delivered as part of a forthcoming release of the VAST AI OS planned for March 2026. With this release, organizations will be able to take advantage of these new building blocks to design AI and analytics systems that remain responsive, efficient, and manageable at extreme scale.

In the posts that follow, we will go deeper into the performance realities behind this architecture:

- See [hyperscale vector performance](https://www.vastdata.com/blog/architecture-behind-our-11x-vector-benchmark) in action, including real-time ingest and search at extreme scale

- Learn how VAST DataBase is [optimizing and accelerating EDW performance at scale](https://www.vastdata.com/blog/transactional-lakehousing-with-the-vast-database)

- Explore [a new model for event streaming at scale](https://www.vastdata.com/blog/understanding-the-vast-message-broker), built for sustained throughput and real-time processing


#### More from this topic

[![VAST AI OS 5.5 Is Generally Available](https://images.ctfassets.net/2f3meiv6rg5s/1solR7v208QzY4x05LiV8v/f871e17aef249c0bbf556e106077e58d/vast-ai-os-5-5-is-generally-available.webp?w=3200&fm=png)\\
\\
VAST AI OS 5.5 Is Generally Available\\
\\
Discover how VAST AI OS 5.5 unifies hyperscale vector search, native analytics, managed AI pipelines, and zero-copy operations for enterprise AI workloads.](https://www.vastdata.com/blog/vast-ai-os-5-5-is-generally-available)

[![The Fastest, Most Scalable AI and Analytics Platform - Period. ](https://images.ctfassets.net/2f3meiv6rg5s/LaTU7mOrf0ZaVwDeh15Jq/368bb694c58e010b345a8d3e964a0dda/the-fastest-most-scalable-ai-analytics-platform-period.webp?w=3200&fm=png)\\
\\
The Fastest, Most Scalable AI and Analytics Platform - Period. \\
\\
VAST: The fastest AI and analytics platform for real-time inference, streaming, and scale - powered by all-flash storage, DASE architecture, and NVMe-oF.](https://www.vastdata.com/blog/the-fastest-most-scalable-ai-analytics-platform-period)

[![Advancing the State of The Art with NVIDIA BlueField-4](https://images.ctfassets.net/2f3meiv6rg5s/2AKfJLkJwLEr7v9TrAQPBu/fc81a5dd24c7eafc18190563afb2a6ca/advancing-the-state-of-the-art-with-nvidia-blue-field-4.webp?w=3200&fm=png)\\
\\
Advancing the State of the Art with NVIDIA BlueField-4\\
\\
The Nvidia BlueField-4 networking platform enables fast, efficient performance for the VAST AI Operating System.](https://www.vastdata.com/blog/advancing-the-state-of-the-art-with-nvidia-blue-field-4)

Learn what VAST can do for you

Sign up for our newsletter and learn more about VAST or request a [demo](https://www.vastdata.com/demo) and see for yourself.

Country \*United StatesAfghanistanAlbaniaAlgeriaAndorraAngolaAnguillaAntigua & BarbudaArgentinaArmeniaArubaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBosnia & HerzegovinaBotswanaBrazilBritish Virgin IslandsBruneiBulgariaBurkina FasoBurundiCambodiaCameroonCanadaCape VerdeCayman IslandsChadChileChinaColombiaCongoCook IslandsCosta RicaCote D IvoireCroatiaCruise ShipCubaCyprusCzech RepublicDenmarkDjiboutiDominicaDominican RepublicEcuadorEgyptEl SalvadorEquatorial GuineaEstoniaEthiopiaFalkland IslandsFaroe IslandsFijiFinlandFranceFrench PolynesiaFrench West IndiesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuamGuatemalaGuernseyGuineaGuinea BissauGuyanaHaitiHondurasHong KongHungaryIcelandIndiaIndonesiaIraqIrelandIsle of ManIsraelItalyJamaicaJapanJerseyJordanKazakhstanKenyaKuwaitKyrgyz RepublicLaosLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgMacauMacedoniaMadagascarMalawiMalaysiaMaldivesMaliMaltaMauritaniaMauritiusMexicoMoldovaMonacoMongoliaMontenegroMontserratMoroccoMozambiqueNamibiaNepalNetherlandsNetherlands AntillesNew CaledoniaNew ZealandNicaraguaNigerNigeriaNorwayOmanPakistanPalestinePanamaPapua New GuineaParaguayPeruPhilippinesPolandPortugalPuerto RicoQatarReunionRomaniaRwandaSaint Pierre & MiquelonSamoaSan MarinoSatelliteSaudi ArabiaSenegalSerbiaSeychellesSierra LeoneSingaporeSlovakiaSloveniaSouth AfricaSouth KoreaSpainSri LankaSt Kitts & NevisSt LuciaSt VincentSt. LuciaSudanSurinameSwazilandSwedenSwitzerlandTaiwanTajikistanTanzaniaThailandTimor L'EsteTogoTongaTrinidad & TobagoTunisiaTurkeyTurkmenistanTurks & CaicosUgandaUkraineUnited Arab EmiratesUnited KingdomUruguayUzbekistanVenezuelaVietnamVirgin Islands (US)YemenZambiaZimbabwe

How much Data Capacity do you have today? \*Less than 1 Petabyte1-10 Petabytes1-100 Petabytes100+ Petabytes

Want to receive info about products and services from VAST? You may unsubscribe from these communications at anytime.

Submit

By proceeding you agree to the [VAST Data Privacy Policy](https://www.vastdata.com/legal/privacy-policy).

\\* Required field.