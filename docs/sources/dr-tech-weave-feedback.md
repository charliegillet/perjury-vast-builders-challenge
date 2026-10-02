> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.coreweave.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback#content-area)

Evaluating LLM applications requires tooling to collect and analyze feedback. W&B Weave provides an integrated feedback system that lets you provide Call feedback directly through the UI or programmatically through the SDK. Weave supports several feedback types, including emoji reactions, textual comments, and structured data, so your team can:

- Build evaluation datasets for performance monitoring.
- Identify and resolve LLM content issues.
- Gather examples for advanced tasks like fine-tuning.

This guide is for developers and reviewers working with LLM applications in Weave. It covers how to use Weave’s feedback functionality in both the UI and SDK, query and manage feedback, and use human annotations for detailed evaluations.

- [Provide feedback in the UI](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback#provide-feedback-in-the-ui)
- [Provide feedback through the SDK](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback#provide-feedback-through-the-sdk)
- [Add human annotations](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback#add-human-annotations)

## [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#provide-feedback-in-the-ui)  Provide feedback in the UI

The following sections describe how to provide feedback in the Weights & Biases UI, either from the Call details panel or using the feedback icons.

### [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#use-the-call-details-panel)  Use the Call details panel

1. In the Weave project sidebar, navigate to **Traces**.
2. Find the row for the Call that you want to add feedback to.
3. Click the linked Trace name to open the trace tree and Call details panel.
4. In the Call details tab bar, select **Feedback**.
5. Add, view, or delete feedback:
   - _Add and view feedback using the icons_ located in the upper right corner of the Call details feedback view.
   - _View and delete feedback from the Call details feedback table._ Delete feedback by clicking the trashcan icon in the rightmost column of the appropriate feedback row.

![Feedback tab in Call details](https://mintcdn.com/coreweave-dbfa0e8d/3Dv_sw2eg8feUJlx/products/wandb/weave/_media/feedback_tab.png?fit=max&auto=format&n=3Dv_sw2eg8feUJlx&q=85&s=50b49b6e6e2614b182b1a33775754175)

### [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#use-the-feedback-icons)  Use the feedback icons

You can add or remove a reaction, and add a note using the icons that are located in both the Traces table and individual Call details panel.

- _Traces table_: Located in **Feedback** column in the appropriate row in the **Traces** table.
- _Call details panel_: Located in the upper right corner of each Call details panel.

To add a reaction:

1. Click the emoji icon.
2. Add a thumbs up, thumbs down, or click the **+** icon for more emojis.

To remove a reaction:

1. Hover over the emoji reaction you want to remove.
2. Click the reaction to remove it.

> You can also delete feedback from the [**Feedback** column on the Call details panel](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback#use-the-call-details-panel).

To add a comment:

1. Click the comment bubble icon.
2. In the text box, add your note. The maximum number of characters in a feedback note is 1024.
3. To save the note, press the **Enter** key. You can add more notes.

The maximum number of characters in a feedback note is 1024. If a note exceeds this limit, Weave doesn’t create it.

![Calls grid with feedback column](https://mintcdn.com/coreweave-dbfa0e8d/3Dv_sw2eg8feUJlx/products/wandb/weave/_media/feedback_calls.png?fit=max&auto=format&n=3Dv_sw2eg8feUJlx&q=85&s=ab4006b5d636f9e87db1edc7a80fd1ab)

## [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#provide-feedback-through-the-sdk)  Provide feedback through the SDK

Use the SDK when you want to automate feedback collection or integrate it into evaluation pipelines, rather than entering feedback by hand in the UI.You can find SDK usage examples for feedback in the UI under the **Use** tab in the Call details panel.You can use the Weave Python SDK to programmatically [add](https://docs.coreweave.com/products/wandb/weave/reference/python-sdk/trace/feedback#method-add), [remove](https://docs.coreweave.com/products/wandb/weave/reference/python-sdk/trace/feedback#method-purge), and [query feedback](https://docs.coreweave.com/products/wandb/weave/reference/python-sdk/trace/weave_client#method-get_feedback) on calls. The TypeScript SDK does not support feedback functionality.

### [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#query-a-project%E2%80%99s-feedback)  Query a project’s feedback

You can query the feedback for your Weave project using the SDK. The SDK supports the following feedback query operations:

- `client.get_feedback()`: Returns all feedback in a project.
- `client.get_feedback("[FEEDBACK-UUID]")`: Returns a specific feedback object specified by `[FEEDBACK-UUID]` as a collection.
- `client.get_feedback(reaction="[REACTION-TYPE]")`: Returns all feedback objects for a specific reaction type.

You can also get more information for each feedback object in `client.get_feedback()`:

- `id`: The feedback object ID.
- `created_at`: The creation time information for the feedback object.
- `feedback_type`: The type of feedback (reaction, note, custom).
- `payload`: The feedback payload.

- Python

- TypeScript


```
import weave
client = weave.init('intro-example')

# Get all feedback in a project
all_feedback = client.get_feedback()

# Fetch a specific feedback object by id.
# The API returns a collection, which is expected to contain at most one item.
one_feedback = client.get_feedback("[FEEDBACK-UUID]")[0]

# Find all feedback objects with a specific reaction. You can specify offset and limit.
thumbs_up = client.get_feedback(reaction="👍", limit=10)

# After retrieval, view the details of individual feedback objects.
for f in client.get_feedback():
    print(f.id)
    print(f.created_at)
    print(f.feedback_type)
    print(f.payload)
```

```
This feature is not available in TypeScript yet.
```

### [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#add-feedback-to-a-call)  Add feedback to a Call

You can add feedback to a Call using the Call’s UUID. To use the UUID to get a particular Call, [retrieve it during or after Call execution](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback#retrieve-the-call-uuid). The SDK supports the following operations for adding feedback to a Call:

- `call.feedback.add_reaction("[REACTION-TYPE]")`: Add one of the supported `[REACTION-TYPE]` values (emojis), such as 👍.
- `call.feedback.add_note("[NOTE]")`: Add a note.
- `call.feedback.add("[LABEL]", [OBJECT])`: Add a custom feedback `[OBJECT]` specified by `[LABEL]`.

The maximum number of characters in a feedback note is 1024. If a note exceeds this limit, Weave doesn’t create it.

- Python

- TypeScript


```
import weave
client = weave.init('intro-example')

call = client.get_call("[CALL-UUID]")

# Adding an emoji reaction
call.feedback.add_reaction("👍")

# Adding a note
call.feedback.add_note("this is a note")

# Adding custom key/value pairs.
# The first argument is a user-defined "type" string.
# Feedback must be JSON serializable and less than 1 KB when serialized.
call.feedback.add("correctness", { "value": 5 })
```

```
This feature is not available in TypeScript yet.
```

#### [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#retrieve-the-call-uuid)  Retrieve the Call UUID

For scenarios where you must add feedback immediately after a Call, you can retrieve the Call UUID programmatically during or after the Call execution.

##### During Call execution

To retrieve the UUID during Call execution, get the current Call, and return the ID.

- Python

- TypeScript


```

import weave
weave.init("uuid")

@weave.op()
def simple_operation(input_value):
    # Perform some simple operation
    output = f"Processed {input_value}"
    # Get the current call ID
    current_call = weave.require_current_call()
    call_id = current_call.id
    return output, call_id
```

```
This feature is not available in TypeScript yet.
```

##### After Call execution

Alternatively, you can use the `call()` method to execute the operation and retrieve the ID after Call execution:

- Python

- TypeScript


```
import weave
weave.init("uuid")

@weave.op()
def simple_operation(input_value):
    return f"Processed {input_value}"

# Execute the operation and retrieve the result and call ID
result, call = simple_operation.call("example input")
call_id = call.id
```

```
This feature is not available in TypeScript yet.
```

### [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#delete-feedback-from-a-call)  Delete feedback from a Call

You can delete feedback from a particular call by specifying a UUID.

- Python

- TypeScript


```
call.feedback.purge("[FEEDBACK-UUID]")
```

```
This feature is not available in TypeScript yet.
```

## [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#add-human-annotations)  Add human annotations

Human annotations let you capture structured, human-reviewed judgments about Calls so that reviewers can score model output against your own criteria.Human annotations are supported in the Weights & Biases UI. This functionality lets you create custom fields to add human-entered data to your Traces as feedback. To make human annotations, you must first create a Human Annotation scorer using either the [UI](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback#create-a-human-annotation-scorer-in-the-ui) or the [API](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback#create-a-human-annotation-scorer-using-the-api). Then, you can [use the scorer in the UI to make annotations](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback#use-the-human-annotation-scorer-in-the-ui), and [modify your annotation scorers using the API](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback#modify-a-human-annotation-scorer-using-the-api).

### [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#create-a-human-annotation-scorer-in-the-ui)  Create a human annotation scorer in the UI

To create a human annotation scorer in the UI, do the following:

1. In the project sidebar, navigate to **Assets**.
2. In the Assets navigation panel, click **Scorers**.
3. In the **Scorers** panel header, click **New scorer**.
4. In the **Create Scorer** modal dialog, set:
   - `Scorer type` to `Human annotation`
   - `Name`
   - `Description`
   - `Type`, which determines the type of feedback to collect, such as `boolean` or `integer`.
5. Click **Create scorer**. Now, you can use your scorer to make annotations.

In the following example, a human annotator selects which type of document the LLM loaded. The `Type` for the score configuration is an `enum` that contains the possible document types.

![Create Scorer modal dialog](https://mintcdn.com/coreweave-dbfa0e8d/3Dv_sw2eg8feUJlx/products/wandb/weave/_media/human-annotation-scorer-form.png?fit=max&auto=format&n=3Dv_sw2eg8feUJlx&q=85&s=7d38f47385bd21b407caf5a959b1a7e9)

### [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#use-the-human-annotation-scorer-in-the-ui)  Use the human annotation scorer in the UI

After you create a human annotation scorer, it becomes available to use on the Traces page.To use the scorer, do the following:

1. In the project sidebar, navigate to **Traces**.
2. Find the row for the Call that you want to add a human annotation to.
3. Click the linked Trace name to open the trace tree and Call details panel.
4. In the upper right corner of the Call details tab bar, click the **Show feedback** button.![Marker icon in Call header](https://mintcdn.com/coreweave-dbfa0e8d/3Dv_sw2eg8feUJlx/products/wandb/weave/_media/marker-icon.png?fit=max&auto=format&n=3Dv_sw2eg8feUJlx&q=85&s=aafc9db6195967a8ec0acfe214fd5044)Your available human annotation scorers display in an **Annotate** panel.![Human Annotation scorer feedback panel](https://mintcdn.com/coreweave-dbfa0e8d/3Dv_sw2eg8feUJlx/products/wandb/weave/_media/full-feedback-sidebar.png?fit=max&auto=format&n=3Dv_sw2eg8feUJlx&q=85&s=ba9ef22e7d49bd57e0a087b7dcbd05f0)
5. Make an annotation.
6. Click **Save**.
7. In the Call details panel tab bar, click the **Feedback** tab to view the Feedback table. The new annotation displays in the table. You can also view the annotations in the **Annotations** column in the main Traces table.

> Refresh the Traces table to view the most up-to-date information.


![Human Annotation scorer feedback in Traces table](https://mintcdn.com/coreweave-dbfa0e8d/3Dv_sw2eg8feUJlx/products/wandb/weave/_media/feedback-in-the-table.png?fit=max&auto=format&n=3Dv_sw2eg8feUJlx&q=85&s=6118c46e60c28bc3117179d9d44b49fa)

### [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#create-a-human-annotation-scorer-using-the-api)  Create a human annotation scorer using the API

You can also create human annotation scorers through the API. Each scorer is its own object, which you create and update independently. To create a human annotation scorer programmatically, do the following:

1. Import the `AnnotationSpec` class from `weave.flow.annotation_spec`.
2. Use the `publish` method from `weave` to create the scorer.

The following example creates two scorers. The first scorer, `Temperature`, scores the perceived temperature of the LLM call. The second scorer, `Tone`, scores the tone of the LLM response. Each scorer uses `save` with an associated object ID (`temperature-scorer` and `tone-scorer`).

- Python

- TypeScript


```
import weave
from weave.flow.annotation_spec import AnnotationSpec

client = weave.init("feedback-example")

spec1 = AnnotationSpec(
  name="Temperature",
  description="The perceived temperature of the llm call",
  field_schema={
    "type": "number",
    "minimum": -1,
    "maximum": 1,
  }
)
spec2 = AnnotationSpec(
  name="Tone",
  description="The tone of the llm response",
  field_schema={
    "type": "string",
    "enum": ["Aggressive", "Neutral", "Polite", "N/A"],
  },
)
weave.publish(spec1, "temperature-scorer")
weave.publish(spec2, "tone-scorer")
```

```
This feature is not available in TypeScript yet.
```

### [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#modify-a-human-annotation-scorer-using-the-api)  Modify a human annotation scorer using the API

Expanding on [creating a human annotation scorer using the API](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback#create-a-human-annotation-scorer-using-the-api), the following example creates an updated version of the `Temperature` scorer, by using the original object ID (`temperature-scorer`) on `publish`. The result is an updated object, with a history of all versions.

> You can view human annotation scorer object history in the **Scorers** tab under **Human annotations**.

- Python

- TypeScript


```
import weave
from weave.flow.annotation_spec import AnnotationSpec

client = weave.init("feedback-example")

# create a new version of the scorer
spec1 = AnnotationSpec(
  name="Temperature",
  description="The perceived temperature of the llm call",
  field_schema={
    "type": "integer",  # <<- change type to integer
    "minimum": -1,
    "maximum": 1,
  }
)
weave.publish(spec1, "temperature-scorer")
```

```
This feature is not available in TypeScript yet.
```

![Human Annotation scorer history](https://mintcdn.com/coreweave-dbfa0e8d/3Dv_sw2eg8feUJlx/products/wandb/weave/_media/human-annotation-scorer-history.png?fit=max&auto=format&n=3Dv_sw2eg8feUJlx&q=85&s=98b79764fd87597de1bde43f086def64)

### [​](https://docs.coreweave.com/products/wandb/weave/guides/tracking/feedback\#use-a-human-annotation-scorer-using-the-api)  Use a human annotation scorer using the API

The feedback API lets you use a human annotation scorer by specifying a specially constructed name and an `annotation_ref` field. You can obtain the `annotation_spec_ref` from the UI by selecting the appropriate tab, or during the creation of the `AnnotationSpec`.

- Python


```
import weave

client = weave.init("feedback-example")

call = client.get_call("[CALL-ID]")
annotation_spec = weave.ref("[ANNOTATION-SPEC-REF-URI]")

call.feedback.add(
  feedback_type="wandb.annotation." + annotation_spec.name,
  payload={"value": 1},
  annotation_ref=annotation_spec.uri(),
)
```

Last modified onSeptember 28, 2026

Was this page helpful?

YesNo

![Project Logo](<Base64-Image-Removed>)

Ask AI

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**