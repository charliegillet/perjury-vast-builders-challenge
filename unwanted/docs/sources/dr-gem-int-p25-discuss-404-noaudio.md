[Skip to last reply](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805/3) [Skip to top](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805/1)

[Skip to main content](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805#main-container)

# Build with Google AI Forum

[Read the community guidelines\\
_arrow\_forward_](https://discuss.ai.google.dev/faq) [Browse topics by tag\\
_arrow\_forward_](https://discuss.ai.google.dev/tags)

​


Hi Everyone,

Starting June 19, 2026, the Gemini API will stop accepting requests from unrestricted API keys to prevent unauthorized usage and billing risks.

If your Google Cloud project has the Gemini API enabled and contains unrestricted keys, please restrict them immediately.

### [Heading link](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805\#p-311902-what-to-do-1) What to do:

- Option 1 (Restrict existing keys): Go to [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials), select your key, and under API restrictions, restrict it to Gemini API ( [generativelanguage.googleapis.com](http://generativelanguage.googleapis.com/)).
- Option 2 (New keys): Generate new restricted keys in [Google AI Studio](https://aistudio.google.com/app/apikey) and update your code.

Note: Keys generated directly in AI Studio are restricted to the Gemini API by default.

# [Gemini 3 error 404 NOT\_FOUND with videos without an audio stream and media resolution not set to high](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805)

[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4)

- [bug](https://discuss.ai.google.dev/tag/bug/7),
- [video](https://discuss.ai.google.dev/tag/video/410)

You have selected **0** posts.

[select all](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805)

[cancel selecting](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805)

[Jan 1](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805/1 "Jump to the first post")

1 / 2


Jan 1


[Jan 9](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805/3)

## post by Sahan\_Reddy on Jan 1

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/sahan_reddy/48/80245_2.png)](https://discuss.ai.google.dev/u/sahan_reddy)

[Sahan\_Reddy](https://discuss.ai.google.dev/u/sahan_reddy)

1

[Jan 1](https://discuss.ai.google.dev/t/gemini-3-error-404-not-found-with-videos-without-an-audio-stream-and-media-resolution-not-set-to-high/113805 "Post date")

It seems like when passing videos without an audio stream to Gemini 3 models, it fails unless MEDIA\_RESOLUTION\_HIGH is set. Videos with an audio stream work in all cases, and Gemini 2.5 doesn’t seem to have this issue. Minimal repro below:

```python

import os
import subprocess
import time
from pathlib import Path

import google.genai as genai
import google.genai.types as genai_types

VIDEO_URL = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4" # video with no audio stream
VIDEO_PATH_NO_AUDIO = Path.cwd() / "noaudio.mp4"
VIDEO_PATH_AUDIO = Path.cwd() / "withaudio.mp4"
if not VIDEO_PATH_NO_AUDIO.exists():
    subprocess.run(["curl", "-L", "-o", str(VIDEO_PATH_NO_AUDIO), VIDEO_URL], check=True)
if not VIDEO_PATH_AUDIO.exists():
    subprocess.run([\
        "ffmpeg", "-i", str(VIDEO_PATH_NO_AUDIO),\
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",\
        "-c:v", "copy", "-c:a", "aac", "-shortest",\
        str(VIDEO_PATH_AUDIO)\
    ], check=True) # make video with an audio stream

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"],
    http_options=genai_types.HttpOptions(api_version="v1beta", timeout=600_000),
)
def test_video(video_path: Path, model: str, media_resolution: str | None):
    print(f"=== Testing {video_path.name} with {model} and resolution {media_resolution}")
    uploaded = client.files.upload(file=video_path)
    while uploaded.state != genai_types.FileState.ACTIVE:
        time.sleep(2)
        assert uploaded.name
        uploaded = client.files.get(name=uploaded.name)
    try:
        response = client.models.generate_content(
            model=model,
            contents=[{\
                "role": "user",\
                "parts": [\
                    {"file_data": {"file_uri": uploaded.uri, "mime_type": uploaded.mime_type}},\
                    {"text": "What is happening in this video?"},\
                ],\
            }],
            config={
                "media_resolution": media_resolution,
            } # type: ignore
        )
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {str(e)}")
    print()

test_video(VIDEO_PATH_AUDIO, "gemini-3-flash-preview", None) # success
test_video(VIDEO_PATH_NO_AUDIO, "gemini-3-flash-preview", None) # Error: 404 NOT_FOUND
test_video(VIDEO_PATH_NO_AUDIO, "gemini-3-flash-preview", "MEDIA_RESOLUTION_HIGH") # success
test_video(VIDEO_PATH_NO_AUDIO, "gemini-2.5-flash", None) # success
```

And my output from a run of that:

```csharp

=== Testing withaudio.mp4 with gemini-3-flash-preview and resolution None
Response: A rabbit comes out of its burrow in a green forest and starts cleaning its ears and fur.

=== Testing noaudio.mp4 with gemini-3-flash-preview and resolution None
Error: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'Requested entity was not found.', 'status': 'NOT_FOUND'}}

=== Testing noaudio.mp4 with gemini-3-flash-preview and resolution MEDIA_RESOLUTION_HIGH
Response: In this video, a rabbit emerges from its burrow beneath a large tree in a sun-drenched forest clearing.

Initially, the rabbit is seen peeking its head out from the dark entrance of the burrow. It then cautiously steps out onto the lush, green grass surrounding the base of the tree. After taking a moment to look around, the rabbit begins to hop away across the grassy mound and further into the forest.

=== Testing noaudio.mp4 with gemini-2.5-flash and resolution None
Response: The video displays a serene and vibrant animated forest scene.

In the foreground, a lush green, moss-covered hillock features a large tree with prominent, gnarled roots. At the base of the tree, a dark opening suggests a cave or burrow entrance. The hillock is surrounded by vibrant green grass, with a few scattered rocks visible. Tall, verdant trees form a dense background, creating a rich woodland atmosphere.

The primary action in the video is the subtle, gradual shift of sunlight filtering through the leaves and across the grassy terrain. This movement creates dynamic patterns of light and shadow that slowly evolve over the short clip, suggesting the gentle passage of time in the forest. Small purple or red specks, possibly berries or tiny flowers, also appear and subtly shift position on the mossy mound, further enhancing the sense of a living environment. The camera remains mostly static throughout the clip.
```

Me too

188
views
1
link


Summarize

## post by Sonali\_Kumari1 on Jan 9

Reply

### Related topics

| Topic | Replies | Views | Activity |
| --- | --- | --- | --- |
| [404 Error When Uploading Video, Audio, and PDF Files to Gemini API for Moderation](https://discuss.ai.google.dev/t/404-error-when-uploading-video-audio-and-pdf-files-to-gemini-api-for-moderation/42335)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [models](https://discuss.ai.google.dev/tag/models/20),<br>- [api](https://discuss.ai.google.dev/tag/api/8),<br>- [gemini-15](https://discuss.ai.google.dev/tag/gemini-15/1) | [1](https://discuss.ai.google.dev/t/404-error-when-uploading-video-audio-and-pdf-files-to-gemini-api-for-moderation/42335/1) | 381 | [Oct 2024](https://discuss.ai.google.dev/t/404-error-when-uploading-video-audio-and-pdf-files-to-gemini-api-for-moderation/42335/2) |
| [Repeated image-to-video audio failures on Veo 3.1 Lite and Fast](https://discuss.ai.google.dev/t/repeated-image-to-video-audio-failures-on-veo-3-1-lite-and-fast/184792)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [audio](https://discuss.ai.google.dev/tag/audio/378) | [1](https://discuss.ai.google.dev/t/repeated-image-to-video-audio-failures-on-veo-3-1-lite-and-fast/184792/1) | 34 | [3d](https://discuss.ai.google.dev/t/repeated-image-to-video-audio-failures-on-veo-3-1-lite-and-fast/184792/2) |
| [Gemini Developer API generateContent returns 404 although models.list reports gemini-2.5-flash with generateContent support](https://discuss.ai.google.dev/t/gemini-developer-api-generatecontent-returns-404-although-models-list-reports-gemini-2-5-flash-with-generatecontent-support/179730)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [api](https://discuss.ai.google.dev/tag/api/8) | [1](https://discuss.ai.google.dev/t/gemini-developer-api-generatecontent-returns-404-although-models-list-reports-gemini-2-5-flash-with-generatecontent-support/179730/1) | 350 | [Aug 26](https://discuss.ai.google.dev/t/gemini-developer-api-generatecontent-returns-404-although-models-list-reports-gemini-2-5-flash-with-generatecontent-support/179730/2) |
| [mediaResolution ‘low’ returns an error](https://discuss.ai.google.dev/t/mediaresolution-low-returns-an-error/83408)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [api](https://discuss.ai.google.dev/tag/api/8),<br>- [video](https://discuss.ai.google.dev/tag/video/410) | [4](https://discuss.ai.google.dev/t/mediaresolution-low-returns-an-error/83408/1) | 494 | [Jun 2025](https://discuss.ai.google.dev/t/mediaresolution-low-returns-an-error/83408/8) |
| [Gemini-2.5-flash api cannot process video input](https://discuss.ai.google.dev/t/gemini-2-5-flash-api-cannot-process-video-input/80093)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [gemini-flash](https://discuss.ai.google.dev/tag/gemini-flash/391),<br>- [video](https://discuss.ai.google.dev/tag/video/410) | [19](https://discuss.ai.google.dev/t/gemini-2-5-flash-api-cannot-process-video-input/80093/1) | 1.7k | [Dec 2025](https://discuss.ai.google.dev/t/gemini-2-5-flash-api-cannot-process-video-input/80093/30) |

Topic list, column headers with buttons are sortable.