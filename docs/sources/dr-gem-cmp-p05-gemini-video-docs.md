[Skip to main content](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#main-content)

[![Gemini Generate Content API (Legacy)](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding)
- [Deutsch](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fgenerate-content%2Fvideo-understanding&prompt=select_account)

- On this page
- [Upload a video file](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#upload-video)
- [Pass video data inline](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#inline-video)
- [Pass YouTube URLs](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#youtube)
- [Agentic video understanding](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#agentic-video-understanding)
  - [Choose a processing mode](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#choose_a_processing_mode)
  - [Set the processing mode](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#set_the_processing_mode)
  - [Response structure](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#response-structure)
  - [Mix processing modes across videos](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#mix_processing_modes_across_videos)
- [Use context caching for long videos](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#context-caching)
- [Refer to timestamps in the content](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#refer-timestamps)
- [Extract detailed insights from video](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#transcribe-video)
- [Customize video processing](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#customize-video-processing)
  - [Set clipping intervals](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#clipping-intervals)
  - [Set a custom frame rate](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#custom-frame-rate)
- [Supported video formats](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#supported-formats)
- [Technical details about videos](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#technical-details-video)
- [What's next](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#whats-next)

Gemini 3.8 Flash is now available. [Try it out](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content)

Interactions API (Recommended)generateContent APILearn more

Select an optiongenerateContent API

- [Interactions API (Recommended)](https://ai.google.dev/gemini-api/docs/video-understanding)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding)
- [Learn more](https://ai.google.dev/gemini-api/docs/interactions)



 Send feedback



# Video understanding

- On this page
- [Upload a video file](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#upload-video)
- [Pass video data inline](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#inline-video)
- [Pass YouTube URLs](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#youtube)
- [Agentic video understanding](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#agentic-video-understanding)
  - [Choose a processing mode](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#choose_a_processing_mode)
  - [Set the processing mode](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#set_the_processing_mode)
  - [Response structure](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#response-structure)
  - [Mix processing modes across videos](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#mix_processing_modes_across_videos)
- [Use context caching for long videos](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#context-caching)
- [Refer to timestamps in the content](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#refer-timestamps)
- [Extract detailed insights from video](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#transcribe-video)
- [Customize video processing](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#customize-video-processing)
  - [Set clipping intervals](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#clipping-intervals)
  - [Set a custom frame rate](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#custom-frame-rate)
- [Supported video formats](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#supported-formats)
- [Technical details about videos](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#technical-details-video)
- [What's next](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#whats-next)

> To learn about video generation, see the [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni) guide.

Gemini models can process videos, enabling many frontier developer use cases
that would have historically required domain specific models.
Some of Gemini's vision capabilities include the ability to: describe, segment,
and extract information from videos, answer questions about video content, and
refer to specific timestamps within a video.

You can provide videos as input to Gemini in the following ways:

| Input method | Max size | Recommended use case |
| --- | --- | --- |
| [File API](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#upload-video) | 20GB (paid) / 2GB (free) | Large files (100MB+), long videos (10min+), reusable files. |
| [Cloud Storage Registration](https://ai.google.dev/gemini-api/docs/file-input-methods#registration) | 2GB (per file, no storage limits) | Large files (100MB+), long videos (10min+), persistent, reusable files. |
| [Inline Data](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#inline-video) | < 100MB | Small files (<100MB), short duration (<1min), one-off inputs. |
| [YouTube URLs](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#youtube) | N/A | Public YouTube videos. |

> **Note:** The [File API](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#upload-video) is recommended for most use cases, especially for files larger than 100MB or when you want to reuse the file across multiple requests.

To learn about other file input methods, such as using external URLs or files
stored in Google Cloud, see the
[File input methods](https://ai.google.dev/gemini-api/docs/file-input-methods) guide.

### Upload a video file

The following code downloads a sample video, uploads it using the [Files API](https://ai.google.dev/gemini-api/docs/files),
waits for it to be processed, and then uses the uploaded file reference to
summarize the video.

[Python](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#rest)More

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([\
      createPartFromUri(myfile.uri, myfile.mimeType),\
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",\
    ]),
  });
  console.log(response.text);
}

await main();
```

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
```

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},\
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]\
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

To optimize token efficiency and performance, consider using
[Agentic video processing](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#agentic-video-understanding).

Always use the Files API when the total request size (including the file, text
prompt, system instructions, etc.) is larger than 20 MB, the video duration is
significant, or if you intend to use the same video in multiple prompts.
The File API accepts video file formats directly.

To learn more about working with media files, see
[Files API](https://ai.google.dev/gemini-api/docs/files).

### Pass video data inline

Instead of uploading a video file using the File API, you can pass smaller
videos directly in the request to `generateContent`. This is suitable for
shorter videos under 20MB total request size.

Here's an example of providing inline video data:

[Python](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#javascript)[REST](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#rest)More

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[\
            types.Part(\
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')\
            ),\
            types.Part(text='Please summarize the video in 3 sentences.')\
        ]
    )
)
print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [\
  {\
    inlineData: {\
      mimeType: "video/mp4",\
      data: base64VideoFile,\
    },\
  },\
  { text: "Please summarize the video in 3 sentences." }\
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
            {\
              "inline_data": {\
                "mime_type":"video/mp4",\
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"\
              }\
            },\
            {"text": "Please summarize the video in 3 sentences."}\
        ]\
      }]
    }' 2> /dev/null
```

### Pass YouTube URLs

You can pass YouTube URLs directly to Gemini API as part of your request as follows:

[Python](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#rest)More

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[\
            types.Part(\
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')\
            ),\
            types.Part(text='Please summarize the video in 3 sentences.')\
        ]
    )
)
print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [\
  {\
    fileData: {\
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",\
    },\
  },\
  { text: "Please summarize the video in 3 sentences." }\
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
            {"text": "Please summarize the video in 3 sentences."},\
            {\
              "file_data": {\
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"\
              }\
            }\
        ]\
      }]
    }' 2> /dev/null
```

**Limitations:**

- For the free tier, you can't upload more than 8 hours of YouTube video per day.
- For the paid tier, there is no limit based on video length.
- For models prior to Gemini 2.5, you can upload only 1 video per request. For Gemini 2.5 and later models, you can upload a maximum of 10 videos per request.
- You can only upload public videos (not private or unlisted videos).

## Agentic video understanding

By default, video inputs use static processing (extracting frames at 1 FPS).
Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, and 3.5 Flash Lite models also support
**agentic video understanding**, where the model dynamically explores the video
timeline, selectively inspecting transcripts and adaptively adjusting frame
rates and resolution on the fly based on the prompt.

| **Mode** | **Description** | **Supported models** |
| --- | --- | --- |
| **Static** (default) | Extracts frames at a fixed rate (1 FPS) and places them into context in a single pass. Works well for short clips. | All Gemini models |
| **Agentic** | The model dynamically navigates the video timeline, loading only the content it needs based on the prompt. Up to 88% more token-efficient and ~7% higher quality on long-form content. | Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite |

### Choose a processing mode

As a general guideline, start with **agentic** mode, especially when optimizing
for response quality or token efficiency.

- **Agentic:** Long-form videos or queries targeting specific moments. The
model dynamically navigates the timeline to target contextually relevant
information without filling the context window.
- **Static:** Latency-sensitive queries on short clips (under 5 minutes), or
cases where frame-level precision across the entire clip is needed.

> **Note:** For long videos or complex prompts where agentic processing takes
> more time, use streaming (`client.models.generate_content_stream`). This keeps
> the connection active, surfaces intermediate reasoning steps, and avoids
> connection or authentication timeouts.

### Set the processing mode

[Python](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#rest)More

```
import time
from google import genai
from google.genai import types

client = genai.Client()

video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[\
        types.Part.from_uri(\
            file_uri=video_file.uri,\
            mime_type=video_file.mime_type,\
            media_processing="AGENTIC",\
        ),\
        "What are the three main arguments presented?",\
    ],
)
print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" },
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [\
    {\
      role: "user",\
      parts: [\
        {\
          fileData: {\
            fileUri: videoFile.uri,\
            mimeType: videoFile.mimeType,\
          },\
          mediaProcessing: "AGENTIC",\
        },\
        { text: "What are the three main arguments presented?" },\
      ],\
    },\
  ],
});
console.log(response.text);
```

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/lecture.mp4", nil)
parts := []*genai.Part{
    {
        FileData: &genai.FileData{
            FileURI:  uploadedFile.URI,
            MIMEType: uploadedFile.MIMEType,
        },
        MediaProcessing: genai.MediaProcessingAgentic,
    },
    genai.NewPartFromText("What are the three main arguments presented?"),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)
fmt.Println(result.Text())
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{\
      "parts": [\
        {\
          "file_data": {\
            "file_uri": "'${file_uri}'",\
            "mime_type": "video/mp4"\
          },\
          "media_processing": "AGENTIC"\
        },\
        {"text": "What are the three main arguments presented?"}\
      ]\
    }]
  }'
```

> **Note:** To verify that agentic processing was used, inspect `response.candidates[0].content.parts`. The presence of `tool_call` and `tool_response` parts with the `MEDIA_PROCESSING` tool type indicates that the model dynamically navigated the video.

> **Note:** Unlike other server-side tools (such as Google Search or URL
> context), agentic video does not require setting
> `include_server_side_tool_invocations=True` in `ToolConfig` for tool calls and
> results to be returned or streamed. The `tool_call` and `tool_response` parts
> for video navigation are returned automatically when
> `media_processing="AGENTIC"` is set on any input part.

### Response structure

When agentic processing is enabled, the response includes additional parts that expose the internal navigation trace:

- `tool_call` **parts** (`tool_type: "MEDIA_PROCESSING"`): emitted each time the model requests a video segment or audio transcript.
- `tool_response` **parts** (`tool_type: "MEDIA_PROCESSING"`): the result of each load operation.

You do not need to handle or reply to these parts manually: pass the full response back as conversation history and they are handled automatically.

If `include_thoughts=True` is set in `ThinkingConfig`, reasoning steps appear as `thought: true` parts interleaved with the tool call/response pairs. With thoughts disabled, thought text is omitted but tool parts are still present.

The following example shows the response payload with interleaved tool call and response parts:

```
{
  "candidates": [\
    {\
      "content": {\
        "role": "model",\
        "parts": [\
          {\
            "thought": true,\
            "text": "Inspecting transcript for key discussion topics..."\
          },\
          {\
            "thought_signature": "sig_A",\
            "tool_call": {\
              "tool_type": "MEDIA_PROCESSING"\
            }\
          },\
          {\
            "thought_signature": "sig_B",\
            "tool_response": {\
              "tool_type": "MEDIA_PROCESSING"\
            }\
          },\
          {\
            "thought": true,\
            "text": "Loading visual frames to verify slide content..."\
          },\
          {\
            "thought_signature": "sig_C",\
            "tool_call": {\
              "tool_type": "MEDIA_PROCESSING"\
            }\
          },\
          {\
            "thought_signature": "sig_D",\
            "tool_response": {\
              "tool_type": "MEDIA_PROCESSING"\
            }\
          },\
          {\
            "thought": true,\
            "text": "Synthesizing answer from gathered evidence..."\
          },\
          {\
            "text": "The three main arguments presented in the lecture are...",\
            "thought_signature": "sig_E"\
          }\
        ]\
      }\
    }\
  ]
}
```

### Mix processing modes across videos

You can set different processing modes for each video Part in the same request:

[Python](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#rest)More

```
from google import genai
from google.genai import types

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[\
        types.Part.from_uri(\
            file_uri=lecture.uri,\
            mime_type=lecture.mime_type,\
            media_processing="AGENTIC",  # Use agentic video understanding\
        ),\
        types.Part.from_uri(\
            file_uri=experiment.uri,\
            mime_type=experiment.mime_type,\
            media_processing="STATIC",  # Use static processing\
        ),\
        "Compare the lecture content with the experiment results.",\
    ],
)
print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" },
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" },
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [\
    {\
      role: "user",\
      parts: [\
        {\
          fileData: {\
            fileUri: lecture.uri,\
            mimeType: lecture.mimeType,\
          },\
          mediaProcessing: "AGENTIC", // Use agentic video understanding\
        },\
        {\
          fileData: {\
            fileUri: experiment.uri,\
            mimeType: experiment.mimeType,\
          },\
          mediaProcessing: "STATIC", // Use static processing\
        },\
        { text: "Compare the lecture content with the experiment results." },\
      ],\
    },\
  ],
});
console.log(response.text);
```

```
lecturePart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  lectureFile.URI,
        MIMEType: lectureFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingAgentic, // Use agentic
}
experimentPart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  experimentFile.URI,
        MIMEType: experimentFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingStatic, // Use static
}
parts := []*genai.Part{
    lecturePart,
    experimentPart,
    genai.NewPartFromText("Compare the lecture content with the experiment results."),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
fmt.Println(result.Text())
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{\
      "parts": [\
        {\
          "file_data": {\
            "file_uri": "'${lecture_uri}'",\
            "mime_type": "video/mp4"\
          },\
          "media_processing": "AGENTIC"\
        },\
        {\
          "file_data": {\
            "file_uri": "'${experiment_uri}'",\
            "mime_type": "video/mp4"\
          },\
          "media_processing": "STATIC"\
        },\
        {"text": "Compare the lecture content with the experiment results."}\
      ]\
    }]
  }'
```

## Use context caching for long videos

For videos longer than 10 minutes, or when you plan to make multiple requests
against the same video file, use [context caching](https://ai.google.dev/gemini-api/docs/caching) to
reduce costs and improve latency. Context caching lets you process the video
once and reuse the tokens for subsequent queries, making it ideal for chat
sessions or repeated analysis of long-form content.

## Refer to timestamps in the content

You can ask questions about specific points in time within the video using
timestamps of the form `MM:SS`.

[Python](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#rest)More

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[\
        myfile,\
        "What are the examples given at 00:05 and 00:10 supposed to show us?",\
    ],
)
print(response.text)
```

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [\
    myfile,\
    "What are the examples given at 00:05 and 00:10 supposed to show us?",\
  ],
});
console.log(response.text);
```

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("What are the examples given at 00:05 and 00:10 supposed to show us?"),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},\
          {"text": "What are the examples given at 00:05 and 00:10 supposed to show us?"}\
        ]\
      }]
    }' 2> /dev/null
```

## Extract detailed insights from video

Gemini models offer powerful capabilities for understanding video content by
processing information from both the **audio and visual** streams. This lets you
extract a rich set of details, including generating descriptions of what is
happening in a video and answering questions about its content.

For visual descriptions, the model samples the video at a rate of **1 frame**
**per second** (FPS). This default sampling rate works well for most content, but
note that it may miss details in videos with rapid motion or quick scene changes.
For such high-motion content, consider [setting a custom frame rate](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#custom-frame-rate).

[Python](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#rest)More

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[\
        myfile,\
        "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",\
    ],
)
print(response.text)
```

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [\
    myfile,\
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",\
  ],
});
console.log(response.text);
```

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
        "Include timestamps for salient moments."),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},\
          {"text": "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."}\
        ]\
      }]
    }' 2> /dev/null
```

## Customize video processing

You can customize video processing in the Gemini API by setting clipping
intervals or providing custom frame rate sampling. These customization options
are only supported when processing the video in `"static"` mode.

### Set clipping intervals

You can clip video by specifying `videoMetadata` with start and end offsets.

[Python](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#javascript)More

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[\
            types.Part(\
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),\
                video_metadata=types.VideoMetadata(\
                    start_offset='1250s',\
                    end_offset='1570s'\
                )\
            ),\
            types.Part(text='Please summarize the video in 3 sentences.')\
        ]
    )
)
```

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.8-flash';

async function main() {
const contents = [\
  {\
    role: 'user',\
    parts: [\
      {\
        fileData: {\
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',\
          mimeType: 'video/*',\
        },\
        videoMetadata: {\
          startOffset: '40s',\
          endOffset: '80s',\
        }\
      },\
      {\
        text: 'Please summarize the video in 3 sentences.',\
      },\
    ],\
  },\
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### Set a custom frame rate

You can set custom frame rate sampling by passing an `fps` argument to
`videoMetadata`.

[Python](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#javascript)More

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
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

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const myfile = await ai.files.upload({
  file: "path/to/sample.mp4",
  mimeType: "video/mp4",
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [\
    {\
      fileData: {\
        fileUri: myfile.uri,\
        mimeType: myfile.mimeType,\
      },\
      videoMetadata: {\
        fps: 5,\
      },\
    },\
    "Please summarize the video in 3 sentences.",\
  ],
});

console.log(response.text);
```

By default 1 frame per second (FPS) is sampled from the video. You might want to
set low FPS (< 1) for long videos. This is especially useful for mostly static
videos (e.g. lectures). Use a higher FPS for videos requiring granular temporal
analysis, such as fast-action understanding or high-speed motion tracking.

## Supported video formats

Gemini supports the following video format MIME types:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Technical details about videos

- **Supported models and context**: All Gemini models can process video data.

  - Models with a 1M context window can process videos up to 3 hours long by
    default (at low media resolution), or up to 1 hour long at high media
    resolution.
- **Processing modes**: Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite,
and later models support two video processing modes:

  - **Static**: Frames are extracted at 1 FPS and placed into context (default
    for all models). Audio is processed at 1Kbps (single channel).
    Timestamps are added every second. Best for short clips or when every frame
    matters (such as frame-by-frame inspection). Note that fast action sequences
    might lose detail due to the 1 FPS sampling rate.
  - **Agentic**: The model dynamically navigates the video, loading
    transcript and/or frames and/or audio on demand. This uses up to 88%
    fewer tokens for long-form content, though navigation may slightly
    increase Time to First Token (TTFT) on short clips (<5 minutes) due to
    internal reasoning and tool round-trips before generation begins.
    Responses include `MEDIA_PROCESSING` tool call and response parts to
    preserve reasoning context across turns. Best for long-form videos to
    optimize token costs and response quality. Supported on Gemini 3.8 Flash,
    3.7 Flash, 3.6 Flash, and 3.5 Flash Lite. See
    [Agentic video understanding](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#agentic-video-understanding) for details.
- **Token calculation (static mode)**: Each second of video is tokenized as
follows:

  - Individual frames (sampled at 1 FPS):
    - If `media_resolution` is set to low, frames are tokenized at 66
      tokens per frame.
    - Otherwise, frames are tokenized at 258 tokens per frame.
  - Audio: 32 tokens per second.
  - Metadata is also included.
  - Total: Approximately 100 tokens per second of video at default (low) media
    resolution, or approximately 300 tokens per second of video at high media
    resolution.
- **Token calculation (agentic mode)**: Token usage varies based on content
complexity and the model's navigation strategy. Navigation reasoning tokens
generated during video exploration are accounted as **thinking tokens**
(`thoughts_token_count`), while frames, audio, and transcript loaded on
demand are accounted as tool prompt tokens (`tool_use_prompt_token_count`).
Agentic processing typically uses up to 88% fewer total tokens than static
processing for long-form content because the model loads only the transcript
and/or frames and/or audio it needs to answer the prompt (see the
[tokens guide](https://ai.google.dev/gemini-api/docs/generate-content/tokens#video-token-usage)).
- **Media resolution**: Gemini 3 introduces granular control over multimodal
vision processing with the `media_resolution` parameter. The
`media_resolution` parameter determines the **maximum number of tokens**
**allocated per input image or video frame.** Higher resolutions improve the
model's ability to read fine text or identify small details, but increase
token usage and latency. The `media_resolution` and `media_processing`
parameters are independent: you can set both on the same video Part.

For more details on token calculations, see the
[tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens) guide.

- **Timestamp format**: When referring to specific moments in a video within
your prompt, use the `MM:SS` format (e.g., `01:15` for 1 minute and 15
seconds).
- **Prompt placement**: If combining text and a single video, place the text prompt
_after_ the video part in the `contents` array.
- **Timeouts for long requests**: For videos that require extended
processing time or complex multi-step reasoning, use streaming
(`client.models.generate_content_stream`). Synchronous, non-streaming
requests that experience backend retries under high demand can exceed
connection or authentication token validity windows, which may surface as
unexpected `401 Unauthorized` or timeout errors. Streaming keeps the
connection active and surfaces intermediate reasoning and tool call progress.

## What's next

- [Media resolution](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution): Control the
resolution of video frames to balance quality and token usage.
- [Tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens): Understand how video content is tokenized
in both static and agentic processing modes.
- [System instructions](https://ai.google.dev/gemini-api/docs/generate-content/text-generation#system-instructions):
System instructions let you steer the behavior of the model based on your
specific needs and use cases.
- [Files API](https://ai.google.dev/gemini-api/docs/files): Learn more about uploading and managing
files for use with Gemini.
- [File prompting strategies](https://ai.google.dev/gemini-api/docs/files#prompt-guide): The Gemini
API supports prompting with text, image, audio, and video data, also known as
multimodal prompting.
- [Safety guidance](https://ai.google.dev/gemini-api/docs/safety-guidance): Sometimes generative AI
models produce unexpected outputs, such as outputs that are inaccurate,
biased, or offensive. Post-processing and human evaluation are essential to
limit the risk of harm from such outputs.



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-16 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-09-16 UTC."\],\[\],\[\]\]