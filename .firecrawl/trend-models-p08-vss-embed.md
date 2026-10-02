[Skip to main content](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html#main-content)

Back to top`⌘` + `K`

[![VSS - Home](https://docs.nvidia.com/vss/latest/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg)![VSS - Home](https://docs.nvidia.com/vss/latest/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg)\\
VSS](https://docs.nvidia.com/vss/latest/index.html)

3.2.1

[3.2.1](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html) [3.2.0](https://docs.nvidia.com/vss/3.2.0/models/cosmos-embed1.html) [3.1.0](https://docs.nvidia.com/vss/3.1.0/models/cosmos-embed1.html) [3.0.0](https://docs.nvidia.com/vss/3.0.0/models/cosmos-embed1.html) [2.4.1](https://docs.nvidia.com/vss/2.4.1/models/cosmos-embed1.html) [2.4.0](https://docs.nvidia.com/vss/2.4.0/models/cosmos-embed1.html) [2.3.1](https://docs.nvidia.com/vss/2.3.1/models/cosmos-embed1.html) [2.3.0](https://docs.nvidia.com/vss/2.3.0/models/cosmos-embed1.html) [2.2.0](https://docs.nvidia.com/vss/2.2.0/models/cosmos-embed1.html)

LightDarkSystem Settings

# Cosmos-Embed1 (video embedding) [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#cosmos-embed1-video-embedding "Link to this heading")

## Role in VSS [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#role-in-vss "Link to this heading")

The Real-Time Embedding microservice ( [Real-Time Embedding](https://docs.nvidia.com/vss/latest/real-time-embedding.html)) loads **Cosmos-Embed1** variants by default (for example 224p / 336p / 448p Hugging Face checkpoints) and publishes **video** and **text** embeddings for semantic search and Kafka consumers. The updated model card also includes a 448p anomaly-detection variant fine-tuned with LoRA. Container variables such as `MODEL_PATH`, optional `MODEL_IMPLEMENTATION_PATH`, and Triton repo scripts are described under [Customizations](https://docs.nvidia.com/vss/latest/real-time-embedding.html#rt-embedding-customizations) on [Real-Time Embedding](https://docs.nvidia.com/vss/latest/real-time-embedding.html).

Note

Full TAO reference for Cosmos-Embed1—including experiment schema tables, dataset configs, and optional Weights & Biases logging—lives in the published embedding chapter and mirrors the in-repo `tlt-docs/docs/text/embedding/cosmos_embed1.rst` (and `cosmos_embed1_tables.rst`) sources.

## Architecture and tasks [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#architecture-and-tasks "Link to this heading")

Cosmos-Embed1 is a **dual-encoder video–text** model: an **EVA-ViT-G** visual encoder on sampled frames, a **Q-Former** distilled from video features, a **BERT-style** text encoder, and **CLIP-style or SigLIP-style** contrastive alignment. Each forward pass runs in either text-encoding mode or video-encoding mode and produces a normalized embedding in a shared vector space. **LoRA** is supported for efficient fine-tuning of visual and Q-Former attention layers.

TAO tasks:

```
tao model cosmos-embed1 <action> -e /path/to/spec.yaml [overrides]
```

Copy to clipboard

Where `<action>` is one of `train`, `evaluate`, `inference`, or `export`.

## Model variants [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#model-variants "Link to this heading")

The current [Cosmos-Embed1 model card](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1) lists these checkpoints:

| Variant | Resolution | Frames | Embedding dim | Notes |
| --- | --- | --- | --- | --- |
| `Cosmos-Embed1-224p` | 224x224 | 8 | 256 | Base video-text embedder |
| `Cosmos-Embed1-336p` | 336x336 | 8 | 768 | Base video-text embedder |
| `Cosmos-Embed1-448p` | 448x448 | 8 | 768 | Base video-text embedder |
| `Cosmos-Embed1-448p-anomaly-detection` | 448x448 | 8 | 768 | LoRA fine-tune from 448p on Vad-Reasoning for anomaly detection, anomaly classification, and video retrieval |

The checkpoints default to their optimized square resolution, but the model card notes that arbitrary non-square resolutions are supported. If you switch between 224p and the 336p/448p variants, plan to re-index vector stores because the embedding dimension changes from 256 to 768.

## Hardware requirements [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#hardware-requirements "Link to this heading")

**Minimum (typical single-GPU training at 224p):** one NVIDIA GPU with **at least 40 GB** GPU memory; Ubuntu 20.04+; CUDA 12.1+.

**Recommended:** multiple A100 or H100 GPUs, fast storage for video I/O, and sufficient CPU cores for dataloaders. Exact needs depend on resolution, batch size, and `train.max_iter`.

## Data input (summary) [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#data-input-summary "Link to this heading")

Cosmos-Embed1 uses a **JSON or JSONL metadata** file mapping each video to a caption (and optional labels). The `dataset_type` field selects loaders. Common types include:

| `dataset_type` | Description |
| --- | --- |
| `mock` | Synthetic data for pipeline tests (no real video files) |
| `vad_r1` / `vad_r1_chunks` | VAD-R1 anomaly-style video with captions and optional temporal chunks |
| `msrvtt` | MSR-VTT-style video–description pairs |
| `kinetics` | Kinetics-style action clips with metadata CSV |
| `http` | Videos referenced by HTTP URLs in metadata |

Field-level requirements (paths, `caption_field`, chunking) are in the [Cosmos-Embed1 TAO chapter](https://docs.nvidia.com/tao/tao-toolkit/latest/text/embedding/cosmos_embed1.html). Align your **frame sampling** and **resolution** with the variant you deploy. The model card reports optimization around **8 frames**, typically sampled at **1-2 FPS**; confirm the production chunking in your runtime config.

## TAO fine-tuning configuration [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#tao-fine-tuning-configuration "Link to this heading")

Fine-tuning uses YAML experiment files that follow the `ExperimentConfig` schema. Full parameter tables live in the published [Cosmos-Embed1](https://docs.nvidia.com/tao/tao-toolkit/latest/text/embedding/cosmos_embed1.html) chapter; they are generated from `tlt-docs/docs/text/embedding/cosmos_embed1_tables.rst`.

```
tao model cosmos-embed1 <action> -e /path/to/spec.yaml [overrides]
```

Copy to clipboard

Top-level sections in the experiment file:

- `results_dir` — run output root

- `wandb` — optional Weights & Biases logging

- `model` — `pretrained_model_path`, `precision`, `input_hw`, `network` (EVA-ViT, Q-Former, frames, resolution, contrastive type), `lora`, `fsdp`

- `dataset` — `train_dataset`, `val_dataset`, `test_dataset`, `inference_dataset` (each a `SingleDatasetConfig` with `dataset_type`, `metadata`, `data_root`, batching, etc.)

- `train` — `max_iter`, `num_gpus`, `optim`, `loss_weights`, `callbacks`, `ema`, resume paths, `freeze_visual_encoder`, …

- `evaluate` — checkpoint, callbacks (top-K, UMAP), optional embedding cache paths

- `inference` — checkpoint, query config, `k`, corpus cache paths

- `export` — `mode` (`video` / `text` / `combined` / Hugging Face), `onnx_file`, `opset_version`, `hf_output_dir`


### Example experiment specification [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#example-experiment-specification "Link to this heading")

Illustrative 224p layout (`vad_r1`-style metadata). Replace `??` with your paths; align `network.num_video_frames` and `dataset.*.num_video_frames` with deployment. When available, start from the packaged `cosmos_embed1/configs/experiment_specs/*.yaml` files in your TAO Toolkit tree and merge overrides rather than authoring a spec from scratch.

```
results_dir: /results/cosmos_experiment

wandb:
  enable: false
  project: cosmos_embed1

model:
  pretrained_model_path: nvidia/Cosmos-Embed1-224p
  pretrained_model_strict: true
  precision: bf16
  input_hw: [224, 224]
  network:
    embed_dim: 256
    num_query_tokens: 32
    max_txt_len: 128
    num_video_frames: 8
    spatial_resolution: [224, 224]
    contrastive_type: clip
  lora:
    enabled: false
    lora_rank: 8
    lora_alpha: 16

dataset:
  train_dataset:
    dataset_type: vad_r1
    metadata: /data/train.jsonl
    data_root: /data/videos
    batch_size: 4
    num_video_frames: 8
    resolution: [224, 224]
    caption_field: anomaly_type
  val_dataset:
    dataset_type: vad_r1
    metadata: /data/val.jsonl
    data_root: /data/videos
    batch_size: 4
    num_video_frames: 8
    resolution: [224, 224]

train:
  max_iter: 50000
  num_gpus: 1
  num_nodes: 1
  gpu_ids: [0]
  validation_iter: 1000
  checkpoint_iter: 1000
  clip_grad_norm: 0.0
  precision: bf16
  resume_training_checkpoint_path: null
  freeze_visual_encoder: true
  use_captioning_loss: true
  use_text_matching_loss: false
  optim:
    optim: adamw
    lr: 1.0e-5
    weight_decay: 1.0e-5
    betas: [0.9, 0.98]
    warmup_steps: 1000
    policy: cosine
    lr_decay_iters: 50000
  loss_weights:
    contrastive_loss: 1.0
    captioning_loss: 1.0
    matching_loss: 1.0

evaluate:
  checkpoint: /results/cosmos_experiment/train/cosmos_embed1_model_latest.pth
  num_gpus: 1

inference:
  checkpoint: /results/cosmos_experiment/train/cosmos_embed1_model_latest.pth
  k: 5

export:
  checkpoint: /results/cosmos_experiment/train/cosmos_embed1_model_latest.pth
  mode: combined
  opset_version: 17
  batch_size: 1
  simplify: false
```

Copy to clipboard

### LoRA fine-tuning (config fragment) [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#lora-fine-tuning-config-fragment "Link to this heading")

Use a LoRA spec (for example `finetune_224p_lora.yaml` in the TAO starter layouts) and ensure the visual encoder allows PEFT injection (`transformer_engine: false` on the visual encoder when required by the TAO release):

```
model:
  lora:
    enabled: true
    lora_rank: 8
    lora_alpha: 16
```

Copy to clipboard

### Launch model fine-tuning [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#launch-model-fine-tuning "Link to this heading")

Update dataset paths and training budget, then run:

```
dataset:
  train_dataset:
    metadata: ??  # JSON or JSONL
    data_root: ??
  val_dataset:
    metadata: ??
    data_root: ??
```

Copy to clipboard

```
train:
  max_iter: ??  # e.g. 10000–50000 depending on data
  num_gpus: ??  # or train.num_gpus=-1 for all GPUs
```

Copy to clipboard

```
tao model cosmos-embed1 train \
    -e /path/to/finetune_224p.yaml \
    results_dir=/results/my_experiment \
    model.pretrained_model_path=nvidia/Cosmos-Embed1-224p \
    dataset.train_dataset.metadata=/data/train.jsonl \
    dataset.train_dataset.data_root=/data/videos \
    dataset.val_dataset.metadata=/data/val.jsonl \
    dataset.val_dataset.data_root=/data/videos
```

Copy to clipboard

Checkpoints are written under `<results_dir>/train/` (for example `cosmos_embed1_model_latest.pth`).

### Evaluate the fine-tuned model [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#evaluate-the-fine-tuned-model "Link to this heading")

```
tao model cosmos-embed1 evaluate \
    -e /path/to/evaluate_224p.yaml \
    results_dir=/results/my_eval \
    evaluate.checkpoint=/results/my_experiment/train/cosmos_embed1_model_latest.pth \
    dataset.test_dataset.metadata=/data/test.jsonl \
    dataset.test_dataset.data_root=/data/videos
```

Copy to clipboard

Optional: set `evaluate.save_dataset_pkl` / `evaluate.load_dataset_pkl` to cache embeddings between runs.

### Run inference (text / video search) [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#run-inference-text-video-search "Link to this heading")

```
tao model cosmos-embed1 inference \
    -e /path/to/inference_224p.yaml \
    inference.checkpoint=/results/my_experiment/train/cosmos_embed1_model_latest.pth \
    dataset.inference_dataset.metadata=/data/search_corpus.jsonl \
    dataset.inference_dataset.data_root=/data/videos \
    'inference.query.input_texts=["a car crash", "flooding on highway"]'
```

Copy to clipboard

Use `inference.save_dataset_pkl` / `inference.load_dataset_pkl` to cache the encoded corpus.

### Export ONNX and Hugging Face [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#export-onnx-and-hugging-face "Link to this heading")

**ONNX** — `export.mode` selects `video`, `text`, `combined`, or Hugging Face export paths:

```
tao model cosmos-embed1 export \
    -e /path/to/export_onnx_224p.yaml \
    export.checkpoint=/results/my_experiment/train/cosmos_embed1_model_latest.pth \
    export.mode=combined
```

Copy to clipboard

**Hugging Face layout** (for drop-in `MODEL_PATH`):

```
tao model cosmos-embed1 export \
    -e /path/to/export_hf_224p.yaml \
    export.checkpoint=/results/my_experiment/train/cosmos_embed1_model_latest.pth \
    export.hf_output_dir=/results/my_experiment/hf_export
```

Copy to clipboard

## Integrating fine-tuned weights into RT-Embedding [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#integrating-fine-tuned-weights-into-rt-embedding "Link to this heading")

1. **Fine-tune** with TAO using resolution and sampling that match production (chunk length, frame count, variant).

2. **Export** to ONNX or Hugging Face layout as required by your runtime.

3. Set `MODEL_PATH` to a `git:` Hugging Face URL or a **mounted local directory** with the expected structure. If you change the Python implementation or Triton repository layout, set `MODEL_IMPLEMENTATION_PATH` and `MODEL_REPOSITORY_SCRIPT_PATH` consistently with [Real-Time Embedding](https://docs.nvidia.com/vss/latest/real-time-embedding.html).

4. **Re-index** Elasticsearch (or other vector stores) if embedding dimension or semantics change; rerun integration tests for RTSP ingest, file ingest, and Kafka consumers.


Note

For embedding search and agent workflows, see [Search Workflow](https://docs.nvidia.com/vss/latest/agent-workflow-search.html) and [Model customization overview](https://docs.nvidia.com/vss/latest/models/model-customization.html).

## Source material in this repo’s doc trees [\#](https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html\#source-material-in-this-repos-doc-trees "Link to this heading")

- `tlt-docs/docs/text/embedding/cosmos_embed1.rst` — full narrative, commands, and configuration

- `tlt-docs/docs/text/embedding/cosmos_embed1_tables.rst` — generated parameter tables

- `tlt-docs/docs/text/embedding/index.rst` — embedding overview and launcher pattern


On this page