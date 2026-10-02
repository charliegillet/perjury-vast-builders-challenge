[Skip to main content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#main-content)

[![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/vfdb441d2e08dbd9d3e48d8cd72b242388a87bcf7626bf5fb9df50c2bdd4a70fd/clouddocs/images/lockup_full_color.svg)](https://docs.cloud.google.com/)

`/`

[Console](https://console.cloud.google.com/)Language

- [English](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding)
- [Deutsch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding?hl=de)
- [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding?hl=es-419)
- [Français](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding?hl=fr)
- [Indonesia](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding?hl=id)
- [Italiano](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding?hl=it)
- [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding?hl=pt-br)
- [עברית](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding?hl=he)
- [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding?hl=zh-cn)
- [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding?hl=zh-tw)
- [日本語](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding?hl=ja)
- [한국어](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding?hl=ko)

Sign in

[![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/192px.svg)](https://docs.cloud.google.com/gemini-enterprise-agent-platform)

- [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform)

[Start free](https://console.cloud.google.com/freetrial)

- On this page
- [Supported models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#supported-models)
- [Add videos to a request](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#add-videos)
  - [Single video](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#single-video)
  - [Video with audio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#video-audio)
- [Customize video processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#customize-video-processing)
  - [Set clipping intervals](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#clipping-intervals)
  - [Set a custom frame rate](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#custom-frame-rate)
- [Agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#agentic-video-processing)
  - [Supported models and file types](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#agentic-video-processing-support)
  - [When to use agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#when-to-use-agentic-video-processing)
  - [Use agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#use-agentic-video-processing)
- [Adjust media resolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#adjust-media-resolution)
- [Set optional model parameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#set-optional-model-parameters)
- [Video tokenization](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#video-tokenization)
- [Best practices](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#best-practices)
- [Limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#limitations)
- [Technical details about videos](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#technical-details-video)
- [What's next](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#whats-next)

- [Home](https://docs.cloud.google.com/)
- [Documentation](https://docs.cloud.google.com/docs)
- [AI and ML](https://docs.cloud.google.com/docs/ai-ml)
- [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
- [Models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



 Send feedback



# Video understanding    Stay organized with collections      Save and categorize content based on your preferences.

- On this page
- [Supported models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#supported-models)
- [Add videos to a request](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#add-videos)
  - [Single video](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#single-video)
  - [Video with audio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#video-audio)
- [Customize video processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#customize-video-processing)
  - [Set clipping intervals](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#clipping-intervals)
  - [Set a custom frame rate](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#custom-frame-rate)
- [Agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#agentic-video-processing)
  - [Supported models and file types](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#agentic-video-processing-support)
  - [When to use agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#when-to-use-agentic-video-processing)
  - [Use agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#use-agentic-video-processing)
- [Adjust media resolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#adjust-media-resolution)
- [Set optional model parameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#set-optional-model-parameters)
- [Video tokenization](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#video-tokenization)
- [Best practices](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#best-practices)
- [Limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#limitations)
- [Technical details about videos](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#technical-details-video)
- [What's next](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#whats-next)

You can add videos to Gemini requests to perform tasks that involve
understanding the contents of the included videos. This page
shows you how to add videos to your requests to Gemini in
Gemini Enterprise Agent Platform by using the Google Cloud console and the Agent Platform API.

## Supported models

The following table lists the models that support video understanding:

| Models | Media details | MIME types |
| --- | --- | --- |
| - [Gemini Omni Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-flash-preview) preview | - Maximum video length (with audio):<br>   10 seconds<br>   <br>- Maximum video length (without audio):<br>   10 seconds<br>   <br>- Maximum number of videos per prompt:<br>   3 | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| - [Gemini Omni 1.1 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-1-1-flash) preview | - Maximum video length (with audio):<br>   10 seconds<br>   <br>- Maximum video length (without audio):<br>   10 seconds<br>   <br>- Maximum number of videos per prompt:<br>   3<br>   <br>- Supported aspect ratios:<br>   16:9, 9:16<br>   <br>- Supported resolutions:<br>   360p, 720p, 1080p, 4k | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| - [Gemini 3.8 Live](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-live) | - Supported resolutions:<br>   Minimum: 704x1280 or 1280x704<br>   <br>- Supported aspect ratios:<br>   Portrait, Landscape | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| - [Gemini 3.8 Flash Cyber](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash-cyber)<br>- [Gemini 3.8 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash)<br>- [Gemini 3.7 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash)<br>- [Gemini 3.6 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-6-flash)<br>- [Gemini 3.5 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash-lite)<br>- [Gemini 3.5 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash)<br>- [Gemini 3.1 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite)<br>- [Gemini 2.5 Pro](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-pro)<br>- [Gemini 2.5 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite)<br>- [Gemini 2.5 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash) | - Maximum video length (with audio):<br>   Approximately 45 minutes<br>   <br>- Maximum video length (without audio):<br>   Approximately 1 hour<br>   <br>- Maximum number of videos per prompt:<br>   10 | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| - [Gemini 3.1 Pro](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-pro) preview<br>- [Gemini 3 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-flash) preview | - Maximum video length (with audio):<br>   Approximately 45 minutes<br>   <br>- Maximum video length (without audio):<br>   Approximately 1 hour<br>   <br>- Maximum number of videos per prompt:<br>   10<br>   <br>- Default resolution tokens per frame:<br>   70 | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| - [Gemini 3.1 Flash-Lite Image (Nano Banana 2 Lite)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite-image) | - Maximum number of input video files per prompt:<br>   10<br>   <br>- Maximum YouTube URLs per prompt:<br>   1<br>   <br>- Maximum video length (without audio):<br>   As supported by the 65,536 token context window (approximately 12 minutes). | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| - [Gemini 3.1 Flash Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-image) | - Maximum number of input video files per prompt:<br>   10<br>   <br>- Maximum YouTube URLs per prompt:<br>   1<br>   <br>- Maximum video length (without audio):<br>   As supported by the 128k token context window (approximately 25 minutes). | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| - [Gemini 2.5 Flash with Gemini Live API native audio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-live-api) | - Standard resolution:<br>   768 x 768 | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |

For a list of languages supported by Gemini models, see model information
[Google models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). To learn
more about how to design multimodal prompts, see
[Design multimodal prompts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/design-multimodal-prompts).
If you're looking for a way to use Gemini directly from your mobile and
web apps, see the
[Firebase AI Logic client SDKs](https://firebase.google.com/docs/ai-logic) for
Swift, Android, Web, Flutter, and Unity apps.

## Add videos to a request

You can add a single video or multiple videos in your request to Gemini and the
videos can include audio.

### Single video

The sample code in each of the following tabs shows a different way to identify
what's in a video. This sample works with all Gemini multimodal models.

[Console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#console)[Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#python-google-gen-ai-sdk)[Go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#go-google-gen-ai-sdk)[Java](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#java-google-gen-ai-sdk)[Node.js](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#node.js-google-gen-ai-sdk)[REST](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#rest)More







To send a multimodal prompt by using the Google Cloud console, do the
following:

01. In the Agent Platform section of the Google Cloud console, go to
     the **Agent Studio** page.

    [Go to Agent Studio](https://console.cloud.google.com/agent-platform/generative/multimodal)

02. Click **Create prompt**.

03. Optional: Configure the model and parameters:

    - **Model**: Select a model.
04. Optional: To configure advanced parameters, click **Advanced** and
     configure as follows:


    **Click to expand advanced configurations**

    - **Top-K**: Use the slider or textbox to enter a value for top-K.


      Top-K changes how the model selects tokens for output. A top-K of
      `1` means the next selected token is the most probable among all
      tokens in the model's vocabulary (also called greedy decoding), while a top-K of
      `3` means that the next token is selected from among the three most
      probable tokens by using temperature.


      For each token selection step, the top-K tokens with the highest
      probabilities are sampled. Then tokens are further filtered based on top-P with
      the final token selected using temperature sampling.

      Specify a lower value for less random responses and a higher value for more
      random responses.

    - **Top-P**: Use the slider or textbox to enter a value for top-P.
       Tokens are selected from most probable to the least until the sum of their
       probabilities equals the value of top-P. For the least variable results,
       set top-P to `0`.
    - **Max responses**: Use the slider or textbox to enter a value for
       the number of responses to generate.
    - **Streaming responses**: Enable to print responses as they're
       generated.
    - **Safety filter threshold**: Select the threshold of how likely you
       are to see responses that could be harmful.
    - **Enable Grounding**: Grounding isn't supported for multimodal
       prompts.
    - **Region**: Select the region that you want to use.
    - **Temperature**: Use the slider or textbox to enter a value for
       temperature.





      ```

      The temperature is used for sampling during response generation, which occurs when topP
      and topK are applied. Temperature controls the degree of randomness in token selection.
      Lower temperatures are good for prompts that require a less open-ended or creative response, while
      higher temperatures can lead to more diverse or creative results. A temperature of 0
      means that the highest probability tokens are always selected. In this case, responses for a given
      prompt are mostly deterministic, but a small amount of variation is still possible.

      If the model returns a response that's too generic, too short, or the model gives a fallback
      response, try increasing the temperature. If the model enters infinite generation, increasing the
      temperature to at least 0.1 may lead to improved results.
       1.0 is the
      recommended starting value for temperature.
      </li>
        <li>**Output token limit**: Use the slider or textbox to enter a value for
          the max output limit.


      Maximum number of tokens that can be generated in the response. A token is
      approximately four characters. 100 tokens correspond to roughly 60-80 words.

      Specify a lower value for shorter responses and a higher value for potentially longer
      responses.

      </li>
        <li>**Add stop sequence**: Optional. Enter a stop sequence, which is a
          series of characters that includes spaces. If the model encounters a
          stop sequence, the response generation stops. The stop sequence isn't
          included in the response, and you can add up to five stop sequences.</li>
      </ul>
      ```


05. Click **Insert Media**, and select a source for your file.



    [Upload](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#upload)[By URL](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#by-url)[YouTube](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#youtube)[Cloud Storage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#cloud-storage)[Google Drive](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#google-drive)More







    Select the file that you want to upload and click **Open**.



    Enter the URL of the file that you want to use and click **Insert**.











    Enter the URL of the YouTube video that you want to use and click
    **Insert**.



    You can use any public video or a video that's owned by the account that
    you used to sign in to the Google Cloud console.



    Select the bucket and then the file from the bucket that
    you want to import and click **Select**.



    1. Choose an account and give consent to
       Agent Studio to access your account the first
       time you select this option. You can upload multiple files that
       have a total size of up to 10 MB. A single file can't exceed
       7 MB.
    2. Click the file that you want to add.
    3. Click **Select**.

       The file thumbnail displays in the **Prompt** pane. The total
       number of tokens also displays. If your prompt data exceeds the
       [token limit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models), the
       tokens are truncated and aren't included in processing your data.


06. Enter your text prompt in the **Prompt** pane.

07. Optional: To view the **Token ID to text** and **Token IDs**, click the
     **tokens count** in the **Prompt** pane.

08. Click **Submit**.

09. Optional: To save your prompt to **My prompts**, click save\_alt **Save**.

10. Optional: To get the Python code or a curl command for your prompt, click
     code **Build with code > Get code**.




#### Install

```
pip install --upgrade google-genai
```

To learn more, see the
[SDK reference documentation](https://googleapis.github.io/python-genai/).


Set environment variables to use the Google Gen AI SDK with Vertex AI:

```
# Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values
# with appropriate values for your project.
export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_ENTERPRISE=True
```

```
from google import genai
from google.genai.types import HttpOptions, Part

client = genai.Client(http_options=HttpOptions(api_version="v1"))
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[\
        Part.from_uri(\
            file_uri="gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",\
            mime_type="video/mp4",\
        ),\
        "What is in the video?",\
    ],
)
print(response.text)
# Example response:
# The video shows several people surfing in an ocean with a coastline in the background. The camera ...
```

Learn how to install or update the [Go](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/sdks/overview).


To learn more, see the
[SDK reference documentation](https://pkg.go.dev/google.golang.org/genai).


Set environment variables to use the Google Gen AI SDK with Vertex AI:

```
# Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values
# with appropriate values for your project.
export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_ENTERPRISE=True
```

```
import (
	"context"
	"fmt"
	"io"

	genai "google.golang.org/genai"
)

// generateWithMuteVideo shows how to generate text using a video with no sound as the input.
func generateWithMuteVideo(w io.Writer) error {
	ctx := context.Background()

	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
	})
	if err != nil {
		return fmt.Errorf("failed to create genai client: %w", err)
	}

	modelName := "gemini-2.5-flash"
	contents := []*genai.Content{
		{Parts: []*genai.Part{
			{Text: "What is in the video?"},
			{FileData: &genai.FileData{
				FileURI:  "gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",
				MIMEType: "video/mp4",
			}},
		},
			Role: genai.RoleUser},
	}

	resp, err := client.Models.GenerateContent(ctx, modelName, contents, nil)
	if err != nil {
		return fmt.Errorf("failed to generate content: %w", err)
	}

	respText := resp.Text()

	fmt.Fprintln(w, respText)

	// Example response:
	// The video shows several surfers riding waves in an ocean setting. The waves are ...

	return nil
}
```

Learn how to install or update the [Java](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/sdks/overview).


To learn more, see the
[SDK reference documentation](https://central.sonatype.com/artifact/com.google.genai/google-genai).


Set environment variables to use the Google Gen AI SDK with Vertex AI:

```
# Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values
# with appropriate values for your project.
export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_ENTERPRISE=True
```

```

import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.HttpOptions;
import com.google.genai.types.Part;

public class TextGenerationWithMuteVideo {

  public static void main(String[] args) {
    // TODO(developer): Replace these variables before running the sample.
    String modelId = "gemini-2.5-flash";
    generateContent(modelId);
  }

  // Generates text with mute video input
  public static String generateContent(String modelId) {
    // Initialize client that will be used to send requests. This client only needs to be created
    // once, and can be reused for multiple requests.
    try (Client client =
        Client.builder()
            .location("global")
            .vertexAI(true)
            .httpOptions(HttpOptions.builder().apiVersion("v1").build())
            .build()) {

      GenerateContentResponse response =
          client.models.generateContent(
              modelId,
              Content.fromParts(
                  Part.fromUri(
                      "gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",
                      "video/mp4"),
                  Part.fromText("What is in this video?")),
              null);

      System.out.print(response.text());
      // Example response:
      // This video features **surfers in the ocean**.
      //
      // The main focus is on **one individual who catches and rides a wave**, executing various
      // turns and maneuvers as the wave breaks and dissipates into whitewater...
      return response.text();
    }
  }
}
```

#### Install

```
npm install @google/genai
```

To learn more, see the
[SDK reference documentation](https://googleapis.github.io/js-genai/).


Set environment variables to use the Google Gen AI SDK with Vertex AI:

```
# Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values
# with appropriate values for your project.
export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_ENTERPRISE=True
```

```
const {GoogleGenAI} = require('@google/genai');

const GOOGLE_CLOUD_PROJECT = process.env.GOOGLE_CLOUD_PROJECT;
const GOOGLE_CLOUD_LOCATION = process.env.GOOGLE_CLOUD_LOCATION || 'global';

async function generateText(
  projectId = GOOGLE_CLOUD_PROJECT,
  location = GOOGLE_CLOUD_LOCATION
) {
  const client = new GoogleGenAI({
    vertexai: true,
    project: projectId,
    location: location,
  });

  const response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: [\
      {\
        role: 'user',\
        parts: [\
          {\
            fileData: {\
              mimeType: 'video/mp4',\
              fileUri:\
                'gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4',\
            },\
          },\
          {\
            text: 'What is in the video?',\
          },\
        ],\
      },\
    ],
    config: {
      mediaResolution: 'MEDIA_RESOLUTION_LOW',
    },
  });

  console.log(response.text);

  // Example response:
  // The video shows several people surfing in an ocean with a coastline in the background. The camera ...

  return response.text;
}
```

After you set up your environment, you can use REST to test a text prompt. The
following sample sends a request to the publisher model endpoint.

Before using any of the request data,
make the following replacements:

- `PROJECT_ID`:
Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
.
- `FILE_URI`:
The URI or URL of the file to include in the prompt. Acceptable values include the following:



  - **Cloud Storage bucket URI:** The object must either be publicly readable or reside in
     the same Google Cloud project that's sending the request.
  - **HTTP URL:** The file URL must be publicly readable. You can specify one video file, one
     audio file, and up to 10 image files per request. Audio files, video files, and documents can't
     exceed 15 MB.
  - **YouTube video URL:** The YouTube video must be either owned by the account that you used
     to sign in to the Google Cloud console or be public. Only one YouTube video URL is supported per
     request.

When specifying a `fileURI`, you must also specify the media type
(`mimeType`) of the file. If VPC Service Controls is enabled, specifying a media file
URL for `fileURI` is not supported.

If you don't have a video file in Cloud Storage, then you can use the following
publicly available file:
`gs://cloud-samples-data/video/animals.mp4` with a mime type of
`video/mp4`. To view this video,
[open the sample MP4](https://storage.googleapis.com/cloud-samples-data/video/animals.mp4)
file.


- `MIME_TYPE`:
The media type of the file specified in the `data` or `fileUri`
fields. Acceptable values include the following:

**Click to expand MIME types**


  - `application/pdf`
  - `audio/mpeg`
  - `audio/mp3`
  - `audio/wav`
  - `image/png`
  - `image/jpeg`
  - `image/webp`
  - `text/plain`
  - `video/mov`
  - `video/mpeg`
  - `video/mp4`
  - `video/mpg`
  - `video/avi`
  - `video/wmv`
  - `video/mpegps`
  - `video/flv`

- `TEXT`:
The text instructions to include in the prompt.
For example,
`What is in the video?`

To send your request, choose one of these options:

[curl](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#curl)[PowerShell](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#powershell)More

Save the request body in a file named `request.json`.
Run the following command in the terminal to create or overwrite
this file in the current directory:


```
cat > request.json << 'EOF'
{
  "contents": {
    "role": "USER",
    "parts": [\
      {\
        "fileData": {\
          "fileUri": "FILE_URI",\
          "mimeType": "MIME_TYPE"\
        }\
      },\
      {\
        "text": "TEXT"\
      }\
    ]
  }
}
EOF
```

Then execute the following command to send your REST request:


```
curl -X POST \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     -d @request.json \
     "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-3.5-flash:generateContent"
```

Save the request body in a file named `request.json`.
Run the following command in the terminal to create or overwrite
this file in the current directory:


```
@'
{
  "contents": {
    "role": "USER",
    "parts": [\
      {\
        "fileData": {\
          "fileUri": "FILE_URI",\
          "mimeType": "MIME_TYPE"\
        }\
      },\
      {\
        "text": "TEXT"\
      }\
    ]
  }
}
'@  | Out-File -FilePath request.json -Encoding utf8
```

Then execute the following command to send your REST request:


```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
    -Method POST `
    -Headers $headers `
    -ContentType: "application/json; charset=utf-8" `
    -InFile request.json `
    -Uri "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-3.5-flash:generateContent" | Select-Object -Expand Content
```

You should receive a JSON response similar to the following.

**Response**

```
{
  "candidates": [\
    {\
      "content": {\
        "role": "model",\
        "parts": [\
          {\
            "text": "This video is a commercial for Google Photos, featuring animals taking selfies\
              with the Google Photos app. The commercial plays on the popularity of media in which\
              animals act like humans, especially their use of technology. The commercial also\
              highlights the app's ability to automatically back up photos."\
          }\
        ]\
      },\
      "finishReason": "STOP",\
      "safetyRatings": [\
        {\
          "category": "HARM_CATEGORY_HATE_SPEECH",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.053601142,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.053799648\
        },\
        {\
          "category": "HARM_CATEGORY_DANGEROUS_CONTENT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.06278921,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.07850098\
        },\
        {\
          "category": "HARM_CATEGORY_HARASSMENT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.090253234,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.058453236\
        },\
        {\
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.1647851,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.09285216\
        }\
      ]\
    }\
  ],
  "usageMetadata": {
    "promptTokenCount": 28916,
    "candidatesTokenCount": 61,
    "totalTokenCount": 28977
  }
}
```



Note the following in the URL for this sample:

- Use the
[`generateContent`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.publishers.models/generateContent)
method to request that the response is returned after it's fully generated.
To reduce the perception of latency to a human audience, stream the response as it's being
generated by using the
[`streamGenerateContent`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.publishers.models/streamGenerateContent)
method.

- The multimodal model ID is located at the end of the URL before the method
(for example, `gemini-3.5-flash`). This sample might support other
models as well.

- When you use a regional API endpoint (for example, `us-central1`), the region from the endpoint URL determines where the request is processed. Any conflicting location in the resource path is ignored.

### Video with audio

The following shows you how to summarize a video file with audio and return
chapters with timestamps. This sample works with all Gemini multimodal
models that support video with audio.

[Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#python-google-gen-ai-sdk)[REST](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#rest)[Console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#console)More

#### Install

```
pip install --upgrade google-genai
```

To learn more, see the
[SDK reference documentation](https://googleapis.github.io/python-genai/).


Set environment variables to use the Google Gen AI SDK with Vertex AI:

```
# Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values
# with appropriate values for your project.
export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_ENTERPRISE=True
```

```
from google import genai
from google.genai.types import HttpOptions, Part

client = genai.Client(http_options=HttpOptions(api_version="v1"))
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[\
        Part.from_uri(\
            file_uri="gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",\
            mime_type="video/mp4",\
        ),\
        "What is in the video?",\
    ],
)
print(response.text)
# Example response:
# The video shows several people surfing in an ocean with a coastline in the background. The camera ...
```

After you set up your environment, you can use REST to test a text prompt. The
following sample sends a request to the publisher model endpoint.

Before using any of the request data,
make the following replacements:

- `PROJECT_ID`: .
- `FILE_URI`:
The URI or URL of the file to include in the prompt. Acceptable values include the following:



  - **Cloud Storage bucket URI:** The object must either be publicly readable or reside in
     the same Google Cloud project that's sending the request.
  - **HTTP URL:** The file URL must be publicly readable. You can specify one video file, one
     audio file, and up to 10 image files per request. Audio files, video files, and documents can't
     exceed 15 MB.
  - **YouTube video URL:** The YouTube video must be either owned by the account that you used
     to sign in to the Google Cloud console or be public. Only one YouTube video URL is supported per
     request.

When specifying a `fileURI`, you must also specify the media type
(`mimeType`) of the file. If VPC Service Controls is enabled, specifying a media file
URL for `fileURI` is not supported.

If you don't have a video file in Cloud Storage, then you can use the following
publicly available file:
`gs://cloud-samples-data/generative-ai/video/pixel8.mp4` with a mime type of
`video/mp4`. To view this video,
[open the sample MP4](https://storage.googleapis.com/cloud-samples-data/generative-ai/video/pixel8.mp4)
file.


- `MIME_TYPE`:
The media type of the file specified in the `data` or `fileUri`
fields. Acceptable values include the following:

**Click to expand MIME types**


  - `application/pdf`
  - `audio/mpeg`
  - `audio/mp3`
  - `audio/wav`
  - `image/png`
  - `image/jpeg`
  - `image/webp`
  - `text/plain`
  - `video/mov`
  - `video/mpeg`
  - `video/mp4`
  - `video/mpg`
  - `video/avi`
  - `video/wmv`
  - `video/mpegps`
  - `video/flv`

- ```
TEXT
```


The text instructions to include in the prompt.
For example,
`Provide a description of the video. The description should also contain anything
        important which people say in the video.`

To send your request, choose one of these options:

[curl](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#curl)[PowerShell](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#powershell)More

Save the request body in a file named `request.json`.
Run the following command in the terminal to create or overwrite
this file in the current directory:


```
cat > request.json << 'EOF'
{
"contents": {
    "role": "USER",
    "parts": [\
      {\
        "fileData": {\
          "fileUri": "FILE_URI",\
          "mimeType": "MIME_TYPE"\
        }\
      },\
      {\
        "text": "TEXT"\
      }\
    ]
}
}
EOF
```

Then execute the following command to send your REST request:


```
curl -X POST \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     -d @request.json \
     "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-2.5-flash:generateContent"
```

Save the request body in a file named `request.json`.
Run the following command in the terminal to create or overwrite
this file in the current directory:


```
@'
{
"contents": {
    "role": "USER",
    "parts": [\
      {\
        "fileData": {\
          "fileUri": "FILE_URI",\
          "mimeType": "MIME_TYPE"\
        }\
      },\
      {\
        "text": "TEXT"\
      }\
    ]
}
}
'@  | Out-File -FilePath request.json -Encoding utf8
```

Then execute the following command to send your REST request:


```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
    -Method POST `
    -Headers $headers `
    -ContentType: "application/json; charset=utf-8" `
    -InFile request.json `
    -Uri "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-2.5-flash:generateContent" | Select-Object -Expand Content
```

You should receive a JSON response similar to the following.

**Response**

```
{
"candidates": [\
    {\
      "content": {\
        "role": "model",\
        "parts": [\
          {\
            "text": "The video opens with a shot of a train traveling over a bridge in the night. \n\
              \nThe scene changes to a woman walking in the streets of Tokyo. She says "My name is\
              Saeko. I am a photographer in Tokyo. Tokyo has many faces. The city at night\
              is totally different from what you see during the day. The new Pixel has a feature\
              called "Video Boost". In low light, it activates "Night Sight" to make the quality\
              even better." \n\nShe then uses her phone to take several photos of different parts of\
              the city including a street with a lot of shops, a small alleyway, and a small\
              restaurant. She says "Sancha is where I used to live when I first moved to Tokyo. I\
              have a lot of great memories here. Oh, I like this." \n\nShe smiles and says\
              "Beautiful".\n\nThe video ends with the woman standing in a different part of the\
              city. She says "Next, I came to Shibuya." The scene shows the famous Shibuya crossing\
              in the night. \n\nThe video features a woman showcasing the camera features of the\
              Google Pixel phone while walking around the streets of Tokyo. She mentions "Night\
              Sight" and "Video Boost" features. \n"\
          }\
        ]\
      },\
      "finishReason": "STOP",\
      "safetyRatings": [\
        {\
          "category": "HARM_CATEGORY_HATE_SPEECH",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.053601142,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.053799648\
        },\
        {\
          "category": "HARM_CATEGORY_DANGEROUS_CONTENT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.06278921,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.07850098\
        },\
        {\
          "category": "HARM_CATEGORY_HARASSMENT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.090253234,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.058453236\
        },\
        {\
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.1647851,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.09285216\
        }\
      ]\
    }\
],
"usageMetadata": {
    "promptTokenCount": 28916,
    "candidatesTokenCount": 61,
    "totalTokenCount": 28977
}
}
```



Note the following in the URL for this sample:

- Use the
[`generateContent`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.publishers.models/generateContent)
method to request that the response is returned after it's fully generated.
To reduce the perception of latency to a human audience, stream the response as it's being
generated by using the
[`streamGenerateContent`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.publishers.models/streamGenerateContent)
method.

- The multimodal model ID is located at the end of the URL before the method
(for example, `gemini-3.5-flash`). This sample might support other
models as well.

- When you use a regional API endpoint (for example, `us-central1`), the region from the endpoint URL determines where the request is processed. Any conflicting location in the resource path is ignored.







To send a multimodal prompt by using the Google Cloud console, do the
following:

01. In the Agent Platform section of the Google Cloud console, go to
     the **Agent Studio** page.

    [Go to Agent Studio](https://console.cloud.google.com/agent-platform/generative/multimodal)

02. Click **Create prompt**.

03. Optional: Configure the model and parameters:

    - **Model**: Select a model.
04. Optional: To configure advanced parameters, click **Advanced** and
     configure as follows:


    **Click to expand advanced configurations**

    - **Top-K**: Use the slider or textbox to enter a value for top-K.


      Top-K changes how the model selects tokens for output. A top-K of
      `1` means the next selected token is the most probable among all
      tokens in the model's vocabulary (also called greedy decoding), while a top-K of
      `3` means that the next token is selected from among the three most
      probable tokens by using temperature.


      For each token selection step, the top-K tokens with the highest
      probabilities are sampled. Then tokens are further filtered based on top-P with
      the final token selected using temperature sampling.

      Specify a lower value for less random responses and a higher value for more
      random responses.

    - **Top-P**: Use the slider or textbox to enter a value for top-P.
       Tokens are selected from most probable to the least until the sum of their
       probabilities equals the value of top-P. For the least variable results,
       set top-P to `0`.
    - **Max responses**: Use the slider or textbox to enter a value for
       the number of responses to generate.
    - **Streaming responses**: Enable to print responses as they're
       generated.
    - **Safety filter threshold**: Select the threshold of how likely you
       are to see responses that could be harmful.
    - **Enable Grounding**: Grounding isn't supported for multimodal
       prompts.
    - **Region**: Select the region that you want to use.
    - **Temperature**: Use the slider or textbox to enter a value for
       temperature.





      ```

      The temperature is used for sampling during response generation, which occurs when topP
      and topK are applied. Temperature controls the degree of randomness in token selection.
      Lower temperatures are good for prompts that require a less open-ended or creative response, while
      higher temperatures can lead to more diverse or creative results. A temperature of 0
      means that the highest probability tokens are always selected. In this case, responses for a given
      prompt are mostly deterministic, but a small amount of variation is still possible.

      If the model returns a response that's too generic, too short, or the model gives a fallback
      response, try increasing the temperature. If the model enters infinite generation, increasing the
      temperature to at least 0.1 may lead to improved results.
       1.0 is the
      recommended starting value for temperature.
      </li>
        <li>**Output token limit**: Use the slider or textbox to enter a value for
          the max output limit.


      Maximum number of tokens that can be generated in the response. A token is
      approximately four characters. 100 tokens correspond to roughly 60-80 words.

      Specify a lower value for shorter responses and a higher value for potentially longer
      responses.

      </li>
        <li>**Add stop sequence**: Optional. Enter a stop sequence, which is a
          series of characters that includes spaces. If the model encounters a
          stop sequence, the response generation stops. The stop sequence isn't
          included in the response, and you can add up to five stop sequences.</li>
      </ul>
      ```


05. Click **Insert Media**, and select a source for your file.



    [Upload](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#upload)[By URL](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#by-url)[YouTube](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#youtube)[Cloud Storage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#cloud-storage)[Google Drive](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#google-drive)More







    Select the file that you want to upload and click **Open**.



    Enter the URL of the file that you want to use and click **Insert**.











    Enter the URL of the YouTube video that you want to use and click
    **Insert**.



    You can use any public video or a video that's owned by the account that
    you used to sign in to the Google Cloud console.



    Select the bucket and then the file from the bucket that
    you want to import and click **Select**.



    1. Choose an account and give consent to
       Agent Studio to access your account the first
       time you select this option. You can upload multiple files that
       have a total size of up to 10 MB. A single file can't exceed
       7 MB.
    2. Click the file that you want to add.
    3. Click **Select**.

       The file thumbnail displays in the **Prompt** pane. The total
       number of tokens also displays. If your prompt data exceeds the
       [token limit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models), the
       tokens are truncated and aren't included in processing your data.


06. Enter your text prompt in the **Prompt** pane.

07. Optional: To view the **Token ID to text** and **Token IDs**, click the
     **tokens count** in the **Prompt** pane.

08. Click **Submit**.

09. Optional: To save your prompt to **My prompts**, click save\_alt **Save**.

10. Optional: To get the Python code or a curl command for your prompt, click
     code **Build with code > Get code**.




## Customize video processing

You can customize video processing in the Gemini for Google Cloud API by setting
clipping intervals or providing custom frame rate sampling.

### Set clipping intervals

You can clip videos by specifying
[`videoMetadata`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Content#VideoMetadata)
with start and end offsets.

### Set a custom frame rate

You can set custom frame rate sampling by passing an `fps` argument to
`videoMetadata`.

By default, 1 frame per second (FPS) is sampled from the video. You might want
to set low FPS (< 1) for long videos. This is especially useful for mostly
static videos (for example, lectures). If you want to capture more details in
rapidly changing visuals, consider setting a higher FPS value.

## Agentic video understanding

**Agentic video understanding** allows the model to dynamically navigate
video content instead of having to process every frame statically.
Agentic video understanding uses fewer tokens than static processing
and can improve response quality. This can result in lower costs and
faster responses for long-form video workloads.

You can use agentic video understanding and static processing for
different videos in the same request. For example, if you have long-form videos
(such as an hour-long lecture) and short-form video content (like YouTube
Shorts), you can use agentic video understanding on the long-form
videos to target contextually relevant information and static processing on the
short-form video content for frame-level precision.

Video context must be preserved across turns in a conversation. When using
agentic processing with the GenerateContent API, the response may include opaque
steps (`step_list`) that encode video context. You must include these steps in
the following turn to preserve context. If you omit them, the video context is
lost and the model cannot answer follow-up questions about the video without
reprocessing it.

### Supported models and file types

Agentic video understanding is supported in the following
models:

**Click to expand supported models**

- [Gemini 3.8 Flash Cyber](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash-cyber)
- [Gemini 3.7 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash)
- [Gemini 3.6 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-6-flash)
- [Gemini 3.5 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash-lite)

You can use the following sources when using agentic video understanding:

- YouTube URLs
- Cloud Storage URIs
- Inline Base64 encoded video files

### When to use agentic video understanding

If your use case is similar to one of the following examples, you may want to
use agentic video understanding:

- **Long-form video Q&A**: Ask questions about hour-long lectures, meetings,
  or video tutorials.
- **Multi-video comparison**: Compare multiple videos in a single request. You
  can use different processing modes for each video within the same request.
- **Video-powered agents**: Build agents that reason over video content with
  multi-turn conversation support. Video context is preserved across turns
  without reprocessing.
- **Cost optimization for video workloads**: Dramatically reduce token
  consumption for video-heavy applications.

### Use agentic video understanding

You can use agentic video understanding using the GenerateContent API. Use [`media_processing =\\
"AGENTIC"`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference#parts) in the request:

[Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#python)[REST](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#rest)More

```
from google import genai
from google.genai import types

client = genai.Client()

# Example: Controlling media_processing explicitly
video_part = types.Part(
file_data=types.FileData(
      file_uri="gs://my-bucket-name/sports_clip.mp4",
      mime_type="video/mp4",
),
media_processing="agentic" # Options: "agentic", "static"
)

response = client.models.generate_content(
model="gemini-3.7-flash",
contents=[\
      video_part,\
      "Analyze the player's footwork right before the shot."\
]
)
print(response.text)
```

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
https://aiplatform.googleapis.com/v1beta1/projects/YOUR_PROJECT_ID/locations/global/publishers/google/models/gemini-3.7-flash:generateContent \
-d '{
"contents": [\
    {\
      "role": "USER",\
      "parts": [\
        {\
          "fileData": {\
            "mimeType": "video/mp4",\
            "fileUri": "gs://my-bucket/lecture.mp4"\
          },\
          "mediaProcessing": "AGENTIC"\
        },\
        {\
          "text": "Summarize the key takeaways."\
        }\
      ]\
    }\
],
"generationConfig": {
    "thinkingLevel": "MEDIUM"
}
}'
```

Agentic video understanding is set to `STATIC` or disabled by default for
all supported models.

## Adjust media resolution

You can adjust
[`MediaResolution`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/MediaResolution)
to process your videos with fewer tokens.

## Set optional model parameters

Each model has a set of optional parameters that you can set. For more
information, see [Content generation parameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/content-generation-parameters).

## Video tokenization

With Gemini 3, video tokenization uses a variable sequence length,
which replaces the Pan and Scan method used in previous models for better
quality and latency.

You can specify a media resolution for video inputs, which affects
how videos are tokenized and how many tokens are used for each video.
You can set `media_resolution` in `generationConfig` to apply to all media in
the request, or set it for individual media parts, which will override the
top-level setting. The default resolution for videos is 70 tokens per frame.

The following resolutions are available for Gemini 3 models:

- `MEDIA_RESOLUTION_HIGH`: 280 tokens per frame
- `MEDIA_RESOLUTION_MEDIUM`: 70 tokens per frame
- `MEDIA_RESOLUTION_LOW`: 70 tokens per frame
- `MEDIA_RESOLUTION_UNSPECIFIED`: 70 tokens per frame (default)

For models earlier than Gemini 3, each frame is tokenized at 258
tokens per frame for default resolution, or 66 tokens per frame for low
resolution.

This code sample demonstrates how to adjust `media_resolution`:

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
model="gemini-3.1-pro-preview",
contents=[\
      types.Part(\
          file_data=types.FileData(\
              file_uri="gs://cloud-samples-data/generative-ai/image/a-man-and-a-dog.png",\
              mime_type="image/jpeg",\
          ),\
          media_resolution=types.PartMediaResolution(\
              level=types.PartMediaResolutionLevel.MEDIA_RESOLUTION_HIGH\
          ),\
      ),\
      Part(\
          file_data=types.FileData(\
              file_uri="gs://cloud-samples-data/generative-ai/video/behind_the_scenes_pixel.mp4",\
              mime_type="video/mp4",\
          ),\
          media_resolution=types.PartMediaResolution(\
              level=types.PartMediaResolutionLevel.MEDIA_RESOLUTION_LOW\
          ),\
      ),\
      "When does the image appear in the video? What is the context?",\
],
)
print(response.text)
```

## Best practices

When using video, use the following best practices and information for the
best results:

- If your prompt contains a single video, place the video before the text
   prompt.

- If you require timestamp localization in a video with audio, ask the model
   to generate timestamps that follow the format as described in "Timestamp
   format".


For Gemini 3 models, also consider the following:

- Use a higher Frame Per Second (FPS) sampling rate for videos requiring
  granular temporal analysis, such as fast-action understanding or high-speed
  motion tracking.

## Limitations

While Gemini multimodal models are powerful in many multimodal use
cases, it's important to understand the limitations of the models:

- **Content moderation**: The models refuse to provide answers
   on videos that violate our safety policies.

- **Non-speech sound recognition**: The models that support
   audio might make mistakes recognizing sound that's not speech.


## Technical details about videos

- **File API processing**: When using the File API, videos are sampled at 1
  frame per second (FPS) and audio is processed at 1Kbps (single channel).
  Timestamps are added every second.

  - These rates are subject to change in the future for improvements in
    inference.
- **Timestamp format**: When referring to specific moments in a video within
  your prompt, the timestamp format depends on your video's frame per second
  (FPS) sampling rate:

  - **For sampling rates at 1 FPS or below**: Use the `MM:SS` format, where
    the first two digits represent minutes and the last two digits represent
    seconds. If you have offsets that are greater than 1 hour, use the
    `H:MM:SS` format.

  - **For sampling rates above 1 FPS**: Use the `MM:SS.sss` format, or, if
    you have offsets that are greater than 1 hour, use the
    `H:MM:SS.sss` format, described as follows:

    - The first digit represents the hour.
    - The second two digits represent minutes.
    - The third two digits represent seconds.
    - The final three digits represent subseconds.
- **Best practices**:

  - Use only one video per prompt request for optimal results.

  - If combining text and a single video, place the text prompt _after_ the
    video part in the `contents` array.

  - Be aware that fast action sequences might lose detail due to the 1 FPS
    sampling rate. Consider slowing down such clips if necessary.

## What's next

- Start building with Gemini multimodal models - new customers [get $300 in free Google Cloud credits](https://console.cloud.google.com/freetrial?redirectPath=/vertex-ai/model-garden) to explore what they can do with Gemini.
- Learn how to [send chat prompt requests](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/send-chat-prompts-gemini).
- Learn about [responsible AI best practices and Agent Platform's safety filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai).



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Hard to understand","hardToUnderstand","thumb-down"\],\["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"\],\["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-10-01 UTC."\],\[\],\[\]\]