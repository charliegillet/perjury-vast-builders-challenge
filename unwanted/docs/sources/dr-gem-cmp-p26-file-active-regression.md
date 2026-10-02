[Skip to last reply](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/28) [Skip to top](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/1)

[Skip to main content](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800#main-container)

# Build with Google AI Forum

[Read the community guidelines\\
_arrow\_forward_](https://discuss.ai.google.dev/faq) [Browse topics by tag\\
_arrow\_forward_](https://discuss.ai.google.dev/tags)

​


Hi Everyone,

Starting June 19, 2026, the Gemini API will stop accepting requests from unrestricted API keys to prevent unauthorized usage and billing risks.

If your Google Cloud project has the Gemini API enabled and contains unrestricted keys, please restrict them immediately.

### [Heading link](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800\#p-311902-what-to-do-1) What to do:

- Option 1 (Restrict existing keys): Go to [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials), select your key, and under API restrictions, restrict it to Gemini API ( [generativelanguage.googleapis.com](http://generativelanguage.googleapis.com/)).
- Option 2 (New keys): Generate new restricted keys in [Google AI Studio](https://aistudio.google.com/app/apikey) and update your code.

Note: Keys generated directly in AI Studio are restricted to the Gemini API by default.

# [Urgent: Significant Regression in File Status Transition to ACTIVE](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800)

[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4)

- [bug](https://discuss.ai.google.dev/tag/bug/7),
- [gemini](https://discuss.ai.google.dev/tag/gemini/44)

You have selected **0** posts.

[select all](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800)

[cancel selecting](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800)

656
views
7
likes
3
links
10
users


[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/vishal/48/5016_2.png)4](https://discuss.ai.google.dev/u/Vishal "Vishal")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/nguyenfromvn/48/35402_2.png)4](https://discuss.ai.google.dev/u/NguyenfromVN "NguyenfromVN")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/yann_gagnon/48/50319_2.png)2](https://discuss.ai.google.dev/u/Yann_Gagnon "Yann_Gagnon")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/wenjun_wang/48/51379_2.png)2](https://discuss.ai.google.dev/u/Wenjun_Wang "Wenjun_Wang")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/ronit_panda/48/23254_2.png)2](https://discuss.ai.google.dev/u/Ronit_Panda "Ronit_Panda")

Summarize

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/1 "Jump to the first post")

1 / 20


May 2025


[Dec 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/28)

## post by Wenjun\_Wang on May 2, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/wenjun_wang/48/51379_2.png)](https://discuss.ai.google.dev/u/wenjun_wang)

[Wenjun\_Wang](https://discuss.ai.google.dev/u/wenjun_wang)

1

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800 "Post date")

Hi Gemini Team,

We’re observing a serious regression in the time it takes for files to transition to **ACTIVE** status.

Previously, this process would complete in under 3 minutes—often within a minute. However, it now consistently takes **15 to 25 minutes**, typically **over 18 minutes**, which is a drastic increase.

This delay is significantly impacting our workflow. Could you please look into this and let us know what’s going on?

Looking forward to your help.

Best regards,

Wenjun Wang

Me too

- [Persistent Video Upload Failure - HTTP 500 Internal Server Error](https://discuss.ai.google.dev/t/persistent-video-upload-failure-http-500-internal-server-error/81824/6)

656
views
7
likes
3
links
10
users


[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/vishal/48/5016_2.png)4](https://discuss.ai.google.dev/u/Vishal "Vishal")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/nguyenfromvn/48/35402_2.png)4](https://discuss.ai.google.dev/u/NguyenfromVN "NguyenfromVN")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/yann_gagnon/48/50319_2.png)2](https://discuss.ai.google.dev/u/Yann_Gagnon "Yann_Gagnon")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/wenjun_wang/48/51379_2.png)2](https://discuss.ai.google.dev/u/Wenjun_Wang "Wenjun_Wang")

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/ronit_panda/48/23254_2.png)2](https://discuss.ai.google.dev/u/Ronit_Panda "Ronit_Panda")

Summarize

## post by Yann\_Gagnon on May 3, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/yann_gagnon/48/50319_2.png)](https://discuss.ai.google.dev/u/yann_gagnon)

[Yann\_Gagnon](https://discuss.ai.google.dev/u/yann_gagnon)

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/2 "Post date")

We are also experiencing the same for about 2 days. Files that took 5-10s are now taking 2-5 minutes.

I wonder if it has anything to do with the roll-out of Gemini to Google Drive files.

## post by Vishal on May 4, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/vishal/48/5016_2.png)](https://discuss.ai.google.dev/u/vishal)

[Vishal](https://discuss.ai.google.dev/u/vishal)
Google


[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/3 "Post date")

Thanks for flagging! Can you share some details on the file type & size? I’ll raise this with the team as well

## post by Wenjun\_Wang on May 5, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/wenjun_wang/48/51379_2.png)](https://discuss.ai.google.dev/u/wenjun_wang)

[Wenjun\_Wang](https://discuss.ai.google.dev/u/wenjun_wang)

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/5 "Post date")

I don’t think it’s caused by file size though.

The file size is really small, like 3MB.

File type is also normal, which is mp4.

## post by Vishal on May 5, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/vishal/48/5016_2.png)](https://discuss.ai.google.dev/u/vishal)

[Vishal](https://discuss.ai.google.dev/u/vishal)
Google


[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/6 "Post date")

Noted - thank you. We’re investigating the issue

## post by Alec\_Watts on May 6, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/alec_watts/48/31728_2.png)](https://discuss.ai.google.dev/u/alec_watts)

[Alec\_Watts](https://discuss.ai.google.dev/u/alec_watts)

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/8 "Post date")

This is a huge issue for us rn

## post by Subu\_Ramachandran on May 6, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/subu_ramachandran/48/31910_2.png)](https://discuss.ai.google.dev/u/subu_ramachandran)

[Subu\_Ramachandran](https://discuss.ai.google.dev/u/subu_ramachandran)

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/9 "Post date")

[@Vishal](https://discuss.ai.google.dev/u/vishal) any fix for this? The latency is quite alarming. Its creating a significant performance issue for us. Process that takes less than a minute is now well over 10 mins.

## post by Vishal on May 6, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/vishal/48/5016_2.png)](https://discuss.ai.google.dev/u/vishal)

[Vishal](https://discuss.ai.google.dev/u/vishal)
Google


[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/10 "Post date")

Hey folks, to help us with our investigation if you’re experiencing this issue, can you please DM me your project # (found here: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey))?

## post by NguyenfromVN on May 6, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/nguyenfromvn/48/35402_2.png)](https://discuss.ai.google.dev/u/nguyenfromvn)

[NguyenfromVN](https://discuss.ai.google.dev/u/nguyenfromvn)

1

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/11 "Post date")

it happened to me too, the file size really doesn’t matter, below 1MB file will take forever to process until it shows “FAILED”, I tried in both Google AI Studio and my demo app

## post by NguyenfromVN on May 6, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/nguyenfromvn/48/35402_2.png)](https://discuss.ai.google.dev/u/nguyenfromvn)

[NguyenfromVN](https://discuss.ai.google.dev/u/nguyenfromvn)

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/vishal/24/5016_2.png)Vishal](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800 "Load parent post")

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/12 "Post date")

Hi Vishal, you can re-produce this issue by using Google AI Studio, upload a short video under 10s, if you can’t see it then something went wrong with the quota for individual API key or for project or whatever, I didn’t try to re-produce this issue on a brand new API key but if your side can not re-reproduce, I think I have no choice but try a brand new API key

## post by Yann\_Gagnon on May 6, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/yann_gagnon/48/50319_2.png)](https://discuss.ai.google.dev/u/yann_gagnon)

[Yann\_Gagnon](https://discuss.ai.google.dev/u/yann_gagnon)

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/13 "Post date")

[@Vishal](https://discuss.ai.google.dev/u/vishal)

I generated a new API key and tried and the same issue was reproduced.

I don’t know if it’s helpful, but when it’s the first “run” in a while, as it was with this new key, it seems fine, but subsequent calls are slow. In my workflow, I do both small videos and images. The time for the images seem fine. The videos however will stay as “PROCESSING” for a very long time.

## post by yunus on May 6, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/yunus/48/51619_2.png)](https://discuss.ai.google.dev/u/yunus)

[yunus](https://discuss.ai.google.dev/u/yunus)

2

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/14 "Post date")

Hi folks we are having a similar issue. We use the async API to upload and infer- `await client.aio.files.upload()` . Upload into Gemini server is very fast - but files take a while for videos to turn `ACTIVE`

Yesterday we’d get stuck in `PROCESSING` for 10+ minutes. Today it seems slightly better, but still very variable across different videos uploads

[@Vishal](https://discuss.ai.google.dev/u/vishal) \- Feel free to open your DMs so we can share our project too!

- [The process of uploading videos using the File API is very slow](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134/5)

## post by NguyenfromVN on May 7, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/nguyenfromvn/48/35402_2.png)](https://discuss.ai.google.dev/u/nguyenfromvn)

[NguyenfromVN](https://discuss.ai.google.dev/u/nguyenfromvn)

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/16 "Post date")

I just read a news about the new release for the upgrade of Gemini 2.5 Pro, I used Google AI Studio and did notice that the name of the model automatically switched to “Preview 05-06”, which was great, but then I tried to upload a video, it was fast for the upload and it was fast too to say “FAILED” for the token extracting process. So the same issue is happening even after the upgrade for 2.5 Pro, which means the issue is still there ![:expressionless_face:](https://d1dlmcr85iqnpo.cloudfront.net/images/emoji/twitter/expressionless_face.png?v=14)

## post by NguyenfromVN on May 9, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/nguyenfromvn/48/35402_2.png)](https://discuss.ai.google.dev/u/nguyenfromvn)

[NguyenfromVN](https://discuss.ai.google.dev/u/nguyenfromvn)

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/18 "Post date")

latest update from my side: it works again now, I just tested by uploading a 10 seconds long video, around 2MB in size, and it took a short time to upload and to extract that file (turned into ACTIVE status). My location is Singapore, hope your side will see the same thing. Enjoy coding!

## post by Vishal on May 9, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/vishal/48/5016_2.png)](https://discuss.ai.google.dev/u/vishal)

[Vishal](https://discuss.ai.google.dev/u/vishal)
Google


[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/20 "Post date")

Hey folks, we pushed a number of small improvements to improve the processing for the File API. Please let me know if you’re still running into any issues / higher latency

10 days later


## post by Akshay\_Joshi on May 19, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/akshay_joshi/48/52505_2.png)](https://discuss.ai.google.dev/u/akshay_joshi)

[Akshay\_Joshi](https://discuss.ai.google.dev/u/akshay_joshi)

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/22 "Post date")

We’re still facing the same issue. It still gets arbitarily stuck at PROCESSING for 10+ mins. This behaviour fluctuates by hours. Please suggest what do we do to handle this uncertainity better.

Thanks!

## post by Ronit\_Panda on May 21, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/ronit_panda/48/23254_2.png)](https://discuss.ai.google.dev/u/ronit_panda)

[Ronit\_Panda](https://discuss.ai.google.dev/u/ronit_panda)

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/vishal/24/5016_2.png)Vishal](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800 "Load parent post")

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/24 "Post date")

Yeah it’s still pretty unpredictable at times we are using gemini 2.0 flash

and for us the step to upload a file to gemini takes up a long time, although this happens unpredictably sometimes quite fast else very slow

[![Screenshot 2025-05-21 at 9.22.15 AM](https://d3qe71uytubmmx.cloudfront.net/optimized/3X/6/b/6b8cc9a210ba954c4c15f6566a7817e53181eaae_2_690x339.png)\\
Screenshot 2025-05-21 at 9.22.15 AM1950×960 133 KB](https://d3qe71uytubmmx.cloudfront.net/original/3X/6/b/6b8cc9a210ba954c4c15f6566a7817e53181eaae.png "Screenshot 2025-05-21 at 9.22.15 AM")

## post by Ronit\_Panda on May 21, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/ronit_panda/48/23254_2.png)](https://discuss.ai.google.dev/u/ronit_panda)

[Ronit\_Panda](https://discuss.ai.google.dev/u/ronit_panda)

[May 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/25 "Post date")

same attachment on another try gives the following results

[![Screenshot 2025-05-21 at 9.22.49 AM](https://d3qe71uytubmmx.cloudfront.net/optimized/3X/f/b/fb706c4d239a99797337c7b97e5c6ecfd3a6929d_2_690x339.png)\\
Screenshot 2025-05-21 at 9.22.49 AM1950×960 130 KB](https://d3qe71uytubmmx.cloudfront.net/original/3X/f/b/fb706c4d239a99797337c7b97e5c6ecfd3a6929d.png "Screenshot 2025-05-21 at 9.22.49 AM")

7 months later


## post by Evan\_Lesmez on Dec 3, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/evan_lesmez/48/48874_2.png)](https://discuss.ai.google.dev/u/evan_lesmez)

[Evan\_Lesmez](https://discuss.ai.google.dev/u/evan_lesmez)

[Dec 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/27 "Post date")

Same issue today. Waitad for my 10 minute video/mp4 220MB stuck in processing state for over 40 mins now. This behavior makes the File API/Gemini API virtually useless for my case. I have uploaded larger files in both size and duration before without seeing such ridiculous upload times. My internet upload speed is 175 MB/s so definitely not the bottlekneck.

## post by Evan\_Lesmez on Dec 3, 2025

[![](https://d1dlmcr85iqnpo.cloudfront.net/user_avatar/discuss.ai.google.dev/evan_lesmez/48/48874_2.png)](https://discuss.ai.google.dev/u/evan_lesmez)

[Evan\_Lesmez](https://discuss.ai.google.dev/u/evan_lesmez)

[Dec 2025](https://discuss.ai.google.dev/t/urgent-significant-regression-in-file-status-transition-to-active/81800/28 "Post date")

Then on the next run completely fine done in 40 seconds…

Reply

### Related topics

| Topic | Replies | Views | Activity |
| --- | --- | --- | --- |
| [The process of uploading videos using the File API is very slow](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [api](https://discuss.ai.google.dev/tag/api/8),<br>- [video](https://discuss.ai.google.dev/tag/video/410) | [6](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134/1) | 835 | [Dec 2025](https://discuss.ai.google.dev/t/the-process-of-uploading-videos-using-the-file-api-is-very-slow/82134/13) |
| [File api always PROCESSING](https://discuss.ai.google.dev/t/file-api-always-processing/85107)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [api](https://discuss.ai.google.dev/tag/api/8),<br>- [generative-ai](https://discuss.ai.google.dev/tag/generative-ai/316) | [1](https://discuss.ai.google.dev/t/file-api-always-processing/85107/1) | 720 | [May 2025](https://discuss.ai.google.dev/t/file-api-always-processing/85107/2) |
| [Video file upload state not changing from processing](https://discuss.ai.google.dev/t/video-file-upload-state-not-changing-from-processing/3914)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [help\_request](https://discuss.ai.google.dev/tag/318-tag/318),<br>- [video](https://discuss.ai.google.dev/tag/video/410) | [3](https://discuss.ai.google.dev/t/video-file-upload-state-not-changing-from-processing/3914/1) | 325 | [Apr 2025](https://discuss.ai.google.dev/t/video-file-upload-state-not-changing-from-processing/3914/4) |
| [File Search Store documents stuck in STATE\_PENDING for over 10 minutes — no transition to ACTIVE or FAILED](https://discuss.ai.google.dev/t/file-search-store-documents-stuck-in-state-pending-for-over-10-minutes-no-transition-to-active-or-failed/140221)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [api](https://discuss.ai.google.dev/tag/api/8) | [19](https://discuss.ai.google.dev/t/file-search-store-documents-stuck-in-state-pending-for-over-10-minutes-no-transition-to-active-or-failed/140221/1) | 626 | [Apr 17](https://discuss.ai.google.dev/t/file-search-store-documents-stuck-in-state-pending-for-over-10-minutes-no-transition-to-active-or-failed/140221/23) |
| [Uploads in File Search Store stuck in Pending state](https://discuss.ai.google.dev/t/uploads-in-file-search-store-stuck-in-pending-state/130018)<br>[Gemini API](https://discuss.ai.google.dev/c/gemini-api/4) <br>- [bug](https://discuss.ai.google.dev/tag/bug/7),<br>- [api](https://discuss.ai.google.dev/tag/api/8),<br>- [performance](https://discuss.ai.google.dev/tag/performance/312),<br>- [ground-search](https://discuss.ai.google.dev/tag/ground-search/413) | [0](https://discuss.ai.google.dev/t/uploads-in-file-search-store-stuck-in-pending-state/130018/1) | 219 | [Mar 9](https://discuss.ai.google.dev/t/uploads-in-file-search-store-stuck-in-pending-state/130018/1) |

Topic list, column headers with buttons are sortable.