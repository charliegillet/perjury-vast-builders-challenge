|     |     |     |
| --- | --- | --- |
| |     |     |     |
| --- | --- | --- |
| [![](https://news.ycombinator.com/y18.svg)](https://news.ycombinator.com/) | **[Hacker News](https://news.ycombinator.com/news)** [new](https://news.ycombinator.com/newest) \| [past](https://news.ycombinator.com/front) \| [comments](https://news.ycombinator.com/newcomments) \| [ask](https://news.ycombinator.com/ask) \| [show](https://news.ycombinator.com/show) \| [jobs](https://news.ycombinator.com/jobs) \| [submit](https://news.ycombinator.com/submit) | [login](https://news.ycombinator.com/login?goto=item%3Fid%3D49351020) | |

| |     |     |     |
| --- | --- | --- |
|  |  | [Show HN: Argus, agentic QA for teams whose coding agents move faster than QA](https://github.com/argus-testing/argus) ( [github.com/argus-testing](https://news.ycombinator.com/from?site=github.com/argus-testing)) |
|  | 8 points by [canergl](https://news.ycombinator.com/user?id=canergl) [43 days ago](https://news.ycombinator.com/item?id=49351020) \| [hide](https://news.ycombinator.com/hide?id=49351020&goto=item%3Fid%3D49351020) \| [past](https://hn.algolia.com/?query=Show%20HN%3A%20Argus%2C%20agentic%20QA%20for%20teams%20whose%20coding%20agents%20move%20faster%20than%20QA&type=story&dateRange=all&sort=byDate&storyText=false&prefix&page=0) \| [favorite](https://news.ycombinator.com/fave?id=49351020&auth=60c789c122be3216bef3d659f0283f6d7c745a05) \| [9 comments](https://news.ycombinator.com/item?id=49351020) |
|  |  |

|     |     |     |
| --- | --- | --- |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [debarshri](https://news.ycombinator.com/user?id=debarshri) [43 days ago](https://news.ycombinator.com/item?id=49351596) \| [next](https://news.ycombinator.com/item?id=49351020#49351674)\[–\]<br>I dont this is top most priority. We do this with codex or claude in chrome and validate the UX.<br>I think BDD is going to be back in style for agent generate code.<br>When you generate at scale discovering, maintaining and scaling test is the major problem, thats why were katana \[1\] a behavior driven testinf utility thay discovers behavior and maintain, generates test cases.<br>\[1\] [https://github.com/adaptive-scale/katana](https://github.com/adaptive-scale/katana) | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [canergl](https://news.ycombinator.com/user?id=canergl) [43 days ago](https://news.ycombinator.com/item?id=49352276) \| [parent](https://news.ycombinator.com/item?id=49351020#49351596) \| [next](https://news.ycombinator.com/item?id=49351020#49351674)\[–\]<br>cool project but, It's not always code that's broken.<br>Imagine you have a discrepancy in DB level that ends up with an error in frontend.<br>You always need real QA tests to ensure things are working smoothly. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [ramoz](https://news.ycombinator.com/user?id=ramoz) [43 days ago](https://news.ycombinator.com/item?id=49351674) \| [prev](https://news.ycombinator.com/item?id=49351020#49351596) \| [next](https://news.ycombinator.com/item?id=49351020#49351503)\[–\]<br>"It reads the screen, not the DOM", but is built completely on Playwright? At first it made me think you have some visual model at play, but doesn't actually seem that way. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [canergl](https://news.ycombinator.com/user?id=canergl) [43 days ago](https://news.ycombinator.com/item?id=49352248) \| [parent](https://news.ycombinator.com/item?id=49351020#49351674) \| [next](https://news.ycombinator.com/item?id=49351020#49351503)\[–\]<br>yes, It uses gemini vision models on top of playwright | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [ramoz](https://news.ycombinator.com/user?id=ramoz) [43 days ago](https://news.ycombinator.com/item?id=49355114) \| [root](https://news.ycombinator.com/item?id=49351020#49351674) \| [parent](https://news.ycombinator.com/item?id=49351020#49352248) \| [next](https://news.ycombinator.com/item?id=49351020#49351503)\[–\]<br>ah interesting | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [rgbrgb](https://news.ycombinator.com/user?id=rgbrgb) [43 days ago](https://news.ycombinator.com/item?id=49351503) \| [prev](https://news.ycombinator.com/item?id=49351020#49351674) \| [next](https://news.ycombinator.com/item?id=49351020#49352161)\[–\]<br>CI with regular e2e tests usually gets pretty expensive and slow. How does cost compare to regular playwright tests? | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [canergl](https://news.ycombinator.com/user?id=canergl) [43 days ago](https://news.ycombinator.com/item?id=49352217) \| [parent](https://news.ycombinator.com/item?id=49351020#49351503) \| [next](https://news.ycombinator.com/item?id=49351020#49352161)\[–\]<br>Argus adds one more layer onto Playwright, so we expect it to be slower. Think of it as a kind of tradeoff where you gain human-level QA by accepting slower runs. | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [qqrun](https://news.ycombinator.com/user?id=qqrun) [43 days ago](https://news.ycombinator.com/item?id=49352161) \| [prev](https://news.ycombinator.com/item?id=49351020#49351503)\[–\]<br>We built something like this haha | |
| |     |     |     |
| --- | --- | --- |
| ![](https://news.ycombinator.com/s.gif) |  | [canergl](https://news.ycombinator.com/user?id=canergl) [43 days ago](https://news.ycombinator.com/item?id=49352251) \| [parent](https://news.ycombinator.com/item?id=49351020#49352161)\[–\]<br>can you share with us if It's public? | | |
| ![](https://news.ycombinator.com/s.gif)

|     |
| --- |
|  |

[Guidelines](https://news.ycombinator.com/newsguidelines.html) \| [FAQ](https://news.ycombinator.com/newsfaq.html) \| [Lists](https://news.ycombinator.com/lists) \| [API](https://github.com/HackerNews/API) \| [Security](https://news.ycombinator.com/security.html) \| [Legal](https://www.ycombinator.com/legal/) \| [Apply to YC](https://www.ycombinator.com/apply/) \| [Contact](mailto:hn@ycombinator.com)

Search: |