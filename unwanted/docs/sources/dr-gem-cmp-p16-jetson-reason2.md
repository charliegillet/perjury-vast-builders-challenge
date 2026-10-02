🎉

Welcome to Jetson AI Lab 2.0!

We've redesigned the site with curated tutorials. Looking for old content?
[Browse the archive →](https://www.jetson-ai-lab.com/archive/index.html)

×

Multimodal

# Cosmos Reason 2 8B

NVIDIA's 8B parameter vision-language model with advanced chain-of-thought reasoning capabilities

[Benchmark](https://www.jetson-ai-lab.com/models/cosmos-reason2-8b/#model-benchmark) [Model Details](https://www.jetson-ai-lab.com/models/cosmos-reason2-8b/#model-details)

Parameters8B

Modalities

Text  Image  Video

Context Length256K

LicenseNVIDIA Open Model License

Precision

FP8

## Benchmark

**Cosmos Reasoning 2 8B**
· vLLM
· NVFP4\* / W4A16 · ISL 2048 / OSL 128

Engine

vLLM

Concurrency

C=1

C=8

NVFP4\*

W4A16

[Cosmos Reasoning 2 2B (NVFP4\*) ↗](https://www.jetson-ai-lab.com/models/cosmos-reason2-2b#model-benchmark)

0306090120150tok/sJetson ThorT5000Jetson ThorT4000JetsonAGX Orin64GBJetsonOrin NX16GBJetsonOrin Nano8GB40108328919

No data available for this combination.

C = concurrent requests. Results will vary with image, clocks, and workload.

## Model Details

[![HuggingFace](https://www.jetson-ai-lab.com/images/icons/hf-logo.png)\\
View on HuggingFace](https://huggingface.co/nvidia/Cosmos-Reason2-8B)

[NVIDIA Cosmos Reason 2 8B](https://huggingface.co/nvidia/Cosmos-Reason2-8B) is the larger variant in the Cosmos Reason 2 family, offering enhanced reasoning performance with 8 billion parameters. It provides stronger chain-of-thought reasoning capabilities compared to the 2B variant, suitable for more demanding vision-language tasks on Jetson.

## Key Capabilities

- **Enhanced Reasoning**: Stronger chain-of-thought reasoning compared to the 2B variant
- **Spatial Reasoning**: Advanced understanding of spatial relationships between objects
- **Anomaly Detection**: Identifies unusual patterns and anomalies in visual data
- **Scene Analysis**: Comprehensive and detailed analysis of complex visual scenes
- **Video Understanding**: Supports video frame analysis for temporal reasoning

## Running with vLLM

The vLLM path uses an [FP8 quantized checkpoint from NGC](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/models/cosmos-reason2-8b?version=1208-fp8-static-kv8) downloaded via the NGC CLI.

### Step 1: Install and Configure the NGC CLI

```
wget -O ngccli_arm64.zip https://api.ngc.nvidia.com/v2/resources/nvidia/ngc-apps/ngc_cli/versions/4.13.0/files/ngccli_arm64.zip
unzip ngccli_arm64.zip && chmod u+x ngc-cli/ngc
export PATH="$PATH:$(pwd)/ngc-cli"
ngc config set
```

You will need an [NGC account](https://ngc.nvidia.com/) with access to the `nim` org and a valid API key.

### Step 2: Download the FP8 Model

```
ngc registry model download-version "nim/nvidia/cosmos-reason2-8b:1208-fp8-static-kv8" \
  --dest ~/.cache/huggingface/hub
export MODEL_PATH="${HOME}/.cache/huggingface/hub/cosmos-reason2-8b_v1208-fp8-static-kv8"
```

### Step 3: Serve

The second volume `-v ${HOME}/.cache/vllm:/root/.cache/vllm` persists vLLM’s **torch.compile cache** on the host. The first run compiles kernels and writes them there; later runs reuse the cache and start faster. Create the dir if needed: `mkdir -p ~/.cache/vllm`.

Jetson ThorAGX Orin

```
mkdir -p ~/.cache/vllm
sudo sysctl -w vm.drop_caches=3

sudo docker run -it --rm --runtime=nvidia --network host \
  -v $MODEL_PATH:/models/cosmos-reason2-8b:ro \
  -v ${HOME}/.cache/vllm:/root/.cache/vllm \
  vllm/vllm-openai:latest \
  /models/cosmos-reason2-8b \
    --served-model-name nvidia/cosmos-reason2-8b-fp8 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.7 \
    --reasoning-parser qwen3 \
    --media-io-kwargs '{"video": {"num_frames": -1}}' \
    --enable-prefix-caching \
    --port 8010
```

```
mkdir -p ~/.cache/vllm
sudo sysctl -w vm.drop_caches=3

sudo docker run -it --rm --runtime=nvidia --network host \
  -v $MODEL_PATH:/models/cosmos-reason2-8b:ro \
  -v ${HOME}/.cache/vllm:/root/.cache/vllm \
  ghcr.io/nvidia-ai-iot/vllm:latest-jetson-orin \
  vllm serve /models/cosmos-reason2-8b \
    --max-model-len 8192 --gpu-memory-utilization 0.8 --reasoning-parser qwen3 \
    --media-io-kwargs '{"video": {"num_frames": -1}}' \
    --enable-prefix-caching \
    --port 8010
```

## Running with llama.cpp (Recommended for Orin Nano)

Jetson ThorAGX OrinOrin Nano

```
sudo docker run -it --rm --pull always --runtime=nvidia --network host \
  -v $HOME/.cache/huggingface:/root/.cache/huggingface \
  ghcr.io/nvidia-ai-iot/llama_cpp:latest-jetson-thor \
  llama-server -hf Kbenkhaled/Cosmos-Reason2-8B-GGUF:Q4_K_M -c 8192
```

```
sudo docker run -it --rm --pull always --runtime=nvidia --network host \
  -v $HOME/.cache/huggingface:/root/.cache/huggingface \
  ghcr.io/nvidia-ai-iot/llama_cpp:latest-jetson-orin \
  llama-server -hf Kbenkhaled/Cosmos-Reason2-8B-GGUF:Q4_K_M -c 8192
```

```
sudo docker run -it --rm --pull always --runtime=nvidia --network host \
  -v $HOME/.cache/huggingface:/root/.cache/huggingface \
  ghcr.io/nvidia-ai-iot/llama_cpp:latest-jetson-orin \
  llama-server -hf Kbenkhaled/Cosmos-Reason2-8B-GGUF:Q4_K_M -c 8192
```

## Cosmos Reason 2 Family

| Model | Parameters | Memory | Best For |
| --- | --- | --- | --- |
| [Cosmos Reason 2 2B](https://www.jetson-ai-lab.com/models/cosmos-reason2-2b) | 2B | 8GB RAM | Lightweight edge deployment |
| **Cosmos Reason 2 8B** | 8B | 18GB RAM | Higher accuracy, demanding tasks |

## Additional Resources

- [NGC FP8 Checkpoint](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/models/cosmos-reason2-8b?version=1208-fp8-static-kv8) \- FP8 quantized model for vLLM
- [Live VLM WebUI](https://github.com/NVIDIA-AI-IOT/live-vlm-webui) \- real-time webcam-to-VLM interface