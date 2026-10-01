[Skip to main content](https://build.nvidia.com/nvidia/cosmos3-nano-reasoner#main-content)

[![NVIDIA](https://build.nvidia.com/_next/image?url=%2Fnvidia-logo.png&w=600&q=75)](https://build.nvidia.com/)

[Explore](https://build.nvidia.com/explore/discover) [Models](https://build.nvidia.com/models) [Skills](https://build.nvidia.com/skills) [Blueprints](https://build.nvidia.com/blueprints) [GPUs](https://brev.nvidia.com/environment/new/public) [Docs](https://docs.api.nvidia.com/)

Search `⌘KCtrl+K`

?

Help Center

Getting Started

1. 1
Set up your account

Create and verify your account to unlock full access to NVIDIA NIM APIs.

Create an Account

2. 2
Generate API Key

3. 3
Make your first API call

4. 4
Prototype in your environment

5. 5
Connect to inference partners


Resources [Developer Forums](https://forums.developer.nvidia.com/c/ai-data-science/nvidia-nim/678) [Contact Support](mailto:help@build.nvidia.com)

FAQs

- Are all models free to use?


All models on [build.nvidia.com](https://build.nvidia.com/) are free to prototype with. Once you hit rate limits, see the Deploy section to use partner endpoints or deploy a NIM locally.

- How many requests can I make?


The free tier runs on rate limits - up to 40 requests per minute (RPM) for most models, with no per-token billing. Your personal rate limit is shown in the top-right of the dashboard.

- Why are the API endpoints free?


We believe open model inference offers the best cost-performance for most workloads. The free tier exists so you can verify that yourself before committing to anything.

- How do I choose the right model?


Each model page lists benchmarks, supported tasks, and context window. When in doubt, use the playground to test before you integrate.

- How do I deploy to my own infrastructure?


Download a NIM container and run it on your own cloud, via a CSP partner (AWS, Azure, GCP, OCI), or on a Brev GPU instance. The API is identical - no code changes required.

- What is NemoClaw?


NemoClaw is a sandboxed runtime for autonomous agents. Network requests, file access, and inference calls are all policy-gated. Nothing is permitted by default.


Login

![](https://build.nvidia.com/_next/image?url=https%3A%2F%2Fassets.ngc.nvidia.com%2Fproducts%2Fapi-catalog%2Fimages%2Fcosmos3-nano-reasoner.jpg&w=3840&q=75)

[NVIDIA](https://build.nvidia.com/nvidia)

# cosmos3-nano-reasoner

DownloadableFree Endpoint

Vision language model that excels in understanding the physical world using structured reasoning on videos or images.

- [Physical AI](https://build.nvidia.com/models?label=Physical+AI)
- [autonomous vehicles](https://build.nvidia.com/models?label=autonomous+vehicles)
- [industrial](https://build.nvidia.com/models?label=industrial)
- [reasoning](https://build.nvidia.com/models?label=reasoning)
- [robotics](https://build.nvidia.com/models?label=robotics)
- [smart cities](https://build.nvidia.com/models?label=smart+cities)
- [Synthetic Data Generation](https://build.nvidia.com/models?filters=usecase%3Ausecase_sdg)
- [video understanding](https://build.nvidia.com/models?label=video+understanding)
- [vision language model](https://build.nvidia.com/models?label=vision+language+model)

[Download Now](https://build.nvidia.com/nvidia/cosmos3-nano-reasoner?modal=fine-tune)

ExperienceExperienceModel CardModel CardDeployDeploySystem CardSystem Card

[Accelerated by DGX Cloud](https://www.nvidia.com/en-us/data-center/dgx-cloud/)

## Before You Use AI Models

NVIDIA hosts a variety of AI models for developers and businesses to explore and evaluate.

**Model Outputs.** AI models generate responses and outputs that may be inaccurate, harmful, biased or indecent. NVIDIA hosts third-party models that could contain political content or potentially misleading information. NVIDIA does not endorse, verify or assume responsibility for a third-party model. By using an API Service, you assume the risk of any harm caused by any response or output of any model.

**Privacy.** Your input and output will be recorded to provide you with this trial experience and to improve NVIDIA products and services, including AI models, in accordance with our [Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/). Do not upload any confidential information or personal data unless expressly permitted. Your use is logged for security, fraud or abuse monitoring and shared with third party service providers for this purpose. If the demo necessarily requires the input of personal data, logging for product development purposes will be turned off.

By clicking Acknowledge and Continue you consent to such processing and agree to the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf).

Please contact us if you might want to develop guardrails to manage prompt inputs and outputs.

Acknowledge & Continue

Close Modal

### Input

View Examples

Input

Drop files here.mp4, .jpg, .jpeg, .png

.mp4.jpg.jpeg.png

Upload Video or Image

User Prompt

Your question or task. Aim for up to 400 tokens (300 words); max 1000 tokens. Model can accommodate reasoning or non-reasoning answers. Enable reasoning by including this text string in the user prompt: Answer the question using the following format:<think>Your reasoning.</think> Write your final answer immediately after the </think> tag

Your question or task. Aim for up to 400 tokens (300 words); max 1000 tokens. Model can accommodate reasoning or non-reasoning answers. Enable reasoning by including this text string in the user prompt: Answer the question using the following format:<think>Your reasoning.</think> Write your final answer immediately after the </think> tag

182/4000

System Prompt

Defines AI role/rules for session. Max 250 tokens.

Defines AI role/rules for session. Max 250 tokens.

28/250

View Parameters

Temperature

Controls the randomness and creativity of responses. Lower values (0.1-0.5) produce more focused, deterministic outputs suitable for factual tasks. Higher values (0.6-2.0) generate more creative, varied responses but may be less predictable. Default 0.6.

00.250.50.751

Top P

Nucleus sampling threshold that dynamically selects tokens based on cumulative probability. Lower values (0.1-0.5) restrict selection to highly probable tokens for more focused responses. Higher values (0.7-1.0) allow broader token selection for increased diversity. Default 0.9.

0.010.260.510.761

Repetition Penalty

Reduces the likelihood of repeating words or phrases by penalizing tokens that have already appeared. Values above 1.0 discourage repetition, while values below 1.0 encourage it. Higher values create more varied responses but may affect coherence. Default 1.0.

11.31.51.82

Seed

If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result.

Reasoning

Controls whether the model shows its step-by-step thinking process (chain-of-thought) or provides only the final answer. When enabled, reasoning mode helps solve complex problems more accurately but uses more computational resources.

ResetRun

### Output

PreviewPreviewJSONJSON

## Reasoning Complete

Below is the entire thinking process the model went through to arrive at its response.

Collapse

Okay, let's see. The video has two robot arms. Robot Arm 1 is holding a yellow object on the left, not moving. Robot Arm 2 is on the right and has just picked up a white object from the table. The white object was near the air column wrap, which is on the right side next to the cardboard box. The air column wrap is partially unrolled, so maybe it's for packaging.

Since Robot Arm 2 has lifted the white object, the next step would likely be moving it towards the cardboard box. The box is open and has plastic-wrapped items inside. The white object might be placed into the box, possibly to be packed with the other items. Since the air column wrap is nearby, maybe they use it to cushion the item. So the next action is probably moving the white object to the box and placing it inside, maybe using the air column wrap for protection. But since the air column wrap is stationary, maybe the robot just places the white object into the box. Alternatively, the robot might position the white object near the air column wrap to wrap it, but since the air column wrap is already there, maybe the next immediate step is placing the white object into the box. So the answer should be that Robot Arm 2 moves the white object towards the cardboard box to place it inside.

Reasoning Complete

Response

Robot Arm 2 places the white object into the cardboard box

hCaptcha

[Terms of Use](https://developer.nvidia.com/legal/terms)

[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/)

[Your Privacy Choices](https://www.nvidia.com/en-us/about-nvidia/privacy-center/)

[Contact](https://developer.nvidia.com/contact)

Copyright © 2026 NVIDIA Corporation

hCaptcha

Please try again. ⚠️

Verify

Afrikaans

Albanian

Amharic

Arabic

Armenian

Azerbaijani

Basque

Belarusian

Bengali

Bulgarian

Bosnian

Burmese

Catalan

Cebuano

Chinese

Chinese Simplified

Chinese Traditional

Corsican

Croatian

Czech

Danish

Dutch

English

Esperanto

Estonian

Finnish

French

Frisian

Gaelic

Galacian

Georgian

German

Greek

Gujurati

Haitian

Hausa

Hawaiian

Hebrew

Hindi

Hmong

Hungarian

Icelandic

Igbo

Indonesian

Irish

Italian

Japanese

Javanese

Kannada

Kazakh

Khmer

Kinyarwanda

Kirghiz

Korean

Kurdish

Lao

Latin

Latvian

Lithuanian

Luxembourgish

Macedonian

Malagasy

Malay

Malayalam

Maltese

Maori

Marathi

Mongolian

Nepali

Norwegian

Nyanja

Oriya

Persian

Polish

Portuguese (Brazil)

Portuguese (Portugal)

Pashto

Punjabi

Romanian

Russian

Samoan

Shona

Sindhi

Sinhalese

Serbian

Slovak

Slovenian

Somali

Southern Sotho

Spanish

Sundanese

Swahili

Swedish

Tagalog

Tajik

Tamil

Tatar

Teluga

Thai

Turkish

Turkmen

Uyghur

Ukrainian

Urdu

Uzbek

Vietnamese

Welsh

Xhosa

Yiddish

Yoruba

Zulu

EN

[hCaptcha logo, opens new window with more information](https://www.hcaptcha.com/what-is-hcaptcha-about?ref=build.nvidia.com&utm_campaign=0c6a1e45-75d7-43cc-b836-a0c9d886b8ee&utm_medium=challenge&hl=en "hCaptcha logo, opens new window with more information")