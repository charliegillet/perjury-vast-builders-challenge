Solutions

Feb 9, 2026

# Talk to Your Data Infrastructure: Accelerate Infrastructure Management with MCPs

![Talk to Your Data Infrastructure: Accelerate Infrastructure Management with MCPs](https://images.ctfassets.net/2f3meiv6rg5s/2LnM2HWA3ZkxWEiUZ8E6o2/79a1f83a84594c888a5654b712a1a37d/data-infrastructure-accelerate-infrastructure-management-with-mcps.webp?w=1280&fm=png&q=80)

Authored by

Haim Marko, Solution Architect \| Ram Bansal, Developer Advocate

Share This

[![Twitter](https://images.ctfassets.net/2f3meiv6rg5s/13UM456sGH9JXUxLl81X5O/7969616967f999451929bb5be0f435cc/icon-x.svg)](https://twitter.com/share?text=Talk%20to%20Your%20Data%20Infrastructure:%20Accelerate%20Infrastructure%20Management%20with%20MCPs%20-%20VAST%20Data&url=https://www.vastdata.com/blog/data-infrastructure-accelerate-infrastructure-management-with-mcps&hashtags=vastdata)

[![LinkedIn](https://images.ctfassets.net/2f3meiv6rg5s/4JynFMRw5umhHhRleKsV9W/f2269da24d5cba265f2b443aa45aacef/blog-linkedin.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https://www.vastdata.com/blog/data-infrastructure-accelerate-infrastructure-management-with-mcps&title=Talk%20to%20Your%20Data%20Infrastructure:%20Accelerate%20Infrastructure%20Management%20with%20MCPs%20-%20VAST%20Data&source=https://www.vastdata.com/blog/data-infrastructure-accelerate-infrastructure-management-with-mcps)

[![Reddit](https://images.ctfassets.net/2f3meiv6rg5s/gFi1N7KiqWuKHzDMNYwhf/720a9e9cdbc4bba4bc3c554aff3bba18/blog-reddit.svg)](https://www.reddit.com/submit?url=https://www.vastdata.com/blog/data-infrastructure-accelerate-infrastructure-management-with-mcps&title=Talk%20to%20Your%20Data%20Infrastructure:%20Accelerate%20Infrastructure%20Management%20with%20MCPs%20-%20VAST%20Data)

[![Email](https://images.ctfassets.net/2f3meiv6rg5s/30LFr1HT6NynCevNDxKd06/9f76a25c5fb820cf82f56cb2f6fe44a2/blog-email.svg)](mailto:?subject=Talk%20to%20Your%20Data%20Infrastructure:%20Accelerate%20Infrastructure%20Management%20with%20MCPs%20-%20VAST%20Data&body=Talk%20to%20Your%20Data%20Infrastructure:%20Accelerate%20Infrastructure%20Management%20with%20MCPs%20-%20VAST%20Data%0D%0Ahttps://www.vastdata.com/blog/data-infrastructure-accelerate-infrastructure-management-with-mcps)

![Copy Link](https://images.ctfassets.net/2f3meiv6rg5s/2KGF0XrDXSq3x2jDAgneCX/b2ccf23de3c4ccc5a9fb4cc073d7a46a/blog-link.svg)

Imagine a VAST administrator managing multiple clusters across the organization. It's late on a Friday, and the team lead asks, "Can you tell me which views are using the most capacity across all clusters?"

Currently, we need to:

1. Navigate the UI across clusters, filters and collect the information and/or run command line interface (CLI) commands

2. Parse JSON outputs

3. Aggregate the data in a spreadsheet

4. Create a report


But what if you could just prompt your code editor **:** "For all tenants across all clusters, show me the top 10 views with the most used capacity."

And what if that job was done in seconds?

This isn't science fiction; it's the [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) in action, and specifically, how the VAST Admin MCP streamlines VAST cluster administration from mouse clicks and CLI complexity to conversational simplicity.

#### Why Data Admins Need Modern Infrastructure Tools

VAST Data's [disaggregated shared-everything](https://www.vastdata.com/platform/how-it-works) (DASE) architecture delivers incredible performance and scale, but with exabyte scale brings management overhead.  The [VAST AI OS](https://www.vastdata.com/platform/ai-os), the foundation for AI inference at scale, is driving the adoption of modern infrastructure tools.

#### The Challenge:

- Multi-cluster management: Organizations run dozens of VAST clusters

- Tenant isolation: Each tenant has its own logical objects like views, quotas, and policies

- Performance monitoring: Tracking IOPS, bandwidth, and capacity across hundreds of objects

- Compliance & security: Ensuring snapshots, replication, and access policies are correctly configured


Administrators navigate GUIs and build scripts to handle complex REST API calls. Let’s consider an alternative approach using natural language.

### Enter VAST Admin MCP

The [VAST Admin MCP](https://github.com/vast-data/vast-admin-mcp) is an open-source MCP server for secure access to VAST Data clusters. It supports both **cluster** and **tenant admins**, with granular control over write operations. Note the VAST Admin MCP by default runs in read-only mode to ensure write operations are disabled. Let’s go over some [use cases](https://github.com/vast-data/vast-admin-mcp):

**1\. Cluster Discovery and Monitoring**

plaintext

Copy

```
"Identify any critical alerts on all clusters that were not acknowledged"
```

**2\. Capacity Analysis**

plaintext

Copy

```
"Compare views with path '/' across all clusters, showing capacity information"
```

**3\. Performance Insights**

plaintext

Copy

```
"Create Bandwidth and IOPS graph for cluster1 over the last hour"
```

**4\. Multi-Step Operations** (Yes, AI can chain operations!)

plaintext

Copy

```
"Get performance metrics for cluster1, then get metrics for all cnodes, and finally get metrics for top 3 views. Show me a summary of IOPS and bandwidth for each object type."
```

### VAST Admin MCP Quickstart

You can setup the MCP with Python or Docker to add the MCP to any coding agent (Cursor, Claude Code, VSCode, Gemini, Windsurf):

##### Option 1: Python

bash

Copy

```
    # Install pip install vast-admin-mcp
    pip install vast-admin-mcp

    # Configure VAST cluster connection vast-admin-mcp setup
    vast-admin-mcp setup

    # Configure your AI assistant (Cursor, Claude, VSCode, etc.) vast-admin-mcp mcpsetup cursor
    vast-admin-mcp mcpsetup cursor
```

##### Option 2: Docker

bash

Copy

```
    # Build image (or pull from dockerhub)
    ./build-docker.sh

    # Run setup
    ./vast-admin-mcp-docker.sh setup

    # Configure AI assitant
    ./vast-admin-mcp-docker.sh mcpsetup cursor
```

That's it! Your AI assistant can access VAST infrastructure. Get started with a simple query: "List all VAST clusters".

#### Real-World Example: Capacity Planning through Natural Language

Let's walk through a scenario to illustrate conversational storage management.

#### Scenario: Quarterly Capacity Review

The CFO wants a report on storage utilization across all tenants before the next budget cycle. Let’s go over how to report storage utilization using the VAST Admin MCP:

**Explore tenants across clusters:**

![Talk to Your Data Infrastructure: Accelerate Infrastructure Management with MCPs ](https://images.ctfassets.net/2f3meiv6rg5s/dOnNs4o4AlpIS2wQAXzy0/f88a6dea68f7bfbd3085a208d038d1fc/data-infrastructure-accelerate-infrastructure-management-with-mcps-1.webp?w=2580&fm=png&q=80)

**List views with used capacity:**

![Talk to Your Data Infrastructure: Accelerate Infrastructure Management with MCPs](https://images.ctfassets.net/2f3meiv6rg5s/52k3EqGfaXpavYCZjO9mN9/517cb4e9a08ffa521b22128872b17990/data-infrastructure-accelerate-infrastructure-management-with-mcps-2.webp?w=2580&fm=png&q=80)

**Create reports:**

![Talk to Your Data Infrastructure: Accelerate Infrastructure Management with MCPs](https://images.ctfassets.net/2f3meiv6rg5s/7leItt8YDrjjkdv0TyTgch/31b5aa6a0ce3f1f90a654b46c8002c71/data-infrastructure-accelerate-infrastructure-management-with-mcps-3.webp?w=2580&fm=png&q=80)

**Generate graphs:**

![Talk to Your Data Infrastructure: Accelerate Infrastructure Management with MCPs](https://images.ctfassets.net/2f3meiv6rg5s/4FktlmIzdcwLxQKPtvgOza/58e12a654e490199be1293e6ca37eac5/data-infrastructure-accelerate-infrastructure-management-with-mcps-4.webp?w=2580&fm=png&q=80)

Data is synthesized across multiple API calls, generates graphs, and creates a formatted report via conversational prompts.

#### Beyond Monitoring: Data Infrastructure Write Operations

In read-write mode, VAST Admin MCP becomes an automation tool. Note that read-write mode requires explicit activation and is protected by API whitelist so only approved operations are allowed.

Let’s explore how to perform cluster modifications:

##### Snapshot Management

plaintext

Copy

```
"Create a snapshot named 'backup-2024-01-15' for view path /data/app1 on cluster1, tenant1 and keep it for 24h"

"Create an indestructible snapshot named restore-point_<view name> for all vmware views on cluster1"
```

##### View Provisioning

plaintext

Copy

```
"Create a new NFS view on cluster1 with path /data/newview in tenant1"

"Create a view on cluster1 with path /shared/data in tenant1 that supports both NFS and S3 protocols"

"Create 3 new views for vmware based on template"
```

##### Quota Management

plaintext

Copy

```
"Set a hard quota of 10TB for view path /data/app1 on cluster1, tenant1"
```

##### Clone Operations

plaintext

Copy

```
"Create a clone from snapshot 'backup-2024-01-15' of view /data/app1. The clone should be at path /data/app1-clone in tenant1 on cluster1"

"Refresh a clone from most recent snapshot of view /data/app1 at path /data/app1-clone in tenant1 on cluster1"
```

#### How VAST Admin MCP Works

Let’s go over what's happening under the hood:

![How VAST Admin MCP Works](https://images.ctfassets.net/2f3meiv6rg5s/1lhwVtfbqWtmV892f7LBB1/30f1f3a1e654df2fe45abd79a6e51817/data-infrastructure-accelerate-infrastructure-management-with-mcps-5.webp?w=2580&fm=png&q=80)

##### Components

1. **MCP Server**: Exposes over [30 tools](https://github.com/vast-data/vast-admin-mcp/blob/main/src/vast_admin_mcp/functions.py) (i.e. pre-defined functions) for AI assistants to call

2. **Dynamic functions**: [YAML-based templates](https://github.com/vast-data/vast-admin-mcp/tree/main?tab=readme-ov-file#yaml-template-structure) for low-code modification of tool calls

3. **vastpy SDK**: Leverages [VAST Data Python SDK](https://github.com/vast-data/vastpy) for API calls

4. **Docker**: Container for ease of deployment and environment isolation


##### Features

- **Context Awareness**: AI models understand the relationship between logical objects like clusters, tenants, views, and quotas

- **Multi-step Reasoning**: Chain tool calls (e.g., "find views > 1TB, then get their performance metrics")

- **Natural Language Filters**: Use of normal language like "views prefixed with 'prod'" instead of using regex patterns

- **Automatic Formatting**: Modify responses to be human-readable format (i.e. table, list)


##### Security

Let’s go over the built-in protections:

1. **API Whitelisting**: Only approved [REST API endpoints and HTTP methods](https://github.com/vast-data/vast-admin-mcp/blob/main/mcp_list_cmds_template.yaml#L26) are accessible

2. **Read-Only by Default**: Write operations require use of explicit use of --read-write flag

3. **Encrypted Credentials**: Passwords stored in system keyring or file-based encryption

4. **Audit Trail**: All operations logged locally for compliance

5. **Tenant Isolation**: Tenant admins can only access assigned tenant

6. **MCP in STDIO Mode**: MCP runs on the same host as the AI assistance, so no network exposure


As you get started with using the MCP, consider the following best practices:

- Run the MCP in docker to ensure it is isolated from other environments

- Start with read-only mode for exploration and monitoring and only attempt \`read-write mode\` for changes that you can verify manually, preferably minor changes to start

- Review the YAML template and consider ways to customize operations for specific scenarios


#### Looking Ahead

MCPs represent a fundamental shift in how we interact with and manage infrastructure. As highlighted in VAST's vision, we're creating the AI Operating System powering AI inference at scale **.** The combination of VAST's disaggregated architecture, rich API surface, and MCP's natural language interface unlocks opportunities for automation. Whether you manage two or two hundred clusters, whether you use Python or are just starting with automation, VAST Admin MCP makes your infrastructure accessible, understandable, and manageable.

We welcome questions, feedback, and feature requests. Join the conversation on [Cosmos](https://community.vastdata.com/).

_Build and ship on the VAST AI Operating System at_ [VAST Forward](https://www.vastdata.com/vast-forward) _, February 24–26, 2026 in Salt Lake City. Go deep with VAST engineers and power users in architecture-level sessions, hands-on labs, and real-world implementations of large-scale AI, data, and GPU-driven workloads. Leave with practical patterns, tooling knowledge, and certifications you can put into production immediately._ [Register here to join](https://vastforward.vastdata.com/vastforward-2026?utm_medium=WebDirect&utm_source=openai&utm_term=Partner-Marketing&utm_campaign=2025-02-25-WW-Webinar-AI-Factory-With-Deloitte)_._

**Additional reading:**

- [vast-admin-mcp - GitHub](https://github.com/vast-data/vast-admin-mcp)

- [Model Context Protocol Specification](https://modelcontextprotocol.io/)

- [VAST Data Platform Documentation](https://support.vastdata.com/)

- [vastpy - VAST Data Python SDK](https://pypi.org/project/vastpy/)


#### More from this topic

[![Running Lightning-Fast Functions and AI Workloads on Kubernetes](https://images.ctfassets.net/2f3meiv6rg5s/1tLUFJES2St76lU90recX1/b0daab0ad931f55348cd16631307957d/kubernetes-ai-agents-pipelines.webp?w=3200&fm=png)\\
\\
Running Lightning-Fast Functions and AI Workloads on Kubernetes\\
\\
The VAST Data AI OS breaks down silos while delivering an unparalleled combination of scalability and performance AI agents, RL, and more.](https://www.vastdata.com/blog/kubernetes-ai-agents-pipelines)

[![When the City Thinks: Real-Time Video Agents with VAST and NVIDIA Cosmos Reason 2](https://images.ctfassets.net/2f3meiv6rg5s/6Mzeenwilq7LyHv310J6QC/e1cd80860df73159e3b3767689103b60/more-inference-less-infrastructure-vast-nvidia.webp?w=3200&fm=png)\\
\\
When the City Thinks: Real-Time Video Agents with VAST and NVIDIA Cosmos Reason 2\\
\\
Smart cities are no longer just about collecting petabytes of video footage—they are about understanding it and acting on it. VAST Data and NVIDIA can help.](https://www.vastdata.com/blog/vast-nvidia-cosmos-reason-smart-cities)

[![This Is the Moment VAST Certification Counts](https://images.ctfassets.net/2f3meiv6rg5s/oaa6ovq9iFfXj1B9Fq7Mo/651897106c0b2136c87af4b8c576424f/this-is-the-moment-vast-certification-counts.webp?w=3200&fm=png)\\
\\
This Is the Moment VAST Certification Counts\\
\\
Move beyond recall to mastery. Discover why the new VAST Certification focuses on rigorous, real-world competence for the modern disaggregated infrastructure.](https://www.vastdata.com/blog/this-is-the-moment-vast-certification-counts)

Learn what VAST can do for you

Sign up for our newsletter and learn more about VAST or request a [demo](https://www.vastdata.com/demo) and see for yourself.

Country \*United StatesAfghanistanAlbaniaAlgeriaAndorraAngolaAnguillaAntigua & BarbudaArgentinaArmeniaArubaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBosnia & HerzegovinaBotswanaBrazilBritish Virgin IslandsBruneiBulgariaBurkina FasoBurundiCambodiaCameroonCanadaCape VerdeCayman IslandsChadChileChinaColombiaCongoCook IslandsCosta RicaCote D IvoireCroatiaCruise ShipCubaCyprusCzech RepublicDenmarkDjiboutiDominicaDominican RepublicEcuadorEgyptEl SalvadorEquatorial GuineaEstoniaEthiopiaFalkland IslandsFaroe IslandsFijiFinlandFranceFrench PolynesiaFrench West IndiesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuamGuatemalaGuernseyGuineaGuinea BissauGuyanaHaitiHondurasHong KongHungaryIcelandIndiaIndonesiaIraqIrelandIsle of ManIsraelItalyJamaicaJapanJerseyJordanKazakhstanKenyaKuwaitKyrgyz RepublicLaosLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgMacauMacedoniaMadagascarMalawiMalaysiaMaldivesMaliMaltaMauritaniaMauritiusMexicoMoldovaMonacoMongoliaMontenegroMontserratMoroccoMozambiqueNamibiaNepalNetherlandsNetherlands AntillesNew CaledoniaNew ZealandNicaraguaNigerNigeriaNorwayOmanPakistanPalestinePanamaPapua New GuineaParaguayPeruPhilippinesPolandPortugalPuerto RicoQatarReunionRomaniaRwandaSaint Pierre & MiquelonSamoaSan MarinoSatelliteSaudi ArabiaSenegalSerbiaSeychellesSierra LeoneSingaporeSlovakiaSloveniaSouth AfricaSouth KoreaSpainSri LankaSt Kitts & NevisSt LuciaSt VincentSt. LuciaSudanSurinameSwazilandSwedenSwitzerlandTaiwanTajikistanTanzaniaThailandTimor L'EsteTogoTongaTrinidad & TobagoTunisiaTurkeyTurkmenistanTurks & CaicosUgandaUkraineUnited Arab EmiratesUnited KingdomUruguayUzbekistanVenezuelaVietnamVirgin Islands (US)YemenZambiaZimbabwe

How much Data Capacity do you have today? \*Less than 1 Petabyte1-10 Petabytes1-100 Petabytes100+ Petabytes

Want to receive info about products and services from VAST? You may unsubscribe from these communications at anytime.

Submit

By proceeding you agree to the [VAST Data Privacy Policy](https://www.vastdata.com/legal/privacy-policy).

\\* Required field.