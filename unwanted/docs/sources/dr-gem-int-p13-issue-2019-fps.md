[Skip to content](https://github.com/googleapis/python-genai/issues/2019#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/googleapis/python-genai/issues/2019) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/googleapis/python-genai/issues/2019) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/googleapis/python-genai/issues/2019) to refresh your session.Dismiss alert

{{ message }}

[googleapis](https://github.com/googleapis)/ **[python-genai](https://github.com/googleapis/python-genai)** Public

- [Notifications](https://github.com/login?return_to=%2Fgoogleapis%2Fpython-genai) You must be signed in to change notification settings
- [Fork\\
1k](https://github.com/login?return_to=%2Fgoogleapis%2Fpython-genai)
- [Star\\
4k](https://github.com/login?return_to=%2Fgoogleapis%2Fpython-genai)


# VideoMetadata / fps in REST\#2019

New issue

Copy link

New issue

Copy link

Closed as not planned

Closed as not planned

[VideoMetadata / fps in REST](https://github.com/googleapis/python-genai/issues/2019#top)#2019

Copy link

Assignees

[![janasangeetha](https://avatars.githubusercontent.com/u/180526454?s=64&u=275a3828bb309d0db30d7136785c6abf45045497&v=4)](https://github.com/janasangeetha)

Labels

[priority: p3Desirable enhancement or fix. May not be included in next release.](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22priority%3A%20p3%22) Desirable enhancement or fix. May not be included in next release. [status:awaiting user response](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22status%3Aawaiting%20user%20response%22) [status:stale](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22status%3Astale%22) [type: questionRequest for information or clarification. Not an issue.](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22type%3A%20question%22) Request for information or clarification. Not an issue.

## Description

[![@gitlabspy](https://avatars.githubusercontent.com/u/61307585?v=4&size=48)](https://github.com/gitlabspy)

[gitlabspy](https://github.com/gitlabspy)

opened [on Feb 3, 2026](https://github.com/googleapis/python-genai/issues/2019#issue-3890491410)

Issue body actions

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3-flash-preview',
    contents=types.Content(
        parts=[\
            types.Part(\
                inline_data=types.Blob(\
                    data=video_bytes,\
                    mime_type='video/mp4'),\
                video_metadata=types.VideoMetadata(fps=5)\
            ),\
            types.Part(text='Please summarize the video in 3 sentences.')\
        ]
    )
)
```

How can I put `fps` in the REST request?

Reactions are currently unavailable

## Activity

[Sign up for free](https://github.com/signup?return_to=https://github.com/googleapis/python-genai/issues/2019)**to join this conversation on GitHub.** Already have an account?[Sign in to comment](https://github.com/login?return_to=https://github.com/googleapis/python-genai/issues/2019)

## Metadata

## Metadata

### Assignees

- [![@janasangeetha](https://avatars.githubusercontent.com/u/180526454?s=64&u=275a3828bb309d0db30d7136785c6abf45045497&v=4)\\
janasangeetha](https://github.com/janasangeetha)

### Labels

[priority: p3Desirable enhancement or fix. May not be included in next release.](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22priority%3A%20p3%22) Desirable enhancement or fix. May not be included in next release. [status:awaiting user response](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22status%3Aawaiting%20user%20response%22) [status:stale](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22status%3Astale%22) [type: questionRequest for information or clarification. Not an issue.](https://github.com/googleapis/python-genai/issues?q=state%3Aopen%20label%3A%22type%3A%20question%22) Request for information or clarification. Not an issue.

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

## Issue actions

- ![](https://github.githubassets.com/assets/github-copilot-app-light-15ad5534265eeacd.svg)Open in GitHub Copilot app

You can’t perform that action at this time.