![](https://prod-files-secure.s3.us-west-2.amazonaws.com/329e2348-6f01-463b-a190-8fc22cf0316a/f711a1b5-5750-4712-a04c-9618381ff174/IMG_7470_2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHZOK63S%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T005315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICIRL2KowPyKtxmCIJhGrO9oJ0QNxn10HrJyHjfHHNKHAiBZCIURWXcjjpvMLN04HD%2BKqwmuIOTa4VuENSPtWJkedyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMR%2BmPSRYuLZPZbeU%2FKtwDhVt7iUX7yqxyMKK2u60noP2nXIP0riJ9K2ff3NQpzaz9y00uKx5KoyBgRxZFJ7kenynUlEUOS8JMEuNhBcYzna3lMHt1%2BHmPPeh1Uo4Ji7bQGhd4PILdh9aG6GLlpyWbb3%2F5bBJNKMN2ort6qJ2Wi36ps4hN%2BnuLstqrzWbOPkz5aevVKSzx%2BNJ3xqA2mTm4G25HOrk8rgRpgc5hkvm7T6O%2ByIL1FecPZ7HfmylrvWALNC4x8STQOOFKiy%2Ff4r8vnNk0I1dy1IfjzQUKSvFY509Bn6BsnT2D4Ui4ijEl%2F1FnLXrXyZlqO3PfAUQjRNDCRmA8%2F6I%2B9G6X6UxeERyrCmNI9Ugkr2PluXPQ%2FJNLg8hmZG7j9NyscmslA9StU6Izbxm48CFyByGZ1BgECtpkLn%2F4U%2BBlfM7DTuc3svKj0JU%2F7hrtTD%2BkOkOs5ekoX6FrQqYeDPaUeGrQX3Lc7w1gMcY%2Fi8wy3GI%2FdgOH%2B9l8afmT2NYo9l1gfY4me5eYI5bJ2LQRDPh3i%2B7XoYLDghtGHkxTS6O1D1wrJ9f5Akx3h9f92VaohutJh7RCGCt1%2BSl4gm4SqDLLY8k6sf2jqYD%2BZ4c4sTKh0PSuVBXNwQeR0IjH3kpEkkYMlMf8mnQwqO371QY6pgHCY9JjM%2FY09tFbUrxSe7vSOiunuMpE5lSRdO5M3FI%2BdTXuN7XVvLv0UdioRxmdEUa2JrXWrDz1yMs2gv7rSGGafK1%2FRqHmrAJLuGxJEJ5I2iIeGtZuKcl6LRq6F%2BUlT6Gpv9Rr9Wcd9w4e79HsTW1JAkKJs9XN58STxxRrnLKV7ikZoaNw2U4QHNxaZ8PG9%2F2HdVotJ40cNtbgciV4kGea3B%2FTKDpo&X-Amz-Signature=9fc5a241105a55f90d1849d3ddb10052c52d813d62f762a286d7437019865708&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

TLDR: I had 2,207 GoPro videos, and I need to rewatch them to find interesting moments from my cycling journey. I built a project to index them locally on my M1 Max using open-source ML models, search for those moments, and send the best clips straight to my DaVinci Resolve timeline. I indexed 628 videos (668.68 GB, 15h 13m 18s of footage duration), more details in the metrics table in the last section of this article.

As you may know, I love cycling. I discovered many great places and met amazing people through my cycling journey. For example, I went from Casablanca to Imsouane (470+ KM in 5 days) in 2024, from Kenitra to Tangier (220 KM in one and a half days) in 2023, and went on mountain biking trips in between.

![IMG_7456.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/329e2348-6f01-463b-a190-8fc22cf0316a/be2c3e3c-b098-438e-9101-cd27781a5e72/IMG_7456.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGN4BOWN%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T005315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERYDA92S3cnx0iLL5x3IT7QIpu4HHoC6AFE%2FwO1A7PbAiAqH8OPVnXj%2B29VgZmkHEbQ5eQFr5KDxeDViQbkDXjAiCqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhiKSsTg2k0AbwhjQKtwDNyDBn51JydTzdpGnTw9bcFkHI%2F%2FoWBwv%2FJVv0x6%2FoDpqVrgcIOHc4HK8m5zgaNFUfX39FbcC9e03EFMLQQHp38jiE%2BJntkHA5Yrx6eMEBD9jgAH%2FtTZuG0bAvMKfOkHzjOnO%2BUSiR7liGzFKlV0bU5EeZJX1uIFCXNmOU4IQ%2BdI9kpmuAN4XRKajb4j43BOeU9ywzGC5XXAcxGVQ6xW0ehFvaaYFLkoRX7zF3%2BHqoDx0ZUE1iPpDL%2BtIyowOXjVmT2mSsAeBhpIarZzo4u21TEqFRcrQGRmpHEDbrMRml9XmWLU41cK1qvPdZzMDGfxLxsmzJRJegrj5AVz%2FMWaUQNVR72uyCTGgBYHG4xhWcuInbW85149auchrxZu0yjMCH%2F9eVRQl4G1xQWedROq77L%2FzokglPEeIrJVRa30dj1ZCzkRW9U5ncRFUlklIg7JshxYcIobUZgOgeNzqKipqu7RqDcTpYPCJ5i0lJqV6iZaZ9jQ1xr8su%2Bzqt2K69USzOu4dg36RyWVQc7WXyI%2BryfJ6X9Bbn9ESCQzOqagGFfVP7z4VvesPhjQEiXl5AbLSZMcTuDBK8fQRjokeg4JxeGMzzIMJ7G82xFJd0or8ia1hVG7yM9BH6NaWZ0Mw8uz71QY6pgGLal8DtYosNypecJSE1i8WPUtxrszxi15cNcXJXeivsgR4HXWthdFZCH5g8kPztFg7Lc1pmA6OhpAablM09qZrRn1y8jfzYWaQYLK74WhEiorDdhP8ZD7mpejtIHNRbyHxfZ%2BSzYQIGi2LtdPU47oDBZuVmxhtYhbhHPmZKqLXfHuFnBupYNgQfGEUhmLF%2FlRuMDaGczit7to7rjt%2FTFqzqbUhdwpz&X-Amz-Signature=f788a0a99ff38dd488d82210c4214aba763300fba20211f4443251dfbc3e98ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Doing those biking trips, I captured most of them using my GoPro camera. Many of the videos I captured amazing moments, and sometimes it's kind of hard to watch the full videos to get those moments. This was one of the main reasons that I built this project ( [https://github.com/iliashad/edit-mind](https://github.com/iliashad/edit-mind))

Now, let’s talk about those videos and this project. I had about 2,207 GoPro videos in one SSD drive, and I wanna search across all of them for amazing moments, but I didn’t have the time to view them again.

I decided to use the desktop app version of this project ( [https://edit-mind.com](https://edit-mind.com/)) because it’s optimized for Apple Silicon computers, and I can have an agent that I can talk to find the moments and send them directly to my DaVinci Resolve editing timeline to edit them. And, the Docker version couldn’t access the M1 Max GPU to utilize its power.

Now, let’s talk about the indexing process because the desktop app uses a similar indexing process as the source available version [https://github.com/IliasHad/edit-mind](https://github.com/IliasHad/edit-mind).

I’ll select a folder in the desktop app, and it’ll find all videos that start with GX because I have other videos from my phone as well.

After that, it’ll transcribe the full video if we have an audio track using the OpenAI Whisper model.

Then, run the frame analysis pipeline, which will divide the video into separate video scenes (1s each, or 1fps). I have a face recognition plugin using my custom faces data, object detection, on-screen text, shot type, and scene description.

After that, I’ll be embedding the video scene data like faces, transcription, description as a document text, and saving it over a local vector DB. Later on, embed the scene frames over a visual embedding vector DB collection to use them for image search, and the same for video scene audio.

Finally, we will have three vector DB collections that have all the information about our videos, like video location metadata, camera name, faces recognized, objects detected, on-screen text, transcription, description of each scene, and many more.

Now, let’s talk about performance metrics for those indexed videos that were processed using my machine's GPU and CPU.

Here’s the metric-value table of all the videos indexed.

Note: Those metrics are still not the final ones because the project is still in development.

| Metric | Value |
| --- | --- |
| Videos indexed | 628 |
| Total footage size | 668.68 GB |
| Total footage length | 15h 13m 18s |
| Total compute time | 67h 40m 42s |
| Speed vs realtime | 0.22× or ~4.4× slower than playback |
| Frames analyzed | 57,537 |
|  |  |

And this is a table for the stage breakdown

| Stage | Total | Avg/video | % of compute |
| --- | --- | --- | --- |
| Transcription | 25h 12m 54s | 2m 25s | 37.3% |
| Frame analysis | 24h 55m 42s | 2m 23s | 36.8% |
| Scene creation | 48m 0s | 5s | 1.2% |
| Text embedding | 36m 42s | 5s | 0.9% |
| Visual embedding | 11h 49m 17s | 1m 9s | 17.5% |
| Audio embedding | 4h 18m 7s | 27s | 6.4% |

Now, let’s talk about the search feature. I prefer to use the chat assistant to ask about my videos, with the option to send them directly to my DaVinci Resolve editing timeline.

Also, we can get better indexed data if you use the advanced mode indexing to use the Qwen2.5-VL-7B-Instruct model to understand and describe your video much better, but at a slower indexing speed

With that, I indexed my GoPro videos, search and sent the video scenes that I was looking for, and made a video using the great clips.

I can confirm that running this project over an NVIDIA GPU like RTX 3060 with 12GB VRAM, I was able to get faster results than running it over my M1 Max. This project is still in development and I’m working on new improvements to make it optimized for accuracy and speed.

![Screenshot_2026-06-12_at_20.47.21.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/329e2348-6f01-463b-a190-8fc22cf0316a/2433dd3f-8ea8-4e5b-9561-fe9d5d054c4b/Screenshot_2026-06-12_at_20.47.21.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGN4BOWN%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T005315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERYDA92S3cnx0iLL5x3IT7QIpu4HHoC6AFE%2FwO1A7PbAiAqH8OPVnXj%2B29VgZmkHEbQ5eQFr5KDxeDViQbkDXjAiCqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhiKSsTg2k0AbwhjQKtwDNyDBn51JydTzdpGnTw9bcFkHI%2F%2FoWBwv%2FJVv0x6%2FoDpqVrgcIOHc4HK8m5zgaNFUfX39FbcC9e03EFMLQQHp38jiE%2BJntkHA5Yrx6eMEBD9jgAH%2FtTZuG0bAvMKfOkHzjOnO%2BUSiR7liGzFKlV0bU5EeZJX1uIFCXNmOU4IQ%2BdI9kpmuAN4XRKajb4j43BOeU9ywzGC5XXAcxGVQ6xW0ehFvaaYFLkoRX7zF3%2BHqoDx0ZUE1iPpDL%2BtIyowOXjVmT2mSsAeBhpIarZzo4u21TEqFRcrQGRmpHEDbrMRml9XmWLU41cK1qvPdZzMDGfxLxsmzJRJegrj5AVz%2FMWaUQNVR72uyCTGgBYHG4xhWcuInbW85149auchrxZu0yjMCH%2F9eVRQl4G1xQWedROq77L%2FzokglPEeIrJVRa30dj1ZCzkRW9U5ncRFUlklIg7JshxYcIobUZgOgeNzqKipqu7RqDcTpYPCJ5i0lJqV6iZaZ9jQ1xr8su%2Bzqt2K69USzOu4dg36RyWVQc7WXyI%2BryfJ6X9Bbn9ESCQzOqagGFfVP7z4VvesPhjQEiXl5AbLSZMcTuDBK8fQRjokeg4JxeGMzzIMJ7G82xFJd0or8ia1hVG7yM9BH6NaWZ0Mw8uz71QY6pgGLal8DtYosNypecJSE1i8WPUtxrszxi15cNcXJXeivsgR4HXWthdFZCH5g8kPztFg7Lc1pmA6OhpAablM09qZrRn1y8jfzYWaQYLK74WhEiorDdhP8ZD7mpejtIHNRbyHxfZ%2BSzYQIGi2LtdPU47oDBZuVmxhtYhbhHPmZKqLXfHuFnBupYNgQfGEUhmLF%2FlRuMDaGczit7to7rjt%2FTFqzqbUhdwpz&X-Amz-Signature=1fc990b6573f2891293096003f118816f6845c04dd5370a04e8b4bfd2fdb10e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Here are a couple of example video clips using these prompts:

_Find every clip where I’m biking and have a dog barking at me -_ [https://youtu.be/0SNiNlX3rzQ](https://youtu.be/0SNiNlX3rzQ)

_Make a highlight reel of the most scenic and exciting moments from my biking trips -_ [https://youtu.be/CsNLs-cyZo0](https://youtu.be/CsNLs-cyZo0)

Updated: 15/06/2026

_Show me the fastest point-of-view riding moments with the sound of wind and send it to Davinci Resolve, remove duplicate video scenes -_ [https://youtu.be/COD3Fgc-l\_A](https://youtu.be/COD3Fgc-l_A)

- Video

## More articles

### I indexed 37h of my YouTube library using an RTX 4090 and local ML models in 24h

June 27, 2026

Following my recent blog post and Hacker News post. where I ran the desktop app on my M1 Max, this time, I used the self-hosted version running in Docker with an NVIDIA RTX 4090 (24 GB VRAM).

[Read more](https://iliashaddad.com/blog/i-indexed-669-gb-of-my-gopro-videos-using-my-m1-max-computer)

## Tell me about your project

[Say Hei](https://iliashaddad.com/contact)