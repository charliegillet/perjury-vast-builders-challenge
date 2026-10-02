[Skip to main content](https://ai.google.dev/gemini-api/docs/caching#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/caching)
- [Deutsch](https://ai.google.dev/gemini-api/docs/caching?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/caching?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/caching?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/caching?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/caching?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/caching?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/caching?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/caching?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/caching?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/caching?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/caching?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/caching?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/caching?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/caching?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/caching?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/caching?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/caching?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/caching?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)Sign in

- On this page
- [Implicit caching](https://ai.google.dev/gemini-api/docs/caching#implicit-caching)

Gemini 3.8 Flash is now available. [Try it out](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Docs](https://ai.google.dev/gemini-api/docs)

Interactions API (Recommended)generateContent APILearn more

Select an optionInteractions API (Recommended)

- [Interactions API (Recommended)](https://ai.google.dev/gemini-api/docs/caching)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content/caching)
- [Learn more](https://ai.google.dev/gemini-api/docs/interactions)



 Send feedback



# Context caching

- On this page
- [Implicit caching](https://ai.google.dev/gemini-api/docs/caching#implicit-caching)

In a typical AI workflow, you might pass the same input tokens over and over to
a model. The Gemini API offers implicit caching to optimize performance and costs.

## Implicit caching

Implicit caching is enabled by default for all Gemini 2.5 and newer models. It is
supported for both [stateful](https://ai.google.dev/gemini-api/docs/text-generation#multi-turn-conversations) (using `previous_interaction_id`)
and [stateless](https://ai.google.dev/gemini-api/docs/text-generation#stateless-conversations) conversation modes.
We automatically pass on cost savings if your request hits caches. There is nothing you need to do
in order to enable this. The minimum input
token count for context caching is listed in the following table for each model:

| Model | Min token limit |
| --- | --- |
| Gemini 3.8 Flash | 4,096 |
| Gemini 3.7 Flash | 4,096 |
| Gemini 3.6 Flash | 4,096 |
| Gemini 3.5 Flash | 4,096 |
| Gemini 3.1 Pro Preview | 4,096 |
| Gemini 2.5 Flash | 2,048 |
| Gemini 2.5 Pro | 2,048 |

To increase the chance of an implicit cache hit:

- Try putting large and common contents at the beginning of your prompt
- Try to send requests with similar prefix in a short amount of time

You can see the number of tokens which were cache hits in the response object's
`usage.total_cached_tokens` (Python and JavaScript) field.



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-09-02 UTC."\],\[\],\[\]\]