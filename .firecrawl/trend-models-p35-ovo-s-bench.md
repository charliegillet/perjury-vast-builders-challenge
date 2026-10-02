[Skip to content](https://github.com/InternLM/OVO-S-Bench#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/InternLM/OVO-S-Bench) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/InternLM/OVO-S-Bench) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/InternLM/OVO-S-Bench) to refresh your session.Dismiss alert

{{ message }}

[InternLM](https://github.com/InternLM)/ **[OVO-S-Bench](https://github.com/InternLM/OVO-S-Bench)** Public

- [Notifications](https://github.com/login?return_to=%2FInternLM%2FOVO-S-Bench) You must be signed in to change notification settings
- [Fork\\
0](https://github.com/login?return_to=%2FInternLM%2FOVO-S-Bench)
- [Star\\
55](https://github.com/login?return_to=%2FInternLM%2FOVO-S-Bench)


main

[**2** Branches](https://github.com/InternLM/OVO-S-Bench/branches) [**0** Tags](https://github.com/InternLM/OVO-S-Bench/tags)

[Go to Branches page](https://github.com/InternLM/OVO-S-Bench/branches)[Go to Tags page](https://github.com/InternLM/OVO-S-Bench/tags)

Go to file

Code

Open more actions menu

## Latest commit

![buaaplay](https://avatars.githubusercontent.com/u/140368158?v=4&size=40)![cursoragent](https://avatars.githubusercontent.com/u/199161495?v=4&size=40)

[buaaplay](https://github.com/InternLM/OVO-S-Bench/commits?author=buaaplay)

and

[cursoragent](https://github.com/InternLM/OVO-S-Bench/commits?author=cursoragent)

[Cite the EMNLP 2026 proceedings instead of the arXiv preprint](https://github.com/InternLM/OVO-S-Bench/commit/e22849e6326acd36f3099a0b46bd7244da0197f3)

Open commit details

2 months agoAug 25, 2026

[e22849e](https://github.com/InternLM/OVO-S-Bench/commit/e22849e6326acd36f3099a0b46bd7244da0197f3) · 2 months agoAug 25, 2026

## History

[14 Commits](https://github.com/InternLM/OVO-S-Bench/commits/main/)

Open commit details

[View commit history for this file.](https://github.com/InternLM/OVO-S-Bench/commits/main/) 14 Commits

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| [assets](https://github.com/InternLM/OVO-S-Bench/tree/main/assets "assets") | [assets](https://github.com/InternLM/OVO-S-Bench/tree/main/assets "assets") | [Vendor figures into assets/ and use repo-local refs](https://github.com/InternLM/OVO-S-Bench/commit/c735562ec17e03e0feb55a4986d6fc1a3ab604cb "Vendor figures into assets/ and use repo-local refs  Previously the teaser and taxonomy figures pointed at raw.githubusercontent.com/InternLM/OVO-S-Bench/webpage/... which (a) requires the repo to be public for raw URLs to serve, and (b) couples the README to the webpage branch's directory layout.  Copy the three referenced figures into assets/ on main (teaser.png, taxonomy_examples.png, taxonomy_statistics.png; ~7 MB total) and use relative paths. README now renders standalone, no cross-branch coupling.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [data](https://github.com/InternLM/OVO-S-Bench/tree/main/data "data") | [data](https://github.com/InternLM/OVO-S-Bench/tree/main/data "data") | [Update paper and dataset release links](https://github.com/InternLM/OVO-S-Bench/commit/daceab144caa571e07f98d7bfe7536be0c4e2212 "Update paper and dataset release links") | 4 months agoJun 4, 2026 |
| [docs](https://github.com/InternLM/OVO-S-Bench/tree/main/docs "docs") | [docs](https://github.com/InternLM/OVO-S-Bench/tree/main/docs "docs") | [Rename release parquet: ovo\_s\_bench\_l1\_l4.parquet → ovo\_s\_bench.parquet](https://github.com/InternLM/OVO-S-Bench/commit/41d61318e138c6f49e6ab1f60e3296b16b798118 "Rename release parquet: ovo_s_bench_l1_l4.parquet → ovo_s_bench.parquet  The shorter name matches the HF dataset's authoritative filename. Updated every reference across README.md, data/README.md, docs/*.md, precache.py, launch.py, and the eval_api.sh / eval_vllm.sh examples. Inference results follow the parquet stem so they're now written to results/<model>/ovo_s_bench.json.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 2, 2026 |
| [models](https://github.com/InternLM/OVO-S-Bench/tree/main/models "models") | [models](https://github.com/InternLM/OVO-S-Bench/tree/main/models "models") | [Polish stale cluster-internal language](https://github.com/InternLM/OVO-S-Bench/commit/f220010816655d5a677107fbc445b4788af9f746 "Polish stale cluster-internal language  After release-grade extraction we still had a few leftover comments and docstrings referring to internal infra (rjob containers, H200 runtime, _src/<upstream> paths, scripts/build_master_parquet.py). Generalize all of them, fix the precache.py usage examples to point at the released parquet, and drop the broken script reference in benchmarking_protocol.md.  No code behavior changes; just comments and docstrings.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [scripts](https://github.com/InternLM/OVO-S-Bench/tree/main/scripts "scripts") | [scripts](https://github.com/InternLM/OVO-S-Bench/tree/main/scripts "scripts") | [Rename release parquet: ovo\_s\_bench\_l1\_l4.parquet → ovo\_s\_bench.parquet](https://github.com/InternLM/OVO-S-Bench/commit/41d61318e138c6f49e6ab1f60e3296b16b798118 "Rename release parquet: ovo_s_bench_l1_l4.parquet → ovo_s_bench.parquet  The shorter name matches the HF dataset's authoritative filename. Updated every reference across README.md, data/README.md, docs/*.md, precache.py, launch.py, and the eval_api.sh / eval_vllm.sh examples. Inference results follow the parquet stem so they're now written to results/<model>/ovo_s_bench.json.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 2, 2026 |
| [utils](https://github.com/InternLM/OVO-S-Bench/tree/main/utils "utils") | [utils](https://github.com/InternLM/OVO-S-Bench/tree/main/utils "utils") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [.env.example](https://github.com/InternLM/OVO-S-Bench/blob/main/.env.example ".env.example") | [.env.example](https://github.com/InternLM/OVO-S-Bench/blob/main/.env.example ".env.example") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [.gitignore](https://github.com/InternLM/OVO-S-Bench/blob/main/.gitignore ".gitignore") | [.gitignore](https://github.com/InternLM/OVO-S-Bench/blob/main/.gitignore ".gitignore") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [LICENSE](https://github.com/InternLM/OVO-S-Bench/blob/main/LICENSE "LICENSE") | [LICENSE](https://github.com/InternLM/OVO-S-Bench/blob/main/LICENSE "LICENSE") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [README.md](https://github.com/InternLM/OVO-S-Bench/blob/main/README.md "README.md") | [README.md](https://github.com/InternLM/OVO-S-Bench/blob/main/README.md "README.md") | [Cite the EMNLP 2026 proceedings instead of the arXiv preprint](https://github.com/InternLM/OVO-S-Bench/commit/e22849e6326acd36f3099a0b46bd7244da0197f3 "Cite the EMNLP 2026 proceedings instead of the arXiv preprint  Co-authored-by: Cursor <cursoragent@cursor.com>") | 2 months agoAug 25, 2026 |
| [annotation\_utils.py](https://github.com/InternLM/OVO-S-Bench/blob/main/annotation_utils.py "annotation_utils.py") | [annotation\_utils.py](https://github.com/InternLM/OVO-S-Bench/blob/main/annotation_utils.py "annotation_utils.py") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [config.yaml](https://github.com/InternLM/OVO-S-Bench/blob/main/config.yaml "config.yaml") | [config.yaml](https://github.com/InternLM/OVO-S-Bench/blob/main/config.yaml "config.yaml") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [inference.py](https://github.com/InternLM/OVO-S-Bench/blob/main/inference.py "inference.py") | [inference.py](https://github.com/InternLM/OVO-S-Bench/blob/main/inference.py "inference.py") | [Polish stale cluster-internal language](https://github.com/InternLM/OVO-S-Bench/commit/f220010816655d5a677107fbc445b4788af9f746 "Polish stale cluster-internal language  After release-grade extraction we still had a few leftover comments and docstrings referring to internal infra (rjob containers, H200 runtime, _src/<upstream> paths, scripts/build_master_parquet.py). Generalize all of them, fix the precache.py usage examples to point at the released parquet, and drop the broken script reference in benchmarking_protocol.md.  No code behavior changes; just comments and docstrings.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [launch.py](https://github.com/InternLM/OVO-S-Bench/blob/main/launch.py "launch.py") | [launch.py](https://github.com/InternLM/OVO-S-Bench/blob/main/launch.py "launch.py") | [Rename release parquet: ovo\_s\_bench\_l1\_l4.parquet → ovo\_s\_bench.parquet](https://github.com/InternLM/OVO-S-Bench/commit/41d61318e138c6f49e6ab1f60e3296b16b798118 "Rename release parquet: ovo_s_bench_l1_l4.parquet → ovo_s_bench.parquet  The shorter name matches the HF dataset's authoritative filename. Updated every reference across README.md, data/README.md, docs/*.md, precache.py, launch.py, and the eval_api.sh / eval_vllm.sh examples. Inference results follow the parquet stem so they're now written to results/<model>/ovo_s_bench.json.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 2, 2026 |
| [merge\_results.py](https://github.com/InternLM/OVO-S-Bench/blob/main/merge_results.py "merge_results.py") | [merge\_results.py](https://github.com/InternLM/OVO-S-Bench/blob/main/merge_results.py "merge_results.py") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [option\_utils.py](https://github.com/InternLM/OVO-S-Bench/blob/main/option_utils.py "option_utils.py") | [option\_utils.py](https://github.com/InternLM/OVO-S-Bench/blob/main/option_utils.py "option_utils.py") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [precache.py](https://github.com/InternLM/OVO-S-Bench/blob/main/precache.py "precache.py") | [precache.py](https://github.com/InternLM/OVO-S-Bench/blob/main/precache.py "precache.py") | [Rename release parquet: ovo\_s\_bench\_l1\_l4.parquet → ovo\_s\_bench.parquet](https://github.com/InternLM/OVO-S-Bench/commit/41d61318e138c6f49e6ab1f60e3296b16b798118 "Rename release parquet: ovo_s_bench_l1_l4.parquet → ovo_s_bench.parquet  The shorter name matches the HF dataset's authoritative filename. Updated every reference across README.md, data/README.md, docs/*.md, precache.py, launch.py, and the eval_api.sh / eval_vllm.sh examples. Inference results follow the parquet stem so they're now written to results/<model>/ovo_s_bench.json.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 2, 2026 |
| [prompts.py](https://github.com/InternLM/OVO-S-Bench/blob/main/prompts.py "prompts.py") | [prompts.py](https://github.com/InternLM/OVO-S-Bench/blob/main/prompts.py "prompts.py") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [requirements-vllm.txt](https://github.com/InternLM/OVO-S-Bench/blob/main/requirements-vllm.txt "requirements-vllm.txt") | [requirements-vllm.txt](https://github.com/InternLM/OVO-S-Bench/blob/main/requirements-vllm.txt "requirements-vllm.txt") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [requirements.txt](https://github.com/InternLM/OVO-S-Bench/blob/main/requirements.txt "requirements.txt") | [requirements.txt](https://github.com/InternLM/OVO-S-Bench/blob/main/requirements.txt "requirements.txt") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| [score.py](https://github.com/InternLM/OVO-S-Bench/blob/main/score.py "score.py") | [score.py](https://github.com/InternLM/OVO-S-Bench/blob/main/score.py "score.py") | [Initial release of OVO-S-Bench evaluation framework](https://github.com/InternLM/OVO-S-Bench/commit/cd4768ef38f43ce7b05ed8eb914f74250626876b "Initial release of OVO-S-Bench evaluation framework  Release-grade rewrite of the internal eval_v1/ codebase. Highlights:  - Top-level CLI: inference.py, score.py, launch.py, precache.py,   merge_results.py — multi-GPU dynamic sharding via fcntl-locked queue file. - Pluggable models: tier-1 wrappers (API providers, vLLM-based Qwen3-VL /   InternVL3.5 / LLaVA-OneVision / MiniCPM-V) under models/; tier-2 wrappers   requiring upstream repos (HERMES, FluxMem, StreamingTOM, InfiniPot-V, etc.)   under models/extras/ with a `find_upstream_src()` resolver and BYO install   guide. - Frame-caching pipeline keyed on (video, sampling-params) hash with decord   primary + OpenCV fallback. - Image-option support for §4.3 trajectory matching: PNGs embedded as   base64 data URIs in the release parquet and rendered into prompts via   option_utils.append_option_images_to_frames. - Config: 84 models flattened from nested category/series/variants, all   cluster-internal paths and conda_env entries stripped. - Docs: adding_models.md, benchmarking_protocol.md, frame_caching.md. - License: MIT.  Benchmark data (1695 questions across L1-L4 + source videos) is distributed separately via HuggingFace Datasets.  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") | 5 months agoJun 1, 2026 |
| View all files |

## Repository files navigation

# OVO-S-Bench

[Permalink: OVO-S-Bench](https://github.com/InternLM/OVO-S-Bench#ovo-s-bench)

_A Hierarchical Benchmark for Streaming Spatial Intelligence in Multimodal LLMs_

🔥🔥OVO-S-Bench is accepted by EMNLP 2026!🔥🔥

[Yifei Li](https://joeleelyf.github.io/) 1,2,†  ·
[Pengyiang Liu](https://buaaplay.github.io/) 3,†  ·
[Yuhang Zang](https://scholar.google.com/citations?hl=en&user=hW23VKIAAAAJ) 2,\*  ·
Zhongyue Shi3  ·
Qi Fu3  ·
Hongye Hao3  ·
[Jiwen Lu](https://scholar.google.com/citations?hl=en&user=TN8uDQoAAAAJ) 1

1Tsinghua University    2Shanghai AI Laboratory    3Beihang University

†Equal Contribution    \*Project Leader

[![arXiv](https://camo.githubusercontent.com/c63476aa6fb0249f5da161819ad9183da9f08865131f9659842f164fbd146ba2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d323630362e30333839302d6233316231622e737667)](https://arxiv.org/abs/2606.03890)[![Paper](https://camo.githubusercontent.com/97fea2e07a1f2ff31e19d5f8dabd4cc09e650363f2979538cc94b18e7e709137/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617065722d5044462d726564)](https://arxiv.org/pdf/2606.03890)[![Code](https://camo.githubusercontent.com/b6c2d487972a87e6a1fa24712ee3b485dfe57bf266c28d67de640de5eef2fe92/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f64652d4769744875622d3138313731373f6c6f676f3d676974687562)](https://github.com/InternLM/OVO-S-Bench)[![HuggingFace Paper](https://camo.githubusercontent.com/eb4a33fc331a26f4ebc31af688622505eba701a6cccb6c2a8ea87747df996b9e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2546302539462541342539375f50617065722d323630362e30333839302d79656c6c6f77)](https://huggingface.co/papers/2606.03890)[![ModelScope Dataset](https://camo.githubusercontent.com/86a8c79d0e2c479a9c7b808686620c0bf6c78c09a59bfec4ed7b0e5bbada32ca/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446174617365742d4d6f64656c53636f70652d626c7565)](https://modelscope.cn/datasets/JoeLeelyf/OVO-S-Bench/)[![Project Page](https://camo.githubusercontent.com/770087043ad1711155d368e4827d5620a1ea645fb413309182f079b85e4b3641/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2546302539462538432539305f50726f6a6563742d506167652d626c7565)](https://internlm.github.io/OVO-S-Bench/)

[![OVO-S-Bench overview](https://github.com/InternLM/OVO-S-Bench/raw/main/assets/teaser.png)](https://github.com/InternLM/OVO-S-Bench/blob/main/assets/teaser.png)

_**Overview of OVO-S-Bench.** The benchmark evaluates streaming spatial understanding across four levels, from instantaneous egocentric perception and spatiotemporal context tracking to generative spatial reasoning and global topological mapping. The right panel summarizes representative model behavior across task families._

* * *

## Abstract

[Permalink: Abstract](https://github.com/InternLM/OVO-S-Bench#abstract)

Multimodal agents in robotics, AR, and autonomous driving must reason about places and layouts from continuous egocentric streams, often using evidence outside the current view. Existing benchmarks either evaluate offline over full videos or target events rather than spatial structure. We introduce **OVO-S-Bench**, a fully human-annotated benchmark for streaming spatial intelligence, comprising **1,680 questions over 348 source videos**. Annotation involves 12 trained annotators (each also serving as a blind cross-reviewer) across roughly **804 person-hours** of multi-round quality assurance. Each question carries a query timestamp and an evidence interval, and at evaluation, the model sees only the prefix preceding the query. Questions span four levels of increasing abstraction: instantaneous egocentric perception, spatiotemporal context tracking, spatial simulation and reasoning, and allocentric mapping. Across **38 proprietary and open-source MLLMs**, Gemini-3.1-Pro trails human experts by **27 points (59.2 vs. 86.6)**, with allocentric mapping as the dominant bottleneck. Notably, streaming and spatially fine-tuned MLLMs underperform their own backbones. We further find that chain-of-thought reasoning amplifies spatial errors when ungrounded in the stream. By exposing these limitations, OVO-S-Bench establishes a demanding testbed for next-generation streaming spatial MLLMs.

## Four-Level Streaming Spatial Taxonomy

[Permalink: Four-Level Streaming Spatial Taxonomy](https://github.com/InternLM/OVO-S-Bench#four-level-streaming-spatial-taxonomy)

OVO-S-Bench organizes questions into **four cumulative levels** by the spatial state a model must access at query time. The progression goes from evidence directly available in the current view to allocentric map queries that require cross-viewpoint integration, reflecting a gradient of persistence and abstraction.

| Level | Capability | Task families |
| --- | --- | --- |
| **L1 — Instantaneous Egocentric Perception** | Answerable from frames near the query timestamp alone, without recalling any past observation | egocentric metric perception (distance, scale, clearance, viewpoint height) · local spatial relations (containment, occlusion, support, visible layout) · dynamic spatial perception (camera motion, object motion, relative speed) |
| **L2 — Spatiotemporal Context Tracking** | Evidence has appeared in the prefix but is no longer visible at query time | scene revisit recognition · spatial memory beyond the view · chronological spatial memory |
| **L3 — Spatial Simulation and Reasoning** | Operate on spatial structure rather than merely retrieve an observation | spatial simulation (reorientation, removal consequences, physical feasibility) · spatiotemporal consistency verification · spatial route planning |
| **L4 — Allocentric Spatial Mapping** | Integrate the egocentric stream into an allocentric representation and query its global structure | allocentric direction reasoning · topological structure reasoning · **trajectory-map alignment** (image options) |

The released benchmark comprises **1,680 questions over 348 source videos from 9 datasets**, organized into **30 canonical task types** across four levels. Mean prefix at query time: **8.8 min**. Evidence-span medians by level: **L1 2.0 s · L2 36.8 s · L3 2.0 s · L4 278.7 s** — reflecting the spatial persistence each level demands.

[![Representative OVO-S-Bench examples](https://github.com/InternLM/OVO-S-Bench/raw/main/assets/taxonomy_examples.png)](https://github.com/InternLM/OVO-S-Bench/blob/main/assets/taxonomy_examples.png)

_**Representative OVO-S-Bench examples.** Each card pairs a spatial question with visual evidence, illustrating the progression from current-view perception to allocentric mapping._

[![Taxonomy and benchmark statistics](https://github.com/InternLM/OVO-S-Bench/raw/main/assets/taxonomy_statistics.png)](https://github.com/InternLM/OVO-S-Bench/blob/main/assets/taxonomy_statistics.png)

_**Taxonomy and benchmark statistics.** Left: four-level spatial taxonomy. Right: task-family counts, source distribution, and evidence-interval lengths by level._

> L4.3 trajectory-matching questions ship their option images **embedded inline** as base64 data URIs in the parquet's `options` column. No separate image-asset download is needed.

## Benchmark Construction

[Permalink: Benchmark Construction](https://github.com/InternLM/OVO-S-Bench#benchmark-construction)

- **Video sources.** OVO-S-Bench draws from 9 publicly available or accessible sources covering five regimes: _indoor walkthroughs_ (RoomTour3D), _egocentric activities_ (Ego4D), _outdoor/world scenes_ (Sekai, OmniWorld, YouTube walking tours), _driving videos_ (CODa, Honda HDD), and _spatially annotated 3D environments_ (ARKitScenes, VSI-Bench).
- **Human annotators write every item.** Annotators with 3D-vision backgrounds choose clips with stable motion, clear viewpoints, and enough spatial variation for the target level. For each item, they record the video, task label, question, options, answer, query timestamp, and evidence interval.
- **Each item follows the streaming setting.** The answer must be derivable from the video prefix before the query timestamp. Annotators mark the shortest interval that contains the needed evidence and write distractors that are plausible under the visual context but wrong under the annotated evidence.
- **Quality control removes shortcuts.** A text-only LLM probe flags items that leak the answer through wording, common sense, or option asymmetry. A second annotator then cross-reviews each item without seeing the original answer, checking that the answer and evidence interval are sufficient. Recurring problems are folded back into the annotation guideline.

## Key Findings

[Permalink: Key Findings](https://github.com/InternLM/OVO-S-Bench#key-findings)

Six observations about the current state of streaming spatial intelligence, from 38 evaluated systems on OVO-S-Bench:

|  | Finding |
| :-: | --- |
| **27 pts** | **Significant gap with human performance.** Strongest system **Gemini-3.1-Pro** reaches **59.2** overall, far below human experts under the same streaming protocol ( **86.6**; **92.2** offline). Best open-source: **Qwen3-VL-235B-A22B** at **53.6**, trailing human-streaming by **33 points**. The Random (31.3) and Text-Only (37.1) baselines fall below all general backbones, confirming the gap reflects genuine visual-streaming difficulty rather than language priors. |
| **28 / 34** | **Allocentric mapping is the dominant bottleneck.** L4 is the lowest-scoring level for **28 of 34** systems, with an average gap of **9.3 %** between L1–L3 and L4. Even the largest open-source backbones drop more than 10 points (Qwen3-VL-235B-A22B: 10.6; InternVL-3.5-241B-A28B: 13.8). The six exceptions all have L1 below 41, so their flipped ordering reflects degraded current-view perception rather than competent allocentric mapping. |
| **+5.6** | **Closed-source advantage is narrow and uneven.** The closed-source lead is only **5.6 points overall** (Gemini-3.1-Pro 59.2 vs Qwen3-VL-235B-A22B 53.6), narrower than the 10+ point gap reported on recent video and multimodal benchmarks. The gap is uneven across levels: it widens on memory-heavy L2 ( **+5.9**) and narrows on L4 ( **+4.1**); on L3, the best open-source backbone **exceeds Gemini-3.1-Pro by 5.3 points** (61.2 vs 55.9). |
| **13 / 15** | **Specialization hurts the backbone.** No streaming-architecture or spatially fine-tuned variant outperforms its comparable general backbone, and **13 of 15** lag behind their own base on overall accuracy (median −2.0, range −18.4 to +0.5). **L4 is the most uniformly damaged level**: 13 of 15 methods regress on allocentric mapping (mean Δ = −6.1; Flash-VStream-7B −16.7, Cosmos-Reason1-7B −12.8). |
| **+3.9 / −1.0** | **Chain-of-thought is double-edged.** Across paired thinking-mode comparisons, explicit reasoning consistently helps L2 (mean Δ = **+3.9**, 8/9 pairs positive) but shows a small mean drop on L1 (mean Δ = **−1.0**, 6/9 pairs negative). A GPT-5.4 judge over wrong traces finds that **60–80 % of CoT failures are mis-grounded visual evidence** (non-visual + visual-content errors) in GLM-4.6V-Flash, Qwen3-VL, and InternVL-3.5. |
| **r ≈ 0** | **Retention is not the bottleneck.** For HERMES, StreamingTOM, and FluxMem, per-query Pearson correlation between Evidence Recall and correctness is essentially zero ( **r ∈ \[−0.07, 0.00\]**). Neither an oracle-evidence sampler nor doubling the frame budget improves over uniform 128 frames by more than +0.3 points. The 27-point gap to human performance therefore **does not reduce to a retrieval problem** solvable by better frame selection or larger memory. |

* * *

## Leaderboard

[Permalink: Leaderboard](https://github.com/InternLM/OVO-S-Bench#leaderboard)

Main results under the streaming protocol (multiple-choice accuracy). Numbers replicated from the paper's main results table. The public dataset release is linked above; a live submission portal will follow.

| Model | Params | L1 | L2 | L3 | L4 | Overall | Rank |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| _Baselines & Controls_ |  |  |  |  |  |  |  |
| Random Baseline | – | 29.8 | 35.1 | 33.3 | 27.1 | 31.3 | – |
| Text-Only (GPT-5.4) | – | 38.4 | 35.6 | 38.9 | 35.5 | 37.1 | – |
| Human (streaming) | – | 93.2 | 81.0 | 86.4 | 79.2 | **86.6** | – |
| Human (offline) | – | 97.0 | 86.2 | 94.2 | 89.2 | **92.2** | – |
| _Closed-source proprietary MLLMs_ |  |  |  |  |  |  |  |
| **Gemini-3.1-Pro** | – | **61.9** | **64.0** | 55.9 | **54.9** | **59.2** | 🥇 1 |
| GPT-5.4 | – | 54.6 | 57.6 | 50.8 | 40.5 | 50.9 | 5 |
| Gemini-3.1-Flash-Lite | – | 54.1 | 52.2 | 54.1 | 42.8 | 50.8 | 7 |
| Grok-4.1-Fast | – | 44.8 | 46.6 | 48.5 | 35.0 | 43.7 | 19 |
| _Open-source general video MLLMs_ |  |  |  |  |  |  |  |
| **Qwen3-VL** | 235B-A22B | 52.5 | 55.2 | **61.2** | 45.7 | 53.6 | 🥈 2 |
| Qwen3.5 | 397B-A17B | 49.6 | 55.4 | 58.1 | 45.4 | 52.1 | 🥉 3 |
| Qwen3.5 | 27B | 51.5 | 55.2 | 52.4 | 47.7 | 51.7 | 4 |
| InternVL-3.5 | 241B-A28B | 55.6 | 55.7 | 51.6 | 40.5 | 50.9 | 6 |
| InternVL-3.5 | 38B | 54.7 | 54.4 | 45.5 | 41.9 | 49.1 | 8 |
| Qwen3-VL | 32B | 50.1 | 51.9 | 51.9 | 41.2 | 48.8 | 9 |
| Qwen3-VL | 4B | 43.3 | 48.2 | 54.5 | 41.4 | 46.8 | 10 |
| Qwen3.5 | 9B | 47.5 | 49.4 | 50.2 | 36.6 | 45.9 | 12 |
| Qwen3.5 | 4B | 45.4 | 48.2 | 49.3 | 38.7 | 45.4 | 13 |
| InternVL-3.5 | 8B | 45.9 | 45.8 | 47.2 | 39.3 | 44.6 | 16 |
| Qwen2.5-VL | 7B | 40.7 | 45.5 | 45.9 | 44.7 | 44.2 | 17 |
| GLM-4.6V-Flash | 9B | 44.6 | 48.0 | 46.6 | 33.8 | 43.2 | 22 |
| Gemma-4 | 26B-A4B | 49.3 | 46.6 | 45.0 | 29.3 | 42.6 | 24 |
| Gemma-4 | E4B | 40.9 | 42.8 | 42.8 | 32.3 | 39.7 | 30 |
| Gemma-4 | E2B | 38.8 | 36.5 | 39.3 | 29.6 | 36.1 | 36 |
| _Streaming video MLLMs_ |  |  |  |  |  |  |  |
| StreamForest | 7B | 46.6 | 45.2 | 49.7 | 34.9 | 44.1 | 18 |
| StreamingVLM | 7B | 38.7 | 50.5 | 41.8 | 41.2 | 43.0 | 23 |
| Flash-VStream | 7B | 18.7 | 29.9 | 22.5 | 28.7 | 24.9 | 38 |
| _Token-compression and memory-based methods_ |  |  |  |  |  |  |  |
| FluxMem | 7B | 43.0 | 47.6 | 45.5 | 42.6 | 44.7 | 14 |
| HERMES | 7B | 40.9 | 45.4 | 49.4 | 42.9 | 44.6 | 15 |
| StreamingTOM | 7B | 37.2 | 48.2 | 38.7 | 33.5 | 39.4 | 31 |
| InfiniPot-V | 7B | 39.1 | 35.7 | 41.9 | 40.6 | 39.3 | 32 |
| _Spatially fine-tuned MLLMs_ |  |  |  |  |  |  |  |
| VST-7B-SFT | 7B | 43.3 | 44.0 | 43.6 | 37.9 | 42.2 | 26 |
| VST-7B-RL | 7B | 45.7 | 44.2 | 40.9 | 38.0 | 42.2 | 25 |
| SenseNova-SI-1.5 | 8B | 42.1 | 42.4 | 42.7 | 32.8 | 40.0 | 29 |
| Spatial-TTT | 2B | 38.7 | 35.4 | 41.0 | 32.7 | 37.0 | 33 |
| Cambrian-S | 7B | 40.2 | 40.0 | 36.9 | 29.9 | 36.8 | 34 |
| Spatial-MLLM | 7B | 35.7 | 39.2 | 34.4 | 36.3 | 36.4 | 35 |
| Cambrian-S-LFP | 7B | 38.8 | 38.0 | 34.2 | 28.7 | 34.9 | 37 |
| _Embodied foundation models_ |  |  |  |  |  |  |  |
| RynnBrain | 8B | 45.3 | 50.3 | 47.3 | 42.7 | 46.4 | 11 |
| VeBrain | 7B | 42.7 | 44.2 | 46.2 | 40.8 | 43.5 | 21 |
| RoboBrain2.5-NV | 8B | 42.9 | 46.6 | 50.6 | 34.1 | 43.6 | 20 |
| RoboBrain2.5 | 4B | 40.1 | 43.4 | 48.1 | 35.7 | 41.8 | 27 |
| Cosmos-Reason1 | 7B | 44.8 | 43.7 | 45.5 | 31.9 | 41.5 | 28 |

Interactive version with sorting + per-category drill-down: [https://internlm.github.io/OVO-S-Bench/](https://internlm.github.io/OVO-S-Bench/)

* * *

## Quick Start

[Permalink: Quick Start](https://github.com/InternLM/OVO-S-Bench#quick-start)

### Install

[Permalink: Install](https://github.com/InternLM/OVO-S-Bench#install)

```
git clone https://github.com/InternLM/OVO-S-Bench.git
cd OVO-S-Bench

# Default install (API providers only; ~1 min)
pip install -r requirements.txt

# Optional: open-source MLLMs via vLLM
pip install -r requirements-vllm.txt
```

### Download the benchmark

[Permalink: Download the benchmark](https://github.com/InternLM/OVO-S-Bench#download-the-benchmark)

The release pages are:

- Hugging Face: [https://huggingface.co/datasets/JoeLeelyf/OVO-S-Bench](https://huggingface.co/datasets/JoeLeelyf/OVO-S-Bench)
- ModelScope: [https://modelscope.cn/datasets/JoeLeelyf/OVO-S-Bench/](https://modelscope.cn/datasets/JoeLeelyf/OVO-S-Bench/)

The complete annotations parquet and source videos are currently available from ModelScope:

```
pip install -U modelscope
python - <<'PY'
from modelscope.hub.snapshot_download import snapshot_download

snapshot_download(
    repo_id='JoeLeelyf/OVO-S-Bench',
    repo_type='dataset',
    local_dir='./data',
)
PY
```

Layout you should see after download:

```
data/
├── ovo_s_bench.parquet     # questions, ~35 MB
└── videos/                       # source .mp4 files
    ├── Ego4D/ ...
    ├── RoomTour3D/ ...
    ├── annotated_videos/ ...
    └── ...
```

### Configure API keys

[Permalink: Configure API keys](https://github.com/InternLM/OVO-S-Bench#configure-api-keys)

```
cp .env.example .env
$EDITOR .env       # fill in the provider(s) you'll use
```

### Run

[Permalink: Run](https://github.com/InternLM/OVO-S-Bench#run)

**API model** (single-process, threaded):

```
bash scripts/eval_api.sh gpt-4o data/ovo_s_bench.parquet
```

**Open-source MLLM via vLLM** (multi-GPU auto-sharded; default 128 uniformly-sampled frames per prefix):

```
GPUS=8 bash scripts/eval_vllm.sh qwen3-vl-32b data/ovo_s_bench.parquet
```

Both scripts call `inference.py` then `score.py`. Inference auto-resumes on rerun — interrupted jobs pick up from the last checkpoint.

### Add a new model

[Permalink: Add a new model](https://github.com/InternLM/OVO-S-Bench#add-a-new-model)

See [docs/adding\_models.md](https://github.com/InternLM/OVO-S-Bench/blob/main/docs/adding_models.md). The contract is `BaseModel.inference(frames: List[PIL.Image], prompt: str) -> str`; add a config entry to `config.yaml::MODELS` and register the wrapper in `models/api_models.py` or `models/vllm_models.py`.

### Custom API endpoint

[Permalink: Custom API endpoint](https://github.com/InternLM/OVO-S-Bench#custom-api-endpoint)

Set `*_BASE_URL` in `.env` to point at your proxy or local vLLM server. API providers (`openai`, `gemini-native`, `anthropic`) honor the standard `*_BASE_URL` env var convention.

* * *

## Evaluation Protocol

[Permalink: Evaluation Protocol](https://github.com/InternLM/OVO-S-Bench#evaluation-protocol)

All systems are evaluated under a **unified streaming protocol**: each source video is truncated at the annotated query timestamp tq, and the model receives **128 frames uniformly sampled from the resulting prefix** together with the question and multiple-choice options. For streaming-architecture models that implement a native sequential ingestion path, we instead feed the video at each model's published streaming rate and query the resulting compressed state. No model sees frames after tq. Answers are extracted by regular expression without further post-processing.

Per-query responses land under `results/<model>/ovo_s_bench.json`. `score.py` aggregates accuracy by main category and subcategory:

```
python score.py --result results/gpt-4o/ovo_s_bench.json --verbose
```

For sharded multi-GPU runs, `merge_results.py` consolidates `*_rank{N}.json` shards into a single result file (auto-invoked by `launch.py`).

* * *

## Repository Layout

[Permalink: Repository Layout](https://github.com/InternLM/OVO-S-Bench#repository-layout)

```
OVO-S-Bench/
├── inference.py            # Main eval entry point
├── score.py                # Per-category accuracy aggregator
├── launch.py               # Multi-GPU dynamic-sharding launcher (auto-merges)
├── precache.py             # CPU-only frame pre-extraction
├── merge_results.py        # Shard merger
├── prompts.py              # Pluggable prompt templates (default/verbose/cot)
├── annotation_utils.py     # Parquet / JSON annotation loader
├── option_utils.py         # Image-option helpers (L4.3 PNG decoding)
├── config.yaml             # 84+ pre-registered model entries
├── models/
│   ├── base.py             # BaseModel ABC
│   ├── api_models.py       # OpenAI / Gemini / Claude
│   ├── vllm_models.py      # Qwen3-VL / Qwen3.5 / Gemma4 / GLM-4.6V
│   ├── internvl_models.py
│   ├── llava_onevision_vllm_models.py
│   ├── minicpmv_models.py
│   └── extras/             # 12 wrappers requiring upstream repos
│       ├── README.md       # BYO install instructions
│       └── *_models.py     # HERMES / FluxMem / StreamingTOM / InfiniPot-V / ...
├── utils/
│   ├── frame_utils.py      # decord + OpenCV fallback, .frame_cache logic
│   └── config_utils.py     # nested → flat config flatten
├── scripts/
│   ├── eval_api.sh
│   └── eval_vllm.sh
├── data/README.md          # HF dataset download instructions
└── docs/
    ├── adding_models.md
    ├── benchmarking_protocol.md
    └── frame_caching.md
```

* * *

## BibTeX

[Permalink: BibTeX](https://github.com/InternLM/OVO-S-Bench#bibtex)

```
@inproceedings{li2026ovosbench,
  title     = {{OVO-S-Bench}: A Hierarchical Benchmark for Streaming Spatial Intelligence in Multimodal {LLM}s},
  author    = {Li, Yifei and Liu, Pengyiang and Zang, Yuhang and Shi, Zhongyue and Fu, Qi and Hao, Hongye and Lu, Jiwen},
  booktitle = {Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing},
  year      = {2026}
}
```

* * *

## Acknowledgements

[Permalink: Acknowledgements](https://github.com/InternLM/OVO-S-Bench#acknowledgements)

OVO-S-Bench draws videos from publicly released datasets — many thanks to:
**[Ego4D](https://ego4d-data.org/)**, **[RoomTour3D](https://roomtour3d.github.io/)**, **[CODa](https://amrl.cs.utexas.edu/coda/)**, **[OmniWorld](https://omniworld.github.io/)**, **[VSI-Bench](https://github.com/vision-x-nyu/thinking-in-space)**, **[Sekai](https://huggingface.co/datasets/SekaiTrip/SekaiBench)**, **[ARKitScenes](https://github.com/apple/ARKitScenes)**, **[Honda HDD](https://usa.honda-ri.com/HDD)**, and selected **YouTube** walking tours.

The evaluation framework integrates wrappers for several token-compression and streaming MLLM research repos:
**[HERMES](https://github.com/microsoft/HERMES)**, **[FluxMem](https://github.com/FluxMem)**, **[StreamingTOM](https://github.com/StreamingTOM)**, **[InfiniPot-V](https://github.com/InfiniPot-V)**, **[InfiniteVL](https://github.com/InfiniteVL)**, **[Flash-VStream](https://github.com/IVGSZ/Flash-VStream)**, **[StreamForest](https://github.com/StreamForest)**, **[Spatial-MLLM](https://github.com/diankun-wu/Spatial-MLLM)**, **[Cambrian-S](https://github.com/cambrian-mllm/cambrian)**, **[SenseNova-SI](https://github.com/SenseTime/sensenova-si)**, **[Spatial-TTT](https://github.com/spatial-ttt)**.

Project page template adapted from [OVO-Bench](https://github.com/JoeLeelyf/OVO-Bench), which itself builds on the [Nerfies](https://nerfies.github.io/) template.

* * *

## License

[Permalink: License](https://github.com/InternLM/OVO-S-Bench#license)

MIT — see [LICENSE](https://github.com/InternLM/OVO-S-Bench/blob/main/LICENSE). Annotations released under CC-BY-4.0; source videos retain their original licenses.

## About

\[EMNLP 2026 Oral\] An official implementation of "OVO-S-Bench: A Hierarchical Benchmark for Streaming Spatial Intelligence in Multimodal LLMs"

### Resources

[Readme](https://github.com/InternLM/OVO-S-Bench#readme-ov-file)

[MIT license](https://github.com/InternLM/OVO-S-Bench#MIT-1-ov-file)

[Activity](https://github.com/InternLM/OVO-S-Bench/activity)

[Custom properties](https://github.com/InternLM/OVO-S-Bench/custom-properties)

### Stars

**55** stars

### Watchers

**0** watching

### Forks

[**0** forks](https://github.com/InternLM/OVO-S-Bench/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FInternLM%2FOVO-S-Bench&report=InternLM+%28user%29)

## Releases

## Packages

## Contributors

## Languages

You can’t perform that action at this time.