[Skip to main content](https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html#main-content)

![country_code](https://www.nvidia.com/content/dam/1x1-00000000.png)

Back to top`⌘` + `K`

[![NVIDIA NIM Cosmos Embed1 - Home](https://docs.nvidia.com/nim/cosmos-embed1/latest/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg)![NVIDIA NIM Cosmos Embed1 - Home](https://docs.nvidia.com/nim/cosmos-embed1/latest/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg)\\
NVIDIA NIM Cosmos Embed1](https://docs.nvidia.com/nim/cosmos-embed1/latest/index.html)

1.1.0

[1.1.0](https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/api-reference.html) [1.0.0](https://docs.nvidia.com/nim/cosmos-embed1/1.0.0/api-reference.html)

LightDarkSystem Settings

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# API Reference [\#](https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html\#api-reference "Link to this heading")

For the full OpenAPI 3.1 schema, you can access the interactive
documentation or the raw JSON file:

- Interactive Docs: `http://<host>:8000/docs`

- OpenAPI JSON: `http://<host>:8000/openapi.json`


## Endpoints [\#](https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html\#endpoints "Link to this heading")

### POST /v1/embeddings [\#](https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html\#post-v1-embeddings "Link to this heading")

Generates embedding vectors for text or video inputs. This is the
primary inference endpoint.

**Request Body**

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `input` | string | array\[string\] | Yes |  |
| `request_type` | string | Yes |  | Specifies the<br>processing mode, which can<br>be `query`,<br>`bulk_text`,<br>or<br>`bulk_video`. |
| `model` | string | Yes |  | The ID of<br>the<br>embedding<br>model to<br>use, which currently must<br>be `nvidia/cosmos-embed1`. |
| `encoding_format` | string | No | `float` | The format<br>for the<br>returned<br>embeddings, which can be<br>`float` or<br>`base64`. |

**Input String Formats**

The input field accepts the following formats:

- **Plain Text**: “A sentence to be embedded.”

- **Base64-Encoded Video**: “ [data:video/mp4;base64](data:video/mp4;base64),<base64-encoded-video-data>” (`query` only)

- **Presigned URL for Video**: “ [data:video/mp4;presigned\_url,https://your-url/video.mp4](data:video/mp4;presigned_url,https://your-url/video.mp4)”
(for `bulk_video` and `query` modes).

- **Video Frames (Presigned URLs)**: “ [data:video\_frames/jpg;presigned\_url](data:video_frames/jpg;presigned_url),{<frame\_url\_0>,<frame\_url\_1>,<frame\_url\_2>,<frame\_url\_3>,<frame\_url\_4>,<frame\_url\_5>,<frame\_url\_6>,<frame\_url\_7>}”
(for `bulk_video` and `query` modes).

- **Video Frames (Base64)**: “ [data:video\_frames/jpg;base64](data:video_frames/jpg;base64),{<frame\_0\_b64>,<frame\_1\_b64>,<frame\_2\_b64>,<frame\_3\_b64>,<frame\_4\_b64>,<frame\_5\_b64>,<frame\_6\_b64>,<frame\_7\_b64>}”
(for `bulk_video` and `query` modes).


**Notes and constraints**

- `query` supports a single input item (text, video, or `video_frames`).

- `bulk_text` supports up to 64 plain-text strings per request.

- `bulk_video` supports up to 64 items, where each item must be one of the following:

  - `data:video/<type>;presigned_url,<url>`

  - `data:video_frames/<type>;presigned_url,{...}` or `data:video_frames/<type>;base64,{...}`
- `video_frames` requires _exactly 8 frames_ per item.

- Maximum inputs per request: 64 items for `bulk_text` and `bulk_video` modes

- Recommended video duration: 15 seconds

- Maximum recommended video duration: 1-2 minutes; no strict maximum is enforced by the NIM.

- Supported codecs depend on the runtime decode stack (PyNvVideoCodec 2.0.3 / NVDEC) and the host GPU/driver; common codecs include H.264, HEVC, AV1, VP8, VP9, VC1, MPEG4, MPEG2, and MPEG1.

- Base64-encoded _full videos_ are accepted only in `query` mode.


**Text Query Payload**

```
{
"input": "A fluffy white cat basking in the sun.",
"model": "nvidia/cosmos-embed1",
"request_type": "query"
}
```

Copy to clipboard

**Bulk Text Payload**

```
{
"input": [\
  "This is the first sentence.",\
  "Here is a second one for batch processing."\
],
"model": "nvidia/cosmos-embed1",
"request_type": "bulk_text"
}
```

Copy to clipboard

**Bulk Video Payload**

```
{
"input": [\
  "data:video/webm;presigned_url,https://upload.wikimedia.org/wikipedia/commons/3/3d/Branko_Paukovic%2C_javelin_throw.webm",\
  "data:video/webm;presigned_url,https://upload.wikimedia.org/wikipedia/commons/3/3d/Branko_Paukovic%2C_javelin_throw.webm"\
],
"model": "nvidia/cosmos-embed1",
"request_type": "bulk_video"
}
```

Copy to clipboard

**Video Frames Payload (Query)**

```
{
"input": "data:video_frames/jpg;presigned_url,{<frame_url_0>,<frame_url_1>,<frame_url_2>,<frame_url_3>,<frame_url_4>,<frame_url_5>,<frame_url_6>,<frame_url_7>}",
"model": "nvidia/cosmos-embed1",
"request_type": "query"
}
```

Copy to clipboard

**Response Body**

The response is a JSON object containing the generated embeddings and
usage statistics.

| Parameter | Type | Description |
| --- | --- | --- |
| object | string | The type of object, always list |
| data | array\[object\] | An array of embedding objects |
| model | string | The model used for the request (e.g.<br>`nvidia/cosmos-embed1`) |
| usage | object | An object containing token and video<br>counts |

**Embedding Object**

| Parameter | Type | Description |
| --- | --- | --- |
| object | string | The type of object, always embedding. |
| index | integer | The index of this embedding in the data<br>array |
| embedding | array\[float\] | The embedding vector |

**Usage Object**

| Parameter | Type | Description |
| --- | --- | --- |
| num\_videos | integer | Number of videos processed in the<br>request. |
| prompt\_tokens | integer | Number of text tokens in the prompt. |
| total\_tokens | integer | Total tokens processed. |

**Example Response**

```
{
"object": "list",
"data": [\
    {\
    "object": "embedding",\
    "index": 0,\
"embedding": [\
    0.0123456789,\
    -0.0987654321\
    ]\
}\
],
"model": "nvidia/cosmos-embed1",
"usage": {
    "num_videos": 0,
    "prompt_tokens": 10,
    "total_tokens": 10
}
}
```

Copy to clipboard

### GET /v1/health/ready [\#](https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html\#get-v1-health-ready "Link to this heading")

Checks if the service is ready to accept inference requests.

**Example Response**

```
{
"object": "health.response",
"message": "NIM Service is ready"
}
```

Copy to clipboard

### GET /v1/health/live [\#](https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html\#get-v1-health-live "Link to this heading")

Checks if the service is running (live). It may not yet be ready for
inference.

**Example Response**

```
{
"object": "health.response",
"message": "NIM Service is live"
}
```

Copy to clipboard

### GET /health/metrics [\#](https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html\#get-health-metrics "Link to this heading")

Returns a JSON snapshot of service metrics (requests, latency percentiles, throughput, errors, and business counters). Latency values are in seconds.

This endpoint complements the Prometheus-compatible metrics at `GET /v1/metrics`.

**Example Response**

```
{
  "service": {
    "uptime_seconds": 12.3,
    "start_time": 1730000000.0
  },
  "requests": {
    "total": 10,
    "success": 9,
    "error": 1,
    "success_rate_percent": 90.0,
    "error_rate_percent": 10.0,
    "in_flight": 0,
    "in_flight_by_type": {
      "query": 0,
      "bulk_text": 0,
      "bulk_video": 0
    }
  },
  "requests_by_type": {
    "success": {
      "query": 8,
      "bulk_video": 1
    },
    "error": {
      "bulk_video": 1
    }
  },
  "requests_by_input_type": {
    "total": {
      "text": 8,
      "video_presigned_url": 2
    },
    "success": {
      "text": 8,
      "video_presigned_url": 1
    },
    "error": {
      "video_presigned_url": 1
    }
  },
  "encoding_format_distribution": {
    "float": 10
  },
  "status_codes": {
    "200": 9,
    "400": 1
  },
  "errors_by_classification": {
    "download_error": 1
  },
  "latency": {
    "p50": 0.12,
    "p95": 0.30,
    "p99": 0.35,
    "p99.9": 0.35,
    "min": 0.05,
    "max": 0.40,
    "avg": 0.15
  },
  "latency_by_type": {
    "query": {
      "p50": 0.10,
      "p95": 0.20,
      "p99": 0.25,
      "avg": 0.12,
      "count": 8
    },
    "bulk_video": {
      "p50": 0.40,
      "p95": 0.40,
      "p99": 0.40,
      "avg": 0.40,
      "count": 1
    }
  },
  "latency_by_input_type": {
    "text": {
      "p50": 0.10,
      "p95": 0.20,
      "p99": 0.25,
      "avg": 0.12,
      "count": 8
    },
    "video_presigned_url": {
      "p50": 0.40,
      "p95": 0.40,
      "p99": 0.40,
      "avg": 0.40,
      "count": 1
    }
  },
  "error_latency": {
    "p50": 0.08,
    "p95": 0.08,
    "p99": 0.08,
    "min": 0.08,
    "max": 0.08,
    "avg": 0.08,
    "count": 1
  },
  "error_latency_by_type": {
    "bulk_video": {
      "p50": 0.08,
      "p95": 0.08,
      "p99": 0.08,
      "avg": 0.08,
      "count": 1
    }
  },
  "error_latency_by_input_type": {
    "video_presigned_url": {
      "p50": 0.08,
      "p95": 0.08,
      "p99": 0.08,
      "avg": 0.08,
      "count": 1
    }
  },
  "throughput": {
    "requests_per_minute": {
      "1min": 60.0,
      "5min": 12.0,
      "15min": 4.0
    }
  },
  "business_metrics": {
    "total_embeddings": 10,
    "total_tokens": 100,
    "total_videos": 2,
    "total_video_frames": 16,
    "failed_inputs_total": 0
  },
  "retries": {
    "total": 1,
    "success": 0,
    "failure": 1,
    "success_rate_percent": 0.0,
    "last_retry_time": 1730000005.0
  }
}
```

Copy to clipboard

### GET /v1/metadata [\#](https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html\#get-v1-metadata "Link to this heading")

Provides metadata about the NIM container, including version and model
information.

### GET /v1/manifest [\#](https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html\#get-v1-manifest "Link to this heading")

Returns the NIM manifest file content.

### GET /v1/license [\#](https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html\#get-v1-license "Link to this heading")

Returns the license information for the NIM.

### GET /v1/metrics [\#](https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html\#get-v1-metrics "Link to this heading")

Returns Prometheus-compatible metrics for monitoring.

On this page