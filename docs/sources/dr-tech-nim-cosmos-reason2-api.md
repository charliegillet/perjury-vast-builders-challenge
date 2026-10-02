[Skip to main content](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html#main-content)

![country_code](https://www.nvidia.com/content/dam/1x1-00000000.png)

Back to top`⌘` + `K`

[![NVIDIA NIM for Vision Language Models (VLMs) - Home](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg)![NVIDIA NIM for Vision Language Models (VLMs) - Home](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg)\\
NVIDIA NIM for Vision Language Models (VLMs)](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/index.html)

Choose version

LightDarkSystem Settings

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Query the Cosmos Reason2 API [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#query-the-cosmos-reason2-api "Link to this heading")

This model is available in two sizes: 2B and 8B. This guide uses the 2B version
as an example, but the 8B version is easily adaptable as shown in the following example.

For more information on this model, refer to the model cards:

- [Cosmos Reason2 2B model card](https://huggingface.co/nvidia/Cosmos-Reason2-2B)

- [Cosmos Reason2 8B model card](https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard)


## Launch NIM [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#launch-nim "Link to this heading")

Make sure you complete the steps in [Get Started with NIM](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/getting-started.html#vlm-getting-started)
before you launch the NIM.

The following command launches a [Docker container](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-2b)
for the 2B version of this specific model:

Note

NIM initialization may take several minutes as it compiles the model for optimal performance.

```
# Choose a container name for bookkeeping
export CONTAINER_NAME="nvidia-cosmos-reason2-2b" # or "nvidia-cosmos-reason2-8b"

# The container name from the previous ngc registry image list command
Repository="cosmos-reason2-2b" # or "cosmos-reason2-8b"
Latest_Tag="1.7.0"

# Choose a VLM NIM Image from NGC
export IMG_NAME="nvcr.io/nim/nvidia/${Repository}:${Latest_Tag}"

# Choose a path on your system to cache the downloaded models
export LOCAL_NIM_CACHE=~/.cache/nim
mkdir -p "$LOCAL_NIM_CACHE"

# Start the VLM NIM
docker run -it --rm --name=$CONTAINER_NAME \
--runtime=nvidia \
--gpus all \
--shm-size=32GB \
-e NGC_API_KEY=$NGC_API_KEY \
-v "$LOCAL_NIM_CACHE:/opt/nim/.cache" \
-u $(id -u) \
-p 8000:8000 \
$IMG_NAME
```

Copy to clipboard

Note

The `-u $(id -u)` option in the preceding `docker run` command ensures that the UID in the spawned
container is the same as the user’s on the host. It is usually recommended if the `$LOCAL_NIM_CACHE`
path on the host has permissions that forbid other users from writing to it.

Refer to the [Docker container](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b) for the 8B
version of this specific model.

```
export CONTAINER_NAME="nvidia-cosmos-reason2-8b"
export REPOSITORY="cosmos-reason2-8b"
export IMG_NAME="nvcr.io/nim/nvidia/${REPOSITORY}:${Latest_Tag}"

docker run -it --rm --name=$CONTAINER_NAME \
--runtime=nvidia \
--gpus all \
--shm-size=32GB \
-e NGC_API_KEY=$NGC_API_KEY \
-v "$LOCAL_NIM_CACHE:/opt/nim/.cache" \
-u $(id -u) \
-p 8000:8000 \
$IMG_NAME
```

Copy to clipboard

## OpenAI Chat Completion Request [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#openai-chat-completion-request "Link to this heading")

The Chat Completions endpoint is typically used with `chat` or `instruct`
tuned models designed for a conversational approach. Using the endpoint, prompts
are sent in the form of messages with roles and content. To stream the result,
set `"stream": true`.

Important

Update the model name according to the model you are running.

Note

The following examples use `max_tokens` to terminate generation at a
reasonable length. Reasoning examples use a higher upper bound to
accommodate longer chain-of-thought outputs.

Query the `nvidia/cosmos-reason2-2b` model using an image URL from the command line:

```
curl -X 'POST' \
'http://127.0.0.1:8000/v1/chat/completions' \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "model": "nvidia/cosmos-reason2-2b",
        "messages": [\
            {\
                "role": "system",\
                "content": "You are a helpful assistant."\
            },\
            {\
                "role": "user",\
                "content": [\
                    {\
                        "type": "image_url",\
                        "image_url":\
                            {\
                                "url": "https://assets.ngc.nvidia.com/products/api-catalog/phi-3-5-vision/example1b.jpg"\
                            }\
                    },\
                    {\
                        "type": "text",\
                        "text": "What is in this image?"\
                    }\
                ]\
            }\
        ],
        "max_tokens": 256,
        "stream": false
    }'
```

Copy to clipboard

You can include `"stream": true` in the request body for streaming responses.

Alternatively, you can use the [OpenAI Python SDK library](https://github.com/openai/openai-python)

```
pip install -U openai
```

Copy to clipboard

Run the client and query the Chat Completions API:

```
from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="not-used")
messages = [\
    {\
        "role": "system",\
        "content": "You are a helpful assistant."\
    },\
    {\
        "role": "user",\
        "content": [\
            {\
                "type": "image_url",\
                "image_url": {\
                    "url": "https://assets.ngc.nvidia.com/products/api-catalog/phi-3-5-vision/example1b.jpg"\
                }\
            },\
            {\
                "type": "text",\
                "text": "What is in this image?"\
            }\
        ]\
    }\
]
chat_response = client.chat.completions.create(
    model="nvidia/cosmos-reason2-2b",
    messages=messages,
    max_tokens=256,
    stream=False,
)
assistant_message = chat_response.choices[0].message
print(assistant_message)
```

Copy to clipboard

The preceding code snippet can be adapted to handle streaming responses as follows:

```
# Code preceding `client.chat.completions.create` is the same.
stream = client.chat.completions.create(
    model="nvidia/cosmos-reason2-2b",
    messages=messages,
    max_tokens=256,
    # Take note of this param.
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        text = delta.content
        # Print immediately and without a newline to update the output as the response is
        # streamed in.
        print(text, end="", flush=True)
# Final newline.
print()
```

Copy to clipboard

### Passing Images [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#passing-images "Link to this heading")

NIM for VLMs follows the [OpenAI specification](https://platform.openai.com/docs/guides/vision) to pass images as part of the HTTP payload in a user message.

Important

Supported image formats are JPG, JPEG, and PNG.

**Public direct URL**

Passing a direct URL prompts the container to download the image at runtime.

```
{
    "type": "image_url",
    "image_url": {
        "url": "https://assets.ngc.nvidia.com/products/api-catalog/phi-3-5-vision/example1b.jpg"
    }
}
```

Copy to clipboard

**Base64 data**

Another option, which is useful for images that are not already hosted on the
web, is to Base64-encode the image bytes and send the data in the payload.

```
{
    "type": "image_url",
    "image_url": {
        "url": "data:image/jpeg;base64,SGVsbG8gZGVh...ciBmZWxsb3chIQ=="
    }
}
```

Copy to clipboard

To convert images to base64, you can use the `base64` command, or in Python:

```
with open("image.png", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()
```

Copy to clipboard

### Passing Videos [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#passing-videos "Link to this heading")

NIM for VLMs extends the [OpenAI specification](https://platform.openai.com/docs/guides/vision) to accept videos in the HTTP payload.
The format matches that of image payloads, but uses `video_url` instead of `image_url`.

**Public direct URL**

Passing a direct URL prompts the container to download the video at runtime.

```
{
    "type": "video_url",
    "video_url": {
        "url": "https://download.samplelib.com/mp4/sample-5s.mp4"
    }
}
```

Copy to clipboard

**Base64 data**

Another option, which is useful for videos that are not already hosted on the
web, is to Base64-encode the video bytes and send the data in the payload.

```
{
    "type": "video_url",
    "video_url": {
        "url": "data:video/mp4;base64,SGVsbG8gZGVh...ciBmZWxsb3chIQ=="
    }
}
```

Copy to clipboard

To convert videos to base64, you can use the `base64` command, or in Python:

```
with open("video.mp4", "rb") as f:
    video_b64 = base64.b64encode(f.read()).decode()
```

Copy to clipboard

**Pre-decoded Video Frames**

For scenarios where video is already decoded by upstream services, you can pass pre-decoded frames directly using `video_frames`. Unlike sending frames as separate `image_url` entries (which processes each frame independently), `video_frames` preserves temporal relationships between frames and uses fewer tokens.

```
{
    "type": "video_frames",
    "video_frames": [\
        "data:image/jpeg;base64,<frame1_base64>",\
        "data:image/jpeg;base64,<frame2_base64>",\
        "data:image/jpeg;base64,<frame3_base64>"\
    ]
}
```

Copy to clipboard

### Sampling and Preprocessing Parameters [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#sampling-and-preprocessing-parameters "Link to this heading")

Use the following OpenAI API extensions to control image and video preprocessing
at request time. Two separate parameter fields are used for different aspects of preprocessing:

- `media_io_kwargs`: Controls **temporal sampling** — how many frames to extract from a video (using `fps` or `num_frames`). This affects the number of frames the model sees. Does not apply to image inputs.

- `mm_processor_kwargs`: Controls **total pixel budget** — the minimum and maximum number of pixels across all sampled frames combined (using `shortest_edge` and `longest_edge`). More frames means fewer pixels per frame. Applies to both video and image inputs.


**Video sampling**

Control video frame sampling using the top-level `media_io_kwargs` API field.

Specify either `fps` or `num_frames`. These parameters are mutually exclusive — providing both will result in an error.

```
"media_io_kwargs": {"video": { "fps": 3.0 }}
```

Copy to clipboard

or

```
"media_io_kwargs": {"video": { "num_frames": 16 }}
```

Copy to clipboard

Sampling more frames improves accuracy but decreases performance. The default rate is 4.0 FPS, matching the training data.

Note

Specifying values of `fps` or `num_frames` higher than the actual values for a given video will result in a 400 error code.

Note

The value of `fps` or `num_frames` is directly correlated to the temporal resolution of the model’s outputs.
For example, at 2 FPS, timestamp precision in the generated output will be at best within +/- 0.25 seconds of
the true values.

**Video pixel count**

To balance accuracy and performance, you can specify `shortest_edge` and
`longest_edge` to control the size of frames after preprocessing. These
parameters specify the minimum and maximum number of pixels across the sampled
frames.

This is done using the top-level field `mm_processor_kwargs`:

```
"mm_processor_kwargs": {"size": { "shortest_edge": 1568, "longest_edge": 262144 }}
```

Copy to clipboard

Defaults are `shortest_edge=3136` and `longest_edge=12845056` per image.

Note

For video, Cosmos Reason2 applies `longest_edge` per temporal group of 2 frames,
so the effective default for video is `25690112` (2 × 12845056). The `longest_edge` value
controls the total pixel budget across all sampled frames — more frames means fewer pixels per frame.

Each patch of 32x32x2=2048 pixels maps to a multimodal input token. This model was tested to perform best with 16k multimodal tokens or less.

Note

`prompt_tokens` in the API response includes both text tokens (~100-150) and vision tokens.
Subtract text tokens for a more accurate vision token count. Frame dimensions are also rounded
to multiples of 28 pixels (patch alignment), which causes slight non-linearity in the ratio.

**Image frame size**

Image inputs accept the same size parameters:

```
"mm_processor_kwargs": {"size": { "shortest_edge": 1568, "longest_edge": 262144 }}
```

Copy to clipboard

Each patch of 32x32=1024 pixels, for each image, maps to a multimodal input token.
This model was tested to perform best with 16k multimodal tokens or less.

**OpenAI Python SDK**

Use the `extra_body` parameter to pass these parameters in the OpenAI Python SDK.

```
from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="not-used")
model = client.models.list().data[0].id

messages = [\
    {\
        "role": "system",\
        "content": "You are a helpful assistant."\
    },\
    {\
        "role": "user",\
        "content": [\
            {\
                "type": "video_url",\
                "video_url": {\
                    "url": "https://download.samplelib.com/mp4/sample-5s.mp4"\
                }\
            },\
            {\
                "type": "text",\
                "text": "What is in this video?"\
            }\
        ]\
    }\
]
chat_response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=1024,
    stream=False,
    extra_body={
        "mm_processor_kwargs": {"size": {"shortest_edge": 1568, "longest_edge": 262144}},
        # Alternatively, this can be:
        # "media_io_kwargs": {"video": {"num_frames": some_int}},
        "media_io_kwargs": {"video": {"fps": 1.0}},
    }
)
assistant_message = chat_response.choices[0].message
print(assistant_message)
```

Copy to clipboard

**Summary table**

The following table summarizes the parameters used in the preceding sample code:

| Name | Example | Default | Notes |
| --- | --- | --- | --- |
| Video FPS sampling | `"media_io_kwargs": {"video": {"fps": 3.0}}` | 4 FPS | - Higher FPS can enhance accuracy at the cost of more computation.<br>  <br>- Mutually exclusive with explicit number of frames. |
| Sampling \_N\_ frames in a video | `"media_io_kwargs": {"video": {"num_frames": 16}}` | N/A (default is FPS sampling, not fixed number of frames) | - A higher number of frames can enhance accuracy at the cost of more computation.<br>  <br>- Mutually exclusive with explicit FPS. |
| Minimum and maximum number of pixels for **videos** and **images** | `"mm_processor_kwargs": {"size": { "shortest_edge": 1568, "longest_edge": 262144 }}` | `shortest_edge=3136, longest_edge=12845056` | Higher resolutions can enhance accuracy at the cost of more computation. |

Preprocessing and sampling params [#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html#id1 "Link to this table")

### Efficient Video Sampling (EVS) [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#efficient-video-sampling-evs "Link to this heading")

Important

EVS is only supported for the 8B model. The 2B model does not support EVS.

The 8B model supports efficient video sampling (EVS) to reduce video processing
time and memory consumption. Control video frame processing efficiency using the
`NIM_VIDEO_PRUNING_RATE` environment variable:

```
# Only for 8B model
export CONTAINER_NAME="nvidia-cosmos-reason2-8b"
export IMG_NAME="nvcr.io/nim/nvidia/cosmos-reason2-8b:${Latest_Tag}"

docker run -it --rm --name=$CONTAINER_NAME \
--runtime=nvidia \
--gpus all \
--shm-size=32GB \
-e NGC_API_KEY=$NGC_API_KEY \
-e NIM_VIDEO_PRUNING_RATE=0.3 \
-v "$LOCAL_NIM_CACHE:/opt/nim/.cache" \
-u $(id -u) \
-p 8000:8000 \
$IMG_NAME
```

Copy to clipboard

- `NIM_VIDEO_PRUNING_RATE=0`: (Default) No frame pruning

- `NIM_VIDEO_PRUNING_RATE=0.3`: Prune 30% of frames for faster processing

- `NIM_VIDEO_PRUNING_RATE=0.7`: Prune 70% of frames for maximum speed


Higher pruning rates improve performance but may reduce video understanding quality.

## Reasoning [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#reasoning "Link to this heading")

To enable reasoning and encourage a chain-of-thought response, append the following to the user prompt:

```
Answer the question in the following format: <think>\nyour reasoning\n</think>\n\n<answer>\nyour answer\n</answer>.
```

Copy to clipboard

For example:

```
curl -X 'POST' \
'http://127.0.0.1:8000/v1/chat/completions' \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "model": "nvidia/cosmos-reason2-2b",
        "messages": [\
            {\
                "role": "system",\
                "content": "You are a helpful assistant."\
            },\
            {\
                "role": "user",\
                "content": [\
                    {\
                        "type": "image_url",\
                        "image_url":\
                            {\
                                "url": "https://assets.ngc.nvidia.com/products/api-catalog/phi-3-5-vision/example1b.jpg"\
                            }\
                    },\
                    {\
                        "type": "text",\
                        "text": "What is in this image? \nAnswer the question in the following format: <think>\nyour reasoning\n</think>\n\n<answer>\nyour answer\n</answer>."\
                    }\
                ]\
            }\
        ],
        "max_tokens": 4096
    }'
```

Copy to clipboard

## Synthetic Data Generation Critic [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#synthetic-data-generation-critic "Link to this heading")

The `cosmos-reason2` model can act as a critic for Synthetically
Generated Data (SDG) by evaluating adherence to physical laws, object
permanence, and the presence of anomalies.

```
from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="not-used")
model = client.models.list().data[0].id

_USER_PROMPT = """Approve or reject this generated video for inclusion in a dataset for physical world model AI training. It must perfectly adhere to physics, object permanence, and have no anomalies. Any issue or concern causes rejection.
Answer the question using the following format:

<think>
Your reasoning.
</think>

Write your final answer immediately after the </think> tag. Answer with Approve or Reject only."""
message = [\
    {"role": "system", "content": "You are a helpful assistant."},\
    {"role": "user", "content": [\
        {"type": "video_url", "video_url": {"url": "https://assets.ngc.nvidia.com/products/api-catalog/cosmos-reason1-7b/car_curb.mp4"}},\
        {"type": "text", "text": _USER_PROMPT},\
    ]},\
]

response = client.chat.completions.create(
    model=model,
    messages=message,
    max_tokens=4096,
    temperature=0.3,
    top_p=0.3,
    extra_body={"media_io_kwargs": {"video": {"fps": 4}}},
)

print(response.choices[0].message.content)
```

Copy to clipboard

## 2D Trajectory Creation [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#d-trajectory-creation "Link to this heading")

`cosmos-reason2` supports point coordinates on image inputs.
Pixel coordinates are normalized to a range of 0 to 1000. The origin is the
top-left corner. X increases to the right (horizontal axis), and Y increases
downward (vertical axis). The aspect ratio does not matter; each axis has
independent 0-1000 normalization (for example, 1920x1080).

```
from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="not-used")
model = client.models.list().data[0].id

_USER_PROMPT = """You are given the task "Move the left bottle to far right". Specify the 2D trajectory your end effector should follow in pixel space. Return the trajectory coordinates in JSON format like this: {"point_2d": [x, y], "label": "gripper trajectory"}.
Answer the question using the following format:

<think>
Your reasoning.
</think>

Write your final answer immediately after the </think> tag."""
message = [\
    {"role": "system", "content": "You are a helpful assistant."},\
    {"role": "user", "content": [\
        {"type": "image_url", "image_url": {"url": "https://assets.ngc.nvidia.com/products/api-catalog/cosmos-reason1-7b/critic_rejection_sampling.jpg"}},\
        {"type": "text", "text": _USER_PROMPT},\
    ]},\
]

response = client.chat.completions.create(
    model=model,
    messages=message,
    max_tokens=4096,
    temperature=0.3,
    top_p=0.3,
)

print(response.choices[0].message.content)
```

Copy to clipboard

## Text-only Queries [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#text-only-queries "Link to this heading")

VLMs like `nvidia/cosmos-reason2-2b` and
`nvidia/cosmos-reason2-8b` support text-only queries, functioning as standard LLMs.

Important

Text-only capability is not available for all VLMs. Refer to the model cards in [Support Matrix](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/support-matrix.html#vlm-support-matrix) for support on text-only queries.

```
curl -X 'POST' \
'http://127.0.0.1:8000/v1/chat/completions' \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "model": "nvidia/cosmos-reason2-2b",
        "messages": [\
            {\
                "role": "system",\
                "content": "You are a helpful assistant."\
            },\
            {\
                "role": "user",\
                "content": "Create a detailed itinerary for a week-long adventure trip through Southeast Asia."\
            }\
        ],
        "max_tokens": 4096
    }'
```

Copy to clipboard

Or using the OpenAI SDK:

```
from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="not-used")
model = client.models.list().data[0].id

messages = [\
    {\
        "role": "system",\
        "content": "You are a helpful assistant."\
    },\
    {\
        "role": "user",\
        "content": "Create a detailed itinerary for a week-long adventure trip through Southeast Asia."\
    }\
]
chat_response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=4096,
    stream=False,
)
assistant_message = chat_response.choices[0].message
print(assistant_message)
```

Copy to clipboard

## Bring Your Own Checkpoint (BYOC) EAGLE Support [\#](https://docs.nvidia.com/nim/vision-language-models/_1.7.0/1.7.0/examples/cosmos-reason2/api.html\#bring-your-own-checkpoint-byoc-eagle-support "Link to this heading")

You can train and use your own EAGLE speculative decoding heads with this model.
Refer to the [GitHub repository](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/speculative_decoding/recipes/train_eagle_head_cosmos_reason2.ipynb)
for instructions on how to create your custom EAGLE checkpoint.

To use your custom EAGLE checkpoint, organize your files as follows:

```
my-model/
├── config.json
├── generation_config.json
├── tokenizer.json
├── tokenizer_config.json
├── model.safetensors
├── model.safetensors.index.json
│
└── eagle/
    ├── config.json
    ├── model.safetensors
    └── generation_config.json
```

Copy to clipboard

Mount this directory as your model cache, and the NIM will automatically detect
and use the EAGLE speculative decoding weights.

On this page