> ## Documentation Index
>
> Fetch the complete documentation index at: [https://kb.vastdata.com/llms.txt](https://kb.vastdata.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

# Event Handling

- Published on Aug 5, 2026

- 7 minute(s) read
- Focus
- Listen

Follow

Copy pageCopy as Markdown for LLMsView as MarkdownView the page as plain text

Open in ChatGPTAsk ChatGPT about this pageOpen in ClaudeAsk Claude about this page

Article summary[Prev](https://kb.vastdata.com/documentation/docs/initializing-the-runtime-55 "Initializing the Runtime")[Next](https://kb.vastdata.com/documentation/docs/accessing-secrets-and-environment-variables-55 "Accessing Secrets and Environment Variables")

## handler()

The handler function is invoked whenever the function receives an event or a batch of events. Events can be passed to each function as single or batched events, depending whether batching is configured in the function deployment configured in the pipeline.

The runtime supports asynchronous event handling, which is recommended for improved throughput and performance. You can define your event handler as `async def`.

For processing single events:

Plain text

```plaintext
async def handler(ctx, event)
```

Plain text

Copy

For processing a batch of events:

Plain text

```plaintext
async def handler(ctx, events_list)
```

Plain text

Copy

### Parameters

- `ctx` (required). Provides access to the [ctx](https://kb.vastdata.com/documentation/docs/class-reference-55#ctx-class "ctx Class") object. The ctx object provides information from the function invocation. This includes logs, traces, pipeline and function secrets, and custom attributes initialized by the `init()` function.

- `event`. Provides access to the event object. The event object provides access to event telemetry and properties. The event argument accepts an object of class [VastEvent](https://kb.vastdata.com/documentation/docs/class-reference-55#vastevent-class "VastEvent Class") or one of its subclasses: [ElementTriggerVastEvent](https://kb.vastdata.com/documentation/docs/class-reference-55#elementtriggervastevent-class "ElementTriggerVastEvent Class"), [FunctionVastEvent](https://kb.vastdata.com/documentation/docs/class-reference-55#functionvastevent-class "FunctionVastEvent Class") and [ScheduleVastEvent](https://kb.vastdata.com/documentation/docs/class-reference-55#schedulevastevent-class "ScheduleVastEvent Class"). You can also use it without an object type.

- `events_list`. Provides access to the `VastEventList` batch container holding incoming batched events.


### Return Value

The return value can be either of:

- `VastEvent` object, which will be forwarded to the next functions in the pipeline for processing, or

- Python `dict` or `str`, which will automatically be wrapped by runtime as VastEvent and forwarded.


## Import Event Classes

Import the class and subclasses into your code from _vast.dataengine.sdk_.

For example:

Plain text

```plaintext
from vast.dataengine.sdk import Context, VastEventList, event_batching_handler
```

Plain text

Copy

## Using Event Trigger Type-Specific Helpers

You can cast event to a specific subclass to access properties that are specific to the event type:

- `as_element_event()`. Checks the event is an element type event ( [ElementTriggerVastEvent](https://kb.vastdata.com/documentation/docs/class-reference-55 "Class Reference")). Otherwise, an error is raised.

- `as_function_event()`. Checks the event is a function type event ( [FunctionVastEvent](https://kb.vastdata.com/documentation/docs/class-reference-55#functionvastevent-class "FunctionVastEvent Class")). Otherwise, an error is raised.

- `as_schedule_event()`. Checks the event is a schedule type event ( [ScheduleVastEvent](https://kb.vastdata.com/documentation/docs/class-reference-55#schedulevastevent-class "ScheduleVastEvent Class")). Otherwise, an error is raised.


### Example

Plain text

```plaintext
 try:
        schedule_event = event.as_schedule_event()
        ctx.logger.info(f"Schedule cron: {schedule_event.cron_schedule}")
        ctx.logger.info(f"Schedule timer elapsed: {schedule_event.timer_elapsed_timestamp}")
    except TypeError:
            ctx.logger.info("validate-event: expected schedule event")
```

Plain text

Copy

## Batch Event Processing

The following abstractions help you implement batch event processing in a function:

- `@event_batching_handler`. A decorator from vast.dataengine.sdk that signals to the runtime that this handler expects a batch container of events (VastEventList) rather than a single event object.

- `VastEventList`: A specialized SDK container type representing the accumulated list of events passed to the function. Pass this as a second argument to your handle function. This implements a native batch container to implement standard Python sequence behaviors. `@event_batching_handler` is required when the handler takes `VastEventList`.

- `event.get_data()`: A helper method on individual event objects within the batch to retrieve the underlying payload.


To implement batch event processing:

- Import `Context`, `VastEventList`, and the `@event_batching_handler` decorator from `vast.dataengine.sdk`.

- Place `@event_batching_handler` above your handler function. This informs the DataEngine runtime SDK that the second argument of the handler function will be a VastEventList batch container rather than a single event object.

- In your handler, for the second positional argument, use `events_list: VastEventList` – the batch container holding the incoming events.

- Loop through `events_list` and invoke `.get_data()` on each event object to retrieve its payload dictionary.

- Return a standard Python list containing the transformed event payloads. The return list length must equal the input batch size.


Example:

Plain text

```plaintext
from typing import List

#  Import the necessary classes and decorators from the DataEngine SDK:
from vast.dataengine.sdk import Context, VastEventList, event_batching_handler

# Initialize the DataEngine runtime when a function instance starts up.
def init(ctx: Context):
      # Use the SDK's context logger to write an informational log indicating the function instance has been initialized.
      ctx.logger.info("Initializing Bulk Event Processor...")

# Tell DataEngine that this function is configured to receive event batches.
@event_batching_handler
# Pass events_list as the second argument in the event handler, to accept batches of events wrapped in VastEventList. DataEngine accumulates events in batches according to batch size and batch timeout configured in function deployment.
def handler(ctx: Context, events_list: VastEventList):
    ctx.logger.info(f"Processing batch of {len(events_list)} events in '{ctx.function_name}'.")

    # Extract data dictionaries from the batch wrapper
    payloads = [event.get_data() for event in events_list]

    # Execute bulk operation (e.g., 1 database request instead of N requests)
    perform_bulk_operation(payloads)

    # Mutate payloads if necessary and return the list
    for payload in payloads:
        payload["processed_by"] = ctx.function_name

    # Return list of processed payloads to send downstream
    return payloads

def perform_bulk_operation(records: List[dict]):
    """
    Placeholder helper function for bulk DB insertions or batch API calls.
    Replace with actual database or HTTP client call.
    """
    # e.g., db.execute_many("INSERT INTO events VALUES (...)", records)
    pass
```

Plain text

Copy

## Conditional Function Routing

To implement conditional function routing, use the `set_trigger_labels()` setter method to attach labels to event objects. In your DataEngine pipelines, if you attach a label to a connector that routes the function to another function, only events that have a label matching the configured trigger label will invoke the function.

> Note
>
> Passing an empty dictionary to `event.set_trigger_labels({})` is not allowed and raises a `ValueError`. To intentionally prevent an event from routing downstream, attach a dummy label that does not match any configured connector (e.g., `{"noRoute": "skip"}`).

For example, suppose you have an e-commerce platform processing customer orders. When a new order occurs, the incoming order is received as an event. Depending on what is inside the order, the pipeline needs to route the data to different specialized downstream function. You might have all events routed to an initial sorting function which routes the orders to different functions downstream.

You might use conditional function routing to implement this in your pipeline. To do this, you would write your first function, function A, to inspect the payload fields, construct routing labels and attach them to the events before returning them to the pipeline. In the pipeline, you connect the trigger that produces the events to Function A, which would look something like this:

Plain text

```plaintext
import json
from vast.dataengine.sdk import VastEvent

def init(ctx):
    pass

def handler(ctx, event: VastEvent):
    data = event.get_data()
    message_str = data["message"]

    # 1. Parse the incoming raw JSON message into a structured dictionary
    payload = json.loads(message_str)

    # 2. Create an empty dictionary to hold trigger labels
    labels = {}

    # 3. Apply business logic to build labels from raw payload fields
    customer_tier = payload.get("customer", {}).get("tier")
    if customer_tier == "VIP":
        labels["tier"] = "vip_customer"

    risk_score = payload.get("payment", {}).get("risk_score", 0)
    if risk_score > 80:
        labels["alert_type"] = "security_flag"

    order_amount = payload.get("payment", {}).get("amount", 0)
    if order_amount >= 1000:
        labels["value_tier"] = "high_value"

    # 4. Apply the extracted/computed labels to the event
    if labels:
        ctx.logger.info(f"Applying generated trigger labels: {labels}")
        event.set_trigger_labels(labels)
    else:
        # Handle non-matching routing (must use non-empty dict)
        event.set_trigger_labels({"noRoute": "skip"})

    # 5. Return the structured dict payload for downstream pipeline steps
    return payload
```

Plain text

Copy

You might then prepare function B to process events labelled vip\_customer, function C to process events labelled security\_flag, and function D to process events labelled high\_value.

On the DataEngine platform, when building the pipeline, you would route function A to functions B, C and D, and apply event trigger labels on the connectors from function A to each of the other functions:

- On the route from A to B, label: key=`tier`, value=`vip_customer`. Events returned by function A will be routed to function B only if they are labeled _tier=vip\_customer_.

- On the route from A to C, label: key=`alert_type`, value=`security_flag`. Events returned by function A will be routed to function C only if they are labeled _alert\_type=security\_flag_.

- On the route from A to D: label: key=`value_tier`, value=`high_value` Events returned by function A will be routed to function D only if they are labeled _value\_tier=high\_value_.


### Multiple Label Logic

When multiple key-value pairs are configured on a routing link between functions, all labels must match the event in order for it to be routed to the linked function.

### Label Merging

Successive calls to `event.set_trigger_labels()` on the same event object merge new key-value pairs into the existing label set rather than overwriting the whole dictionary. Existing keys are updated and new keys are added.This behavior is essential for fan-out routing, allowing different conditional checks in your function to attach distinct routing labels incrementally without clearing previously set labels.

Plain text

```plaintext
# Step 1: Attach initial routing label based on user tier
event.set_trigger_labels({"tier": "vip"})

# Step 2: Attach an additional label based on region
# This merges with step 1 rather than replacing it
event.set_trigger_labels({"region": "us-east"})

# Final active label set on event:
# {"tier": "vip", "region": "us-east"}
# Downstream connectors matching either "tier=vip" OR "region=us-east" will trigger.
```

Plain text

Copy

### Topology Enforcement and Hop-by-Hop Routing Rules

Conditional routing operates strictly hop-by-hop along declared pipeline links:

- Immediate connections only: Trigger labels attached via `event.set_trigger_labels()` are evaluated only against connectors directly originating from the current function.

- No skip-ahead routing: You cannot route an event to a distant function further down the pipeline unless a direct link exists between the current function and that target in the pipeline topology.

- Inspecting available routes: Use `ctx.pipeline_triggers_map` to programmatically inspect the direct downstream connections available from the active function.


Was this article helpful? (Provide Feedback)

Yes  No

Previous article

Initializing the Runtime

Next article

Accessing Secrets and Environment Variables

Related articles

- [Implementing a VAST DataEngine Pipeline](https://kb.vastdata.com/documentation/docs/implementing-a-vast-dataengine-pipeline-55)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 DataEngine User Guide

- [Class Reference](https://kb.vastdata.com/documentation/docs/class-reference-55)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 DataEngine Runtime SDK Developer’s Guide

- [Logs and Traces](https://kb.vastdata.com/documentation/docs/logs-and-traces-55)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 DataEngine Runtime SDK Developer’s Guide