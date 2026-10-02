|     |     |     |
| --- | --- | --- |
| |     |     |     |
| --- | --- | --- |
| [![](https://news.ycombinator.com/y18.svg)](https://news.ycombinator.com/) | **[Hacker News](https://news.ycombinator.com/news)** [new](https://news.ycombinator.com/newest) \| [past](https://news.ycombinator.com/front) \| [comments](https://news.ycombinator.com/newcomments) \| [ask](https://news.ycombinator.com/ask) \| [show](https://news.ycombinator.com/show) \| [jobs](https://news.ycombinator.com/jobs) \| [submit](https://news.ycombinator.com/submit) | [login](https://news.ycombinator.com/login?goto=item%3Fid%3D47503617) | |

| |     |     |     |
| --- | --- | --- |
|  |  | [Show HN: Gemini can now natively embed video, so I built sub-second video search](https://github.com/ssrajadh/sentrysearch) ( [github.com/ssrajadh](https://news.ycombinator.com/from?site=github.com/ssrajadh)) |
|  | 438 points by [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47503617) \| [hide](https://news.ycombinator.com/hide?id=47503617&goto=item%3Fid%3D47503617) \| [past](https://hn.algolia.com/?query=Show%20HN%3A%20Gemini%20can%20now%20natively%20embed%20video%2C%20so%20I%20built%20sub-second%20video%20search&type=story&dateRange=all&sort=byDate&storyText=false&prefix&page=0) \| [favorite](https://news.ycombinator.com/fave?id=47503617&auth=084ea4f0301431e5febc5109c7eec2cca44dc9f7) \| [108 comments](https://news.ycombinator.com/item?id=47503617) |
|  | Gemini Embedding 2 can project raw video directly into a 768-dimensional vector space alongside text. No transcription, no frame captioning, no intermediate text. A query like "green car cutting me off" is directly comparable to a 30-second video clip at the vector level.<br>I used this to build a CLI that indexes hours of footage into ChromaDB, then searches it with natural language and auto-trims the matching clip. Demo video on the GitHub README.<br>Indexing costs ~$2.50/hr of footage. Still-frame detection skips idle chunks, so security camera / sentry mode footage is much cheaper. |

|     |     |     |
| --- | --- | --- |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [macNchz](https://news.ycombinator.com/user?id=macNchz) [6 months ago](https://news.ycombinator.com/item?id=47506611) \| [next](https://news.ycombinator.com/item?id=47503617#47508125)\[–\]<br>This is a really cool implementation—embeddings still often feel like magic to me. That said, this exact use case is sort of also my biggest point of concern with where AI takes us, much more so than most of the common AI risks you hear lots of chatter about. We live in a world absolutely loaded with cameras now but ultimately retain some semblance of semi-anonymity/privacy in public by virtue of the fact that nobody can actually watch or review all of the video from those cameras except when there is a compelling reason to do so, but these technologies are making that a much more realistic proposition.<br>The presence of cameras everywhere is considerably more concerning than the status quo, to me at least, when there is an AI watching and indexing every second of every feed—where camera owners or manufacturers or governments could set simple natural language parameters for highly specific people or activities notify about. There are obviously compelling and easy-to-sell cases here that will surely drive adoption as it becomes cost effective: get an alert to crime in progress, get an alert when a neighbor who doesn't clean up after his dog, get an alert when someone has fallen...but the potential implications of living in a panopticon like this if not well regulated are pretty ugly. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [citruscomputing](https://news.ycombinator.com/user?id=citruscomputing) [6 months ago](https://news.ycombinator.com/item?id=47507598) \| [parent](https://news.ycombinator.com/item?id=47503617#47506611) \| [next](https://news.ycombinator.com/item?id=47503617#47507132)\[–\]<br>It's being built as we speak. I attended at a city council meeting yesterday, discussing approving a contract for ALPR cameras. I learned about a product from the camera vendor called Fusus\[0\], a dashboard that integrates various camera systems, ALPRs, alerts, etc. Two things stood out to me: natural-language querying of video feeds, and future planned integration with civilian-deployed cameras. The city only had budget for 50 ALPRs, and they stressed how they're only deploying them on main streets, but it seems like only a matter of time before your neighbor is able to install a camera that feeds right into the local PD's AI-enabled systems. One council member raised concerns about integrations with the citizen app\[1\] specifically (and a few others I didn't catch the names of). I'm very worried about where all this is heading.<br>\[0\]: [https://www.axon.com/products/axon-fusus](https://www.axon.com/products/axon-fusus)<br>\[1\]: [https://citizen.com/](https://citizen.com/) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [robertlagrant](https://news.ycombinator.com/user?id=robertlagrant) [6 months ago](https://news.ycombinator.com/item?id=47517147) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47507598) \| [next](https://news.ycombinator.com/item?id=47503617#47507132)\[–\]<br>I live in Oxford, UK and walked past a police van that said "automatic facial recognition in use". Not exactly a good sign without any caveats. I imagine they recorded me staring at their van. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47507132) \| [parent](https://news.ycombinator.com/item?id=47503617#47506611) \| [prev](https://news.ycombinator.com/item?id=47503617#47507598) \| [next](https://news.ycombinator.com/item?id=47503617#47507807)\[–\]<br>Totally valid concern. Right now the cost ($2.50/hr) and latency make continuous real-time indexing impractical, but that won't always be the case. This is one of the reasons I'd want to see open-weight local models for this, keeps the indexing on your own hardware with no footage leaving your machine. But you're right that the broader trajectory here is worth thinking carefully about. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [mpalmer](https://news.ycombinator.com/user?id=mpalmer) [6 months ago](https://news.ycombinator.com/item?id=47507588) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47507132) \| [next](https://news.ycombinator.com/item?id=47503617#47510419)\[–\]<br>It's 2.50 an hour because Google has margins. A nation state could do it at cost, and even if it's not a huge difference, the price of a year's worth of embeddings is just $21,900. That's a rounding error, especially considering it's a one time cost for footage. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [wholinator2](https://news.ycombinator.com/user?id=wholinator2) [6 months ago](https://news.ycombinator.com/item?id=47507635) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47507588) \| [next](https://news.ycombinator.com/item?id=47503617#47510419)\[–\]<br>Right? $2.50 an hour is trivial to a Government that can vote to invent a trillion dollars. Even just 1 million dollars is the cost of monitoring 45 real time feeds for a year. I'm sure just many very rich people would pay that for the safety of their compound. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [jimmySixDOF](https://news.ycombinator.com/user?id=jimmySixDOF) [6 months ago](https://news.ycombinator.com/item?id=47510419) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47507132) \| [prev](https://news.ycombinator.com/item?id=47503617#47507588) \| [next](https://news.ycombinator.com/item?id=47503617#47507807)\[–\]<br>How are you getting to $2.50/hr ? The price sheet says its 0.00079 per frame.<br>[https://ai.google.dev/gemini-api/docs/pricing#gemini-embeddi...](https://ai.google.dev/gemini-api/docs/pricing#gemini-embedding-2) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [jjwiseman](https://news.ycombinator.com/user?id=jjwiseman) [6 months ago](https://news.ycombinator.com/item?id=47511227) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47510419) \| [next](https://news.ycombinator.com/item?id=47503617#47507807)\[–\]<br>From what I see the code downsamples video to 5 fps, so 1 hour of video is 3600 seconds \* 5 fps = 18,000 frames. 18,000 frames \* $0.00079/frame = $14.22. A couple dollars more with the overlap.<br>(The code also tries to skip "still" frames, but if your video is dynamic you're looking at the cost above.) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47512061) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47511227) \| [next](https://news.ycombinator.com/item?id=47503617#47507807)\[–\]<br>you're right that the code uses ffmpeg to downsample the chunks to 5fps before sending them, but that's only a local/bandwidth optimization, not what the api actually processes.<br>regardless of the file's frame rate, the gemini api natively extracts and tokenizes exactly 1 fps. the 5 fps downscaling just keeps the payload sizes small so the api requests are fast and don't timeout.<br>i'll update the readme to make this more clear. thanks for bringing this up. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [jjwiseman](https://news.ycombinator.com/user?id=jjwiseman) [6 months ago](https://news.ycombinator.com/item?id=47513290) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47512061) \| [next](https://news.ycombinator.com/item?id=47503617#47507807)\[–\]<br>Thanks for the details and correction. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [Ajedi32](https://news.ycombinator.com/user?id=Ajedi32) [6 months ago](https://news.ycombinator.com/item?id=47507807) \| [parent](https://news.ycombinator.com/item?id=47503617#47506611) \| [prev](https://news.ycombinator.com/item?id=47503617#47507132) \| [next](https://news.ycombinator.com/item?id=47503617#47507715)\[–\]<br>Most cameras are also not queryable by any one person or organization. They are owned by different companies and if the government wants access they have to subpoena them after the fact.<br>The problems start cropping up when you get things like Flock where governments start deploying cameras on a massive scale, or Ring where a single company has unrestricted access to everyone's private cameras. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [Spivak](https://news.ycombinator.com/user?id=Spivak) [6 months ago](https://news.ycombinator.com/item?id=47508182) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47507807) \| [next](https://news.ycombinator.com/item?id=47503617#47507715)\[–\]<br>I think Flock is just a symptom of the underlying tech becoming so cheap that "just blanket the city in cameras" starts to sound like a viable solution when police rely so heavily on camera footage.<br>I don't think it's a good thing but it seems the limiting factor has been technological feasibility instead of any kind of principle against it. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [cake\_robot](https://news.ycombinator.com/user?id=cake_robot) [6 months ago](https://news.ycombinator.com/item?id=47507715) \| [parent](https://news.ycombinator.com/item?id=47503617#47506611) \| [prev](https://news.ycombinator.com/item?id=47503617#47507807) \| [next](https://news.ycombinator.com/item?id=47503617#47511318)\[–\]<br>Yeah, the panopticon is now technically very feasible it's just expensive to implement (for now). | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [whattheheckheck](https://news.ycombinator.com/user?id=whattheheckheck) [6 months ago](https://news.ycombinator.com/item?id=47511238) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47507715) \| [next](https://news.ycombinator.com/item?id=47503617#47511318)\[–\]<br>Its very cheap to target an individual though so they dont need to look everywhere | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [FuckButtons](https://news.ycombinator.com/user?id=FuckButtons) [6 months ago](https://news.ycombinator.com/item?id=47511318) \| [parent](https://news.ycombinator.com/item?id=47503617#47506611) \| [prev](https://news.ycombinator.com/item?id=47503617#47507715) \| [next](https://news.ycombinator.com/item?id=47503617#47508933)\[–\]<br>Once the hardware to run inference for something like the vision understanding module of this can be run on a low / medium power asic drones are going to be absolutely horrifying weapons. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [mbokinala](https://news.ycombinator.com/user?id=mbokinala) [6 months ago](https://news.ycombinator.com/item?id=47515123) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47511318) \| [next](https://news.ycombinator.com/item?id=47503617#47508933)\[–\]<br>[https://www.youtube.com/watch?v=O-2tpwW0kmU](https://www.youtube.com/watch?v=O-2tpwW0kmU) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [greggsy](https://news.ycombinator.com/user?id=greggsy) [6 months ago](https://news.ycombinator.com/item?id=47508933) \| [parent](https://news.ycombinator.com/item?id=47503617#47506611) \| [prev](https://news.ycombinator.com/item?id=47503617#47511318) \| [next](https://news.ycombinator.com/item?id=47503617#47511687)\[–\]<br>All the major cloud providers offer some form of face detection and numberplate reading, with many supporting object detection (ie package, vehicle, person) out of the camera itself. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [macNchz](https://news.ycombinator.com/user?id=macNchz) [6 months ago](https://news.ycombinator.com/item?id=47510388) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47508933) \| [next](https://news.ycombinator.com/item?id=47503617#47511687)\[–\]<br>It's definitely creeping into things, though most of the features I've seen are fairly simplistic compared to what would be possible if the video was being reviewed + indexed by current SoTA multimodal LLMs. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [zahlman](https://news.ycombinator.com/user?id=zahlman) [6 months ago](https://news.ycombinator.com/item?id=47511687) \| [parent](https://news.ycombinator.com/item?id=47503617#47506611) \| [prev](https://news.ycombinator.com/item?id=47503617#47508933) \| [next](https://news.ycombinator.com/item?id=47503617#47508005)\[–\]<br>\> this exact use case is sort of also my biggest point of concern with where AI takes us, much more so than most of the common AI risks you hear lots of chatter about.<br>I've been hearing warnings that AI would be used for this since well before it seemed feasible. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [macNchz](https://news.ycombinator.com/user?id=macNchz) [6 months ago](https://news.ycombinator.com/item?id=47512423) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47511687) \| [next](https://news.ycombinator.com/item?id=47503617#47508005)\[–\]<br>Not claiming to have hit on something unique here, but I think it’s realistic and often drowned out in favor of sci-fi nonsense. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [janalsncm](https://news.ycombinator.com/user?id=janalsncm) [6 months ago](https://news.ycombinator.com/item?id=47508005) \| [parent](https://news.ycombinator.com/item?id=47503617#47506611) \| [prev](https://news.ycombinator.com/item?id=47503617#47511687) \| [next](https://news.ycombinator.com/item?id=47503617#47508125)\[–\]<br>For specific people they probably wouldn’t use general embeddings. These embeddings can let you search for “tall man in a trenchcoat” but if you want a specific person you would use facial recognition. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [hypeatei](https://news.ycombinator.com/user?id=hypeatei) [6 months ago](https://news.ycombinator.com/item?id=47508251) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47508005) \| [next](https://news.ycombinator.com/item?id=47503617#47508125)\[–\]<br>I think a general description is better for surveillance/tracking like this, no? If they're at a weird angle or intentionally concealing their face then facial recognition falls apart but being able to describe them naturally would result in better tracking IMO. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [macNchz](https://news.ycombinator.com/user?id=macNchz) [6 months ago](https://news.ycombinator.com/item?id=47510328) \| [root](https://news.ycombinator.com/item?id=47503617#47506611) \| [parent](https://news.ycombinator.com/item?id=47503617#47508251) \| [next](https://news.ycombinator.com/item?id=47503617#47508125)\[–\]<br>Presumably the ideal is some kind of a fusion. Upload or tag some images/videos and link someone's social profiles and the system can look out for them based on facial recognition, gait recognition, vehicle/pets/common wardrobe items in combination. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [rigrassm](https://news.ycombinator.com/user?id=rigrassm) [6 months ago](https://news.ycombinator.com/item?id=47508125) \| [prev](https://news.ycombinator.com/item?id=47503617#47506611) \| [next](https://news.ycombinator.com/item?id=47503617#47513088)\[–\]<br>I picked up a Rexing dash cam a few months back and after getting frustrated with how clunky it is to get footage of it, I decided to look into building something out myself to browse and download the recordings without having to pull the SD card. While scrolling through the recordings, I explicitly remember thinking it would be nice to just describe what I was looking for and run a search. Looking forward to incorporating this into my project.<br>Thanks for sharing! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [npilk](https://news.ycombinator.com/user?id=npilk) [6 months ago](https://news.ycombinator.com/item?id=47513088) \| [prev](https://news.ycombinator.com/item?id=47503617#47508125) \| [next](https://news.ycombinator.com/item?id=47503617#47507935)\[–\]<br>Multimodal AI will lead to an interesting arms race in ad detection vs ad insertion. I played around with AI ad removal with older Gemini models, but it seems like this would be even more powerful to instantly identify ads (and potentially mute or strip them out).<br>[https://notes.npilk.com/experiments-with-ai-adblock](https://notes.npilk.com/experiments-with-ai-adblock) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sbinnee](https://news.ycombinator.com/user?id=sbinnee) [6 months ago](https://news.ycombinator.com/item?id=47514224) \| [parent](https://news.ycombinator.com/item?id=47503617#47513088) \| [next](https://news.ycombinator.com/item?id=47503617#47507935)\[–\]<br>Nice article. I saw someone depicting the future of web search with AI. The conclusion was not the bright future. Simply put, ads will never go away. Either AI providers will get paid for whitelisting ads, or even worse these AI will directly promote advertised products. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [WarmWash](https://news.ycombinator.com/user?id=WarmWash) [6 months ago](https://news.ycombinator.com/item?id=47517366) \| [root](https://news.ycombinator.com/item?id=47503617#47513088) \| [parent](https://news.ycombinator.com/item?id=47503617#47514224) \| [next](https://news.ycombinator.com/item?id=47503617#47520044)\[–\]<br>People could collectively decide to start paying for stuff and most of our gripes could at least switch to providers not accommodating their customers. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [greesil](https://news.ycombinator.com/user?id=greesil) [6 months ago](https://news.ycombinator.com/item?id=47517975) \| [root](https://news.ycombinator.com/item?id=47503617#47513088) \| [parent](https://news.ycombinator.com/item?id=47503617#47517366) \| [next](https://news.ycombinator.com/item?id=47503617#47520044)\[–\]<br>Collective action is not our strong suit. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [CamperBob2](https://news.ycombinator.com/user?id=CamperBob2) [6 months ago](https://news.ycombinator.com/item?id=47520044) \| [root](https://news.ycombinator.com/item?id=47503617#47513088) \| [parent](https://news.ycombinator.com/item?id=47503617#47514224) \| [prev](https://news.ycombinator.com/item?id=47503617#47517366) \| [next](https://news.ycombinator.com/item?id=47503617#47507935)\[–\]<br>To which I'd say to the advertiser, "Good luck paying off the AI adblocker running in my closet at home."<br>Then again, let's not be too hasty here. Let's see what you're willing to offer. I can sell you the eyeballs of the AI ad- _watcher_ running in my closet for $10/impression. Or, for $1000/impression, you can bring your message to the attention of myself, an actual human. A bargain at any price! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [cloogshicer](https://news.ycombinator.com/user?id=cloogshicer) [6 months ago](https://news.ycombinator.com/item?id=47507935) \| [prev](https://news.ycombinator.com/item?id=47503617#47513088) \| [next](https://news.ycombinator.com/item?id=47503617#47505089)\[–\]<br>Could this be used for creating video editing software?<br>Imagine a Premiere plugin where you could say "remove all scenes containing cats" and it'll spit out an EDL (Edit Decision List) that you can still manually adjust. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47508356) \| [parent](https://news.ycombinator.com/item?id=47503617#47507935) \| [next](https://news.ycombinator.com/item?id=47503617#47505089)\[–\]<br>Yeah, this is a great idea, I’ve actually been thinking about exactly this as the next logical step.<br>SentrySearch already returns precise in/out timestamps for any natural-language query and uses ffmpeg to auto-trim clips. Turning that into an EDL (or even a direct Premiere plugin that exports an editable cut list) feels natural.<br>I’m not a Premiere expert myself, but I’d love to see this happen. If you (or anyone) wants to sketch out a quick EDL exporter or plugin, I’ll happily review + merge a PR and help wherever I can. Just drop a GitHub issue if you start something! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [mdrzn](https://news.ycombinator.com/user?id=mdrzn) [6 months ago](https://news.ycombinator.com/item?id=47505089) \| [prev](https://news.ycombinator.com/item?id=47503617#47507935) \| [next](https://news.ycombinator.com/item?id=47503617#47510430)\[–\]<br>Very interesting (not for a dashcam, but for home monitoring). | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [SoftTalker](https://news.ycombinator.com/user?id=SoftTalker) [6 months ago](https://news.ycombinator.com/item?id=47513650) \| [parent](https://news.ycombinator.com/item?id=47503617#47505089) \| [next](https://news.ycombinator.com/item?id=47503617#47511751)\[–\]<br>Most home monitoring only records when there is movement though? So that already compresses the search space a lot. And just zipping forward and back it's pretty easy to quickly find the 30 seconds where there is a figure wallking up to your front door. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [fhe](https://news.ycombinator.com/user?id=fhe) [6 months ago](https://news.ycombinator.com/item?id=47511751) \| [parent](https://news.ycombinator.com/item?id=47503617#47505089) \| [prev](https://news.ycombinator.com/item?id=47503617#47513650) \| [next](https://news.ycombinator.com/item?id=47503617#47510430)\[–\]<br>this function will be a must-have for all home security systems. I used to spend hours going through home security cameras to check if our cat went out the house when the door was accidentally left open (turned out it was just really good at hiding within the house). | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [lwarfield](https://news.ycombinator.com/user?id=lwarfield) [6 months ago](https://news.ycombinator.com/item?id=47510430) \| [prev](https://news.ycombinator.com/item?id=47503617#47505089) \| [next](https://news.ycombinator.com/item?id=47503617#47506848)\[–\]<br>Damn, I need to going with my embeddings project. I've currently got a prototype for using embeddings (not gemini in my case) for making a game that's kinda reverse connections:<br>collections.lwarfield.dev | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [danbrooks](https://news.ycombinator.com/user?id=danbrooks) [6 months ago](https://news.ycombinator.com/item?id=47506848) \| [prev](https://news.ycombinator.com/item?id=47503617#47510430) \| [next](https://news.ycombinator.com/item?id=47503617#47506518)\[–\]<br>I work in content/video intelligence. Gemini is great for this type of use case out of the box. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [simonreiff](https://news.ycombinator.com/user?id=simonreiff) [6 months ago](https://news.ycombinator.com/item?id=47506518) \| [prev](https://news.ycombinator.com/item?id=47503617#47506848) \| [next](https://news.ycombinator.com/item?id=47503617#47506174)\[–\]<br>Very impressive! A webhook could be configured to trigger an alarm if a semantic match to any category of activities is detected, and then you basically have a virtual security guard and private investigator. Well played. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47507205) \| [parent](https://news.ycombinator.com/item?id=47503617#47506518) \| [next](https://news.ycombinator.com/item?id=47503617#47506174)\[–\]<br>Thanks! Yeah that would be pretty cool, but continuous indexing would be pretty expensive now, because the model's in public preview and there are no local alternatives afaik.<br>This very well might be a reality in a couple years though! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [jakejmnz](https://news.ycombinator.com/user?id=jakejmnz) [6 months ago](https://news.ycombinator.com/item?id=47531215) \| [root](https://news.ycombinator.com/item?id=47503617#47506518) \| [parent](https://news.ycombinator.com/item?id=47503617#47507205) \| [next](https://news.ycombinator.com/item?id=47503617#47513178)\[–\]<br>Very cool stuff, gave me the inspiration to try it locally. Works fairly well I think: [https://github.com/jakejimenez/sentinelsearch](https://github.com/jakejimenez/sentinelsearch) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [CamperBob2](https://news.ycombinator.com/user?id=CamperBob2) [6 months ago](https://news.ycombinator.com/item?id=47513178) \| [root](https://news.ycombinator.com/item?id=47503617#47506518) \| [parent](https://news.ycombinator.com/item?id=47503617#47507205) \| [prev](https://news.ycombinator.com/item?id=47503617#47531215) \| [next](https://news.ycombinator.com/item?id=47503617#47506174)\[–\]<br>Could [https://qwen.ai/blog?id=qwen3-vl-embedding](https://qwen.ai/blog?id=qwen3-vl-embedding) be a possible local alternative? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [SpaceManNabs](https://news.ycombinator.com/user?id=SpaceManNabs) [6 months ago](https://news.ycombinator.com/item?id=47506174) \| [prev](https://news.ycombinator.com/item?id=47503617#47506518) \| [next](https://news.ycombinator.com/item?id=47503617#47505771)\[–\]<br>\> No transcription, no frame captioning, no intermediate text.<br>If there is text on the video (like a caption or wtv), will the embedding capture that? Never thought about this before.<br>If the video has audio, does the embedding capture that too? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47506303) \| [parent](https://news.ycombinator.com/item?id=47503617#47506174) \| [next](https://news.ycombinator.com/item?id=47503617#47505771)\[–\]<br>Yes to both. The embedding is over raw video frames, so anything visible (text, signs, captions) gets captured in the vector. And Gemini Embedding 2 extracts the audio track and embeds it alongside the visual frames. So a query like 'someone yelling' would theoretically match on audio. My dashcam footage doesn't have audio though, so I haven't tested that side yet. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [7777777phil](https://news.ycombinator.com/user?id=7777777phil) [6 months ago](https://news.ycombinator.com/item?id=47505771) \| [prev](https://news.ycombinator.com/item?id=47503617#47506174) \| [next](https://news.ycombinator.com/item?id=47503617#47524780)\[–\]<br>Today I learned that Gemini can now natively embed video..<br>Cool Project, thanks for sharing! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [emmitska](https://news.ycombinator.com/user?id=emmitska) [6 months ago](https://news.ycombinator.com/item?id=47524780) \| [prev](https://news.ycombinator.com/item?id=47503617#47505771) \| [next](https://news.ycombinator.com/item?id=47503617#47508952)\[–\]<br>The cost structure here is what stands out to me. $2.50/hr makes this viable for personal or small-business use cases that would have been unthinkable a year ago — security footage, home cameras, dashcam archives. The interesting design question is what happens when that cost drops another 10x and this is just a default feature of consumer cameras. Most people won't opt out of something they didn't know they opted into. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [bobafett-9902](https://news.ycombinator.com/user?id=bobafett-9902) [6 months ago](https://news.ycombinator.com/item?id=47508952) \| [prev](https://news.ycombinator.com/item?id=47503617#47524780) \| [next](https://news.ycombinator.com/item?id=47503617#47514813)\[–\]<br>I wonder if the underlying improvements in visual language learning will allow for even more efficient search. The First Fully General Computer Action Model -> [https://si.inc/posts/fdm1/](https://si.inc/posts/fdm1/) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [bob1029](https://news.ycombinator.com/user?id=bob1029) [6 months ago](https://news.ycombinator.com/item?id=47514813) \| [prev](https://news.ycombinator.com/item?id=47503617#47508952) \| [next](https://news.ycombinator.com/item?id=47503617#47532895)\[–\]<br>\> Check if a video chunk contains mostly still frames. Extracts 3 evenly-spaced frames as JPEG and compares file sizes.<br>I believe you could use a combination of select and scene parameters in ffmpeg to do this automatically when a chunk of video is created each time. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [shivang2607](https://news.ycombinator.com/user?id=shivang2607) [6 months ago](https://news.ycombinator.com/item?id=47532895) \| [prev](https://news.ycombinator.com/item?id=47503617#47514813) \| [next](https://news.ycombinator.com/item?id=47503617#47514530)\[–\]<br>But don't you think 768 dimensional space is too less for comparing a video ? I build a similarity search for Anime and it worked Okayish. Really interested to know how it will work for video similarity search. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [novoreorx](https://news.ycombinator.com/user?id=novoreorx) [6 months ago](https://news.ycombinator.com/item?id=47514530) \| [prev](https://news.ycombinator.com/item?id=47503617#47532895) \| [next](https://news.ycombinator.com/item?id=47503617#47509946)\[–\]<br>In the demo bro shows how to search for "a car with a bike rack on the back that cut me off at night." Given the grudge he must've held from being cut off, I strongly suspect that finding this specific car was his main motivation for building the project in the first place | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47517675) \| [parent](https://news.ycombinator.com/item?id=47503617#47514530) \| [next](https://news.ycombinator.com/item?id=47503617#47509946)\[–\]<br>ur not wrong | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [WatchDog](https://news.ycombinator.com/user?id=WatchDog) [6 months ago](https://news.ycombinator.com/item?id=47509946) \| [prev](https://news.ycombinator.com/item?id=47503617#47514530) \| [next](https://news.ycombinator.com/item?id=47503617#47506364)\[–\]<br>I don't quite understand the 5 second overlap. <br>I assume it's so that events that occur over the chunk boundary don't get missed, but is there any examples or benchmarking to examine how useful this is? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47510466) \| [parent](https://news.ycombinator.com/item?id=47503617#47509946) \| [next](https://news.ycombinator.com/item?id=47503617#47506364)\[–\]<br>yea, it's so events on a chunk boundary still get captured in at least one chunk. i haven't had the chance to do formal benchmarks on overlap vs. no-overlap yet. the 5s default is a pragmatic choice, long enough to catch most events that would otherwise be split, short enough to not add much cost (120 chunks/hr to ~138). also it's configurable via the --overlap flag. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [nullbyte](https://news.ycombinator.com/user?id=nullbyte) [6 months ago](https://news.ycombinator.com/item?id=47506364) \| [prev](https://news.ycombinator.com/item?id=47503617#47509946) \| [next](https://news.ycombinator.com/item?id=47503617#47513373)\[–\]<br>What a brilliant idea! is this all done locally? That's incredible. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [apwheele](https://news.ycombinator.com/user?id=apwheele) [6 months ago](https://news.ycombinator.com/item?id=47506445) \| [parent](https://news.ycombinator.com/item?id=47503617#47506364) \| [next](https://news.ycombinator.com/item?id=47503617#47531226)\[–\]<br>While the vector store is local, it is sending the data to Gemini's API for embedding. (Which if using a paid API key is probably fine for most use cases, no long term retention/training etc.) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [jakejmnz](https://news.ycombinator.com/user?id=jakejmnz) [6 months ago](https://news.ycombinator.com/item?id=47531233) \| [root](https://news.ycombinator.com/item?id=47503617#47506364) \| [parent](https://news.ycombinator.com/item?id=47503617#47506445) \| [next](https://news.ycombinator.com/item?id=47503617#47531226)\[–\]<br>works completely locally with a decent model: [https://github.com/jakejimenez/sentinelsearch](https://github.com/jakejimenez/sentinelsearch) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [jakejmnz](https://news.ycombinator.com/user?id=jakejmnz) [6 months ago](https://news.ycombinator.com/item?id=47531226) \| [parent](https://news.ycombinator.com/item?id=47503617#47506364) \| [prev](https://news.ycombinator.com/item?id=47503617#47506445) \| [next](https://news.ycombinator.com/item?id=47503617#47513373)\[–\]<br>Make a proof of concept, honestly worked fairly well: [https://github.com/jakejimenez/sentinelsearch](https://github.com/jakejimenez/sentinelsearch) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [febed](https://news.ycombinator.com/user?id=febed) [6 months ago](https://news.ycombinator.com/item?id=47513373) \| [prev](https://news.ycombinator.com/item?id=47503617#47506364) \| [next](https://news.ycombinator.com/item?id=47503617#47504790)\[–\]<br>This seems like something that would be very expensive to run. Do you have some representative figures at a particular resolution and frame rate? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [addandsubtract](https://news.ycombinator.com/user?id=addandsubtract) [6 months ago](https://news.ycombinator.com/item?id=47520027) \| [parent](https://news.ycombinator.com/item?id=47503617#47513373) \| [next](https://news.ycombinator.com/item?id=47503617#47504790)\[–\]<br>The README on the GitHub has a section on this\[0\]:<br>>Indexing 1 hour of footage costs ~$2.84 with Gemini's embedding API (default settings: 30s chunks, 5s overlap):<br>>1 hour = 3,600 seconds of video = 3,600 frames processed by the model. 3,600 frames × $0.00079 = ~$2.84/hr<br>>The Gemini API natively extracts and tokenizes exactly 1 frame per second from uploaded video, regardless of the file's actual frame rate. The preprocessing step (which downscales chunks to 480p at 5fps via ffmpeg) is a local/bandwidth optimization — it keeps payload sizes small so API requests are fast and don't timeout — but does not change the number of frames the API processes.<br>\[0\] [https://github.com/ssrajadh/sentrysearch#cost](https://github.com/ssrajadh/sentrysearch#cost) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [ygouzerh](https://news.ycombinator.com/user?id=ygouzerh) [6 months ago](https://news.ycombinator.com/item?id=47504790) \| [prev](https://news.ycombinator.com/item?id=47503617#47513373) \| [next](https://news.ycombinator.com/item?id=47503617#47504887)\[–\]<br>That's quite interesting, well done! I haven't thought of this use case for embeddings. It open the door to quite many potential applications! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [stavros](https://news.ycombinator.com/user?id=stavros) [6 months ago](https://news.ycombinator.com/item?id=47505302) \| [parent](https://news.ycombinator.com/item?id=47503617#47504790) \| [next](https://news.ycombinator.com/item?id=47503617#47504887)\[–\]<br>Man, the surveillance applications for this are staggering. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [dev\_tools\_lab](https://news.ycombinator.com/user?id=dev_tools_lab) [6 months ago](https://news.ycombinator.com/item?id=47504887) \| [prev](https://news.ycombinator.com/item?id=47503617#47504790) \| [next](https://news.ycombinator.com/item?id=47503617#47534287)\[–\]<br>Nice use of native video embedding. How do you handle <br>cases where Gemini's response confidence is low? <br>Do you have a fallback or threshold? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47505369) \| [parent](https://news.ycombinator.com/item?id=47503617#47504887) \| [next](https://news.ycombinator.com/item?id=47503617#47534287)\[–\]<br>as of now, no threshold but that is planned in the future.<br>for example, for now if i search "cybertruck" in my indexed dashcam footage, i don't have any cybertrucks in my footage, so it'll return a clip of the next best match which is a big truck, but not a cybertruck | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [dev\_tools\_lab](https://news.ycombinator.com/user?id=dev_tools_lab) [6 months ago](https://news.ycombinator.com/item?id=47515177) \| [root](https://news.ycombinator.com/item?id=47503617#47504887) \| [parent](https://news.ycombinator.com/item?id=47503617#47505369) \| [next](https://news.ycombinator.com/item?id=47503617#47534287)\[–\]<br>Makes sense for now. Thresholding becomes <br>critical at scale though — good luck with <br>the next iteration! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [wuliwong](https://news.ycombinator.com/user?id=wuliwong) [6 months ago](https://news.ycombinator.com/item?id=47534287) \| [prev](https://news.ycombinator.com/item?id=47503617#47504887) \| [next](https://news.ycombinator.com/item?id=47503617#47512141)\[–\]<br>I am working on a really similar thing. My buddy just sent me this. Hit me up if you wanna chat! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [rao-v](https://news.ycombinator.com/user?id=rao-v) [6 months ago](https://news.ycombinator.com/item?id=47512141) \| [prev](https://news.ycombinator.com/item?id=47503617#47534287) \| [next](https://news.ycombinator.com/item?id=47503617#47506066)\[–\]<br>Is there a decent open video embedding model out there? I’d love to play with this without uploading video. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [kamranjon](https://news.ycombinator.com/user?id=kamranjon) [6 months ago](https://news.ycombinator.com/item?id=47506066) \| [prev](https://news.ycombinator.com/item?id=47503617#47512141) \| [next](https://news.ycombinator.com/item?id=47503617#47510942)\[–\]<br>Does anyone know of an open weights models that can embed video? Would love to experiment locally with this. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47506358) \| [parent](https://news.ycombinator.com/item?id=47503617#47506066) \| [next](https://news.ycombinator.com/item?id=47503617#47513187)\[–\]<br>Not aware of any that do native video-to-vector embedding the way Gemini Embedding 2 does. There are CLIP-based models (like VideoCLIP) that embed frames individually, but they don't process temporal video. you'd need to average frame embeddings which loses a lot.<br>Would love to see open-weight models with this capability since it would eliminate the API cost and the privacy concern of uploading footage. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [CamperBob2](https://news.ycombinator.com/user?id=CamperBob2) [6 months ago](https://news.ycombinator.com/item?id=47513187) \| [parent](https://news.ycombinator.com/item?id=47503617#47506066) \| [prev](https://news.ycombinator.com/item?id=47503617#47506358) \| [next](https://news.ycombinator.com/item?id=47503617#47510942)\[–\]<br>A quick search brought up [https://qwen.ai/blog?id=qwen3-vl-embedding](https://qwen.ai/blog?id=qwen3-vl-embedding) but I have no idea if it does what Gemini is doing here. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [jakejmnz](https://news.ycombinator.com/user?id=jakejmnz) [6 months ago](https://news.ycombinator.com/item?id=47520744) \| [root](https://news.ycombinator.com/item?id=47503617#47506066) \| [parent](https://news.ycombinator.com/item?id=47503617#47513187) \| [next](https://news.ycombinator.com/item?id=47503617#47510942)\[–\]<br>more or less works similarly, made a proof of concept for it: [https://github.com/jakejimenez/sentinelsearch](https://github.com/jakejimenez/sentinelsearch) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [CamperBob2](https://news.ycombinator.com/user?id=CamperBob2) [6 months ago](https://news.ycombinator.com/item?id=47526656) \| [root](https://news.ycombinator.com/item?id=47503617#47506066) \| [parent](https://news.ycombinator.com/item?id=47503617#47520744) \| [next](https://news.ycombinator.com/item?id=47503617#47510942)\[–\]<br>Very cool, thanks. Will check it out. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [cat-turner](https://news.ycombinator.com/user?id=cat-turner) [6 months ago](https://news.ycombinator.com/item?id=47510942) \| [prev](https://news.ycombinator.com/item?id=47503617#47506066) \| [next](https://news.ycombinator.com/item?id=47503617#47514760)\[–\]<br>This is great, thanks for sharing | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [subhashp](https://news.ycombinator.com/user?id=subhashp) [6 months ago](https://news.ycombinator.com/item?id=47514760) \| [prev](https://news.ycombinator.com/item?id=47503617#47510942) \| [next](https://news.ycombinator.com/item?id=47503617#47513930)\[–\]<br>Can I give it a photo of a person and ask it to search for the person in the video? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [martz](https://news.ycombinator.com/user?id=martz) [6 months ago](https://news.ycombinator.com/item?id=47513930) \| [prev](https://news.ycombinator.com/item?id=47503617#47514760) \| [next](https://news.ycombinator.com/item?id=47503617#47508144)\[–\]<br>this can be done locally [https://github.com/intel/openvino-ai-video-retrieval-analysi...](https://github.com/intel/openvino-ai-video-retrieval-analysis) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [totisjosema](https://news.ycombinator.com/user?id=totisjosema) [6 months ago](https://news.ycombinator.com/item?id=47508144) \| [prev](https://news.ycombinator.com/item?id=47503617#47513930) \| [next](https://news.ycombinator.com/item?id=47503617#47528141)\[–\]<br>What is your experience so far with the quality of the retrieved pieces? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47508195) \| [parent](https://news.ycombinator.com/item?id=47503617#47508144) \| [next](https://news.ycombinator.com/item?id=47503617#47528141)\[–\]<br>I've found I have to be very specific to get the clip I'm searching for. For example, "car cuts me off" just returned a clip of a car driving past my blindspot. But, "car with bike rack on back cuts me off at night" gave me exactly the clip I was looking for. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [giversoftheint](https://news.ycombinator.com/user?id=giversoftheint) [6 months ago](https://news.ycombinator.com/item?id=47528141) \| [prev](https://news.ycombinator.com/item?id=47503617#47508144) \| [next](https://news.ycombinator.com/item?id=47503617#47512318)\[–\]<br>Oh I'm getting this for my website. Cool. Thanks. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sans\_souse](https://news.ycombinator.com/user?id=sans_souse) [6 months ago](https://news.ycombinator.com/item?id=47512318) \| [prev](https://news.ycombinator.com/item?id=47503617#47528141) \| [next](https://news.ycombinator.com/item?id=47503617#47521001)\[–\]<br>Total aside here but is that you driving the pickup I assume? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47512341) \| [parent](https://news.ycombinator.com/item?id=47503617#47512318) \| [next](https://news.ycombinator.com/item?id=47503617#47521001)\[–\]<br>haha no i'm driving the tesla and that clip is from the left repeater camera (teslas record from all around the car) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [ideashower](https://news.ycombinator.com/user?id=ideashower) [6 months ago](https://news.ycombinator.com/item?id=47521001) \| [prev](https://news.ycombinator.com/item?id=47503617#47512318) \| [next](https://news.ycombinator.com/item?id=47503617#47512290)\[–\]<br>Is there a local model that this would work with? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [crashabr](https://news.ycombinator.com/user?id=crashabr) [6 months ago](https://news.ycombinator.com/item?id=47512290) \| [prev](https://news.ycombinator.com/item?id=47503617#47521001) \| [next](https://news.ycombinator.com/item?id=47503617#47505320)\[–\]<br>I wonder how well this would work with dance videos. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [Aeroi](https://news.ycombinator.com/user?id=Aeroi) [6 months ago](https://news.ycombinator.com/item?id=47505320) \| [prev](https://news.ycombinator.com/item?id=47503617#47512290) \| [next](https://news.ycombinator.com/item?id=47503617#47510087)\[–\]<br>very cool, anybody have apparent use cases for this? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [mannyv](https://news.ycombinator.com/user?id=mannyv) [6 months ago](https://news.ycombinator.com/item?id=47510806) \| [parent](https://news.ycombinator.com/item?id=47503617#47505320) \| [next](https://news.ycombinator.com/item?id=47503617#47505572)\[–\]<br>Indexing all your porn and skipping all the filler. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [iso1631](https://news.ycombinator.com/user?id=iso1631) [6 months ago](https://news.ycombinator.com/item?id=47516306) \| [root](https://news.ycombinator.com/item?id=47503617#47505320) \| [parent](https://news.ycombinator.com/item?id=47503617#47510806) \| [next](https://news.ycombinator.com/item?id=47503617#47505572)\[–\]<br>isn't the "fill her" the point of porn? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47505572) \| [parent](https://news.ycombinator.com/item?id=47503617#47505320) \| [prev](https://news.ycombinator.com/item?id=47503617#47510806) \| [next](https://news.ycombinator.com/item?id=47503617#47513124)\[–\]<br>dashcam and home security footage are the 2 main ones i can think of.<br>a bit expensive right now so it's not as practical at scale. but once the embedding model comes out of public preview, and we hopefully get a local equivalent, this will be a lot more practical. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [CamperBob2](https://news.ycombinator.com/user?id=CamperBob2) [6 months ago](https://news.ycombinator.com/item?id=47513124) \| [parent](https://news.ycombinator.com/item?id=47503617#47505320) \| [prev](https://news.ycombinator.com/item?id=47503617#47505572) \| [next](https://news.ycombinator.com/item?id=47503617#47506029)\[–\]<br>Trail and game cams come to mind. "Create a montage of all deer encounters," "Find first appearance of black bear this year," that sort of thing. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [giozaarour](https://news.ycombinator.com/user?id=giozaarour) [6 months ago](https://news.ycombinator.com/item?id=47506029) \| [parent](https://news.ycombinator.com/item?id=47503617#47505320) \| [prev](https://news.ycombinator.com/item?id=47503617#47513124) \| [next](https://news.ycombinator.com/item?id=47503617#47505784)\[–\]<br>I think a good use case would be searching for certain products or videos across social media (TikTok and Instagram). especially useful for shopping, maybe | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [vidarh](https://news.ycombinator.com/user?id=vidarh) [6 months ago](https://news.ycombinator.com/item?id=47506227) \| [root](https://news.ycombinator.com/item?id=47503617#47505320) \| [parent](https://news.ycombinator.com/item?id=47503617#47506029) \| [next](https://news.ycombinator.com/item?id=47503617#47505784)\[–\]<br>Branding/marketing monitoring companies would be all over this. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [hebelehubele](https://news.ycombinator.com/user?id=hebelehubele) [6 months ago](https://news.ycombinator.com/item?id=47505784) \| [parent](https://news.ycombinator.com/item?id=47503617#47505320) \| [prev](https://news.ycombinator.com/item?id=47503617#47506029) \| [next](https://news.ycombinator.com/item?id=47503617#47510087)\[–\]<br>State surveillance | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [wahnfrieden](https://news.ycombinator.com/user?id=wahnfrieden) [6 months ago](https://news.ycombinator.com/item?id=47506213) \| [root](https://news.ycombinator.com/item?id=47503617#47505320) \| [parent](https://news.ycombinator.com/item?id=47503617#47505784) \| [next](https://news.ycombinator.com/item?id=47503617#47510087)\[–\]<br>Worker surveillance | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [thegabriele](https://news.ycombinator.com/user?id=thegabriele) [6 months ago](https://news.ycombinator.com/item?id=47510087) \| [prev](https://news.ycombinator.com/item?id=47503617#47505320) \| [next](https://news.ycombinator.com/item?id=47503617#47505177)\[–\]<br>Why just the dash cam? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47510383) \| [parent](https://news.ycombinator.com/item?id=47503617#47510087) \| [next](https://news.ycombinator.com/item?id=47503617#47505177)\[–\]<br>dashcam is just one of the use cases and the one i tested on. but this could theoretically work with any kind of video footage like home security footage | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [klntsky](https://news.ycombinator.com/user?id=klntsky) [6 months ago](https://news.ycombinator.com/item?id=47505177) \| [prev](https://news.ycombinator.com/item?id=47503617#47510087) \| [next](https://news.ycombinator.com/item?id=47503617#47511952)\[–\]<br>why not skip the text conversion? is it usable at all? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sohamrj](https://news.ycombinator.com/user?id=sohamrj) [6 months ago](https://news.ycombinator.com/item?id=47505271) \| [parent](https://news.ycombinator.com/item?id=47503617#47505177) \| [next](https://news.ycombinator.com/item?id=47503617#47511952)\[–\]<br>gemini embedding 2 converts straight video to vectors. in this case, dashcam clips don't have audio to transcribe and even if they did, it would be useless in the search | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [password4321](https://news.ycombinator.com/user?id=password4321) [6 months ago](https://news.ycombinator.com/item?id=47505729) \| [root](https://news.ycombinator.com/item?id=47503617#47505177) \| [parent](https://news.ycombinator.com/item?id=47503617#47505271) \| [next](https://news.ycombinator.com/item?id=47503617#47511952)\[–\]<br>What are the SoA audio models right now? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [emsign](https://news.ycombinator.com/user?id=emsign) [6 months ago](https://news.ycombinator.com/item?id=47505718) \| [prev](https://news.ycombinator.com/item?id=47503617#47514239) \| [next](https://news.ycombinator.com/item?id=47503617#47522669)\[–\]<br>Where is the Exit to this dystopia? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [nclin\_](https://news.ycombinator.com/user?id=nclin_) [6 months ago](https://news.ycombinator.com/item?id=47506910) \| [parent](https://news.ycombinator.com/item?id=47503617#47505718) \| [next](https://news.ycombinator.com/item?id=47503617#47506417)\[–\]<br>Well, with data analysis powers like this a few treasonous words in front of a flock camera will show you the way. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [RobotToaster](https://news.ycombinator.com/user?id=RobotToaster) [6 months ago](https://news.ycombinator.com/item?id=47506417) \| [parent](https://news.ycombinator.com/item?id=47503617#47505718) \| [prev](https://news.ycombinator.com/item?id=47503617#47506910) \| [next](https://news.ycombinator.com/item?id=47503617#47510261)\[–\]<br>In the matrix the exit was pay phones, which perhaps explains why our overlords are removing them | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [greesil](https://news.ycombinator.com/user?id=greesil) [6 months ago](https://news.ycombinator.com/item?id=47517986) \| [root](https://news.ycombinator.com/item?id=47503617#47505718) \| [parent](https://news.ycombinator.com/item?id=47503617#47506417) \| [next](https://news.ycombinator.com/item?id=47503617#47510261)\[–\]<br>Suicide booths a la Futurama | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [anxoo](https://news.ycombinator.com/user?id=anxoo) [6 months ago](https://news.ycombinator.com/item?id=47510261) \| [parent](https://news.ycombinator.com/item?id=47503617#47505718) \| [prev](https://news.ycombinator.com/item?id=47503617#47506417) \| [next](https://news.ycombinator.com/item?id=47503617#47514550)\[–\]<br>[https://pauseai.info/](https://pauseai.info/) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sbinnee](https://news.ycombinator.com/user?id=sbinnee) [6 months ago](https://news.ycombinator.com/item?id=47514241) \| [root](https://news.ycombinator.com/item?id=47503617#47505718) \| [parent](https://news.ycombinator.com/item?id=47503617#47510261) \| [next](https://news.ycombinator.com/item?id=47503617#47514550)\[–\]<br>Thanks for sharing. They say "pause", not stop. Assume that we pause now. When should we resume then? How do we know? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [moomoo11](https://news.ycombinator.com/user?id=moomoo11) [6 months ago](https://news.ycombinator.com/item?id=47514550) \| [parent](https://news.ycombinator.com/item?id=47503617#47505718) \| [prev](https://news.ycombinator.com/item?id=47503617#47510261) \| [next](https://news.ycombinator.com/item?id=47503617#47506644)\[–\]<br>You don’t wanna live in Night City? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [jama211](https://news.ycombinator.com/user?id=jama211) [6 months ago](https://news.ycombinator.com/item?id=47506644) \| [parent](https://news.ycombinator.com/item?id=47503617#47505718) \| [prev](https://news.ycombinator.com/item?id=47503617#47514550) \| [next](https://news.ycombinator.com/item?id=47503617#47506749)\[–\]<br>I don’t think this means we’re in a dystopia | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [zwirbl](https://news.ycombinator.com/user?id=zwirbl) [6 months ago](https://news.ycombinator.com/item?id=47507040) \| [root](https://news.ycombinator.com/item?id=47503617#47505718) \| [parent](https://news.ycombinator.com/item?id=47503617#47506644) \| [next](https://news.ycombinator.com/item?id=47503617#47506749)\[–\]<br>You might not have been paying attention | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [52-6F-62](https://news.ycombinator.com/user?id=52-6F-62) [6 months ago](https://news.ycombinator.com/item?id=47507377) \| [root](https://news.ycombinator.com/item?id=47503617#47505718) \| [parent](https://news.ycombinator.com/item?id=47503617#47507040) \| [next](https://news.ycombinator.com/item?id=47503617#47506749)\[–\]<br>I think Radiohead said that | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [draw\_down](https://news.ycombinator.com/user?id=draw_down) [6 months ago](https://news.ycombinator.com/item?id=47506749) \| [parent](https://news.ycombinator.com/item?id=47503617#47505718) \| [prev](https://news.ycombinator.com/item?id=47503617#47506644) \| [next](https://news.ycombinator.com/item?id=47503617#47505964)\[–\]<br>The dystopia of searching for video clips and finding them? What? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [bitexploder](https://news.ycombinator.com/user?id=bitexploder) [6 months ago](https://news.ycombinator.com/item?id=47510239) \| [root](https://news.ycombinator.com/item?id=47503617#47505718) \| [parent](https://news.ycombinator.com/item?id=47503617#47506749) \| [next](https://news.ycombinator.com/item?id=47503617#47505964)\[–\]<br>Yes? Right now it is relatively expensive to search video. As embedding tech like this advances and makes it even cheaper it just increases the ability to search and analyze every movement. “Locate speech patterns that indicate dissident activity using the dissident activity skill” | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [BrokenCogs](https://news.ycombinator.com/user?id=BrokenCogs) [6 months ago](https://news.ycombinator.com/item?id=47505964) \| [parent](https://news.ycombinator.com/item?id=47503617#47505718) \| [prev](https://news.ycombinator.com/item?id=47503617#47506749) \| [next](https://news.ycombinator.com/item?id=47503617#47522669)\[–\]<br>The Matrix style human pods: we live in blissful ignorance in the Matrix, while the LLMs extract more and more compute power from us so some CEO somewhere can claim they have now replaced all humans with machines in their business. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [throwup238](https://news.ycombinator.com/user?id=throwup238) [6 months ago](https://news.ycombinator.com/item?id=47506191) \| [root](https://news.ycombinator.com/item?id=47503617#47505718) \| [parent](https://news.ycombinator.com/item?id=47503617#47505964) \| [next](https://news.ycombinator.com/item?id=47503617#47506362)\[–\]<br>I was thinking more of the season 3 episode of Doctor Who titled _Gridlock_ where everyone lives in flying cars circling a giant expressway underground, while all the upper class people on the surface died years ago from a pandemic. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [ting0](https://news.ycombinator.com/user?id=ting0) [6 months ago](https://news.ycombinator.com/item?id=47506362) \| [root](https://news.ycombinator.com/item?id=47503617#47505718) \| [parent](https://news.ycombinator.com/item?id=47503617#47505964) \| [prev](https://news.ycombinator.com/item?id=47503617#47506191) \| [next](https://news.ycombinator.com/item?id=47503617#47522669)\[–\]<br>Ever get the feeling that the universe is reading your mind? Maybe there's some truth to that after all. | | |
| ![](https://news.ycombinator.com/s.gif)

|     |
| --- |
|  |

[Guidelines](https://news.ycombinator.com/newsguidelines.html) \| [FAQ](https://news.ycombinator.com/newsfaq.html) \| [Lists](https://news.ycombinator.com/lists) \| [API](https://github.com/HackerNews/API) \| [Security](https://news.ycombinator.com/security.html) \| [Legal](https://www.ycombinator.com/legal/) \| [Apply to YC](https://www.ycombinator.com/apply/) \| [Contact](mailto:hn@ycombinator.com)

Search: |