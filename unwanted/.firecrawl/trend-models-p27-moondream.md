[NewPhoton: 400 tok/s on Qwen 3.5](https://moondream.ai/blog/photon-2-6-qwen-400-tokens-per-second)

# State-of-the-art vision foryour task.detect · 0.98

Build, fine-tune, and deploy visual AI that works on your real-world edge cases.

[Try the playground](https://moondream.ai/playground) [View docs](https://docs.moondream.ai/)

$pip install moondream

5M+ monthly downloads · open weights · commercial use

WarehouseApp interfaceAdvertisingAircraft IDScene taggingWarehouseApp interfaceAdvertisingAircraft IDScene taggingWarehouseApp interfaceAdvertisingAircraft IDScene taggingWarehouseApp interfaceAdvertisingAircraft IDScene taggingWarehouseApp interfaceAdvertisingAircraft IDScene tagging

![](https://depot.moondream.ai/images/warehouse.jpeg)

Misoriented box

manufacturing / logistics

>model.detect(image, "Misoriented box")

{ "x\_min": 0.70, "y\_min": 0.39, "x\_max": 0.98, "y\_max": 0.61 }

33 ms·Linux RTX 6000

Moondream 3.1 on Photon, fine-tuned with Lens

01

Step 1 · Try it

## Try the open models. You might already be done.

Moondream might already nail your use case out of the box. The open models are commercially friendly and can run anywhere. Use our playground to try it out or download it and run it yourself.

[Open playground](https://moondream.ai/playground)

No credit card required. $5 in credits added monthly.

python

```
# Caption an image in four lines
import moondream as md
from PIL import Image

model = md.vl(api_key="YOUR_API_KEY")
image = Image.open("shelf.jpg")
print(model.caption(image).caption)
# → 'A warehouse shelf with six cardboard cartons…'
```

[**Moondream 3.1** Recommended\\
\\
Sparse mixture-of-experts architecture with frontier-level visual reasoning, segmentation, and long-context queries.\\
\\
9B MoE · 2B active\\
\\
QueryCaptionDetectPointSegment\\
\\
Model card](https://moondream.ai/models/moondream_3-1_9B_A2B) [**Moondream 2** Stable\\
\\
The production workhorse: compact, proven, commercially friendly, and easy to deploy across GPUs, CPUs, and edge devices.\\
\\
2B dense\\
\\
QueryCaptionDetectPointSegment\\
\\
Model card](https://moondream.ai/models#moondream-2) [**Moondream 2 0.5B** Tiny\\
\\
A small fine-tuning base for constrained hardware where every megabyte matters.\\
\\
0.5B dense\\
\\
QueryCaptionDetectPointSegment\\
\\
Model card](https://moondream.ai/models#moondream-2-0-5b)

02

Step 2 · Fine-tune it

## Need more? Lens gets you to production-grade accuracy.

Your data is specific, so the model has to be. Lens is a fine-tuning platform with a simple API. No dataset uploads, no infrastructure, no ML team required.

[Learn more about Lens](https://moondream.ai/lens) [Start fine-tuning](https://docs.moondream.ai/finetuning/)

Self-serve API

A simple hosted API — no hardware to rent or manage. Supports SFT and RL. Vibe-code your fine-tune script in minutes.

Tune and go

Your fine-tuned model is instantly ready to run on Moondream Cloud or locally with Photon. No cumbersome download or install step.

White-glove option

Our team handles the labeling protocol, loss design, and evaluation. You keep the weights, the training code, and the data. Unlike ML consulting, you walk away self-sufficient.

No massive dataset required

Our reinforcement-learning fine-tune API can dramatically improve accuracy with as few as 20 labeled images — not thousands.

03

Step 3 · Run it anywhere

## Fast, efficient, and runs anywhere you need it.

Once your model is accurate, performance and cost become the next wall. Photon is the inference engine we built to run Moondream in production. Moondream Cloud and partner clouds give you a hosted path if you want one.

Speed

Under 500 ms is the difference between a useful answer and a late one. Photon answers a direct query in under 60 ms on an H100, and stays real-time all the way down to Jetson.

59 msP50 · H100 · batch 1

Cost

A VLM running across a fleet of cameras at the wrong efficiency costs thousands a day. Moondream is the lowest-cost VLM we have measured across the inference providers we tested.

$0.06per 1K images, cloud

Flexibility

Your deployment story will change. Start in the cloud, move to the edge, or run air-gapped. You pick the hardware. The model and APIs stay the same.

9benchmarked hardware tiers

Internal benchmark

Time per request

median of 200 runs · lower is better

Moondream 3.1 + PhotonH100 · batch 1

59 msbaseline

Qwen 3.5 4B + vLLMH100 · batch 1

73 ms1.2× slower

GPT-5.4 MiniOpenAI API

2.78 s47× slower

Gemini 2.5 FlashGoogle API

3.79 s64× slower

direct-answer query · batch 1 · NVIDIA H100 80GB · 2026-02 build

Photon · hardware

Same model, every tier.

Moondream 3.1 on Photon, benchmarked from datacenter to Jetson. Latency is the median for a single direct-answer query; throughput is peak sustained requests per second.

HardwareP50 latencyPeak throughput

NVIDIA B200Datacenter49 _ms_77.7 _req/s_

NVIDIA H100Datacenter59 _ms_58.0 _req/s_

RTX PRO 6000Workstation68 _ms_38.8 _req/s_

NVIDIA L40SServer99 _ms_24.7 _req/s_

NVIDIA A100 80GBCloud136 _ms_16.7 _req/s_

Jetson AGX ThorEdge246 _ms_12.6 _req/s_

NVIDIA A10Cloud280 _ms_7.2 _req/s_

NVIDIA L4Cloud317 _ms_6.9 _req/s_

Jetson AGX OrinEdge · Moondream 2514 _ms_4.6 _req/s_

ChartQA test split · prefix caching enabled · Jetson AGX Orin runs Moondream 2 · [full data on GitHub](https://github.com/m87-labs/kestrel/blob/main/PERFORMANCE.md)

Available on

FAL

Self-hosted

Moondream Cloud

Photon

Same code. Edge, workstation, server.

[Read the Photon docs](https://docs.moondream.ai/running-locally)

python

```
import moondream as md
from PIL import Image

# Initialize with local GPU inference
model = md.vl(api_key="YOUR_API_KEY", local=True)

# Load an image
image = Image.open("path/to/image.jpg")

# Generate a caption
caption = model.caption(image)["caption"]
print("Caption:", caption)
```

04

Step 4 · Keep it running

## Launch is just the start.

One vendor for the full stack. Models drift. Engineers leave. New use cases appear. With stitched-together vendors, nobody owns the outage. On Moondream, we do.

Competitor stack

- Model vendor (weights only)
- Fine-tuning vendor (your data goes elsewhere)
- Inference provider (different SLA)
- Your on-call engineer (owns everything)

Moondream

- Model, weights, and roadmap
- Lens fine-tuning and evals
- Photon and Moondream Cloud
- One team on call, 24/7 on enterprise plans

[See Plans](https://moondream.ai/pricing)

The platform

## Four products that work together. Use one, or all four.

[01\\
\\
Open Models\\
\\
The foundation. Free for commercial use. 2B, 1B, and 0.5B checkpoints on Hugging Face.\\
\\
View on Hugging Face](https://moondream.ai/models) [02\\
\\
Lens\\
\\
Fine-tuning with a simple API. Self-serve or white-glove. You keep the weights.\\
\\
Start fine-tuning](https://moondream.ai/lens) [03\\
\\
Photon\\
\\
Inference engine. Hand-tuned kernels. Mac, Windows, CUDA — Jetson to B200.\\
\\
Run Moondream fast](https://moondream.ai/photon) [04\\
\\
Moondream Cloud\\
\\
Hosted inference. OpenAI-compatible API. Pay per image, no commitment.\\
\\
Get an API key](https://moondream.ai/cloud)

## Moondream is trusted by

CalPoly

CalPoly

## Every machine will see.

Build with Moondream 3.1 today.

[Try the playground](https://moondream.ai/playground) Talk to us