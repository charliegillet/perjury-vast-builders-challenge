[Skip to content](https://github.com/googleapis/python-genai/issues/854#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/googleapis/python-genai/issues/854) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/googleapis/python-genai/issues/854) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/googleapis/python-genai/issues/854) to refresh your session.Dismiss alert

{{ message }}

[googleapis](https://github.com/googleapis)/ **[python-genai](https://github.com/googleapis/python-genai)** Public

- [Notifications](https://github.com/login?return_to=%2Fgoogleapis%2Fpython-genai) You must be signed in to change notification settings
- [Fork\\
1k](https://github.com/login?return_to=%2Fgoogleapis%2Fpython-genai)
- [Star\\
4k](https://github.com/login?return_to=%2Fgoogleapis%2Fpython-genai)


# Any generation request with `video_metadata` results in a 500 error\#854

[New issue](https://github.com/login?return_to=https://github.com/googleapis/python-genai/issues/854)

Copy link

[New issue](https://github.com/login?return_to=https://github.com/googleapis/python-genai/issues/854)

Copy link

Closed as not planned

Closed as not planned

[Any generation request with `video_metadata` results in a 500 error](https://github.com/googleapis/python-genai/issues/854#top)#854

Copy link

Assignees

[![janasangeetha](https://avatars.githubusercontent.com/u/180526454?s=64&u=275a3828bb309d0db30d7136785c6abf45045497&v=4)](https://github.com/janasangeetha)

Labels

[api: gemini-api](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22api%3A%20gemini-api%22) [priority: p2Moderately-important priority. Fix may not be included in next release.](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22priority%3A%20p2%22) Moderately-important priority. Fix may not be included in next release. [status:awaiting user response](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22status%3Aawaiting%20user%20response%22) [status:stale](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22status%3Astale%22) [type: bugError or flaw in code with unintended results or allowing sub-optimal usage patterns.](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22type%3A%20bug%22) Error or flaw in code with unintended results or allowing sub-optimal usage patterns.

## Description

[![@kfajdsl](https://avatars.githubusercontent.com/u/38165247?u=ccfeec5ff6628f7efe66c7fff30f74808cc64b77&v=4&size=48)](https://github.com/kfajdsl)

[kfajdsl](https://github.com/kfajdsl)

opened [on May 23, 2025on May 23, 2025](https://github.com/googleapis/python-genai/issues/854#issue-3087740614)

Last edited by kfajdsl

Issue body actions

#### Environment details

- Programming language: Python (also tested with REST API)
- OS: macOS
- Language runtime version: 3.12.9
- Package version: 1.16.1

#### Steps to reproduce

1. Run the following script:

```
from google import genai
from google.genai import types
from pathlib import Path
import os

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

video_path = Path("vid.mp4")
video_bytes = video_path.read_bytes()

response = client.models.generate_content(
    model='models/gemini-2.5-flash-preview-05-20',
    contents=types.Content(
        parts=[\
            types.Part(\
                inline_data=types.Blob(\
                    data=video_bytes,\
                    mime_type='video/mp4',\
                ),\
                video_metadata=types.VideoMetadata(\
                    fps=5\
                )\
            ),\
            types.Part(text='Please summarize the video in 3 sentences.')\
        ]
    )
)
```

This also happens with start\_offset and end\_offset.

Also, note, the [docs page](https://ai.google.dev/gemini-api/docs/video-understanding#custom-frame-rate) seems wrong. It has the following:

```
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4',
                    video_metadata=types.VideoMetadata(fps=5)
            )),
```

This fails with a Pydantic error when run, and according to the API reference and other examples, `video_metadata` is a member of `Part`, not `Blob`.

## Activity

[![](https://avatars.githubusercontent.com/u/38165247?s=64&u=ccfeec5ff6628f7efe66c7fff30f74808cc64b77&v=4)kfajdsl](https://github.com/kfajdsl)

added

[type: bugError or flaw in code with unintended results or allowing sub-optimal usage patterns.](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22type%3A%20bug%22) Error or flaw in code with unintended results or allowing sub-optimal usage patterns.

[priority: p2Moderately-important priority. Fix may not be included in next release.](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22priority%3A%20p2%22) Moderately-important priority. Fix may not be included in next release.

[on May 23, 2025on May 23, 2025](https://github.com/googleapis/python-genai/issues/854#event-17797461862)

### Madhuvod commented on May 26, 2025on May 26, 2025

[![@Madhuvod](https://avatars.githubusercontent.com/u/124294538?u=e5e23d01d13dd9ab9a56097eddbbc50364f21113&v=4&size=48)](https://github.com/Madhuvod)

[Madhuvod](https://github.com/Madhuvod)

[on May 26, 2025on May 26, 2025](https://github.com/googleapis/python-genai/issues/854#issuecomment-2908780711)

More actions

i think this is a sdk issue no. i have been getting the same errror - 400 INVALID\_ARGUMENT. {'error': {'code': 400, 'message': '\* GenerateContentRequest.contents\[1\].parts: contents.parts must not be empty.\\n', 'status': 'INVALID\_ARGUMENT'}}

MOS Log: Error type: ClientError ; for the code: `gemini_api_response = gemini_client.models.generate_content( model=GEMINI_MODEL_NAME, contents=[ AUDIO_ONLY_SYSTEM_PROMPT, types.Part.from_bytes(data=audio_data, mime_type=mime_type) ], config={ "response_mime_type": "application/json", "response_schema": GeminiMOSResponse, } )` ; but the same thing works for google-genai 1.15.0

### kfajdsl commented on May 26, 2025on May 26, 2025

[![@kfajdsl](https://avatars.githubusercontent.com/u/38165247?u=ccfeec5ff6628f7efe66c7fff30f74808cc64b77&v=4&size=48)](https://github.com/kfajdsl)

[kfajdsl](https://github.com/kfajdsl)

[on May 26, 2025on May 26, 2025](https://github.com/googleapis/python-genai/issues/854#issuecomment-2910358430)

Last edited by kfajdsl

Author

More actions

[@Madhuvod](https://github.com/Madhuvod) I believe my particular issue is an api issue since I have the same issue when calling the REST API directly rather than using the Python SDK.

### Jumaron commented on May 27, 2025on May 27, 2025

[![@Jumaron](https://avatars.githubusercontent.com/u/41344875?u=14967c0b9332fb88618d61e5d2367d272a3d8205&v=4&size=48)](https://github.com/Jumaron)

[Jumaron](https://github.com/Jumaron)

[on May 27, 2025on May 27, 2025](https://github.com/googleapis/python-genai/issues/854#issuecomment-2911224104)

More actions

Same Issue, looks like an API Issue.

### kiransair commented on May 27, 2025on May 27, 2025

[![@kiransair](https://avatars.githubusercontent.com/u/106319630?v=4&size=48)](https://github.com/kiransair)

[kiransair](https://github.com/kiransair)

[on May 27, 2025on May 27, 2025](https://github.com/googleapis/python-genai/issues/854#issuecomment-2911722100)

More actions

Hi [@kfajdsl](https://github.com/kfajdsl), Thanks for reporting this issue. While trying to reproduce the error it seems the issue is with `gemini-2.5-flash-preview-05-20` but works fine with `gemini-2.0-flash`. Will bring this issue to the engineering team's attention. Please refer to this [gist](https://gist.github.com/kiransair/9c0ea7a98e0eb9a7e7a2d3c07620f025). Thank You

[![](https://avatars.githubusercontent.com/u/4653660?s=64&u=50d6f9d69e409ffd5615c1359fc1a55f96fed2fe&v=4)hkt74](https://github.com/hkt74)

added

[api: gemini-api](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22api%3A%20gemini-api%22)

[on May 27, 2025on May 27, 2025](https://github.com/googleapis/python-genai/issues/854#event-17841775769)

### hkt74 commented on May 28, 2025on May 28, 2025

[![@hkt74](https://avatars.githubusercontent.com/u/4653660?u=50d6f9d69e409ffd5615c1359fc1a55f96fed2fe&v=4&size=48)](https://github.com/hkt74)

[hkt74](https://github.com/hkt74)

[on May 28, 2025on May 28, 2025](https://github.com/googleapis/python-genai/issues/854#issuecomment-2915044694)

Contributor

More actions

Hi [@kfajdsl](https://github.com/kfajdsl)

Your code snippet works for me with model `models/gemini-2.5-flash-preview-05-20`, (and I agree the docs page is incorrect)

I tried with this [sample video](https://file-examples.com/wp-content/storage/2017/04/file_example_MP4_480_1_5MG.mp4)

Perhaps the issue might be with the video processing itself? Have you had a chance to try it with a different video?

### Jumaron commented on May 28, 2025on May 28, 2025

[![@Jumaron](https://avatars.githubusercontent.com/u/41344875?u=14967c0b9332fb88618d61e5d2367d272a3d8205&v=4&size=48)](https://github.com/Jumaron)

[Jumaron](https://github.com/Jumaron)

[on May 28, 2025on May 28, 2025](https://github.com/googleapis/python-genai/issues/854#issuecomment-2915218070)

More actions

> Hi [@kfajdsl](https://github.com/kfajdsl)
>
> Your code snippet works for me with model `models/gemini-2.5-flash-preview-05-20`, (and I agree the docs page is incorrect)
>
> I tried with this [sample video](https://file-examples.com/wp-content/storage/2017/04/file_example_MP4_480_1_5MG.mp4)
>
> Perhaps the issue might be with the video processing itself? Have you had a chance to try it with a different video?

Super confusing, the video works for me with gemini-2.5-flash-preview-05-20 and flash 2.0.

But my own video gives the 500 internal error, flash 2.0 works.

### Jumaron commented on May 28, 2025on May 28, 2025

[![@Jumaron](https://avatars.githubusercontent.com/u/41344875?u=14967c0b9332fb88618d61e5d2367d272a3d8205&v=4&size=48)](https://github.com/Jumaron)

[Jumaron](https://github.com/Jumaron)

[on May 28, 2025on May 28, 2025](https://github.com/googleapis/python-genai/issues/854#issuecomment-2915939633)

More actions

I might have found the issue,

it seems like the new API only accepts videos with an valid audiotrack, atleast adding an audiotrack to my video solved it for me.

Having no audio track will result in that error.

🎉React with 🎉2Reacted by kuwabara-S and David Dickinson

### Etragas commented on Jun 12, 2025on Jun 12, 2025

[![@Etragas](https://avatars.githubusercontent.com/u/6620250?u=0f7681de2974a1626a43c2baf9b070acd35c0cb6&v=4&size=48)](https://github.com/Etragas)

[Etragas](https://github.com/Etragas)

[on Jun 12, 2025on Jun 12, 2025](https://github.com/googleapis/python-genai/issues/854#issuecomment-2968448326)

More actions

Wow thank you [@Jumaron](https://github.com/Jumaron) I added empty audio to my video and it worked!

👍React with 👍1Reacted by Jumaron

[![](https://avatars.githubusercontent.com/u/180526454?s=64&u=275a3828bb309d0db30d7136785c6abf45045497&v=4)janasangeetha](https://github.com/janasangeetha)

self-assigned this

[on Jul 18, 2025on Jul 18, 2025](https://github.com/googleapis/python-genai/issues/854#event-18694002129)

### janasangeetha commented on Jul 18, 2025on Jul 18, 2025

[![@janasangeetha](https://avatars.githubusercontent.com/u/180526454?u=275a3828bb309d0db30d7136785c6abf45045497&v=4&size=48)](https://github.com/janasangeetha)

[janasangeetha](https://github.com/janasangeetha)

[on Jul 18, 2025on Jul 18, 2025](https://github.com/googleapis/python-genai/issues/854#issuecomment-3087191762)

More actions

Hi [@kfajdsl](https://github.com/kfajdsl)

Looks like the issue is resolved! Please let us know if you are still facing issue.

Thank you!

[![](https://avatars.githubusercontent.com/u/180526454?s=64&u=275a3828bb309d0db30d7136785c6abf45045497&v=4)janasangeetha](https://github.com/janasangeetha)

added

[status:awaiting user response](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22status%3Aawaiting%20user%20response%22)

[on Jul 18, 2025on Jul 18, 2025](https://github.com/googleapis/python-genai/issues/854#event-18694021085)

### khayyamkhan commented on Jul 19, 2025on Jul 19, 2025

[![@khayyamkhan](https://avatars.githubusercontent.com/u/70283413?u=cd380a0b2775f8a60938c96473b319d051057b11&v=4&size=48)](https://github.com/khayyamkhan)

[khayyamkhan](https://github.com/khayyamkhan)

[on Jul 19, 2025on Jul 19, 2025](https://github.com/googleapis/python-genai/issues/854#issuecomment-3092569947)

More actions

I have a bit of a dilemna:

Current setup (Vertex AI SDK):

- Using `vertexai.generative_models.GenerativeModel`
- Limited to 1fps video analysis (no VideoMetadata fps parameter support)
- Works fine for basic analysis but lacks timing precision

Desired setup (Google GenAI SDK):

- Using `google.generativeai` library with API keys
- Has VideoMetadata class with fps parameter for 24fps analysis
- Would give me much better timing precision for shot detection

The problem is IP protection. I work with unreleased content from major studios (think pre-release studio work etc.) and need to ensure maximum data protection.

My understanding was that:

- Vertex AI = enterprise-grade, content not used for training, better IP protection
- GenAI SDK with API keys = less secure, potentially used for training?

But I'm honestly not sure if this is accurate or just assumptions I've picked up. The documentation isn't super clear on the security differences between these two approaches.

Specific questions:

1. Are there actual security/IP protection differences between the Vertex AI SDK and GenAI SDK?
2. Does vertexai.generative\_models support VideoMetadata fps feature in a way that I'm missing?

The VideoMetadata fps feature would be incredibly valuable for my work, but I can't risk client IP. If both libraries offer the same enterprise protections, I'd love to switch. If not, I'll stick with Vertex AI.

Any clarity you can provide would be hugely appreciated!

### 15 remaining items

Load more

Loading

[Sign up for free](https://github.com/signup?return_to=https://github.com/googleapis/python-genai/issues/854)**to join this conversation on GitHub.** Already have an account? [Sign in to comment](https://github.com/login?return_to=https://github.com/googleapis/python-genai/issues/854)

## Metadata

## Metadata

### Assignees

- [![@janasangeetha](https://avatars.githubusercontent.com/u/180526454?s=64&u=275a3828bb309d0db30d7136785c6abf45045497&v=4)\\
janasangeetha](https://github.com/janasangeetha)

### Labels

[api: gemini-api](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22api%3A%20gemini-api%22) [priority: p2Moderately-important priority. Fix may not be included in next release.](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22priority%3A%20p2%22) Moderately-important priority. Fix may not be included in next release. [status:awaiting user response](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22status%3Aawaiting%20user%20response%22) [status:stale](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22status%3Astale%22) [type: bugError or flaw in code with unintended results or allowing sub-optimal usage patterns.](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22type%3A%20bug%22) Error or flaw in code with unintended results or allowing sub-optimal usage patterns.

### Type

No type

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

No branches or pull requests

### Participants

[![@hkt74](https://avatars.githubusercontent.com/u/4653660?s=64&u=50d6f9d69e409ffd5615c1359fc1a55f96fed2fe&v=4)](https://github.com/hkt74)[![@Etragas](https://avatars.githubusercontent.com/u/6620250?s=64&u=0f7681de2974a1626a43c2baf9b070acd35c0cb6&v=4)](https://github.com/Etragas)[![@Districtfine](https://avatars.githubusercontent.com/u/14914622?s=64&u=65fadfbf6798cb6215b613ffa52b5a55867255ab&v=4)](https://github.com/Districtfine)[![@kfajdsl](https://avatars.githubusercontent.com/u/38165247?s=64&u=ccfeec5ff6628f7efe66c7fff30f74808cc64b77&v=4)](https://github.com/kfajdsl)[![@Jumaron](https://avatars.githubusercontent.com/u/41344875?s=64&u=14967c0b9332fb88618d61e5d2367d272a3d8205&v=4)](https://github.com/Jumaron)

+5

## Issue actions

- ![](https://github.githubassets.com/assets/github-copilot-app-light-15ad5534265eeacd.svg)Open in GitHub Copilot app

You can’t perform that action at this time.