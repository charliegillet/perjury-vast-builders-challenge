[Skip to main content](https://docs.nvidia.com/vss/2.4.0/content/examples.html#main-content)

Back to top

`⌘` + `K`

[![Video Search and Summarization Agent - Home](https://docs.nvidia.com/vss/2.4.0/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg)![Video Search and Summarization Agent - Home](https://docs.nvidia.com/vss/2.4.0/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg)\\
Video Search and Summarization Agent](https://docs.nvidia.com/vss/2.4.0/index.html)

2.4.0

[3.2.1](https://docs.nvidia.com/vss/latest/content/examples.html) [3.2.0](https://docs.nvidia.com/vss/3.2.0/content/examples.html) [3.1.0](https://docs.nvidia.com/vss/3.1.0/content/examples.html) [3.0.0](https://docs.nvidia.com/vss/3.0.0/content/examples.html) [2.4.1](https://docs.nvidia.com/vss/2.4.1/content/examples.html) [2.4.0](https://docs.nvidia.com/vss/2.4.0/content/examples.html) [2.3.1](https://docs.nvidia.com/vss/2.3.1/content/examples.html) [2.3.0](https://docs.nvidia.com/vss/2.3.0/content/examples.html) [2.2.0](https://docs.nvidia.com/vss/2.2.0/content/examples.html)

# Examples [\#](https://docs.nvidia.com/vss/2.4.0/content/examples.html\#examples "Link to this heading")

There are multiple example clips provided in the UI Application, which can be explored to better understand how the agent works. For each example,
we’ve provided a **Prompt**, **Caption Summarization Prompt**, and **Summary Aggregation Prompt** to get started. Refer to
[Tuning Prompts](https://docs.nvidia.com/vss/2.4.0/content/via_customization.html#tuning-prompts) for more details on the prompts.

## Traffic Camera Video (its) [\#](https://docs.nvidia.com/vss/2.4.0/content/examples.html\#traffic-camera-video-its "Link to this heading")

This is a two-minute ten-second video (its.mp4) consisting of a synthetically generated traffic scene.

**Chunk Size**: 10 sec

**VLM Input Resolution**: 1920 x 1080 (Set from the parameters dialog by clicking on **Show Parameters** on the top right corner of the UI)

> **Prompt**
>
> ```
> You are an intelligent traffic system.
> You must monitor and take note of all traffic related events.
> Start and end each sentence with a time stamp.
> ```
>
> Copy to clipboard
>
> **Caption Summarization Prompt**
>
> ```
> You will be given captions from sequential clips of a video.
> Aggregate captions in the format start_time:end_time:caption
> based on whether captions are related to one another or create
> a continuous scene.
> ```
>
> Copy to clipboard
>
> **Summary Aggregation Prompt**
>
> ```
> Based on the available information, generate a traffic report
> that is organized chronologically and in logical sections.
> This must be a concise, yet descriptive summary of all the important events.
> The format should be intuitive and easy for a user to read and understand what happened.
> Format the output in Markdown so it can be displayed nicely.
> ```
>
> Copy to clipboard

**Sample questions**

1. Did a car crash occur?

2. When do the police arrive at the crash?

3. What cars were involved in the crash?


## Warehouse Video (short) (with Alerts) [\#](https://docs.nvidia.com/vss/2.4.0/content/examples.html\#warehouse-video-short-with-alerts "Link to this heading")

This is a three-minute, 30-second video (warehouse.mp4) consisting of clips within a warehouse environment.

**Chunk Size**: 10 sec

> **Prompt**
>
> ```
> You are a warehouse monitoring system. Describe the events
> in this warehouse and look for any anomalies.
> Start and end each sentence with a time stamp.
> ```
>
> Copy to clipboard
>
> **Caption Summarization Prompt**
>
> ```
> Summarize similar captions that are sequential to one another,
> while maintaining the details of each caption, in the format
> start_time:end_time:caption. The output should be bullet points
> in the format start_time:end_time: detailed_event_description.
> ```
>
> Copy to clipboard
>
> **Summary Aggregation Prompt**
>
> ```
> Aggregate captions in the format start_time:end_time:caption
> based on whether captions are related to one another or create
> a continuous scene. The output should only be bullet points in
> the format start_time:end_time: detailed_event_description.
> ```
>
> Copy to clipboard

**Alerts**

Select “Create Alerts” tab and add the following alerts:

- Alert Name: `Box Dropped`

- Events: `box dropping`


**Sample questions**

1. When did the forklift first arrive?

2. Did a worker drop any boxes?

3. What breaches of safety protocol took place?


## Bridge Inspection Video [\#](https://docs.nvidia.com/vss/2.4.0/content/examples.html\#bridge-inspection-video "Link to this heading")

This is a three-minute video (bridge.mp4) consisting of drone footage inspecting a bridge.

**Chunk Size**: 20 sec

> **Prompt**
>
> ```
> You are a bridge inspection system. Describe the condition of
> the bridge. Start and end each sentence with a time stamp.
> ```
>
> Copy to clipboard
>
> **Caption Summarization Prompt**
>
> ```
> You will be given captions from sequential clips of a video.
> Aggregate captions in the format start_time:end_time:caption
> based on whether captions are related to one another or create
> a continuous scene.
> ```
>
> Copy to clipboard
>
> **Summary Aggregation Prompt**
>
> ```
> Based on the available information, generate a summary that
> describes the condition of the bridge. The summary should be
> organized chronologically and in logical sections. This should be a
> concise, yet descriptive summary of all the important events.
> The format should be intuitive and easy for a user to understand what happened.
> Format the output in Markdown so it can be displayed nicely.
> ```
>
> Copy to clipboard

**Sample questions**

1. Where is graffiti located?

2. At what time do you see graffiti?

3. Are there people on the bridge?


## Warehouse Video (long) [\#](https://docs.nvidia.com/vss/2.4.0/content/examples.html\#warehouse-video-long "Link to this heading")

This is an 82-minute video (warehouse\_82min.mp4) consisting of clips within a warehouse environment.

**Chunk Size**: 60 sec

> **Prompt**
>
> ```
> Write a concise and clear dense caption for the provided warehouse video,
> focusing on irregular or hazardous events such as boxes falling, workers
> not wearing PPE, workers falling, workers taking photographs,
> workers chitchatting, forklift stuck, etc. Start and end each sentence
> with a time stamp.
> ```
>
> Copy to clipboard
>
> **Caption Summarization Prompt**
>
> ```
> You should summarize the following events of a warehouse in the format
> start_time:end_time:caption. For start_time and end_time use, to
> separate seconds, minutes, and hours. If during a time segment only regular
> activities happen, then ignore them, else note any irregular activities
> in detail. The output should be bullet points in the format
> start_time:end_time:detailed_event_description. Don't return anything
> else except the bullet points.
> ```
>
> Copy to clipboard
>
> **Summary Aggregation Prompt**
>
> ```
> You are a warehouse monitoring system. Given the caption in the form
> start_time:end_time:caption, Aggregate the following captions in the
> format start_time:end_time:event_description. If the event_description
> is the same as another event_description, aggregate the captions in
> the format start_time1:end_time1,...,start_timek:end_timek:event_description.
> If any two adjacent end_time1 and start_time2 is within a few tenths of a second,
> merge the captions in the format start_time1:end_time2. The output should
> only contain bullet points.  Cluster the output into Unsafe Behavior,
> Operational Inefficiencies, Potential Equipment Damage and Unauthorized Personnel.
> ```
>
> Copy to clipboard

**Sample questions**

1. When did the red forklift first appear in the scene?

2. Was anyone not wearing personal protective equipment?

3. What were workers doing?


## Traffic Camera Images [\#](https://docs.nvidia.com/vss/2.4.0/content/examples.html\#traffic-camera-images "Link to this heading")

This example is a sequence of images sampled from a traffic camera with a timestamp overlay. Multiple images can be provided under the “IMAGE FILE SUMMARIZATION & Q&A” tab of the UI.

> **Images**
>
> Select multiple images from the samples list sequentially until all images are loaded, as shown below.
>
> ![Select multiple images from samples.](https://docs.nvidia.com/vss/2.4.0/_images/multiimage.gif)
>
> **Prompt**
>
> ```
> You are an intelligent traffic system. You will be given a set of images from a traffic intersection.
> Write a detailed caption for each image to capture all traffic related events and details. For each caption,
> include the timestamp from the image.
> ```
>
> Copy to clipboard
>
> **Caption Summarization Prompt**
>
> ```
> Combine the captions if needed. Do not lose any information.
> ```
>
> Copy to clipboard
>
> **Summary Aggregation Prompt**
>
> ```
> You will be given a set of captions describing several images from a traffic intersection.
> Write a summary of the events from the captions and include the timestamp information.
> ```
>
> Copy to clipboard

**Sample questions**

1. What time did the car crash occur?

2. Did a police car respond to the crash?

3. When did the firetruck arrive?


## Jensen Huang’s Special Address at AI Summit India 2024 (With Audio) [\#](https://docs.nvidia.com/vss/2.4.0/content/examples.html\#jensen-huang-s-special-address-at-ai-summit-india-2024-with-audio "Link to this heading")

This is a four minute video (Jensen\_AI\_Summit\_India\_2024\_clip.mp4) clip from NVIDIA CEO Jensen Huang’s Special Address at AI Summit India 2024.
The clip contains both video and audio streams. The following tools must be installed to use the prompts with
**Enable Audio** selected:

**Chunk Size**: 30 sec

> **Prompt**
>
> ```
> Write a concise and clear dense caption for the provided
> NVIDIA AI Summit video, focusing on the technologies and products.
> ```
>
> Copy to clipboard
>
> **Caption Summarization Prompt**
>
> ```
> You should summarize the following events of a conference.
> The output should be in bullet points with timestamps.
> Do not return anything else except the bullet points.
> ```
>
> Copy to clipboard
>
> **Summary Aggregation Prompt**
>
> ```
> You are a video description service.  Given the video captions and
> audio transcripts, aggregate them to a concise summary with timestamps.
> The output should only contain bullet points.
> Cluster the output into main themes in chronological order.
> ```
>
> Copy to clipboard

**Sample questions**

1. According to the presenter, how has the method of software development changed?

2. What are the different acceleration libraries mentioned in the presentation?

3. What examples of translating information from one modality to another were given by the speaker?


## Traffic Camera Video (its) (With “Enable CV Metadata” Selected) [\#](https://docs.nvidia.com/vss/2.4.0/content/examples.html\#traffic-camera-video-its-with-enable-cv-metadata-selected "Link to this heading")

Replace the first prompt in [Traffic Camera Video (its)](https://docs.nvidia.com/vss/2.4.0/content/examples.html#traffic-camera-video-its) with the prompt below, so that VLM uses IDs in the event descriptions.

**Chunk Size**: 10 sec.

**VLM Input Resolution**: 1920 x 1080 (Set from the parameters dialog by clicking on **Show Parameters** on the top right corner of the UI)

> **Prompt**
>
> ```
> You are a traffic monitoring system. For each traffic event:
> 1. Pause at the event's start and review visible numeric IDs on all vehicles.
> 2. For each vehicle (car, truck, bus, motorcycle, etc.), record its overlayed ID exactly as seen. If an ID is not visible, use "ID: None". If unreadable, use "ID: Unclear".
> 3. Describe the event, always referencing vehicles as "Type ID: X" (e.g., "Car ID: 7"). Do not use generic phrases like "black car" unless an ID is missing.
> 4. List every vehicle involved in each event, whether acting individually or as a group.
> 5. If a numeric ID matches two different vehicles at different times, note: "ID reused—possibly different vehicle."
> 6. Format each event as:
> 7. [start timestamp]-[end timestamp]: <Vehicle(s) with ID(s)>: <Action>
> Example:
> - 00.05-00.10: Car ID: 7 turns left at intersection.
> - 00.12-00.16: Truck ID: None passes through.
> - 00.20-00.23: Car ID: 9, Motorcycle ID: 12 overtake Bus ID: 3.
> - 00.30-00.35: Car ID: 3 (ID reused—possibly different vehicle) enters from right.
> For each event, focus on ID extraction first, then give a precise action description.
> ```
>
> Copy to clipboard
>
> **Alternate Prompt(For gpt-4o, VILA and NVILA)**
>
> ```
> You are an intelligent traffic system. The provided video is
> a processed clip where each vehicle is overlaid with an ID.
> You must monitor and take note of all traffic related events.
> Start each event description with a start and end time stamp
> of the event, and use vehicle IDs in event description.
> ```
>
> Copy to clipboard
>
> **CV Pipeline Prompt**
>
> Also, set the following CV Pipeline Prompt:
>
> ```
> vehicle
> ```
>
> Copy to clipboard
>
> If you need to specify threshold (0-1.0) for object detection,
> you can do so by adding it after object prompts using semicolon as delimiter
> as shown in the following prompt:
>
> ```
> vehicle;0.48
> ```
>
> Copy to clipboard

**Sample questions**

1. Do you see any abnormal events in the clip? If so, which cars are involved?

2. Did a police car respond to the collision? If so, please answer with the ID of the police car.

3. Did a firetruck respond to the collision? If so, please answer with the ID of the fire truck.


## Warehouse Video Short (With “Enable CV Metadata” Selected) [\#](https://docs.nvidia.com/vss/2.4.0/content/examples.html\#warehouse-video-short-with-enable-cv-metadata-selected "Link to this heading")

Replace the first prompt in [Warehouse Video (short)](https://docs.nvidia.com/vss/2.4.0/content/examples.html#warehouse-video-short-with-alerts) with the prompt below, and set the following CV Pipeline Prompt.

**Chunk Size**: 10 sec.

> **Prompt**
>
> ```
> You are a warehouse monitoring system. For each major event, follow these steps:
> 1.Pause the video at the event's start. Carefully observe all visible overlayed numeric IDs (e.g., 1, 2, 10) associated with people in the frame.
> 2. For each individual (man, woman, worker, person, etc.), identify and extract their numeric overlayed ID. If no ID is visible, write "ID: None".
> 3. Describe the event, always referencing each person as "e.g., man ID: 7", not with generic terms.
> 4. Output should enumerate each event as:
> 5. [start timestamp]-[end timestamp]: <Person description with ID>: <Action>
> Example:
> - 00.00-05.00: Man ID: 3 enters from the right carrying two boxes.
> - 05.00-08.00: Worker ID: 3 places one box on a lower shelf.
> - 30.00-35.00: Woman ID: 7 enters from the left.
> ```
>
> Copy to clipboard
>
> **Alternate Prompt(For gpt-4o, VILA and NVILA)\***
>
> ```
> You are a warehouse monitoring system. The provided video is
> a processed clip where each worker is overlaid with an ID.
> Describe the events in this warehouse and look for any anomalies,
> for example, box dropping, not waring PPE, unsafe forklift operations.
> Start each sentence with start and end timestamp of the event,
> and use worker IDs in event description.
> ```
>
> Copy to clipboard
>
> **CV Pipeline Prompt**
>
> ```
> person . forklift;0.5
> ```
>
> Copy to clipboard

**Sample questions**

1. Which worker dropped a box?

2. Which worker put on the caution tape?

3. Are there any workers who are not wearing a safety vest or helmet? If so, please identify them by their IDs.

4. Did anyone cross the restricted area?


## VSS Event Reviewer [\#](https://docs.nvidia.com/vss/2.4.0/content/examples.html\#vss-event-reviewer "Link to this heading")

The reference workflow for event review comes with a set of sample videos. This workflow uses a GDINO computer vision model to detect events in the video, and then VSS perception pipeline to analyze the video clip using a VLM. For all bundled sample videos, we have provided the GDINO configurations, and VLM prompt.

**Drive Sim Jaywalking Video**

This video is synthetically generated using NVIDIA Drive Sim, and shows pedestrians crossing the road with and without a crosswalk.

> **GDINO Configuration**:
>
> ```
> "gdino_classes": "person",
> "gdino_box_threshold": 0.8,
> "gdino_text_threshold": 0.8
> ```
>
> Copy to clipboard
>
> **VLM Prompt**
>
> ```
> Is the person walking on the white striped crosswalk?
> ```
>
> Copy to clipboard

**Warehouse Ladder Safety Video**

Warehouse video where workers are climbing a ladder with and without a safety gear.

> **GDINO Configuration**:
>
> ```
> "gdino_classes": "person",
> "gdino_box_threshold": 0.5,
> "gdino_text_threshold": 0.5
> ```
>
> Copy to clipboard
>
> **VLM Prompt**
>
> ```
> Is anyone on the ladder without a hardhat and safety vest?
> ```
>
> Copy to clipboard

**Conveyor Belt Inspection Video**

This video is synthetically generated using NVIDIA Isaac Sim, and shows boxes of different conditions being transported on a conveyor belt.

> **GDINO Configuration**:
>
> ```
> "gdino_classes": "cardboard box",
> "gdino_box_threshold": 0.5,
> "gdino_text_threshold": 0.5
> ```
>
> Copy to clipboard
>
> **VLM Prompt**
>
> ```
> You are a warehouse conveyor belt inspection system. You must inspect the cardboard box on the
>  conveyor belt to look for signs of physical damage. Physical damage includes but is not limited
>  to: 1) Crumpling 2) Tearing 3) Dents 4) Creases 5) Open boxes The box should be in near perfect
>  condition. Does one of the cardboard box in the video show signs of physical damage?
> ```
>
> Copy to clipboard

On this page