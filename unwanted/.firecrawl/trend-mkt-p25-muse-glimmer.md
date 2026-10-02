[BT](https://www.infoq.com/int/bt/ "bt")

## InfoQ Software Architects' Newsletter

A monthly overview of things you need to know as an architect or aspiring architect.

[View an example](https://www.infoq.com/software-architects-newsletter#placeholderPastIssues)

Enter your e-mail address

Select your countrySelect a countryAfghanistanÅlandAlbaniaAlgeriaAmerican SamoaAndorraAngolaAnguillaAntarcticaAntigua and BarbudaArgentinaArmeniaArubaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBonaire, Sint Eustatius, and SabaBosnia and HerzegovinaBotswanaBouvet IslandBrazilBritish Indian Ocean TerritoryBrunei DarussalamBulgariaBurkina FasoBurundiCambodiaCameroonCanadaCape VerdeCayman IslandsCentral African RepublicChadChileChinaChristmas IslandCocos (Keeling) IslandsColombiaComorosCongo (Democratic Republic)Congo (People's Republic)Cook IslandsCosta RicaCote D'IvoireCroatiaCubaCuraçaoCyprusCzech RepublicDenmarkDjiboutiDominicaDominican RepublicEast TimorEcuadorEgyptEl SalvadorEquatorial GuineaEritreaEstoniaEthiopiaFalkland Islands (Malvinas)Faroe IslandsFijiFinlandFranceFrench GuianaFrench PolynesiaFrench Southern TerritoriesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuadeloupeGuamGuatemalaGuernseyGuineaGuinea-BissauGuyanaHaitiHeard Island and McDonald IslandsHondurasHong KongHungaryIcelandIndiaIndonesiaIranIraqIrelandIsle of ManIsraelItalyJamaicaJapanJerseyJordanKazakhstanKenyaKiribatiKosovoKuwaitKyrgyzstanLaosLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgMacauMacedoniaMadagascarMalawiMalaysiaMaldivesMaliMaltaMarshall IslandsMartiniqueMauritaniaMauritiusMayotteMexicoMicronesiaMoldovaMonacoMongoliaMontenegroMontserratMoroccoMozambiqueMyanmarNamibiaNauruNepalNetherlandsNetherlands AntillesNew CaledoniaNew ZealandNicaraguaNigerNigeriaNiueNorfolk IslandNorth KoreaNorthern Mariana IslandsNorwayOmanPakistanPalauPalestinian TerritoryPanamaPapua New GuineaParaguayPeruPhilippinesPitcairnPolandPortugalPuerto RicoQatarReunionRomaniaRussian FederationRwandaSaint HelenaSaint Kitts and NevisSaint LuciaSaint MartinSaint Pierre and MiquelonSaint Vincent and the GrenadinesSaint-BarthélemySamoaSan MarinoSao Tome and PrincipeSaudi ArabiaSenegalSerbiaSeychellesSierra LeoneSingaporeSint MaartenSlovakiaSloveniaSolomon IslandsSomaliaSouth AfricaSouth Georgia and the South Sandwich IslandsSouth KoreaSouth SudanSpainSri LankaSudanSurinameSvalbard and Jan MayenSwazilandSwedenSwitzerlandSyriaTaiwanTajikistanTanzaniaThailandTogoTokelauTongaTrinidad and TobagoTunisiaTurkeyTurkmenistanTurks and Caicos IslandsTuvaluUgandaUkraineUnited Arab EmiratesUnited KingdomUnited States Minor Outlying IslandsUruguayUSAUzbekistanVanuatuVatican City (Holy See)VenezuelaVietnamVirgin Islands (British)Virgin Islands (U.S.)Wallis and FutunaWestern SaharaYemenZaireZambiaZimbabwe

I consent to InfoQ.com handling my data as explained in this [Privacy Notice](https://www.infoq.com/privacy-notice).

[We protect your privacy.](https://www.infoq.com/privacy-notice/)

Close

Live Webinar and Q&A: When AI Accelerates Development, Can Your CI Pipeline Keep Up? (Oct 8, 2026) [Save Your Seat](https://www.infoq.com/url/pb/273a2222-ac40-45d2-b8b6-06c13381e2e2/)

Close


[InfoQ Homepage](https://www.infoq.com/ "InfoQ Homepage")[News](https://www.infoq.com/news "News")Meta Open-Sources Muse Glimmer: a 30B Local Agentic Model Optimised for On-Device Execution

[AI, ML & Data Engineering](https://www.infoq.com/ai-ml-data-eng/ "AI, ML & Data Engineering")

[InfoQ Certified AI-Assisted Engineering Program (online, Oct 19): Build the harness that holds.](https://certification.qconferences.com/ai-assisted-engineering?utm_source=infoq&utm_medium=referral&utm_campaign=infoqyellowbox_onlinecohortaiassistedengineering26)

# Meta Open-Sources Muse Glimmer: a 30B Local Agentic Model Optimised for On-Device Execution

Aug 14, 2026




2
min read



#### Follow us on

[Youtube232K Followers](https://bit.ly/4bg6QM8) [Linkedin26K Followers](https://bit.ly/44IzAtf) [InstagramNew](https://bit.ly/4eYXrtM) [RSS19K Readers](https://bit.ly/3RaJalC) [X57.1k Followers](https://bit.ly/4pfxivv) [Facebook21K Likes](https://bit.ly/3QrGMH2) [BlueskyNew](https://bit.ly/4eS8FjG)

Log in to listen to this article

Loading audio

Your browser does not support the audio element.


0:00

0:00

Normal1.25x1.5x

Like

- [Reading list](https://www.infoq.com/showbookmarks.action)

[Meta AI Research has announced Muse Glimmer](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model), a 30-billion-parameter open-weight model released under the Apache 2.0 license. Engineered specifically for always-on local workflows, Muse Glimmer enables developers to run autonomous agents, complex tool invocation, local coding, and LLM-as-a-judge evaluations directly on consumer GPUs and workstations without depending on cloud APIs.

![](https://www.infoq.com/news/2026/08/meta-muse-glimmer/news/2026/08/meta-muse-glimmer/en/resources/26image1-1786614485447.png)

_Muse Glimmer 30B model architecture and agentic benchmarks. Source: Sebastian Raschka_

To deliver agentic execution within strict memory budgets, Meta employed a multi-stage training strategy derived from its larger flagship model, Muse Spark:

- **Logit Distillation (Pre-training):** The model transfers foundational reasoning capabilities from Muse Spark using a matched pre-training dataset mix.
- **Mid-Training:** Training scales up on long-context sequences containing complex reasoning traces, interleaved text-and-image data, and multi-step tool call trajectories.
- **Post-Training Alignment:** A blend of Supervised Fine-Tuning (SFT), on-policy distillation, and Reinforcement Learning (RL) refines multi-domain performance across code generation, tool usage, and structured planning.

A dedicated 1.8B parameter perception encoder allows Muse Glimmer to process interleaved multimodal inputs natively, enabling local agents to interpret screenshots, diagrams, and documentation inline during code execution or workflow automation.

Uncompressed 30B parameter models typically require over 55 GB of VRAM, pricing them out of standard consumer hardware. Muse Glimmer addresses this via two primary runtime optimisations:

![](https://www.infoq.com/news/2026/08/meta-muse-glimmer/news/2026/08/meta-muse-glimmer/en/resources/1Screenshot%202026-08-13%20at%2012.44.47-1786614485447.png)

**Dynamic Quantisation:** Utilising 4-bit dynamic compression (K-Quant), the model footprint drops to roughly 17 GB to 20 GB. This leaves adequate memory headroom within standard 24 GB to 32 GB GPU/NPU envelopes for the Key-Value (KV) cache, perception embeddings, and speculative decoding overhead.

**DFlash Speculative Decoding:** Rather than predicting one token at a time, Muse Glimmer pairs with a lightweight companion "drafter" model based on the DFlash architecture. The drafter proposes multi-token blocks that the base model validates in parallel, yielding up to a 3.1x increase in generation throughput on hardware like Apple Silicon (M4/M5 Max) and NVIDIA RTX 5090 cards.

Muse Glimmer is trained to execute long-horizon plans and handle unexpected failure states. When an API call or terminal command returns an error, the model diagnoses the failure and attempts alternative paths rather than terminating execution. It supports agent frameworks like OpenClaw and features adjustable reasoning effort, allowing developers to balance execution speed against decision quality.

In standardised benchmark evaluations( SWE-Bench, DeepSearch QA, τ-Bench, and MCP-Atlas) Muse Glimmer achieves strong success rates compared to leading open models in the 30B class. When evaluated against peer models such as Gemma 4 31B and Qwen 3.6 27B, Muse Glimmer demonstrates superior multi-step tool reliability and failure recovery while maintaining competitive general coding and reasoning capabilities.

The model weights are available on Hugging Face. Meta has partnered with the open-source community to provide native execution across popular local frameworks, including llama.cpp, ExecuTorch, Apple MLX, Ollama, LM Studio, and vLLM. Fine-tuning workflows are also supported via PyTorch's TorchTitan framework.

Muse Glimmer represents a significant shift toward viable, high-capability local AI agents that safeguard data privacy while maintaining low-latency execution. To run this model effectively on your own machine, a system equipped with 24 GB to 32 GB of unified memory or VRAM is recommended—such as a Mac with an M4/M5 Max chip or a PC with a modern GPU like the RTX 5090 or RTX 4090. This hardware envelope ensures sufficient memory for the quantised 4-bit weights alongside the vision encoder, DFlash drafter, and KV context cache required for extended agentic sessions.

## About the Author

[![Olimpiu Pop](https://cdn.infoq.com/statics_s2_20261001082741/images/profiles/xdEJUM0sXSfDbXIFRMaailphJmX1ZcmX.jpg)](https://www.infoq.com/profile/Olimpiu-Pop/)

#### **Olimpiu Pop**

Tech Executive and Engineer Focused on a Holistic Approach and using technology to provide solutions to real problems with minimal impact on the environment. He has experience in developing real-time applications ranging from financial software to IAM. Passionate about tooling and optimising development flows with or without AI. Led and shaped technical organisations of hundreds of developers (from support engineers to Architects).
Tech community builder: Transylvania JUG facilitator, member of the program committee for Voxxed Romania and Devoxx UK, conference speaker and podcaster on cybersecurity and open-source topics for 505updates.com. Main editor and troublemaker of JavaAdventCalendar.

Show moreShow less

- #### Popular in AI, ML & Data Engineering



  - ##### [Google Open-Sources AX a Kubernetes Style Orchestrator for Autonomous AI Agents](https://www.infoq.com/news/2026/09/google-ax-orchestrator/ "")

  - ##### [Beyond Kubernetes at Modal: How to Scale 1 Million Concurrent Sandboxes in Seconds](https://www.infoq.com/news/2026/09/modal-scaling-sandboxes/ "")

  - ##### [Graphify: Unifying Codebase Context to Streamline Agentic Software Engineering](https://www.infoq.com/news/2026/09/graphify-codebase-exploration/ "")

  - ##### [Stateless MCP Removes Session Affinity Requirements for AWS Server Deployments](https://www.infoq.com/news/2026/09/aws-stateless-mcp/ "")

  - ##### [Alibaba Open Sources OpenCodeReview for AI-Assisted Code Review](https://www.infoq.com/news/2026/09/alibaba-opencodereview/ "")


#### Related Sponsors

  - ##### [Beyond the Data Lake: Building AI-Ready Data Foundations for Agentic AI](https://www.infoq.com/vendorcontent/show.action?vcr=216a3114-ceef-4bfc-ad6a-08ec5bc8cc51&primaryTopicId=4523&vcrPlace=BOTTOM&pageType=NEWS_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fnews%2F2026%2F08%2Fmeta-muse-glimmer%2F)

  - ##### [When AI Accelerates Development, Can Your CI Pipeline Keep Up? (Live Webinar October 8, 2026) - Save Your Seat](https://www.infoq.com/vendorcontent/show.action?vcr=6d71a148-a5f6-4736-b69e-687cf88f4ef2&primaryTopicId=4523&vcrPlace=BOTTOM&pageType=NEWS_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fnews%2F2026%2F08%2Fmeta-muse-glimmer%2F)

  - ##### [How Morgan Stanley Is Scaling Software Modernization with Automated Refactoring](https://www.infoq.com/vendorcontent/show.action?vcr=2c235f81-3999-49e9-b6d7-107b14946621&primaryTopicId=4523&vcrPlace=BOTTOM&pageType=NEWS_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fnews%2F2026%2F08%2Fmeta-muse-glimmer%2F)

  - ##### [Understanding Postgres Performance Limits for Analytics on Live Data](https://www.infoq.com/vendorcontent/show.action?vcr=a7d3e79b-c1f0-48c9-a1ef-84a625436518&primaryTopicId=4523&vcrPlace=BOTTOM&pageType=NEWS_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fnews%2F2026%2F08%2Fmeta-muse-glimmer%2F)

  - ##### [From Tokens to Features: Architecting Cost Attribution for AI-Assisted Engineering (Live Webinar October 29, 2026) - Save Your Seat](https://www.infoq.com/vendorcontent/show.action?vcr=cb891241-1041-45a8-8a57-757a73bdbbcd&primaryTopicId=4523&vcrPlace=BOTTOM&pageType=NEWS_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fnews%2F2026%2F08%2Fmeta-muse-glimmer%2F)
- #### Related Sponsor

[![Related sponsor icon](https://imgopt.infoq.com//fit-in/218x500/filters:quality(100)/filters:no_upscale()/sponsorship/topic/01c3ec08-be6b-4257-a1bb-791a3b43efbf/HarnessWebinarOct29-RSB-1790089548054.png)](https://www.infoq.com/url/f/99c3ecb1-6ab2-4f92-a238-716411126d94/)



  - October 29, 2026, 1 PM EDT

    ##### [From Tokens to Features: Architecting Cost Attribution for AI-Assisted Engineering](https://www.infoq.com/url/f/7dd9ac94-cd65-4b0e-a0ed-107843fe3c08/)


    [Presented by: Martin Reynolds - Field CTO at Harness](https://www.infoq.com/url/f/3653a3d7-6e45-464b-b6f6-57287daf9ce9/)


[BT](https://www.infoq.com/int/bt/ "bt")