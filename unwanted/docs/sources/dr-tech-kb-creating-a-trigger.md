> ## Documentation Index
>
> Fetch the complete documentation index at: [https://kb.vastdata.com/llms.txt](https://kb.vastdata.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

# Creating a Trigger

- Updated on Jan 30, 2026
- Published on Jan 25, 2026

- 2 minute(s) read
- Focus
- Listen

Follow

Copy pageCopy as Markdown for LLMsView as MarkdownView the page as plain text

Open in ChatGPTAsk ChatGPT about this pageOpen in ClaudeAsk Claude about this page

Article summary[Prev](https://kb.vastdata.com/documentation/docs/installing-the-vast-dataengine-cli "Installing the VAST DataEngine CLI")[Next](https://kb.vastdata.com/documentation/docs/creating-a-dataengine-function "Creating a DataEngine Function")

DataEngine functions are triggered by events. Create triggers to define which events to watch for. A trigger can either produce events on a schedule or watch for events related to objects in a bucket. You can build triggers into a pipeline and so that they trigger functions.

1. From the left navigation menu, select Manage Elements (![ManageElementsMenuIcon.png](https://cdn.document360.io/726fb2d3-253d-48b7-a67b-bcf45100fafc/Images/Documentation/img-b3d2ad07e044da6d7a37d19d29da0a16(1).png?sv=2026-02-06&spr=https&st=2026-10-02T00%3A05%3A12Z&se=2026-10-02T00%3A17%3A12Z&sr=c&sp=r&sig=49gyB60a243CQD5CDJGbnZusDJS8j6Qk8cq%2BMdJ4jO0%3D)) and then Triggers.

2. Click Create New Trigger.

3. Enter a name for the trigger in the Trigger Name field.

4. In the Trigger Type dropdown, select the type of trigger you want to create:



   - Element. A trigger that watches for events related to elements in a source view.

   - Schedule. A trigger that produces events on a schedule.


5. Complete the relevant fields:



   - If you selected _Element_ as the _Trigger Type_:



     |     |     |
     | --- | --- |
     | Description | A description for the trigger. |
     | Source view | From the dropdown, select the view in which the events will occur. The dropdown lists all S3 bucket views on the local VAST Cluster tenant to which you have permission to access. |
     | Event type | From the dropdown, select a type of event.<br>     - ElementCreated. The creation of an element in the source view. <br>       <br>     - ElementDeleted. The deletion of an element from the source view. <br>       <br>     - ElementTagCreated. The creation of a tag on an element in the source view.  <br>       <br>     - ElementTagDeleted. The deletion of a tag on an element in the source view. <br>       <br>> Note<br>> <br>> You will be able to restrict the relevant elements by object key prefix and suffix. |
     | Source type | The type of elements that register events for the trigger. This is restricted to S3 objects in the current version. Therefore, the field is read only and displays S3. |
     | Destination |
     | Target Event Broker View | From the dropdown, select the view that hosts the VAST Event Broker to use to stream events for the trigger. |
     | Topic | From the dropdown, select the event broker topic that should be used. |
     | Filters |
     | Object Key Filters | To filter elements by suffix or prefix, enter a prefix and/or a suffix. The event type definition will be restricted to objects with the specified prefix and/or suffix in their object keys. |
     |  |
     | Custom Extensions | Use this field to add key-value pairs to be passed as event output extensions. Each key can contain only lowercase letters and digits, must start with a letter, and must be 1-20 characters long. |
     | Tags | Use this field to tag the trigger. <br>To add a tag, click Add Tags, enter a key-value pair in the fields provided and then click Add to Tags. |

   - If you selected _Schedule_ as the _Trigger Type_:



     |     |     |
     | --- | --- |
     | Description | A description for the trigger. |
     | Destination |
     | Target Kafka View | From the dropdown, select the view that hosts the VAST Event Broker to use to stream events for the trigger. |
     | Topic | From the dropdown, select the event broker topic that should be used. |
     | Schedule | Do either of the following to define a schedule for the trigger:<br>     - Select Simple and use the fields provided to enter a frequency. <br>       <br>     - Select Advanced to type the schedule in Quartz syntax. |
     | Custom Extensions | Use this field to add key-value pairs to be passed as event output extensions. Each key can contain only lowercase letters and digits, must start with a letter, and must be 1-20 characters long. |
     | Tags | Optionally add tags to the trigger. To add a tag, click Add Tags, enter a key-value pair in the fields provided and then click Add to Tags. |


6. Click Create Trigger.

The trigger is created and is listed in the Triggers page.


Was this article helpful? (Provide Feedback)

Yes  No

Previous article

Installing the VAST DataEngine CLI

Next article

Creating a DataEngine Function

Related articles

- [Creating a Trigger](https://kb.vastdata.com/documentation/docs/creating-a-trigger-55)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 DataEngine User Guide

- [Managing Triggers](https://kb.vastdata.com/documentation/docs/managing-triggers-55)



VAST AI OS > Version 5.5 > VAST Cluster 5.5 DataEngine User Guide

- [Managing Triggers](https://kb.vastdata.com/documentation/docs/managing-triggers)



VAST AI OS > Version 5.4 > VAST Cluster 5.4 DataEngine User Guide