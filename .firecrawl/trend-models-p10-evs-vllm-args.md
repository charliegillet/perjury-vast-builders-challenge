[Skip to content](https://docs.vllm.ai/en/stable/configuration/engine_args/#engine-arguments)

[Provide feedback](https://github.com/vllm-project/vllm/issues/new?template=100-documentation.yml&title=%5BDocs%5D%20Feedback%20for%20%60%2Fen%2Fstable%2Fconfiguration%2Fengine_args%2F%60&body=%F0%9F%93%84%20**Reference%3A**%0Ahttps%3A%2F%2Fdocs.vllm.ai%2Fen%2Fstable%2Fconfiguration%2Fengine_args%2F%0A%0A%F0%9F%93%9D%20**Feedback%3A**%0A_Your%20response_ "Provide feedback") [Edit this page](https://github.com/vllm-project/vllm/edit/main/docs/configuration/engine_args.md "Edit this page")

# Engine Arguments [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#engine-arguments "Permanent link")

Engine arguments control the behavior of the vLLM engine.

- For [offline inference](https://docs.vllm.ai/en/stable/serving/offline_inference/), they are part of the arguments to [LLM](https://docs.vllm.ai/en/stable/api/vllm/#vllm.LLM "            LLM") class.
- For [online serving](https://docs.vllm.ai/en/stable/serving/online_serving/), they are part of the arguments to `vllm serve`.

The engine argument classes, [EngineArgs](https://docs.vllm.ai/en/stable/api/vllm/engine/arg_utils/#vllm.engine.arg_utils.EngineArgs "            EngineArgs            dataclass   ") and [AsyncEngineArgs](https://docs.vllm.ai/en/stable/api/vllm/engine/arg_utils/#vllm.engine.arg_utils.AsyncEngineArgs "            AsyncEngineArgs            dataclass   "), are a combination of the configuration classes defined in [vllm.config](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config "            vllm.config"). Therefore, if you are interested in developer documentation, we recommend looking at these configuration classes as they are the source of truth for types, defaults and docstrings.

## JSON CLI Arguments [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#json-cli-arguments "Permanent link")

When passing JSON CLI arguments, the following sets of arguments are equivalent:

- `--json-arg '{"key1": "value1", "key2": {"key3": "value2"}}'`
- `--json-arg.key1 value1 --json-arg.key2.key3 value2`

Additionally, list elements can be passed individually using `+`:

- `--json-arg '{"key4": ["value3", "value4", "value5"]}'`
- `--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`

## [`EngineArgs`](https://docs.vllm.ai/en/stable/api/vllm/engine/arg_utils/\#vllm.engine.arg_utils.EngineArgs "            EngineArgs            dataclass   ") [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#engineargs "Permanent link")

#### `--disable-log-stats` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-disable-log-stats "Permanent link")

Disable logging statistics.Default: `False`

#### `--aggregate-engine-logging` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-aggregate-engine-logging "Permanent link")

Log aggregate rather than per-engine statistics when using data parallelism.Default: `False`

#### `--fail-on-environ-validation`, `--no-fail-on-environ-validation` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-fail-on-environ-validation-no-fail-on-environ-validation "Permanent link")

If set, the engine will raise an error if environment validation fails.Default: `False`

#### `--shutdown-timeout` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-shutdown-timeout "Permanent link")

Shutdown timeout in seconds. 0 = abort, >0 = wait.Default: `0`

#### `--gdn-prefill-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-gdn-prefill-backend "Permanent link")

Possible choices: `flashinfer`, `triton`, `cutedsl`Select GDN prefill backend.

#### `--kda-prefill-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kda-prefill-backend "Permanent link")

Possible choices: `auto`, `triton`, `flashkda`, `flashinfer`, `fused`Select KDA prefill backend. 'flashkda' is CUDA-only and 'fused' is ROCm-only; 'auto' picks a supported backend.

#### `--kda-decode-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kda-decode-backend "Permanent link")

Possible choices: `auto`, `native`, `flashinfer`, `triton`Select KDA decode backend.

### ModelConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#modelconfig "Permanent link")

Configuration for the model.

#### `--model` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-model "Permanent link")

Name or path of the Hugging Face model to use. It is also used as the content for `model_name` tag in metrics output when `served_model_name` is not specified.Default: `Qwen/Qwen3-0.6B`

#### `--runner` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-runner "Permanent link")

Possible choices: `auto`, `draft`, `generate`, `pooling`The type of model runner to use. Each vLLM instance only supports one model runner, even if the same model can be used for multiple types.Default: `auto`

#### `--convert` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-convert "Permanent link")

Possible choices: `auto`, `classify`, `embed`, `none`Convert the model using adapters defined in [vllm.model\_executor.models.adapters](https://docs.vllm.ai/en/stable/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters "            vllm.model_executor.models.adapters"). The most common use case is to adapt a text generation model to be used for pooling tasks.Default: `auto`

#### `--tokenizer` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-tokenizer "Permanent link")

Name or path of the Hugging Face tokenizer to use. If unspecified, model name or path will be used.

#### `--tokenizer-mode` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-tokenizer-mode "Permanent link")

Possible choices: `auto`, `cohere`, `deepseek_v32`, `deepseek_v4`, `hf`, `inkling`, `kimi_k3`, `mistral`, `slow`

Tokenizer mode:

- "auto" will use the tokenizer from `mistral_common` for Mistral models if available, otherwise it will use the "hf" tokenizer.
- "hf" will use the fast tokenizer if available.
- "slow" will always use the slow tokenizer.
- "mistral" will always use the tokenizer from `mistral_common`.
- "deepseek\_v32" will always use the tokenizer from `deepseek_v32`.
- "deepseek\_v4" will always use the tokenizer from `deepseek_v4`.
- "deepseek\_v41" will use the DeepSeek V4.1 prompt encoder.
- "kimi\_k3" will always use the "hf" tokenizer but render chat prompts with Kimi K3's Python XTML encoding instead of a Jinja template.
- "cohere" uses the standard HF tokenizer but renders the chat template via the `cohere_melody` library (cmd3 / cmd4 templates) instead of Jinja, and surfaces grounded-citation metadata on responses.
- Other custom values can be supported via plugins.

To swap the Rust BPE backend that powers HF fast tokenizers for the [fastokens](https://github.com/crusoecloud/fastokens) implementation, set `VLLM_USE_FASTOKENS=1` instead — that override applies to any mode that loads an HF fast tokenizer (`hf`, `deepseek_v32`, `deepseek_v4`, …).

Default: `auto`

#### `--trust-remote-code`, `--no-trust-remote-code` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-trust-remote-code-no-trust-remote-code "Permanent link")

Trust remote code (e.g., from HuggingFace) when downloading the model and tokenizer.Default: `False`

#### `--dtype` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-dtype "Permanent link")

Possible choices: `auto`, `bfloat16`, `float`, `float16`, `float32`, `half`

Data type for model weights and activations:

- "auto" will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models.
- "half" for FP16. Recommended for AWQ quantization.
- "float16" is the same as "half".
- "bfloat16" for a balance between precision and range.
- "float" is shorthand for FP32 precision.
- "float32" for FP32 precision.

Default: `auto`

#### `--seed` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-seed "Permanent link")

Random seed for reproducibility.

We must set the global seed because otherwise, different tensor parallel workers would sample different tokens, leading to inconsistent results.

Default: `0`

#### `--hf-config-path` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-hf-config-path "Permanent link")

Name or path of the Hugging Face config to use. If unspecified, model name or path will be used.

#### `--allowed-local-media-path` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-allowed-local-media-path "Permanent link")

Allowing API requests to read local images or videos from directories specified by the server file system. This is a security risk. Should only be enabled in trusted environments.Default: `""`

#### `--allowed-media-domains` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-allowed-media-domains "Permanent link")

If set, only media URLs that belong to this domain can be used for multi-modal inputs.

#### `--revision` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-revision "Permanent link")

The specific model version to use. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

#### `--code-revision` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-code-revision "Permanent link")

The specific revision to use for the model code on the Hugging Face Hub. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

#### `--tokenizer-revision` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-tokenizer-revision "Permanent link")

The specific revision to use for the tokenizer on the Hugging Face Hub. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

#### `--max-model-len` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-model-len "Permanent link")

Model context length (prompt and output). If unspecified, will be automatically derived from the model config.

When passing via `--max-model-len`, supports k/m/g/K/M/G in human-readable format. Examples:

- 1k -> 1000
- 1K -> 1024
- 25.6k -> 25,600
- -1 or 'auto' -> Automatically choose the maximum model length that fits in GPU memory. This will use the model's maximum context length if it fits, otherwise it will find the largest length that can be accommodated.

Parse human-readable integers like '1k', '2M', etc. Including decimal values with decimal multipliers. Also accepts -1 or 'auto' as a special value for auto-detection.

```
Examples:
- '1k' -> 1,000
- '1K' -> 1,024
- '25.6k' -> 25,600
- '-1' or 'auto' -> -1 (special value for auto-detection)
```

#### `--quantization`, `-q` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-quantization-q "Permanent link")

Method used to quantize the weights. If `None`, we first check the `quantization_config` attribute in the model config file. If that is `None`, we assume the model weights are not quantized and use `dtype` to determine the data type of the weights.

#### `--quantization-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-quantization-config "Permanent link")

User-facing quantization configuration. Carries per-layer-kind specs (linear, moe) and ignore patterns; see :class: [`QuantizationConfigArgs`](https://docs.vllm.ai/en/stable/api/vllm/config/quantization/#vllm.config.quantization.QuantizationConfigArgs "            QuantizationConfigArgs"). Auto-populated from the matching online shorthand when `quantization` is one of the values in `ONLINE_QUANT_SHORTHAND_NAMES`.

Should either be a valid JSON string or JSON keys passed individually.

#### `--allow-deprecated-quantization`, `--no-allow-deprecated-quantization` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-allow-deprecated-quantization-no-allow-deprecated-quantization "Permanent link")

Whether to allow deprecated quantization methods.Default: `False`

#### `--enforce-eager`, `--no-enforce-eager` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enforce-eager-no-enforce-eager "Permanent link")

Whether to always use eager-mode PyTorch. If True, we will disable CUDA graph and always execute the model in eager mode. If False, we will use CUDA graph and eager execution in hybrid for maximal performance and flexibility.

NOTE: This disables both `torch.compile` and CUDA graphs, and is equivalent to setting `-cc.mode=none -cc.cudagraph_mode=none`.

Default: `False`

#### `--enable-return-routed-experts`, `--no-enable-return-routed-experts` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-return-routed-experts-no-enable-return-routed-experts "Permanent link")

Whether to return routed experts.Default: `False`

#### `--return-sampling-mask`, `--no-return-sampling-mask` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-return-sampling-mask-no-return-sampling-mask "Permanent link")

Whether to return the post-processing token support for each sample.Default: `False`

#### `--max-logprobs` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-logprobs "Permanent link")

Maximum number of log probabilities to return when `logprobs` is specified in [`SamplingParams`](https://docs.vllm.ai/en/stable/api/vllm/sampling_params/#vllm.sampling_params.SamplingParams "            SamplingParams"). The default value comes the default for the OpenAI Chat Completions API. -1 means no cap, i.e. all (output\_length \* vocab\_size) logprobs are allowed to be returned and it may cause OOM.Default: `20`

#### `--logprobs-mode` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-logprobs-mode "Permanent link")

Possible choices: `processed_logits`, `processed_logprobs`, `raw_logits`, `raw_logprobs`Indicates the content returned in the logprobs and prompt\_logprobs. Supported mode: 1) raw\_logprobs, 2) processed\_logprobs, 3) raw\_logits, 4) processed\_logits. Raw means the values before applying any logit processors, like bad words. Processed means the values after applying all processors, including temperature and top\_k/top\_p. Note: for prompt\_logprobs, processed\_ _and raw\__ yield identical results because prompt tokens do not go through sampling processors.Default: `raw_logprobs`

#### `--use-fp64-gumbel`, `--no-use-fp64-gumbel` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-use-fp64-gumbel-no-use-fp64-gumbel "Permanent link")

Whether to use FP64 (instead of FP32) random noise for Gumbel-max and equivalent exponential-race sampling. FP64 preserves lower-tail sampling events that fp32 uniform/exponential draws can truncate, at the cost of significantly lower throughput on most GPUs.Default: `False`

#### `--enable-trace-replay`, `--no-enable-trace-replay` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-trace-replay-no-enable-trace-replay "Permanent link")

Whether to allow requests to set `SamplingParams.trace_decode_token_ids`, which forces decoding to follow a predetermined token sequence while still computing real logprobs. Reserved for debugging and RL workflows: enabling it reserves a per-request trace buffer, so it is off by default.Default: `False`

#### `--disable-sliding-window`, `--no-disable-sliding-window` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-disable-sliding-window-no-disable-sliding-window "Permanent link")

Whether to disable sliding window. If True, we will disable the sliding window functionality of the model, capping to sliding window size. If the model does not support sliding window, this argument is ignored.Default: `False`

#### `--disable-cascade-attn`, `--no-disable-cascade-attn` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-disable-cascade-attn-no-disable-cascade-attn "Permanent link")

Disable cascade attention for V1. While cascade attention does not change the mathematical correctness, disabling it could be useful for preventing potential numerical issues. This defaults to True, so users must opt in to cascade attention by setting this to False. Even when this is set to False, cascade attention will only be used when the heuristic tells that it's beneficial.Default: `True`

#### `--skip-tokenizer-init`, `--no-skip-tokenizer-init` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-skip-tokenizer-init-no-skip-tokenizer-init "Permanent link")

Skip initialization of tokenizer and detokenizer. Expects valid `prompt_token_ids` and `None` for prompt from the input. The generated output will contain token ids.Default: `False`

#### `--enable-prompt-embeds`, `--no-enable-prompt-embeds` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-prompt-embeds-no-enable-prompt-embeds "Permanent link")

If `True`, enables passing text embeddings as inputs via the `prompt_embeds` key.

WARNING: The vLLM engine may crash if incorrect shape of embeddings is passed. Only enable this flag for trusted users!

Default: `False`

#### `--served-model-name` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-served-model-name "Permanent link")

The model name(s) used in the API. If multiple names are provided, the server will respond to any of the provided names. The model name in the model field of a response will be the first name in this list. If not specified, the model name will be the same as the `--model` argument. Noted that this name(s) will also be used in `model_name` tag content of prometheus metrics, if multiple names provided, metrics tag will take the first one.

#### `--config-format` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-config-format "Permanent link")

Possible choices: `auto`, `hf`, `mistral`

The format of the model config to load:

- "auto" will try to load the config in hf format if available after trying to load in mistral format.
- "hf" will load the config in hf format.
- "mistral" will load the config in mistral format.

Default: `auto`

#### `--hf-token` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-hf-token "Permanent link")

The token to use as HTTP bearer authorization for remote files . If `True`, will use the token generated when running `hf auth login` (stored in `~/.cache/huggingface/token`).

#### `--hf-overrides` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-hf-overrides "Permanent link")

If a dictionary, contains arguments to be forwarded to the Hugging Face config. If a callable, it is called to update the HuggingFace config.Default: `{}`

#### `--model-class-overrides` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-model-class-overrides "Permanent link")

Override the model class used for one or more architectures, mapping the architecture name to a `"module:class"` target (the same format accepted by `ModelRegistry.register_model`). This registers the target class at runtime, e.g. `{"GlmMoeDsaForCausalLM": "vllm.models.deepseek_v32.nvidia.model:DeepseekV32ForCausalLM"}`. This argument is for development and debugging purposes only.

Should either be a valid JSON string or JSON keys passed individually.

Default: `{}`

#### `--pooler-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-pooler-config "Permanent link")

Pooler config which controls the behaviour of output pooling in pooling models.

API docs: [`vllm.config.PoolerConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.PoolerConfig "            PoolerConfig")

Should either be a valid JSON string or JSON keys passed individually.

#### `--generation-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-generation-config "Permanent link")

The folder path to the generation config. Defaults to `"auto"`, the generation config will be loaded from model path. If set to `"vllm"`, no generation config is loaded, vLLM defaults will be used. If set to a folder path, the generation config will be loaded from the specified folder path. If `max_new_tokens` is specified in generation config, then it sets a server-wide limit on the number of output tokens for all requests.Default: `auto`

#### `--override-generation-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-override-generation-config "Permanent link")

Overrides or sets generation config. e.g. `{"temperature": 0.5}`. If used with `--generation-config auto`, the override parameters will be merged with the default config from the model. If used with `--generation-config vllm`, only the override parameters are used.

Should either be a valid JSON string or JSON keys passed individually.

Default: `{}`

#### `--enable-sleep-mode`, `--no-enable-sleep-mode` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-sleep-mode-no-enable-sleep-mode "Permanent link")

Enable sleep mode for the engine (only cuda and hip platforms are supported).Default: `False`

#### `--enable-cumem-allocator`, `--no-enable-cumem-allocator` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-cumem-allocator-no-enable-cumem-allocator "Permanent link")

Enable the custom cumem allocator to leverage advanced GPU memory allocation features such as multi-node NVLink support.

Sleep mode automatically enables this allocator. Only cuda and hip platforms are supported.

Default: `False`

#### `--enable-nccl-comm-suspend`, `--no-enable-nccl-comm-suspend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-nccl-comm-suspend-no-enable-nccl-comm-suspend "Permanent link")

Enable releasing NCCL communicator memory during sleep mode (`ncclCommSuspend`/`ncclCommResume`). Experimental; when disabled (the default) sleep still releases weights/KV-cache memory as before.Default: `False`

#### `--model-impl` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-model-impl "Permanent link")

Possible choices: `auto`, `terratorch`, `transformers`, `vllm`

Which implementation of the model to use:

- "auto" will try to use the vLLM implementation, if it exists, and fall back to the Transformers implementation if no vLLM implementation is available.
- "vllm" will use the vLLM model implementation.
- "transformers" will use the Transformers model implementation.
- "terratorch" will use the TerraTorch model implementation.

Default: `auto`

#### `--logits-processors` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-logits-processors "Permanent link")

One or more logits processors' fully-qualified class names or class definitions

#### `--io-processor-plugin` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-io-processor-plugin "Permanent link")

IOProcessor plugin name to load at model startup

#### `--renderer-num-workers` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-renderer-num-workers "Permanent link")

Number of worker threads in the renderer thread pool. The pool is consumed by the async renderer path (e.g. the OpenAI-compatible API server started by `vllm serve`) to parallelize tokenization, chat template rendering, and multimodal preprocessing across concurrent requests.

The offline [`LLM`](https://docs.vllm.ai/en/stable/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM "            LLM") entrypoint uses the synchronous renderer path and processes prompts (including multimodal preprocessing) serially, so this setting has no effect there.

Default: `1`

### LoadConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#loadconfig "Permanent link")

Configuration for loading the model weights.

#### `--load-format` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-load-format "Permanent link")

The format of the model weights to load.

- "auto" will try to load the weights in the safetensors format and fall back to the pytorch bin format if safetensors format is not available.
- "pt" will load the weights in the pytorch bin format.
- "safetensors" will load the weights in the safetensors format.
- "instanttensor" will load the Safetensors weights on CUDA devices using InstantTensor, which enables distributed loading with pipelined prefetching and fast direct I/O.
- "ipc\_cache" will map post-quantized weights from a local weight cache daemon via CUDA IPC for fast engine restarts. See `vllm/model_executor/model_loader/weight_cache/daemon.py` for how to launch the daemon.
- "npcache" will load the weights in pytorch format and store a numpy cache to speed up the loading.
- "dummy" will initialize the weights with random values, which is mainly for profiling.
- "tensorizer" will use CoreWeave's tensorizer library for fast weight loading. See the Tensorize vLLM Model script in the Examples section for more information.
- "runai\_streamer" will load the Safetensors weights using Run:ai Model Streamer.
- "runai\_streamer\_sharded" will load weights from pre-sharded checkpoint files using Run:ai Model Streamer.
- "sharded\_state" will load weights from pre-sharded checkpoint files, supporting efficient loading of tensor-parallel models.
- "mistral" will load weights from consolidated safetensors files used by Mistral models.
- "modelexpress" will load weights using ModelExpress.
- Other custom values can be supported via plugins.

Default: `auto`

#### `--download-dir` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-download-dir "Permanent link")

Directory to download and load the weights, default to the default cache directory of Hugging Face.

#### `--safetensors-load-strategy` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-safetensors-load-strategy "Permanent link")

Possible choices: `eager`, [`lazy`](https://docs.vllm.ai/en/stable/api/vllm/logging_utils/lazy/#vllm.logging_utils.lazy.lazy "            lazy"), `prefetch`, `torchao`, `None`

Specifies the loading strategy for safetensors weights.

- None (default): Uses memory-mapped (lazy) loading. When an NFS filesystem is detected and the total checkpoint size fits within 90%%%% of available RAM, prefetching is enabled automatically.
- "lazy": Weights are memory-mapped from the file. This enables on-demand loading and is highly efficient for models on local storage. Unlike the default (None), auto-prefetch on NFS is not performed.
- "eager": The entire file is read into CPU memory upfront before loading. This is recommended for models on network filesystems (e.g., Lustre, NFS) as it avoids inefficient random reads, significantly speeding up model initialization. However, it uses more CPU RAM.
- "prefetch": Checkpoint files are read into the OS page cache before workers load them, speeding up the model loading phase. Useful on network or high-latency storage.
- "torchao": Weights are loaded in upfront and then reconstructed into torchao tensor subclasses. This is used when the checkpoint was quantized using torchao and saved using safetensors. Needs `torchao >= 0.14.0`.

#### `--safetensors-prefetch-num-threads` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-safetensors-prefetch-num-threads "Permanent link")

Number of worker threads used to prefetch safetensors checkpoint files into the OS page cache when safetensors prefetching is enabled.Default: `8`

#### `--safetensors-prefetch-block-size` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-safetensors-prefetch-block-size "Permanent link")

Read size in bytes for each safetensors checkpoint file prefetch.

Parse human-readable integers like '1k', '2M', etc. Including decimal values with decimal multipliers.

```
Examples:
- '1k' -> 1,000
- '1K' -> 1,024
- '25.6k' -> 25,600
```

Default: `16777216`

#### `--model-loader-extra-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-model-loader-extra-config "Permanent link")

Extra config for model loader. This will be passed to the model loader corresponding to the chosen load\_format.Default: `{}`

#### `--ignore-patterns` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-ignore-patterns "Permanent link")

The list of patterns to ignore when loading the model. Default to "original/\* _/_" to avoid repeated loading of llama's checkpoints.Default: `['original/**/*']`

#### `--use-tqdm-on-load`, `--no-use-tqdm-on-load` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-use-tqdm-on-load-no-use-tqdm-on-load "Permanent link")

Whether to enable tqdm for showing progress bar when loading model weights.Default: `True`

#### `--pt-load-map-location` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-pt-load-map-location "Permanent link")

The map location for loading pytorch checkpoint, to support loading checkpoints can only be loaded on certain devices like "cuda", this is equivalent to `{"": "cuda"}`. Another supported format is mapping from different devices like from GPU 1 to GPU 0: `{"cuda:1": "cuda:0"}`. Note that when passed from command line, the strings in dictionary need to be double quoted for json parsing. For more details, see the original doc for `map_location` parameter in [`torch.load`](https://pytorch.org/docs/stable/generated/torch.load.html#torch.load) parameter.Default: `cpu`

### AttentionConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#attentionconfig "Permanent link")

Configuration for attention mechanisms in vLLM.

#### `--attention-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-attention-backend "Permanent link")

Attention backend to use. Use "auto" or None for automatic selection.

### MambaConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#mambaconfig "Permanent link")

Configuration for Mamba SSM backends.

#### `--mamba-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mamba-backend "Permanent link")

Mamba SSU backend to use.Default: `MambaBackendEnum.TRITON`

#### `--mamba-ssu-algorithm` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mamba-ssu-algorithm "Permanent link")

Possible choices: `auto`, `horizontal`, `simple`, `vertical`, `None`Selective state update algorithm to use with the FlashInfer backend. None defaults to FlashInfer's "auto" algorithm. Forced algorithms must be supported by FlashInfer for the active GPU, state dtype, and decoding mode.

#### `--enable-mamba-cache-stochastic-rounding`, `--no-enable-mamba-cache-stochastic-rounding` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-mamba-cache-stochastic-rounding-no-enable-mamba-cache-stochastic-rounding "Permanent link")

Enable stochastic rounding when writing SSM state to fp16 cache. Uses random bits to unbias the rounding error, which can improve numerical stability for long sequences.Default: `False`

#### `--mamba-cache-philox-rounds` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mamba-cache-philox-rounds "Permanent link")

Number of Philox PRNG rounds for stochastic rounding random number generation. 0 uses the Triton default. Higher values improve randomness quality at the cost of compute.Default: `0`

### StructuredOutputsConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#structuredoutputsconfig "Permanent link")

Dataclass which contains structured outputs config for the engine.

#### `--reasoning-parser` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-reasoning-parser "Permanent link")

Select the reasoning parser depending on the model that you're using. This is used to parse the reasoning content into OpenAI API format.Default: `""`

#### `--reasoning-parser-plugin` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-reasoning-parser-plugin "Permanent link")

Path to a dynamically reasoning parser plugin that can be dynamically loaded and registered.Default: `""`

### ParallelConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#parallelconfig "Permanent link")

Configuration for the distributed execution.

#### `--distributed-executor-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-distributed-executor-backend "Permanent link")

Possible choices: `external_launcher`, `mp`, `ray`, `uni`

Backend to use for distributed model workers, either "ray" or "mp" (multiprocessing). If the product of pipeline\_parallel\_size and tensor\_parallel\_size is less than or equal to the number of GPUs available, "mp" will be used to keep processing on a single host. Otherwise, an error will be raised. To use "mp" you must also set nnodes, and to use "ray" you must manually set distributed\_executor\_backend to "ray".

Note: [TPU](https://docs.vllm.ai/projects/tpu/en/latest/) platform only supports Ray for distributed inference.

#### `--pipeline-parallel-size`, `-pp` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-pipeline-parallel-size-pp "Permanent link")

Number of pipeline parallel groups.Default: `1`

#### `--master-addr` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-master-addr "Permanent link")

distributed master address for multi-node distributed inference when distributed\_executor\_backend is mp.Default: `127.0.0.1`

#### `--master-port` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-master-port "Permanent link")

distributed master port for multi-node distributed inference when distributed\_executor\_backend is mp.Default: `29501`

#### `--nnodes`, `-n` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-nnodes-n "Permanent link")

num of nodes for multi-node distributed inference when distributed\_executor\_backend is mp.Default: `1`

#### `--node-rank`, `-r` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-node-rank-r "Permanent link")

distributed node rank for multi-node distributed inference when distributed\_executor\_backend is mp.Default: `0`

#### `--distributed-timeout-seconds` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-distributed-timeout-seconds "Permanent link")

Timeout in seconds for distributed operations (e.g., init\_process\_group). If set, this value is passed to torch.distributed.init\_process\_group as the timeout parameter. If None, PyTorch's default timeout is used (600s for NCCL). Increase this for multi-node setups where model downloads may be slow.

#### `--cpu-distributed-timeout-seconds` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-cpu-distributed-timeout-seconds "Permanent link")

Timeout (in seconds) for cpu communication groups. If None, PyTorch's default timeout is used (1800s for gloo).

#### `--numa-bind`, `--no-numa-bind` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-numa-bind-no-numa-bind "Permanent link")

Enable NUMA binding for GPU worker subprocesses.

By default, workers are pinned to their GPU's NUMA-local CPUs and memory; on PCT-capable Xeons they also auto-bind to the SKU's PCT priority cores.

Default: `False`

#### `--numa-bind-nodes` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-numa-bind-nodes "Permanent link")

NUMA node to bind each GPU worker to.

Specify one NUMA node per visible GPU, for example `[0, 0, 1, 1]` for a 4-GPU system with GPUs 0-1 on NUMA node 0 and GPUs 2-3 on NUMA node 1. If unset and `numa_bind=True`, vLLM auto-detects the GPU-to-NUMA topology. The values are passed to `numactl --membind` and `--cpunodebind`, so they must be valid `numactl` NUMA node indices.

#### `--numa-bind-cpus` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-numa-bind-cpus "Permanent link")

Optional CPU lists to bind each GPU worker to.

Specify one CPU list per visible GPU, for example `["0-3", "4-7", "8-11", "12-15"]`. When set, vLLM uses `numactl --physcpubind` instead of `--cpunodebind`. This is useful for custom policies such as binding to PCT or other high-frequency cores. Each entry must use `numactl --physcpubind` CPU-list syntax, for example `"0-3"` or `"0,2,4-7"`.

#### `--device-ids` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-device-ids "Permanent link")

Comma-separated physical GPU device IDs or UUIDs to use (e.g. --device-ids "2,3,5,7"). Avoids setting CUDA\_VISIBLE\_DEVICES, preserving full GPU topology visibility for GPU-NIC affinity and DeepGEMM. Note: has no effect with Ray executors; use Ray placement groups for GPU selection instead.

#### `--tensor-parallel-size`, `-tp` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-tensor-parallel-size-tp "Permanent link")

Number of tensor parallel groups.Default: `1`

#### `--decode-context-parallel-size`, `-dcp` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-decode-context-parallel-size-dcp "Permanent link")

Number of ranks that shard the decode KV cache. DCP does not expand the process world size. Without PCP, DCP reuses TP ranks. With PCP, DCP either spans the PCP axis or the full TP x PCP block.Default: `1`

#### `--dcp-comm-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-dcp-comm-backend "Permanent link")

Possible choices: `a2a`, `ag_rs`, `None`

Communication backend for Decode Context Parallel (DCP). - "ag\_rs": AllGather + ReduceScatter (existing behavior) - "a2a": All-to-All exchange of partial outputs + LSE, then combine with Triton kernel. Reduces NCCL calls from 3 to 2 per layer for MLA models.

`None` selects the model default, which is "ag\_rs" unless the model overrides it via [`set_dcp_defaults`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.ParallelConfig.set_dcp_defaults "            set_dcp_defaults(comm_backend='ag_rs', q_replicate=False)").

#### `--dcp-q-replicate`, `--no-dcp-q-replicate` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-dcp-q-replicate-no-dcp-q-replicate "Permanent link")

Replicate the MLA query projection within each DCP group so decode can skip the query all-gather.

With DCP the KV cache is sharded across the group, so the standard MLA decode path all-gathers the query every step. Replicating the (small) query projection at load time lets each rank materialize the full group-local head set and skip that collective, at the cost of computing the projection redundantly on every rank in the group.

#### `--dcp-kv-cache-interleave-size` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-dcp-kv-cache-interleave-size "Permanent link")

Interleave size of kv\_cache storage while using DCP. dcp\_kv\_cache\_interleave\_size has been replaced by cp\_kv\_cache\_interleave\_size, and will be deprecated when PCP is fully supported.Default: `1`

#### `--cp-kv-cache-interleave-size` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-cp-kv-cache-interleave-size "Permanent link")

Interleave size of kv\_cache storage while using DCP. Store interleave\_size tokens on dcp\_rank i, then store next interleave\_size tokens on dcp\_rank i+1. Interleave\_size=1: token-level alignment, where token `i` is stored on dcp\_rank `i %% dcp_world_size`. Interleave\_size=block\_size: block-level alignment, where tokens are first populated to the preceding ranks. Tokens are then stored in (rank i+1, block j) only after (rank i, block j) is fully occupied. Block\_size should be greater than or equal to cp\_kv\_cache\_interleave\_size. Block\_size should be divisible by cp\_kv\_cache\_interleave\_size.

When --cp-kv-cache-interleave-size is omitted (None), the interleave size is resolved automatically based on NIXL transfer requirements. Explicit settings take priority.

#### `--prefill-context-parallel-size`, `-pcp` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-prefill-context-parallel-size-pcp "Permanent link")

Number of ranks that split prefill sequence computation. PCP expands the process world size but does not increase the KV-cache shard count.Default: `1`

#### `--data-parallel-size`, `-dp` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-data-parallel-size-dp "Permanent link")

Number of data parallel groups. MoE layers will be sharded according to the product of the tensor, prefill-context, and data parallel sizes.Default: `1`

#### `--data-parallel-rank`, `-dpn` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-data-parallel-rank-dpn "Permanent link")

Data parallel rank of this instance. When set, enables external load balancer mode for MoE data-parallel deployments. Unsupported for non-MoE models; launch independent vLLM instances instead.

#### `--data-parallel-start-rank`, `-dpr` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-data-parallel-start-rank-dpr "Permanent link")

Starting data parallel rank for secondary nodes.

#### `--data-parallel-size-local`, `-dpl` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-data-parallel-size-local-dpl "Permanent link")

Number of data parallel replicas to run on this node.

#### `--data-parallel-address`, `-dpa` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-data-parallel-address-dpa "Permanent link")

Address of data parallel cluster head-node.

#### `--data-parallel-rpc-port`, `-dpp` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-data-parallel-rpc-port-dpp "Permanent link")

Fixed port for data parallel RPC communication. All nodes must use the same port.

#### `--data-parallel-backend`, `-dpb` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-data-parallel-backend-dpb "Permanent link")

Backend for data parallel, either "mp" or "ray".Default: `mp`

#### `--data-parallel-hybrid-lb`, `--no-data-parallel-hybrid-lb`, `-dph` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-data-parallel-hybrid-lb-no-data-parallel-hybrid-lb-dph "Permanent link")

Whether to use "hybrid" DP LB mode. Applies only to online serving and when data\_parallel\_size > 0. Enables running an AsyncLLM and API server on a "per-node" basis where vLLM load balances between local data parallel ranks, but an external LB balances between vLLM nodes/replicas. Set explicitly in conjunction with --data-parallel-start-rank.Default: `False`

#### `--data-parallel-external-lb`, `--no-data-parallel-external-lb`, `-dpe` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-data-parallel-external-lb-no-data-parallel-external-lb-dpe "Permanent link")

Whether to use "external" DP LB mode. Applies only to online serving and when data\_parallel\_size > 0. This is useful for a "one-pod-per-rank" wide-EP setup in Kubernetes. Supported only for MoE deployments; non-MoE models should use independent vLLM instances without --data-parallel-\* arguments. Set implicitly when --data-parallel-rank is provided explicitly to vllm serve.Default: `False`

#### `--data-parallel-multi-port-external-lb`, `-dpm` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-data-parallel-multi-port-external-lb-dpm "Permanent link")

Run a node-local supervisor that launches one external-LB API server per local data parallel rank and exposes aggregated health on a supervisor port.Default: `False`

#### `--enable-expert-parallel`, `--no-enable-expert-parallel`, `-ep` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-expert-parallel-no-enable-expert-parallel-ep "Permanent link")

Use expert parallelism instead of tensor parallelism for MoE layers.Default: `False`

#### `--enable-batch-sharded-sampling`, `--no-enable-batch-sharded-sampling` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-batch-sharded-sampling-no-enable-batch-sharded-sampling "Permanent link")

Use sharded sampling across tensor parallel ranks. Each rank samples a slice of the batch instead of every rank sampling all of it. Currently defaults to False if not set. Enabling it explicitly raises when the config cannot support it (`tensor_parallel_size` must be > 1, `max_num_seqs` at least `tensor_parallel_size`, and `max_logprobs` non-negative). Models opt in by implementing `compute_logits_local`.

#### `--enable-ep-weight-filter`, `--no-enable-ep-weight-filter` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-ep-weight-filter-no-enable-ep-weight-filter "Permanent link")

Skip non-local expert weights during model loading when expert parallelism is active. Each rank only reads its own expert shard from disk, which can drastically reduce storage I/O for MoE models with per-expert weight tensors (e.g. DeepSeek, Mixtral, Kimi-K2.5). Has no effect on 3D fused-expert checkpoints (e.g. GPT-OSS) or non-MoE models.Default: `False`

#### `--all2all-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-all2all-backend "Permanent link")

Possible choices: `allgather_reducescatter`, `deepep_high_throughput`, `deepep_low_latency`, `deepep_v2`, `flashinfer_all2allv`, `flashinfer_nvlink_one_sided`, `flashinfer_nvlink_two_sided`, `mori_high_throughput`, `mori_low_latency`, `naive`, `nixl_ep`, `pplx`

All2All backend for MoE expert parallel communication. Available options:

- "allgather\_reducescatter": All2all based on allgather and reducescatter
- "deepep\_high\_throughput": Use deepep high-throughput kernels
- "deepep\_low\_latency": Use deepep low-latency kernels
- "mori\_high\_throughput": MoRI EP with InterNodeV1 for multi-node
- "mori\_low\_latency": MoRI EP with InterNodeV1LL for multi-node
- "nixl\_ep": Use nixl-ep kernels
- "flashinfer\_nvlink\_one\_sided": Use flashinfer high-throughput a2a kernels
- "flashinfer\_nvlink\_two\_sided": Use flashinfer two-sided kernels for mnnvl

Default: `allgather_reducescatter`

#### `--enable-dbo`, `--no-enable-dbo` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-dbo-no-enable-dbo "Permanent link")

Enable dual batch overlap for the model executor.Default: `False`

#### `--ubatch-size` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-ubatch-size "Permanent link")

Number of ubatch size.Default: `0`

#### `--enable-elastic-ep`, `--no-enable-elastic-ep` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-elastic-ep-no-enable-elastic-ep "Permanent link")

Enable elastic expert parallelism with stateless NCCL groups for DP/EP.Default: `False`

#### `--elastic-ep-max-dp-size` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-elastic-ep-max-dp-size "Permanent link")

Maximum data parallel size supported by elastic expert parallelism.

#### `--dbo-decode-token-threshold` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-dbo-decode-token-threshold "Permanent link")

The threshold for dual batch overlap for batches only containing decodes. If the number of tokens in the request is greater than this threshold, microbatching will be used. Otherwise, the request will be processed in a single batch.Default: `32`

#### `--dp-sync-interval` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-dp-sync-interval "Permanent link")

Steps between DP finish-sync all-reduces; must match across DP ranks.Default: `16`

#### `--dbo-prefill-token-threshold` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-dbo-prefill-token-threshold "Permanent link")

The threshold for dual batch overlap for batches that contain one or more prefills. If the number of tokens in the request is greater than this threshold, microbatching will be used. Otherwise, the request will be processed in a single batch.Default: `512`

#### `--disable-nccl-for-dp-synchronization`, `--no-disable-nccl-for-dp-synchronization` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-disable-nccl-for-dp-synchronization-no-disable-nccl-for-dp-synchronization "Permanent link")

Forces the dp synchronization logic in vllm/v1/worker/dp\_utils.py to use Gloo instead of NCCL for its all reduce.

Defaults to True when async scheduling is enabled, False otherwise.

#### `--enable-eplb`, `--no-enable-eplb` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-eplb-no-enable-eplb "Permanent link")

Enable expert parallelism load balancing for MoE layers.Default: `False`

#### `--eplb-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-eplb-config "Permanent link")

Expert parallelism configuration.

API docs: [`vllm.config.EPLBConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.EPLBConfig "            EPLBConfig")

Should either be a valid JSON string or JSON keys passed individually.

Default: `EPLBConfig(window_size=1000, step_interval=3000, num_redundant_experts=0, log_balancedness=False, log_balancedness_interval=1, use_async=True, policy='default', communicator=None)`

#### `--expert-placement-strategy` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-expert-placement-strategy "Permanent link")

Possible choices: `linear`, `round_robin`

The expert placement strategy for MoE layers:

- "linear": Experts are placed in a contiguous manner. For example, with 4 experts and 2 ranks, rank 0 will have experts \[0, 1\] and rank 1 will have experts \[2, 3\].
- "round\_robin": Experts are placed in a round-robin manner. For example, with 4 experts and 2 ranks, rank 0 will have experts \[0, 2\] and rank 1 will have experts \[1, 3\]. This strategy can help improve load balancing for grouped expert models with no redundant experts.

Default: `linear`

#### `--max-parallel-loading-workers` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-parallel-loading-workers "Permanent link")

Maximum number of parallel loading workers when loading model sequentially in multiple batches. To avoid RAM OOM when using tensor parallel and large models.

#### `--ray-workers-use-nsight`, `--no-ray-workers-use-nsight` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-ray-workers-use-nsight-no-ray-workers-use-nsight "Permanent link")

Whether to profile Ray workers with nsight, see https://docs.ray.io/en/latest/ray-observability/user-guides/profiling.html#profiling-nsight-profiler.Default: `False`

#### `--disable-custom-all-reduce`, `--no-disable-custom-all-reduce` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-disable-custom-all-reduce-no-disable-custom-all-reduce "Permanent link")

Disable the custom all-reduce kernel and fall back to NCCL.Default: `False`

#### `--worker-cls` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-worker-cls "Permanent link")

The full name of the worker class to use. If "auto", the worker class will be determined based on the platform.Default: `auto`

#### `--worker-extension-cls` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-worker-extension-cls "Permanent link")

The full name of the worker extension class to use. The worker extension class is dynamically inherited by the worker class. This is used to inject new attributes and methods to the worker class for use in collective\_rpc calls.Default: `""`

#### `--enable-fault-tolerance`, `--no-enable-fault-tolerance` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-fault-tolerance-no-enable-fault-tolerance "Permanent link")

Enable fault tolerance for detailed error recovery, such as scaling down fault DPEngineCore.Default: `False`

#### `--fault-tolerance-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-fault-tolerance-config "Permanent link")

The configurations for fault tolerance.

API docs: [`vllm.config.FaultToleranceConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.FaultToleranceConfig "            FaultToleranceConfig")

Should either be a valid JSON string or JSON keys passed individually.

Default: `FaultToleranceConfig(engine_recovery_timeout_sec=120)`

### CacheConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#cacheconfig "Permanent link")

Configuration for the KV cache.

#### `--block-size` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-block-size "Permanent link")

Size of a contiguous cache block in number of tokens. Accepts None (meaning "use default"). After construction, always int.

#### `--gpu-memory-utilization` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-gpu-memory-utilization "Permanent link")

The fraction of GPU memory to be used for the model executor, which can range from 0 to 1. For example, a value of 0.5 would imply 50%% GPU memory utilization. If unspecified, will use the default value of 0.92. This is a per-instance limit, and only applies to the current vLLM instance. It does not matter if you have another vLLM instance running on the same GPU. For example, if you have two vLLM instances running on the same GPU, you can set the GPU memory utilization to 0.5 for each instance.Default: `0.92`

#### `--kv-cache-memory-bytes` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kv-cache-memory-bytes "Permanent link")

Size of KV Cache per GPU in bytes. By default, this is set to None and vllm can automatically infer the kv cache size based on gpu\_memory\_utilization. However, users may want to manually specify the kv cache memory size. kv\_cache\_memory\_bytes allows more fine-grain control of how much memory gets used when compared with using gpu\_memory\_utilization. Note that kv\_cache\_memory\_bytes (when not-None) ignores gpu\_memory\_utilization

Parse human-readable integers like '1k', '2M', etc. Including decimal values with decimal multipliers.

```
Examples:
- '1k' -> 1,000
- '1K' -> 1,024
- '25.6k' -> 25,600
```

#### `--kv-cache-dtype` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kv-cache-dtype "Permanent link")

Possible choices: `auto`, `bfloat16`, `float16`, `fp8`, `fp8_ds_mla`, `fp8_e4m3`, `fp8_e5m2`, `fp8_inc`, `fp8_per_token_head`, `int4_per_token_head`, `int8_per_token_head`, `nvfp4`, `nvfp4_4over6`, `nvfp4_ds_mla`, `turboquant_3bit_nc`, `turboquant_4bit_nc`, `turboquant_k3v4_nc`, `turboquant_k8v4`Data type for kv cache storage. If "auto", will use model data type. CUDA 11.8+ supports fp8 (=fp8\_e4m3) and fp8\_e5m2. ROCm (AMD GPU) supports fp8 (=fp8\_e4m3). Intel Gaudi (HPU) supports fp8 (using fp8\_inc). Some models (namely DeepSeekV3.2) default to fp8, set to bfloat16 to use bfloat16 instead, this is an invalid option for models that do not default to fp8. "nvfp4\_4over6" uses the NVFP4 layout and selects between max/6 and max/4 scales per 16 values by minimizing squared reconstruction error.Default: `auto`

#### `--num-gpu-blocks-override` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-num-gpu-blocks-override "Permanent link")

Number of GPU blocks to use. This overrides the profiled `num_gpu_blocks` if specified. Does nothing if `None`. Used for testing preemption.

#### `--enable-prefix-caching`, `--no-enable-prefix-caching` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-prefix-caching-no-enable-prefix-caching "Permanent link")

Whether to enable prefix caching.

#### `--prefix-caching-hash-algo` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-prefix-caching-hash-algo "Permanent link")

Possible choices: `sha256`, `sha256_cbor`, `xxhash`, `xxhash_cbor`

Set the hash algorithm for prefix caching:

- "sha256" uses Pickle for object serialization before hashing. This is the current default, as SHA256 is the most secure choice to avoid potential hash collisions.
- "sha256\_cbor" provides a reproducible, cross-language compatible hash. It serializes objects using canonical CBOR and hashes them with SHA-256.
- "xxhash" uses Pickle serialization with xxHash (128-bit) for faster, non-cryptographic hashing. Requires the optional `xxhash` package. IMPORTANT: Use of a hashing algorithm that is not considered cryptographically secure theoretically increases the risk of hash collisions, which can cause undefined behavior or even leak private information in multi-tenant environments. Even if collisions are still very unlikely, it is important to consider your security risk tolerance against the performance benefits before turning this on.
- "xxhash\_cbor" combines canonical CBOR serialization with xxHash for reproducible hashing. Requires the optional `xxhash` package.

Default: `sha256`

#### `--prefix-cache-retention-interval` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-prefix-cache-retention-interval "Permanent link")

Token interval between retained sliding-window and Mamba prefix-cache checkpoints. `0` retains only semantic checkpoints, including the latest replay boundary and shared-prefix junctions. Positive values additionally retain periodic checkpoints at the specified interval, which must be a multiple of the scheduler block size. `None` retains checkpoints densely. Applies only to sliding-window and Mamba cache groups.Default: `0`

#### `--kv-cache-dtype-skip-layers` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kv-cache-dtype-skip-layers "Permanent link")

Layer patterns to skip KV cache quantization. Accepts layer indices (e.g., '0', '2', '4') or attention type names (e.g., 'sliding\_window').Default: `[]`

#### `--kv-sharing-fast-prefill`, `--no-kv-sharing-fast-prefill` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kv-sharing-fast-prefill-no-kv-sharing-fast-prefill "Permanent link")

In some KV sharing setups, e.g. YOCO (https://arxiv.org/abs/2405.05254), some layers can skip tokens corresponding to prefill. This flag enables attention metadata for eligible layers to be overridden with metadata necessary for implementing this optimization in some models (e.g. Gemma3n)Default: `False`

#### `--mamba-cache-dtype` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mamba-cache-dtype "Permanent link")

Possible choices: `auto`, `bfloat16`, `float16`, `float32`The data type to use for the Mamba cache (both the conv as well as the ssm state). If set to 'auto', the data type will be inferred from the model config.Default: `auto`

#### `--mamba-ssm-cache-dtype` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mamba-ssm-cache-dtype "Permanent link")

Possible choices: `auto`, `bfloat16`, `float16`, `float32`The data type to use for the Mamba cache (ssm state only, conv state will still be controlled by mamba\_cache\_dtype). If set to 'auto', the data type for the ssm state will be determined by mamba\_cache\_dtype.Default: `auto`

#### `--mamba-block-size` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mamba-block-size "Permanent link")

Size of a contiguous cache block in number of tokens for mamba cache. Can be set only when prefix caching is enabled. Value must be a multiple of 8 to align with causal\_conv1d kernel.

#### `--prefix-match-unit` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-prefix-match-unit "Permanent link")

The finest token boundary (in tokens) a prefix-cache hit can land on.

Prefix-cache keys are computed every `prefix_match_unit` tokens. It can be set finer than the physical KV cache block sizes (e.g. 32 vs a 1024-token hybrid-model block) as long as every KV cache group's `block_size` is divisible by it, enabling cache hits at boundaries inside a physical block. It controls matching granularity only, not how often states are stored.

This equals to the `hash_block_size` used throughout the KV cache code.

#### `--mamba-cache-mode` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mamba-cache-mode "Permanent link")

Possible choices: `align`, `all`, `none`

The cache strategy for Mamba layers:

- "none": set when prefix caching is disabled.
- "all": cache the mamba state of all tokens at position i \* block\_size.
- "align": only cache the mamba state of the last token of each scheduler step and when the token is at position i \* block\_size. This is the default when prefix caching is enabled.

Default: `none`

#### `--enable-mamba-fine-grained-prefix-cache`, `--no-enable-mamba-fine-grained-prefix-cache` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-mamba-fine-grained-prefix-cache-no-enable-mamba-fine-grained-prefix-cache "Permanent link")

Also register a Mamba "align" checkpoint at the shared-prefix junction -- where an EAGLE/MTP sibling was observed to resume -- instead of only at the prompt tail. Off by default; only takes effect with `mamba_cache_mode` "align", EAGLE on the Mamba group, and a prefix match unit smaller than the Mamba block size.Default: `False`

#### `--replayssm-buffer-len` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-replayssm-buffer-len "Permanent link")

ReplaySSM logical history length B for Mamba2. Triton uses B physical rows and FlashInfer uses B+1. Kimi-K3 speculative decode does not use B. Default 16.Default: `16`

#### `--use-replayssm`, `--no-use-replayssm` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-use-replayssm-no-use-replayssm "Permanent link")

Use the ReplaySSM Mamba2 decode kernel: cache recent SSM inputs and skip the per-step full-state store, writing the checkpoint back only on flush. Requires mamba\_cache\_mode 'none' or 'align' (prefix caching) and the Triton or FlashInfer mamba backend; standard (non-speculative) decode only. In align mode flushes are most efficient when mamba\_block\_size is a multiple of replayssm\_buffer\_len, but this is not required.Default: `False`

#### `--kv-offloading-size` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kv-offloading-size "Permanent link")

Size of the KV cache offloading buffer in GiB. When TP > 1, this is the total buffer size summed across all TP ranks. By default, this is set to None, which means no KV offloading is enabled. When set, vLLM will enable KV cache offloading to CPU using the kv\_offloading\_backend.

#### `--kv-offloading-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kv-offloading-backend "Permanent link")

Possible choices: `lmcache`, `native`The backend to use for KV cache offloading. Supported backends include 'native' (vLLM native CPU offloading), 'lmcache'. KV offloading is only activated when kv\_offloading\_size is set.Default: `native`

### OffloadConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#offloadconfig "Permanent link")

Configuration for model weight offloading to reduce GPU memory usage.

#### `--offload-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-offload-backend "Permanent link")

Possible choices: `auto`, `prefetch`, `uva`The backend for weight offloading. Options: - "auto": Selects based on which sub-config has non-default values (prefetch if offload\_group\_size > 0, uva if cpu\_offload\_gb > 0). - "uva": UVA (Unified Virtual Addressing) zero-copy offloading. - "prefetch": Async prefetch with group-based layer offloading.Default: `auto`

#### `--cpu-offload-gb` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-cpu-offload-gb "Permanent link")

The space in GiB to offload to CPU, per GPU. Default is 0, which means no offloading. Intuitively, this argument can be seen as a virtual way to increase the GPU memory size. For example, if you have one 24 GB GPU and set this to 10, virtually you can think of it as a 34 GB GPU. Then you can load a 13B model with BF16 weight, which requires at least 26GB GPU memory. Note that this requires fast CPU-GPU interconnect, as part of the model is loaded from CPU memory to GPU memory on the fly in each model forward pass. This uses UVA (Unified Virtual Addressing) for zero-copy access.Default: `0`

#### `--cpu-offload-params` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-cpu-offload-params "Permanent link")

The set of parameter name segments to target for CPU offloading. Unmatched parameters are not offloaded. If this set is empty, parameters are offloaded non-selectively until the memory limit defined by `cpu_offload_gb` is reached. Examples: - For parameter name "mlp.experts.w2\_weight": - "experts" or "experts.w2\_weight" will match. - "expert" or "w2" will NOT match (must be exact segments). This allows distinguishing parameters like "w2\_weight" and "w2\_weight\_scale".Default: `set()`

#### `--offload-group-size` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-offload-group-size "Permanent link")

Group every N layers together. Offload last `offload_num_in_group` layers of each group. Default is 0 (disabled). Example: group\_size=8, num\_in\_group=2 offloads layers 6,7,14,15,22,23,... Unlike cpu\_offload\_gb, this uses explicit async prefetching to hide transfer latency.Default: `0`

#### `--offload-num-in-group` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-offload-num-in-group "Permanent link")

Number of layers to offload per group. Must be <= offload\_group\_size. Default is 1.Default: `1`

#### `--offload-prefetch-step` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-offload-prefetch-step "Permanent link")

Number of layers to prefetch ahead. Higher values hide more latency but use more GPU memory. Default is 1.Default: `1`

#### `--offload-params` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-offload-params "Permanent link")

The set of parameter name segments to target for prefetch offloading. Unmatched parameters are not offloaded. If this set is empty, ALL parameters of each offloaded layer are offloaded. Uses segment matching: "w13\_weight" matches "mlp.experts.w13\_weight" but not "mlp.experts.w13\_weight\_scale".Default: `set()`

### MultiModalConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#multimodalconfig "Permanent link")

Controls the behavior of multimodal models.

#### `--language-model-only`, `--no-language-model-only` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-language-model-only-no-language-model-only "Permanent link")

If True, disables all multimodal inputs by setting all modality limits to 0. Equivalent to setting `--limit-mm-per-prompt` to 0 for every modality.Default: `False`

#### `--limit-mm-per-prompt` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-limit-mm-per-prompt "Permanent link")

The maximum number of input items and options allowed per prompt for each modality.

Defaults to 999 for each modality.

Legacy format (count only):

Configurable format (with options): {"video": {"count": 1, "num\_frames": 32, "width": 512, "height": 512}, "image": {"count": 5, "width": 512, "height": 512}}

Mixed format (combining both): {"image": 16, "video": {"count": 1, "num\_frames": 32, "width": 512, "height": 512}}

Should either be a valid JSON string or JSON keys passed individually.

Default: `{}`

#### `--enable-mm-embeds`, `--no-enable-mm-embeds` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-mm-embeds-no-enable-mm-embeds "Permanent link")

If `True`, enables passing multimodal embeddings: for [`LLM`](https://docs.vllm.ai/en/stable/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM "            LLM") class, this refers to tensor inputs under `multi_modal_data`; for the OpenAI-compatible server, this refers to chat messages with content `"type": "*_embeds"`.

When enabled with `--limit-mm-per-prompt` set to 0 for a modality, precomputed embeddings skip count validation for that modality, saving memory by not loading encoder modules while still enabling embeddings as an input. Limits greater than 0 still apply to embeddings.

WARNING: The vLLM engine may crash if incorrect shape of embeddings is passed. Only enable this flag for trusted users!

Default: `False`

#### `--media-io-kwargs` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-media-io-kwargs "Permanent link")

Additional args passed to process media inputs, keyed by modalities. For example, to set num\_frames for video, set `--media-io-kwargs '{"video": {"num_frames": 40} }'`

Should either be a valid JSON string or JSON keys passed individually.

Default: `{}`

#### `--mm-processor-kwargs` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-processor-kwargs "Permanent link")

Arguments to be forwarded to the model's processor for multi-modal data, e.g., image processor. Overrides for the multi-modal processor obtained from `transformers.AutoProcessor.from_pretrained`.

The available overrides depend on the model that is being run.

For example, for Phi-3-Vision: `{"num_crops": 4}`.

Should either be a valid JSON string or JSON keys passed individually.

#### `--mm-processor-cache-gb` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-processor-cache-gb "Permanent link")

The size (in GiB) of the multi-modal processor cache, which is used to avoid re-processing past multi-modal inputs.

This cache is duplicated for each API process and engine core process, resulting in a total memory usage of `mm_processor_cache_gb * (api_server_count + data_parallel_size)`.

A single processed item larger than this budget is served uncached (with a warning) instead of failing. Raise this value to cache such items.

Set to `0` to disable this cache completely (not recommended).

Default: `4`

#### `--mm-processor-cache-type` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-processor-cache-type "Permanent link")

Possible choices: `lru`, `shm`Type of cache to use for the multi-modal preprocessor/mapper. If `shm`, use shared memory FIFO cache. If `lru`, use mirrored LRU cache.Default: `lru`

#### `--mm-hasher-algorithm` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-hasher-algorithm "Permanent link")

Possible choices: `blake3`, `sha256`, `sha512`Hash algorithm to use for multi-modal input caching. Use `"sha256"` or `"sha512"` for FIPS-compliant deployments.Default: `blake3`

#### `--mm-shm-cache-max-object-size-mb` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-shm-cache-max-object-size-mb "Permanent link")

Size limit (in MiB) for each object stored in the multi-modal processor shared memory cache. Only effective when `mm_processor_cache_type` is `"shm"`.Default: `128`

#### `--mm-encoder-only`, `--no-mm-encoder-only` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-encoder-only-no-mm-encoder-only "Permanent link")

When enabled, skips the language component of the model.

This is usually only valid in disaggregated Encoder process.

Default: `False`

#### `--mm-encoder-tp-mode` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-encoder-tp-mode "Permanent link")

Possible choices: `data`, `weights`

Indicates how to optimize multi-modal encoder inference using tensor parallelism (TP).

- `"weights"`: Within the same vLLM engine, split the weights of each layer across TP ranks. (default TP behavior)
- `"data"`: Within the same vLLM engine, split the batched input data across TP ranks to process the data in parallel, while hosting the full weights on each TP rank. This batch-level DP is not to be confused with API request-level DP (which is controlled by `--data-parallel-size`). This is only supported on a per-model basis and falls back to `"weights"` if the encoder does not support DP.

Default: `weights`

#### `--mm-encoder-attn-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-encoder-attn-backend "Permanent link")

Optional override for the multi-modal encoder attention backend when using vision transformers. Accepts any value from `vllm.v1.attention.backends.registry.AttentionBackendEnum` (e.g. `FLASH_ATTN`).

#### `--mm-encoder-attn-dtype` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-encoder-attn-dtype "Permanent link")

Possible choices: `fp8`, `None`Optional dtype override for ViT encoder attention. Set to `"fp8"` to enable FP8 quantization via the FlashInfer cuDNN backend. When set to `"fp8"` without a scale file, dynamic scaling is used automatically. See docs/features/quantization/fp8\_vit\_attn.md for details.

#### `--mm-encoder-fp8-scale-path` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-encoder-fp8-scale-path "Permanent link")

Path to a JSON file containing per-layer FP8 Q/K/V scales for ViT encoder attention. When provided (with `mm_encoder_attn_dtype="fp8"`), static scaling is used. When omitted, dynamic scaling is used.

#### `--mm-encoder-fp8-scale-save-path` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-encoder-fp8-scale-save-path "Permanent link")

When set with dynamic FP8 scaling (`mm_encoder_attn_dtype="fp8"` and no `mm_encoder_fp8_scale_path`), saves the calibrated scales to this file after the amax history buffer is full. The saved file can then be used as `mm_encoder_fp8_scale_path` in subsequent runs.

#### `--mm-encoder-fp8-scale-save-margin` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-encoder-fp8-scale-save-margin "Permanent link")

Safety margin multiplied onto scales when auto-saving. A value > 1 leaves headroom so that inputs with larger activations than the calibration set do not overflow FP8 range. Default 1.5.Default: `1.5`

#### `--interleave-mm-strings`, `--no-interleave-mm-strings` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-interleave-mm-strings-no-interleave-mm-strings "Permanent link")

Enable fully interleaved support for multimodal prompts, while using --chat-template-content-format=string.Default: `False`

#### `--skip-mm-profiling`, `--no-skip-mm-profiling` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-skip-mm-profiling-no-skip-mm-profiling "Permanent link")

When enabled, skips multimodal memory profiling and only profiles with language backbone model during engine initialization.

This reduces engine startup time but shifts the responsibility to users for estimating the peak memory usage of the activation of multimodal encoder and embedding cache.

Default: `False`

#### `--video-pruning-rate` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-video-pruning-rate "Permanent link")

Fraction of video tokens to prune from each video. Value sits in range \[0;1); pruning is enabled when it is greater than 0. The pruning algorithm is selected by `video_pruning_method`.\
\
#### `--video-pruning-method` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-video-pruning-method "Permanent link")\
\
Possible choices: `evs`, `vidcom2`Video token pruning algorithm applied when `video_pruning_rate` \> 0: - "evs": Efficient Video Sampling. - "vidcom2": Video Compression Commander.Default: `evs`\
\
#### `--mm-tensor-ipc` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-tensor-ipc "Permanent link")\
\
Possible choices: `direct_rpc`, `torch_shm`IPC (inter-process communication) method for multimodal tensors. - "direct\_rpc": Use msgspec serialization via RPC - "torch\_shm": Use torch.multiprocessing shared memory for zero-copy IPC Defaults to "direct\_rpc".Default: `direct_rpc`\
\
#### `--mm-processor-device` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-processor-device "Permanent link")\
\
Possible choices: `auto`, `cpu`\
\
Device the HF multi-modal processor runs the image/video transform on. Convenience for `--mm-processor-kwargs '{"device": ...}'`: the value is resolved here and stored there, it is not kept as separate state. Only takes effect for HF "fast" (torchvision-backed) processors, which accept a `device` argument; the others ignore it and stay on CPU.\
\
"auto" uses the accelerator on encoder instances of an encode/prefill/decode deployment -- an EC producer that is not also a consumer allocates no KV cache, so its accelerator is not contended by the language model -- and then only when `--mm-tensor-ipc=torch_shm` can carry device tensors, since every other transport would copy the result back to the host and that copy costs more than it saves. "auto" resolves to "cpu" everywhere else.\
\
Default: `auto`\
\
#### `--mm-ipc-gpu-memory-gb` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-ipc-gpu-memory-gb "Permanent link")\
\
Amount of GPU memory (in GiB) sequestered on the engine's device for GPU-side multimodal work in the API-server (frontend) process, such as hardware video decoding.\
\
This budget is carved out of the engine's KV-cache memory so the headroom physically exists, and frontend GPU decode paths acquire from a blocking byte-counting semaphore of this size before allocating on the device.\
\
Set to `0` (default) to disable frontend GPU multimodal memory gating.\
\
Default: `0`\
\
#### `--mm-device-do-normalize`, `--no-mm-device-do-normalize` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-mm-device-do-normalize-no-mm-device-do-normalize "Permanent link")\
\
Move the do\_normalize computation in the mm preprocessing to before the ViT, and let the device do it, so that CPU computation can be saved.\
\
### LoRAConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#loraconfig "Permanent link")\
\
Configuration for LoRA.\
\
#### `--enable-lora`, `--no-enable-lora` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-lora-no-enable-lora "Permanent link")\
\
If True, enable handling of LoRA adapters.\
\
#### `--max-loras` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-loras "Permanent link")\
\
Max number of LoRAs in a single batch.Default: `1`\
\
#### `--max-lora-rank` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-lora-rank "Permanent link")\
\
Possible choices: `1`, `8`, `16`, `32`, `64`, `128`, `256`, `320`, `512`Max LoRA rank.Default: `16`\
\
#### `--lora-dtype` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-lora-dtype "Permanent link")\
\
Data type for LoRA. If auto, will default to base model dtype.Default: `auto`\
\
#### `--enable-tower-connector-lora`, `--no-enable-tower-connector-lora` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-tower-connector-lora-no-enable-tower-connector-lora "Permanent link")\
\
If `True`, LoRA support for the tower (vision encoder) and connector of multimodal models will be enabled. This is an experimental feature and currently only supports some MM models such as the Qwen VL series. The default is False.Default: `False`\
\
#### `--max-cpu-loras` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-cpu-loras "Permanent link")\
\
Maximum number of LoRAs to store in CPU memory. Must be >= than `max_loras`.\
\
#### `--fully-sharded-loras`, `--no-fully-sharded-loras` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-fully-sharded-loras-no-fully-sharded-loras "Permanent link")\
\
By default, only half of the LoRA computation is sharded with tensor parallelism. Enabling this will use the fully sharded layers. At high sequence length, max rank or tensor parallel size, this is likely faster.Default: `False`\
\
#### `--lora-target-modules` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-lora-target-modules "Permanent link")\
\
Restrict LoRA to specific module suffixes (e.g., \["o\_proj", "qkv\_proj"\]). If None, all supported LoRA modules are used. This allows deployment-time control over which modules have LoRA applied, useful for performance tuning.\
\
#### `--default-mm-loras` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-default-mm-loras "Permanent link")\
\
Dictionary mapping specific modalities to LoRA model paths; this field is only applicable to multimodal models and should be leveraged when a model always expects a LoRA to be active when a given modality is present. Note that currently, if a request provides multiple additional modalities, each of which have their own LoRA, we do NOT apply default\_mm\_loras because we currently only support one lora adapter per prompt. When run in offline mode, the lora IDs for n modalities will be automatically assigned to 1-n with the names of the modalities in alphabetic order.\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
#### `--specialize-active-lora`, `--no-specialize-active-lora` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-specialize-active-lora-no-specialize-active-lora "Permanent link")\
\
Whether to construct lora kernel grid by the number of active LoRA adapters. When set to True, separate cuda graphs will be captured for different counts of active LoRAs (powers of 2 up to max\_loras), which can improve performance for variable LoRA usage patterns at the cost of increased startup time and memory usage. Only takes effect when cudagraph\_specialize\_lora is True.Default: `False`\
\
#### `--enable-mixed-moe-lora-format`, `--no-enable-mixed-moe-lora-format` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-mixed-moe-lora-format-no-enable-mixed-moe-lora-format "Permanent link")\
\
If True, force the engine to use the universal 2D MoE LoRA wrapper (`FusedMoEWithLoRA`) regardless of the model's `is_3d_moe_weight` flag, so that 2D-format and 3D-format MoE LoRA adapters can be served in the same deployment. Only meaningful for MoE models; ignored otherwise. Default False keeps the existing model-driven behavior.Default: `False`\
\
#### `--enable-moe-shared-loras`, `--no-enable-moe-shared-loras` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-moe-shared-loras-no-enable-moe-shared-loras "Permanent link")\
\
If True, load MoE expert adapters in the "shared-outer" layout, where the gate/up (`w1`/`w3`) lora\_A and the down (`w2`) lora\_B are shared across all experts (stored once with expert-dim 1) instead of per-expert. The shared factors are broadcast to the expert count at kernel time. Only meaningful for MoE models whose adapters use this layout; ignored otherwise.Default: `False`\
\
### ObservabilityConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#observabilityconfig "Permanent link")\
\
Configuration for observability - metrics and tracing.\
\
#### `--show-hidden-metrics-for-version` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-show-hidden-metrics-for-version "Permanent link")\
\
Enable deprecated Prometheus metrics that have been hidden since the specified version. For example, if a previously deprecated metric has been hidden since the v0.7.0 release, you use `--show-hidden-metrics-for-version=0.7` as a temporary escape hatch while you migrate to new metrics. The metric is likely to be removed completely in an upcoming release.\
\
#### `--otlp-traces-endpoint` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-otlp-traces-endpoint "Permanent link")\
\
Target URL to which OpenTelemetry traces will be sent.\
\
#### `--collect-detailed-traces` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-collect-detailed-traces "Permanent link")\
\
Possible choices: `all`, `model`, `worker`, `None`, `model,worker`, `model,all`, `worker,model`, `worker,all`, `all,model`, `all,worker`\
\
It makes sense to set this only if `--otlp-traces-endpoint` is set. If set, it will collect detailed traces for the specified modules. This involves use of possibly costly and or blocking operations and hence might have a performance impact.\
\
Note that collecting detailed timing information for each request can be expensive.\
\
#### `--per-request-spec-decode-metrics` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-per-request-spec-decode-metrics "Permanent link")\
\
Possible choices: `detailed`, `none`, `summary`Include per-request speculative-decoding acceptance metrics in the response under `metrics.speculative_decoding`. `none` disables; `summary` adds mean acceptance length, draft acceptance rate, and the step-by-draft-length histogram; `detailed` additionally records the ordered per-step accepted/proposed arrays (one entry per verify step). Only reported for single-sequence requests (`n == 1`), mirroring the timing metrics. No effect unless speculative decoding is enabled. Independent of `--disable-log-stats`. This is the per-request response-body counterpart of the aggregate `vllm:spec_decode_*` Prometheus metrics. The response field is experimental and its shape may change in a future release.Default: `none`\
\
#### `--kv-cache-metrics`, `--no-kv-cache-metrics` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kv-cache-metrics-no-kv-cache-metrics "Permanent link")\
\
Enable KV cache residency metrics (lifetime, idle time, reuse gaps). Uses sampling to minimize overhead. Requires log stats to be enabled (i.e., --disable-log-stats not set).Default: `False`\
\
#### `--kv-cache-metrics-sample` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kv-cache-metrics-sample "Permanent link")\
\
Sampling rate for KV cache metrics (0.0, 1.0\]. Default 0.01 = 1%% of blocks.Default: `0.01`

#### `--cudagraph-metrics`, `--no-cudagraph-metrics` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-cudagraph-metrics-no-cudagraph-metrics "Permanent link")

Enable CUDA graph metrics (number of padded/unpadded tokens, runtime cudagraph dispatch modes, and their observed frequencies at every logging interval).Default: `False`

#### `--enable-layerwise-nvtx-tracing`, `--no-enable-layerwise-nvtx-tracing` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-layerwise-nvtx-tracing-no-enable-layerwise-nvtx-tracing "Permanent link")

Enable layerwise NVTX tracing. This traces the execution of each layer or module in the model and attach information such as input/output shapes to nvtx range markers. Noted that this doesn't work with CUDA graphs enabled.Default: `False`

#### `--enable-mfu-metrics`, `--no-enable-mfu-metrics` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-mfu-metrics-no-enable-mfu-metrics "Permanent link")

Enable Model FLOPs Utilization (MFU) metrics.Default: `False`

#### `--enable-logging-iteration-details`, `--no-enable-logging-iteration-details` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-logging-iteration-details-no-enable-logging-iteration-details "Permanent link")

Enable detailed logging of iteration details. If set, vllm EngineCore will log iteration details This includes number of context/generation requests and tokens and the elapsed cpu time for the iteration.Default: `False`

#### `--jit-monitor-mode` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-jit-monitor-mode "Permanent link")

Possible choices: `error`, `warn`How to handle post-warmup JIT compilation events.Default: `warn`

#### `--jit-monitor-verbose`, `--no-jit-monitor-verbose` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-jit-monitor-verbose-no-jit-monitor-verbose "Permanent link")

Log every monitored JIT compile with runtime details. This can emit many logs and add overhead, so it is intended for debugging.Default: `False`

### SchedulerConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#schedulerconfig "Permanent link")

Scheduler configuration.

#### `--max-num-batched-tokens` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-num-batched-tokens "Permanent link")

Maximum number of tokens that can be processed in a single iteration.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`.

Parse human-readable integers like '1k', '2M', etc. Including decimal values with decimal multipliers.

```
Examples:
- '1k' -> 1,000
- '1K' -> 1,024
- '25.6k' -> 25,600
```

#### `--max-num-scheduled-tokens` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-num-scheduled-tokens "Permanent link")

Maximum number of tokens that the scheduler may issue in a single iteration.

This is usually equal to max\_num\_batched\_tokens, but can be smaller in cases when the model might append tokens into the batch (such as speculative decoding). Defaults to max\_num\_batched\_tokens.

Parse human-readable integers like '1k', '2M', etc. Including decimal values with decimal multipliers.

```
Examples:
- '1k' -> 1,000
- '1K' -> 1,024
- '25.6k' -> 25,600
```

#### `--max-num-seqs` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-num-seqs "Permanent link")

Maximum number of sequences to be processed in a single iteration.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`.

#### `--max-num-queued-reqs` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-num-queued-reqs "Permanent link")

Maximum number of requests that can be in-flight (waiting or running) at the same time, or None for no limit. When the limit is reached, new requests are rejected with HTTP 503 so the client can retry on another instance. This bounds vLLM's otherwise unbounded request queue and is primarily a coarse capacity valve.

Unlike `max_num_seqs`, which applies per data-parallel rank, this limit is enforced in the API server process and counts in-flight requests across all DP ranks it routes to. Size it as roughly `data_parallel_size * max_num_seqs` plus the desired queue depth if it should not bind before per-rank admission does.

#### `--max-num-queued-tokens` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-num-queued-tokens "Permanent link")

Maximum total prompt tokens of requests currently in the prefill phase, or None for no limit. When the limit is reached, new requests are rejected with HTTP 503.

This is a TTFT QoS mechanism: by setting it to `target_TTFT * prefill_throughput` you reject requests when the prefill backlog would exceed the latency target. In a disaggregated prefill-decode setup this maps directly to the prefill pool's capacity.

Like `max_num_queued_reqs`, this limit is enforced in the API server process and covers the prefill backlog across all DP ranks it routes to, so `prefill_throughput` in the formula above is the aggregate throughput of the deployment.

Note: the count is conservative. A partially prefilled request still contributes its full `prompt_len` until it transitions out of the prefill phase, because the scheduler's per-iteration `num_computed_tokens` progress is not propagated to the API server process during prefill (`EngineCoreOutput` is only emitted once the request starts producing tokens). Similarly, prefix-cache hits (`num_cached_tokens`) are only known to the OutputProcessor after prefill completes. This overestimates the real backlog, causing earlier rejection than strictly necessary — the safe direction for QoS. The impact is limited to long prompts under chunked prefill; short prompts that prefill in a single iteration are unaffected.

Parse human-readable integers like '1k', '2M', etc. Including decimal values with decimal multipliers.

```
Examples:
- '1k' -> 1,000
- '1K' -> 1,024
- '25.6k' -> 25,600
```

#### `--long-prefill-token-threshold` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-long-prefill-token-threshold "Permanent link")

For chunked prefill, a request is considered long if the prompt is longer than this number of tokens. 0 disables the cap (default).Default: `0`

#### `--scheduling-policy` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-scheduling-policy "Permanent link")

Possible choices: `fcfs`, `priority`

The scheduling policy to use:

- "fcfs" means first come first served, i.e. requests are handled in order of arrival.
- "priority" means requests are handled based on given priority (lower value means earlier handling) and time of arrival deciding any ties).

Default: `fcfs`

#### `--enable-chunked-prefill`, `--no-enable-chunked-prefill` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-chunked-prefill-no-enable-chunked-prefill "Permanent link")

If True, prefill requests can be chunked based on the remaining `max_num_batched_tokens`.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`.

#### `--disable-chunked-mm-input`, `--no-disable-chunked-mm-input` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-disable-chunked-mm-input-no-disable-chunked-mm-input "Permanent link")

If set to true and chunked prefill is enabled, we do not want to partially schedule a multimodal item. Only used in V1 This ensures that if a request has a mixed prompt (like text tokens TTTT followed by image tokens IIIIIIIIII) where only some image tokens can be scheduled (like TTTTIIIII, leaving IIIII), it will be scheduled as TTTT in one step and IIIIIIIIII in the next.Default: `False`

#### `--scheduler-cls` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-scheduler-cls "Permanent link")

The scheduler class to use. "vllm.v1.core.sched.scheduler.Scheduler" is the default scheduler. Can be a class directly or the path to a class of form "mod.custom\_class".

#### `--scheduler-reserve-full-isl`, `--no-scheduler-reserve-full-isl` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-scheduler-reserve-full-isl-no-scheduler-reserve-full-isl "Permanent link")

If True, the scheduler checks whether the full input sequence length fits in the KV cache before admitting a new request, rather than only checking the first chunk. Prevents over-admission and KV cache thrashing with chunked prefill.Default: `True`

#### `--watermark` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-watermark "Permanent link")

Fraction of total KV cache blocks to keep free (the watermark) when admitting waiting or preempted requests into the running queue. This headroom helps avoid frequent KV cache eviction and the resulting repeated preemption of requests when GPU memory is scarce. Must be in the range \[0.0, 1.0); 0.0 (the default) disables the watermark.Default: `0.0`\
\
#### `--prefill-schedule-interval` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-prefill-schedule-interval "Permanent link")\
\
For data-parallel deployments, only admit new prefill requests once every N engine steps, aligned across DP ranks, to better balance per-step forward-pass times.Default: `1`\
\
#### `--disable-hybrid-kv-cache-manager`, `--no-disable-hybrid-kv-cache-manager` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-disable-hybrid-kv-cache-manager-no-disable-hybrid-kv-cache-manager "Permanent link")\
\
If set to True, KV cache manager will allocate the same size of KV cache for all attention layers even if there are multiple type of attention layers like full attention and sliding window attention. If set to None, the default value will be determined based on the environment and starting configuration.\
\
#### `--async-scheduling`, `--no-async-scheduling` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-async-scheduling-no-async-scheduling "Permanent link")\
\
If set to False, disable async scheduling. Async scheduling helps to avoid gaps in GPU utilization, leading to better latency and throughput.\
\
#### `--stream-interval` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-stream-interval "Permanent link")\
\
The interval (or buffer size) for streaming in terms of token length. A smaller value (1) makes streaming smoother by sending each token immediately, while a larger value (e.g., 10) reduces host overhead and may increase throughput by batching multiple tokens before sending.Default: `1`\
\
### CompilationConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#compilationconfig "Permanent link")\
\
Configuration for compilation.\
\
You must pass CompilationConfig to VLLMConfig constructor. VLLMConfig's post\_init does further initialization. If used outside of the VLLMConfig, some fields will be left in an improper state.\
\
It contains PassConfig, which controls the custom fusion/transformation passes. The rest has three parts:\
\
- Top-level Compilation control:\
  - [`mode`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.mode "            mode = None           class-attribute       instance-attribute   ")\
  - [`debug_dump_path`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.debug_dump_path "            debug_dump_path = None           class-attribute       instance-attribute   ")\
  - [`cache_dir`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.cache_dir "            cache_dir = ''           class-attribute       instance-attribute   ")\
  - [`backend`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.backend "            backend = ''           class-attribute       instance-attribute   ")\
  - [`custom_ops`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.custom_ops "            custom_ops = field(default_factory=list)           class-attribute       instance-attribute   ")\
  - [`splitting_ops`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.splitting_ops "            splitting_ops = None           class-attribute       instance-attribute   ")\
  - [`compile_mm_encoder`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.compile_mm_encoder "            compile_mm_encoder = False           class-attribute       instance-attribute   ")\
- CudaGraph capture:\
  - [`cudagraph_mode`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.cudagraph_mode "            cudagraph_mode = None           class-attribute       instance-attribute   ")\
  - [`cudagraph_capture_sizes`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.cudagraph_capture_sizes "            cudagraph_capture_sizes = None           class-attribute       instance-attribute   ")\
  - [`max_cudagraph_capture_size`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.max_cudagraph_capture_size "            max_cudagraph_capture_size = None           class-attribute       instance-attribute   ")\
  - [`cudagraph_num_of_warmups`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.cudagraph_num_of_warmups "            cudagraph_num_of_warmups = 0           class-attribute       instance-attribute   ")\
  - [`cudagraph_copy_inputs`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.cudagraph_copy_inputs "            cudagraph_copy_inputs = False           class-attribute       instance-attribute   ")\
- Inductor compilation:\
  - [`compile_sizes`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.compile_sizes "            compile_sizes = None           class-attribute       instance-attribute   ")\
  - \[`compile_ranges_endpoints`\] \[vllm.config.CompilationConfig.compile\_ranges\_endpoints\]\
  - [`inductor_compile_config`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.inductor_compile_config "            inductor_compile_config = field(default_factory=dict)           class-attribute       instance-attribute   ")\
  - [`inductor_passes`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig.inductor_passes "            inductor_passes = field(default_factory=dict)           class-attribute       instance-attribute   ")\
  - custom inductor passes\
\
Why we have different sizes for cudagraph and inductor: - cudagraph: a cudagraph captured for a specific size can only be used for the same size. We need to capture all the sizes we want to use. - inductor: a graph compiled by inductor for a general shape can be used for different sizes. Inductor can also compile for specific sizes, where it can have more information to optimize the graph with fully static shapes. However, we find the general shape compilation is sufficient for most cases. It might be beneficial to compile for certain small batchsizes, where inductor is good at optimizing.\
\
#### `--cudagraph-capture-sizes` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-cudagraph-capture-sizes "Permanent link")\
\
Sizes to capture cudagraph. - None (default): capture sizes are inferred from vllm config. - list\[int\]: capture sizes are specified as given.\
\
#### `--max-cudagraph-capture-size` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-max-cudagraph-capture-size "Permanent link")\
\
The maximum cudagraph capture size.\
\
If cudagraph\_capture\_sizes is specified, this will be set to the largest size in that list (or checked for consistency if specified). If cudagraph\_capture\_sizes is not specified, the list of sizes is generated automatically following the pattern:\
\
```\
[1, 2, 4] + list(range(8, 256, 8)) + list(\
range(256, max_cudagraph_capture_size + 1, 16))\
```\
\
If not specified, max\_cudagraph\_capture\_size is capped at 512 by default, or 1024 on data center Blackwell GPUs. This avoids OOM in tight memory scenarios with small max\_num\_seqs, and limits capture of large graphs that increase startup time and memory usage. Uniform decode sizes are appended only within this default ceiling.\
\
### KernelConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#kernelconfig "Permanent link")\
\
Configuration for kernel selection and warmup behavior.\
\
#### `--ir-op-priority` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-ir-op-priority "Permanent link")\
\
vLLM IR op priority for dispatching/lowering during the forward pass. Platform defaults appended automatically during VllmConfig. **post\_init**.\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
Default: `IrOpPriorityConfig(rms_norm=[], fused_add_rms_norm=[], gelu_and_mul_sparse=[])`\
\
#### `--enable-flashinfer-autotune`, `--no-enable-flashinfer-autotune` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-flashinfer-autotune-no-enable-flashinfer-autotune "Permanent link")\
\
If True, run FlashInfer autotuning during kernel warmup.\
\
#### `--moe-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-moe-backend "Permanent link")\
\
Possible choices: `aiter`, `aiter_triton_mxfp4_bf16`, `auto`, `b12x`, `batched_triton`, `cutlass`, `deep_gemm`, `deep_gemm_mega_moe`, `emulation`, `flashinfer_b12x`, `flashinfer_cutedsl`, `flashinfer_cutlass`, `flashinfer_moe_ep_mega_cutedsl`, `flashinfer_moe_ep_mega_deep_gemm`, `flashinfer_trtllm`, `flydsl`, `hpc`, `humming`, `marlin`, `rdna3`, `triton`, `triton_unfused`\
\
Backend for MoE expert computation kernels. Available options:\
\
- "auto": Automatically select the best backend based on model and hardware\
- "triton": Use Triton-based fused MoE kernels\
- "batched\_triton": Use batched Triton experts (moe\_mmk) on the batched activation format (\[E\_local, max\_num\_tokens, K\])\
- "deep\_gemm": Use DeepGEMM kernels (FP8 block-quantized only)\
- "deep\_gemm\_mega\_moe": Use DeepGEMM mega MoE kernels\
- "cutlass": Use vLLM CUTLASS kernels\
- "flashinfer\_trtllm": Use FlashInfer with TRTLLM-GEN kernels\
- "flashinfer\_cutlass": Use FlashInfer with CUTLASS kernels\
- "flashinfer\_cutedsl": Use FlashInfer with CuteDSL kernels (FP4 only)\
- "flashinfer\_b12x": Use FlashInfer CuteDSL fused MoE for SM12x (RTX Pro 6000 / DGX Spark)\
- "b12x": Use b12x FP4 MoE kernels on SM12x\
- "flashinfer\_moe\_ep\_mega\_deep\_gemm": Use the FlashInfer moe\_ep expert-parallel mega-MoE with the DeepGEMM megakernel, which consumes an MXFP4 checkpoint verbatim (Blackwell, requires expert parallel; DeepSeek-V4 only)\
- "flashinfer\_moe\_ep\_mega\_cutedsl": Same, with the CuteDSL megakernel (additionally requires NVSHMEM). The checkpoint selects the weight path: an NVFP4 checkpoint is consumed prequantized, MXFP4 weights are requantized at load\
- "marlin": Use Marlin kernels (weight-only quantization)\
- "humming": Use Humming Mixed Precision kernels\
- "triton\_unfused": Use Triton unfused MoE kernels\
- "aiter": Use AMD AITer kernels (ROCm only)\
- "aiter\_triton\_mxfp4\_bf16": Use the AITER Triton MXFP4 W4A16 (moe\_gemm\_a16w4) MoE kernel (ROCm gfx942/gfx950/gfx1250)\
- "flydsl": Use AMD FlyDSL kernels (ROCm only)\
- "rdna3": Use the fused RDNA3 W4A16 HIP kernel (ROCm gfx1100 only)\
- "hpc": Use HPC kernels (FP8 and Hopper only)\
- "emulation": use BF16/FP16 GEMM, dequantizing weights and running QDQ on activations.\
\
Default: `auto`\
\
#### `--linear-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-linear-backend "Permanent link")\
\
Possible choices: `aiter`, `auto`, `b12x`, `conch`, `cutlass`, `deep_gemm`, `emulation`, `exllama`, `fbgemm`, `flashinfer_b12x`, `flashinfer_cudnn`, `flashinfer_cutedsl`, `flashinfer_cutlass`, `flashinfer_trtllm`, `humming`, `machete`, `marlin`, `torch`, `triton`, `xpu`, `xpu_woq`\
\
Backend for linear layer GEMM kernels. Available options:\
\
Layer types without an implementation from the requested backend use automatic selection.\
\
- "auto": Automatically select the best backend based on model and hardware\
- "cutlass": Use CUTLASS-based kernels\
- "flashinfer\_cutlass": Use FlashInfer with CUTLASS kernels\
- "flashinfer\_cutedsl": Use FlashInfer with CuTe-DSL kernels (BF16, NVFP4, MXFP8, W4A16\_NVFP4)\
- "flashinfer\_trtllm": Use FlashInfer with TensorRT-LLM kernels\
- "flashinfer\_cudnn": Use FlashInfer with cuDNN kernels\
- "flashinfer\_b12x": Use FlashInfer b12x CuteDSL NVFP4 GEMM (SM120+)\
- "b12x": Use native B12X FP8 and FP4 linear kernels on SM12x\
- "marlin": Use Marlin kernels\
- "triton": Use Triton-based kernels\
- "deep\_gemm": Use DeepGEMM kernels\
- "torch": Use PyTorch native scaled\_mm kernels\
- "aiter": Use AMD AITer kernels (ROCm only)\
- "machete": Use Machete kernels (mixed-precision)\
- "fbgemm": Use FBGEMM kernels\
- "conch": Use Conch mixed-precision kernels\
- "exllama": Use Exllama mixed-precision kernels\
- "emulation": Use slow dequant-to-BF16 emulation (for testing only)\
- "xpu": Use XPU kernels\
- "xpu\_woq": Use XPU kernels for weight-only quantization (e.g. W8A16)\
\
Default: `auto`\
\
#### `--sparse-indexer-topk-backend` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-sparse-indexer-topk-backend "Permanent link")\
\
Possible choices: `auto`, `cooperative`, `deep_select`, `flashinfer`, `per_row`, `persistent`, `torch`\
\
Backend for the DSA sparse indexer decode top-k kernel. Available options:\
\
- "auto": The pre-existing chain (cooperative -> persistent -> per\_row); the other backends are opt-in\
- "deep\_select": Use DeepSelect kernels (SM100a/SM103a only)\
- "cooperative": Use vLLM's cooperative\_topk kernel\
- "persistent": Use vLLM's persistent\_topk kernel\
- "per\_row": Use vLLM's top\_k\_per\_row\_decode kernel\
- "flashinfer": Use FlashInfer's top\_k\_ragged\_transform kernel\
- "torch": Use a plain torch.topk implementation (debug reference)\
\
Explicit values raise RuntimeError when their constraints are not met.\
\
Default: `auto`\
\
### VllmConfig [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#vllmconfig "Permanent link")\
\
Dataclass which contains all vllm-related configuration. This simplifies passing around the distinct configurations in the codebase.\
\
#### `--speculative-config`, `-sc` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-speculative-config-sc "Permanent link")\
\
Speculative decoding configuration.\
\
API docs: [`vllm.config.SpeculativeConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.SpeculativeConfig "            SpeculativeConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
#### `--spec-method` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-spec-method "Permanent link")\
\
Possible choices: `bailing_hybrid_mtp`, `bailing_hybrid_v3_mtp`, `custom_class`, `deepseek_mtp`, `dflash`, `dots3_note_mtp`, `draft_model`, `dspark`, `eagle`, `eagle3`, `ernie_mtp`, `exaone4_5_mtp`, `exaone_moe_mtp`, `extract_hidden_states`, `gemma4_mtp`, `glm4_moe_lite_mtp`, `glm4_moe_mtp`, `glm5_next_mtp`, `glm_ocr_mtp`, `hy_v3_mtp`, `hy_v4_mtp`, `inkling_mtp`, `kimi_k3_mtp`, `longcat_flash_mtp`, `medusa`, `mimo_mtp`, `mimo_v2_mtp`, `minimax_m3_mtp`, `mlp_speculator`, `mtp`, `nemotron_h_mtp`, `ngram`, `ngram_gpu`, `pangu_ultra_moe_mtp`, `qwen3_5_mtp`, `qwen3_next_mtp`, `qwen4_exp_mtp`, `step3p5_mtp`, `suffix`, `None`\
\
The name of the speculative method to use. If users provide and set the `model` param, the speculative method type will be detected automatically if possible, if `model` param is not provided, the method name must be provided.\
\
If using `ngram` method, the related configuration `prompt_lookup_max` and `prompt_lookup_min` should be considered.\
\
#### `--spec-model` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-spec-model "Permanent link")\
\
The name of the draft model, eagle head, or additional weights, if provided.\
\
#### `--spec-tokens` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-spec-tokens "Permanent link")\
\
The number of speculative tokens, if provided. It will default to the number in the draft model config if present, otherwise, it is required.\
\
#### `--watermark-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-watermark-config "Permanent link")\
\
Text watermarking configuration.\
\
API docs: [`vllm.config.WatermarkConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.WatermarkConfig "            WatermarkConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
#### `--diffusion-config`, `-dc` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-diffusion-config-dc "Permanent link")\
\
Diffusion LLM (dLLM) configuration.\
\
API docs: [`vllm.config.DiffusionConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.DiffusionConfig "            DiffusionConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
#### `--kv-transfer-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kv-transfer-config "Permanent link")\
\
The configurations for distributed KV cache transfer.\
\
API docs: [`vllm.config.KVTransferConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.KVTransferConfig "            KVTransferConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
#### `--kv-events-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kv-events-config "Permanent link")\
\
The configurations for event publishing.\
\
API docs: [`vllm.config.KVEventsConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.KVEventsConfig "            KVEventsConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
#### `--ec-transfer-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-ec-transfer-config "Permanent link")\
\
The configurations for distributed EC cache transfer.\
\
API docs: [`vllm.config.ECTransferConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.ECTransferConfig "            ECTransferConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
#### `--ec-manager-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-ec-manager-config "Permanent link")\
\
The configurations for custom encoder cache manager.\
\
API docs: [`vllm.config.EncoderCacheManagerConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.EncoderCacheManagerConfig "            EncoderCacheManagerConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
Default: `EncoderCacheManagerConfig(encoder_cache_manager_cls=None, manager_config={})`\
\
#### `--compilation-config`, `-cc` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-compilation-config-cc "Permanent link")\
\
`torch.compile` and cudagraph capture configuration for the model.\
\
As a shorthand, one can append compilation arguments via -cc.parameter=argument such as `-cc.mode=3` (same as `-cc='{"mode":3}'`).\
\
You can specify the full compilation config like so: `{"mode": 3, "cudagraph_capture_sizes": [1, 2, 4, 8]}`\
\
API docs: [`vllm.config.CompilationConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.CompilationConfig "            CompilationConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
Default: `{'mode': None, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': [], 'ir_enable_torch_wrap': None, 'splitting_ops': None, 'compile_mm_encoder': False, 'cudagraph_mm_encoder': False, 'encoder_cudagraph_token_budgets': [], 'encoder_cudagraph_max_vision_items_per_batch': 0, 'encoder_cudagraph_max_frames_per_batch': None, 'compile_sizes': None, 'compile_ranges_endpoints': None, 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': None, 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': None, 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': None, 'pass_config': {}, 'max_cudagraph_capture_size': None, 'dynamic_shapes_config': {'type': <DynamicShapesType.BACKED: 'backed'>, 'evaluate_guards': False, 'assume_32_bit_indexing': False}, 'local_cache_dir': None, 'fast_moe_cold_start': None, 'static_all_moe_layers': []}`\
\
#### `--attention-config`, `-ac` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-attention-config-ac "Permanent link")\
\
Attention configuration.\
\
API docs: [`vllm.config.AttentionConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.AttentionConfig "            AttentionConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
Default: `AttentionConfig(backend=None, minimax_m3_msa_decode_backend='triton', backend_per_kind={}, flash_attn_version=None, flash_attn_max_num_splits_for_cuda_graph=32, tq_max_kv_splits_for_cuda_graph=32, use_trtllm_attention=None, disable_flashinfer_q_quantization=False, mla_prefill_backend=None, use_prefill_query_quantization=False, indexer_kv_dtype='auto', hisparse_config=None, use_non_causal=False, sparse_mla_force_mqa=False, flex_attn_block_m=None, flex_attn_block_n=None, flex_attn_q_block_size=None, flex_attn_kv_block_size=None)`\
\
#### `--engram-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-engram-config "Permanent link")\
\
N-gram embedding storage and sharding settings.\
\
API docs: [`vllm.config.EngramConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.EngramConfig "            EngramConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
#### `--reasoning-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-reasoning-config "Permanent link")\
\
The configurations for reasoning model.\
\
API docs: [`vllm.config.ReasoningConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.ReasoningConfig "            ReasoningConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
#### `--kernel-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-kernel-config "Permanent link")\
\
Kernel configuration.\
\
API docs: [`vllm.config.KernelConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.KernelConfig "            KernelConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
Default: `KernelConfig(ir_op_priority=IrOpPriorityConfig(rms_norm=[], fused_add_rms_norm=[], gelu_and_mul_sparse=[]), enable_flashinfer_autotune=None, enable_cutedsl_warmup=True, enable_jit_warmup=True, moe_backend='auto', sparse_indexer_topk_backend='auto', linear_backend='auto', linear_backend_per_quant=None)`\
\
#### `--additional-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-additional-config "Permanent link")\
\
Additional config for specified platform. Different platforms may support different configs. Make sure the configs are valid for the platform you are using. Contents must be hashable.Default: `{}`\
\
#### `--structured-outputs-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-structured-outputs-config "Permanent link")\
\
Structured outputs configuration.\
\
API docs: [`vllm.config.StructuredOutputsConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.StructuredOutputsConfig "            StructuredOutputsConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
Default: `StructuredOutputsConfig(backend='auto', disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enable_in_reasoning=False)`\
\
#### `--profiler-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-profiler-config "Permanent link")\
\
Profiling configuration.\
\
API docs: [`vllm.config.ProfilerConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.ProfilerConfig "            ProfilerConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
Default: `ProfilerConfig(profiler=None, torch_profiler_dir='', proton_profiler_dir='', proton_context='shadow', proton_data='tree', proton_backend=None, proton_mode=None, proton_hook=None, proton_output_format=None, proton_graph_attribution=False, torch_profiler_with_stack=True, torch_profiler_with_flops=False, torch_profiler_use_gzip=True, torch_profiler_dump_cuda_time_total=True, torch_profiler_record_shapes=False, torch_profiler_with_memory=False, capture_torch_profiler=False, detailed_trace_annotation=False, ignore_frontend=False, delay_iterations=0, max_iterations=0, warmup_iterations=0, active_iterations=5, wait_iterations=0)`\
\
#### `--optimization-level` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-optimization-level "Permanent link")\
\
The optimization level. These levels trade startup time cost for performance, with -O0 having the best startup time and -O3 having the best performance. -O2 is used by default. See OptimizationLevel for full description.Default: `2`\
\
#### `--performance-mode` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-performance-mode "Permanent link")\
\
Possible choices: `balanced`, `interactivity`, `throughput`Performance mode for runtime behavior, 'balanced' is the default. 'interactivity' favors low end-to-end per-request latency at small batch sizes (fine-grained CUDA graphs, latency-oriented kernels). 'throughput' favors aggregate tokens/sec at high concurrency (larger CUDA graphs, more aggressive batching, throughput-oriented kernels).Default: `balanced`\
\
#### `--weight-transfer-config` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-weight-transfer-config "Permanent link")\
\
The configurations for weight transfer during RL training.\
\
API docs: [`vllm.config.WeightTransferConfig`](https://docs.vllm.ai/en/stable/api/vllm/config/#vllm.config.WeightTransferConfig "            WeightTransferConfig")\
\
Should either be a valid JSON string or JSON keys passed individually.\
\
## [`AsyncEngineArgs`](https://docs.vllm.ai/en/stable/api/vllm/engine/arg_utils/\#vllm.engine.arg_utils.AsyncEngineArgs "            AsyncEngineArgs            dataclass   ") [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#asyncengineargs "Permanent link")\
\
#### `--enable-log-requests`, `--no-enable-log-requests` [¶](https://docs.vllm.ai/en/stable/configuration/engine_args/\#-enable-log-requests-no-enable-log-requests "Permanent link")\
\
Enable logging request information, dependent on log level: - INFO: Request ID, parameters and LoRA request. - DEBUG: Prompt inputs (e.g: text, token IDs). You can set the minimum log level via `VLLM_LOGGING_LEVEL`.Default: `False`\
\
Back to top\
\
Versions[latest](https://docs.vllm.ai/en/latest/configuration/engine_args/)**[stable](https://docs.vllm.ai/en/stable/configuration/engine_args/)**[v0.30.0](https://docs.vllm.ai/en/v0.30.0/configuration/engine_args/)[v0.29.0](https://docs.vllm.ai/en/v0.29.0/configuration/engine_args/)[v0.28.0](https://docs.vllm.ai/en/v0.28.0/configuration/engine_args/)[v0.27.1](https://docs.vllm.ai/en/v0.27.1/configuration/engine_args/)[v0.27.0](https://docs.vllm.ai/en/v0.27.0/configuration/engine_args/)[v0.26.0](https://docs.vllm.ai/en/v0.26.0/configuration/engine_args/)[v0.25.1](https://docs.vllm.ai/en/v0.25.1/configuration/engine_args/)[v0.25.0](https://docs.vllm.ai/en/v0.25.0/configuration/engine_args/)[v0.24.0](https://docs.vllm.ai/en/v0.24.0/configuration/engine_args/)[v0.23.0](https://docs.vllm.ai/en/v0.23.0/configuration/engine_args/)[v0.22.1](https://docs.vllm.ai/en/v0.22.1/configuration/engine_args/)[v0.22.0](https://docs.vllm.ai/en/v0.22.0/configuration/engine_args/)[v0.21.0](https://docs.vllm.ai/en/v0.21.0/configuration/engine_args/)[v0.20.2](https://docs.vllm.ai/en/v0.20.2/configuration/engine_args/)[v0.20.1](https://docs.vllm.ai/en/v0.20.1/configuration/engine_args/)[v0.20.0](https://docs.vllm.ai/en/v0.20.0/configuration/engine_args/)[v0.19.1](https://docs.vllm.ai/en/v0.19.1/configuration/engine_args/)[v0.19.0](https://docs.vllm.ai/en/v0.19.0/configuration/engine_args/)[v0.18.2](https://docs.vllm.ai/en/v0.18.2/configuration/engine_args/)[v0.18.1](https://docs.vllm.ai/en/v0.18.1/configuration/engine_args/)[v0.18.0](https://docs.vllm.ai/en/v0.18.0/configuration/engine_args/)[v0.17.1](https://docs.vllm.ai/en/v0.17.1/configuration/engine_args/)[v0.17.0](https://docs.vllm.ai/en/v0.17.0/configuration/engine_args/)[v0.16.0](https://docs.vllm.ai/en/v0.16.0/configuration/engine_args/)[v0.15.1](https://docs.vllm.ai/en/v0.15.1/configuration/engine_args/)[v0.15.0](https://docs.vllm.ai/en/v0.15.0/configuration/engine_args/)[v0.14.1](https://docs.vllm.ai/en/v0.14.1/configuration/engine_args/)[v0.14.0](https://docs.vllm.ai/en/v0.14.0/configuration/engine_args/)[v0.13.0](https://docs.vllm.ai/en/v0.13.0/configuration/engine_args/)[v0.12.0](https://docs.vllm.ai/en/v0.12.0/configuration/engine_args/)[v0.11.2](https://docs.vllm.ai/en/v0.11.2/configuration/engine_args/)[v0.11.1](https://docs.vllm.ai/en/v0.11.1/configuration/engine_args/)[v0.11.0](https://docs.vllm.ai/en/v0.11.0/configuration/engine_args/)[v0.10.2](https://docs.vllm.ai/en/v0.10.2/configuration/engine_args/)[v0.10.1.1](https://docs.vllm.ai/en/v0.10.1.1/configuration/engine_args/)[v0.10.1](https://docs.vllm.ai/en/v0.10.1/configuration/engine_args/)[v0.10.0](https://docs.vllm.ai/en/v0.10.0/configuration/engine_args/)[v0.9.2](https://docs.vllm.ai/en/v0.9.2/configuration/engine_args/)[v0.9.1](https://docs.vllm.ai/en/v0.9.1/configuration/engine_args/)[v0.9.0.1](https://docs.vllm.ai/en/v0.9.0.1/configuration/engine_args/)[v0.9.0](https://docs.vllm.ai/en/v0.9.0/configuration/engine_args/)[v0.8.5.post1](https://docs.vllm.ai/en/v0.8.5.post1/configuration/engine_args/)[v0.8.5](https://docs.vllm.ai/en/v0.8.5/configuration/engine_args/)[v0.8.4](https://docs.vllm.ai/en/v0.8.4/configuration/engine_args/)[v0.8.3](https://docs.vllm.ai/en/v0.8.3/configuration/engine_args/)[v0.8.2](https://docs.vllm.ai/en/v0.8.2/configuration/engine_args/)[v0.8.1](https://docs.vllm.ai/en/v0.8.1/configuration/engine_args/)[v0.8.0](https://docs.vllm.ai/en/v0.8.0/configuration/engine_args/)[v0.7.3](https://docs.vllm.ai/en/v0.7.3/configuration/engine_args/)[v0.7.2](https://docs.vllm.ai/en/v0.7.2/configuration/engine_args/)[v0.7.1](https://docs.vllm.ai/en/v0.7.1/configuration/engine_args/)[v0.7.0](https://docs.vllm.ai/en/v0.7.0/configuration/engine_args/)[v0.6.6.post1](https://docs.vllm.ai/en/v0.6.6.post1/configuration/engine_args/)[v0.6.6](https://docs.vllm.ai/en/v0.6.6/configuration/engine_args/)[v0.6.5](https://docs.vllm.ai/en/v0.6.5/configuration/engine_args/)[v0.6.4.post1](https://docs.vllm.ai/en/v0.6.4.post1/configuration/engine_args/)[v0.6.4](https://docs.vllm.ai/en/v0.6.4/configuration/engine_args/)[v0.6.3.post1](https://docs.vllm.ai/en/v0.6.3.post1/configuration/engine_args/)[v0.6.3](https://docs.vllm.ai/en/v0.6.3/configuration/engine_args/)[v0.6.2](https://docs.vllm.ai/en/v0.6.2/configuration/engine_args/)[v0.6.1.post2](https://docs.vllm.ai/en/v0.6.1.post2/configuration/engine_args/)[v0.6.1.post1](https://docs.vllm.ai/en/v0.6.1.post1/configuration/engine_args/)[v0.6.1](https://docs.vllm.ai/en/v0.6.1/configuration/engine_args/)[v0.6.0](https://docs.vllm.ai/en/v0.6.0/configuration/engine_args/)[v0.5.5](https://docs.vllm.ai/en/v0.5.5/configuration/engine_args/)[v0.5.4](https://docs.vllm.ai/en/v0.5.4/configuration/engine_args/)[v0.5.3.post1](https://docs.vllm.ai/en/v0.5.3.post1/configuration/engine_args/)[v0.5.3](https://docs.vllm.ai/en/v0.5.3/configuration/engine_args/)[v0.5.2](https://docs.vllm.ai/en/v0.5.2/configuration/engine_args/)[v0.5.1](https://docs.vllm.ai/en/v0.5.1/configuration/engine_args/)[v0.5.0.post1](https://docs.vllm.ai/en/v0.5.0.post1/configuration/engine_args/)[v0.5.0](https://docs.vllm.ai/en/v0.5.0/configuration/engine_args/)[v0.4.3](https://docs.vllm.ai/en/v0.4.3/configuration/engine_args/)[v0.4.2](https://docs.vllm.ai/en/v0.4.2/configuration/engine_args/)[v0.4.1](https://docs.vllm.ai/en/v0.4.1/configuration/engine_args/)[v0.4.0.post1](https://docs.vllm.ai/en/v0.4.0.post1/configuration/engine_args/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/vllm/?utm_source=vllm&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/vllm/builds/?utm_source=vllm&utm_content=flyout)Search\
\
* * *\
\
[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=vllm&utm_content=flyout) ― Hosted by\
[Read the Docs](https://about.readthedocs.com/?utm_source=vllm&utm_content=flyout)\
\
Ask AI