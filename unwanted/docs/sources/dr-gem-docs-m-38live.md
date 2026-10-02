[Skip to main content](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live)
- [Deutsch](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fmodels%2Fgemini-3.8-live&prompt=select_account)

- On this page
- [Documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live#documentation)
- [gemini-3.8-live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live#gemini-3.8-live)
- [Migrating from Gemini 3.1 Flash Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live#migrating)

Gemini 3.8 Flash is now available. [Try it out](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Docs](https://ai.google.dev/gemini-api/docs)



 Send feedback



# Gemini 3.8 Live

- On this page
- [Documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live#documentation)
- [gemini-3.8-live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live#gemini-3.8-live)
- [Migrating from Gemini 3.1 Flash Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live#migrating)

Gemini 3.8 Live is the default option for most low-latency voice agent
experiences and real-time dialogue without reasoning-induced delays. It supports
interleaved reasoning, asynchronous function calling, full session client
content updates, and built-in audio streaming.

[Try in Google AI Studio](https://aistudio.google.com/live?model=gemini-3.8-live)

## Documentation

Visit the [Live API](https://ai.google.dev/gemini-api/docs/live-api) guide for full coverage
of features and capabilities.

## gemini-3.8-live

| Property | Description |
| --- | --- |
| id\_cardModel code | `gemini-3.8-live` |
| saveSupported data types | **Inputs**<br>Text, images, audio, video<br>**Output**<br>Text and audio |
| token\_autoToken limits[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens) | **Input token limit**<br>131,072<br>**Output token limit**<br>65,536 |
| handymanCapabilities | **[Audio generation](https://ai.google.dev/gemini-api/docs/speech-generation)**<br>Supported<br>**[Caching](https://ai.google.dev/gemini-api/docs/caching)**<br>Not supported<br>**[Code execution](https://ai.google.dev/gemini-api/docs/code-execution)**<br>Not supported<br>**[File search](https://ai.google.dev/gemini-api/docs/file-search)**<br>Not supported<br>**[Function calling](https://ai.google.dev/gemini-api/docs/function-calling)**<br>Supported<br>**[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding)**<br>Not supported<br>**[Image generation](https://ai.google.dev/gemini-api/docs/image-generation)**<br>Not supported<br>**[Live API](https://ai.google.dev/gemini-api/docs/live-api)**<br>Supported<br>**[Search grounding](https://ai.google.dev/gemini-api/docs/google-search)**<br>Supported<br>**[Structured outputs](https://ai.google.dev/gemini-api/docs/structured-output)**<br>Not supported<br>**[Thinking](https://ai.google.dev/gemini-api/docs/thinking)**<br>Supported (interleaved reasoning)<br>**[URL context](https://ai.google.dev/gemini-api/docs/url-context)**<br>Not supported |
| speedConsumption options | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api)**<br>Not supported |
| 123Versions | Read the [model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions) for more details.<br>- Stable: `gemini-3.8-live` |
| calendar\_monthLatest update | September 2026 |
| id\_cardModel card | [Model card](https://deepmind.google/models/model-cards/gemini-3-8-audio/) |

## Migrating from Gemini 3.1 Flash Live

Gemini 3.8 Live delivers ultra-low latency audio-to-audio interactions
and expands support for asynchronous workflows. When migrating from
`gemini-3.1-flash-live-preview`, review the following updates:

- **Model string**: Update your model string from
`gemini-3.1-flash-live-preview` to `gemini-3.8-live`.
- **Thinking level**: `thinking_level` is not supported for `gemini-3.8-live`.
Omit `thinking_level` (or `thinking_config`) from your session setup.
- **Asynchronous function calling**: Async execution (`behavior: NON_BLOCKING`)
is now the default function calling mode. You can still use synchronous
blocking mode for backwards compatibility by setting `behavior: BLOCKING` on
your tool declarations. Function scheduling (`SILENT`, `WHEN_IDLE`,
`INTERRUPTED`) is supported.
- **Client content updates**: `send_client_content` is supported throughout the
entire session lifecycle with explicit roles (`user` or `model`). Setting
`turn_complete=true` unconditionally interrupts active model generation. If
you send content without `turn_complete`, the server waits for subsequent
messages before responding.
- **Proactive audio**: Proactive audio is now permanently enabled. Setting
`proactive_audio: false` returns an error.
- **Affective dialogue**: Affective dialogue is removed from the API. Remove
any `enable_affective_dialog` configurations from your code.
- **Turn coverage**: Defaults to
`TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO`. Video frames are sent to the
model by default, so only send frames when needed to manage context and cost.
- **Response modalities**: Audio is the supported response modality. Enable
output audio transcription if your application requires a text transcript.

For a feature comparison across all Live API models, see the
[Model comparison](https://ai.google.dev/gemini-api/docs/live-api/capabilities#model-comparison)
table.



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-09-15 UTC."\],\[\],\[\]\]