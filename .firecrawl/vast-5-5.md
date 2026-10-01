[Skip to content](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#wp--skip-link--target)

![](https://lotsofdata.blog/wp-content/uploads/2026/05/lotsofdata-logomark.png)[Lots of Data](https://lotsofdata.blog/)

AI workloads, data platforms, and infrastructure notes, written from the engineering edge between benchmarks and production.

[AI](https://lotsofdata.blog/category/ai/) [Kubernetes](https://lotsofdata.blog/category/virtualization/kubernetes/) [vSphere](https://lotsofdata.blog/category/virtualization/vsphere/) [VAST Data](https://lotsofdata.blog/category/vast-data/) [About](https://lotsofdata.blog/about/)

[RSS feed](https://lotsofdata.blog/feed/) Night mode

Search postsSearch

[Agentic AI](https://lotsofdata.blog/category/ai/agentic-ai/) / [AI](https://lotsofdata.blog/category/ai/) / [VAST Data](https://lotsofdata.blog/category/vast-data/)

# VAST AI OS 5.5, Part 1: Vectors, Analytics, and Pipeline Compute

VAST AI OS 5.5 Part 1: vectors, analytics, and pipeline compute—and what the release means for storage, database, and AI teams.

I

Itzik _— VP Mission Alignment, VAST Data_

·

06 Aug 2026

·

13 min read

* * *

_The AI and database half of what’s new in 5.5, and why it’s the part that actually earns the “AI Operating System” name_

![](https://i0.wp.com/lotsofdata.blog/wp-content/uploads/2026/08/image-3.png?resize=1024%2C470&ssl=1)

# Where 5.5 Fits in VAST’s Story

VAST Data has spent the last year turning its data platform into something we call the AI Operating System: a single stack meant to carry data, database services, and AI compute through one architecture instead of stitching them together from separate products. The AI OS itself was unveiled in May 2025, and VAST has been layering capability onto it release by release ever since.

**On this page**

- [Hyperscale Vector Index](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#hyperscale-vector-index)
- [Partitioning for Large Tables](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#partitioning-for-large-tables)
- [How the Indexing Actually Works](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#how-the-indexing-actually-works)
- [New VASTDB Query Engine SQL Capabilities](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#new-vastdb-query-engine-sql-capabilities)
- [Row & Column Security](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#row-and-column-security)
- [Larger Cells: 5MB (up from 126KB)](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#larger-cells-5mb-up-from-126kb)
- [VAST Native Compute for DataEngine](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#vast-native-compute-for-dataengine)
- [NFSv4 File Triggers](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#nfsv4-file-triggers)
- [Kafka mTLS](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#kafka-mtls)
- [DataEngine Runtime SDK](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#dataengine-runtime-sdk)
- [On the Horizon: S3 over RDMA](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#on-the-horizon-s3-over-rdma)

5.5 is the next major step in that arc. we previewed it publicly in a February 2026 blog post, and the pitch behind it was less about any single feature than a diagnosis: most AI shops end up running their vector store, their analytics engine, their event pipeline, and their Kubernetes footprint as four separate systems stitched together after the fact, and every seam between them costs latency, headcount, or both. VAST’s answer was to fold four of those jobs back under one roof: faster vector lookups at scale, analytics that run without shipping data elsewhere, Kubernetes workloads hosted on the cluster itself, and quicker movement of data for inference. A company MeetUp deck circulated in Japan around the same time pointed to an April 2026 release window and singled out three of those as the headline items: the Hyperscale Vector Index, an in-storage Native Query Engine, and an internal Kubernetes environment for DataEngine pipelines.

That target held, and then some. VAST AI OS 5.5 went generally available today, August 6, 2026, the same date the internal deck’s restricted-GA banner had been counting down to. This is the first of two posts covering the release: this one is about the AI and database side, the vector index, the analytics engine, and DataEngine’s new native compute. A companion piece covers the other half, the storage-operations changes (DBox decommission, block QoS, mTLS, replication) that matter more to whoever actually runs the cluster day to day. Everything below draws on both the internal technical materials VAST’s field teams use and VAST’s own public 5.5 announcements, cross-checked against the official 5.5.0 release notes.

![](https://i0.wp.com/lotsofdata.blog/wp-content/uploads/2026/08/image-36.jpeg?resize=907%2C510&ssl=1)

_The full 5.5 feature summary, grouped by AI OS pillar. This post covers DataBase and DataEngine; the companion post covers DataStore, DataSpace, and Cloud._

# VAST DataBase: Vector Scale, SQL Depth, and Fine-Grained Security

DataBase is where 5.5’s AI-era ambitions are most visible, anchored by a vector index built to operate at a scale most vector databases can’t reach without a large hardware expansion.

## Hyperscale Vector Index

VAST’s vector index is built directly into VAST DataBase rather than bolted on as a separate service, storing embeddings as an additional column alongside a row’s regular metadata and files. 5.5 extends that index’s performance and scale ceiling to trillions of vectors, designed for real-time ingestion and search at that scale.

![](https://i0.wp.com/lotsofdata.blog/wp-content/uploads/2026/08/image-29.jpeg?resize=864%2C486&ssl=1)

_The Hyperscale Vector Index, built into VAST DataBase, targets trillion-vector scale with real-time ingest._

- array\_distance: Euclidean distance
- array\_cosine\_distance: semantic similarity
- array\_negative\_inner\_product: common in recommendation engines

VAST’s own published benchmarks put vector retrieval at roughly 10x faster than a leading open-source vector database at 1 billion 128-dimensional vectors. Push the comparison to 50 billion vectors on the same 8-node footprint, and that architectural efficiency turns into roughly 91% lower cost per 1,000 searches against the same open-source configuration, since VAST loads only the relevant quantized subset of vectors into memory per query rather than holding the whole graph index resident in RAM. Scale ends up bounded by storage, not by how much memory you can afford to buy.

A few boundaries worth knowing before you design around this: a vector index has to be chosen at table-creation time (Euclidean distance or cosine inner product), can’t be added retroactively to an existing table, can’t be disabled once enabled, and can’t have its distance metric changed afterward. Only one vector column per table is supported. And notably, vector index search only works through VAST’s own Query Engine right now, the Trino, Spark, and Dremio connectors don’t support vector index-based search yet, so a hybrid SQL-plus-similarity query has to go through the native engine, not your existing BI or Spark pipeline.

## Partitioning for Large Tables

This one didn’t appear anywhere in the internal deck this post started from, which is a useful reminder that some of the sharper numbers only surface once a release actually ships. VASTDB now supports SQL-native declarative partitioning: name a partitioning scheme, up to four column transformations plus up to four sort-key columns, and query execution gets faster on its own, since the engine skips over irrelevant partitions, optimizes joins, and cleans up deleted data without being told how. A Spark example from the documentation makes the shape of it concrete: CREATE TABLE my\_table (…) PARTITIONED BY (day(event\_time), event\_type) ORDERED BY (event\_time). Nobody on the customer side is managing shards or rebalancing data by hand; the engine owns that job.

Benchmarked against Iceberg-based tables, VAST is claiming a substantial edge: over 60% faster on queries that filter down to a small slice of data, roughly 200 times faster on updates, and about a fifth faster overall runtime in one real customer’s manufacturing deployment. If those figures look familiar from elsewhere in VAST’s messaging around 5.5, they belong here, to partitioning, rather than to the vector index above; the two capabilities get compared against different baselines (Iceberg tables versus an open-source vector database) and it’s easy to see how they’d get conflated in a fast-moving launch.

It’s also worth being clear-eyed about scope: partitioning is defined at table creation and can’t be turned off afterward, it’s mutually exclusive with vector indexing, semi-sorted projections, and user-defined row IDs on the same table, replication of partitioned tables isn’t supported yet, and, somewhat counterintuitively given everything else in this post, VAST’s own Query Engine does not support table partitions at all. Partitioned tables are a Trino- and Spark-side capability today, not a native-engine one.

## How the Indexing Actually Works

The index uses hierarchical clustering with a radix (K) of 1,000: vectors land in an unclustered table on ingest, get grouped into initial Level-2 clusters of roughly a million vectors, and a centralized background task continuously selects the least-optimal clusters and re-runs k-means on them, recreating denser clusters one level at a time as data accumulates.

![](https://i0.wp.com/lotsofdata.blog/wp-content/uploads/2026/08/image-30.jpeg?resize=864%2C486&ssl=1)

_Hierarchical clustering repeatedly reclusters the least-optimal groups into denser clusters, level by level._

Search works as progressive narrowing: a top-down traversal from the coarse top-level clusters down to the final candidate set, which VAST reports achieves roughly 11x queries-per-second at 99% recall against comparable alternatives. Because embeddings live in the same table structure as the rest of a row’s data, vector columns inherit VAST’s existing enterprise security model rather than needing a separate access-control layer.

## New VASTDB Query Engine SQL Capabilities

5.5 brings VASTDB’s native query engine up to a much fuller SQL surface, adding both Data Definition Language (DDL: CREATE, ALTER, DROP, TRUNCATE for tables, indexes, schemas, and views) and Data Manipulation Language (DML: INSERT, UPDATE, DELETE, SELECT) support.

![](https://i0.wp.com/lotsofdata.blog/wp-content/uploads/2026/08/image-38.jpeg?resize=864%2C486&ssl=1)

_DDL and DML support, plus a broader library of aggregation, statistical, and precision-arithmetic functions._

Alongside DDL/DML, the query engine’s function library, built on DuckDB logic, expands substantially: core aggregates (SUM, MIN, MAX, AVG, COUNT with conditionals), statistical functions (variance, standard deviation, skewness, kurtosis, covariance), regression and correlation (regr\_slope, regr\_intercept, corr), advanced quantiles (median, mode, percentile\_cont/disc, reservoir-based sampling), boolean/bitwise operations, and Kahan-based precision arithmetic (fsum, favg) for floating-point accuracy at scale.

It’s worth being upfront about what’s deliberately left out of this pass, since VAST’s own release notes are candid about it: you can’t yet sort results, dedupe them, or group rows together within an aggregate query, and approximate functions, histogram-based aggregations, weighted aggregations, and list-producing functions are still on the roadmap. The scope choice is single-pass aggregation and statistical analysis on live, in-place data, not full data-warehouse SQL coverage. That’s a reasonable place to draw the line for a first pass, and it fits the broader pattern in 5.5: depth where AI and operational workloads actually need it first, breadth later.

## Row & Column Security

Fine-Grained Access Control (FGAC) adds row- and column-level restriction on top of VASTDB’s existing security model: allow/deny lists and masking at the column level, row-level filtering, and end-user pushdown (impersonation) for Trino, with row filtering coordinated against VAST’s own authorization layer.

![](https://i0.wp.com/lotsofdata.blog/wp-content/uploads/2026/08/image-34.jpeg?resize=864%2C486&ssl=1)

_A user with column-level allow-listing sees only the columns their policy permits: the same table, filtered per identity._

This is squarely a compliance feature, the GDPR, HIPAA, CCPA-style requirements where the same underlying table needs to present different views of itself depending on who’s querying it, without pushing that logic into every application that touches the data.

## Larger Cells: 5MB (up from 126KB)

The maximum size of a single database cell rises from 126KB to 5MB in 5.5, with every connector (Spark, Trino, the Python and Java SDKs, and the native query engine) updated to handle the larger size. Insert, update, import, query, and deletion (including background truncation of the larger cell’s constituent pieces) are all supported at the new limit, and replication of large cells works between clusters where every member supports them.

# VAST DataEngine: Compute Comes Inside the Cluster

DataEngine is VAST’s serverless compute layer, and 5.5’s biggest structural change here is letting the entire data lifecycle (ingest, transform, serve) run inside the VAST cluster itself, without shipping data out to an external compute environment first.

## VAST Native Compute for DataEngine

Running DataEngine in production means deciding how its compute gets managed, and 5.5 formalizes two paths rather than forcing one. Bring Your Own Compute (BYOC) is the option for organizations that already have Kubernetes infrastructure and just want VAST to own the data-and-pipeline side of things while their own team keeps running the cluster underneath it. VAST Native Compute is the newer, more hands-off option: an administrator dedicates a subset of a cluster’s CNodes to run a fully managed, internal Kubernetes cluster hosting DataEngine’s serverless functions, and from there VAST owns provisioning, scaling, upgrades, and lifecycle end to end. That compute cluster is created independent of any tenant and can then be attached to one tenant exclusively or shared across several, each with its own isolated namespace. A single VAST cluster can host up to 32 of these physical Kubernetes clusters, which gives real room for physical isolation between tenants that need it, not just namespace-level separation.

![](https://i0.wp.com/lotsofdata.blog/wp-content/uploads/2026/08/image-35.jpeg?resize=864%2C486&ssl=1)

_CNodes host DataEngine’s serverless functions directly, rather than routing to external compute._

- Minimum of 3 CNodes to form a compute cluster, needing N+1 available IPs
- High availability via N-1/N quorum, snapshot-based control-plane recovery, and rolling non-disruptive upgrades
- Strict tenant isolation through Kubernetes namespaces (tenant-{guid}), or full physical isolation via separate clusters

The security posture is more locked-down than a typical self-managed cluster too: Kubernetes runs as a hardened RKE2 distribution in FIPS mode, control-plane state is backed up automatically, and the Kubernetes API and metrics endpoints are only reachable over mutual TLS, with no external control-plane exposure permitted at all. For a team that would otherwise have to own RBAC, certificate rotation, and OS patching themselves, that’s a meaningful chunk of Day 2 operational burden that simply goes away.

Administrators choose how much of the selected CNodes’ resources to dedicate: Low Compute (roughly 25%, no cap on CNode count), Balanced Compute & Storage (roughly 50%, split evenly), Memory Heavy (RAM-weighted), or High Compute (100% of the selected CNodes). Memory Heavy and High Compute carry the steepest hardware floor: on top of the 3 CNodes needed to stand up the compute cluster itself, both modes require at least 2 additional unallocated CNodes, 5 CNodes minimum, in practice, before either option is available. One thing worth flagging for anyone sizing this: the official 5.5.0 release notes describe HA master allocation kicking in at a higher watermark than the earlier public materials suggested, once a compute cluster grows past 15 CNodes, five master nodes get allocated automatically rather than the smaller cluster’s usual three. If you’re planning capacity, size against that number rather than against the smaller thresholds floating around in earlier collateral. A CNode can only belong to one compute cluster at a time, and this capability isn’t available on VAST on Cloud as of 5.5.0.

![](https://i0.wp.com/lotsofdata.blog/wp-content/uploads/2026/08/image-31.jpeg?resize=864%2C486&ssl=1)

_Creating a VAST Compute Cluster: selecting CNodes and a resource-allocation profile._

The net effect is that a customer without an existing Kubernetes environment can now run DataEngine’s serverless functions natively on VAST hardware, with autoscaling and fault tolerance handled by VMS, instead of standing up and maintaining an external cluster just to host pipeline logic. And this is explicitly a first step rather than the end state: SyncEngine, for moving data across external sources and regions with the same containerized simplicity, is already available on top of this compute layer, AgentEngine (autonomous agents acting on data patterns in real time) is coming next, and GPU-accelerated CNode-X worker nodes are in technical preview for running generative AI and deep learning workloads without shipping data out to an external GPU cluster.

## NFSv4 File Triggers

DataEngine’s event triggers were S3-only before 5.5. Now NFSv4 gets native, file-based triggers too (the deck’s own naming shifted from “object-based” to “file-based” between revisions, since these fire on NFSv4 files rather than S3 objects), so a pipeline can wake up in response to activity on files written over NFS rather than only objects written over S3.

![](https://i0.wp.com/lotsofdata.blog/wp-content/uploads/2026/08/image-32.jpeg?resize=864%2C486&ssl=1)

_Configuring a native NFSv4 trigger in DataEngine, explicitly flagged as NFSv4-protocol-only._

- File Created: ElementCreated
- File Deleted: ElementDeleted
- File Xattr Created/Deleted: ElementTagCreated / ElementTagDeleted
- File ACL Changed: ElementAccessModified

A view needs both S3 and NFS enabled to carry NFSv4 triggers, the feature isn’t supported on NFSv3, and it’s incompatible with NFSv4 delegations, details worth knowing before wiring a pipeline to it. And, consistent with the NFSv4.2 xattr feature covered in the companion post, the NFSv4 xattr trigger types are explicitly called out as separate from S3 tags.

## Kafka mTLS

Kafka client connections pick up the same certificate-based model already introduced for NFS (covered in the companion post): mutual TLS gives both the client and the Kafka broker a trusted certificate, which serves double duty as both tenant identification (allowing a shared VIP pool across tenants) and user identification.

![](https://i0.wp.com/lotsofdata.blog/wp-content/uploads/2026/08/image-37.jpeg?resize=864%2C486&ssl=1)

_Kafka clients authenticate via mTLS certificates, mapped to tenants through VMS._

This secures client-to-tenant data in transit and is aimed squarely at zero-trust environments where unauthenticated broker access isn’t acceptable.

## DataEngine Runtime SDK

A new runtime SDK removes a lot of the boilerplate from writing DataEngine functions, variable passing, initialization code, by leveraging VAST’s integrated operators and runtimes directly. It ships with native clients for S3, VASTDB, Kafka, Trino, and Spark, integrated support for user-defined metrics, and facilities for batch execution.

![](https://i0.wp.com/lotsofdata.blog/wp-content/uploads/2026/08/image-33.jpeg?resize=864%2C486&ssl=1)

_The DataEngine Runtime SDK exposes native clients for S3, VASTDB, Kafka, Trino, and Spark._

## On the Horizon: S3 over RDMA

One capability from VAST’s public roadmap is worth flagging even though it’s a preview rather than a GA feature in 5.5, because it explains where the data-movement side of this release is headed. As context windows push past hundreds of thousands of tokens, a single inference session’s KV cache can grow larger than the GPU’s own memory has room for, so it needs somewhere fast to live outside the GPU, and that somewhere increasingly has to look like real storage rather than scratch space. The trouble is that ordinary S3 runs over HTTP, and HTTP brings CPU cycles and unpredictable response times into a path where neither is welcome at inference speeds. VAST is previewing S3 over RDMA to route around that: object payloads move over RDMA while control-plane calls stay on ordinary HTTP, so existing S3 tooling keeps working while the data path gets fast enough to feed a GPU directly, including via NVIDIA’s BlueField-4 DPU. It’s an early look rather than a shipping feature, but it’s a good indicator of where VAST is taking the data-movement side of the AI OS next.

That covers the AI and database half of 5.5. The companion post picks up the other half, the storage-operations changes, DBox decommission, block QoS, mTLS, async replication for block, and the multi-tenancy scale increase, and closes with my overall take on the release and a working upgrade checklist.

# Appendix: Official Documentation

Version 5.5 documentation index: [kb.vastdata.com/documentation/docs/version-5-5](https://kb.vastdata.com/documentation/docs/version-5-5)

VAST Cluster 5.5 Administrator’s Guide: [kb.vastdata.com/documentation/docs/vast-cluster-5-5-administrator-s-guide](https://kb.vastdata.com/documentation/docs/vast-cluster-5-5-administrator-s-guide)

VAST Cluster 5.5 DataEngine User Guide: [kb.vastdata.com/documentation/docs/vast-cluster-5-5-dataengine-user-guide](https://kb.vastdata.com/documentation/docs/vast-cluster-5-5-dataengine-user-guide)

VAST Cluster 5.5.0 Release Notes (the definitive new-features and limitations list): [kb.vastdata.com/documentation/docs/vast-cluster-5-5-release-notes](https://kb.vastdata.com/documentation/docs/vast-cluster-5-5-release-notes)

**Related on Lots of Data:** [VAST AI OS 5.5 Part 2](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-part-2-what-changes-for-the-team-running-the-cluster/) · [VMware XCOPY on VAST AI OS 5.5](https://lotsofdata.blog/2026/08/23/integrating-vmware-xcopy-with-vast-ai-os-5-5/)

### Share this:

- [Share on X (Opens in new window)X](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/?share=twitter&nb=1)
- [Share on Facebook (Opens in new window)Facebook](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/?share=facebook&nb=1)

### Like this:

LikeLoading…

[Share →](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#) [Cite this post →](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#) [Discuss on LinkedIn →](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#)

[← Previous](https://lotsofdata.blog/2026/08/05/replicating-kubernetes-workloads-with-vast-data-5-5-csi-2-6-6/)

[Next →](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-part-2-what-changes-for-the-team-running-the-cluster/)

## More like this

- Sep 2026



## [VAST CSI & COSI Drivers 2.7: Grown-Up Buckets, Safer NFS and Fully Documented Replication](https://lotsofdata.blog/2026/09/24/vast-csi-cosi-drivers-2-7-grown-up-buckets-safer-nfs-and-fully-documented-replication/)

- Sep 2026



## [Automating VAST Data with Ansible: Inside the vastdata.vms Collection](https://lotsofdata.blog/2026/09/24/automating-vast-data-with-ansible-inside-the-vastdata-vms-collection/)

- Sep 2026



## [VAST DataEnclave: Bringing Frontier AI to the Data That Could Never Leave the Building](https://lotsofdata.blog/2026/09/23/vast-dataenclave-bringing-frontier-ai-to-the-data-that-could-never-leave-the-building/)


#### Subscribe

A short note when something new goes up. No tracking, no marketing.

Notify me

#### Elsewhere

[RSS Feed →](https://lotsofdata.blog/feed/) [LinkedIn →](https://www.linkedin.com/in/itzikreich/) [X →](https://x.com/itzikr) [Email →](https://lotsofdata.blog/about/)

Set in Fraunces, Newsreader & IBM Plex.

©  — Lots of Data

## Discover more from Lots of Data

Subscribe now to keep reading and get access to the full archive.

Type your email…

Subscribe

[Continue reading](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#)

[Toggle photo metadata visibility](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#)[Toggle photo comments visibility](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#)

Loading Comments...

Write a Comment...

Email (Required)Name (Required)Website

[Download image](https://lotsofdata.blog/2026/08/06/vast-ai-os-5-5-a-deep-dive-into-the-operating-systems-next-release/#)

%d