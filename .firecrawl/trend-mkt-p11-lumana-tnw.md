[Skip to content](https://thenextweb.com/news/video-first-frontier-ai-physical-world-lumana#main)

![Photo of AI Learning and Artificial Intelligence Concept. Business, modern technology, internet and networking concept.](https://media.thenextweb.com/2026/09/video-first-frontier-ai-physical-world-lumana2.avif)

**AI Learning and Artificial Intelligence Concept.**

![Image Credits](https://static.thenextweb.com/assets/icons/camera.svg)_Credit: Canva_

#### TL;DR

_Hundreds of millions of cameras are already deployed, but most footage still requires a human to know what to look for. Lumana, founded by ex-Intel computer vision leaders, processes over a billion images daily across 50,000+ cameras using its VIA-1 model, which learns what is normal for each individual camera and flags deviations. The company filters locally before sending anything to the cloud, following a principle of “filter before you spend.” Video may be physical AI’s natural starting point because the infrastructure already exists._

A camera overlooking a loading dock might record twelve hours of trucks arriving, workers moving through the site, and boxes leaving the building. Most days, nobody has a reason to watch any of it. The footage only becomes useful when a package goes missing, an accident happens or somebody needs to work backwards from an event and find out what happened.

That has been one of the strange limitations of video surveillance for years. Cameras became digital long ago, but the footage they produce still depends heavily on a person knowing what to look for and where to find it. AI is beginning to make more of that footage understandable and searchable while events are still unfolding.

Axis Communications [estimates](https://www.axis.com/dam/public/permalink/256299/axis-perspectives-2026-en-US_256299.pdf) that 562 million surveillance cameras were installed worldwide outside China by the end of 2025. More of those cameras are also arriving with intelligence built in. About two-thirds of cameras shipped in 2024 included [deep-learning](https://thenextweb.com/news/recruiters-specialised-ai-jobs-pivot) analytics, according to the company’s research.

For companies building what is increasingly called [physical AI](https://thenextweb.com/news/a16z-machine-age-fund-1-1bn-hardware), much of the infrastructure is therefore already hanging from walls and ceilings. The opportunity is in making those existing cameras more useful by teaching [software](https://thenextweb.com/news/cursor-anysphere-2-billion-funding-50-billion-valuation-ai-coding) to understand what is happening in front of them.

Lumana is one of the companies betting on that transition. Its founders came to the problem with years of experience in [computer vision](https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era) at Intel. CEO Sagi Ben Moshe previously led Intel’s RealSense business, while CTO Ofir Mulla worked on the architecture behind its 3D and LiDAR cameras.

The California-based startup [raised $40 million](https://www.axios.com/pro/enterprise-software-deals/2025/07/29/video-security-lumana-40m-series-a) in July 2025 in a Series A led by Wing Venture Capital, with participation from Norwest Venture Partners and S Capital, taking its total funding to $64 million. By December, it reported that more than 50,000 cameras connected to its platform, with customers including [Fortune 500](https://thenextweb.com/news/sap-autonomous-enterprise-ai-agents-sapphire) businesses across the United States.

The company says its AI video surveillance systems now process more than a billion images a day across more than 50,000 cameras. For customers, however, the early changes are usually much more ordinary than that number suggests.

## First, stop staring at the screens

For decades, a familiar sight in [security control](https://thenextweb.com/news/ai-generated-code-security-flaw-sygnia-claude-onboarding) rooms has been a wall of video feeds and people expected to notice when something looks wrong.

![Photo of Ofir Mulla, CTO of Lumana](https://media.thenextweb.com/2026/09/video-first-frontier-ai-physical-world-lumana.avif)Ofir Mulla, CTO of Lumana — Credit: Lumana

Lumana CTO Ofir Mulla says teams spend the first month after deploying its technology mostly sorting out much more ordinary problems. Teams find cameras that are offline, work out where coverage is inconsistent, and decide who should receive which alerts.

As that work settles, operators can spend less time trying to follow every feed and more time looking at the events the system has flagged for investigation.

“ _Instead of spending time watching passive video walls and trying to spot something unusual, operators can focus their attention on events that warrant investigation,_” Mulla said in an interview.

Doing that well depends heavily on context, something traditional motion detection and fixed rules have struggled to capture.

A person standing beside a warehouse door might be perfectly normal at 2pm and worth investigating at 2am. A delivery truck parked at a loading dock for 20 minutes could be expected. The same truck sitting there for three hours may not be.

Lumana’s [VIA-1 model](https://www.lumana.ai/products/via-1) is designed to learn from the environment seen by each camera rather than apply exactly the same definition of normal everywhere. The company says this can reduce false alerts by up to 90% compared with legacy motion detection and rule-based systems, although Mulla is careful to describe that figure as the higher end of what Lumana has observed rather than a result every customer should expect.

But the much harder test comes when the environment itself changes.

## What happens when normal changes?

What looks normal to a camera can change quickly. A warehouse might rearrange its layout over a weekend, while a retailer suddenly has to deal with the Christmas rush or a factory introduces a night shift that brings dozens of people into an area that used to be empty at that hour. In each case, activity that might have raised an alert yesterday could be perfectly routine today.

Mulla says VIA-1 can adjust its understanding of an individual camera as its environment changes, with feedback from operators helping when something has materially shifted. He would not give a fixed time for how long that adjustment takes, saying it depends on the scale and type of change.

A useful AI video system has to learn that a new shift pattern is now routine while still noticing the activity that should raise questions. Because the time needed to adjust depends on what has changed, operator feedback remains part of that process, particularly when a site has undergone a substantial change. In practice, the system is learning alongside an environment that does not stay still for long.

Making all of this footage easier to search and understand also raises [privacy](https://thenextweb.com/news/why-2026-will-be-the-year-of-governed-cybersecurity-ai) questions, particularly in workplaces and other spaces where people are routinely recorded. Lumana allows customers to set retention and access policies and disable features such as face and gender recognition depending on local requirements. But as existing cameras become more capable, companies also have to consider what they should collect, who should be able to search it, and how long that information should be kept.

Today, much of the work is still about helping people decide where to look. Lumana sees a larger role for the same technology as these systems become more capable.

Mulla describes “ _physical AI agents_” that can divide up monitoring, verification, and response. Lumana’s platform already supports actions ranging from sending notifications and triggering webhooks to activating connected systems when particular events are detected.

That puts the camera in a different place inside the business. Footage can become an input to software that interprets an event and, in some cases, triggers what happens next.

## Filter before you spend

Doing this across tens of thousands of cameras gets expensive quickly because video is costly to move and process at scale. Sending every frame to the cloud for more intensive AI processing would rapidly become expensive, particularly as camera resolution and deployment sizes grow.

Lumana handles much of the continuous processing locally instead. Its Core hardware sits close to the cameras and performs the initial processing there. According to the company’s [platform overview](https://www.lumana.ai/products/platform-overview), most video processing runs locally, while the cloud provides additional processing, remote access, and management across sites.

“ _The vast majority of video is routine and never needs to leave the site,_” Mulla said.

Only footage that warrants deeper analysis needs more expensive processing. The company’s principle is more simply: “ _We filter before we spend._”

The same economics are likely to matter well beyond Lumana. Cameras and other sensors generate too much information for every frame to receive the same amount of computation, which makes deciding what deserves deeper analysis part of the technical and economic problem.

Video also has one advantage over some of the more ambitious ideas around physical AI. Companies do not have to wait for millions of new robots or rebuild their sites around new hardware. Hundreds of millions of cameras are already pointed at factories, shops, universities, warehouses, and streets.

Most of those cameras were installed to record what happened. If AI can reliably understand more of that footage as events unfold, the same infrastructure can help companies understand what is happening while it is still happening and, in some cases, decide what should happen next. And that might just be what makes video such a natural starting point for AI’s move into the physical world.

## Get the TNW newsletter

Get the most important tech news in your inbox each week.

Contributed article. Not produced by the TNW newsroom and does not reflect the editorial stance of TNW.

[![Share on Facebook](https://static.thenextweb.com/assets/icons/facebook-white.svg)](https://www.facebook.com/sharer/sharer.php?s=100&p[url]=https%3A%2F%2Fthenextweb.com%2Fnews%2Fvideo-first-frontier-ai-physical-world-lumana%3Futm_source%3Dfacebook%26utm_medium%3Dshare%26utm_campaign%3Darticle-share-button&p[title]=Why%20video%20is%20the%20first%20frontier%20as%20AI%20learns%20to%20read%20the%20physical%20world&p[images][0]=https%3A%2F%2Fmedia.thenextweb.com%2F2026%2F09%2Fvideo-first-frontier-ai-physical-world-lumana2.avif&u=https%3A%2F%2Fthenextweb.com%2Fnews%2Fvideo-first-frontier-ai-physical-world-lumana&t=Why%20video%20is%20the%20first%20frontier%20as%20AI%20learns%20to%20read%20the%20physical%20world)[![Share on X](https://static.thenextweb.com/assets/icons/twitter-white.svg)](https://x.com/intent/post?url=https%3A%2F%2Fthenextweb.com%2Fnews%2Fvideo-first-frontier-ai-physical-world-lumana%3Futm_source%3Dx%26utm_medium%3Dshare%26utm_campaign%3Darticle-share-button%26referral&via=thenextweb&related=thenextweb&text=Why%20video%20is%20the%20first%20frontier%20as%20AI%20learns%20to%20read%20the%20physical%20world)[![Share on Flipboard](https://static.thenextweb.com/assets/icons/flipboard-white.svg)](https://share.flipboard.com/bookmarklet/popout?url=https%3A%2F%2Fthenextweb.com%2Fnews%2Fvideo-first-frontier-ai-physical-world-lumana%3Futm_source%3Dflipboard%26utm_medium%3Dshare%26utm_campaign%3Darticle-share-button)[![Share on LinkedIn](https://static.thenextweb.com/assets/icons/linkedin-white.svg)](https://www.linkedin.com/shareArticle/?mini=true&url=https%3A%2F%2Fthenextweb.com%2Fnews%2Fvideo-first-frontier-ai-physical-world-lumana%3Futm_source%3Dlinkedin%26utm_medium%3Dshare%26utm_campaign%3Darticle-share-button)[![Share on Telegram](https://static.thenextweb.com/assets/icons/telegram.svg)](https://t.me/share/url?url=https%3A%2F%2Fthenextweb.com%2Fnews%2Fvideo-first-frontier-ai-physical-world-lumana%3Futm_source%3Dtelegram%26utm_medium%3Dshare%26utm_campaign%3Darticle-share-button)[![Share on Email](https://static.thenextweb.com/assets/icons/mail-white.svg)](mailto:?subject=Why%20video%20is%20the%20first%20frontier%20as%20AI%20learns%20to%20read%20the%20physical%20world&body=https%3A%2F%2Fthenextweb.com%2Fnews%2Fvideo-first-frontier-ai-physical-world-lumana%3Futm_source%3Demail%26utm_medium%3Dshare%26utm_campaign%3Darticle-share-button)