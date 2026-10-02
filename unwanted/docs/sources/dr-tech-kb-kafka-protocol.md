> ## Documentation Index
>
> Fetch the complete documentation index at: [https://kb.vastdata.com/llms.txt](https://kb.vastdata.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

# Kafka Protocol Support

- Updated on Feb 10, 2026
- Published on Jan 30, 2026

- 1 minute(s) read
- Focus
- Listen

Follow

Copy pageCopy as Markdown for LLMsView as MarkdownView the page as plain text

Open in ChatGPTAsk ChatGPT about this pageOpen in ClaudeAsk Claude about this page

Article summary[Prev](https://kb.vastdata.com/documentation/docs/publishing-events-to-vast-event-broker-1 "Publishing Events to VAST Event Broker")[Next](https://kb.vastdata.com/documentation/docs/configuring-vast-event-broker-1 "Configuring VAST Event Broker")

The VAST implementation of the Kafka protocol supports a basic subset of the Kafka APIs to allow clients to publish and consume events from the VAST Event Broker.

- VAST Event Broker supports:

  - Producer API

  - Consumer API

  - Consumer groups

  - Database queries on topics

  - Admin API:

    - Create topics

    - Get topic configuration ( ​`describeConfigs`​​ )

    - Update topic configuration (​​`alterConfigs`​​)

    - Delete topics

    - Delete consumer groups
  - Topic compaction

  - SSL

The following Kafka capabilities are not supported:

- Over-the-wire compression of messages. Note that VAST compression of data is supported.

- Automatic creation of topics

- Transactions


The following limitations apply:

- Producer API:

  - Messages are limited to 1MB.

  - In the event record, the key is limited to 126KB and the value is limited to 126KB.

  - Idempotent producing is not supported.

  - Automatic creation of topics is not supported.
- Consumer API:

  - No more than 256 consumer groups per view (broker)

  - The following is not supported:

    - Consumer group stickiness parameters (such as ​group.instance.id​​)

    - READ UNCOMMITTED isolation level

    - Cooperative rebalancing

    - Client rack awareness

    - Fetch sessions (only full fetch will be applied), delayed fetch parameters

    - Seek by time
- Only one virtual IP pool can be associated with a Kafka-enabled view.

- The amount of VAST Event Broker views that you can create on a VAST cluster, is limited by the maximum number of views supported by the cluster and by the maximum number of virtual IP pools (since each broker view requires a dedicated virtual IP pool). See _​VAST Cluster Scale Guidelines_ ​​ for details.

- The amount of event topics that you can create on a VAST cluster, is limited by the maximum number of tables per VAST Database table (see _​VAST Cluster Scale Guidelines_ ​​) and the overall amount of event topic partitions.

- A topic can have up to 20,000 partitions. The number of partitions in a topic cannot be changed after the topic has been created. Up to 200,000 partitions are supported per VAST Event Broker view.

- Event queries based on the topic partition are not supported.

- When listing consumer groups, the response is limited to 256 groups per Kafka-enabled view.

- VAST replication of consumer groups is not supported.

- Event publishing and consuming operations, as well as topic management operations are not subject to VAST Protocol Auditing or Quality of Service (QoS).


## Supported Kafka Clients

VAST Cluster supports Confluent Kafka Python client 2.4 - 2.8. The aiokafka client is not supported.

Was this article helpful? (Provide Feedback)

Yes  No

Previous article

Publishing Events to VAST Event Broker

Next article

Configuring VAST Event Broker

Related articles

- [Kafka Protocol Support](https://kb.vastdata.com/documentation/docs/kafka-protocol-support-1)



VAST AI OS > Version 5.4 > VAST Cluster 5.4 Tenant Administrator's Guide > Managing Data > Event Publishing > Publishing Events to VAST Event Broker

- [Publishing Events to VAST Event Broker](https://kb.vastdata.com/documentation/docs/publishing-events-to-vast-event-broker-55-1)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 Tenant Administrator’s Guide > Managing Data > Event Publishing

- [Publishing Events to VAST Event Broker](https://kb.vastdata.com/documentation/docs/publishing-events-to-vast-event-broker-55)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 Administrator’s Guide > Managing Data > Event Publishing