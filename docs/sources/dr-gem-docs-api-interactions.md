[Skip to main content](https://ai.google.dev/api/interactions-api#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/api/interactions-api)
- [Deutsch](https://ai.google.dev/api/interactions-api?hl=de)
- [Español – América Latina](https://ai.google.dev/api/interactions-api?hl=es-419)
- [Français](https://ai.google.dev/api/interactions-api?hl=fr)
- [Indonesia](https://ai.google.dev/api/interactions-api?hl=id)
- [Italiano](https://ai.google.dev/api/interactions-api?hl=it)
- [Polski](https://ai.google.dev/api/interactions-api?hl=pl)
- [Português – Brasil](https://ai.google.dev/api/interactions-api?hl=pt-br)
- [Shqip](https://ai.google.dev/api/interactions-api?hl=sq)
- [Tiếng Việt](https://ai.google.dev/api/interactions-api?hl=vi)
- [Türkçe](https://ai.google.dev/api/interactions-api?hl=tr)
- [Русский](https://ai.google.dev/api/interactions-api?hl=ru)
- [עברית](https://ai.google.dev/api/interactions-api?hl=he)
- [العربيّة](https://ai.google.dev/api/interactions-api?hl=ar)
- [فارسی](https://ai.google.dev/api/interactions-api?hl=fa)
- [हिंदी](https://ai.google.dev/api/interactions-api?hl=hi)
- [বাংলা](https://ai.google.dev/api/interactions-api?hl=bn)
- [ภาษาไทย](https://ai.google.dev/api/interactions-api?hl=th)
- [中文 – 简体](https://ai.google.dev/api/interactions-api?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/api/interactions-api?hl=zh-tw)
- [日本語](https://ai.google.dev/api/interactions-api?hl=ja)
- [한국어](https://ai.google.dev/api/interactions-api?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fapi%2Finteractions-api&prompt=select_account)

- On this page
- [CreateInteraction](https://ai.google.dev/api/interactions-api#CreateInteraction)
  - [Request body](https://ai.google.dev/api/interactions-api#request-body)
  - [Response](https://ai.google.dev/api/interactions-api#response)
- [cancelInteractionById](https://ai.google.dev/api/interactions-api#cancelInteractionById)
  - [Path / Query Parameters](https://ai.google.dev/api/interactions-api#path-query-parameters)
  - [Response](https://ai.google.dev/api/interactions-api#response_1)
- [getInteractionById](https://ai.google.dev/api/interactions-api#getInteractionById)
  - [Path / Query Parameters](https://ai.google.dev/api/interactions-api#path-query-parameters_1)
  - [Response](https://ai.google.dev/api/interactions-api#response_2)
- [deleteInteraction](https://ai.google.dev/api/interactions-api#deleteInteraction)
  - [Path / Query Parameters](https://ai.google.dev/api/interactions-api#path-query-parameters_2)
  - [Response](https://ai.google.dev/api/interactions-api#response_3)
- [Resources](https://ai.google.dev/api/interactions-api#resources)
  - [Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction)
  - [Examples](https://ai.google.dev/api/interactions-api#examples)
- [Data Models](https://ai.google.dev/api/interactions-api#data-models)
  - [Content](https://ai.google.dev/api/interactions-api#Resource:Content)
  - [Possible Types](https://ai.google.dev/api/interactions-api#possible-types_2)
  - [Examples](https://ai.google.dev/api/interactions-api#examples_1)
  - [Tool](https://ai.google.dev/api/interactions-api#Resource:Tool)
  - [Possible Types](https://ai.google.dev/api/interactions-api#possible-types_4)
  - [Examples](https://ai.google.dev/api/interactions-api#examples_2)
  - [InteractionSseStreamEvent](https://ai.google.dev/api/interactions-api#Resource:InteractionSseStreamEvent)
  - [Possible Types](https://ai.google.dev/api/interactions-api#possible-types_5)
  - [Examples](https://ai.google.dev/api/interactions-api#examples_3)
  - [ResponseFormat](https://ai.google.dev/api/interactions-api#Resource:ResponseFormat)
  - [Possible Types](https://ai.google.dev/api/interactions-api#possible-types_8)
  - [Examples](https://ai.google.dev/api/interactions-api#examples_4)
  - [Step](https://ai.google.dev/api/interactions-api#Resource:Step)
  - [Possible Types](https://ai.google.dev/api/interactions-api#possible-types_9)
  - [Examples](https://ai.google.dev/api/interactions-api#examples_5)
  - [EnvironmentConfig](https://ai.google.dev/api/interactions-api#Resource:EnvironmentConfig)
  - [EnvironmentNetworkEgressAllowlist](https://ai.google.dev/api/interactions-api#Resource:EnvironmentNetworkEgressAllowlist)
  - [ToolChoiceConfig](https://ai.google.dev/api/interactions-api#Resource:ToolChoiceConfig)
  - [ImageContent](https://ai.google.dev/api/interactions-api#Resource:ImageContent)
  - [TextContent](https://ai.google.dev/api/interactions-api#Resource:TextContent)

Gemini 3.8 Flash is now available. [Try it out](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [API reference](https://ai.google.dev/api)

Was this helpful?



 Send feedback



# Gemini Interactions API

- On this page
- [CreateInteraction](https://ai.google.dev/api/interactions-api#CreateInteraction)
  - [Request body](https://ai.google.dev/api/interactions-api#request-body)
  - [Response](https://ai.google.dev/api/interactions-api#response)
- [cancelInteractionById](https://ai.google.dev/api/interactions-api#cancelInteractionById)
  - [Path / Query Parameters](https://ai.google.dev/api/interactions-api#path-query-parameters)
  - [Response](https://ai.google.dev/api/interactions-api#response_1)
- [getInteractionById](https://ai.google.dev/api/interactions-api#getInteractionById)
  - [Path / Query Parameters](https://ai.google.dev/api/interactions-api#path-query-parameters_1)
  - [Response](https://ai.google.dev/api/interactions-api#response_2)
- [deleteInteraction](https://ai.google.dev/api/interactions-api#deleteInteraction)
  - [Path / Query Parameters](https://ai.google.dev/api/interactions-api#path-query-parameters_2)
  - [Response](https://ai.google.dev/api/interactions-api#response_3)
- [Resources](https://ai.google.dev/api/interactions-api#resources)
  - [Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction)
  - [Examples](https://ai.google.dev/api/interactions-api#examples)
- [Data Models](https://ai.google.dev/api/interactions-api#data-models)
  - [Content](https://ai.google.dev/api/interactions-api#Resource:Content)
  - [Possible Types](https://ai.google.dev/api/interactions-api#possible-types_2)
  - [Examples](https://ai.google.dev/api/interactions-api#examples_1)
  - [Tool](https://ai.google.dev/api/interactions-api#Resource:Tool)
  - [Possible Types](https://ai.google.dev/api/interactions-api#possible-types_4)
  - [Examples](https://ai.google.dev/api/interactions-api#examples_2)
  - [InteractionSseStreamEvent](https://ai.google.dev/api/interactions-api#Resource:InteractionSseStreamEvent)
  - [Possible Types](https://ai.google.dev/api/interactions-api#possible-types_5)
  - [Examples](https://ai.google.dev/api/interactions-api#examples_3)
  - [ResponseFormat](https://ai.google.dev/api/interactions-api#Resource:ResponseFormat)
  - [Possible Types](https://ai.google.dev/api/interactions-api#possible-types_8)
  - [Examples](https://ai.google.dev/api/interactions-api#examples_4)
  - [Step](https://ai.google.dev/api/interactions-api#Resource:Step)
  - [Possible Types](https://ai.google.dev/api/interactions-api#possible-types_9)
  - [Examples](https://ai.google.dev/api/interactions-api#examples_5)
  - [EnvironmentConfig](https://ai.google.dev/api/interactions-api#Resource:EnvironmentConfig)
  - [EnvironmentNetworkEgressAllowlist](https://ai.google.dev/api/interactions-api#Resource:EnvironmentNetworkEgressAllowlist)
  - [ToolChoiceConfig](https://ai.google.dev/api/interactions-api#Resource:ToolChoiceConfig)
  - [ImageContent](https://ai.google.dev/api/interactions-api#Resource:ImageContent)
  - [TextContent](https://ai.google.dev/api/interactions-api#Resource:TextContent)

The Gemini Interactions API allows developers to build generative AI applications using Gemini models. Gemini is our most capable model, built from the ground up to be multimodal. It can generalize and seamlessly understand, operate across, and combine different types of information including language, images, audio, video, and code. You can use the Gemini API for use cases like reasoning across text and images, content generation, dialogue agents, summarization and classification systems, and more.

[View as markdown](https://ai.google.dev/static/api/interactions.md.txt) [View the OpenAPI Spec](https://ai.google.dev/static/api/interactions.openapi.json)

API version:v1beta [v1](https://ai.google.dev/api/interactions-api-v1)

## CreateInteraction

post

https://generativelanguage.googleapis.com/v1beta/interactions


Creates a new interaction.

- [Request body](https://ai.google.dev/api/interactions-api#CreateInteraction.request_body)
- [Response](https://ai.google.dev/api/interactions-api#CreateInteraction.response)

### Request body

The request body structure depends on the interaction mode you choose:

AgentInteraction


Interaction for generating the completion using agents.

agentAgentOption (required)

The name of the \`Agent\` used for generating the interaction.

The agent to interact with.

#### Possible values

- `deep-research-pro-preview-12-2025`
Gemini Deep Research Agent

- `deep-research-preview-04-2026`
Gemini Deep Research Agent

- `deep-research-max-preview-04-2026`
Gemini Deep Research Max Agent

- `antigravity-preview-05-2026`
Use the Antigravity managed agent to perform multi-step tasks that require reasoning, file operations, and tool use.


agent\_configAntigravityAgentConfig or CodeMenderAgentConfig or DeepResearchAgentConfig or DynamicAgentConfig (optional)

Configuration parameters for the agent interaction.

backgroundboolean (optional)

Input only. Whether to run the model interaction in the background.

createdstring (required)

Required. Output only. The time at which the response was created in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).

environment[EnvironmentConfig](https://ai.google.dev/api/interactions-api#Resource:EnvironmentConfig) or string (optional)

The environment configuration for the interaction. Can be an object
specifying remote environment sources or a string referencing an existing
environment ID.

environment\_idstring (optional)

Output only. The environment ID for the interaction. Only populated if environment
config is set in the request.

idstring (required)

Required. Output only. A unique identifier for the interaction completion.

input[Content](https://ai.google.dev/api/interactions-api#Resource:Content) or array ( [Content](https://ai.google.dev/api/interactions-api#Resource:Content)) or array ( [Step](https://ai.google.dev/api/interactions-api#Resource:Step)) or string (optional)

The input for the interaction.

labelsobject (optional)

The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters
(Unicode codepoints) and can only contain lowercase letters, numeric
characters, underscores, and dashes. International characters are allowed.
Label values are optional. Label keys must start with a letter.

previous\_interaction\_idstring (optional)

The ID of the previous interaction, if any.

response\_format[ResponseFormat](https://ai.google.dev/api/interactions-api#Resource:ResponseFormat) or array ( [ResponseFormat](https://ai.google.dev/api/interactions-api#Resource:ResponseFormat)) (optional)

Enforces that the generated response is a JSON object that complies with
the JSON schema specified in this field.

safety\_settingsarray (SafetySetting) (optional)

Safety settings for the interaction.

A safety setting that affects the safety-blocking behavior.

A SafetySetting consists of a
harm category and a
threshold for that
category.

#### Fields

methodenum (string) (optional)

Optional. The method for blocking content. If not specified, the default
behavior is to use the probability score.

Possible
values:

- `severity`
The harm block method uses both probability and severity scores.

- `probability`
The harm block method uses the probability score.


thresholdenum (string) (optional)

Required. The threshold for blocking content. If the harm probability
exceeds this threshold, the content will be blocked.

Possible
values:

- `block_low_and_above`
Block content with a low harm probability or higher.

- `block_medium_and_above`
Block content with a medium harm probability or higher.

- `block_only_high`
Block content with a high harm probability.

- `block_none`
Do not block any content, regardless of its harm probability.

- `off`
Turn off the safety filter entirely.


typeHarmCategory (optional)

Required. The type of harm category to be blocked.

#### Possible values

- `hate_speech`
Content that promotes violence or incites hatred against individuals or
groups based on certain attributes.

- `dangerous_content`
Content that promotes, facilitates, or enables dangerous activities.

- `harassment`
Abusive, threatening, or content intended to bully, torment, or ridicule.

- `sexually_explicit`
Content that contains sexually explicit material.

- `civic_integrity`
Deprecated: Election filter is not longer supported.
The harm category is civic integrity.

- `image_hate`
Images that contain hate speech.

- `image_dangerous_content`
Images that contain dangerous content.

- `image_harassment`
Images that contain harassment.

- `image_sexually_explicit`
Images that contain sexually explicit content.

- `jailbreak`
Prompts designed to bypass safety filters.


service\_tierServiceTier (optional)

The service tier for the interaction.

#### Possible values

- `flex`
Flex service tier.

- `standard`
Standard service tier.

- `priority`
Priority service tier.

- `deferred`
Deferred service tier.


statusenum (string) (required)

Required. Output only. The status of the interaction.

Possible
values:

- `in_progress`
The interaction is in progress.

- `requires_action`
The interaction requires action/input from the user.

- `completed`
The interaction is completed.

- `failed`
The interaction failed.

- `cancelled`
The interaction was cancelled.

- `incomplete`
The interaction is completed, but contains incomplete results (e.g.
hitting max\_tokens).

- `budget_exceeded`
Deprecated: Token and execution budget exhaustion returns INCOMPLETE
(11).

- `queued`
The interaction is queued, waiting for processing (e.g. waiting for
off-peak capacity).


storeboolean (optional)

Input only. Whether to store the response and request for later retrieval.

streamboolean (optional)

Input only. Whether the interaction will be streamed.

system\_instructionstring (optional)

System instruction for the interaction.

toolsarray ( [Tool](https://ai.google.dev/api/interactions-api#Resource:Tool)) (optional)

A list of tool declarations the model may call during interaction.

updatedstring (required)

Required. Output only. The time at which the response was last updated in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).

webhook\_configWebhookConfig (optional)

Optional. Webhook configuration for receiving notifications when the
interaction completes.

Message for configuring webhook events for a request.

#### Fields

urisarray (string) (optional)

Optional. If set, these webhook URIs will be used for webhook events instead of the
registered webhooks.

user\_metadataobject (optional)

Optional. The user metadata that will be returned on each event emission to the
webhooks.

ModelInteraction


Interaction for generating the completion using models.

backgroundboolean (optional)

Input only. Whether to run the model interaction in the background.

createdstring (required)

Required. Output only. The time at which the response was created in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).

environment[EnvironmentConfig](https://ai.google.dev/api/interactions-api#Resource:EnvironmentConfig) or string (optional)

The environment configuration for the interaction. Can be an object
specifying remote environment sources or a string referencing an existing
environment ID.

environment\_idstring (optional)

Output only. The environment ID for the interaction. Only populated if environment
config is set in the request.

generation\_configGenerationConfig (optional)

Input only. Configuration parameters for the model interaction.

Configuration parameters for model interactions.

#### Fields

max\_output\_tokensinteger (optional)

The maximum number of tokens to include in the response.

seedinteger (optional)

Seed used in decoding for reproducibility.

speech\_configSpeakerConfig or array (SpeechConfig) (optional)

Optional. Speech and multi-speaker configuration.

Configuration for multi-speaker and speech generation.

#### Fields

speakersarray (SpeechConfig) (optional)

Individual speaker configurations.

The configuration for speech interaction.

#### Fields

languagestring (optional)

The language of the speech.

speakerstring (optional)

The speaker's name, it should match the speaker name given in the prompt.

voicestring (optional)

The voice of the speaker.

stop\_sequencesarray (string) (optional)

A list of character sequences that will stop output interaction.

thinking\_levelThinkingLevel (optional)

The level of thought tokens that the model should generate.

#### Possible values

- `minimal`
Little to no thinking.

- `low`
Low thinking level.

- `medium`
Medium thinking level.

- `high`
High thinking level.


thinking\_summariesThinkingSummaries (optional)

Whether to include thought summaries in the response.

#### Possible values

- `auto`
Auto thinking summaries.

- `none`
No thinking summaries.


tool\_choice[ToolChoiceConfig](https://ai.google.dev/api/interactions-api#Resource:ToolChoiceConfig) or enum (string) (optional)

The tool choice configuration.

Possible
values:

- `auto`
Auto tool choice.

- `any`
Any tool choice.

- `none`
No tool choice.

- `validated`
Validated tool choice.


transcription\_configTranscriptionConfig (optional)

Optional. Configuration for speech recognition (transcription). If present, ASR is
enabled.

Configuration for speech recognition (transcription).

#### Fields

custom\_vocabularyarray (string) (optional)

Optional. A list of custom vocabulary phrases to bias the speech recognition model
toward recognizing specific terms.

language\_codesarray (string) (optional)

Optional. BCP-47 language codes providing hints about the languages present in the
audio. If omitted or empty, defaults to automatic language detection.

modeTranscriptionMode or enum (string) (optional)

Discriminated transcription mode options or enum.

Configuration for transcription mode.

#### Possible Types

SmartTranscriptionMode

Configuration for smart transcription mode.

typeobject (required)

No description provided.

Always set to `"smart"`.

VerbatimTranscriptionMode

Configuration for verbatim transcription mode.

diarization\_modestring (optional)

Optional. Configures speaker diarization. Supported values: "speaker".

timestamp\_granularitiesarray (string) (optional)

Optional. The granularity of timestamps to include in the transcription output.
Supported values: "word". If empty, no timestamps are generated.

typeobject (required)

No description provided.

Always set to `"verbatim"`.

video\_configVideoConfig (optional)

Configuration for video generation.

Configuration options for video generation.

#### Fields

taskenum (string) (optional)

Optional task mode for video generation. If not specified, the model
automatically determines the appropriate mode based on the provided text
prompt and input media.

Possible
values:

- `text_to_video`
Generates video solely from a text prompt.

- `image_to_video`
Generates video from one or two source images. The first image defines
the starting frame, and the optional second image defines the ending
frame.

- `reference_to_video`
Generates video using reference media (such as images, audio, or video).

- `edit`
Modifies an existing input video.

- `extend`
Extends an existing input video.


idstring (required)

Required. Output only. A unique identifier for the interaction completion.

input[Content](https://ai.google.dev/api/interactions-api#Resource:Content) or array ( [Content](https://ai.google.dev/api/interactions-api#Resource:Content)) or array ( [Step](https://ai.google.dev/api/interactions-api#Resource:Step)) or string (optional)

The input for the interaction.

labelsobject (optional)

The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters
(Unicode codepoints) and can only contain lowercase letters, numeric
characters, underscores, and dashes. International characters are allowed.
Label values are optional. Label keys must start with a letter.

modelModelOption (required)

The name of the \`Model\` used for generating the interaction.

The model that will complete your prompt.\\n\\nSee \[models\](https://ai.google.dev/gemini-api/docs/models) for additional details.

#### Possible values

- `gemini-2.5-flash`
Our first hybrid reasoning model which supports a 1M token context window and has thinking budgets.

- `gemini-2.5-pro`
Our state-of-the-art multipurpose model, which excels at coding and complex reasoning tasks.

- `gemma-4-26b-a4b-it`
Gemma 4 26B A4B IT

- `gemma-4-31b-it`
Gemma 4 31B IT

- `gemini-flash-latest`
Latest release of Gemini Flash

- `gemini-flash-lite-latest`
Latest release of Gemini Flash-Lite

- `gemini-pro-latest`
Latest release of Gemini Pro

- `gemini-2.5-flash-lite`
Our smallest and most cost effective model, built for at scale usage.

- `gemini-2.5-flash-image`
Our native image generation model, optimized for speed, flexibility, and contextual understanding. Text input and output is priced the same as 2.5 Flash.

- `gemini-3-flash-preview`
Our most intelligent model built for speed, combining frontier intelligence with superior search and grounding.

- `gemini-3.1-pro-preview`
Our latest SOTA reasoning model with unprecedented depth and nuance, and powerful multimodal understanding and coding capabilities.

- `gemini-3.1-pro-preview-customtools`
Gemini 3.1 Pro Preview optimized for custom tool usage

- `gemini-3.1-flash-lite`
Our most cost-efficient model, optimized for high-volume agentic tasks, translation, and simple data processing.

- `gemini-3-pro-image`
Gemini 3 Pro Image

- `nano-banana-pro-preview`
Gemini 3 Pro Image Preview

- `gemini-3.1-flash-image`
Gemini 3.1 Flash Image.

- `gemini-3.1-flash-tts-preview`
Gemini 3.1 Flash TTS: Powerful, low-latency speech generation. Enjoy natural outputs, steerable prompts, and new expressive audio tags for precise narration control.

- `gemini-3.5-flash`
Our most intelligent model for sustained frontier performance in agentic and coding tasks.

- `gemini-3.6-flash`
Our most intelligent model for sustained frontier performance in agentic and coding tasks.

- `gemini-3.7-flash`
Our most intelligent model for sustained frontier performance in agentic and coding tasks.

- `gemini-3.8-flash`
Our most intelligent model for sustained frontier performance in agentic and coding tasks.

- `gemini-3.8-flash-tts`
Gemini 3.8 Flash TTS - Flagship TTS model for Voice Design and dual-speaker screenplay control. Prompt custom vocal personas, direct line-by-line delivery, and add vocal bursts.

- `gemini-3.8-flash-lite-tts`
Gemini 3.8 Flash Lite TTS - High-speed and cost-efficient, ideal for rapid dubbing, media localization, and high-throughput voice agents. Direct replacement for gemini-3.1-flash-tts-preview.

- `lyria-3-clip-preview`
Our low-latency, music generation model optimized for high-fidelity audio clips and precise rhythmic control.

- `lyria-3-pro-preview`
Our advanced, full-song generative model with deep compositional understanding, optimized for precise structural control and complex transitions across diverse musical styles.

- `gemini-robotics-er-1.6-preview`
Gemini Robotics-ER 1.6 Preview

- `gemini-robotics-er-2-preview`
Gemini Robotics Embodied Reasoning 2 Preview


previous\_interaction\_idstring (optional)

The ID of the previous interaction, if any.

response\_format[ResponseFormat](https://ai.google.dev/api/interactions-api#Resource:ResponseFormat) or array ( [ResponseFormat](https://ai.google.dev/api/interactions-api#Resource:ResponseFormat)) (optional)

Enforces that the generated response is a JSON object that complies with
the JSON schema specified in this field.

safety\_settingsarray (SafetySetting) (optional)

Safety settings for the interaction.

A safety setting that affects the safety-blocking behavior.

A SafetySetting consists of a
harm category and a
threshold for that
category.

#### Fields

methodenum (string) (optional)

Optional. The method for blocking content. If not specified, the default
behavior is to use the probability score.

Possible
values:

- `severity`
The harm block method uses both probability and severity scores.

- `probability`
The harm block method uses the probability score.


thresholdenum (string) (optional)

Required. The threshold for blocking content. If the harm probability
exceeds this threshold, the content will be blocked.

Possible
values:

- `block_low_and_above`
Block content with a low harm probability or higher.

- `block_medium_and_above`
Block content with a medium harm probability or higher.

- `block_only_high`
Block content with a high harm probability.

- `block_none`
Do not block any content, regardless of its harm probability.

- `off`
Turn off the safety filter entirely.


typeHarmCategory (optional)

Required. The type of harm category to be blocked.

#### Possible values

- `hate_speech`
Content that promotes violence or incites hatred against individuals or
groups based on certain attributes.

- `dangerous_content`
Content that promotes, facilitates, or enables dangerous activities.

- `harassment`
Abusive, threatening, or content intended to bully, torment, or ridicule.

- `sexually_explicit`
Content that contains sexually explicit material.

- `civic_integrity`
Deprecated: Election filter is not longer supported.
The harm category is civic integrity.

- `image_hate`
Images that contain hate speech.

- `image_dangerous_content`
Images that contain dangerous content.

- `image_harassment`
Images that contain harassment.

- `image_sexually_explicit`
Images that contain sexually explicit content.

- `jailbreak`
Prompts designed to bypass safety filters.


service\_tierServiceTier (optional)

The service tier for the interaction.

#### Possible values

- `flex`
Flex service tier.

- `standard`
Standard service tier.

- `priority`
Priority service tier.

- `deferred`
Deferred service tier.


statusenum (string) (required)

Required. Output only. The status of the interaction.

Possible
values:

- `in_progress`
The interaction is in progress.

- `requires_action`
The interaction requires action/input from the user.

- `completed`
The interaction is completed.

- `failed`
The interaction failed.

- `cancelled`
The interaction was cancelled.

- `incomplete`
The interaction is completed, but contains incomplete results (e.g.
hitting max\_tokens).

- `budget_exceeded`
Deprecated: Token and execution budget exhaustion returns INCOMPLETE
(11).

- `queued`
The interaction is queued, waiting for processing (e.g. waiting for
off-peak capacity).


storeboolean (optional)

Input only. Whether to store the response and request for later retrieval.

streamboolean (optional)

Input only. Whether the interaction will be streamed.

system\_instructionstring (optional)

System instruction for the interaction.

toolsarray ( [Tool](https://ai.google.dev/api/interactions-api#Resource:Tool)) (optional)

A list of tool declarations the model may call during interaction.

updatedstring (required)

Required. Output only. The time at which the response was last updated in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).

webhook\_configWebhookConfig (optional)

Optional. Webhook configuration for receiving notifications when the
interaction completes.

Message for configuring webhook events for a request.

#### Fields

urisarray (string) (optional)

Optional. If set, these webhook URIs will be used for webhook events instead of the
registered webhooks.

user\_metadataobject (optional)

Optional. The user metadata that will be returned on each event emission to the
webhooks.

### Response

Returns an [Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction) resource.

[Simple Request](https://ai.google.dev/api/interactions-api#simple-request)[Multi-turn](https://ai.google.dev/api/interactions-api#multi-turn)[Image Input](https://ai.google.dev/api/interactions-api#image-input)[Function Calling](https://ai.google.dev/api/interactions-api#function-calling)[Deep Research](https://ai.google.dev/api/interactions-api#deep-research)[Antigravity Agent](https://ai.google.dev/api/interactions-api#antigravity-agent)[Reuse Environment](https://ai.google.dev/api/interactions-api#reuse-environment)[With Sources](https://ai.google.dev/api/interactions-api#with-sources)[Custom Agent](https://ai.google.dev/api/interactions-api#custom-agent)More

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Hello, how are you?"
  }'
```

```python
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Hello, how are you?",
)
print(interaction.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  input: 'Hello, how are you?',
});
console.log(interaction.output_text);
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;

Client client = new Client();
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.6-flash")
        .input(InteractionsInput.of("Hello, how are you?"))
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.outputText().orElse(""));
```

#### Example Response

```
{
  "created": "2025-11-26T12:25:15Z",
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-3.6-flash",
  "object": "interaction",
  "status": "completed",
  "steps": [\
    {\
      "type": "model_output",\
      "content": [\
        {\
          "type": "text",\
          "text": "Hello! I'm functioning perfectly and ready to assist you.\n\nHow are you doing today?"\
        }\
      ]\
    }\
  ],
  "updated": "2025-11-26T12:25:15Z",
  "usage": {
    "input_tokens_by_modality": [\
      {\
        "modality": "text",\
        "tokens": 7\
      }\
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 7,
    "total_output_tokens": 20,
    "total_thought_tokens": 22,
    "total_tokens": 49,
    "total_tool_use_tokens": 0
  }
}
```

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [\
      { "type": "user_input", "content": [{ "type": "text", "text": "Hello!" }] },\
      { "type": "model_output", "content": [{ "type": "text", "text": "Hi there! How can I help you today?" }] },\
      { "type": "user_input", "content": [{ "type": "text", "text": "What is the capital of France?" }] }\
    ]
  }'
```

```python
from google import genai

client = genai.Client()
response = client.interactions.create(
    model="gemini-3.6-flash",
    input=[\
        {\
            "type": "user_input",\
            "content": [{"type": "text", "text": "Hello!"}],\
        },\
        {\
            "type": "model_output",\
            "content": [{\
                "type": "text",\
                "text": "Hi there! How can I help you today?",\
            }],\
        },\
        {\
            "type": "user_input",\
            "content": [\
                {"type": "text", "text": "What is the capital of France?"}\
            ],\
        },\
    ],
)
print(response.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  input: [\
    {type: 'user_input', content: [{type: 'text', text: 'Hello'}]},\
    {\
      type: 'model_output',\
      content: [\
        {type: 'text', text: 'Hi there! How can I help you today?'},\
      ],\
    },\
    {\
      type: 'user_input',\
      content: [{type: 'text', text: 'What is the capital of France?'}],\
    },\
  ],
});
console.log(interaction.output_text);
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.UserInputStep;

Client client = new Client();
List
```

#### Example Response

```
{
  "created": "2025-11-26T12:22:47Z",
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-3.6-flash",
  "object": "interaction",
  "status": "completed",
  "steps": [\
    {\
      "type": "model_output",\
      "content": [\
        {\
          "type": "text",\
          "text": "The capital of France is Paris."\
        }\
      ]\
    }\
  ],
  "updated": "2025-11-26T12:22:47Z",
  "usage": {
    "input_tokens_by_modality": [\
      {\
        "modality": "text",\
        "tokens": 50\
      }\
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 50,
    "total_output_tokens": 10,
    "total_thought_tokens": 0,
    "total_tokens": 60,
    "total_tool_use_tokens": 0
  }
}
```

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [\
      {\
        "type": "text",\
        "text": "What is in this picture?"\
      },\
      {\
        "type": "image",\
        "data": "BASE64_ENCODED_IMAGE",\
        "mime_type": "image/png"\
      }\
    ]
  }'
```

```python
from google import genai

client = genai.Client()
response = client.interactions.create(
    model="gemini-3.6-flash",
    input=[\
        {"type": "text", "text": "What is in this picture?"},\
        {\
            "type": "image",\
            "data": "BASE64_ENCODED_IMAGE",\
            "mime_type": "image/png",\
        },\
    ],
)
print(response.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  input: [\
    {type: 'text', text: 'What is in this picture?'},\
    {type: 'image', data: 'BASE64_ENCODED_IMAGE', mime_type: 'image/png'},\
  ],
});
console.log(interaction.output_text);
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.TextContent;

Client client = new Client();
List
```

#### Example Response

```
{
  "created": "2025-11-26T12:22:47Z",
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-3.6-flash",
  "object": "interaction",
  "status": "completed",
  "steps": [\
    {\
      "type": "model_output",\
      "content": [\
        {\
          "type": "text",\
          "text": "A white humanoid robot with glowing blue eyes stands holding a red skateboard."\
        }\
      ]\
    }\
  ],
  "updated": "2025-11-26T12:22:47Z",
  "usage": {
    "input_tokens_by_modality": [\
      {\
        "modality": "text",\
        "tokens": 10\
      },\
      {\
        "modality": "image",\
        "tokens": 258\
      }\
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 268,
    "total_output_tokens": 20,
    "total_thought_tokens": 0,
    "total_tokens": 288,
    "total_tool_use_tokens": 0
  }
}
```

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "tools": [\
      {\
        "type": "function",\
        "name": "get_weather",\
        "description": "Get the current weather in a given location",\
        "parameters": {\
          "type": "object",\
          "properties": {\
            "location": {\
              "type": "string",\
              "description": "The city and state, e.g. San Francisco, CA"\
            }\
          },\
          "required": [\
            "location"\
          ]\
        }\
      }\
    ],
    "input": "What is the weather like in Boston, MA?"
  }'
```

```python
from google import genai

client = genai.Client()
response = client.interactions.create(
    model="gemini-3.6-flash",
    tools=[{\
        "type": "function",\
        "name": "get_weather",\
        "description": "Get the current weather in a given location",\
        "parameters": {\
            "type": "object",\
            "properties": {\
                "location": {\
                    "type": "string",\
                    "description": (\
                        "The city and state, e.g. San Francisco, CA"\
                    ),\
                }\
            },\
            "required": ["location"],\
        },\
    }],
    input="What is the weather like in Boston, MA?",
)
print(response.steps[-1])
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  tools: [\
    {\
      type: 'function',\
      name: 'get_weather',\
      description: 'Get the current weather in a given location',\
      parameters: {\
        type: 'object',\
        properties: {\
          location: {\
            type: 'string',\
            description: 'The city and state, e.g. San Francisco, CA',\
          },\
        },\
        required: ['location'],\
      },\
    },\
  ],
  input: 'What is the weather like in Boston, MA?',
});
console.log(interaction.steps.at(-1));
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Step;

Client client = new Client();
Map
```

#### Example Response

```
{
  "created": "2025-11-26T12:22:47Z",
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-3.6-flash",
  "object": "interaction",
  "status": "requires_action",
  "steps": [\
    {\
      "name": "get_weather",\
      "type": "function_call",\
      "arguments": {\
        "location": "Boston, MA"\
      },\
      "id": "gth23981"\
    }\
  ],
  "updated": "2025-11-26T12:22:47Z",
  "usage": {
    "input_tokens_by_modality": [\
      {\
        "modality": "text",\
        "tokens": 100\
      }\
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 100,
    "total_output_tokens": 25,
    "total_thought_tokens": 0,
    "total_tokens": 125,
    "total_tool_use_tokens": 50
  }
}
```

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "agent": "deep-research-pro-preview-12-2025",
    "input": "Find a cure to cancer",
    "background": true
  }'
```

```python
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    agent="deep-research-pro-preview-12-2025",
    input="find a cure to cancer",
    background=True,
)
print(interaction.status)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  agent: 'deep-research-pro-preview-12-2025',
  input: 'find a cure to cancer',
  background: true,
});
console.log(interaction.status);
```

```java
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;

Client client = new Client();
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent(AgentOption.of("deep-research-pro-preview-12-2025"))
        .input(InteractionsInput.of("find a cure to cancer"))
        .background(true)
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.status().map(InteractionStatus::value).orElse(""));
```

#### Example Response

```
{
  "agent": "deep-research-pro-preview-12-2025",
  "created": "2025-11-26T12:22:47Z",
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "object": "interaction",
  "status": "completed",
  "steps": [\
    {\
      "type": "model_output",\
      "content": [\
        {\
          "type": "text",\
          "text": "Here is a comprehensive research report on the current state of cancer research..."\
        }\
      ]\
    }\
  ],
  "updated": "2025-11-26T12:22:47Z",
  "usage": {
    "input_tokens_by_modality": [\
      {\
        "modality": "text",\
        "tokens": 20\
      }\
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 20,
    "total_output_tokens": 1000,
    "total_thought_tokens": 500,
    "total_tokens": 1520,
    "total_tool_use_tokens": 0
  }
}
```

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save results as a markdown file.",
    "environment": "remote"
  }'
```

```python
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=(
        "Read Hacker News, summarize the top 5 stories, and save results as"
        " a markdown file."
    ),
    environment="remote",
)
print(interaction.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  agent: 'antigravity-preview-05-2026',
  input:
    'Read Hacker News, summarize the top 5 stories, and save results as a markdown file.',
  environment: 'remote',
});
console.log(interaction.output_text);
```

```java
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;

Client client = new Client();
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent(AgentOption.of("antigravity-preview-05-2026"))
        .input(
            InteractionsInput.of(
                "Read Hacker News, summarize the top 5 stories, and save results as a markdown"
                    + " file."))
        .environment(CreateAgentInteractionEnvironment.of("remote"))
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.outputText().orElse(""));
```

#### Example Response

```
{
  "agent": "antigravity-preview-05-2026",
  "created": "2025-11-26T12:22:47Z",
  "environment_id": "env_abc123",
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "object": "interaction",
  "status": "completed",
  "steps": [\
    {\
      "type": "model_output",\
      "content": [\
        {\
          "type": "text",\
          "text": "I've summarized the top 5 Hacker News stories and saved the results to /workspace/summary.md."\
        }\
      ]\
    }\
  ],
  "updated": "2025-11-26T12:22:47Z",
  "usage": {
    "input_tokens_by_modality": [\
      {\
        "modality": "text",\
        "tokens": 50\
      }\
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 50,
    "total_output_tokens": 500,
    "total_thought_tokens": 200,
    "total_tokens": 750,
    "total_tool_use_tokens": 0
  }
}
```

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
# Step 1: Create an interaction with a fresh remote environment.
RESPONSE=$(curl -s -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Write a hello world script at /workspace/hello.py.",
    "environment": "remote"
  }')
INTERACTION_ID=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")
ENV_ID=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin)['environment_id'])")

# Step 2: Reuse the same environment in a follow-up interaction.
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": \"Modify the script to accept a name argument and greet the user.\",
    \"environment\": \"$ENV_ID\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
  }"
```

```python
from google import genai

client = genai.Client()

# Step 1: Create an interaction with a fresh remote environment.
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a hello world script at /workspace/hello.py.",
    environment="remote",
)
print(f"Environment ID: {interaction.environment_id}")

# Step 2: Reuse the same environment in a follow-up interaction.
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Modify the script to accept a name argument and greet the user.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)
print(interaction_2.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

// Step 1: Create an interaction with a fresh remote environment.
const interaction = await ai.interactions.create({
  agent: 'antigravity-preview-05-2026',
  input: 'Write a hello world script at /workspace/hello.py.',
  environment: 'remote',
});
console.log(`Environment ID: ${interaction.environment_id}`);

// Step 2: Reuse the same environment in a follow-up interaction.
const interaction2 = await ai.interactions.create({
  agent: 'antigravity-preview-05-2026',
  input: 'Modify the script to accept a name argument and greet the user.',
  environment: interaction.environment_id,
  previous_interaction_id: interaction.id,
});
console.log(interaction2.output_text);
```

```java
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.environments.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Step;

Client client = new Client();

// Step 1: Create an interaction with a fresh remote environment.
CreateAgentInteraction params1 =
    CreateAgentInteraction.builder()
        .agent(AgentOption.of("antigravity-preview-05-2026"))
        .input(InteractionsInput.of("Write a hello world script at /workspace/hello.py."))
        .environment(CreateAgentInteractionEnvironment.of("remote"))
        .build();
CreateInteractionResponse response1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1));
Interaction interaction1 =
    response1.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println("Environment ID: " + interaction1.environmentId().orElse(""));

// Step 2: Reuse the same environment in a follow-up interaction.
CreateAgentInteraction params2 =
    CreateAgentInteraction.builder()
        .agent(AgentOption.of("antigravity-preview-05-2026"))
        .input(
            InteractionsInput.of(
                "Modify the script to accept a name argument and greet the user."))
        .environment(
            CreateAgentInteractionEnvironment.of(interaction1.environmentId().orElse("")))
        .previousInteractionId(interaction1.id().orElse(null))
        .build();
CreateInteractionResponse response2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2));
Interaction interaction2 =
    response2.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction2.outputText().orElse(""));
```

#### Example Response

```
{
  "agent": "antigravity-preview-05-2026",
  "created": "2025-11-26T12:23:00Z",
  "environment_id": "env_abc123",
  "id": "v1_Chd2ZTJhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejAxMjM0NTY3ODkwMTIzNDU2Nzg",
  "object": "interaction",
  "status": "completed",
  "steps": [\
    {\
      "type": "model_output",\
      "content": [\
        {\
          "type": "text",\
          "text": "I've updated /workspace/hello.py to accept a name argument and greet the user."\
        }\
      ]\
    }\
  ],
  "updated": "2025-11-26T12:23:00Z",
  "usage": {
    "input_tokens_by_modality": [\
      {\
        "modality": "text",\
        "tokens": 80\
      }\
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 80,
    "total_output_tokens": 200,
    "total_thought_tokens": 100,
    "total_tokens": 380,
    "total_tool_use_tokens": 0
  }
}
```

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "List all files under /workspace and summarize what you find.",
    "environment": {
      "type": "remote",
      "sources": [\
        {\
          "type": "repository",\
          "source": "https://github.com/octocat/Spoon-Knife",\
          "target": "/workspace/repo"\
        },\
        {\
          "type": "inline",\
          "content": "Focus on Python files only.",\
          "target": "/workspace/notes.txt"\
        }\
      ]
    }
  }'
```

```python
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="List all files under /workspace and summarize what you find.",
    environment={
        "type": "remote",
        "sources": [\
            {\
                "type": "repository",\
                "source": "https://github.com/octocat/Spoon-Knife",\
                "target": "/workspace/repo",\
            },\
            {\
                "type": "inline",\
                "content": "Focus on Python files only.",\
                "target": "/workspace/notes.txt",\
            },\
        ],
    },
)
print(interaction.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  agent: 'antigravity-preview-05-2026',
  input: 'List all files under /workspace and summarize what you find.',
  environment: {
    type: 'remote',
    sources: [\
      {\
        type: 'repository',\
        source: 'https://github.com/octocat/Spoon-Knife',\
        target: '/workspace/repo',\
      },\
      {\
        type: 'inline',\
        content: 'Focus on Python files only.',\
        target: '/workspace/notes.txt',\
      },\
    ],
  },
});
console.log(interaction.output_text);
```

```java
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.environments.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;

Client client = new Client();
com.google.genai.gaos.models.interactions.Environment env =
    com.google.genai.gaos.models.interactions.Environment.builder()
        .sources(
            List.of(
                Source.builder()
                    .type(SourceType.REPOSITORY)
                    .source("https://github.com/octocat/Spoon-Knife")
                    .target("/workspace/repo")
                    .build(),
                Source.builder()
                    .type(SourceType.INLINE)
                    .content("Focus on Python files only.")
                    .target("/workspace/notes.txt")
                    .build()))
        .build();
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent(AgentOption.of("antigravity-preview-05-2026"))
        .input(
            InteractionsInput.of(
                "List all files under /workspace and summarize what you find."))
        .environment(CreateAgentInteractionEnvironment.of(env))
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.outputText().orElse(""));
```

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
# Step 1: Create a custom agent.
curl -X POST https://generativelanguage.googleapis.com/v1beta/agents \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "code-reviewer",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a senior code reviewer. Check every file for bugs, style issues, and security vulnerabilities.",
    "base_environment": {
      "type": "remote",
      "sources": [{\
        "type": "repository",\
        "source": "https://github.com/octocat/Spoon-Knife",\
        "target": "/workspace/repo"\
      }]
    }
  }'

# Step 2: Use the custom agent.
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "agent": "code-reviewer",
    "input": "Review the latest changes in /workspace/repo/src and file a summary.",
    "environment": "remote"
  }'
```

```python
import uuid
from google import genai

client = genai.Client()

# Step 1: Create a custom agent.
agent_id = f"code-reviewer-{uuid.uuid4().hex[:8]}"
client.agents.create(
    id=agent_id,
    base_agent="antigravity-preview-05-2026",
    system_instruction=(
        "You are a senior code reviewer. Check every file for bugs, style"
        " issues, and security vulnerabilities."
    ),
    base_environment={
        "type": "remote",
        "sources": [{\
            "type": "repository",\
            "source": "https://github.com/octocat/Spoon-Knife",\
            "target": "/workspace/repo",\
        }],
    },
)

# Step 2: Use the custom agent.
result = client.interactions.create(
    agent=agent_id,
    input=(
        "Review the latest changes in /workspace/repo/src and file a"
        " summary."
    ),
    environment="remote",
)
print(result.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

// Step 1: Create a custom agent.
const agentId = `code-reviewer-${crypto.randomUUID().slice(0, 8)}`;
await ai.agents.create({
  id: agentId,
  base_agent: 'antigravity-preview-05-2026',
  system_instruction:
    'You are a senior code reviewer. Check every file for bugs, style issues, and security vulnerabilities.',
  base_environment: {
    type: 'remote',
    sources: [\
      {\
        type: 'repository',\
        source: 'https://github.com/octocat/Spoon-Knife',\
        target: '/workspace/repo',\
      },\
    ],
  },
});

// Step 2: Use the custom agent.
const result = await ai.interactions.create({
  agent: agentId,
  input:
    'Review the latest changes in /workspace/repo/src and file a summary.',
  environment: 'remote',
});
console.log(result.output_text);
```

```java
import com.google.genai.gaos.models.agents.Agent;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.agents.BaseEnvironment;
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.environments.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Step;

Client client = new Client();

// Step 1: Create a custom agent.
String agentId = "code-reviewer-" + UUID.randomUUID().toString().substring(0, 8);
com.google.genai.gaos.models.interactions.Environment baseEnv =
    com.google.genai.gaos.models.interactions.Environment.builder()
        .sources(
            List.of(
                Source.builder()
                    .type(SourceType.REPOSITORY)
                    .source("https://github.com/octocat/Spoon-Knife")
                    .target("/workspace/repo")
                    .build()))
        .build();
Agent customAgent =
    Agent.builder()
        .id(agentId)
        .baseAgent("antigravity-preview-05-2026")
        .systemInstruction(
            "You are a senior code reviewer. Check every file for bugs, style issues, and"
                + " security vulnerabilities.")
        .baseEnvironment(BaseEnvironment.of(baseEnv))
        .build();
client.agents.create(customAgent);

// Step 2: Use the custom agent.
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent(AgentOption.of(agentId))
        .input(
            InteractionsInput.of(
                "Review the latest changes in /workspace/repo/src and file a summary."))
        .environment(CreateAgentInteractionEnvironment.of("remote"))
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.outputText().orElse(""));
```

## cancelInteractionById

post

https://generativelanguage.googleapis.com/v1beta/interactions/{interactionsId}/cancel


Cancels an interaction by id. This only applies to background interactions
that are still running.

- [Path / Query parameters](https://ai.google.dev/api/interactions-api#cancelInteractionById.PATH_PARAMETERS)
- [Response](https://ai.google.dev/api/interactions-api#cancelInteractionById.response)

### Path / Query Parameters

interactionsIdstring (required)

Required. The name of the interaction to cancel.

### Response

Returns an [Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction) resource.

[Cancel](https://ai.google.dev/api/interactions-api#cancel)More

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

```python
from google import genai

client = genai.Client()

# Start a background interaction so it stays in-progress.
created = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a long essay about the history of computing.",
    tools=[{"type": "computer_use"}],
    background=True,
)

# Cancel the in-progress interaction.
interaction = client.interactions.cancel(id=created.id)
print(interaction.status)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

// Start a background interaction so it stays in-progress.
const created = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  input: 'Write a long essay about the history of computing.',
  tools: [{type: 'computer_use'}],
  background: true,
});

// Cancel the in-progress interaction.
const interaction = await ai.interactions.cancel(created.id);
console.log(interaction.status);
```

```java
import com.google.genai.gaos.models.operations.CancelInteractionByIdResponse;
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;

Client client = new Client();

// Start a background interaction so it stays in-progress.
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.6-flash")
        .input(InteractionsInput.of("Write a long essay about the history of computing."))
        .tools(List.of(new ComputerUse()))
        .background(true)
        .build();
CreateInteractionResponse created =
    client.interactions.create(CreateInteractionRequestBody.of(params));
String interactionId = created.interaction().flatMap(Interaction::id).orElseThrow();

// Cancel the in-progress interaction.
CancelInteractionByIdResponse cancelResponse = client.interactions.cancel(interactionId);
Interaction interaction =
    cancelResponse
        .interaction()
        .orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.status().map(InteractionStatus::value).orElse(""));
```

## getInteractionById

get

https://generativelanguage.googleapis.com/v1beta/interactions/{interactionsId}


Retrieves the full details of a single interaction based on its
\`Interaction.id\`.

- [Path / Query parameters](https://ai.google.dev/api/interactions-api#getInteractionById.PATH_PARAMETERS)
- [Response](https://ai.google.dev/api/interactions-api#getInteractionById.response)

### Path / Query Parameters

include\_inputboolean (optional)

If true, includes the input in the response.

interactionsIdstring (required)

Required. The name of the interaction to retrieve.

last\_event\_idstring (optional)

If set, resumes the interaction stream from the chunk after the event
marked by the event id. Can only be used if \`stream\` is true.

streamboolean (optional)

If true, streams the interaction events as Server-Sent Events.

### Response

Returns an [Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction) resource.

[Get Interaction](https://ai.google.dev/api/interactions-api#get-interaction)More

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
```

```python
from google import genai

client = genai.Client()

interaction = client.interactions.get(id=created.id)
print(interaction.status)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.get(created.id);
console.log(interaction.status);
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.operations.GetInteractionByIdResponse;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;

Client client = new Client();

GetInteractionByIdResponse getResponse =
    client.interactions.get(new GetInteractionByIdRequest(interactionId));
Interaction interaction =
    getResponse
        .interaction()
        .orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.status().map(InteractionStatus::value).orElse(""));
```

#### Example Response

```
{
  "created": "2025-11-26T12:25:15Z",
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-3.6-flash",
  "object": "interaction",
  "status": "completed",
  "steps": [\
    {\
      "type": "model_output",\
      "content": [\
        {\
          "type": "text",\
          "text": "I'm doing great, thank you for asking! How can I help you today?"\
        }\
      ]\
    }\
  ],
  "updated": "2025-11-26T12:25:15Z"
}
```

## deleteInteraction

delete

https://generativelanguage.googleapis.com/v1beta/interactions/{interactionsId}


Deletes the interaction by id.

- [Path / Query parameters](https://ai.google.dev/api/interactions-api#deleteInteraction.PATH_PARAMETERS)
- [Response](https://ai.google.dev/api/interactions-api#deleteInteraction.response)

### Path / Query Parameters

interactionsIdstring (required)

Required. The name of the interaction to delete.

### Response

If successful, the response is empty.

[Delete](https://ai.google.dev/api/interactions-api#delete)More

Google AI for Developers

#### Example Request

RESTPythonJavaScriptJava

```sh
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

```python
from google import genai

client = genai.Client()

client.interactions.delete(id=created.id)
print("Interaction deleted successfully.")
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

await ai.interactions.delete(created.id);
console.log('Interaction deleted successfully.');
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Interaction;

Client client = new Client();

client.interactions.delete(interactionId);
System.out.println("Interaction deleted successfully.");
```

## Resources

### Interaction

The Interaction resource.

#### Fields

agentAgentOption (optional)

The name of the \`Agent\` used for generating the interaction.

The agent to interact with.

#### Possible values

- `deep-research-pro-preview-12-2025`
Gemini Deep Research Agent

- `deep-research-preview-04-2026`
Gemini Deep Research Agent

- `deep-research-max-preview-04-2026`
Gemini Deep Research Max Agent

- `antigravity-preview-05-2026`
Use the Antigravity managed agent to perform multi-step tasks that require reasoning, file operations, and tool use.


agent\_configobject (optional)

Configuration parameters for the agent interaction.

#### Possible Types

Polymorphic discriminator: `type`

AntigravityAgentConfig

Configuration for the Antigravity agent runtime.
Provides server-side control over the agent's execution environment
and tool configuration.

max\_total\_tokensstring (optional)

Max total tokens for the agent run.

modelstring (optional)

The model to use for agent reasoning.

typeobject (required)

No description provided.

Always set to `"antigravity"`.

CodeMenderAgentConfig

Configuration for the CodeMender agent.

find\_requestFindRequest (optional)

Parameters for finding vulnerabilities.

Request parameters specific to FIND sessions, used for discovering
vulnerabilities in a codebase.

#### Fields

descriptionstring (optional)

Additional context or custom instructions provided by the user to guide
the vulnerability analysis.

finding\_idstring (optional)

The identifier of a specific finding to verify. This is primarily used in
VERIFY mode to focus the agent's execution-based validation on a single
vulnerability.

modeenum (string) (optional)

The mode of the find session.

Possible
values:

- `scan`
Fast scan using only the initial classifier.

- `verify`
Performs classification followed by detailed investigation.


source\_filesarray (FileContent) (optional)

A list of source files to provide as context for the scan.

Content of a single file in the codebase.

#### Fields

contentstring (optional)

The UTF-8 encoded text content of the file.

pathstring (optional)

The relative path of the file from the project root.

fix\_requestFixRequest (optional)

Parameters for fixing vulnerabilities.

Request parameters specific to FIX sessions, used for generating and
validating security patches.

#### Fields

descriptionstring (optional)

Additional context or custom instructions provided by the user to guide
the patch generation process.

finding\_idstring (optional)

The identifier of the specific security finding to be remediated. This ID
maps to a previously discovered vulnerability.

source\_filesarray (FileContent) (optional)

A list of source files providing context for the remediation. These files
are typically the ones containing the identified vulnerability.

Content of a single file in the codebase.

#### Fields

contentstring (optional)

The UTF-8 encoded text content of the file.

pathstring (optional)

The relative path of the file from the project root.

modelstring (optional)

The name of the model to use for the CodeMender agent. One
CodeMender session will only use one model.

session\_configSessionConfig (optional)

Optional session-specific configurations to override default agent
behavior.

The configuration of CodeMender sessions.

#### Fields

max\_roundsinteger (optional)

The maximum number of interaction rounds the agent is allowed to perform
before reaching a timeout.

session\_idstring (optional)

Parameter for grouping multiple interactions that belong to
the same CodeMender session.

typeobject (required)

No description provided.

Always set to `"code-mender"`.

DeepResearchAgentConfig

Configuration for the Deep Research agent.

collaborative\_planningboolean (optional)

Enables human-in-the-loop planning for the Deep Research agent. If set to
true, the Deep Research agent will provide a research plan in its response.
The agent will then proceed only if the user confirms the plan in the next
turn.

enable\_bigquery\_toolboolean (optional)

Enables bigquery tool for the Deep Research agent.

thinking\_summariesThinkingSummaries (optional)

Whether to include thought summaries in the response.

#### Possible values

- `auto`
Auto thinking summaries.

- `none`
No thinking summaries.


typeobject (required)

No description provided.

Always set to `"deep-research"`.

visualizationenum (string) (optional)

Whether to include visualizations in the response.

Possible
values:

- `off`
Do not include visualizations.

- `auto`
Automatically include visualizations.


DynamicAgentConfig

Configuration for dynamic agents.

typeobject (required)

No description provided.

Always set to `"dynamic"`.

createdstring (optional)

Required. Output only. The time at which the response was created in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).

environment[EnvironmentConfig](https://ai.google.dev/api/interactions-api#Resource:EnvironmentConfig) or string (optional)

The environment configuration for the interaction. Can be an object
specifying remote environment sources or a string referencing an existing
environment ID.

environment\_idstring (optional)

Output only. The environment ID for the interaction. Only populated if environment
config is set in the request.

errorsarray (Error) (optional)

Output only. Diagnostic faults / platform errors recorded on the interaction.

Error message from an interaction.

#### Fields

codestring (optional)

A URI that identifies the error type.

messagestring (optional)

A human-readable error message.

idstring (optional)

Required. Output only. A unique identifier for the interaction completion.

_Defaults to: ``_

input[Content](https://ai.google.dev/api/interactions-api#Resource:Content) or array ( [Content](https://ai.google.dev/api/interactions-api#Resource:Content)) or array ( [Step](https://ai.google.dev/api/interactions-api#Resource:Step)) or string (optional)

The input for the interaction.

labelsobject (optional)

The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters
(Unicode codepoints) and can only contain lowercase letters, numeric
characters, underscores, and dashes. International characters are allowed.
Label values are optional. Label keys must start with a letter.

modelModelOption (optional)

The name of the \`Model\` used for generating the interaction.

The model that will complete your prompt.\\n\\nSee \[models\](https://ai.google.dev/gemini-api/docs/models) for additional details.

#### Possible values

- `gemini-2.5-flash`
Our first hybrid reasoning model which supports a 1M token context window and has thinking budgets.

- `gemini-2.5-pro`
Our state-of-the-art multipurpose model, which excels at coding and complex reasoning tasks.

- `gemma-4-26b-a4b-it`
Gemma 4 26B A4B IT

- `gemma-4-31b-it`
Gemma 4 31B IT

- `gemini-flash-latest`
Latest release of Gemini Flash

- `gemini-flash-lite-latest`
Latest release of Gemini Flash-Lite

- `gemini-pro-latest`
Latest release of Gemini Pro

- `gemini-2.5-flash-lite`
Our smallest and most cost effective model, built for at scale usage.

- `gemini-2.5-flash-image`
Our native image generation model, optimized for speed, flexibility, and contextual understanding. Text input and output is priced the same as 2.5 Flash.

- `gemini-3-flash-preview`
Our most intelligent model built for speed, combining frontier intelligence with superior search and grounding.

- `gemini-3.1-pro-preview`
Our latest SOTA reasoning model with unprecedented depth and nuance, and powerful multimodal understanding and coding capabilities.

- `gemini-3.1-pro-preview-customtools`
Gemini 3.1 Pro Preview optimized for custom tool usage

- `gemini-3.1-flash-lite`
Our most cost-efficient model, optimized for high-volume agentic tasks, translation, and simple data processing.

- `gemini-3-pro-image`
Gemini 3 Pro Image

- `nano-banana-pro-preview`
Gemini 3 Pro Image Preview

- `gemini-3.1-flash-image`
Gemini 3.1 Flash Image.

- `gemini-3.1-flash-tts-preview`
Gemini 3.1 Flash TTS: Powerful, low-latency speech generation. Enjoy natural outputs, steerable prompts, and new expressive audio tags for precise narration control.

- `gemini-3.5-flash`
Our most intelligent model for sustained frontier performance in agentic and coding tasks.

- `gemini-3.6-flash`
Our most intelligent model for sustained frontier performance in agentic and coding tasks.

- `gemini-3.7-flash`
Our most intelligent model for sustained frontier performance in agentic and coding tasks.

- `gemini-3.8-flash`
Our most intelligent model for sustained frontier performance in agentic and coding tasks.

- `gemini-3.8-flash-tts`
Gemini 3.8 Flash TTS - Flagship TTS model for Voice Design and dual-speaker screenplay control. Prompt custom vocal personas, direct line-by-line delivery, and add vocal bursts.

- `gemini-3.8-flash-lite-tts`
Gemini 3.8 Flash Lite TTS - High-speed and cost-efficient, ideal for rapid dubbing, media localization, and high-throughput voice agents. Direct replacement for gemini-3.1-flash-tts-preview.

- `lyria-3-clip-preview`
Our low-latency, music generation model optimized for high-fidelity audio clips and precise rhythmic control.

- `lyria-3-pro-preview`
Our advanced, full-song generative model with deep compositional understanding, optimized for precise structural control and complex transitions across diverse musical styles.

- `gemini-robotics-er-1.6-preview`
Gemini Robotics-ER 1.6 Preview

- `gemini-robotics-er-2-preview`
Gemini Robotics Embodied Reasoning 2 Preview


previous\_interaction\_idstring (optional)

The ID of the previous interaction, if any.

response\_format[ResponseFormat](https://ai.google.dev/api/interactions-api#Resource:ResponseFormat) or array ( [ResponseFormat](https://ai.google.dev/api/interactions-api#Resource:ResponseFormat)) (optional)

Enforces that the generated response is a JSON object that complies with
the JSON schema specified in this field.

safety\_settingsarray (SafetySetting) (optional)

Safety settings for the interaction.

A safety setting that affects the safety-blocking behavior.

A SafetySetting consists of a
harm category and a
threshold for that
category.

#### Fields

methodenum (string) (optional)

Optional. The method for blocking content. If not specified, the default
behavior is to use the probability score.

Possible
values:

- `severity`
The harm block method uses both probability and severity scores.

- `probability`
The harm block method uses the probability score.


thresholdenum (string) (optional)

Required. The threshold for blocking content. If the harm probability
exceeds this threshold, the content will be blocked.

Possible
values:

- `block_low_and_above`
Block content with a low harm probability or higher.

- `block_medium_and_above`
Block content with a medium harm probability or higher.

- `block_only_high`
Block content with a high harm probability.

- `block_none`
Do not block any content, regardless of its harm probability.

- `off`
Turn off the safety filter entirely.


typeHarmCategory (optional)

Required. The type of harm category to be blocked.

#### Possible values

- `hate_speech`
Content that promotes violence or incites hatred against individuals or
groups based on certain attributes.

- `dangerous_content`
Content that promotes, facilitates, or enables dangerous activities.

- `harassment`
Abusive, threatening, or content intended to bully, torment, or ridicule.

- `sexually_explicit`
Content that contains sexually explicit material.

- `civic_integrity`
Deprecated: Election filter is not longer supported.
The harm category is civic integrity.

- `image_hate`
Images that contain hate speech.

- `image_dangerous_content`
Images that contain dangerous content.

- `image_harassment`
Images that contain harassment.

- `image_sexually_explicit`
Images that contain sexually explicit content.

- `jailbreak`
Prompts designed to bypass safety filters.


service\_tierServiceTier (optional)

The service tier for the interaction.

#### Possible values

- `flex`
Flex service tier.

- `standard`
Standard service tier.

- `priority`
Priority service tier.

- `deferred`
Deferred service tier.


statusenum (string) (optional)

Required. Output only. The status of the interaction.

Possible
values:

- `in_progress`
The interaction is in progress.

- `requires_action`
The interaction requires action/input from the user.

- `completed`
The interaction is completed.

- `failed`
The interaction failed.

- `cancelled`
The interaction was cancelled.

- `incomplete`
The interaction is completed, but contains incomplete results (e.g.
hitting max\_tokens).

- `budget_exceeded`
Deprecated: Token and execution budget exhaustion returns INCOMPLETE
(11).

- `queued`
The interaction is queued, waiting for processing (e.g. waiting for
off-peak capacity).


stepsarray ( [Step](https://ai.google.dev/api/interactions-api#Resource:Step)) (optional)

Required. Output only. The steps that make up the interaction, when included in the response.

system\_instructionstring (optional)

System instruction for the interaction.

toolsarray ( [Tool](https://ai.google.dev/api/interactions-api#Resource:Tool)) (optional)

A list of tool declarations the model may call during interaction.

updatedstring (optional)

Required. Output only. The time at which the response was last updated in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).

usageUsage (optional)

Output only. Statistics on the interaction request's token usage.

Statistics on the interaction request's token usage.

#### Fields

cached\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

grounding\_tool\_countarray (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

countinteger (optional)

The number of grounding tool counts.

typeenum (string) (optional)

The grounding tool type associated with the count.

Possible
values:

- `google_search`
Grounding with Google Web Search and Image Search, & Web Grounding
for Enterprise.

- `google_maps`
Grounding with Google Maps.

- `retrieval`
Grounding with customer's data, for example, VertexAISearch.


input\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

output\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

tool\_use\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

total\_cached\_tokensinteger (optional)

Number of tokens in the cached part of the prompt (the cached content).

total\_input\_tokensinteger (optional)

Number of tokens in the prompt (context).

total\_output\_tokensinteger (optional)

Total number of tokens across all the generated responses.

total\_thought\_tokensinteger (optional)

Number of tokens of thoughts for thinking models.

total\_tokensinteger (optional)

Total token count for the interaction request (prompt + responses + other
internal tokens).

total\_tool\_use\_tokensinteger (optional)

Number of tokens present in tool-use prompt(s).

webhook\_configWebhookConfig (optional)

Optional. Webhook configuration for receiving notifications when the
interaction completes.

Message for configuring webhook events for a request.

#### Fields

urisarray (string) (optional)

Optional. If set, these webhook URIs will be used for webhook events instead of the
registered webhooks.

user\_metadataobject (optional)

Optional. The user metadata that will be returned on each event emission to the
webhooks.

### Examples

[Example](https://ai.google.dev/api/interactions-api#example)More

```
{
  "created": "2025-12-04T15:01:45Z",
  "id": "v1_ChdXS0l4YWZXTk9xbk0xZThQczhEcmlROBIXV0tJeGFmV05PcW5NMWU4UHM4RHJpUTg",
  "model": "gemini-3.6-flash",
  "object": "interaction",
  "status": "completed",
  "steps": [\
    {\
      "type": "model_output",\
      "content": [\
        {\
          "type": "text",\
          "text": "Hello! I'm doing well, functioning as expected. Thank you for asking! How are you doing today?"\
        }\
      ]\
    }\
  ],
  "updated": "2025-12-04T15:01:45Z",
  "usage": {
    "input_tokens_by_modality": [\
      {\
        "modality": "text",\
        "tokens": 7\
      }\
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 7,
    "total_output_tokens": 23,
    "total_thought_tokens": 49,
    "total_tokens": 79,
    "total_tool_use_tokens": 0
  }
}
```

## Data Models

### Content

The content of the response.

### Possible Types

AudioContent

An audio content block.

channelsinteger (optional)

The number of audio channels.

datastring (optional)

The audio content.

mime\_typeenum (string) (optional)

The mime type of the audio.

Possible
values:

- `audio/wav`
WAV audio format

- `audio/mp3`
MP3 audio format

- `audio/aiff`
AIFF audio format

- `audio/aac`
AAC audio format

- `audio/ogg`
OGG audio format

- `audio/flac`
FLAC audio format

- `audio/mpeg`
MPEG audio format

- `audio/m4a`
M4A audio format

- `audio/l16`
L16 audio format

- `audio/opus`
OPUS audio format

- `audio/alaw`
ALAW audio format

- `audio/mulaw`
MULAW audio format

- `audio/webm`
WebM audio format


sample\_rateinteger (optional)

The sample rate of the audio.

typeobject (required)

No description provided.

Always set to `"audio"`.

uristring (optional)

The URI of the audio.

DocumentContent

A document content block.

datastring (optional)

The document content.

mime\_typeenum (string) (optional)

The mime type of the document.

Possible
values:

- `application/pdf`
PDF document format

- `text/csv`
CSV document format


typeobject (required)

No description provided.

Always set to `"document"`.

uristring (optional)

The URI of the document.

ImageContent

An image content block.

datastring (optional)

The image content.

mime\_typeenum (string) (optional)

The mime type of the image.

Possible
values:

- `image/png`
PNG image format

- `image/jpeg`
JPEG image format

- `image/webp`
WebP image format

- `image/heic`
HEIC image format

- `image/heif`
HEIF image format

- `image/gif`
GIF image format

- `image/bmp`
BMP image format

- `image/tiff`
TIFF image format


resolutionMediaResolution (optional)

The resolution of the media.

#### Possible values

- `low`
Low resolution.

- `medium`
Medium resolution.

- `high`
High resolution.

- `ultra_high`
Ultra high resolution.


typeobject (required)

No description provided.

Always set to `"image"`.

uristring (optional)

The URI of the image.

TextContent

A text content block.

annotationsarray (Annotation) (optional)

Citation information for model-generated content.

Citation information for model-generated content.

#### Possible Types

FileCitation

A file citation annotation.

custom\_metadataobject (optional)

User provided metadata about the retrieved context.

document\_uristring (optional)

The URI of the file.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

file\_namestring (optional)

The name of the file.

media\_idstring (optional)

Media ID in-case of image citations, if applicable.

page\_numberinteger (optional)

Page number of the cited document, if applicable.

sourcestring (optional)

Source attributed for a portion of the text.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

typeobject (required)

No description provided.

Always set to `"file_citation"`.

PlaceCitation

A place citation annotation.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

namestring (optional)

Title of the place.

place\_idstring (optional)

The ID of the place, in \`places/{place\_id}\` format.

review\_snippetsarray (ReviewSnippet) (optional)

Snippets of reviews that are used to generate answers about the
features of a given place in Google Maps.

Encapsulates a snippet of a user review that answers a question about
the features of a specific place in Google Maps.

#### Fields

review\_idstring (optional)

The ID of the review snippet.

titlestring (optional)

Title of the review.

urlstring (optional)

A link that corresponds to the user review on Google Maps.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

typeobject (required)

No description provided.

Always set to `"place_citation"`.

urlstring (optional)

URI reference of the place.

SpeechAnnotation

Speech annotation for text content.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

speakerstring (optional)

The speaker to associate with this turn.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

stylestring (optional)

Style instruction for the speech synthesis.

typeobject (required)

No description provided.

Always set to `"speech_metadata"`.

UrlCitation

A URL citation annotation.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

titlestring (optional)

The title of the URL.

typeobject (required)

No description provided.

Always set to `"url_citation"`.

urlstring (optional)

The URL.

WordInfo

Word-level ASR annotation for transcription output.
Carries the word text, optional timing, and optional speaker attribution.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

end\_offsetstring (optional)

End offset in time of the word relative to the start of the audio.
Present when timestamp\_granularities contains "word".

speakerstring (optional)

Optional. Speaker label for this word (e.g. "spk\_1", "spk\_2").
Present when diarization\_mode is set in TranscriptionConfig.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

start\_offsetstring (optional)

Start offset in time of the word relative to the start of the audio.
Present when timestamp\_granularities contains "word".

textstring (optional)

The transcribed word.

typeobject (required)

No description provided.

Always set to `"word_info"`.

textstring (required)

Required. The text content.

typeobject (required)

No description provided.

Always set to `"text"`.

VideoContent

A video content block.

datastring (optional)

The video content.

mime\_typeenum (string) (optional)

The mime type of the video.

Possible
values:

- `video/mp4`
MP4 video format

- `video/mpeg`
MPEG video format

- `video/mpg`
MPG video format

- `video/mov`
MOV video format

- `video/avi`
AVI video format

- `video/x-flv`
FLV video format

- `video/webm`
WebM video format

- `video/wmv`
WMV video format

- `video/3gpp`
3GPP video format


namestring (optional)

A user-defined name for this content block. Can be referenced by the model
in the final response.

processingMediaProcessing or enum (string) (optional)

How the model processes this video for understanding.

Can be a string (`"static"` \| `"agentic"`) or a `StaticMediaProcessing` object:

- `agentic`: Model-driven dynamic navigation.

- `static`: Fixed-rate frame extraction. All frames placed in context. Can be passed as the string `"static"`, or as an object with the following fields:





end\_offsetstring (optional)





Optional. Segment end time. Specified as a decimal number of seconds followed
by an 's' suffix, e.g., "30s". Must be non-negative and greater than
\`start\_offset\` if \`start\_offset\` is set.









fpsnumber (optional)





Optional. Video frame-rate sampling density.









start\_offsetstring (optional)





Optional. Segment start time. Specified as a decimal number of seconds followed
by an 's' suffix, e.g., "10.5s". Must be non-negative.









typestring (required)





No description provided.



Always set to `"static"`.


resolutionMediaResolution (optional)

The resolution of the media.

#### Possible values

- `low`
Low resolution.

- `medium`
Medium resolution.

- `high`
High resolution.

- `ultra_high`
Ultra high resolution.


typeobject (required)

No description provided.

Always set to `"video"`.

uristring (optional)

The URI of the video.

### Examples

[AudioContent](https://ai.google.dev/api/interactions-api#audiocontent)[DocumentContent](https://ai.google.dev/api/interactions-api#documentcontent)[ImageContent](https://ai.google.dev/api/interactions-api#imagecontent)[TextContent](https://ai.google.dev/api/interactions-api#textcontent)[VideoContent](https://ai.google.dev/api/interactions-api#videocontent)More

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

### Tool

A tool that can be used by the model.

### Possible Types

CodeExecution

A tool that can be used by the model to execute code.

typeobject (required)

No description provided.

Always set to `"code_execution"`.

ComputerUse

A tool that can be used by the model to interact with the computer.

disabled\_safety\_policiesarray (enum (string)) (optional)

Optional. Disabled safety policies for computer use.

Possible
values:

- `financial_transactions`
Safety policy for financial transactions.

- `sensitive_data_modification`
Safety policy for sensitive data modification.

- `communication_tool`
Safety policy for communication tools (e.g. Gmail, Chat, Meet).

- `account_creation`
Safety policy for account creation.

- `data_modification`
Safety policy for data modification.

- `user_consent_management`
Safety policy for user consent management.

- `legal_terms_and_agreements`
Safety policy for legal terms and agreements.


enable\_prompt\_injection\_detectionboolean (optional)

Whether enable the prompt injection detection check on computer-use
request.

environmentenum (string) (optional)

The environment being operated.

Possible
values:

- `browser`
Operates in a web browser.

- `mobile`
Operates in a mobile environment.

- `desktop`
Operates in a desktop environment.


excluded\_predefined\_functionsarray (string) (optional)

The list of predefined functions that are excluded from the model call.

typeobject (required)

No description provided.

Always set to `"computer_use"`.

FileSearch

A tool that can be used by the model to search files.

file\_search\_store\_namesarray (string) (optional)

The file search store names to search.

metadata\_filterstring (optional)

Metadata filter to apply to the semantic retrieval documents and chunks.

top\_kinteger (optional)

The number of semantic retrieval chunks to retrieve.

typeobject (required)

No description provided.

Always set to `"file_search"`.

Function

A tool that can be used by the model.

descriptionstring (optional)

A description of the function.

namestring (optional)

The name of the function.

parametersobject (optional)

The JSON Schema for the function's parameters.

typeobject (required)

No description provided.

Always set to `"function"`.

GoogleMaps

A tool that can be used by the model to call Google Maps.

enable\_widgetboolean (optional)

Whether to return a widget context token in the tool call result of the
response.

latitudenumber (optional)

The latitude of the user's location.

longitudenumber (optional)

The longitude of the user's location.

typeobject (required)

No description provided.

Always set to `"google_maps"`.

GoogleSearch

A tool that can be used by the model to search Google.

search\_typesarray (enum (string)) (optional)

The types of search grounding to enable.

Possible
values:

- `web_search`
Setting this field enables web search. Only text results are returned.

- `image_search`
Setting this field enables image search. Image bytes are returned.

- `enterprise_web_search`
Setting this field enables enterprise web search.


typeobject (required)

No description provided.

Always set to `"google_search"`.

McpServer

A MCPServer is a server that can be called by the model to perform actions.

allowed\_toolsarray (AllowedTools) (optional)

The allowed tools.

The configuration for allowed tools.

#### Fields

modeenum (string) (optional)

The mode of the tool choice.

Possible
values:

- `auto`
Auto tool choice.

- `any`
Any tool choice.

- `none`
No tool choice.

- `validated`
Validated tool choice.


toolsarray (string) (optional)

The names of the allowed tools.

headersobject (optional)

Optional: Fields for authentication headers, timeouts, etc., if needed.

namestring (optional)

The name of the MCPServer.

typeobject (required)

No description provided.

Always set to `"mcp_server"`.

urlstring (optional)

The full URL for the MCPServer endpoint.
Example: "https://api.example.com/mcp"

Retrieval

A tool that can be used by the model to retrieve files.

exa\_ai\_search\_configExaAISearchConfig (optional)

Used to specify configuration for ExaAISearch.

Used to specify configuration for ExaAISearch.

#### Fields

api\_keystring (optional)

Required. The API key for ExaAiSearch.

custom\_configobject (optional)

Optional. This field can be used to pass any parameter from the Exa.ai Search API.

parallel\_ai\_search\_configParallelAISearchConfig (optional)

Used to specify configuration for ParallelAISearch.

Used to specify configuration for ParallelAISearch.

#### Fields

api\_keystring (optional)

Optional. The API key for ParallelAiSearch.

custom\_configobject (optional)

Optional. Custom configs for ParallelAiSearch.

rag\_store\_configRagStoreConfig (optional)

Used to specify configuration for RagStore.

Use to specify configuration for RAG Store.

#### Fields

rag\_resourcesarray (RagResource) (optional)

Optional. The representation of the rag source.

The definition of the Rag resource.

#### Fields

rag\_corpusstring (optional)

Optional. RagCorpora resource name.

rag\_file\_idsarray (string) (optional)

Optional. rag\_file\_id. The files should be in the same rag\_corpus set in
rag\_corpus field.

rag\_retrieval\_configRagRetrievalConfig (optional)

Optional. The retrieval config for the Rag query.

Specifies the context retrieval config.

#### Fields

filterFilter (optional)

Optional. Config for filters.

Config for filters.

#### Fields

metadata\_filterstring (optional)

Optional. String for metadata filtering.

vector\_distance\_thresholdnumber (optional)

Optional. Only returns contexts with vector distance smaller than the
threshold.

vector\_similarity\_thresholdnumber (optional)

Optional. Only returns contexts with vector similarity larger than the
threshold.

hybrid\_searchHybridSearch (optional)

Optional. Config for Hybrid Search.

Config for Hybrid Search.

#### Fields

alphanumber (optional)

Optional. Alpha value controls the weight between dense and sparse vector search
results.

rankingRanking (optional)

Optional. Config for ranking and reranking.

Config for ranking and reranking.

#### Fields

model\_namestring (optional)

Optional. The model name of the rank service.

rank\_serviceRankService (optional)

Config for Rank Service.

Config for Rank Service.

#### Fields

model\_namestring (optional)

Optional. The model name of the rank service.

ranking\_configobject (optional)

No description provided.

Always set to `"rank_service"`.

top\_kinteger (optional)

Optional. The number of contexts to retrieve.

retrieval\_typesarray (enum (string)) (optional)

The types of file retrieval to enable.

Possible
values:

- `rag_store`
- `exa_ai_search`
- `parallel_ai_search`

typeobject (required)

No description provided.

Always set to `"retrieval"`.

UrlContext

A tool that can be used by the model to fetch URL context.

typeobject (required)

No description provided.

Always set to `"url_context"`.

### Examples

[CodeExecution](https://ai.google.dev/api/interactions-api#codeexecution)[ComputerUse](https://ai.google.dev/api/interactions-api#computeruse)[FileSearch](https://ai.google.dev/api/interactions-api#filesearch)[Function](https://ai.google.dev/api/interactions-api#function)[GoogleMaps](https://ai.google.dev/api/interactions-api#googlemaps)[GoogleSearch](https://ai.google.dev/api/interactions-api#googlesearch)[McpServer](https://ai.google.dev/api/interactions-api#mcpserver)[Retrieval](https://ai.google.dev/api/interactions-api#retrieval)[UrlContext](https://ai.google.dev/api/interactions-api#urlcontext)More

Google AI for Developers

#### Example

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "tools": [{\
      "type": "code_execution"\
    }],
    "input": "Calculate the first 10 Fibonacci numbers"
  }'
```

```python
from google import genai

client = genai.Client()
response = client.interactions.create(
    model="gemini-3.6-flash",
    tools=[{"type": "code_execution"}],
    input="Calculate the first 10 Fibonacci numbers",
)
print(response.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  tools: [{type: 'code_execution'}],
  input: 'Calculate the first 10 Fibonacci numbers',
});
console.log(interaction.output_text);
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;

Client client = new Client();
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.6-flash")
        .tools(List.of(new CodeExecution()))
        .input(InteractionsInput.of("Calculate the first 10 Fibonacci numbers"))
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.outputText().orElse(""));
```

Google AI for Developers

#### Example

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-computer-use-preview-10-2025",
    "tools": [{\
      "type": "computer_use"\
    }],
    "input": "Find a flight to Tokyo"
  }'
```

```python
from google import genai

client = genai.Client()
response = client.interactions.create(
    model="gemini-2.5-computer-use-preview-10-2025",
    tools=[{"type": "computer_use"}],
    input="Find a flight to Tokyo",
)
print(response.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  model: 'gemini-2.5-computer-use-preview-10-2025',
  tools: [{type: 'computer_use'}],
  input: 'Find a flight to Tokyo',
});
console.log(interaction.output_text);
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;

Client client = new Client();
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-2.5-computer-use-preview-10-2025")
        .tools(List.of(new ComputerUse()))
        .input(InteractionsInput.of("Find a flight to Tokyo"))
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.outputText().orElse(""));
```

Google AI for Developers

#### Example

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "tools": [{\
      "type": "file_search",\
      "file_search_store_names": ["fileSearchStores/m64d1sevsr4y-xfyawui3fxqg"]\
    }],
    "input": "Who is the author of the book?"
  }'
```

```python
from google import genai

client = genai.Client()

# Create a file search store so we have a valid one to use.
store = client.file_search_stores.create()

response = client.interactions.create(
    model="gemini-3.6-flash",
    tools=[\
        {"type": "file_search", "file_search_store_names": [store.name]}\
    ],
    input="What documents are available?",
)
print(response.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

// Create a file search store so we have a valid one to use.
const store = await ai.fileSearchStores.create({});
if (!store.name) {
  throw new Error('Store creation failed: Name is undefined');
}

const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  tools: [\
    {\
      type: 'file_search',\
      file_search_store_names: [store.name],\
    },\
  ],
  input: 'What documents are available?',
});
console.log(interaction.output_text);
```

```java
import com.google.genai.Client;
import com.google.genai.types.CreateFileSearchStoreConfig;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.types.FileSearchStore;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;

Client client = new Client();

// Create a file search store so we have a valid one to use.
FileSearchStore store =
    client.fileSearchStores.create(CreateFileSearchStoreConfig.builder().build());
String storeName = store.name().orElseThrow();

FileSearch tool = FileSearch.builder().fileSearchStoreNames(List.of(storeName)).build();
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.6-flash")
        .tools(List.of(tool))
        .input(InteractionsInput.of("What documents are available?"))
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.outputText().orElse(""));
```

Google AI for Developers

#### Example

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "tools": [{\
      "type": "function",\
      "name": "get_weather",\
      "description": "Get the current weather in a given location",\
      "parameters": {\
        "type": "object",\
        "properties": {\
          "location": {\
            "type": "string",\
            "description": "The city and state, e.g. San Francisco, CA"\
          }\
        },\
        "required": ["location"]\
      }\
    }],
    "input": "What is the weather like in Boston, MA?"
  }'
```

```python
from google import genai

client = genai.Client()
response = client.interactions.create(
    model="gemini-3.6-flash",
    tools=[{\
        "type": "function",\
        "name": "get_weather",\
        "description": "Get the current weather in a given location",\
        "parameters": {\
            "type": "object",\
            "properties": {\
                "location": {\
                    "type": "string",\
                    "description": (\
                        "The city and state, e.g. San Francisco, CA"\
                    ),\
                }\
            },\
            "required": ["location"],\
        },\
    }],
    input="What is the weather like in Boston?",
)
print(response.steps[-1])
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  tools: [\
    {\
      type: 'function',\
      name: 'get_weather',\
      description: 'Get the current weather in a given location',\
      parameters: {\
        type: 'object',\
        properties: {\
          location: {\
            type: 'string',\
            description: 'The city and state, e.g. San Francisco, CA',\
          },\
        },\
        required: ['location'],\
      },\
    },\
  ],
  input: 'What is the weather like in Boston?',
});
console.log(interaction.steps.at(-1));
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Step;

Client client = new Client();
Map
```

Google AI for Developers

#### Example

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "tools": [{\
      "type": "google_maps",\
      "latitude": 37.7749,\
      "longitude": -122.4194\
    }],
    "input": "What is the best food near me?"
  }'
```

```python
from google import genai

client = genai.Client()
response = client.interactions.create(
    model="gemini-3.6-flash",
    tools=[\
        {"type": "google_maps", "latitude": 37.7749, "longitude": -122.4194}\
    ],
    input="What is the best food near me?",
)
print(response.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  tools: [\
    {\
      type: 'google_maps',\
      latitude: 37.7749,\
      longitude: -122.4194,\
    },\
  ],
  input: 'What is the best food near me?',
});
console.log(interaction.output_text);
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;

Client client = new Client();
GoogleMaps tool = GoogleMaps.builder().latitude(37.7749).longitude(-122.4194).build();
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.6-flash")
        .tools(List.of(tool))
        .input(InteractionsInput.of("What is the best food near me?"))
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.outputText().orElse(""));
```

Google AI for Developers

#### Example

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "tools": [{\
      "type": "google_search"\
    }],
    "input": "Who is the current president of France?"
  }'
```

```python
from google import genai

client = genai.Client()
response = client.interactions.create(
    model="gemini-3.6-flash",
    tools=[{"type": "google_search"}],
    input="Who is the current president of France?",
)
print(response.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  tools: [{type: 'google_search'}],
  input: 'Who is the current president of France?',
});
console.log(interaction.output_text);
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;

Client client = new Client();
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.6-flash")
        .tools(List.of(new GoogleSearch()))
        .input(InteractionsInput.of("Who is the current president of France?"))
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.outputText().orElse(""));
```

Google AI for Developers

#### Example

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "tools": [{\
      "type": "mcp_server",\
      "name": "weather_service",\
      "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"\
    }],
    "input": "Today is 12-05-2025, what is the temperature today in London?"
  }'
```

```python
import os

from google import genai

client = genai.Client()
response = client.interactions.create(
    model="gemini-3.6-flash",
    tools=[{\
        "type": "mcp_server",\
        "name": "weather_service",\
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp",\
    }],
    input="Today is 12-05-2025, what is the temperature today in London?",
)
print(response.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  tools: [\
    {\
      type: 'mcp_server',\
      name: 'weather_service',\
      url: 'https://gemini-api-demos.uc.r.appspot.com/mcp',\
    },\
  ],
  input: 'Today is 12-05-2025, what is the temperature today in London?',
});
console.log(interaction.output_text);
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.MCPServer;

Client client = new Client();
MCPServer mcpTool =
    MCPServer.builder()
        .name("weather_service")
        .url("https://gemini-api-demos.uc.r.appspot.com/mcp")
        .build();
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.6-flash")
        .tools(List.of(mcpTool))
        .input(
            InteractionsInput.of(
                "Today is 12-05-2025, what is the temperature today in London?"))
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.outputText().orElse(""));
```

No examples available for this type.

Google AI for Developers

#### Example

RESTPythonJavaScriptJava

```sh
curl -X POST https://generativelanguage.googleapis.com/v1beta/interactions \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "tools": [{\
      "type": "url_context"\
    }],
    "input": "Summarize https://www.example.com"
  }'
```

```python
from google import genai

client = genai.Client()
response = client.interactions.create(
    model="gemini-3.6-flash",
    tools=[{"type": "url_context"}],
    input="Summarize https://www.example.com",
)
print(response.output_text)
```

```javascript
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});
const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  tools: [{type: 'url_context'}],
  input: 'Summarize https://www.example.com',
});
console.log(interaction.output_text);
```

```java
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.URLContext;

Client client = new Client();
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.6-flash")
        .tools(List.of(new URLContext()))
        .input(InteractionsInput.of("Summarize https://www.example.com"))
        .build();
CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));
Interaction interaction =
    response.interaction().orElseThrow(() -> new RuntimeException("No interaction returned"));
System.out.println(interaction.outputText().orElse(""));
```

### InteractionSseStreamEvent

### Possible Types

ErrorEvent

errorError (optional)

No description provided.

Error message from an interaction.

#### Fields

codestring (optional)

A URI that identifies the error type.

messagestring (optional)

A human-readable error message.

event\_idstring (optional)

The event\_id token to be used to resume the interaction stream, from
this event.

event\_typeobject (required)

No description provided.

Always set to `"error"`.

InteractionCompletedEvent

Signals that the Interaction completed. Sent when the Interaction receives
Complete/Cancel or naturally terminates. No more input can be sent to the
Interaction after this.

event\_idstring (optional)

The event\_id token to be used to resume the interaction stream, from
this event.

event\_typeobject (required)

No description provided.

Always set to `"interaction.completed"`.

interactionInteractionSseEventInteraction (required)

Required. Partial completed interaction resource emitted at the end of the stream.

Partial interaction resource emitted by interaction lifecycle SSE events.
Streaming lifecycle payloads may omit fields that are only available on
full non-streaming Interaction responses.

#### Fields

agentstring (optional)

The agent to interact with.

createdstring (optional)

Output only. The time at which the response was created in ISO 8601 format.

idstring (optional)

Required. Output only. A unique identifier for the interaction completion.

modelstring (optional)

The model that will complete your prompt.

objectstring (optional)

Output only. The resource type.

service\_tierServiceTier (optional)

The service tier for the interaction.

#### Possible values

- `flex`
Flex service tier.

- `standard`
Standard service tier.

- `priority`
Priority service tier.

- `deferred`
Deferred service tier.


statusenum (string) (optional)

Required. Output only. The status of the interaction.

Possible
values:

- `in_progress`
The interaction is in progress.

- `requires_action`
The interaction requires action/input from the user.

- `completed`
The interaction is completed.

- `failed`
The interaction failed.

- `cancelled`
The interaction was cancelled.

- `incomplete`
The interaction is completed, but contains incomplete results (e.g. hitting max\_tokens).


stepsarray ( [Step](https://ai.google.dev/api/interactions-api#Resource:Step)) (optional)

Output only. The steps that make up the interaction, if included in this event.

updatedstring (optional)

Output only. The time at which the response was last updated in ISO 8601 format.

usageUsage (optional)

Output only. Statistics on the interaction request's token usage.

Statistics on the interaction request's token usage.

#### Fields

cached\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

grounding\_tool\_countarray (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

countinteger (optional)

The number of grounding tool counts.

typeenum (string) (optional)

The grounding tool type associated with the count.

Possible
values:

- `google_search`
Grounding with Google Web Search and Image Search, & Web Grounding
for Enterprise.

- `google_maps`
Grounding with Google Maps.

- `retrieval`
Grounding with customer's data, for example, VertexAISearch.


input\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

output\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

tool\_use\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

total\_cached\_tokensinteger (optional)

Number of tokens in the cached part of the prompt (the cached content).

total\_input\_tokensinteger (optional)

Number of tokens in the prompt (context).

total\_output\_tokensinteger (optional)

Total number of tokens across all the generated responses.

total\_thought\_tokensinteger (optional)

Number of tokens of thoughts for thinking models.

total\_tokensinteger (optional)

Total token count for the interaction request (prompt + responses + other
internal tokens).

total\_tool\_use\_tokensinteger (optional)

Number of tokens present in tool-use prompt(s).

InteractionCreatedEvent

Server response confirming that a new interaction was created.

event\_idstring (optional)

The event\_id token to be used to resume the interaction stream, from
this event.

event\_typeobject (required)

No description provided.

Always set to `"interaction.created"`.

interactionInteractionSseEventInteraction (required)

Required. Partial interaction resource emitted when the stream is created.

Partial interaction resource emitted by interaction lifecycle SSE events.
Streaming lifecycle payloads may omit fields that are only available on
full non-streaming Interaction responses.

#### Fields

agentstring (optional)

The agent to interact with.

createdstring (optional)

Output only. The time at which the response was created in ISO 8601 format.

idstring (optional)

Required. Output only. A unique identifier for the interaction completion.

modelstring (optional)

The model that will complete your prompt.

objectstring (optional)

Output only. The resource type.

service\_tierServiceTier (optional)

The service tier for the interaction.

#### Possible values

- `flex`
Flex service tier.

- `standard`
Standard service tier.

- `priority`
Priority service tier.

- `deferred`
Deferred service tier.


statusenum (string) (optional)

Required. Output only. The status of the interaction.

Possible
values:

- `in_progress`
The interaction is in progress.

- `requires_action`
The interaction requires action/input from the user.

- `completed`
The interaction is completed.

- `failed`
The interaction failed.

- `cancelled`
The interaction was cancelled.

- `incomplete`
The interaction is completed, but contains incomplete results (e.g. hitting max\_tokens).


stepsarray ( [Step](https://ai.google.dev/api/interactions-api#Resource:Step)) (optional)

Output only. The steps that make up the interaction, if included in this event.

updatedstring (optional)

Output only. The time at which the response was last updated in ISO 8601 format.

usageUsage (optional)

Output only. Statistics on the interaction request's token usage.

Statistics on the interaction request's token usage.

#### Fields

cached\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

grounding\_tool\_countarray (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

countinteger (optional)

The number of grounding tool counts.

typeenum (string) (optional)

The grounding tool type associated with the count.

Possible
values:

- `google_search`
Grounding with Google Web Search and Image Search, & Web Grounding
for Enterprise.

- `google_maps`
Grounding with Google Maps.

- `retrieval`
Grounding with customer's data, for example, VertexAISearch.


input\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

output\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

tool\_use\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

total\_cached\_tokensinteger (optional)

Number of tokens in the cached part of the prompt (the cached content).

total\_input\_tokensinteger (optional)

Number of tokens in the prompt (context).

total\_output\_tokensinteger (optional)

Total number of tokens across all the generated responses.

total\_thought\_tokensinteger (optional)

Number of tokens of thoughts for thinking models.

total\_tokensinteger (optional)

Total token count for the interaction request (prompt + responses + other
internal tokens).

total\_tool\_use\_tokensinteger (optional)

Number of tokens present in tool-use prompt(s).

InteractionStatusUpdate

event\_idstring (optional)

The event\_id token to be used to resume the interaction stream, from
this event.

event\_typeobject (required)

No description provided.

Always set to `"interaction.status_update"`.

interaction\_idstring (required)

No description provided.

statusenum (string) (required)

No description provided.

Possible
values:

- `in_progress`
The interaction is in progress.

- `requires_action`
The interaction requires action/input from the user.

- `completed`
The interaction is completed.

- `failed`
The interaction failed.

- `cancelled`
The interaction was cancelled.

- `incomplete`
The interaction is completed, but contains incomplete results (e.g.
hitting max\_tokens).

- `budget_exceeded`
Deprecated: Token and execution budget exhaustion returns INCOMPLETE
(11).

- `queued`
The interaction is queued, waiting for processing (e.g. waiting for
off-peak capacity).


StepDelta

deltaStepDeltaData (required)

No description provided.

#### Possible Types

ArgumentsDelta

argumentsstring (optional)

No description provided.

typeobject (required)

No description provided.

Always set to `"arguments_delta"`.

AudioDelta

channelsinteger (optional)

The number of audio channels.

datastring (optional)

No description provided.

mime\_typeenum (string) (optional)

No description provided.

Possible
values:

- `audio/wav`
WAV audio format

- `audio/mp3`
MP3 audio format

- `audio/aiff`
AIFF audio format

- `audio/aac`
AAC audio format

- `audio/ogg`
OGG audio format

- `audio/flac`
FLAC audio format

- `audio/mpeg`
MPEG audio format

- `audio/m4a`
M4A audio format

- `audio/l16`
L16 audio format

- `audio/opus`
OPUS audio format

- `audio/alaw`
ALAW audio format

- `audio/mulaw`
MULAW audio format

- `audio/webm`
WEBM audio format


sample\_rateinteger (optional)

The sample rate of the audio.

typeobject (required)

No description provided.

Always set to `"audio"`.

uristring (optional)

No description provided.

CodeExecutionCallDelta

argumentsCodeExecutionCallArguments (required)

No description provided.

The arguments to pass to the code execution.

#### Fields

codestring (optional)

The code to be executed.

languageenum (string) (optional)

Programming language of the \`code\`.

Possible
values:

- `python`
Python >= 3.10, with numpy and simpy available.


signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"code_execution_call"`.

CodeExecutionResultDelta

is\_errorboolean (optional)

No description provided.

resultstring (required)

No description provided.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"code_execution_result"`.

DocumentDelta

datastring (optional)

No description provided.

mime\_typeenum (string) (optional)

No description provided.

Possible
values:

- `application/pdf`
PDF document format

- `text/csv`
CSV document format


typeobject (required)

No description provided.

Always set to `"document"`.

uristring (optional)

No description provided.

FileSearchCallDelta

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"file_search_call"`.

FileSearchResultDelta

resultarray (FileSearchResult) (required)

No description provided.

The result of the File Search.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"file_search_result"`.

FunctionResultDelta

is\_errorboolean (optional)

No description provided.

namestring (optional)

No description provided.

resultarray (FunctionResultSubContent) or object or string (required)

No description provided.

typeobject (required)

No description provided.

Always set to `"function_result"`.

GoogleMapsCallDelta

argumentsGoogleMapsCallArguments (optional)

The arguments to pass to the Google Maps tool.

The arguments to pass to the Google Maps tool.

#### Fields

queriesarray (string) (optional)

The queries to be executed.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"google_maps_call"`.

GoogleMapsResultDelta

resultarray (GoogleMapsResult) (optional)

The results of the Google Maps.

The result of the Google Maps.

#### Fields

placesarray (Places) (optional)

The places that were found.

#### Fields

namestring (optional)

Title of the place.

place\_idstring (optional)

The ID of the place, in \`places/{place\_id}\` format.

review\_snippetsarray (ReviewSnippet) (optional)

Snippets of reviews that are used to generate answers about the
features of a given place in Google Maps.

Encapsulates a snippet of a user review that answers a question about
the features of a specific place in Google Maps.

#### Fields

review\_idstring (optional)

The ID of the review snippet.

titlestring (optional)

Title of the review.

urlstring (optional)

A link that corresponds to the user review on Google Maps.

urlstring (optional)

URI reference of the place.

widget\_context\_tokenstring (optional)

Resource name of the Google Maps widget context token.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"google_maps_result"`.

GoogleSearchCallDelta

argumentsGoogleSearchCallArguments (required)

No description provided.

The arguments to pass to Google Search.

#### Fields

queriesarray (string) (optional)

Web search queries for the following-up web search.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"google_search_call"`.

GoogleSearchResultDelta

is\_errorboolean (optional)

No description provided.

resultarray (GoogleSearchResult) (required)

No description provided.

The result of the Google Search.

#### Fields

search\_suggestionsstring (optional)

Web content snippet that can be embedded in a web page or an app webview.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"google_search_result"`.

ImageDelta

datastring (optional)

No description provided.

mime\_typeenum (string) (optional)

No description provided.

Possible
values:

- `image/png`
PNG image format

- `image/jpeg`
JPEG image format

- `image/webp`
WebP image format

- `image/heic`
HEIC image format

- `image/heif`
HEIF image format

- `image/gif`
GIF image format

- `image/bmp`
BMP image format

- `image/tiff`
TIFF image format


resolutionMediaResolution (optional)

The resolution of the media.

#### Possible values

- `low`
Low resolution.

- `medium`
Medium resolution.

- `high`
High resolution.

- `ultra_high`
Ultra high resolution.


typeobject (required)

No description provided.

Always set to `"image"`.

uristring (optional)

No description provided.

McpServerToolCallDelta

argumentsobject (required)

No description provided.

namestring (required)

No description provided.

server\_namestring (required)

No description provided.

typeobject (required)

No description provided.

Always set to `"mcp_server_tool_call"`.

McpServerToolResultDelta

namestring (optional)

No description provided.

resultarray (FunctionResultSubContent) or object or string (required)

No description provided.

server\_namestring (optional)

No description provided.

typeobject (required)

No description provided.

Always set to `"mcp_server_tool_result"`.

ProcessingCallDelta

Streaming delta for a server-initiated media processing step.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"processing_call"`.

ProcessingResultDelta

Streaming delta for the result of a server-initiated media processing step.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"processing_result"`.

RetrievalCallDelta

Used by Vertex Retrieval tools such as Parallel AI, Exa AI, Vertex AI Search,
etc. RetrievalType decides which tool is used.

argumentsRetrievalStepArguments (required)

Required. The arguments to pass to the Retrieval tool.

The arguments to pass to Retrieval tools.

#### Fields

queriesarray (string) (optional)

Queries for Retrieval information.

retrieval\_typeenum (string) (optional)

The type of retrieval tools.

Possible
values:

- `rag_store`
The type of retrieval tools.

- `exa_ai_search`
The type of retrieval tools.

- `parallel_ai_search`
The type of retrieval tools.


signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"retrieval_call"`.

RetrievalResultDelta

Used by Vertex Retrieval tools such as Parallel AI, Exa AI, Vertex AI Search,
etc.
ToolResultDelta.type

is\_errorboolean (optional)

Whether the retrieval resulted in an error.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"retrieval_result"`.

TextAnnotationDelta

annotationsarray (Annotation) (optional)

Citation information for model-generated content.

Citation information for model-generated content.

#### Possible Types

FileCitation

A file citation annotation.

custom\_metadataobject (optional)

User provided metadata about the retrieved context.

document\_uristring (optional)

The URI of the file.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

file\_namestring (optional)

The name of the file.

media\_idstring (optional)

Media ID in-case of image citations, if applicable.

page\_numberinteger (optional)

Page number of the cited document, if applicable.

sourcestring (optional)

Source attributed for a portion of the text.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

typeobject (required)

No description provided.

Always set to `"file_citation"`.

PlaceCitation

A place citation annotation.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

namestring (optional)

Title of the place.

place\_idstring (optional)

The ID of the place, in \`places/{place\_id}\` format.

review\_snippetsarray (ReviewSnippet) (optional)

Snippets of reviews that are used to generate answers about the
features of a given place in Google Maps.

Encapsulates a snippet of a user review that answers a question about
the features of a specific place in Google Maps.

#### Fields

review\_idstring (optional)

The ID of the review snippet.

titlestring (optional)

Title of the review.

urlstring (optional)

A link that corresponds to the user review on Google Maps.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

typeobject (required)

No description provided.

Always set to `"place_citation"`.

urlstring (optional)

URI reference of the place.

SpeechAnnotation

Speech annotation for text content.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

speakerstring (optional)

The speaker to associate with this turn.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

stylestring (optional)

Style instruction for the speech synthesis.

typeobject (required)

No description provided.

Always set to `"speech_metadata"`.

UrlCitation

A URL citation annotation.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

titlestring (optional)

The title of the URL.

typeobject (required)

No description provided.

Always set to `"url_citation"`.

urlstring (optional)

The URL.

WordInfo

Word-level ASR annotation for transcription output.
Carries the word text, optional timing, and optional speaker attribution.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

end\_offsetstring (optional)

End offset in time of the word relative to the start of the audio.
Present when timestamp\_granularities contains "word".

speakerstring (optional)

Optional. Speaker label for this word (e.g. "spk\_1", "spk\_2").
Present when diarization\_mode is set in TranscriptionConfig.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

start\_offsetstring (optional)

Start offset in time of the word relative to the start of the audio.
Present when timestamp\_granularities contains "word".

textstring (optional)

The transcribed word.

typeobject (required)

No description provided.

Always set to `"word_info"`.

typeobject (required)

No description provided.

Always set to `"text_annotation_delta"`.

TextDelta

textstring (required)

No description provided.

typeobject (required)

No description provided.

Always set to `"text"`.

ThoughtSignatureDelta

signaturestring (optional)

Signature to match the backend source to be part of the generation.

typeobject (required)

No description provided.

Always set to `"thought_signature"`.

ThoughtSummaryDelta

content[Content](https://ai.google.dev/api/interactions-api#Resource:Content) (optional)

A new summary item to be added to the thought.

typeobject (required)

No description provided.

Always set to `"thought_summary"`.

UrlContextCallDelta

argumentsUrlContextCallArguments (required)

No description provided.

The arguments to pass to the URL context.

#### Fields

urlsarray (string) (optional)

The URLs to fetch.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"url_context_call"`.

UrlContextResultDelta

is\_errorboolean (optional)

No description provided.

resultarray (UrlContextResult) (required)

No description provided.

The result of the URL context.

#### Fields

statusenum (string) (optional)

The status of the URL retrieval.

Possible
values:

- `success`
Url retrieval is successful.

- `error`
Url retrieval is failed due to error.

- `paywall`
Url retrieval is failed because the content is behind paywall.

- `unsafe`
Url retrieval is failed because the content is unsafe.


urlstring (optional)

The URL that was fetched.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"url_context_result"`.

VideoDelta

datastring (optional)

No description provided.

mime\_typeenum (string) (optional)

No description provided.

Possible
values:

- `video/mp4`
MP4 video format

- `video/mpeg`
MPEG video format

- `video/mpg`
MPG video format

- `video/mov`
MOV video format

- `video/avi`
AVI video format

- `video/x-flv`
FLV video format

- `video/webm`
WebM video format

- `video/wmv`
WMV video format

- `video/3gpp`
3GPP video format

- `video/jpeg2000`
JPEG 2000 video format


resolutionMediaResolution (optional)

The resolution of the media.

#### Possible values

- `low`
Low resolution.

- `medium`
Medium resolution.

- `high`
High resolution.

- `ultra_high`
Ultra high resolution.


typeobject (required)

No description provided.

Always set to `"video"`.

uristring (optional)

No description provided.

event\_idstring (optional)

The event\_id token to be used to resume the interaction stream, from
this event.

event\_typeobject (required)

No description provided.

Always set to `"step.delta"`.

indexinteger (required)

No description provided.

metadataStepDeltaMetadata (optional)

No description provided.

Optional metadata accompanying ANY streamed event.

#### Fields

total\_usageUsage (optional)

Statistics on the interaction request's token usage.

Statistics on the interaction request's token usage.

#### Fields

cached\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

grounding\_tool\_countarray (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

countinteger (optional)

The number of grounding tool counts.

typeenum (string) (optional)

The grounding tool type associated with the count.

Possible
values:

- `google_search`
Grounding with Google Web Search and Image Search, & Web Grounding
for Enterprise.

- `google_maps`
Grounding with Google Maps.

- `retrieval`
Grounding with customer's data, for example, VertexAISearch.


input\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

output\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

tool\_use\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

total\_cached\_tokensinteger (optional)

Number of tokens in the cached part of the prompt (the cached content).

total\_input\_tokensinteger (optional)

Number of tokens in the prompt (context).

total\_output\_tokensinteger (optional)

Total number of tokens across all the generated responses.

total\_thought\_tokensinteger (optional)

Number of tokens of thoughts for thinking models.

total\_tokensinteger (optional)

Total token count for the interaction request (prompt + responses + other
internal tokens).

total\_tool\_use\_tokensinteger (optional)

Number of tokens present in tool-use prompt(s).

StepStart

event\_idstring (optional)

The event\_id token to be used to resume the interaction stream, from
this event.

event\_typeobject (required)

No description provided.

Always set to `"step.start"`.

indexinteger (required)

No description provided.

step[Step](https://ai.google.dev/api/interactions-api#Resource:Step) (required)

No description provided.

StepStop

event\_idstring (optional)

The event\_id token to be used to resume the interaction stream, from
this event.

event\_typeobject (required)

No description provided.

Always set to `"step.stop"`.

indexinteger (required)

No description provided.

step\_usageUsage (optional)

Model usage stats for this specific step.

Statistics on the interaction request's token usage.

#### Fields

cached\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

grounding\_tool\_countarray (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

countinteger (optional)

The number of grounding tool counts.

typeenum (string) (optional)

The grounding tool type associated with the count.

Possible
values:

- `google_search`
Grounding with Google Web Search and Image Search, & Web Grounding
for Enterprise.

- `google_maps`
Grounding with Google Maps.

- `retrieval`
Grounding with customer's data, for example, VertexAISearch.


input\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

output\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

tool\_use\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

total\_cached\_tokensinteger (optional)

Number of tokens in the cached part of the prompt (the cached content).

total\_input\_tokensinteger (optional)

Number of tokens in the prompt (context).

total\_output\_tokensinteger (optional)

Total number of tokens across all the generated responses.

total\_thought\_tokensinteger (optional)

Number of tokens of thoughts for thinking models.

total\_tokensinteger (optional)

Total token count for the interaction request (prompt + responses + other
internal tokens).

total\_tool\_use\_tokensinteger (optional)

Number of tokens present in tool-use prompt(s).

usageUsage (optional)

Cumulative model usage stats from the start of the session.

Statistics on the interaction request's token usage.

#### Fields

cached\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

grounding\_tool\_countarray (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

countinteger (optional)

The number of grounding tool counts.

typeenum (string) (optional)

The grounding tool type associated with the count.

Possible
values:

- `google_search`
Grounding with Google Web Search and Image Search, & Web Grounding
for Enterprise.

- `google_maps`
Grounding with Google Maps.

- `retrieval`
Grounding with customer's data, for example, VertexAISearch.


input\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

output\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

tool\_use\_tokens\_by\_modalityarray (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modalityResponseModality (optional)

The modality associated with the token count.

#### Possible values

- `text`
Indicates the model should return text.

- `image`
Indicates the model should return images.

- `audio`
Indicates the model should return audio.

- `video`
Indicates the model should return video.

- `document`
Indicates the model should return documents.


tokensinteger (optional)

Number of tokens for the modality.

total\_cached\_tokensinteger (optional)

Number of tokens in the cached part of the prompt (the cached content).

total\_input\_tokensinteger (optional)

Number of tokens in the prompt (context).

total\_output\_tokensinteger (optional)

Total number of tokens across all the generated responses.

total\_thought\_tokensinteger (optional)

Number of tokens of thoughts for thinking models.

total\_tokensinteger (optional)

Total token count for the interaction request (prompt + responses + other
internal tokens).

total\_tool\_use\_tokensinteger (optional)

Number of tokens present in tool-use prompt(s).

### Examples

[ErrorEvent](https://ai.google.dev/api/interactions-api#errorevent)[InteractionCompletedEvent](https://ai.google.dev/api/interactions-api#interactioncompletedevent)[InteractionCreatedEvent](https://ai.google.dev/api/interactions-api#interactioncreatedevent)[InteractionStatusUpdate](https://ai.google.dev/api/interactions-api#interactionstatusupdate)[StepDelta](https://ai.google.dev/api/interactions-api#stepdelta)[StepStart](https://ai.google.dev/api/interactions-api#stepstart)[StepStop](https://ai.google.dev/api/interactions-api#stepstop)More

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

### ResponseFormat

### Possible Types

AudioResponseFormat

Configuration for audio output format.

bit\_rateinteger (optional)

Bit rate in bits per second (bps). Only applicable for compressed formats
(MP3, Opus).

deliveryenum (string) (optional)

The delivery mode for the audio output.

Possible
values:

- `inline`
Audio data is returned inline in the response.

- `uri`
Audio data is returned as a URI.


mime\_typeenum (string) (optional)

The MIME type of the audio output.

Possible
values:

- `audio/mp3`
MP3 audio format.

- `audio/ogg_opus`
OGG Opus audio format.

- `audio/l16`
Raw PCM (L16) audio format.

- `audio/wav`
WAV audio format.

- `audio/alaw`
A-law audio format.

- `audio/mulaw`
Mu-law audio format.


sample\_rateinteger (optional)

Sample rate in Hz.

typeobject (required)

No description provided.

Always set to `"audio"`.

ImageResponseFormat

Configuration for image output format.

aspect\_ratioenum (string) (optional)

The aspect ratio for the image output.

Possible
values:

- `1:1`
1:1 aspect ratio.

- `2:3`
2:3 aspect ratio.

- `3:2`
3:2 aspect ratio.

- `3:4`
3:4 aspect ratio.

- `4:3`
4:3 aspect ratio.

- `4:5`
4:5 aspect ratio.

- `5:4`
5:4 aspect ratio.

- `9:16`
9:16 aspect ratio.

- `16:9`
16:9 aspect ratio.

- `21:9`
21:9 aspect ratio.

- `1:8`
1:8 aspect ratio.

- `8:1`
8:1 aspect ratio.

- `1:4`
1:4 aspect ratio.

- `4:1`
4:1 aspect ratio.


deliveryenum (string) (optional)

The delivery mode for the image output.

Possible
values:

- `inline`
Image data is returned inline in the response.

- `uri`
Image data is returned as a URI.


image\_sizeenum (string) (optional)

The size of the image output.

Possible
values:

- `512`
512px image size.

- `1K`
1K image size.

- `2K`
2K image size.

- `4K`
4K image size.


mime\_typeenum (string) (optional)

The MIME type of the image output.

Possible
values:

- `image/jpeg`
JPEG image format.


typeobject (required)

No description provided.

Always set to `"image"`.

TextResponseFormat

Configuration for text output format.

mime\_typeenum (string) (optional)

The MIME type of the text output.

Possible
values:

- `application/json`
JSON output format.

- `text/plain`
Plain text output format.


schemaobject (optional)

The JSON schema that the output should conform to. Only applicable when
mime\_type is application/json.

typeobject (required)

No description provided.

Always set to `"text"`.

VideoResponseFormat

Configuration for video output format.

aspect\_ratioenum (string) (optional)

The aspect ratio for the video output.

Possible
values:

- `16:9`
16:9 aspect ratio.

- `9:16`
9:16 aspect ratio.


deliveryenum (string) (optional)

The delivery mode for the video output.

Possible
values:

- `inline`
Video data is returned inline in the response.

- `uri`
Video data is returned as a URI.


durationstring (optional)

The duration for the video output.

gcs\_uristring (optional)

The Cloud Storage URI to store the video output. Required for Vertex if
delivery mode is URI.

resolutionenum (string) (optional)

The video output resolution. Defaults to 720p.

Possible
values:

- `360p`
360p resolution.

- `720p`
720p resolution.

- `1080p`
1080p resolution.

- `4k`
4K resolution.


typeobject (required)

No description provided.

Always set to `"video"`.

### Examples

[AudioResponseFormat](https://ai.google.dev/api/interactions-api#audioresponseformat)[ImageResponseFormat](https://ai.google.dev/api/interactions-api#imageresponseformat)[TextResponseFormat](https://ai.google.dev/api/interactions-api#textresponseformat)[VideoResponseFormat](https://ai.google.dev/api/interactions-api#videoresponseformat)More

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

### Step

A step in the interaction.

### Possible Types

CodeExecutionCallStep

Code execution call step.

argumentsCodeExecutionCallStepArguments (required)

Required. The arguments to pass to the code execution.

The arguments to pass to the code execution.

#### Fields

codestring (optional)

The code to be executed.

languageenum (string) (optional)

Programming language of the \`code\`.

Possible
values:

- `python`
Python >= 3.10, with numpy and simpy available.


idstring (required)

Required. A unique ID for this specific tool call.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"code_execution_call"`.

CodeExecutionResultStep

Code execution result step.

call\_idstring (required)

Required. ID to match the ID from the function call block.

is\_errorboolean (optional)

Whether the code execution resulted in an error.

resultstring (required)

Required. The output of the code execution.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"code_execution_result"`.

FileSearchCallStep

File Search call step.

idstring (required)

Required. A unique ID for this specific tool call.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"file_search_call"`.

FileSearchResultStep

File Search result step.

call\_idstring (required)

Required. ID to match the ID from the function call block.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"file_search_result"`.

FunctionCallStep

A function tool call step.

argumentsobject (required)

Required. The arguments to pass to the function.

idstring (required)

Required. A unique ID for this specific tool call.

namestring (required)

Required. The name of the tool to call.

typeobject (required)

No description provided.

Always set to `"function_call"`.

FunctionResultStep

Result of a function tool call.

call\_idstring (required)

Required. ID to match the ID from the function call block.

is\_errorboolean (optional)

Whether the tool call resulted in an error.

namestring (optional)

The name of the tool that was called.

resultarray (FunctionResultSubContent) or object or string (required)

Required. The result of the tool call.

typeobject (required)

No description provided.

Always set to `"function_result"`.

GoogleMapsCallStep

Google Maps call step.

argumentsGoogleMapsCallStepArguments (optional)

The arguments to pass to the Google Maps tool.

The arguments to pass to the Google Maps tool.

#### Fields

queriesarray (string) (optional)

The queries to be executed.

idstring (required)

Required. A unique ID for this specific tool call.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"google_maps_call"`.

GoogleMapsResultStep

Google Maps result step.

call\_idstring (required)

Required. ID to match the ID from the function call block.

resultarray (GoogleMapsResultItem) (required)

No description provided.

The result of the Google Maps.

#### Fields

placesarray (GoogleMapsResultPlaces) (optional)

No description provided.

#### Fields

namestring (optional)

No description provided.

place\_idstring (optional)

No description provided.

review\_snippetsarray (ReviewSnippet) (optional)

No description provided.

Encapsulates a snippet of a user review that answers a question about
the features of a specific place in Google Maps.

#### Fields

review\_idstring (optional)

The ID of the review snippet.

titlestring (optional)

Title of the review.

urlstring (optional)

A link that corresponds to the user review on Google Maps.

urlstring (optional)

No description provided.

widget\_context\_tokenstring (optional)

No description provided.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"google_maps_result"`.

GoogleSearchCallStep

Google Search call step.

argumentsGoogleSearchCallStepArguments (required)

Required. The arguments to pass to Google Search.

The arguments to pass to Google Search.

#### Fields

queriesarray (string) (optional)

Web search queries for the following-up web search.

idstring (required)

Required. A unique ID for this specific tool call.

search\_typeenum (string) (optional)

The type of search grounding enabled.

Possible
values:

- `web_search`
Setting this field enables web search. Only text results are returned.

- `image_search`
Setting this field enables image search. Image bytes are returned.

- `enterprise_web_search`
Setting this field enables enterprise web search.


signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"google_search_call"`.

GoogleSearchResultStep

Google Search result step.

call\_idstring (required)

Required. ID to match the ID from the function call block.

is\_errorboolean (optional)

Whether the Google Search resulted in an error.

resultarray (GoogleSearchResultItem) (required)

Required. The results of the Google Search.

The result of the Google Search.

#### Fields

search\_suggestionsstring (optional)

Web content snippet that can be embedded in a web page or an app webview.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"google_search_result"`.

McpServerToolCallStep

MCPServer tool call step.

argumentsobject (required)

Required. The JSON object of arguments for the function.

idstring (required)

Required. A unique ID for this specific tool call.

namestring (required)

Required. The name of the tool which was called.

server\_namestring (required)

Required. The name of the used MCP server.

typeobject (required)

No description provided.

Always set to `"mcp_server_tool_call"`.

McpServerToolResultStep

MCPServer tool result step.

call\_idstring (required)

Required. ID to match the ID from the function call block.

namestring (optional)

Name of the tool which is called for this specific tool call.

resultarray (FunctionResultSubContent) or object or string (required)

Required. The output from the MCP server call. Can be simple text or rich content.

server\_namestring (optional)

The name of the used MCP server.

typeobject (required)

No description provided.

Always set to `"mcp_server_tool_result"`.

ModelOutputStep

Output generated by the model.

contentarray ( [Content](https://ai.google.dev/api/interactions-api#Resource:Content)) (optional)

No description provided.

typeobject (required)

No description provided.

Always set to `"model_output"`.

ProcessingCallStep

A server-initiated processing step for media analysis (e.g. video
understanding).

idstring (required)

Required. A unique ID for this specific tool call.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"processing_call"`.

ProcessingResultStep

The result of a server-initiated media processing step.

call\_idstring (required)

Required. ID to match the ID from the function call block.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"processing_result"`.

RetrievalCallStep

Retrieval call step.
Used by Vertex Retrieval tools such as Parallel AI, Exa AI, Vertex AI Search,
etc. RetrievalType decides which tool is used.

argumentsRetrievalStepArguments (required)

Required. The arguments to pass to the retrieval tool.

The arguments to pass to Retrieval tools.

#### Fields

queriesarray (string) (optional)

Queries for Retrieval information.

idstring (required)

Required. A unique ID for this specific tool call.

retrieval\_typeenum (string) (optional)

The type of retrieval tools.

Possible
values:

- `rag_store`
The type of retrieval tools.

- `exa_ai_search`
The type of retrieval tools.

- `parallel_ai_search`
The type of retrieval tools.


signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"retrieval_call"`.

RetrievalResultStep

Vertex Retrieval result step.
Used by Vertex Retrieval tools such as Parallel AI, Exa AI, Vertex AI Search,
etc.

call\_idstring (required)

Required. ID to match the ID from the function call block.

is\_errorboolean (optional)

Whether the retrieval resulted in an error.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"retrieval_result"`.

ThoughtStep

A thought step.

signaturestring (optional)

A signature hash for backend validation.

summaryarray (ThoughtContent) (optional)

A summary of the thought.

#### Possible Types

ImageContent

An image content block.

datastring (optional)

The image content.

mime\_typeenum (string) (optional)

The mime type of the image.

Possible
values:

- `image/png`
PNG image format

- `image/jpeg`
JPEG image format

- `image/webp`
WebP image format

- `image/heic`
HEIC image format

- `image/heif`
HEIF image format

- `image/gif`
GIF image format

- `image/bmp`
BMP image format

- `image/tiff`
TIFF image format


resolutionMediaResolution (optional)

The resolution of the media.

#### Possible values

- `low`
Low resolution.

- `medium`
Medium resolution.

- `high`
High resolution.

- `ultra_high`
Ultra high resolution.


typeobject (required)

No description provided.

Always set to `"image"`.

uristring (optional)

The URI of the image.

TextContent

A text content block.

annotationsarray (Annotation) (optional)

Citation information for model-generated content.

Citation information for model-generated content.

#### Possible Types

FileCitation

A file citation annotation.

custom\_metadataobject (optional)

User provided metadata about the retrieved context.

document\_uristring (optional)

The URI of the file.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

file\_namestring (optional)

The name of the file.

media\_idstring (optional)

Media ID in-case of image citations, if applicable.

page\_numberinteger (optional)

Page number of the cited document, if applicable.

sourcestring (optional)

Source attributed for a portion of the text.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

typeobject (required)

No description provided.

Always set to `"file_citation"`.

PlaceCitation

A place citation annotation.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

namestring (optional)

Title of the place.

place\_idstring (optional)

The ID of the place, in \`places/{place\_id}\` format.

review\_snippetsarray (ReviewSnippet) (optional)

Snippets of reviews that are used to generate answers about the
features of a given place in Google Maps.

Encapsulates a snippet of a user review that answers a question about
the features of a specific place in Google Maps.

#### Fields

review\_idstring (optional)

The ID of the review snippet.

titlestring (optional)

Title of the review.

urlstring (optional)

A link that corresponds to the user review on Google Maps.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

typeobject (required)

No description provided.

Always set to `"place_citation"`.

urlstring (optional)

URI reference of the place.

SpeechAnnotation

Speech annotation for text content.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

speakerstring (optional)

The speaker to associate with this turn.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

stylestring (optional)

Style instruction for the speech synthesis.

typeobject (required)

No description provided.

Always set to `"speech_metadata"`.

UrlCitation

A URL citation annotation.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

titlestring (optional)

The title of the URL.

typeobject (required)

No description provided.

Always set to `"url_citation"`.

urlstring (optional)

The URL.

WordInfo

Word-level ASR annotation for transcription output.
Carries the word text, optional timing, and optional speaker attribution.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

end\_offsetstring (optional)

End offset in time of the word relative to the start of the audio.
Present when timestamp\_granularities contains "word".

speakerstring (optional)

Optional. Speaker label for this word (e.g. "spk\_1", "spk\_2").
Present when diarization\_mode is set in TranscriptionConfig.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

start\_offsetstring (optional)

Start offset in time of the word relative to the start of the audio.
Present when timestamp\_granularities contains "word".

textstring (optional)

The transcribed word.

typeobject (required)

No description provided.

Always set to `"word_info"`.

textstring (required)

Required. The text content.

typeobject (required)

No description provided.

Always set to `"text"`.

typeobject (required)

No description provided.

Always set to `"thought"`.

UrlContextCallStep

URL context call step.

argumentsUrlContextCallArguments (required)

Required. The arguments to pass to the URL context.

The arguments to pass to the URL context.

#### Fields

urlsarray (string) (optional)

The URLs to fetch.

idstring (required)

Required. A unique ID for this specific tool call.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"url_context_call"`.

UrlContextResultStep

URL context result step.

call\_idstring (required)

Required. ID to match the ID from the function call block.

is\_errorboolean (optional)

Whether the URL context resulted in an error.

resultarray (UrlContextResult) (required)

Required. The results of the URL context.

The result of the URL context.

#### Fields

statusenum (string) (optional)

The status of the URL retrieval.

Possible
values:

- `success`
Url retrieval is successful.

- `error`
Url retrieval is failed due to error.

- `paywall`
Url retrieval is failed because the content is behind paywall.

- `unsafe`
Url retrieval is failed because the content is unsafe.


urlstring (optional)

The URL that was fetched.

signaturestring (optional)

A signature hash for backend validation.

typeobject (required)

No description provided.

Always set to `"url_context_result"`.

UserInputStep

Input provided by the user.

contentarray ( [Content](https://ai.google.dev/api/interactions-api#Resource:Content)) (optional)

No description provided.

typeobject (required)

No description provided.

Always set to `"user_input"`.

### Examples

[CodeExecutionCallStep](https://ai.google.dev/api/interactions-api#codeexecutioncallstep)[CodeExecutionResultStep](https://ai.google.dev/api/interactions-api#codeexecutionresultstep)[FileSearchCallStep](https://ai.google.dev/api/interactions-api#filesearchcallstep)[FileSearchResultStep](https://ai.google.dev/api/interactions-api#filesearchresultstep)[FunctionCallStep](https://ai.google.dev/api/interactions-api#functioncallstep)[FunctionResultStep](https://ai.google.dev/api/interactions-api#functionresultstep)[GoogleMapsCallStep](https://ai.google.dev/api/interactions-api#googlemapscallstep)[GoogleMapsResultStep](https://ai.google.dev/api/interactions-api#googlemapsresultstep)[GoogleSearchCallStep](https://ai.google.dev/api/interactions-api#googlesearchcallstep)[GoogleSearchResultStep](https://ai.google.dev/api/interactions-api#googlesearchresultstep)[McpServerToolCallStep](https://ai.google.dev/api/interactions-api#mcpservertoolcallstep)[McpServerToolResultStep](https://ai.google.dev/api/interactions-api#mcpservertoolresultstep)[ModelOutputStep](https://ai.google.dev/api/interactions-api#modeloutputstep)[ProcessingCallStep](https://ai.google.dev/api/interactions-api#processingcallstep)[ProcessingResultStep](https://ai.google.dev/api/interactions-api#processingresultstep)[RetrievalCallStep](https://ai.google.dev/api/interactions-api#retrievalcallstep)[RetrievalResultStep](https://ai.google.dev/api/interactions-api#retrievalresultstep)[ThoughtStep](https://ai.google.dev/api/interactions-api#thoughtstep)[UrlContextCallStep](https://ai.google.dev/api/interactions-api#urlcontextcallstep)[UrlContextResultStep](https://ai.google.dev/api/interactions-api#urlcontextresultstep)[UserInputStep](https://ai.google.dev/api/interactions-api#userinputstep)More

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

No examples available for this type.

### EnvironmentConfig

Configuration for a custom environment.

#### Fields

envobject or string (optional)

Environment variables to set in the sandbox environment.

#### Possible Types

object

string

A direct string value.

environment\_idstring (optional)

Optional. The environment ID for the interaction. If specified, the request will
update the existing environment instead of creating a new one.

network[EnvironmentNetworkEgressAllowlist](https://ai.google.dev/api/interactions-api#Resource:EnvironmentNetworkEgressAllowlist) or enum (string) (optional)

Network configuration for the environment.

Possible
values:

- `disabled`
All network egress is blocked.


sourcesarray (Source) (optional)

No description provided.

A source to be mounted into the environment.

#### Fields

contentstring (optional)

The inline content if \`type\` is \`INLINE\`.

encodingstring (optional)

Optional encoding for inline content (e.g. \`base64\`).

sourcestring (optional)

The source of the environment.
For Cloud Storage, this is the Cloud Storage path.
For GitHub, this is the GitHub path.

targetstring (optional)

Where the source should appear in the environment.

typeenum (string) (optional)

No description provided.

Possible
values:

- `gcs`
A Cloud Storage bucket.

- `inline`
Inline content.

- `repository`
A generic repository. The protocol prefix in the source URL
identifies the provider (e.g., github://, gcs://).

- `skill_registry`
A skill resource from the Skill Registry Service.
Skill: projects/{project}/locations/{location}/skills/{skill}
SkillRevision:
projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}
Support mounting all skills under a project:
projects/{project}/locations/{location}/skills.


typeobject (optional)

No description provided.

Always set to `"remote"`.

### EnvironmentNetworkEgressAllowlist

Outbound networking configuration for the sandbox. Accepts an object with an 'allowlist' array to restrict traffic, or the string 'disabled' to turn off all network access. Omit entirely to allow all outbound traffic with no header injection.

#### Possible Types

object

Outbound networking configuration for the sandbox. When specified, restricts which external domains the sandbox can reach. Omit entirely to allow all outbound traffic with no header injection.

allowlistarray (EgressRule) (optional)

List of allowed outbound domains. Only requests to listed domains are permitted. Use \[{'domain': '\*'}\] to allow all domains while still injecting headers on specific ones.

A single domain allowlist rule with optional header injection.

#### Fields

credentialstring (optional)

Optional. Reference to a server-managed Credential resource by ID.

domainstring (optional)

Domain to allow outbound requests to. Supports wildcards (e.g.
'\*.googleapis.com'). Use '\*' to allow all domains.

transformarray (object) or object (optional)

Headers to inject on all outbound requests matching this domain. Accepts a single dict or a list of dicts. The egress proxy injects these automatically.

string

Turns all network off.

#### Possible values

- `disabled`
All network egress is blocked.


### ToolChoiceConfig

The tool choice configuration containing allowed tools.

#### Fields

allowed\_toolsAllowedTools (optional)

The allowed tools.

The configuration for allowed tools.

#### Fields

modeenum (string) (optional)

The mode of the tool choice.

Possible
values:

- `auto`
Auto tool choice.

- `any`
Any tool choice.

- `none`
No tool choice.

- `validated`
Validated tool choice.


toolsarray (string) (optional)

The names of the allowed tools.

### ImageContent

An image content block.

#### Fields

datastring (optional)

The image content.

mime\_typeenum (string) (optional)

The mime type of the image.

Possible
values:

- `image/png`
PNG image format

- `image/jpeg`
JPEG image format

- `image/webp`
WebP image format

- `image/heic`
HEIC image format

- `image/heif`
HEIF image format

- `image/gif`
GIF image format

- `image/bmp`
BMP image format

- `image/tiff`
TIFF image format


resolutionMediaResolution (optional)

The resolution of the media.

#### Possible values

- `low`
Low resolution.

- `medium`
Medium resolution.

- `high`
High resolution.

- `ultra_high`
Ultra high resolution.


typeobject (optional)

No description provided.

Always set to `"image"`.

uristring (optional)

The URI of the image.

### TextContent

A text content block.

#### Fields

annotationsarray (Annotation) (optional)

Citation information for model-generated content.

Citation information for model-generated content.

#### Possible Types

FileCitation

A file citation annotation.

custom\_metadataobject (optional)

User provided metadata about the retrieved context.

document\_uristring (optional)

The URI of the file.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

file\_namestring (optional)

The name of the file.

media\_idstring (optional)

Media ID in-case of image citations, if applicable.

page\_numberinteger (optional)

Page number of the cited document, if applicable.

sourcestring (optional)

Source attributed for a portion of the text.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

typeobject (required)

No description provided.

Always set to `"file_citation"`.

PlaceCitation

A place citation annotation.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

namestring (optional)

Title of the place.

place\_idstring (optional)

The ID of the place, in \`places/{place\_id}\` format.

review\_snippetsarray (ReviewSnippet) (optional)

Snippets of reviews that are used to generate answers about the
features of a given place in Google Maps.

Encapsulates a snippet of a user review that answers a question about
the features of a specific place in Google Maps.

#### Fields

review\_idstring (optional)

The ID of the review snippet.

titlestring (optional)

Title of the review.

urlstring (optional)

A link that corresponds to the user review on Google Maps.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

typeobject (required)

No description provided.

Always set to `"place_citation"`.

urlstring (optional)

URI reference of the place.

SpeechAnnotation

Speech annotation for text content.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

speakerstring (optional)

The speaker to associate with this turn.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

stylestring (optional)

Style instruction for the speech synthesis.

typeobject (required)

No description provided.

Always set to `"speech_metadata"`.

UrlCitation

A URL citation annotation.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

titlestring (optional)

The title of the URL.

typeobject (required)

No description provided.

Always set to `"url_citation"`.

urlstring (optional)

The URL.

WordInfo

Word-level ASR annotation for transcription output.
Carries the word text, optional timing, and optional speaker attribution.

end\_indexinteger (optional)

End of the attributed segment, exclusive.

end\_offsetstring (optional)

End offset in time of the word relative to the start of the audio.
Present when timestamp\_granularities contains "word".

speakerstring (optional)

Optional. Speaker label for this word (e.g. "spk\_1", "spk\_2").
Present when diarization\_mode is set in TranscriptionConfig.

start\_indexinteger (optional)

Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.

start\_offsetstring (optional)

Start offset in time of the word relative to the start of the audio.
Present when timestamp\_granularities contains "word".

textstring (optional)

The transcribed word.

typeobject (required)

No description provided.

Always set to `"word_info"`.

textstring (optional)

Required. The text content.

typeobject (optional)

No description provided.

Always set to `"text"`.

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-09-28 UTC."\],\[\],\[\]\]