[Skip to main content](https://docs.frigate.video/configuration/genai/genai_review/#__docusaurus_skipToContent_fallback)

🚀
Get more relevant and accurate detections with Frigate+ models.
[Learn more](https://frigate.video/plus/) ✨

On this page

Generative AI can be used to automatically generate structured summaries of review items. These summaries will show up in Frigate's native notifications as well as in the UI. Generative AI can also be used to take a collection of summaries over a period of time and provide a report, which may be useful to get a quick report of everything that happened while out for some amount of time.

Requests for a summary are requested automatically to your AI provider for alert review items when the activity has ended, they can also be optionally enabled for detections as well.

Generative AI review summaries can also be toggled dynamically for a [camera via MQTT](https://docs.frigate.video/integrations/mqtt#frigatecamera_namereview_descriptionsset).

## Review Summary Usage and Best Practices [​](https://docs.frigate.video/configuration/genai/genai_review/\#review-summary-usage-and-best-practices "Direct link to Review Summary Usage and Best Practices")

Review summaries provide structured JSON responses that are saved for each review item:

```text
- `title` (string): A concise, direct title that describes the purpose or overall action (e.g., "Person taking out trash", "Joe walking dog").
- `scene` (string): A narrative description of what happens across the sequence from start to finish, including setting, detected objects, and their observable actions.
- `shortSummary` (string): A brief 2-sentence summary of the scene, suitable for notifications. This is a condensed version of the scene description.
- `confidence` (float): 0-1 confidence in the analysis. Higher confidence when objects/actions are clearly visible and context is unambiguous.
- `other_concerns` (list): List of user-defined concerns that may need additional investigation.
- `potential_threat_level` (integer): 0, 1, or 2 as defined below.
```

This will show in multiple places in the UI to give additional context about each activity, and allow viewing more details when extra attention is required. Frigate's built in notifications will automatically show the title and `shortSummary` when the data is available, while the full `scene` description is available in the UI for detailed review.

### Defining Typical Activity [​](https://docs.frigate.video/configuration/genai/genai_review/\#defining-typical-activity "Direct link to Defining Typical Activity")

Each installation and even camera can have different parameters for what is considered suspicious activity. Frigate allows the `activity_context_prompt` to be defined globally and at the camera level, which allows you to define more specifically what should be considered normal activity. It is important that this is not overly specific as it can sway the output of the response.

To configure the activity context prompt:

- Frigate UI
- YAML

Navigate to **Settings**→ **Global configuration**→ **Review**.

- Set **GenAI config > Activity context prompt** to your custom activity context text

```yaml
review:
  genai:
    activity_context_prompt: |
      ### Normal Activity Indicators (Level 0)
      - Known/verified people in any zone at any time
      ...
```

Default Activity Context Prompt

```yaml
review:
  genai:
    activity_context_prompt: |
      ### Normal Activity Indicators (Level 0)
      - Known/verified people in any zone at any time
      - People with pets in residential areas
      - Deliveries or services during daytime/evening (6 AM - 10 PM): carrying packages to doors/porches, placing items, leaving
      - Services/maintenance workers with visible tools, uniforms, or service vehicles during daytime
      - Activity confined to public areas only (sidewalks, streets) without entering property at any time

      ### Suspicious Activity Indicators (Level 1)
      - **Testing or attempting to open doors/windows/handles on vehicles or buildings** — ALWAYS Level 1 regardless of time or duration
      - **Unidentified person in private areas (driveways, near vehicles/buildings) during late night/early morning (11 PM - 5 AM)** — ALWAYS Level 1 regardless of activity or duration
      - Taking items that don't belong to them (packages, objects from porches/driveways)
      - Climbing or jumping fences/barriers to access property
      - Attempting to conceal actions or items from view
      - Prolonged loitering: remaining in same area without visible purpose throughout most of the sequence

      ### Critical Threat Indicators (Level 2)
      - Holding break-in tools (crowbars, pry bars, bolt cutters)
      - Weapons visible (guns, knives, bats used aggressively)
      - Forced entry in progress
      - Physical aggression or violence
      - Active property damage or theft in progress

      ### Assessment Guidance
      Evaluate in this order:

      1. **If person is verified/known** → Level 0 regardless of time or activity
      2. **If person is unidentified:**
        - Check time: If late night/early morning (11 PM - 5 AM) AND in private areas (driveways, near vehicles/buildings) → Level 1
        - Check actions: If testing doors/handles, taking items, climbing → Level 1
        - Otherwise, if daytime/evening (6 AM - 10 PM) with clear legitimate purpose (delivery, service worker) → Level 0
      3. **Escalate to Level 2 if:** Weapons, break-in tools, forced entry in progress, violence, or active property damage visible (escalates from Level 0 or 1)

      The mere presence of an unidentified person in private areas during late night hours is inherently suspicious and warrants human review, regardless of what activity they appear to be doing or how brief the sequence is.
```

### Image Source [​](https://docs.frigate.video/configuration/genai/genai_review/\#image-source "Direct link to Image Source")

By default, review summaries use preview images (cached preview frames) which have a lower resolution but use fewer tokens per image. For better image quality and more detailed analysis, configure Frigate to extract frames directly from recordings at a higher resolution.

- Frigate UI
- YAML

Navigate to **Settings**→ **Global configuration**→ **Review**.

- Set **GenAI config > Enable GenAI descriptions** to on
- Set **GenAI config > Review image source** to `recordings` (default is `preview`)

```yaml
review:
  genai:
    enabled: true
    image_source: recordings # Options: "preview" (default) or "recordings"
```

When using `recordings`, frames are extracted at 480px height while maintaining the camera's original aspect ratio, providing better detail for the LLM while being mindful of context window size. This is particularly useful for scenarios where fine details matter, such as identifying license plates, reading text, or analyzing distant objects.

The number of frames sent to the LLM is dynamically calculated based on:

- Your LLM provider's context window size
- The camera's resolution and aspect ratio (ultrawide cameras like 32:9 use more tokens per image)
- The image source (recordings use more tokens than preview images)

Frame counts are automatically optimized to use ~98% of the available context window while capping at 20 frames maximum to ensure reasonable inference times. Note that using recordings will:

- Provide higher quality images to the LLM (480p vs 180p preview images)
- Use more tokens per image due to higher resolution
- Result in fewer frames being sent for ultrawide cameras due to larger image size
- Require that recordings are enabled for the camera

If recordings are not available for a given time period, the system will automatically fall back to using preview frames.

### Additional Concerns [​](https://docs.frigate.video/configuration/genai/genai_review/\#additional-concerns "Direct link to Additional Concerns")

Along with the concern of suspicious activity or immediate threat, you may have concerns such as animals in your garden or a gate being left open. Configure these concerns so that review summaries will make note of them if the activity requires additional review.

- Frigate UI
- YAML

Navigate to **Settings**→ **Global configuration**→ **Review**.

- Set **GenAI config > Additional concerns** to a list of your concerns (e.g., `animals in the garden`)

```yaml
review:
  genai:
    enabled: true
    additional_concerns:
      - animals in the garden
```

### Preferred Language [​](https://docs.frigate.video/configuration/genai/genai_review/\#preferred-language "Direct link to Preferred Language")

By default, review summaries are generated in English. Configure Frigate to generate summaries in your preferred language by setting the `preferred_language` option.

- Frigate UI
- YAML

Navigate to **Settings**→ **Global configuration**→ **Review**.

- Set **GenAI config > Preferred language** to the desired language (e.g., `Spanish`)

```yaml
review:
  genai:
    enabled: true
    preferred_language: Spanish
```

## Review Reports [​](https://docs.frigate.video/configuration/genai/genai_review/\#review-reports "Direct link to Review Reports")

Along with individual review item summaries, Generative AI can also produce a single report of review items from all cameras marked "suspicious" over a specified time period (for example, a daily summary of suspicious activity while you're on vacation).

### Requesting Reports Programmatically [​](https://docs.frigate.video/configuration/genai/genai_review/\#requesting-reports-programmatically "Direct link to Requesting Reports Programmatically")

Review reports can be requested via the [API](https://docs.frigate.video/integrations/api/generate-review-summary-review-summarize-start-start-ts-end-end-ts-post) by sending a POST request to `/api/review/summarize/start/{start_ts}/end/{end_ts}` with Unix timestamps.

For Home Assistant users, there is a built-in service (`frigate.review_summarize`) that makes it easy to request review reports as part of automations or scripts. This allows you to automatically generate daily summaries, vacation reports, or custom time period reports based on your specific needs.

## Troubleshooting [​](https://docs.frigate.video/configuration/genai/genai_review/\#troubleshooting "Direct link to Troubleshooting")

If summaries are not being generated, or the generated summaries are not what you expect, see [How do I debug GenAI issues?](https://docs.frigate.video/configuration/genai/genai_config#how-do-i-debug-genai-issues).

- [Review Summary Usage and Best Practices](https://docs.frigate.video/configuration/genai/genai_review/#review-summary-usage-and-best-practices)
  - [Defining Typical Activity](https://docs.frigate.video/configuration/genai/genai_review/#defining-typical-activity)
  - [Image Source](https://docs.frigate.video/configuration/genai/genai_review/#image-source)
  - [Additional Concerns](https://docs.frigate.video/configuration/genai/genai_review/#additional-concerns)
  - [Preferred Language](https://docs.frigate.video/configuration/genai/genai_review/#preferred-language)
- [Review Reports](https://docs.frigate.video/configuration/genai/genai_review/#review-reports)
  - [Requesting Reports Programmatically](https://docs.frigate.video/configuration/genai/genai_review/#requesting-reports-programmatically)
- [Troubleshooting](https://docs.frigate.video/configuration/genai/genai_review/#troubleshooting)

Ask AI

![AI chat avatar](https://frigate.video/images/favicon.png)