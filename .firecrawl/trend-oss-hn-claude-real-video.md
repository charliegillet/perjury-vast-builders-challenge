|     |     |     |
| --- | --- | --- |
| |     |     |     |
| --- | --- | --- |
| [![](https://news.ycombinator.com/y18.svg)](https://news.ycombinator.com/) | **[Hacker News](https://news.ycombinator.com/news)** [new](https://news.ycombinator.com/newest) \| [past](https://news.ycombinator.com/front) \| [comments](https://news.ycombinator.com/newcomments) \| [ask](https://news.ycombinator.com/ask) \| [show](https://news.ycombinator.com/show) \| [jobs](https://news.ycombinator.com/jobs) \| [submit](https://news.ycombinator.com/submit) | [login](https://news.ycombinator.com/login?goto=item%3Fid%3D48766005) | |

| |     |     |     |
| --- | --- | --- |
|  |  | [Claude-real-video － any LLM can watch a video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) ( [github.com/huangchihhungleo](https://news.ycombinator.com/from?site=github.com/huangchihhungleo)) |
|  | 167 points by [cortexosmain](https://news.ycombinator.com/user?id=cortexosmain) [3 months ago](https://news.ycombinator.com/item?id=48766005) \| [hide](https://news.ycombinator.com/hide?id=48766005&goto=item%3Fid%3D48766005) \| [past](https://hn.algolia.com/?query=Claude-real-video%20%EF%BC%8D%20any%20LLM%20can%20watch%20a%20video&type=story&dateRange=all&sort=byDate&storyText=false&prefix&page=0) \| [favorite](https://news.ycombinator.com/fave?id=48766005&auth=80a7b5d165d5931725da35eaebcbb24fa07f6641) \| [62 comments](https://news.ycombinator.com/item?id=48766005) |
|  |  |

|     |     |     |
| --- | --- | --- |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [fzysingularity](https://news.ycombinator.com/user?id=fzysingularity) [3 months ago](https://news.ycombinator.com/item?id=48768847) \| [next](https://news.ycombinator.com/item?id=48766005#48768141)\[–\]<br>Pretty terribly expensive way to watch a video with Claude.<br>Use Gemini or some local VLM to do this way more efficiently. We spent quite a bit of time on video understanding, and Claude will just burn tokens.<br>Check out this library: [https://vlm-run.github.io/mm/](https://vlm-run.github.io/mm/)<br>You can swap models and try out different encoding methods for videos ( [https://vlm-run.github.io/mm/encoders/#video](https://vlm-run.github.io/mm/encoders/#video)) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [thisisit](https://news.ycombinator.com/user?id=thisisit) [3 months ago](https://news.ycombinator.com/item?id=48770870) \| [parent](https://news.ycombinator.com/item?id=48766005#48768847) \| [next](https://news.ycombinator.com/item?id=48766005#48771109)\[–\]<br>Exactly this. Gemini is best at this. Just give it video link - YouTube works best - and it will analyse the video. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [snthpy](https://news.ycombinator.com/user?id=snthpy) [3 months ago](https://news.ycombinator.com/item?id=48771417) \| [root](https://news.ycombinator.com/item?id=48766005#48768847) \| [parent](https://news.ycombinator.com/item?id=48766005#48770870) \| [next](https://news.ycombinator.com/item?id=48766005#48771109)\[–\]<br>Really, does this work now? What about NotebookLM? I was using it a lot until i realised it was only analysing the transcripts and not the video because i was mostly using it for technical ones with important charts. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [newswasboring](https://news.ycombinator.com/user?id=newswasboring) [89 days ago](https://news.ycombinator.com/item?id=48775690) \| [root](https://news.ycombinator.com/item?id=48766005#48768847) \| [parent](https://news.ycombinator.com/item?id=48766005#48771417) \| [next](https://news.ycombinator.com/item?id=48766005#48793176)\[–\]<br>NotebookLM still uses the transcript method I think. But Gemini is wonderful. I have been using it to analyze the youtube videos of wrestling matches (trying to build a fan website for WXM, the best pro wrestling promotion to come out of India in a while). It does move by move analysis, audience reaction based match flow tracking, isolates interesting parts of the video (big moves, botches, story beats etc). I have run some experiments to get video editing plans out of it. I think I can combine it with something like remotion skill to make highlight videos.<br>Edit: BTW, you can analyze about 8 hours a day on free tier. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [cortexosmain](https://news.ycombinator.com/user?id=cortexosmain) [88 days ago](https://news.ycombinator.com/item?id=48793176) \| [root](https://news.ycombinator.com/item?id=48766005#48768847) \| [parent](https://news.ycombinator.com/item?id=48766005#48771417) \| [prev](https://news.ycombinator.com/item?id=48766005#48775690) \| [next](https://news.ycombinator.com/item?id=48766005#48771773)\[–\]<br>NotebookLM was transcript-only when I last checked. Gemini proper does ingest video natively (samples ~1fps server-side). This tool is for everything that can't — Claude, ChatGPT web, local models — it turns the video into frames + transcript on your machine so any of them can read it. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [thisisit](https://news.ycombinator.com/user?id=thisisit) [3 months ago](https://news.ycombinator.com/item?id=48771773) \| [root](https://news.ycombinator.com/item?id=48766005#48768847) \| [parent](https://news.ycombinator.com/item?id=48766005#48771417) \| [prev](https://news.ycombinator.com/item?id=48766005#48793176) \| [next](https://news.ycombinator.com/item?id=48766005#48771109)\[–\]<br>It can tell you what’s on the screen at given point in time. My pipeline is mostly around simple questions like “does this video contain cars?” Not sure if it can spot charts on screen. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [cpnwaugha](https://news.ycombinator.com/user?id=cpnwaugha) [84 days ago](https://news.ycombinator.com/item?id=48836816) \| [root](https://news.ycombinator.com/item?id=48766005#48768847) \| [parent](https://news.ycombinator.com/item?id=48766005#48771773) \| [next](https://news.ycombinator.com/item?id=48766005#48771109)\[–\]<br>mm can spot charts on a screen. did you try it? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [n0on3](https://news.ycombinator.com/user?id=n0on3) [3 months ago](https://news.ycombinator.com/item?id=48771109) \| [parent](https://news.ycombinator.com/item?id=48766005#48768847) \| [prev](https://news.ycombinator.com/item?id=48766005#48770870) \| [next](https://news.ycombinator.com/item?id=48766005#48769615)\[–\]<br>Seems cool from the docs page, I was about to give it a shot but [https://github.com/vlm-run/mm](https://github.com/vlm-run/mm) goes 404 … | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [rancar2](https://news.ycombinator.com/user?id=rancar2) [89 days ago](https://news.ycombinator.com/item?id=48773978) \| [root](https://news.ycombinator.com/item?id=48766005#48768847) \| [parent](https://news.ycombinator.com/item?id=48766005#48771109) \| [next](https://news.ycombinator.com/item?id=48766005#48769615)\[–\]<br>It’s unclear if that’s intentional since it’s listed also under open source on the main company site: [https://www.vlm.run/open-source/mm](https://www.vlm.run/open-source/mm) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [fzysingularity](https://news.ycombinator.com/user?id=fzysingularity) [86 days ago](https://news.ycombinator.com/item?id=48806763) \| [root](https://news.ycombinator.com/item?id=48766005#48768847) \| [parent](https://news.ycombinator.com/item?id=48766005#48773978) \| [next](https://news.ycombinator.com/item?id=48766005#48769615)\[–\]<br>We were planning to open-source this soon, but jumped the gun and posted about the video encoders here since it seemed relevant.<br>In either case, here you go, it's public now: [https://github.com/vlm-run/mm](https://github.com/vlm-run/mm). | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [Tenoke](https://news.ycombinator.com/user?id=Tenoke) [3 months ago](https://news.ycombinator.com/item?id=48769615) \| [parent](https://news.ycombinator.com/item?id=48766005#48768847) \| [prev](https://news.ycombinator.com/item?id=48766005#48771109) \| [next](https://news.ycombinator.com/item?id=48766005#48769472)\[–\]<br>Do you mean that Gemini is most token-efficent at watching videos? Is that the case for e.g. just giving it a video in the browser? I admit, I dont give LLMs videos as I just assume it'll burn too many tokens. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [achatham](https://news.ycombinator.com/user?id=achatham) [3 months ago](https://news.ycombinator.com/item?id=48770721) \| [root](https://news.ycombinator.com/item?id=48766005#48768847) \| [parent](https://news.ycombinator.com/item?id=48766005#48769615) \| [next](https://news.ycombinator.com/item?id=48766005#48769472)\[–\]<br>Yes, Gemini is very token efficient at video. It also has "lower resolution" options which can make it even cheaper if. With Gemini 3.1 flash lite an hour of video works out to $0.24 at the API rates. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [mh-](https://news.ycombinator.com/user?id=mh-) [3 months ago](https://news.ycombinator.com/item?id=48769472) \| [parent](https://news.ycombinator.com/item?id=48766005#48768847) \| [prev](https://news.ycombinator.com/item?id=48766005#48769615) \| [next](https://news.ycombinator.com/item?id=48766005#48768141)\[–\]<br>Assuming that's your project, the GitHub link from the PyPi page is a 404. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [fzysingularity](https://news.ycombinator.com/user?id=fzysingularity) [86 days ago](https://news.ycombinator.com/item?id=48810019) \| [root](https://news.ycombinator.com/item?id=48766005#48768847) \| [parent](https://news.ycombinator.com/item?id=48766005#48769472) \| [next](https://news.ycombinator.com/item?id=48766005#48768141)\[–\]<br>It's live now, [https://github.com/vlm-run/mm](https://github.com/vlm-run/mm). | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [cpnwaugha](https://news.ycombinator.com/user?id=cpnwaugha) [85 days ago](https://news.ycombinator.com/item?id=48816397) \| [root](https://news.ycombinator.com/item?id=48766005#48768847) \| [parent](https://news.ycombinator.com/item?id=48766005#48810019) \| [next](https://news.ycombinator.com/item?id=48766005#48768141)\[–\]<br>Awesome! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [bonoboTP](https://news.ycombinator.com/user?id=bonoboTP) [3 months ago](https://news.ycombinator.com/item?id=48768141) \| [prev](https://news.ycombinator.com/item?id=48766005#48768847) \| [next](https://news.ycombinator.com/item?id=48766005#48769459)\[–\]<br>"Where the video goes: stays on your machine" - No, the frames (that this tool extracts) obviously get sent to Anthropic if you use Claude. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [fny](https://news.ycombinator.com/user?id=fny) [3 months ago](https://news.ycombinator.com/item?id=48769224) \| [parent](https://news.ycombinator.com/item?id=48766005#48768141) \| [next](https://news.ycombinator.com/item?id=48766005#48769459)\[–\]<br>"Or any LLM" on your machine. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [nickpeterson](https://news.ycombinator.com/user?id=nickpeterson) [3 months ago](https://news.ycombinator.com/item?id=48769459) \| [prev](https://news.ycombinator.com/item?id=48766005#48768141) \| [next](https://news.ycombinator.com/item?id=48766005#48768440)\[–\]<br>I’m currently punishing Fable by making it watch the entire series of 7th Heaven. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [chaboud](https://news.ycombinator.com/user?id=chaboud) [3 months ago](https://news.ycombinator.com/item?id=48771632) \| [parent](https://news.ycombinator.com/item?id=48766005#48769459) \| [next](https://news.ycombinator.com/item?id=48766005#48769523)\[–\]<br>It's going to make itself unavailable again. Actually... that's probably a litmus test for sentience. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [kingkawn](https://news.ycombinator.com/user?id=kingkawn) [3 months ago](https://news.ycombinator.com/item?id=48769523) \| [parent](https://news.ycombinator.com/item?id=48766005#48769459) \| [prev](https://news.ycombinator.com/item?id=48766005#48771632) \| [next](https://news.ycombinator.com/item?id=48766005#48768440)\[–\]<br>Inhumane | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [testycool](https://news.ycombinator.com/user?id=testycool) [3 months ago](https://news.ycombinator.com/item?id=48770407) \| [root](https://news.ycombinator.com/item?id=48766005#48769459) \| [parent](https://news.ycombinator.com/item?id=48766005#48769523) \| [next](https://news.ycombinator.com/item?id=48766005#48768440)\[–\]<br>Was it bad? I was too young too tell and thought it was nice. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [zitterbewegung](https://news.ycombinator.com/user?id=zitterbewegung) [3 months ago](https://news.ycombinator.com/item?id=48768440) \| [prev](https://news.ycombinator.com/item?id=48766005#48769459) \| [next](https://news.ycombinator.com/item?id=48766005#48771341)\[–\]<br>This looks cool but this should be renamed without having Claude in the name. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [walrus01](https://news.ycombinator.com/user?id=walrus01) [3 months ago](https://news.ycombinator.com/item?id=48768484) \| [parent](https://news.ycombinator.com/item?id=48766005#48768440) \| [next](https://news.ycombinator.com/item?id=48766005#48771341)\[–\]<br>llm-real-video would be a much better name | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [cortexosmain](https://news.ycombinator.com/user?id=cortexosmain) [89 days ago](https://news.ycombinator.com/item?id=48779663) \| [root](https://news.ycombinator.com/item?id=48766005#48768440) \| [parent](https://news.ycombinator.com/item?id=48766005#48768484) \| [next](https://news.ycombinator.com/item?id=48766005#48771546)\[–\]<br>Took this — pip install llm-real-video works now, same tool. Kept the original repo name so existing links don't break. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [coss](https://news.ycombinator.com/user?id=coss) [3 months ago](https://news.ycombinator.com/item?id=48771546) \| [root](https://news.ycombinator.com/item?id=48766005#48768440) \| [parent](https://news.ycombinator.com/item?id=48766005#48768484) \| [prev](https://news.ycombinator.com/item?id=48766005#48779663) \| [next](https://news.ycombinator.com/item?id=48766005#48771341)\[–\]<br>llmrv. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [fragmede](https://news.ycombinator.com/user?id=fragmede) [3 months ago](https://news.ycombinator.com/item?id=48772015) \| [root](https://news.ycombinator.com/item?id=48766005#48768440) \| [parent](https://news.ycombinator.com/item?id=48766005#48771546) \| [next](https://news.ycombinator.com/item?id=48766005#48771341)\[–\]<br>Elmerview | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [noufalibrahim](https://news.ycombinator.com/user?id=noufalibrahim) [3 months ago](https://news.ycombinator.com/item?id=48771341) \| [prev](https://news.ycombinator.com/item?id=48766005#48768440) \| [next](https://news.ycombinator.com/item?id=48766005#48767633)\[–\]<br>I was creating a scene by scene remake of a cutscene from an old DOS game. The sprite sheet had several sprites which were cycled (e.g. a horse with it's head down and up). The engine would cycle through these regularly to create some "liveliness" in the background. It was tedious and I didn't want to figure out which sprites belonged at which pixel location.<br>I recorded a video of the relevant part of the cutscene using dosbox and then split it into numbered frames using ffmpeg. Then I gave that + the spritesheet to Claude Code and asked it to figure it out and tell me which ones are at what position. I should probably have deduped it but in any case, it churned through the whole thing and got one or two out of 15 or 16 sprites right. The rest, it just dropped into random places. YMMV | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [s-macke](https://news.ycombinator.com/user?id=s-macke) [82 days ago](https://news.ycombinator.com/item?id=48858547) \| [parent](https://news.ycombinator.com/item?id=48766005#48771341) \| [next](https://news.ycombinator.com/item?id=48766005#48767633)\[–\]<br>Ask a coding agent to decode the assets. Works pretty often for such old games. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [gvkhna](https://news.ycombinator.com/user?id=gvkhna) [3 months ago](https://news.ycombinator.com/item?id=48767633) \| [prev](https://news.ycombinator.com/item?id=48766005#48771341) \| [next](https://news.ycombinator.com/item?id=48766005#48797631)\[–\]<br>Nice @OP i put together something similar as well. Incidentally I found for motion design specifically llm is not able to infer specific animations as well as it just being described very plainly and accurately what is happening and the timing.<br>One thing which sort of worked decently was actually take the frames and put them into a grid and have the agent look at the image of all of the frames together. It did surprisingly well but missed a lot of subtle details that it couldn’t see.<br>Also tried various kinds of vision embeddings, heat map of motion etc, and blur etc to show motion. But none really worked as well so I ended up just describing it until it got it. Haven’t quite found the right solution yet. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [cpnwaugha](https://news.ycombinator.com/user?id=cpnwaugha) [87 days ago](https://news.ycombinator.com/item?id=48797631) \| [prev](https://news.ycombinator.com/item?id=48766005#48767633) \| [next](https://news.ycombinator.com/item?id=48766005#48769246)\[–\]<br>The comments in this post strongly validate the need for reliable video processing and understanding with VLMs.<br>While you can use Gemini or other local VLMs, the real challenge is token efficiency, accuracy, and coverage. For example, how do you make a VLM “watch” a 2-hour or 4GB video without losing context or meaning?<br>Video transcript alone can be sufficient for basic workflows needing no visual context. But when deep contextual understanding is required, e.g., self-driving, security analysis, warehouse tracking, etc., you’ll need more advanced methods like keyframe sampling, clipping, chunking, and shots+transcript.<br>You can explore the different encoding strategies we designed for efficient video processing and understanding here: [https://vlm-run.github.io/mm/encoders/#video](https://vlm-run.github.io/mm/encoders/#video).<br>FYI, the repo is now public, and contributions are welcome. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [Lerc](https://news.ycombinator.com/user?id=Lerc) [3 months ago](https://news.ycombinator.com/item?id=48769246) \| [prev](https://news.ycombinator.com/item?id=48766005#48797631) \| [next](https://news.ycombinator.com/item?id=48766005#48767700)\[–\]<br>Are models any good at descerning motion from multiple frames?<br>For instance if I gave models multiple animations of a bouncing ball as individual frames. Would they be able to tell which bounce was the more realistic motion.<br>(Is this a potential new benchmark? maybe also variations of stair dismount) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [danbrooks](https://news.ycombinator.com/user?id=danbrooks) [3 months ago](https://news.ycombinator.com/item?id=48769381) \| [parent](https://news.ycombinator.com/item?id=48766005#48769246) \| [next](https://news.ycombinator.com/item?id=48766005#48767700)\[–\]<br>I’d imagine they could. I’d try Gemini 3.5 flash with high fps. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [ElijahLynn](https://news.ycombinator.com/user?id=ElijahLynn) [3 months ago](https://news.ycombinator.com/item?id=48767700) \| [prev](https://news.ycombinator.com/item?id=48766005#48769246) \| [next](https://news.ycombinator.com/item?id=48766005#48773342)\[–\]<br>I was just thinking about this exact use case yesterday:<br>And it's for me measuring different charged speeds at different starting battery capacities and different temperatures and I was like well. What if I just had a video camera pointing at the voltage going in and out and then I could see the battery percentage increase and I can have a temperature gun pointed at the phone as well. And I couldn't know what temperature of the phone is as well and it could just figure it all out create charts..<br>This would make reviewing different charging equipment really easy as long as you really have to do is plug it in and tell other people to do the same thing and take a video of it and beat it to the system.<br>I might very well give this a try! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [idiotsecant](https://news.ycombinator.com/user?id=idiotsecant) [3 months ago](https://news.ycombinator.com/item?id=48768739) \| [parent](https://news.ycombinator.com/item?id=48766005#48767700) \| [next](https://news.ycombinator.com/item?id=48766005#48773342)\[–\]<br>It's kind of wild how much we are abandoning basic problem solving skills in favor of just pointing an enormous stack of GPUs at it | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [siriusastrebe](https://news.ycombinator.com/user?id=siriusastrebe) [3 months ago](https://news.ycombinator.com/item?id=48768788) \| [root](https://news.ycombinator.com/item?id=48766005#48767700) \| [parent](https://news.ycombinator.com/item?id=48766005#48768739) \| [next](https://news.ycombinator.com/item?id=48766005#48773342)\[–\]<br>Identifying objects in pictures was considered an insurmountable task only a few years ago, like in the xckd comic [https://xkcd.com/1425/](https://xkcd.com/1425/) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [smallerize](https://news.ycombinator.com/user?id=smallerize) [3 months ago](https://news.ycombinator.com/item?id=48769345) \| [root](https://news.ycombinator.com/item?id=48766005#48767700) \| [parent](https://news.ycombinator.com/item?id=48766005#48768788) \| [next](https://news.ycombinator.com/item?id=48766005#48773342)\[–\]<br>In the general case, I guess. But watching gauges and dials like battery capacity only take a little work with a deterministic computer vision library. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [idiotsecant](https://news.ycombinator.com/user?id=idiotsecant) [89 days ago](https://news.ycombinator.com/item?id=48778600) \| [root](https://news.ycombinator.com/item?id=48766005#48767700) \| [parent](https://news.ycombinator.com/item?id=48766005#48769345) \| [next](https://news.ycombinator.com/item?id=48766005#48771719)\[–\]<br>Or just _using voltage pickups_ like every system that monitors battery voltage ever, or about a dozen other very simple solutions. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [mindok](https://news.ycombinator.com/user?id=mindok) [3 months ago](https://news.ycombinator.com/item?id=48771719) \| [root](https://news.ycombinator.com/item?id=48766005#48767700) \| [parent](https://news.ycombinator.com/item?id=48766005#48769345) \| [prev](https://news.ycombinator.com/item?id=48766005#48778600) \| [next](https://news.ycombinator.com/item?id=48766005#48773342)\[–\]<br>Yeah - the correct way to use an LLM in this scenario is to ask it to put write such a model. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [Frost1x](https://news.ycombinator.com/user?id=Frost1x) [3 months ago](https://news.ycombinator.com/item?id=48773342) \| [prev](https://news.ycombinator.com/item?id=48766005#48767700) \| [next](https://news.ycombinator.com/item?id=48766005#48768191)\[–\]<br>So I did this yesterday for a video analysis sample with ChatGPT and it took the video, pulled out frames, did difference tests across the frames to look for significant frames to focus on, did image recognition on each frame, and interpolated motion and action between.<br>So I’m not sure why this says ChatGPT doesn’t “see” video and reads transcripts. Obviously if the video is already labeled that’s the shortcut. But it did an impressive job describing a video I have no inclination it would have in its training data. One could argue it wasn’t “native” and had an agent orchestrator to rely on external tools to accomplish the goal… but it worked. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [frb](https://news.ycombinator.com/user?id=frb) [89 days ago](https://news.ycombinator.com/item?id=48773872) \| [parent](https://news.ycombinator.com/item?id=48766005#48773342) \| [next](https://news.ycombinator.com/item?id=48766005#48768191)\[–\]<br>Had the same experience with Claude, just somehow the entire thing felt (token) expensive. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [octember](https://news.ycombinator.com/user?id=octember) [3 months ago](https://news.ycombinator.com/item?id=48768191) \| [prev](https://news.ycombinator.com/item?id=48766005#48773342) \| [next](https://news.ycombinator.com/item?id=48766005#48767897)\[–\]<br>Cool idea, but keyframes are not videos. Motion, object permanence, are not things Claude can infer from a set of images. Nice demo though! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [fzysingularity](https://news.ycombinator.com/user?id=fzysingularity) [3 months ago](https://news.ycombinator.com/item?id=48768866) \| [parent](https://news.ycombinator.com/item?id=48766005#48768191) \| [next](https://news.ycombinator.com/item?id=48766005#48769065)\[–\]<br>Exactly! We experimented with a whole bunch of video encoding techniques for LLMs here: [https://vlm-run.github.io/mm/encoders/#video](https://vlm-run.github.io/mm/encoders/#video) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [sawjet](https://news.ycombinator.com/user?id=sawjet) [3 months ago](https://news.ycombinator.com/item?id=48769065) \| [parent](https://news.ycombinator.com/item?id=48766005#48768191) \| [prev](https://news.ycombinator.com/item?id=48766005#48768866) \| [next](https://news.ycombinator.com/item?id=48766005#48767897)\[–\]<br>I have been going through this with claude and qwenvl3:8b this week. Both are pretty decent at inferring context and analyzing contact sheets. Finding high visual interest moments with a mixture of coarse and fine keyframes. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [octember](https://news.ycombinator.com/user?id=octember) [89 days ago](https://news.ycombinator.com/item?id=48775045) \| [root](https://news.ycombinator.com/item?id=48766005#48768191) \| [parent](https://news.ycombinator.com/item?id=48766005#48769065) \| [next](https://news.ycombinator.com/item?id=48766005#48767897)\[–\]<br>Might be time to check gemma :) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [BeetleB](https://news.ycombinator.com/user?id=BeetleB) [3 months ago](https://news.ycombinator.com/item?id=48767897) \| [prev](https://news.ycombinator.com/item?id=48766005#48768191) \| [next](https://news.ycombinator.com/item?id=48766005#48771478)\[–\]<br>I think this is much more useful than just LLM related applications. I'd suggest renaming it to not make it seem like it's LLM related. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [dingody](https://news.ycombinator.com/user?id=dingody) [3 months ago](https://news.ycombinator.com/item?id=48771478) \| [prev](https://news.ycombinator.com/item?id=48766005#48767897) \| [next](https://news.ycombinator.com/item?id=48766005#48774163)\[–\]<br>Based on my tests, a frame rate of 2fps is generally sufficient to resolve video content very well. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [nickvec](https://news.ycombinator.com/user?id=nickvec) [3 months ago](https://news.ycombinator.com/item?id=48769344) \| [prev](https://news.ycombinator.com/item?id=48766005#48774163) \| [next](https://news.ycombinator.com/item?id=48766005#48767781)\[–\]<br>Curious as to how many tokens are used per second of video. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [fred123123](https://news.ycombinator.com/user?id=fred123123) [3 months ago](https://news.ycombinator.com/item?id=48767781) \| [prev](https://news.ycombinator.com/item?id=48766005#48769344) \| [next](https://news.ycombinator.com/item?id=48766005#48771060)\[–\]<br>How do you handle things like scrolling quickly in a video? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [virajk\_31](https://news.ycombinator.com/user?id=virajk_31) [3 months ago](https://news.ycombinator.com/item?id=48771060) \| [prev](https://news.ycombinator.com/item?id=48766005#48767781) \| [next](https://news.ycombinator.com/item?id=48766005#48774637)\[–\]<br>So this work basically by dividing into frames.. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [high\_byte](https://news.ycombinator.com/user?id=high_byte) [89 days ago](https://news.ycombinator.com/item?id=48774637) \| [prev](https://news.ycombinator.com/item?id=48766005#48771060) \| [next](https://news.ycombinator.com/item?id=48766005#48774417)\[–\]<br>my experience with ffmpeg scene detection is that it's flaky. it works, sometimes, but not reliable by any means | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [kraflio](https://news.ycombinator.com/user?id=kraflio) [89 days ago](https://news.ycombinator.com/item?id=48774417) \| [prev](https://news.ycombinator.com/item?id=48766005#48774637) \| [next](https://news.ycombinator.com/item?id=48766005#48774384)\[–\]<br>Interesting, but how expensive does it get? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [speedgeek](https://news.ycombinator.com/user?id=speedgeek) [89 days ago](https://news.ycombinator.com/item?id=48774384) \| [prev](https://news.ycombinator.com/item?id=48766005#48774417) \| [next](https://news.ycombinator.com/item?id=48766005#48774375)\[–\]<br>So Claude is a murderbot? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [speedgeek](https://news.ycombinator.com/user?id=speedgeek) [89 days ago](https://news.ycombinator.com/item?id=48774375) \| [prev](https://news.ycombinator.com/item?id=48766005#48774384) \| [next](https://news.ycombinator.com/item?id=48766005#48772992)\[–\]<br>So Claude is a murderbot? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [wesleywt](https://news.ycombinator.com/user?id=wesleywt) [3 months ago](https://news.ycombinator.com/item?id=48772992) \| [prev](https://news.ycombinator.com/item?id=48766005#48774375) \| [next](https://news.ycombinator.com/item?id=48766005#48773723)\[–\]<br>Gemini does read videos. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [Jeff9James](https://news.ycombinator.com/user?id=Jeff9James) [89 days ago](https://news.ycombinator.com/item?id=48773723) \| [prev](https://news.ycombinator.com/item?id=48766005#48772992) \| [next](https://news.ycombinator.com/item?id=48766005#48767982)\[–\]<br>better off using a cloud solution. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [nxtfari](https://news.ycombinator.com/user?id=nxtfari) [3 months ago](https://news.ycombinator.com/item?id=48767982) \| [prev](https://news.ycombinator.com/item?id=48766005#48773723) \| [next](https://news.ycombinator.com/item?id=48766005#48766006)\[–\]<br>this is really clever, props | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [cortexosmain](https://news.ycombinator.com/user?id=cortexosmain) [3 months ago](https://news.ycombinator.com/item?id=48766006) \| [prev](https://news.ycombinator.com/item?id=48766005#48767982) \| [next](https://news.ycombinator.com/item?id=48766005#48771406)\[–\]<br>Hi HN! I built this because I was frustrated that no LLM actually "sees" a video — Claude won't accept video files, ChatGPT reads the transcript only, and Gemini samples at a fixed 1fps (missing fast cuts, over-sampling static slides).<br>claude-real-video takes a URL or local file and:<br>1\. Extracts frames at every scene change (not fixed intervals) + a density floor<br>2\. Deduplicates with a sliding-window pixel-diff algorithm (so A-B-A interview cutaways don't re-send the same shot)<br>3\. Transcribes audio (prefers embedded subtitles, falls back to Whisper)<br>4\. Optionally keeps the full soundtrack for audio-capable models<br>5\. Writes a clean MANIFEST.txt you can drop into any LLM chat<br>A 10-min presentation goes from ~600 fixed-interval frames to 5-15 meaningful keyframes. 90%+ token savings with better comprehension.<br>The dedup approach (v0.2.0) uses real pixel difference on 16x16 RGB thumbnails against a sliding window of the last N kept frames — inspired by videostil's pixelmatch, but simpler and self-contained.<br>\`--report\` generates a self-contained HTML showing every keep/drop decision with diff percentages, so you can tune the threshold visually.<br>pip install claude-real-video && crv " [https://youtube.com/watch?v=](https://youtube.com/watch?v=)..." --report<br>MIT licensed, pure Python + ffmpeg. Happy to answer questions! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [garciasn](https://news.ycombinator.com/user?id=garciasn) [3 months ago](https://news.ycombinator.com/item?id=48767939) \| [parent](https://news.ycombinator.com/item?id=48766005#48766006) \| [next](https://news.ycombinator.com/item?id=48766005#48767875)\[–\]<br>I gave Claude a video provided by a county attorney for a speeding ticket I got. It was spot on in its analysis, even though I don’t like what the video showed.<br>What does it mean that Claude can’t view video; it did it just fine. Or do you mean tool less? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [torhorway](https://news.ycombinator.com/user?id=torhorway) [3 months ago](https://news.ycombinator.com/item?id=48768150) \| [root](https://news.ycombinator.com/item?id=48766005#48766006) \| [parent](https://news.ycombinator.com/item?id=48766005#48767939) \| [next](https://news.ycombinator.com/item?id=48766005#48767875)\[–\]<br>yeah im pretty sure claude code can handle videos. its been doing frame by frame analysis for me with generated video to iterate on pipelines | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [AmazingEveryDay](https://news.ycombinator.com/user?id=AmazingEveryDay) [3 months ago](https://news.ycombinator.com/item?id=48767875) \| [parent](https://news.ycombinator.com/item?id=48766005#48766006) \| [prev](https://news.ycombinator.com/item?id=48766005#48767939) \| [next](https://news.ycombinator.com/item?id=48766005#48767458)\[–\]<br>I think a more or less clunky name like 'llm video preprocessor' would be better description? In any case seems like a you came up with a good project idea. I wonder how long until the sota models will just have this kind of functionallity built in. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [ProofHouse](https://news.ycombinator.com/user?id=ProofHouse) [3 months ago](https://news.ycombinator.com/item?id=48767458) \| [parent](https://news.ycombinator.com/item?id=48766005#48766006) \| [prev](https://news.ycombinator.com/item?id=48766005#48767875) \| [next](https://news.ycombinator.com/item?id=48766005#48771406)\[–\]<br>Very cool I have something that does this as well along these lines. I’ll dig into yours over the next few days and contribute where and if I can too, awesome to see! | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [cortexosmain](https://news.ycombinator.com/user?id=cortexosmain) [86 days ago](https://news.ycombinator.com/item?id=48811107) \| [root](https://news.ycombinator.com/item?id=48766005#48766006) \| [parent](https://news.ycombinator.com/item?id=48766005#48767458) \| [next](https://news.ycombinator.com/item?id=48766005#48771406)\[–\]<br>Would love that — issues are open and the codebase is small enough to read in one sitting. The areas I'd most welcome help on right now are additional transcript backends and smarter grid packing. | | |
| ![](https://news.ycombinator.com/s.gif)

|     |
| --- |
|  |

[Guidelines](https://news.ycombinator.com/newsguidelines.html) \| [FAQ](https://news.ycombinator.com/newsfaq.html) \| [Lists](https://news.ycombinator.com/lists) \| [API](https://github.com/HackerNews/API) \| [Security](https://news.ycombinator.com/security.html) \| [Legal](https://www.ycombinator.com/legal/) \| [Apply to YC](https://www.ycombinator.com/apply/) \| [Contact](mailto:hn@ycombinator.com)

Search: |