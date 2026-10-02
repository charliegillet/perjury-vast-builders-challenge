[Skip to last reply](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134/13) [Skip to top](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134/1)

[Skip to main content](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134#main-container)

# Build with Google AI Forum

[Read the community guidelines\\
_arrow\_forward_](https://discuss.ai.google.dev/faq) [Browse topics by tag\\
_arrow\_forward_](https://discuss.ai.google.dev/tags)

​


Hi Everyone,

Starting June 19, 2026, the Gemini API will stop accepting requests from unrestricted API keys to prevent unauthorized usage and billing risks.

If your Google Cloud project has the Gemini API enabled and contains unrestricted keys, please restrict them immediately.

### [Heading link](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134\#p-311902-what-to-do-1) What to do:

- Option 1 (Restrict existing keys): Go to [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials), select your key, and under API restrictions, restrict it to Gemini API ( [generativelanguage.googleapis.com](http://generativelanguage.googleapis.com/)).
- Option 2 (New keys): Generate new restricted keys in [Google AI Studio](https://aistudio.google.com/app/apikey) and update your code.

Note: Keys generated directly in AI Studio are restricted to the Gemini API by default.

# [The process of uploading videos using the File API is very slow](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134)

[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4)

- [api](https://discuss.ai.google.dev/tag/api/8),
- [video](https://discuss.ai.google.dev/tag/video/410)

You have selected **0** posts.

[select all](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134)

[cancel selecting](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134)

834
views
1
link
6
users


[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/krish_varnakavi1/48/56962_2.png)2](https://discuss.ai.google.dev/u/Krish_Varnakavi1 "Krish_Varnakavi1")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/evan_lesmez/48/48874_2.png)](https://discuss.ai.google.dev/u/Evan_Lesmez "Evan_Lesmez")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/yann_gagnon/48/50319_2.png)](https://discuss.ai.google.dev/u/Yann_Gagnon "Yann_Gagnon")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/yuyang_cai/48/36753_2.png)](https://discuss.ai.google.dev/u/yuyang_cai "yuyang_cai")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/_yu_kai_chen/48/51635_2.png)](https://discuss.ai.google.dev/u/_Yu_Kai_Chen "_Yu_Kai_Chen")

Summarize

[May 2025](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134/1 "Jump to the first post")

1 / 7


May 2025


[Dec 2025](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134/13)

## post by yuyang\_cai on May 6, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/yuyang_cai/48/36753_2.png)](https://discuss.ai.google.dev/u/yuyang_cai)

[yuyang\_cai](https://discuss.ai.google.dev/u/yuyang_cai)

1

[May 2025](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134 "Post date")

The process of uploading videos using the File API has suddenly become very slow. Previously, a 30-second video would upload successfully within a few seconds, but now it can take up to several tens of minutes. This issue has persisted for a few days. I have tried changing the API key, checked the network, and even had other people run it on different hosts, but the problem remains unresolved.

The code I am using is as follows:

```python

video_file = self.gemini_client.files.upload(file=video_segment)
            while video_file.state.name == "PROCESSING":
                time.sleep(1)
                print(".", end="")
                video_file = self.gemini_client.files.get(name=video_file.name)

            contents = [\
                types.Content(\
                    role="user",\
                    parts=[\
                        types.Part.from_uri(\
                            file_uri=video_file.uri,\
                            mime_type=video_file.mime_type,\
                        ),\
                        types.Part.from_text(text=input_prompt),\
                    ],\
                ),\
            ]

            for attempt in range(3):
                try:
                    response = self.gemini_client.models.generate_content(
                        model=self.gemini_model_version,
                        contents=contents,
                        config={
                            'response_mime_type': 'application/json',
                            'response_schema': Output,
                        },
                    )
                    break
                except errors.ServerError as e:
                    print(e.code)
                    print(e.message)
                    wait_time = 2 ** attempt
                    print(f"Attempt {attempt+1}/3: 503 error. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                except Exception as e:
                    print(f"Fatal error: {str(e)}")
                    raise
```

After checking the output, a large number of “.” appears after each video upload.

Me too

834
views
1
link
6
users


[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/krish_varnakavi1/48/56962_2.png)2](https://discuss.ai.google.dev/u/Krish_Varnakavi1 "Krish_Varnakavi1")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/evan_lesmez/48/48874_2.png)](https://discuss.ai.google.dev/u/Evan_Lesmez "Evan_Lesmez")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/yann_gagnon/48/50319_2.png)](https://discuss.ai.google.dev/u/Yann_Gagnon "Yann_Gagnon")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/yuyang_cai/48/36753_2.png)](https://discuss.ai.google.dev/u/yuyang_cai "yuyang_cai")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/_yu_kai_chen/48/51635_2.png)](https://discuss.ai.google.dev/u/_Yu_Kai_Chen "_Yu_Kai_Chen")

Summarize

## post by \_Yu\_Kai\_Chen on May 7, 2025

## post by Yann\_Gagnon on May 7, 2025

1 month later


## post by Krish\_Varnakavi1 on Jun 19, 2025

18 days later


## post by Advaith\_Menon on Jul 8, 2025

4 months later


## post by Krish\_Varnakavi1 on Nov 5, 2025

28 days later


## post by Evan\_Lesmez on Dec 3, 2025

Reply

### Related topics

| Topic | Replies | Views | Activity |
| --- | --- | --- | --- |
| [Urgent: Significant Regression in File Status Transition to ACTIVE](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [bug](https://discuss.ai.google.dev/tag/bug/7),<br>- [gemini](https://discuss.ai.google.dev/tag/gemini/44) | [19](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/1) | 656 | [Dec 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/28) |
| [File api always PROCESSING](https://discuss.ai.google.dev/t/file-api-always-processing/85107)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [api](https://discuss.ai.google.dev/tag/api/8),<br>- [generative-ai](https://discuss.ai.google.dev/tag/generative-ai/316) | [1](https://discuss.ai.google.dev/t/file-api-always-processing/85107/1) | 720 | [May 2025](https://discuss.ai.google.dev/t/file-api-always-processing/85107/2) |
| [Video file upload state not changing from processing](https://discuss.ai.google.dev/t/video-file-upload-state-not-changing-from-processing/3914)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [help\_request](https://discuss.ai.google.dev/tag/318-tag/318),<br>- [video](https://discuss.ai.google.dev/tag/video/410) | [3](https://discuss.ai.google.dev/t/video-file-upload-state-not-changing-from-processing/3914/1) | 325 | [Apr 2025](https://discuss.ai.google.dev/t/video-file-upload-state-not-changing-from-processing/3914/4) |
| [Gemini-2.5-flash api cannot process video input](https://discuss.ai.google.dev/t/gemini-2-5-flash-api-cannot-process-video-input/80093)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [gemini-flash](https://discuss.ai.google.dev/tag/gemini-flash/391),<br>- [video](https://discuss.ai.google.dev/tag/video/410) | [19](https://discuss.ai.google.dev/t/gemini-2-5-flash-api-cannot-process-video-input/80093/1) | 1.7k | [Dec 2025](https://discuss.ai.google.dev/t/gemini-2-5-flash-api-cannot-process-video-input/80093/30) |
| [File API, upload video, how to increase FPS?](https://discuss.ai.google.dev/t/file-api-upload-video-how-to-increase-fps/2183)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) | [12](https://discuss.ai.google.dev/t/file-api-upload-video-how-to-increase-fps/2183/1) | 1.2k | [Jun 2025](https://discuss.ai.google.dev/t/file-api-upload-video-how-to-increase-fps/2183/13) |

Topic list, column headers with buttons are sortable.