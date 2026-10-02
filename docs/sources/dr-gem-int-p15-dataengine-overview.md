> ## Documentation Index
>
> Fetch the complete documentation index at: [https://kb.vastdata.com/llms.txt](https://kb.vastdata.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

# Overview of VAST DataEngine

- Updated on Jan 30, 2026
- Published on Jan 27, 2026

- 1 minute(s) read
- Focus
- Listen

Follow

Copy pageCopy as Markdown for LLMsView as MarkdownView the page as plain text

Open in ChatGPTAsk ChatGPT about this pageOpen in ClaudeAsk Claude about this page

Article summary[Prev](https://kb.vastdata.com/documentation/docs/vast-dataengine-1 "VAST DataEngine")[Next](https://kb.vastdata.com/documentation/docs/enabling-data-engine-on-a-vast-cluster-tenant-1 "Enabling DataEngine on a VAST Cluster Tenant")

VAST DataEngine is the VAST compute orchestration framework. The framework enables users to write, deploy and manage execution pipelines against scheduled or event driven triggers. VAST DataEngine runs on VAST Cluster and dynamically provisions infrastructure and runtime resources according to demand. VAST DataEngine frees users from the need to manage and handle infrastructure scaling and availability or worry about performance.

VAST DataEngine features a web-based graphic user interface, a command line interface and a REST API service for configuring and managing triggers, functions and pipelines and for scheduling, running and monitoring pipelines.

VAST DataEngine features a telemetries service, providing observability over user executed pipelines and functions. The telemetries service collects logs, and traces of pipelines and enables users to query them.

VAST DataEngine can support limitless scope of use cases and a limitless scope of personas who might interact with the framework.

VAST DataEngine utilizes an event broker to stream events into functions. You can choose to use a third party event broker or the VAST Event Broker.

VAST DataEngine is enabled per tenant and can be enabled and configured by a _Cluster Admin_ user or a _Tenant Admin_ user. A user type called _application user_ can be provisioned to non administrative users in order to grant them access to VAST DataEngine.

Deployment of VAST DataEngine involves connecting a VAST Cluster tenant to two external services: a container registry that stores images of functions to be deployed, and a Kubernetes cluster to consume the event broker events and execute the user functions with the above events.

VAST DataEngine supports functions written in Python3. Triggers can be set on any file name suffix and prefix and functions can be written to handle any type of file format. You can also build and deploy HTTP server images.

Was this article helpful? (Provide Feedback)

Yes  No

Previous article

Managing Permissions for Accessing VAST Tabular Databases

Next article

Enabling DataEngine on a VAST Cluster Tenant

Related articles

- [Overview of VAST DataEngine](https://kb.vastdata.com/documentation/docs/overview-of-vast-dataengine-55-1)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 Administrator’s Guide > VAST DataEngine

- [Overview of VAST DataEngine](https://kb.vastdata.com/documentation/docs/overview-of-vast-dataengine)



VAST AI OS > Version 5.4 > VAST Cluster 5.4 Tenant Administrator's Guide > VAST DataEngine

- [Overview of VAST DataEngine](https://kb.vastdata.com/documentation/docs/overview-of-vast-dataengine-55-2)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 Tenant Administrator’s Guide > VAST DataEngine