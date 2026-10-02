[Skip to main content](https://discuss.ai.google.dev/t/gemini-silently-failing-if-audio-cant-be-extracted-from-video-container/129898#main-container)

# Build with Google AI Forum

[Read the community guidelines\\
_arrow\_forward_](https://discuss.ai.google.dev/faq) [Browse topics by tag\\
_arrow\_forward_](https://discuss.ai.google.dev/tags)

​


Hi Everyone,

Starting June 19, 2026, the Gemini API will stop accepting requests from unrestricted API keys to prevent unauthorized usage and billing risks.

If your Google Cloud project has the Gemini API enabled and contains unrestricted keys, please restrict them immediately.

### [Heading link](https://discuss.ai.google.dev/t/gemini-silently-failing-if-audio-cant-be-extracted-from-video-container/129898\#p-311902-what-to-do-1) What to do:

- Option 1 (Restrict existing keys): Go to [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials), select your key, and under API restrictions, restrict it to Gemini API ( [generativelanguage.googleapis.com](http://generativelanguage.googleapis.com/)).
- Option 2 (New keys): Generate new restricted keys in [Google AI Studio](https://aistudio.google.com/app/apikey) and update your code.

Note: Keys generated directly in AI Studio are restricted to the Gemini API by default.

# [Gemini silently “failing” if audio can’t be extracted from video container](https://discuss.ai.google.dev/t/gemini-silently-failing-if-audio-cant-be-extracted-from-video-container/129898)

[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4)

- [bug](https://discuss.ai.google.dev/tag/bug/7),
- [gemini](https://discuss.ai.google.dev/tag/gemini/44),
- [audio](https://discuss.ai.google.dev/tag/audio/378)

You have selected **0** posts.

[select all](https://discuss.ai.google.dev/t/gemini-silently-failing-if-audio-cant-be-extracted-from-video-container/129898)

[cancel selecting](https://discuss.ai.google.dev/t/gemini-silently-failing-if-audio-cant-be-extracted-from-video-container/129898)

## post by lbux on Mar 9

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/lbux/48/101936_2.png)](https://discuss.ai.google.dev/u/lbux)

[lbux](https://discuss.ai.google.dev/u/lbux)

1

[Mar 9](https://discuss.ai.google.dev/t/gemini-silently-failing-if-audio-cant-be-extracted-from-video-container/129898 "Post date")

CREMA-D has several videos in an .flv container. Gemini 2.5 Flash Lite supports both x-flv and .mp3 codecs which are inside the container. If I strip out the video and audio data individually, Gemini is able to ingest both files. However, if pass in the .flv file without any modification, it can ingest the video but it says there is no audio.

Maybe it is controversial to say this is a “failure” but if a video has an audio track and Gemini can not read it, should we not get some type of warning or error?

Me too

59
views


Summarize

Reply

### Related topics

| Topic | Replies | Views | Activity |
| --- | --- | --- | --- |
| [Audio Bug by Priority PayGo Mode](https://discuss.ai.google.dev/t/audio-bug-by-priority-paygo-mode/132335)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [models](https://discuss.ai.google.dev/tag/models/20),<br>- [gemini](https://discuss.ai.google.dev/tag/gemini/44) | [0](https://discuss.ai.google.dev/t/audio-bug-by-priority-paygo-mode/132335/1) | 41 | [Mar 14](https://discuss.ai.google.dev/t/audio-bug-by-priority-paygo-mode/132335/1) |
| [Gemini 2.5 Flash doesn’t have audio processing capability, but why?](https://discuss.ai.google.dev/t/gemini-2-5-flash-doesnt-have-audio-processing-capability-but-why/86520)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [ui](https://discuss.ai.google.dev/tag/ui/425),<br>- [gemini-flash-2-5](https://discuss.ai.google.dev/tag/gemini-flash-2-5/432) | [3](https://discuss.ai.google.dev/t/gemini-2-5-flash-doesnt-have-audio-processing-capability-but-why/86520/1) | 609 | [Jun 2025](https://discuss.ai.google.dev/t/gemini-2-5-flash-doesnt-have-audio-processing-capability-but-why/86520/6) |
| [Gemini-3-flash-preview not returning prompt audio tokens in usage metadata when given a video file with an audio track](https://discuss.ai.google.dev/t/gemini-3-flash-preview-not-returning-prompt-audio-tokens-in-usage-metadata-when-given-a-video-file-with-an-audio-track/113807)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [bug](https://discuss.ai.google.dev/tag/bug/7),<br>- [audio](https://discuss.ai.google.dev/tag/audio/378) | [4](https://discuss.ai.google.dev/t/gemini-3-flash-preview-not-returning-prompt-audio-tokens-in-usage-metadata-when-given-a-video-file-with-an-audio-track/113807/1) | 203 | [Jan 8](https://discuss.ai.google.dev/t/gemini-3-flash-preview-not-returning-prompt-audio-tokens-in-usage-metadata-when-given-a-video-file-with-an-audio-track/113807/8) |
| [\[BUG\] gemini-3.1-flash-lite returns 500 Internal Error for any audio input](https://discuss.ai.google.dev/t/bug-gemini-3-1-flash-lite-returns-500-internal-error-for-any-audio-input/168516)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [audio](https://discuss.ai.google.dev/tag/audio/378) | [1](https://discuss.ai.google.dev/t/bug-gemini-3-1-flash-lite-returns-500-internal-error-for-any-audio-input/168516/1) | 117 | [Jun 4](https://discuss.ai.google.dev/t/bug-gemini-3-1-flash-lite-returns-500-internal-error-for-any-audio-input/168516/2) |
| [Gemini 3 error 404 NOT\_FOUND with videos without an audio stream and media resolution not set to high](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [bug](https://discuss.ai.google.dev/tag/bug/7),<br>- [video](https://discuss.ai.google.dev/tag/video/410) | [1](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805/1) | 188 | [Jan 9](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805/3) |

Topic list, column headers with buttons are sortable.