> ## Documentation Index
>
> Fetch the complete documentation index at: [https://kb.vastdata.com/llms.txt](https://kb.vastdata.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

# VAST Cluster 5.5 DataEngine Runtime SDK Developer’s Guide

Follow

- 9 Articles

[Prev](https://kb.vastdata.com/documentation/docs/viewing-logs-and-traces-55 "Viewing Logs and Traces")[Next](https://kb.vastdata.com/documentation/docs/about-this-guide-dataengine-runtime-sdk-55 "About this Guide - DataEngine Runtime SDK")

[About this Guide - DataEngine Runtime SDK](https://kb.vastdata.com/documentation/docs/about-this-guide-dataengine-runtime-sdk-55)

- Published on Aug 5, 2026

Use this guide to help you implement VAST DataEngine functions using the VAST DataEngine Runtime SDK, as described in step 3 in Prepare the Function Image in the Container Registry in the VAST Cluster 5.5 VAST DataEngine User Guide. This gu...

[Overview](https://kb.vastdata.com/documentation/docs/overview-dataengine-runtime-sdk-55)

- Updated on Aug 6, 2026
- Published on Aug 5, 2026

The VAST DataEngine Runtime relays events, context information, and responses between VAST DataEngine and your function. The VAST DataEngine Runtime SDK is a python SDK that handles event processing as single events or batches, conditional r...

[Getting Started](https://kb.vastdata.com/documentation/docs/getting-started-dataengine-runtime-sdk-55)

- Updated on Aug 6, 2026
- Published on Aug 5, 2026

Prerequisite Steps Application user for a DataEngine instance deployed on a VAST Cluster tenant. Deploying DataEngine and provisioning users requires cluster admin for the VAST cluster or a tenant admin user for the spe...

[Initializing the Runtime](https://kb.vastdata.com/documentation/docs/initializing-the-runtime-55)

- Published on Aug 5, 2026

init() def init() The init() function: Is invoked once when the container pod that deploys the function starts. Enables you to pass custom attributes to be accessible in the event handler path. Parameters ctx ...

[Event Handling](https://kb.vastdata.com/documentation/docs/event-handling-55)

- Published on Aug 5, 2026

handler() The handler function is invoked whenever the function receives an event or a batch of events. Events can be passed to each function as single or batched events, depending whether batching is configured in the function deployme...

[Accessing Secrets and Environment Variables](https://kb.vastdata.com/documentation/docs/accessing-secrets-and-environment-variables-55)

- Updated on Aug 7, 2026
- Published on Aug 5, 2026

Accessing Secrets Secrets can be attached to a pipeline or a function deployment as described in the DataEngine User Guide . DataEngine makes secrets available to functions at runtime via ctx.secrets . The ctx class can access s...

[Collecting Custom Metrics](https://kb.vastdata.com/documentation/docs/collecting-custom-metrics-55)

- Published on Aug 5, 2026

DataEngine supports collection of metrics from data processing functions using OpenTelemetry through the DataEngine SDK. The SDK wraps an OpenTelemetry metrics handler via four methods, supporting four metrics instruments: In the DataEngi...

[Logs and Traces](https://kb.vastdata.com/documentation/docs/logs-and-traces-55)

- Published on Aug 5, 2026

Generating Logs By default, the runtime captures stdout (such as print() statements) and logs from standard Python loggers, automatically transmitting them via OpenTelemetry to VAST DataEngine. The runtime also provides an embedded...

[Class Reference](https://kb.vastdata.com/documentation/docs/class-reference-55)

- Updated on Aug 6, 2026
- Published on Aug 5, 2026

ctx Class The ctx class passes execution context metadata, telemetry interfaces, secrets, and metrics instruments to your function handler. The ctx object is passed as an argument to both the event initializer function ( init(ctx...