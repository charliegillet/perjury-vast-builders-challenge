The Gemini documentation is clear:

> The File API service extracts image frames from videos at 1 frame per second (FPS) and audio at 1Kbps, single channel, adding timestamps every second. These rates are subject to change in the future for improvements in inference.
>
> Note: The details of fast action sequences may be lost at the 1 FPS frame sampling rate. Consider slowing down high-speed clips for improved inference quality.
>
> Individual frames are 258 tokens, and audio is 32 tokens per second. With metadata, each second of video becomes ~300 tokens, which means a 1M context window can fit slightly less than an hour of video.
>
> To ask questions about time-stamped locations, use the format MM:SS, where the first two digits represent minutes and the last two digits represent seconds.

But on this [ThursdAI episode: Oct 17 - Robots, Rockets, and Multi Modal Mania…](https://sub.thursdai.news/p/thursdai-oct-17-robots-rockets-and), at 1:00:50, [Hrishi](https://x.com/hrishioa/) says

> I don’t think it’s a series of images anymore because when I talk to the model and try to get some concept of what it’s perceiving, it’s no longer a series of images.

If that’s the case, it’s a **huge** change. So I tested it with this video.

Video of numbers refreshing at 4 frames per second - YouTube

Tap to unmute

[Video of numbers refreshing at 4 frames per second](https://www.youtube.com/watch?v=Dv8KON7WQYA) [Anand S](https://www.youtube.com/channel/UCBOUVZF7VkeXzGaQ89CxiTQ)

![thumbnail-image](https://yt3.ggpht.com/ytc/AIdro_lNWPx_LcRHxXSnD2diCwmipPxjip-H5Z3G6YVLcJ3KusU=s68-c-k-c0x00ffffff-no-rj)

Anand S1.02K subscribers

This video has 20 numbers refreshing at 4 frames per second.

When I upload it to [AI Studio](https://aistudio.google.com/), it takes 1,316 tokens. This is close enough to 258 tokens per image (no audio). So I’m partly convinced that Gemini still processing videos at 1 frame per second.

Then, I asked it to `Extract all numbers in the video` using Gemini 1.5 Flash 002 as well as Gemini 1.5 Flash 8b. In both cases, the results were: 2018, 85, 47, 37, 38.

These are frames 2, 6, 10, 14, 18 (out of 20). So, **clearly** Gemini is still sampling at about 1 frame per second, starting somewhere between 0.25 or 0.5 seconds.

## Related

- [Screen Scraping with Gemini Using Video](https://www.s-anand.net/blog/screen-scraping-with-gemini-using-video/) Sat, 9 Nov 2024
  Cheap video understanding turns screen recordings into a practical scraping medium, shifting the bottleneck from cost to imagination about what to extract.

- [How to direct a data movie](https://www.s-anand.net/blog/how-to-direct-a-data-movie/) Sun, 7 Feb 2021
  Making a short data movie requires the same essentials as filmmaking—theme, hypothesis, screenplay, visuals, timing, and post-production—even when the tools are PowerPoint and iMovie.

- [LLM Deprecations and Price Changes](https://www.s-anand.net/blog/llm-deprecations-and-price-changes/) Thu, 21 May 2026
  I examine how Gemini, GPT, and Claude model prices change as capabilities improve, why deprecations can raise costs and latency, and how routing and completed-task benchmarks help enterprises adapt.

- [Things I Learned - 27 Sep 2026](https://www.s-anand.net/blog/things-i-learned-27-sep-2026/) Sun, 27 Sep 2026
  I share what I learned this week about extracting web pages with Trafilatura, exposing my laptop to ChatGPT, using voice mode as a tour guide, and easing LLM fatigue, plus corrections to six mistakes.

- [AI video compression](https://www.s-anand.net/blog/ai-video-compression/) Sat, 28 Feb 2026
  I used ChatGPT and Claude to test ffmpeg compression settings for a WEBM screencast, reducing it from 912KB to a visually acceptable 23KB with AV1, lower frame rates, and higher CRF.


[Go to Top (Alt + G)](https://www.s-anand.net/blog/how-does-gemini-process-videos/#top "Go to Top (Alt + G)")