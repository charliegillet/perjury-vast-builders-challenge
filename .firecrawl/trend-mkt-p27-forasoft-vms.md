# AI-Native Platforms: Ambient.ai, Spot AI, Eagle Eye Networks

![Nikolay Sapunov](https://cdn.prod.website-files.com/64e8910adc5a63966a68acea/6a0c72a04c29b22a8ddb991b_6a0c728d356dff40621f0967_nikolay_sapunov.avif)

By

Nikolay Sapunov

·

Published

June 10, 2026

·

21

min read

TL;DR

The platforms in this profile — Eagle Eye Networks, Spot AI, and Ambient.ai — were built around analytics and the cloud from the first line of code, rather than being recording software that later bolted artificial intelligence on, and that origin shapes everything about how they behave, cost, and lock you in. They are not three versions of the same product: Eagle Eye Networks is a full cloud Video Management System that replaces your recorder, Spot AI is an AI camera system and intelligence layer that turns cameras into agents that act, and Ambient.ai is a threat-detection layer that sits on

## Why this matters

If you are choosing a Video Management System (the software platform that ingests, records, and manages many camera streams, abbreviated VMS), the established platforms profiled earlier in this block — [Milestone XProtect](https://www.forasoft.com/learn/video-surveillance/articles-vms/milestone-xprotect), [Genetec Security Center](https://www.forasoft.com/learn/video-surveillance/articles-vms/genetec-security-center), and [Avigilon under Motorola Solutions](https://www.forasoft.com/learn/video-surveillance/articles-vms/avigilon-motorola-solutions) — are only half the market. A newer group of vendors rebuilt the VMS around two ideas the incumbents added later: artificial intelligence as the point of the system, not a feature, and the cloud as the default home, not an option. This profile is for a security integrator, product manager, retail or operations lead, or enterprise security lead deciding whether an analytics-first, cloud-first platform fits — and what it really trades away. Read it to understand what "AI-native" buys you, how Eagle Eye Networks, Spot AI, and Ambient.ai differ from each other, and where each one fits before you put it on a shortlist.

## What "AI-native" actually means

Every VMS vendor says it has artificial intelligence now, so the phrase needs a precise meaning or it is just a sticker. The useful distinction is architectural, and it comes down to the order the system was built in.

The established platforms began life as recording software. Their first job — and the thing they are still superb at — was to take many camera streams, write them to disk reliably, and let an operator watch and search them. Analytics arrived later, as a module you add, a server you stand up, or a camera you buy. That is not a criticism; a recorder that never drops a frame under load is hard engineering, and we said so in the [Milestone](https://www.forasoft.com/learn/video-surveillance/articles-vms/milestone-xprotect) and [Genetec](https://www.forasoft.com/learn/video-surveillance/articles-vms/genetec-security-center) profiles. But the artificial intelligence is a layer on top of a recording core.

An **AI-native** platform inverts that order. It was designed from the start so that understanding the video — detecting, classifying, reasoning about what is happening — is the primary job, and recording is in service of that. Think of the difference between a filing cabinet that someone later taught to read, and a reader that also keeps files. Both hold your documents; only one was built to understand them first. In practice "AI-native" almost always travels with "cloud-native," because the computing power to run modern vision models across hundreds of cameras is cheaper and more elastic to rent in a data center than to buy and rack at every site. The trade is that the video, or at least the analytics on it, now depends on a network link and a subscription.

![Two panels compared. The incumbent VMS, built recorder-first, stacks a thin box marked 2, AI added later - a layer on the recorder, on top of a filled box marked 1, Recording core - the foundation. The AI-native platform, built analytics-first, puts a filled box marked 1, Understanding video - the core job, on top of a box marked 2, Recording - in service of it. Captions read Analytics is a module you add and Compute usually rented in the cloud; the key reads 1 built first, 2 added after.](https://cdn.prod.website-files.com/64e8910adc5a63966a68acea/6aad7c1b81b1374291233e23_6aad7adb81b137429122f047_07_5-ai-native-vms-ambient-spot-eagle-eye__01-ai-native-vs-incumbent.svg)_Figure 1. Two build orders. The incumbent VMS started as a recorder and added artificial intelligence as a layer; the AI-native platform was built so understanding the video is the core job, with recording in service of it, usually in the cloud. Neither is "better" in the abstract — they fit different buyers._

One honest caveat belongs here, before any vendor name. "AI-native" describes how a system is built, not how accurate it is. A platform designed around analytics still produces a precision-and-recall range — a realistic rate of correct detections against missed ones and false alarms — that depends on scene, lighting, angle, and tuning, exactly as every analytic does. Being analytics-first tends to mean the detection is better integrated and easier to use, not that it is perfect. We treat that reality in depth in [tuning analytics: false alarms and accuracy](https://www.forasoft.com/learn/video-surveillance/articles-vms/tuning-analytics-false-alarms-accuracy), and we will hold every vendor in this profile to it.

## Three platforms, three different animals

The biggest mistake a buyer makes with this category is treating the three as interchangeable "AI camera companies." They occupy meaningfully different positions, and the cleanest way to see it is to ask one question: _what does this platform replace?_

**Eagle Eye Networks replaces your recorder and your VMS.** It is a full cloud VMS — the system of record. You point cameras at it, it stores and manages the video, and operators live in its interface. If you adopt Eagle Eye, it is your VMS.

**Spot AI replaces your cameras-and-recorder with an AI camera system, or layers onto the ones you have.** It sells its own cameras and an on-site appliance, but its pitch is that it is the _intelligence layer_ — it can also work with the cameras you already own and turn them into what it calls Video AI Agents that not only watch but act.

**Ambient.ai replaces nothing.** It is a threat-detection layer that sits on top of the cameras and the VMS you already run, reads their feeds, and raises alerts. You keep your recorder; Ambient.ai is the brain you bolt onto it.

Hold that spectrum — overlay, intelligence layer, full platform — because it determines whether one of these is a rip-and-replace decision or an add-on, and it changes who else at the table needs to approve it.

![A left-to-right spectrum with three numbered stops - Overlay, Intelligence layer, Full platform - running from adds on to what you have to becomes your system of record. Three matching cards follow. 1 Ambient.ai, threat-detection overlay, replaces nothing, an add-on decision: sits on the cameras and VMS you run, reads the feeds and raises live alerts, no facial recognition by design. 2 Spot AI, AI cameras plus intelligence, replaces cameras and recorder or layers on: own cameras and an edge appliance, also works with the cameras you own, Video AI Agents act rather than only alert. 3 Eagle Eye Networks, full cloud VMS, replaces your recorder and your VMS: becomes your system of record, records and manages in the cloud, camera-agnostic over ONVIF.](https://cdn.prod.website-files.com/64e8910adc5a63966a68acea/6aad7c1b81b1374291233e2c_6aad7b47b253c5c9321643ce_07_5-ai-native-vms-ambient-spot-eagle-eye__02-positioning-spectrum.svg)_Figure 2. What does it replace? Ambient.ai overlays the cameras and VMS you already own; Spot AI is an AI camera system and intelligence layer that can also work with existing cameras; Eagle Eye Networks is a full cloud VMS that becomes your system of record. The further right, the bigger the switch._

## Eagle Eye Networks: the cloud VMS

Of the three, Eagle Eye Networks is the one that looks most like a traditional VMS — because it is one, rebuilt for the cloud. Understanding its history explains why it behaves the way it does.

Eagle Eye Networks was founded in 2012 by Dean Drako, who had previously founded and run Barracuda Networks, the company that shipped the IT-security industry's first spam-filter appliance and grew, from 2003 to 2012, to more than 200 million US dollars in annual sales and 150,000 customers. Drako brought an internet-infrastructure mindset to surveillance: build it in the cloud, secure it like an IT product, and expose it through a programming interface. The first product, the Eagle Eye Cloud Security Camera VMS, was announced in early 2014, and the platform has been a cloud VMS ever since rather than a desktop product later moved online.

The architecture answers the obvious objection to cloud surveillance — that you cannot push every camera's full-resolution video to a data center over an ordinary internet link. Eagle Eye offers two ways in. The first is the **Bridge**: an on-site appliance that sits between the cameras and the cloud, takes the heavy local video stream, isolates the cameras from the public internet for security, and sends up only what is needed — a model we explained as the edge-buffer pattern in [cloud and hybrid storage for surveillance](https://www.forasoft.com/learn/video-surveillance/articles-vms/cloud-hybrid-storage-for-surveillance). The Bridge suits large single-site deployments with serious camera counts. The second is **Camera Direct**: newer cameras that connect straight to the cloud with no on-site appliance at all, for simpler or smaller sites. Either way, the system of record is the cloud, and recording can be kept in the cloud, on-premises, or both.

Two engineering choices make Eagle Eye truly open at the camera layer, which matters because cloud platforms are often assumed to be closed. First, it is camera-agnostic: it captures video and runs its analytics on cameras from across the market — its materials cite support for several thousand camera models — by speaking **ONVIF**, the common language that lets cameras and video software from different makers work together. Eagle Eye is an ONVIF member, and it can ingest and analyze video from effectively any ONVIF-conformant camera, which is why adopting it rarely means replacing your cameras. The mechanics of that standard are in [ONVIF explained for engineers](https://www.forasoft.com/learn/video-surveillance/articles-vms/onvif-explained-for-engineers). Second, it exposes a developer-friendly web Application Programming Interface (API) — a published way for other software to pull video, events, and analytics in and out — which integrators have used to wire Eagle Eye into alarm monitoring, point-of-sale systems, and third-party dashboards.

The analytics follow the cloud-native promise: most run on the cameras you already have, with no special hardware. Eagle Eye's suite includes Smart Video Search, license-plate recognition (which it markets as working with ordinary cameras rather than dedicated plate cameras), gun detection, person and vehicle detection, heat-mapping and occupancy analytics, and perimeter intrusion detection. Two of those — plate reading and any future face matching — walk a deployment up to a legal gate, and we will return to that in the openness and privacy sections. Commercially, the platform is sold the cloud-native way: a usage-based subscription per camera rather than a one-time licence, bundling the recording, storage, updates, and analytics into a recurring fee.

The most important current fact about Eagle Eye is corporate, not technical. In late December 2025, Eagle Eye Networks merged with Brivo, a cloud-based access-control company, to form what the two companies described as the industry's largest cloud-native physical-security business. The combined company operates under the Brivo name, with Dean Drako as chief executive; the Eagle Eye Cloud VMS becomes the video pillar of a broader "Brivo Security Suite" that spans access control, video, visitor management, and intrusion. For a buyer evaluating Eagle Eye today, that means two things: the cloud VMS itself continues, and the strategic direction is now a unified access-plus-video cloud platform rather than video alone. It is a recent change, and like any post-merger integration it is one to watch as the product roadmaps combine.

![A top-to-bottom flow. ONVIF cameras, any conformant brand across several thousand models, split into two routes: a Bridge appliance for large sites that buffers and secures, and Camera Direct for simple sites that goes straight to the cloud. Both feed the Eagle Eye Cloud VMS, which records in the cloud, on-premises or both, runs analytics on the cameras you already have, and offers Smart Video Search, LPR and gun, person and vehicle detection; a highlighted row notes that plate reading and face matching cross a legal gate. The cloud VMS serves operators with live and recorded video and an open REST API that gets events and video out.](https://cdn.prod.website-files.com/64e8910adc5a63966a68acea/6aad7c1b81b1374291233e29_6aad7b4814ad05066d58dbda_07_5-ai-native-vms-ambient-spot-eagle-eye__03-eagle-eye-architecture.svg)_Figure 3. Eagle Eye Networks, end to end. ONVIF cameras reach the cloud either through an on-site Bridge appliance (large sites) or Camera Direct (simpler sites); the cloud VMS records, runs analytics on existing cameras, and serves operators and an open API. The system of record lives in the cloud._

## Spot AI: the AI camera system that acts

Spot AI starts from a different question than Eagle Eye. Eagle Eye asked, "what does a VMS look like if you build it in the cloud?" Spot AI asks, "what if the camera were a teammate that could act, not just a sensor that records?"

The company was founded in 2018 by three Stanford friends — Rish Gupta (now chief executive), Tanuj Thapliyal, and Sud Bhatija — who came out of the engineering teams at Cisco Meraki and Samsara, two companies known for making once-complex infrastructure simple and cloud-managed. That lineage shows in the product. Spot AI sells its own cameras and an on-site appliance with, by its account, roughly three times the on-device computing power of a traditional artificial-intelligence camera, so that current vision models run at the edge. But it positions itself as an open intelligence layer: its system is designed to work with the cameras a business already owns, regardless of vendor, and turn any of them into what Spot AI calls a Video AI Agent.

The Video AI Agent is the differentiator, and it is worth defining plainly because the word "agent" is overused. A traditional analytic detects something and raises an alert for a human to handle. An agent, in Spot AI's sense, is given a goal and a set of allowed actions, and it both spots a situation and responds to it — alerting the right person, delivering an analytic, triggering lights or sounds, playing a voice message, or starting and stopping a machine if an incident or injury happens. Spot AI launched these agents in late 2024 and has since organized its offering around named agents such as an AI Security Guard and an AI Operations Assistant. The company reports more than a thousand customers across seventeen industries — manufacturing, retail, healthcare, education, construction, and car washes prominent among them — and says it indexes more new video each day than is uploaded to YouTube. It has raised about 93 million US dollars across four rounds, with a 2024 round that added Qualcomm Ventures alongside earlier investors.

The honest framing matters most here, because "an agent that acts on its own" is exactly the claim that needs accuracy-vs-performance discipline. Letting software take a physical action — sounding an alarm, stopping a production line — on the strength of a detection raises the cost of a false positive from "an operator glances at a clip" to "the line stopped for nothing," and the cost of a false negative from "a missed clip" to "the action that should have fired didn't." Spot AI's own customer figures are operational outcomes the vendor reports — a manufacturer cutting injuries, a school cutting incident-resolution time — and they are plausible and useful, but they are vendor-reported results, not independent benchmarks, and the underlying detection is still a precision-and-recall range. The right way to deploy an acting agent is with a human in the loop for consequential actions and a tuned operating point, a discipline that is not optional but a legal expectation under human-oversight rules we cover in [tuning analytics: false alarms and accuracy](https://www.forasoft.com/learn/video-surveillance/articles-vms/tuning-analytics-false-alarms-accuracy). The agent model is a real advance and a useful one; it also concentrates the consequences of being wrong, so it deserves the most careful piloting of anything in this profile.

## Ambient.ai: the threat-detection layer that replaces nothing

Ambient.ai is the purest expression of "analytics-first," because analytics is all it is. It does not want to be your VMS or sell you cameras; it wants to be the intelligence that sits on top of whatever you already run.

The company was founded in 2017 by Shikhar Shrestha (chief executive) and Vikesh Khanna (chief technology officer) and came out of stealth in early 2022 with a platform it calls computer-vision intelligence. The idea is to retrofit into a building's existing cameras and alarm sources, continuously read those feeds, and recognize not just objects but _situations_ — a person tailgating through a door, a weapon being drawn, someone loitering at a perimeter, a vehicle following another too closely. Ambient.ai describes these as "threat signatures": patterns of behavior and context that, when matched, raise a real-time alert so a security team can respond before an incident escalates rather than reviewing it afterward. Because it layers onto existing infrastructure, adopting Ambient.ai is an add-on decision, not a rip-and-replace, which is a meaningfully smaller commitment than swapping a VMS.

Two things make Ambient.ai distinctive. The first is a deliberate privacy stance: the company is publicly built around _not_ using facial recognition, positioning context-and-behavior analysis as a way to detect threats without identifying individuals by their biometrics. That is a deliberate design choice with real consequences, and it sidesteps the heaviest part of the legal gate we describe below — though it does not remove every privacy obligation, because detecting and recording identifiable people is still processing personal data. The second is where the technology is heading: Ambient.ai has begun describing its newer capability around a reasoning vision-language model — an artificial-intelligence model that can describe and reason about a scene in something closer to natural language — aimed at what the industry now calls agentic physical security. That is the same frontier Spot AI is pushing toward from the camera side, and it is the clearest signal of where this whole category is going.

The accuracy discipline applies in full. A system whose entire value is catching threats lives and dies on the balance between catching real ones (recall) and not crying wolf (precision). A threat-detection layer that floods a security team with false alarms gets ignored, and one tuned too conservatively misses the event it was bought to catch. Ambient.ai's pitch is precisely that its context modeling reduces false alarms relative to naive motion alerts — a real and valuable claim — but "fewer false alarms" is not "no false alarms," and the deployment still needs a tuned operating point and human verification on consequential alerts. We treat the rule-free, learn-what-is-normal style of detection it exemplifies in [anomaly detection in surveillance video](https://www.forasoft.com/learn/video-surveillance/articles-vms/anomaly-detection-in-surveillance-video).

## Openness and the standards boundary: the lock-in moved

Here is the counterintuitive thing about cloud, AI-native platforms, and the single most useful idea in this article. They are usually _more_ open at the camera than the incumbents — and _more_ locked-in at the layer that matters.

All three lean on the open camera standard to get video in. Eagle Eye is camera-agnostic over ONVIF; Spot AI advertises that it works with existing cameras regardless of vendor; Ambient.ai retrofits into whatever cameras you already have. Remember, ONVIF only guarantees a baseline — the common features a conformant camera and the platform both support, enough to pull a stream and basic events — and we keep "ONVIF-conformant" and "fully featured" as separate ideas throughout this section. But for the job these platforms need from a camera, the standard is enough, which is why none of them requires you to rip out your cameras. That is a real advantage over an appliance vendor whose best features assume its own hardware.

So where is the lock-in? It moved up the stack. With an AI-native cloud platform, the thing you depend on is not the camera and not even the recorder — it is the cloud service, the subscription, and the accumulated data and analytics living inside the vendor's platform. Your video history, your tuned agents, your threat signatures, your search index: these are in the vendor's cloud, reachable through the vendor's API, on the vendor's commercial terms. Switching cameras is easy; switching platforms means migrating all of that. The open API softens this — it is markedly easier to get your data and events out of these platforms than out of a closed appliance — but the gravity is the cloud, not the hardware. A senior engineer should read this as: the integration surface is excellent and standards-based at ingest, and proprietary at the point of value. Price the exit, not just the entry.

![Two stacked panels. The upper one, Locked at the cloud, holds four items - proprietary analytics, the detection and the reasoning; tuned agents and signatures, the logic you configured; video and search history, months of indexed data; and subscription terms, the commercial relationship - with the note that switching platforms migrates all of this. A label between the panels reads The standards boundary. The lower panel, Open at the camera, holds three items - ONVIF ingest, any conformant camera; open REST API, events and video out; and existing cameras, no rip-and-replace - with the note that the camera layer stays portable.](https://cdn.prod.website-files.com/64e8910adc5a63966a68acea/6aad7c1a81b1374291233e1c_6aad7b50ffd730fc118871c5_07_5-ai-native-vms-ambient-spot-eagle-eye__04-standards-boundary.svg)_Figure 4. The lock-in moved up. AI-native platforms ingest video over the open ONVIF standard and expose open web APIs, so the camera layer is truly portable; the proprietary cloud, the analytics, the tuned agents, and the data history are where the switching cost lives. Open at the camera, locked at the cloud._

The privacy gate sits on the same boundary and deserves a plain statement. Cloud analytics that detect people, plates, or faces process personal data, and the moment a platform is configured for biometric face matching it crosses into special-category data under the European Union's General Data Protection Regulation (GDPR Art. 9) and, in Illinois, the consent-and-private-right-of-action regime of the Biometric Information Privacy Act (BIPA, 740 ILCS 14). Eagle Eye's plate reading is personal data governed by retention and access rules; Ambient.ai's no-facial-recognition stance is partly a way to stay clear of the heaviest gate; any platform's face-matching feature is a legal decision before it is a technical one. We treat the law itself in [GDPR for video surveillance](https://www.forasoft.com/learn/video-surveillance/articles-vms/gdpr-for-video-surveillance), the biometric gate in [face recognition in surveillance](https://www.forasoft.com/learn/video-surveillance/articles-vms/face-recognition-in-surveillance), and plates in [license-plate recognition](https://www.forasoft.com/learn/video-surveillance/articles-vms/license-plate-recognition-lpr-anpr). The point here is that an AI-native platform makes these capabilities a checkbox, so know where the gate is before you tick it.

## The cost shape: renting capability instead of owning it

AI-native platforms almost all share one commercial shape, and seeing it clearly is worth more than any feature list. They are an operating expense — a per-camera subscription — where the on-premises incumbents are a capital expense.

The on-premises model, which we walked through for [Avigilon Unity](https://www.forasoft.com/learn/video-surveillance/articles-vms/avigilon-motorola-solutions) and the others, is a one-time purchase: you buy the camera licences, you buy and rack the servers and storage, and you own it. The AI-native cloud model flips this. You pay a recurring fee per camera that bundles the recording, the storage, the analytics, and the updates, and you own no infrastructure. Walk the arithmetic out loud, because the shape is the point, not the exact figures. Take a 100-camera site and a representative cloud subscription:

```
annual_subscription = price_per_camera_per_month × cameras × 12
annual_subscription = $30 × 100 × 12
annual_subscription = $36,000 per year   (recording, storage, analytics, updates included)
```

Over five years that is roughly 180,000 US dollars, with no servers to buy and nothing to maintain — but it never stops, and it scales linearly with cameras and retention. The on-premises alternative front-loads a large capital cost and then runs cheaper year to year, which is why the honest comparison is never "which is cheaper this month" but "which shape fits how we budget and how long we keep the system," compared on the same multi-year footing. We build that whole-system comparison in [the surveillance cost model](https://www.forasoft.com/learn/video-surveillance/articles-vms/surveillance-cost-model).

![A line chart of cumulative cost per site over five years, vertical axis marked $0 to $200k. The solid AI-native subscription line rises in equal steps of $36,000 a year from $0 to $180,000 at year five. The dashed on-prem purchase line starts near $90,000 and climbs gently to about $130,000. A marked point shows the subscription overtaking the one-time purchase near year three. Notes below give the arithmetic: $30 per camera per month times 100 cameras times 12 equals $36,000 a year.](https://cdn.prod.website-files.com/64e8910adc5a63966a68acea/6aad7c1b81b1374291233e26_6aad7b51ea4980ddc60576f1_07_5-ai-native-vms-ambient-spot-eagle-eye__05-cost-shape.svg)_Figure 5. The two cost shapes. The on-premises purchase is a big up-front capital cost that then climbs gently; the AI-native subscription starts low and climbs steadily, typically overtaking the one-time purchase around year three. Neither is "cheaper" in the abstract — they fit different budgets and time horizons._

Two cloud-specific costs hide inside the subscription and surprise teams that do not plan for them. The first is **bandwidth**: a cloud platform has to get video off-site, and continuous upload of many cameras can exceed an ordinary business internet link, which is exactly why Eagle Eye's Bridge and Spot AI's appliance buffer locally and send up less — the upload wall we quantify in [cloud and hybrid storage for surveillance](https://www.forasoft.com/learn/video-surveillance/articles-vms/cloud-hybrid-storage-for-surveillance). The second is the **cost and latency of cloud analytics** at scale, where sending more video up for processing meters up quickly; we model that in [cloud video analytics cost](https://www.forasoft.com/learn/video-surveillance/articles-vms/cloud-video-analytics-cost) and the broader [edge-vs-cloud deployment decision](https://www.forasoft.com/learn/video-surveillance/articles-vms/edge-vs-cloud-video-analytics). None of this makes cloud wrong — it makes it a different cost shape to plan, not a cheaper one to assume.

### A common mistake to avoid

The costliest errors with AI-native platforms come from believing the label instead of testing the system. Four recur. First, **assuming "AI-native" means "more accurate"**: it means analytics-first by design, not perfect detection — every one of these platforms produces a precision-and-recall range that you must verify on your own scenes and lighting, never a guaranteed number. Second, **letting an agent act without a human in the loop on consequential actions**: an autonomous response amplifies both correct and incorrect detections, so a stopped line or an ignored alarm is the predictable cost of skipping the oversight step — which is also a legal expectation, not just good practice. Third, **forgetting the cloud is a dependency**: if the platform's value is in the cloud and the site's internet link or the service goes down, plan for what keeps recording locally and what degrades gracefully. Fourth, **treating biometric features as ordinary settings**: switching on face matching is a legal decision under GDPR Art. 9 and BIPA before it is a configuration, and "the platform supports it" is not the same as "you may deploy it here." None of these is a flaw in the products; each is a planning gap an honest evaluation closes before the pilot, not after.

## The three versus the incumbents, without spin

The most useful thing a profile can do is place these platforms side by side with the established VMSs from earlier in this block, on the dimensions a buyer actually weighs. All are serious products; the choice is about deployment model, openness, and where the intelligence and the lock-in live.

| Platform | Core idea | Deployment model | Open SDK / API? | Makes its own cameras | Best fit |
| --- | --- | --- | --- | --- | --- |
| **Eagle Eye Networks** (now part of Brivo) | Cloud VMS, analytics on existing cameras | Cloud-native; on-site Bridge or Camera Direct | Yes — open REST API; ONVIF ingest | No — camera-agnostic | Multi-site businesses wanting a cloud system of record with a vast camera estate |
| **Spot AI** | AI camera system; agents that act, not just alert | Cloud + own cameras + edge appliance; works with existing cameras | Yes — open platform / API; ONVIF | Yes — plus works with third-party | Operations-and-safety use beyond security: manufacturing, retail, schools |
| **Ambient.ai** | Threat-detection overlay; no facial recognition | Cloud analytics layer over your existing cameras and VMS | Yes — integrates with existing stack | No — overlay only | Enterprises keeping their VMS but wanting proactive, privacy-conscious threat detection |
| **Milestone / Genetec / Avigilon** | Established VMS; AI added to a recording core | On-prem · hybrid · cloud options | Yes — mature SDKs | Avigilon yes; others no | Large estates wanting a proven recorder, on-prem control, deep integrations |

_Table 1. AI-native platforms versus the incumbents, on the dimensions a buyer weighs. The fork is not "AI or no AI" — every row has AI now. It is what the platform replaces, where it runs, and whether the intelligence was the starting point or a later layer._

The plain reading: choose **Eagle Eye Networks** when you want a cloud VMS as your system of record across many sites, keep your existing cameras, and value an open API and usage-based pricing — and you are comfortable that the company is now inside Brivo's access-plus-video strategy. Choose **Spot AI** when the job reaches past security into operations and safety, and the idea of cameras that take actions, not just raise alerts, solves a real problem you can pilot carefully. Choose **Ambient.ai** when you want to keep the VMS you already run, add proactive threat detection on top, and value a vendor that deliberately avoids facial recognition. Choose an **incumbent** when a proven on-premises recorder, maximal third-party integration, or full local control outweighs the analytics-first, cloud-first pitch. Whether to adopt any platform, assemble on open components, or build is the subject of [custom vs off-the-shelf VMS](https://www.forasoft.com/learn/video-surveillance/articles-vms/custom-vs-off-the-shelf-vms), and how to weigh any comparison like the one above is in [reading a VMS comparison](https://www.forasoft.com/learn/video-surveillance/articles-vms/reading-a-vms-comparison-criteria).

## Where AI-native fits — and where it doesn't

An honest profile names both sides. The analytics-first, cloud-first platforms fit when **proactive intelligence and low operational friction are the job**: a multi-site retailer, a fast-growing operations team, or a security group that wants threats surfaced in real time without standing up and maintaining servers at every location. They fit when you want to keep your existing cameras, value an open API for integration, and prefer a predictable per-camera subscription over a large capital purchase. And they fit especially well when the use case reaches beyond security into operations and safety, where Spot AI's agents and the wider agentic direction have the most to offer.

They are the wrong tool when the constraints point the other way. A site with poor or expensive connectivity, strict data-residency rules that forbid sending video off-premises, or a hard requirement to keep recording through any internet outage will be better served by an on-premises or hybrid design — the trade-offs are in [on-prem, cloud, and hybrid VMS](https://www.forasoft.com/learn/video-surveillance/articles-vms/on-prem-cloud-hybrid-vms). An organization that needs maximal third-party device integration or deep on-prem control may find a mature incumbent fits better. And any buyer tempted by "AI-native" as a guarantee of accuracy should re-read the first section: it is a description of architecture, and the detection still has to be tuned and verified on your scenes. The leading example of analytics-first, cloud-first surveillance is, by the same token, the most network-dependent and the most subscription-bound — which is exactly the trade an honest evaluation weighs against the proven, on-prem alternatives profiled earlier in this block.

For the commercial overview of the market this profile sits inside, see Fora Soft's [video surveillance management systems](https://www.forasoft.com/blog/article/video-surveillance-management-systems) playbook and the rundown of [modern VMS software features](https://www.forasoft.com/blog/article/features-modern-vms-software).

[↓Free download: AI-Native VMS — Evaluation Field GuideA one-page field guide that puts the three platforms on the overlay-to-platform spectrum, marks where the standards boundary sits, and lists the questions to ask before one of them goes on a shortlist.](https://www.forasoft.com/learn/downloads/ai-native-vms-evaluation-field-guide)

## Where Fora Soft fits in

Fora Soft has built real-time video, streaming, and computer-vision software since 2005, across 625+ shipped projects, and a large share of our surveillance work lives exactly where an AI-native platform meets a customer's own systems — pulling video and analytics events out of a cloud VMS through its API into bespoke dashboards and business workflows, building the specific detection a packaged platform does not offer, or wiring an analytics overlay into an existing recorder. The discipline we bring is the one this section preaches: design for how the system behaves at full camera load and on a bad-network day first — realistic detection precision and recall under real lighting, latency you have measured, recording that degrades gracefully when the internet link drops — then the feature list. When a team sits between "subscribe to an AI-native platform" and "build the intelligence ourselves," we help weigh extending an open cloud platform through its API against assembling on components, with the honesty that a reliable cloud VMS and a tuned analytics pipeline are expensive to reinvent and the better vendors here solved a lot of it already.

[![Video Encoding — book cover](https://cdn.prod.website-files.com/64e8910adc5a63966a68acea/6aad7f3e14ad05066d5a6b79_71dKsBA%252BOML._SL1500_.jpeg)![AI for Video: real-time pipelines, agents, serving and compliance — book cover](https://cdn.prod.website-files.com/64e8910adc5a63966a68acea/6aad7f43ac7ca7f6fb2f7375_71LR%252BezUMOL._SL1500_.jpeg)![AI for Video: models, computer vision, speech and search — book cover](https://cdn.prod.website-files.com/64e8910adc5a63966a68acea/6aad7f3e14ad05066d5a6b70_71JIvjpzyML._SL1500_.jpeg)](https://www.amazon.com/dp/B0HF4R78DN)

The handbook

Fora Soft Video Engineering Handbook

We wrote a seven-volume series that takes the whole video stack apart across 9,000+ pages — encoding, delivery, audio and AI. Volume 1 covers the encoding that sets what a camera stream costs to send and store, and volumes 6 and 7 cover the vision models, the real-time serving cost and the compliance work sitting behind every detection claim in this profile. Work through them and you can design and build a platform like the ones profiled here, not only choose between them. Written by Nikolay Sapunov, CEO at Fora Soft.

[Browse the handbook on Amazon →](https://www.amazon.com/dp/B0HF4R78DN) 7 volumes · Kindle & paperback

Weighing an AI-native platform against building the intelligence yourself?

Tell us which cameras you already run, what you need detected, and where the video is allowed to live, and we will tell you what an open cloud platform gets you through its API, what has to be built, and what the exit costs. 250+ video products shipped since 2005.

[Book a 30-min call →](https://calendly.com/vadim-fora-soft/30min) [WhatsApp →](https://wa.me/971585396367) [Email us →](mailto:eager2develop@forasoft.com)

## See our case studies

[Case study\\
\\
Mindbox\\
\\
An AI video management system in 50+ deployments across transport, pharma and gated communities, with face matching at 99.5%+ and plate reading across 500,000+ vehicles a day at about 95% — analytics-first on cameras of every vintage, and the biometric gate in the same breath.](https://www.forasoft.com/projects/mindbox) [Case study\\
\\
VALT\\
\\
A recording and observation platform used by 770+ US organisations and 50,000+ users, which we have built and run as the sole development team for 10+ years — what it actually takes for a platform to be somebody’s system of record.](https://www.forasoft.com/projects/valt) [Case study\\
\\
Worldcast Live\\
\\
Streaming at 1.5 Gb/s with 0.4–0.5 s latency to 10,000 simultaneous viewers: the upload wall in numbers, and the reason an on-site Bridge or edge appliance buffers before anything reaches the cloud.](https://www.forasoft.com/projects/worldcast-live)

## What to read next

[Vendors\\
\\
Reading a VMS Comparison: The Criteria That Matter\\
\\
How to read the feature grid you get handed once these three are on the shortlist.](https://www.forasoft.com/learn/video-surveillance/articles-vms/reading-a-vms-comparison-criteria) [Deployment\\
\\
VMS Software: On-Prem, Cloud, or Hybrid?\\
\\
The trade-off this profile keeps pointing at, worked through on its own terms.](https://www.forasoft.com/learn/video-surveillance/articles-vms/on-prem-cloud-hybrid-vms) [Analytics\\
\\
Tuning Analytics: False Alarms, Accuracy and the Operator\\
\\
The precision-and-recall range every platform here still has to be tuned to.](https://www.forasoft.com/learn/video-surveillance/articles-vms/tuning-analytics-false-alarms-accuracy) [Cost\\
\\
Video Surveillance Software Cost: Build vs Run\\
\\
The whole-system comparison behind the two cost shapes in this article.](https://www.forasoft.com/learn/video-surveillance/articles-vms/surveillance-cost-model)

## References

01. ONVIF — "ONVIF Profiles" and "Member Profile: Eagle Eye Networks" (an ONVIF profile is a fixed set of features a conformant device and client must support; conformance to a profile is what ensures interoperability between ONVIF products; Eagle Eye Networks, as an ONVIF member, can capture video and AI analytics from virtually any ONVIF-conformant camera — the open camera-ingest baseline every cloud VMS in this profile relies on). Primary standard (tier 1). [https://www.onvif.org/profiles/](https://www.onvif.org/profiles/)
02. European Union — "General Data Protection Regulation (Regulation (EU) 2016/679)" (Art. 9 treats biometric data used to uniquely identify a person as special-category data; Art. 35 requires a Data Protection Impact Assessment for high-risk processing such as large-scale systematic monitoring — the legal frame any face-matching or plate-reading feature in a cloud analytics platform must answer to). Primary law (tier 1). [https://eur-lex.europa.eu/eli/reg/2016/679/oj](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
03. Illinois General Assembly — "Biometric Information Privacy Act (740 ILCS 14)" (requires informed written consent before capturing a face template or other biometric identifier, sets a retention-and-destruction duty, and provides a private right of action with statutory damages — the heaviest US biometric gate, the one Ambient.ai's no-facial-recognition stance is partly designed to stay clear of). Primary law (tier 1). [https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3004&ChapterID=57](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3004&ChapterID=57)
04. United States Congress — "John S. McCain National Defense Authorization Act for Fiscal Year 2019, Section 889 (Public Law 115-232)" (bars federal agencies, their contractors, and grant recipients from procuring video-surveillance equipment from named manufacturers on national-security grounds; a camera-procurement gate any cloud VMS deployment in a government or federally funded setting must clear, even when the VMS itself is camera-agnostic). Primary law (tier 1). [https://www.congress.gov/bill/115th-congress/house-bill/5515/text](https://www.congress.gov/bill/115th-congress/house-bill/5515/text)
05. Business Wire / Brivo — "Brivo and Eagle Eye Networks Merge to Form the Industry's Largest AI Cloud-native Physical Security Company" (29 December 2025: Eagle Eye Networks, founder Dean Drako's cloud VMS, merges with cloud access-control company Brivo; the combined company operates under the Brivo name with Drako as CEO and Steve Van Till as President; the Brivo Security Suite spans AI, access control, video intelligence, visitor management, and intrusion — the single most important current fact about Eagle Eye). First-party press (tier 3). [https://www.businesswire.com/news/home/20251229142420/en/Brivo-and-Eagle-Eye-Networks-Merge-to-Form-the-Industrys-Largest-AI-Cloud-native-Physical-Security-Company](https://www.businesswire.com/news/home/20251229142420/en/Brivo-and-Eagle-Eye-Networks-Merge-to-Form-the-Industrys-Largest-AI-Cloud-native-Physical-Security-Company)
06. Eagle Eye Networks — "Eagle Eye Cloud VMS" product and API documentation (a cloud-native VMS with cloud and on-premises recording, the on-site Bridge appliance and direct-to-cloud Camera Direct, support for several thousand camera models, usage-based per-camera subscription pricing, an open RESTful Video API, and analytics — Smart Video Search, LPR, gun detection, person/vehicle detection, occupancy, perimeter intrusion — that run on existing cameras). First-party engineering (tier 3). [https://www.een.com/](https://www.een.com/)
07. Eagle Eye Networks — "Barracuda Networks Founder & Former CEO Dean Drako Launches Eagle Eye Networks" and company history (Eagle Eye founded 2012 by Dean Drako, who built Barracuda Networks from 2003 to 2012 to over US$200M in annual sales and 150,000 customers with the industry's first spam-filter appliance; the Eagle Eye Cloud Security Camera VMS was announced in early 2014 — the cloud, IT-security lineage of the platform). First-party / encyclopedic (tier 4). [https://en.wikipedia.org/wiki/Eagle\_Eye\_Networks](https://en.wikipedia.org/wiki/Eagle_Eye_Networks)
08. Spot AI — "Spot AI Introduces First Video AI Agents for the Physical World as it Nears $100 Million in Funding to Date" (29 October 2024: Spot AI, founded 2018 by Rish Gupta, Tanuj Thapliyal, and Sud Bhatija out of Cisco Meraki and Samsara engineering teams, launches Video AI Agents that act on detections — alerting, triggering lights/sounds, starting/stopping machines; an edge appliance with ~3× the compute of a traditional AI camera; an open system that works with existing cameras; ~$93M raised across four rounds; 1,000+ customers across 17 industries). First-party press (tier 3). [https://www.spot.ai/blog/spot-ai-introduces-first-video-ai-agents-for-the-physical-world-as-it-nears-100-million-in-funding-to-date](https://www.spot.ai/blog/spot-ai-introduces-first-video-ai-agents-for-the-physical-world-as-it-nears-100-million-in-funding-to-date)
09. TechCrunch — "Ambient.ai aims to provide AI-powered building security, minus bias and privacy pitfalls" (19 January 2022: Ambient.ai, founded 2017 by Shikhar Shrestha and Vikesh Khanna, emerges from stealth with a 'computer vision intelligence' platform that retrofits into existing cameras and uses 'threat signatures' to detect threats contextually, deliberately without facial recognition to avoid bias and privacy pitfalls — the no-FR design stance and the overlay model). Institutional reporting (tier 5). [https://techcrunch.com/2022/01/19/ambient-ai-security-without-facial-recognition/](https://techcrunch.com/2022/01/19/ambient-ai-security-without-facial-recognition/)
10. Ambient.ai — "Ambient.ai Raises $20M Strategic Growth Investment from Allegion Ventures" and "Pulsar" announcement (a 2025 strategic investment from Allegion Ventures, described as that fund's largest single check, and a newer reasoning vision-language model aimed at agentic physical security — the funding and the VLM/agentic direction the whole category is moving toward). First-party press (tier 3). [https://www.ambient.ai/press/ambient-ai-strategic-growth-investment-allegion-ventures](https://www.ambient.ai/press/ambient-ai-strategic-growth-investment-allegion-ventures)
11. IEC — "IEC 62676 series: Video surveillance systems for use in security applications" (specifies minimum requirements across the system lifecycle; EN IEC 62676-4:2025 covers application guidelines including information security and data privacy — the system-level floor any VMS, cloud or on-prem, should meet). Primary standard (tier 1). [https://webstore.iec.ch/en/publication/34391](https://webstore.iec.ch/en/publication/34391)
12. Rhombus / Coram / Gartner Peer Insights — "Best cloud-based VMS platforms 2026" and the VSaaS market context (independent market orientation: the shift from on-premises recorders to cloud-native, AI-powered platforms; the VSaaS market sized in the multiple billions for 2026; the generational framing of AI-native versus AI-assisted VMS — used for orientation and the category map, not as the source for any standards or legal claim). Institutional / analyst (tier 5). [https://www.gartner.com/reviews/market/video-surveillance-management-systems](https://www.gartner.com/reviews/market/video-surveillance-management-systems)

Key takeaways

- AI-native means built analytics-first and cloud-first, not a recorder with AI added later.
- The three differ by what they replace: Eagle Eye a VMS, Spot AI cameras, Ambient.ai nothing.
- All ingest over ONVIF, so the lock-in is the cloud and data, not the camera.
- Eagle Eye Networks merged with Brivo in December 2025; it now sits in an access-plus-video suite.
- Spot AI's agents act, not just alert — powerful, but needs human oversight on consequential actions.
- "AI-native" describes architecture, not accuracy: every analytic is still a precision/recall range.

## Related glossary terms

[**ONVIF** \\
The open standard that lets cameras and VMS software from different vendors interoperate; defines profiles for streaming, recording, and analytics.](https://www.forasoft.com/learn/video-surveillance/glossary/terms-vms/onvif)

[**Precision** \\
Of all alerts the system raised, the share that were real events; high precision means few false alarms. Always read together with recall.](https://www.forasoft.com/learn/video-surveillance/glossary/terms-vms/precision)

[**Recall** \\
Of all real events that happened, the share the system caught; high recall means few misses. Trades off against precision via the confidence threshold.](https://www.forasoft.com/learn/video-surveillance/glossary/terms-vms/recall)

[**Cloud analytics** \\
Running video analytics in the cloud; offers elastic compute and heavy models but costs bandwidth to send video up and raises privacy exposure.](https://www.forasoft.com/learn/video-surveillance/glossary/terms-vms/cloud-analytics)

[**GDPR** \\
The EU data-protection law; treats surveillance video as personal data and faces as special-category biometric data with stricter rules.](https://www.forasoft.com/learn/video-surveillance/glossary/terms-vms/gdpr)

[**Hybrid VMS** \\
A deployment that records on-site but manages, views, and stores selected footage in the cloud; the middle path between on-prem VMS and pure VSaaS.](https://www.forasoft.com/learn/video-surveillance/glossary/terms-vms/hybrid-vms)

[**Latency** \\
The delay between an event in front of the camera and the alert or video reaching the operator; edge keeps it in milliseconds, cloud adds seconds.](https://www.forasoft.com/learn/video-surveillance/glossary/terms-vms/latency)

[**Consent** \\
A person's documented agreement to data capture; required before biometric capture in many jurisdictions, where a sign alone is not enough.](https://www.forasoft.com/learn/video-surveillance/glossary/terms-vms/consent)

![Eagle Eye Networks, Spot AI & Ambient.ai: AI-Native VMS](https://cdn.prod.website-files.com/64e8910adc5a63966a68acea/6a0c72a04c29b22a8ddb991b_6a0c728d356dff40621f0967_nikolay_sapunov.avif)

Nikolay Sapunov

CEO at Fora Soft

Nikolay Sapunov is the CEO of Fora Soft, a software studio specialising in video-centric products — streaming platforms, WebRTC apps, video conferencing, and AI-driven video tools. He writes the Video Encoding knowledge base to give product and engineering teams a clear, no-jargon way to reason about codecs, compression, HDR, and the trade-offs behind every video architecture decision.

[View profile →](https://www.forasoft.com/team/nikolay-sapunov)

[← Previous article\\
\\
Avigilon and Motorola Solutions: An Honest VMS Profile](https://www.forasoft.com/learn/video-surveillance/articles-vms/avigilon-motorola-solutions)

[Next article →\\
\\
Custom vs Off-the-Shelf VMS: Build, Buy, or Customize](https://www.forasoft.com/learn/video-surveillance/articles-vms/custom-vs-off-the-shelf-vms)

[![Close](https://cdn.prod.website-files.com/64e8910adc5a63966a68acc1/6a9b19cf3b4cc2231bb2f4b5_hv3-ic-close.svg)](https://www.forasoft.com/learn/video-surveillance/articles-vms/ai-native-vms-ambient-spot-eagle-eye#)

Start the conversation

## Describe your project and we will get in touch

Within 24 hours you get a realistic estimate, technical recommendations and next steps. Free, no obligations.

01

A senior architect reads itReply the same business day, Mon–Fri.

02

30-min call to scope itWe ask the questions that change the budget.

03

Estimate in 24 hoursBudget, timeline, architecture notes. Yours to keep.

[![Minimalist white computer monitor icon with a solid blue dot in the upper left corner on a black background.](https://cdn.prod.website-files.com/64e8910adc5a63966a68acc1/6a9abbe93824b51a2a2ac6e8_fs-cal-mark-light.avif)Book a callPick a slot](https://book.forasoft.com/) [![White WhatsApp logo showing a phone handset inside a speech bubble on a transparent background.](https://cdn.prod.website-files.com/64e8910adc5a63966a68acc1/6a9abf67927016e6008f6306_fs-whatsapp-white.avif)WhatsAppText us](https://wa.me/971585396367) [@Email useager2develop@forasoft.com](mailto:eager2develop@forasoft.com)

Or write here

reCAPTCHA

Recaptcha requires verification.

I'm not a robot

reCAPTCHA

By sending this form you agree with the [Personal Data Processing Policy.](https://www.forasoft.com/legal)

Got it — your message is in. A real engineer will reply within 24 hours with a realistic estimate and next steps. Check your inbox (and spam, just in case).

Hmm — that didn’t go through. Please try again. If the issue keeps happening, email us at eager2develop@forasoft.com and a real engineer will pick it up.

✕

reCAPTCHA