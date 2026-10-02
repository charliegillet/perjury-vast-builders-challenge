[Skip to content](https://arstechnica.com/google/2025/10/unexpectedly-a-deer-briefly-entered-the-family-room-living-with-gemini-home/#main)

Text
settings

Story text

SizeSmallStandardLargeWidth
\*StandardWideLinksStandardOrange

\\* Subscribers only

[Learn more](https://arstechnica.com/store/product/subscriptions/)

Minimize to nav


You just can’t ignore the effects of the generative AI boom.

Even if you don’t go looking for AI bots, they’re being integrated into virtually every product and service. And for what? There’s a lot of hand-wavey chatter about agentic this and AGI that, but what can “gen AI” do for you right now? [Gemini for Home](https://arstechnica.com/google/2025/10/googles-gemini-powered-smart-home-revamp-is-here-with-a-new-app-and-cameras/) is Google’s latest attempt to make this technology useful, integrating Gemini with the smart home devices people already have. Anyone paying for extended video history in the Home app is about to get a heaping helping of AI, including daily summaries, AI-labeled notifications, and more.

Given the supposed power of AI models like Gemini, recognizing events in a couple of videos and answering questions about them doesn’t seem like a bridge too far. And yet Gemini for Home has demonstrated a tenuous grasp of the truth, which can lead to some disquieting interactions, like periodic warnings of home invasion, both human and animal.

It can do some neat things, but is it worth the price—and the headaches?

## Does your smart home need a premium AI subscription?

Simply using the Google Home app to control your devices does not turn your smart home over to Gemini. This is part of Google’s higher-tier paid service, which comes with extended camera history and Gemini features for $20 per month. That subscription pipes your video into a Gemini AI model that generates summaries for notifications, as well as a “Daily Brief” that offers a rundown of everything that happened on a given day. The cheaper $10 plan provides less video history and no AI-assisted summaries or notifications. Both plans enable Gemini Live on smart speakers.

According to Google, it doesn’t send all of your video to Gemini. That would be a huge waste of compute cycles, so Gemini only sees (and summarizes) event clips. Those summaries are then distilled at the end of the day to create the Daily Brief, which usually results in a rather boring list of people entering and leaving rooms, dropping off packages, and so on.

Importantly, the Gemini model powering this experience is not multimodal—it only processes visual elements of videos and does not integrate audio from your recordings. So unusual noises or conversations captured by your cameras will not be searchable or reflected in AI summaries. This may be intentional to ensure your conversations are not regurgitated by an AI.

![Gemini smart home plans](https://cdn.arstechnica.net/wp-content/uploads/2025/10/Gemini-plans.png)

Credit:
Google


Credit:


Google



Paying for Google’s AI-infused subscription also adds Ask Home, a conversational chatbot that can answer questions about what has happened in your home based on the status of smart home devices and your video footage. You can ask questions about events, retrieve video clips, and create automations.

There are definitely some issues with Gemini’s understanding of video, but Ask Home is quite good at creating automations. It was possible to set up automations in the old Home app, but the updated AI is able to piece together automations based on your natural language request. Perhaps thanks to the limited set of possible automation elements, the AI gets this right most of the time. Ask Home is also usually able to dig up past event clips, as long as you are specific about what you want.

The Advanced plan for Gemini Home keeps your videos for 60 days, so you can only query the robot on clips from that time period. Google also says it does not retain any of that video for training. The only instance in which Google will use security camera footage for training is if you choose to “lend” it to Google via an obscure option in the Home app. Google says it will keep these videos for up to 18 months or until you revoke access. However, your interactions with Gemini (like your typed prompts and ratings of outputs) are used to refine the model.

## The unexpected deer

Every generative AI bot makes the occasional mistake, but you’ll probably not notice every one. When the AI hallucinates about your daily life, however, it’s more noticeable. There’s no reason Google should be confused by my smart home setup, which features a couple of outdoor cameras and one indoor camera—all Nest-branded with all the default AI features enabled—to keep an eye on my dogs. So the AI is seeing a lot of dogs lounging around and staring out the window. One would hope that it could reliably summarize something so straightforward.

One may be disappointed, though.

In my first Daily Brief, I was fascinated to see that Google spotted some indoor wildlife. “Unexpectedly, a deer briefly entered the family room,” Gemini said.

![Home Brief with deer](https://cdn.arstechnica.net/wp-content/uploads/2025/10/deer-e1761768371476.png)

Dogs and deer are pretty much the same thing, right?


Credit:
Ryan Whitwam


Dogs and deer are pretty much the same thing, right?


Credit:


Ryan Whitwam



Gemini does deserve some credit for recognizing that the appearance of a deer in the family room would be unexpected. But the “deer” was, naturally, a dog. This was not a one-time occurrence, either. Gemini sometimes identifies my dogs correctly, but many event clips and summaries still tell me about the notable but brief appearance of deer around the house and yard.

This deer situation serves as a keen reminder that this new type of AI doesn’t “think,” although the industry’s [use of that term](https://arstechnica.com/ai/2025/08/google-releases-gemini-2-5-deep-think-for-ai-ultra-subscribers/) to describe simulated reasoning could lead you to believe otherwise. A person looking at this video wouldn’t even entertain the possibility that they were seeing a deer after they’ve already seen the dogs loping around in other videos. Gemini doesn’t have that base of common sense, though. If the tokens say deer, it’s a deer. I will say, though, Gemini is great at recognizing car models and brand logos. Make of that what you will.

The animal mix-up is not ideal, but it’s not a major hurdle to usability. I didn’t seriously entertain the possibility that a deer had wandered into the house, and it’s a little funny the way the daily report continues to express amazement that wildlife is invading. It’s a pretty harmless screw-up.

“Overall identification accuracy depends on several factors, including the visual details available in the camera clip for Gemini to process,” explains a Google spokesperson. “As a large language model, Gemini can sometimes make inferential mistakes, which leads to these misidentifications, such as confusing your dog with a cat or deer.”

Google also says that you can tune the AI by correcting it when it screws up. This works sometimes, but the system still doesn’t truly understand anything—that’s beyond the capabilities of a generative AI model. After telling Gemini that it’s seeing dogs rather than deer, it sees wildlife less often. However, it doesn’t seem to trust me all the time, causing it to report the appearance of a deer that is “probably” just a dog.

## A perfect fit for spooky season

Gemini’s smart home hallucinations also have a less comedic side. When Gemini mislabels an event clip, you can end up with some pretty distressing alerts. Imagine that you’re out and about when your Gemini assistant hits you with a notification telling you, “A person was seen in the family room.”

A person roaming around the house you believed to be empty? That’s alarming. Is it an intruder, a hallucination, a _ghost_? So naturally, you check the camera feed to find… nothing. An Ars Technica investigation confirms AI cannot detect ghosts. So a ghost in the machine?

![](https://cdn.arstechnica.net/wp-content/uploads/2025/10/Some-security.jpg)

Oops, we made you think someone broke into your house.


Credit:
Ryan Whitwam


Oops, we made you think someone broke into your house.


Credit:


Ryan Whitwam



On several occasions, I’ve seen Gemini mistake dogs and totally empty rooms (or maybe a shadow?) for a person. It may be alarming at first, but after a few false positives, you grow to distrust the robot. Now, even if Gemini correctly identified a random person in the house, I’d probably ignore it. This is the default notification experience for Gemini Home Advanced. If you want to turn off these notifications and return to the classic version, you have to [disable Gemini for Home](https://support.google.com/googlenest/answer/15542305?hl=en#zippy=%2Chow-to-enable-gemini-for-home-camera-features) on each affected camera. Google noted that you can also disable person alerts in the app. Those are enabled when you turn on Google’s familiar faces detection.

Gemini often twists reality just a bit instead of creating it from whole cloth. A person holding anything in the backyard is doing yardwork. One person anywhere, doing anything, becomes several people. A dog toy becomes a cat lying in the sun. A couple of birds become a raccoon. Gemini likes to ignore things, too, like denying there was a package delivery even when there’s a video tagged as “person delivers package.”

![Gemini misses package](https://cdn.arstechnica.net/wp-content/uploads/2025/10/Gemini-package.png)

Gemini still refused to admit it was wrong.


Credit:
Ryan Whitwam


Gemini still refused to admit it was wrong.


Credit:


Ryan Whitwam



At the end of the day, Gemini is labeling _most_ clips correctly and therefore produces mostly accurate, if sometimes unhelpful, notifications. The problem is the flip side of “mostly,” which is still a lot of mistakes. Some of these mistakes compel you to check your cameras—at least, before you grow weary of Gemini’s confabulations. Instead of saving time and keeping you apprised of what’s happening at home, it wastes your time. For this thing to be useful, inferential errors cannot be a daily occurrence.

## Learning as it goes

Google says its goal is to make Gemini for Home better for everyone. The team is “investing heavily in improving accurate identification” to cut down on erroneous notifications. The company also believes that having people add custom instructions is a critical piece of the puzzle. Maybe in the future, Gemini for Home will be more honest, but it currently takes a lot of hand-holding to move it in the right direction.

With careful tuning, you can indeed address some of Gemini for Home’s flights of fancy. I see fewer deer identifications after tinkering, and a couple of custom instructions have made the Home Brief waste less space telling me when people walk into and out of rooms that don’t exist. But I still don’t know how to prompt my way out of Gemini seeing people in an empty room.

![Nest Cam 2025](https://cdn.arstechnica.net/wp-content/uploads/2025/10/Google-Gemini-Home-1.jpg)

Gemini AI features work on all Nest cams, but the new 2025 models are “designed for Gemini.”


Credit:
Ryan Whitwam


Gemini AI features work on all Nest cams, but the new 2025 models are “designed for Gemini.”


Credit:


Ryan Whitwam



Despite its intention to improve Gemini for Home, Google is releasing a product that just doesn’t work very well out of the box, and it misbehaves in ways that are genuinely off-putting. Security cameras shouldn’t lie about seeing intruders, nor should they tell me _I’m_ lying when they fail to recognize an event. The Ask Home bot has the standard disclaimer recommending that you verify what the AI says. You have to take that warning seriously with Gemini for Home.

At launch, it’s hard to justify paying for the $20 Advanced Gemini subscription. If you’re already paying because you want the 60-day event history, you’re stuck with the AI notifications. You can ignore the existence of Daily Brief, though. Stepping down to the $10 per month subscription gets you just 30 days of event history with the old non-generative notifications and event labeling. Maybe that’s the smarter smart home bet right now.

Gemini for Home is widely available for those who opted into early access in the Home app. So you can avoid Gemini for the time being, but it’s only a matter of time before Google flips the switch for everyone.

Hopefully it works better by then.

_Updated 11/3 with a clarification from Google on AI notifications._

[![Photo of Ryan Whitwam](https://cdn.arstechnica.net/wp-content/uploads/2025/02/AV4.jpg)](https://arstechnica.com/author/ryanwhitwam/)

[Ryan Whitwam](https://arstechnica.com/author/ryanwhitwam/) Senior Technology Reporter

[Ryan Whitwam](https://arstechnica.com/author/ryanwhitwam/) Senior Technology Reporter

Ryan Whitwam is a senior technology reporter at Ars Technica, covering the ways Google, AI, and mobile technology continue to change the world. Over his 20-year career, he's written for Android Police, ExtremeTech, Wirecutter, NY Times, and more. He has reviewed more phones than most people will ever own. You can [follow him on Bluesky](https://bsky.app/profile/rwhitwam.bsky.social), where you will see photos of his dozens of mechanical keyboards.


[173 Comments](https://arstechnica.com/google/2025/10/unexpectedly-a-deer-briefly-entered-the-family-room-living-with-gemini-home/#comments "173 comments")

Staff Picks

This is why LLM driven interaction keeps having trouble escaping the chat bot. The moment it touches real life, the propensity for getting it horribly wrong more than occasionally makes it untrustworthy.

It’s not that Apple and Google are bad at AI. It’s that even the current state of the art is just not reliable enough to deal with complex ever changing real world state. And that’s worsened by making both terrifying and ridiculous mistakes that an 8 year old wouldn’t.


[Oct 31, 2025 at 12:10 PM](https://arstechnica.com/civis/posts/44065399/)

Comments


[Forum view](https://arstechnica.com/civis/threads/%E2%80%9Cunexpectedly-a-deer-briefly-entered-the-family-room%E2%80%9D-living-with-gemini-home.1510128/)

![Loading](https://cdn.arstechnica.net/wp-content/themes/ars-v9/public/images/firework-loader.75ab30.gif)
Loading comments...


[Prev story](https://arstechnica.com/space/2025/10/rocket-report-chinas-moon-rocket-to-debut-soon-arcaspace-is-back-sort-of/ "Go to: Rocket Report: SpaceX surpasses shuttle launch total; Skyroot has big ambitions")

[Next story](https://arstechnica.com/space/2025/10/as-pressure-mounts-spacex-insists-starship-is-fastest-path-to-moon-landing/ "Go to: SpaceX teases simplified Starship as alarms sound over Moon landing delays")

1. [![Listing image for first story in Most Read: Reddit is putting more limits on Old.Reddit.com](https://cdn.arstechnica.net/wp-content/uploads/2026/09/GettyImages-2227553113-1-500x500.jpg)](https://arstechnica.com/gadgets/2026/09/reddit-will-block-old-reddit-com-from-people-who-havent-used-it-in-6-months/)




1. [Reddit is putting more limits on Old.Reddit.com](https://arstechnica.com/gadgets/2026/09/reddit-will-block-old-reddit-com-from-people-who-havent-used-it-in-6-months/)

2. 2. [NASA has a Dragon dilemma, and there appear to be no good answers](https://arstechnica.com/space/2026/09/nasa-has-a-dragon-dilemma-and-there-appear-to-be-no-good-answers/)

3. 3. [Dinosaur-killing impact crater might have been teeming with life](https://arstechnica.com/science/2026/09/dinosaur-killing-impact-crater-might-have-been-teeming-with-life/)

4. 4. [Google announces Gemini 4 Argon AI model, but you can't use it yet](https://arstechnica.com/google/2026/09/google-announces-gemini-4-argon-ai-model-but-you-cant-use-it-yet/)

5. 5. [PS5 emulation is suddenly making big strides on PC](https://arstechnica.com/gaming/2026/10/ps5-emulation-is-suddenly-making-big-strides-on-pc/)


Customize

Sign in dialog...