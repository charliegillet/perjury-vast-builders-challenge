[Skip to content](https://github.com/nvidia/cosmos#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/nvidia/cosmos) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/nvidia/cosmos) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/nvidia/cosmos) to refresh your session.Dismiss alert

{{ message }}

[NVIDIA](https://github.com/NVIDIA)/ **[cosmos](https://github.com/NVIDIA/cosmos)** Public

- [Notifications](https://github.com/login?return_to=%2FNVIDIA%2Fcosmos) You must be signed in to change notification settings
- [Fork\\
898](https://github.com/login?return_to=%2FNVIDIA%2Fcosmos)
- [Star\\
12k](https://github.com/login?return_to=%2FNVIDIA%2Fcosmos)


main

[**48** Branches](https://github.com/NVIDIA/cosmos/branches) [**1** Tag](https://github.com/NVIDIA/cosmos/tags)

[Go to Branches page](https://github.com/NVIDIA/cosmos/branches)[Go to Tags page](https://github.com/NVIDIA/cosmos/tags)

Go to file

Code

Open more actions menu

## Latest commit

[![ishovkun](https://avatars.githubusercontent.com/u/11154303?v=4&size=40)](https://github.com/ishovkun)[ishovkun](https://github.com/NVIDIA/cosmos/commits?author=ishovkun)

[Add TensorRT-LLM Transfer and Action guides (](https://github.com/NVIDIA/cosmos/commit/3e3c6d61dc15d6517c4793beab5ec3894ffa07f1) [#310](https://github.com/NVIDIA/cosmos/pull/310) [)](https://github.com/NVIDIA/cosmos/commit/3e3c6d61dc15d6517c4793beab5ec3894ffa07f1)

Open commit detailssuccess

2 days agoSep 29, 2026

[3e3c6d6](https://github.com/NVIDIA/cosmos/commit/3e3c6d61dc15d6517c4793beab5ec3894ffa07f1) · 2 days agoSep 29, 2026

## History

[108 Commits](https://github.com/NVIDIA/cosmos/commits/main/)

Open commit details

[View commit history for this file.](https://github.com/NVIDIA/cosmos/commits/main/) 108 Commits

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| [.github](https://github.com/NVIDIA/cosmos/tree/main/.github ".github") | [.github](https://github.com/NVIDIA/cosmos/tree/main/.github ".github") | [docs: add issue templates and security policy (](https://github.com/NVIDIA/cosmos/commit/c92f9470e2460c2e0730174d9b2c5f9e9143320c "docs: add issue templates and security policy (#348)  Brings the new-issue chooser in this repo in line with [NVIDIA/cosmos-framework](https://github.com/NVIDIA/cosmos-framework): **Bug Report**, **Feature Request**, **Blank issue**, and **Report a security vulnerability**.  Today this repo has no `.github/ISSUE_TEMPLATE/` and no security policy, so every new issue starts blank.  ## What's added  | File | Source | Notes | | ---- | ------ | ----- | | `.github/ISSUE_TEMPLATE/bug_report.md` | cosmos-framework `main` | Same sections, `[BUG]` title prefix, `bug` label. Added **Model** and **Integration** rows to the System Information table; **no default assignees**, so reports go through normal triage. | | `.github/ISSUE_TEMPLATE/feature_request.md` | [cosmos-framework#245](https://github.com/NVIDIA/cosmos-framework/pull/245) | Same sections, `[FEAT]` title prefix, `enhancement` label. **Affected Area** scoped to this repo: cookbooks, evaluation, inference integrations, models, finetune/distill, docs. | | `SECURITY.md` | cosmos-framework `SECURITY.md` | NVIDIA PSIRT instructions, copied verbatim. Its presence is what adds the \"Report a security vulnerability\" entry to the chooser. |  Both `bug` and `enhancement` labels already exist in this repo.  Co-authored-by: Claude Opus 5 (1M context) <noreply@anthropic.com>") [#348](https://github.com/NVIDIA/cosmos/pull/348) [)](https://github.com/NVIDIA/cosmos/commit/c92f9470e2460c2e0730174d9b2c5f9e9143320c "docs: add issue templates and security policy (#348)  Brings the new-issue chooser in this repo in line with [NVIDIA/cosmos-framework](https://github.com/NVIDIA/cosmos-framework): **Bug Report**, **Feature Request**, **Blank issue**, and **Report a security vulnerability**.  Today this repo has no `.github/ISSUE_TEMPLATE/` and no security policy, so every new issue starts blank.  ## What's added  | File | Source | Notes | | ---- | ------ | ----- | | `.github/ISSUE_TEMPLATE/bug_report.md` | cosmos-framework `main` | Same sections, `[BUG]` title prefix, `bug` label. Added **Model** and **Integration** rows to the System Information table; **no default assignees**, so reports go through normal triage. | | `.github/ISSUE_TEMPLATE/feature_request.md` | [cosmos-framework#245](https://github.com/NVIDIA/cosmos-framework/pull/245) | Same sections, `[FEAT]` title prefix, `enhancement` label. **Affected Area** scoped to this repo: cookbooks, evaluation, inference integrations, models, finetune/distill, docs. | | `SECURITY.md` | cosmos-framework `SECURITY.md` | NVIDIA PSIRT instructions, copied verbatim. Its presence is what adds the \"Report a security vulnerability\" entry to the chooser. |  Both `bug` and `enhancement` labels already exist in this repo.  Co-authored-by: Claude Opus 5 (1M context) <noreply@anthropic.com>") | 3 weeks agoSep 10, 2026 |
| [assets](https://github.com/NVIDIA/cosmos/tree/main/assets "assets") | [assets](https://github.com/NVIDIA/cosmos/tree/main/assets "assets") | [Readme revamp (](https://github.com/NVIDIA/cosmos/commit/093faf27053e6165af0510c19d76873eb5542fd9 "Readme revamp (#356)  Revamp the top level README file, add model reference page") [#356](https://github.com/NVIDIA/cosmos/pull/356) [)](https://github.com/NVIDIA/cosmos/commit/093faf27053e6165af0510c19d76873eb5542fd9 "Readme revamp (#356)  Revamp the top level README file, add model reference page") | last weekSep 22, 2026 |
| [cookbooks/cosmos3](https://github.com/NVIDIA/cosmos/tree/main/cookbooks/cosmos3 "This path skips through empty directories") | [cookbooks/cosmos3](https://github.com/NVIDIA/cosmos/tree/main/cookbooks/cosmos3 "This path skips through empty directories") | [Add TensorRT-LLM Transfer and Action guides (](https://github.com/NVIDIA/cosmos/commit/3e3c6d61dc15d6517c4793beab5ec3894ffa07f1 "Add TensorRT-LLM Transfer and Action guides (#310)  ## Summary  Add Cosmos3 Action and Transfer cookbooks for TensorRT-LLM's VisualGen serving API.  ### Action  - Forward dynamics from an AV conditioning image and action trajectory. - Inverse dynamics from an AV observation video. - Multipart `image_reference` and `video_reference` requests, safetensors decoding, and MP4 previews.  ### Transfer  - Edge, blur, depth, segmentation, and world-scenario (WSM) examples using the checked-in controls and captions. - Inline control inputs through `extra_params` and synchronous MP4 responses from `/v1/videos/sync`. - Per-control resolution, frame count, and guidance settings, with saved outputs and notebook previews.  ### Setup and documentation  - Shared TensorRT-LLM source setup and Nano/Super VisualGen launch commands. - Server-side guardrail setup that prepares NLTK resources as regular files and exports `NLTK_DATA`, with path security enabled. - Updated audiovisual API examples, explicit MP4 output, and links from the cookbook indexes.  ## Testing  Executed all code cells in the two Action notebooks and the Transfer notebook on one H200 using Cosmos3-Nano and a native build of TensorRT-LLM [`bca6761`](https://github.com/NVIDIA/TensorRT-LLM/commit/bca6761ab84fbcd58fc7f914eade7de48b32e35e). The run used the documented NLTK setup and server command, with `cosmos-guardrail==0.3.0` and `use_guardrails=True`.  | Example | Result | Video output | | --- | --- | --- | | Forward dynamics | PASS | 832×480, 61 frames, 10 fps | | Inverse dynamics | PASS | 832×480, 61 frames, 10 fps | | Transfer edge | PASS | 1280×720, 121 frames, 30 fps | | Transfer blur | PASS | 1104×832, 121 frames, 30 fps | | Transfer depth | PASS | 1280×720, 121 frames, 30 fps | | Transfer segmentation | PASS | 1280×720, 121 frames, 30 fps | | Transfer WSM | PASS | 1280×720, 100 frames, 10 fps |  All seven MP4s were decoded frame by frame. Both Action tensor payloads passed shape, dtype, and finite-value checks. All 40 tracked notebooks passed JSON/schema validation and the CI lint selection; the three added notebooks have cleared outputs and pass strict schema validation.  Guardrail coverage follows the package's default configuration: Blocklist and Qwen3Guard text checks plus RetinaFace face blurring; video-content classification is not enabled in 0.3.0.  The GPU results above cover Nano Action and Transfer.  ---------  Signed-off-by: Igor Shovkun <ishovkun@nvidia.com> Signed-off-by: Igor Shovkun <igshov@gmail.com>") [#310](https://github.com/NVIDIA/cosmos/pull/310) [)](https://github.com/NVIDIA/cosmos/commit/3e3c6d61dc15d6517c4793beab5ec3894ffa07f1 "Add TensorRT-LLM Transfer and Action guides (#310)  ## Summary  Add Cosmos3 Action and Transfer cookbooks for TensorRT-LLM's VisualGen serving API.  ### Action  - Forward dynamics from an AV conditioning image and action trajectory. - Inverse dynamics from an AV observation video. - Multipart `image_reference` and `video_reference` requests, safetensors decoding, and MP4 previews.  ### Transfer  - Edge, blur, depth, segmentation, and world-scenario (WSM) examples using the checked-in controls and captions. - Inline control inputs through `extra_params` and synchronous MP4 responses from `/v1/videos/sync`. - Per-control resolution, frame count, and guidance settings, with saved outputs and notebook previews.  ### Setup and documentation  - Shared TensorRT-LLM source setup and Nano/Super VisualGen launch commands. - Server-side guardrail setup that prepares NLTK resources as regular files and exports `NLTK_DATA`, with path security enabled. - Updated audiovisual API examples, explicit MP4 output, and links from the cookbook indexes.  ## Testing  Executed all code cells in the two Action notebooks and the Transfer notebook on one H200 using Cosmos3-Nano and a native build of TensorRT-LLM [`bca6761`](https://github.com/NVIDIA/TensorRT-LLM/commit/bca6761ab84fbcd58fc7f914eade7de48b32e35e). The run used the documented NLTK setup and server command, with `cosmos-guardrail==0.3.0` and `use_guardrails=True`.  | Example | Result | Video output | | --- | --- | --- | | Forward dynamics | PASS | 832×480, 61 frames, 10 fps | | Inverse dynamics | PASS | 832×480, 61 frames, 10 fps | | Transfer edge | PASS | 1280×720, 121 frames, 30 fps | | Transfer blur | PASS | 1104×832, 121 frames, 30 fps | | Transfer depth | PASS | 1280×720, 121 frames, 30 fps | | Transfer segmentation | PASS | 1280×720, 121 frames, 30 fps | | Transfer WSM | PASS | 1280×720, 100 frames, 10 fps |  All seven MP4s were decoded frame by frame. Both Action tensor payloads passed shape, dtype, and finite-value checks. All 40 tracked notebooks passed JSON/schema validation and the CI lint selection; the three added notebooks have cleared outputs and pass strict schema validation.  Guardrail coverage follows the package's default configuration: Blocklist and Qwen3Guard text checks plus RetinaFace face blurring; video-content classification is not enabled in 0.3.0.  The GPU results above cover Nano Action and Transfer.  ---------  Signed-off-by: Igor Shovkun <ishovkun@nvidia.com> Signed-off-by: Igor Shovkun <igshov@gmail.com>") | 2 days agoSep 29, 2026 |
| [docs/reference](https://github.com/NVIDIA/cosmos/tree/main/docs/reference "This path skips through empty directories") | [docs/reference](https://github.com/NVIDIA/cosmos/tree/main/docs/reference "This path skips through empty directories") | [Readme revamp (](https://github.com/NVIDIA/cosmos/commit/093faf27053e6165af0510c19d76873eb5542fd9 "Readme revamp (#356)  Revamp the top level README file, add model reference page") [#356](https://github.com/NVIDIA/cosmos/pull/356) [)](https://github.com/NVIDIA/cosmos/commit/093faf27053e6165af0510c19d76873eb5542fd9 "Readme revamp (#356)  Revamp the top level README file, add model reference page") | last weekSep 22, 2026 |
| [evaluation/cosmos3](https://github.com/NVIDIA/cosmos/tree/main/evaluation/cosmos3 "This path skips through empty directories") | [evaluation/cosmos3](https://github.com/NVIDIA/cosmos/tree/main/evaluation/cosmos3 "This path skips through empty directories") | [commit the full UGB evaluation script (](https://github.com/NVIDIA/cosmos/commit/9f18ce1e5859052ffd43156bf00cea56c13069e1 "commit the full UGB evaluation script (#289)") [#289](https://github.com/NVIDIA/cosmos/pull/289) [)](https://github.com/NVIDIA/cosmos/commit/9f18ce1e5859052ffd43156bf00cea56c13069e1 "commit the full UGB evaluation script (#289)") | 2 months agoAug 5, 2026 |
| [.gitignore](https://github.com/NVIDIA/cosmos/blob/main/.gitignore ".gitignore") | [.gitignore](https://github.com/NVIDIA/cosmos/blob/main/.gitignore ".gitignore") | [Add Cosmos3-Nano-Policy-DROID finetune cookbook (](https://github.com/NVIDIA/cosmos/commit/ff317a01084629d4a85dac5b798a8d20f114a520 "Add Cosmos3-Nano-Policy-DROID finetune cookbook (#225)  ## Summary - Add a public Cosmos3-Nano-Policy-DROID finetune cookbook for Cosmos3-Nano. - Add a launcher that validates staged DROID data, prepares the Wan2.2 VAE and base DCP checkpoint, then runs the framework SFT entrypoint. - Add the TOML wrapper for the `action_policy_droid_nano` experiment and link it from the action cookbook docs.  ## Validation - `git diff --check origin/main...HEAD` - `bash -n cookbooks/cosmos3/generator/action/finetune/launch_sft_action_policy_droid.sh` - Parsed `action_policy_droid_repro.toml` with `tomli` and verified experiment/shard/max_iter fields.  Co-authored-by: Claude Opus 4.8 <noreply@anthropic.com>") [#225](https://github.com/NVIDIA/cosmos/pull/225) [)](https://github.com/NVIDIA/cosmos/commit/ff317a01084629d4a85dac5b798a8d20f114a520 "Add Cosmos3-Nano-Policy-DROID finetune cookbook (#225)  ## Summary - Add a public Cosmos3-Nano-Policy-DROID finetune cookbook for Cosmos3-Nano. - Add a launcher that validates staged DROID data, prepares the Wan2.2 VAE and base DCP checkpoint, then runs the framework SFT entrypoint. - Add the TOML wrapper for the `action_policy_droid_nano` experiment and link it from the action cookbook docs.  ## Validation - `git diff --check origin/main...HEAD` - `bash -n cookbooks/cosmos3/generator/action/finetune/launch_sft_action_policy_droid.sh` - Parsed `action_policy_droid_repro.toml` with `tomli` and verified experiment/shard/max_iter fields.  Co-authored-by: Claude Opus 4.8 <noreply@anthropic.com>") | 4 months agoJun 23, 2026 |
| [CONTRIBUTING.md](https://github.com/NVIDIA/cosmos/blob/main/CONTRIBUTING.md "CONTRIBUTING.md") | [CONTRIBUTING.md](https://github.com/NVIDIA/cosmos/blob/main/CONTRIBUTING.md "CONTRIBUTING.md") | [docs: fix broken links to removed README sections (](https://github.com/NVIDIA/cosmos/commit/aa8cc7aad33fdc7fa3de20fa7122deca042950e0 "docs: fix broken links to removed README sections (#359)  Fix seven broken backlinks left by the README revamp. Point CUDA and checkpoint references to the maintained guides, and remove redundant backlinks where the instructions or authoritative links are already present.  The root README and code examples are unchanged.  Validation: checked the upstream guide sections, all 33 local fragment links in the edited files, and remaining root README backlinks across Markdown and notebooks. `git diff --check` passes.") [#359](https://github.com/NVIDIA/cosmos/pull/359) [)](https://github.com/NVIDIA/cosmos/commit/aa8cc7aad33fdc7fa3de20fa7122deca042950e0 "docs: fix broken links to removed README sections (#359)  Fix seven broken backlinks left by the README revamp. Point CUDA and checkpoint references to the maintained guides, and remove redundant backlinks where the instructions or authoritative links are already present.  The root README and code examples are unchanged.  Validation: checked the upstream guide sections, all 33 local fragment links in the edited files, and remaining root README backlinks across Markdown and notebooks. `git diff --check` passes.") | last weekSep 23, 2026 |
| [LICENSE](https://github.com/NVIDIA/cosmos/blob/main/LICENSE "LICENSE") | [LICENSE](https://github.com/NVIDIA/cosmos/blob/main/LICENSE "LICENSE") | [Import all content for the release.](https://github.com/NVIDIA/cosmos/commit/284be180c0aea34327eddbb20d9bdf277fa5ab80 "Import all content for the release.  Co-Authored-By: Chen-Hsuan Lin <chenhsuanl@nvidia.com> Co-Authored-By: Dinghao Yang <dinghaoy@nvidia.com> Co-Authored-By: Haotian Zhang <haotzhang@nvidia.com> Co-Authored-By: Hongchi Xia <hongchix@illinois.edu> Co-Authored-By: Imad E <ielhanafi@nvidia.com> Co-Authored-By: Jing Zhang <vinjn@users.noreply.github.com> Co-Authored-By: Jon Allen <joallen@nvidia.com> Co-Authored-By: Maciej Bala <mbala@nvidia.com> Co-Authored-By: Maosheng Liao <maoshengl@nvidia.com> Co-Authored-By: Max Zhaoshuo Li <maxzhaoshuol@nvidia.com> Co-Authored-By: Ming-Yu Liu <mingyul@nvidia.com> Co-Authored-By: Prithvijit Chattopadhyay <pchattopadhy@nvidia.com> Co-Authored-By: Sameer Dharur <sdharur@nvidia.com> Co-Authored-By: Sergiy Fefilatyev <fsergiy@nvidia.com> Co-Authored-By: Siddharth Gururani <sgururani@nvidia.com> Co-Authored-By: Sophia Huang <hhuang@berkeley.edu> Co-Authored-By: Tsung-Yi Lin <tsungyil@nvidia.com> Co-Authored-By: Wei-Cheng Tseng <weichengt@nvidia.com> Co-Authored-By: Yatian Pang <ypang@nvidia.com> Co-Authored-By: Yogesh Balaji <ybalaji@nvidia.com> Co-Authored-By: ashawkey <ashawkey1999@gmail.com> Co-Authored-By: pjannaty <107573555+pjannaty@users.noreply.github.com> Co-Authored-By: vincentz <vincentz@nvidia.com>") | 5 months agoJun 1, 2026 |
| [README.md](https://github.com/NVIDIA/cosmos/blob/main/README.md "README.md") | [README.md](https://github.com/NVIDIA/cosmos/blob/main/README.md "README.md") | [docs: add Guardrail access in the quickstart example (](https://github.com/NVIDIA/cosmos/commit/77ef1929437fab1b4a39e18399539354512fc9c2 "docs: add Guardrail access in the quickstart example (#358)  Running the quickstart enables Guardrail by default and requires access to its separate gated repository. Add that prerequisite before the code and clarify that login alone does not grant access.") [#358](https://github.com/NVIDIA/cosmos/pull/358) [)](https://github.com/NVIDIA/cosmos/commit/77ef1929437fab1b4a39e18399539354512fc9c2 "docs: add Guardrail access in the quickstart example (#358)  Running the quickstart enables Guardrail by default and requires access to its separate gated repository. Add that prerequisite before the code and clarify that login alone does not grant access.") | last weekSep 23, 2026 |
| [RELEASE.md](https://github.com/NVIDIA/cosmos/blob/main/RELEASE.md "RELEASE.md") | [RELEASE.md](https://github.com/NVIDIA/cosmos/blob/main/RELEASE.md "RELEASE.md") | [Import all content for the release.](https://github.com/NVIDIA/cosmos/commit/284be180c0aea34327eddbb20d9bdf277fa5ab80 "Import all content for the release.  Co-Authored-By: Chen-Hsuan Lin <chenhsuanl@nvidia.com> Co-Authored-By: Dinghao Yang <dinghaoy@nvidia.com> Co-Authored-By: Haotian Zhang <haotzhang@nvidia.com> Co-Authored-By: Hongchi Xia <hongchix@illinois.edu> Co-Authored-By: Imad E <ielhanafi@nvidia.com> Co-Authored-By: Jing Zhang <vinjn@users.noreply.github.com> Co-Authored-By: Jon Allen <joallen@nvidia.com> Co-Authored-By: Maciej Bala <mbala@nvidia.com> Co-Authored-By: Maosheng Liao <maoshengl@nvidia.com> Co-Authored-By: Max Zhaoshuo Li <maxzhaoshuol@nvidia.com> Co-Authored-By: Ming-Yu Liu <mingyul@nvidia.com> Co-Authored-By: Prithvijit Chattopadhyay <pchattopadhy@nvidia.com> Co-Authored-By: Sameer Dharur <sdharur@nvidia.com> Co-Authored-By: Sergiy Fefilatyev <fsergiy@nvidia.com> Co-Authored-By: Siddharth Gururani <sgururani@nvidia.com> Co-Authored-By: Sophia Huang <hhuang@berkeley.edu> Co-Authored-By: Tsung-Yi Lin <tsungyil@nvidia.com> Co-Authored-By: Wei-Cheng Tseng <weichengt@nvidia.com> Co-Authored-By: Yatian Pang <ypang@nvidia.com> Co-Authored-By: Yogesh Balaji <ybalaji@nvidia.com> Co-Authored-By: ashawkey <ashawkey1999@gmail.com> Co-Authored-By: pjannaty <107573555+pjannaty@users.noreply.github.com> Co-Authored-By: vincentz <vincentz@nvidia.com>") | 5 months agoJun 1, 2026 |
| [SECURITY.md](https://github.com/NVIDIA/cosmos/blob/main/SECURITY.md "SECURITY.md") | [SECURITY.md](https://github.com/NVIDIA/cosmos/blob/main/SECURITY.md "SECURITY.md") | [docs: add issue templates and security policy (](https://github.com/NVIDIA/cosmos/commit/c92f9470e2460c2e0730174d9b2c5f9e9143320c "docs: add issue templates and security policy (#348)  Brings the new-issue chooser in this repo in line with [NVIDIA/cosmos-framework](https://github.com/NVIDIA/cosmos-framework): **Bug Report**, **Feature Request**, **Blank issue**, and **Report a security vulnerability**.  Today this repo has no `.github/ISSUE_TEMPLATE/` and no security policy, so every new issue starts blank.  ## What's added  | File | Source | Notes | | ---- | ------ | ----- | | `.github/ISSUE_TEMPLATE/bug_report.md` | cosmos-framework `main` | Same sections, `[BUG]` title prefix, `bug` label. Added **Model** and **Integration** rows to the System Information table; **no default assignees**, so reports go through normal triage. | | `.github/ISSUE_TEMPLATE/feature_request.md` | [cosmos-framework#245](https://github.com/NVIDIA/cosmos-framework/pull/245) | Same sections, `[FEAT]` title prefix, `enhancement` label. **Affected Area** scoped to this repo: cookbooks, evaluation, inference integrations, models, finetune/distill, docs. | | `SECURITY.md` | cosmos-framework `SECURITY.md` | NVIDIA PSIRT instructions, copied verbatim. Its presence is what adds the \"Report a security vulnerability\" entry to the chooser. |  Both `bug` and `enhancement` labels already exist in this repo.  Co-authored-by: Claude Opus 5 (1M context) <noreply@anthropic.com>") [#348](https://github.com/NVIDIA/cosmos/pull/348) [)](https://github.com/NVIDIA/cosmos/commit/c92f9470e2460c2e0730174d9b2c5f9e9143320c "docs: add issue templates and security policy (#348)  Brings the new-issue chooser in this repo in line with [NVIDIA/cosmos-framework](https://github.com/NVIDIA/cosmos-framework): **Bug Report**, **Feature Request**, **Blank issue**, and **Report a security vulnerability**.  Today this repo has no `.github/ISSUE_TEMPLATE/` and no security policy, so every new issue starts blank.  ## What's added  | File | Source | Notes | | ---- | ------ | ----- | | `.github/ISSUE_TEMPLATE/bug_report.md` | cosmos-framework `main` | Same sections, `[BUG]` title prefix, `bug` label. Added **Model** and **Integration** rows to the System Information table; **no default assignees**, so reports go through normal triage. | | `.github/ISSUE_TEMPLATE/feature_request.md` | [cosmos-framework#245](https://github.com/NVIDIA/cosmos-framework/pull/245) | Same sections, `[FEAT]` title prefix, `enhancement` label. **Affected Area** scoped to this repo: cookbooks, evaluation, inference integrations, models, finetune/distill, docs. | | `SECURITY.md` | cosmos-framework `SECURITY.md` | NVIDIA PSIRT instructions, copied verbatim. Its presence is what adds the \"Report a security vulnerability\" entry to the chooser. |  Both `bug` and `enhancement` labels already exist in this repo.  Co-authored-by: Claude Opus 5 (1M context) <noreply@anthropic.com>") | 3 weeks agoSep 10, 2026 |
| [inference\_benchmarks.md](https://github.com/NVIDIA/cosmos/blob/main/inference_benchmarks.md "inference_benchmarks.md") | [inference\_benchmarks.md](https://github.com/NVIDIA/cosmos/blob/main/inference_benchmarks.md "inference_benchmarks.md") | [cookbooks/cosmos3 audiovisual + benchmarks: remove Cosmos3-Edge t2i/t…](https://github.com/NVIDIA/cosmos/commit/f9c425669bffd2bf910067fbef7e0d5d8240fa84 "cookbooks/cosmos3 audiovisual + benchmarks: remove Cosmos3-Edge t2i/t2v examples (#324)  Cosmos3-Edge is image-to-video focused (256p/480p). This removes the text-to-image and text-to-video Edge examples and benchmark columns so the Edge material reflects i2v only.  Changes: - cookbooks/cosmos3/generator/audiovisual/run_with_diffusers.ipynb: remove the Edge text-to-image and text-to-video example cells (keep Edge i2v). - cookbooks/cosmos3/generator/audiovisual/run_with_vllm_omni.ipynb: same removal (keep Edge i2v). - inference_benchmarks.md: drop the Text-to-Video and Text-to-Image columns from the Cosmos3-Edge Generator latency tables (vLLM-Omni + PyTorch), and update the intro/notes to i2v only.  Not touched: run_with_cosmos_framework.ipynb (its Edge example is already i2v-only) and README.md.  ---------  Co-authored-by: Claude Opus 4.8 (1M context) <noreply@anthropic.com>") | 2 months agoAug 18, 2026 |
| View all files |

## Repository files navigation

[![NVIDIA Cosmos](https://github.com/NVIDIA/cosmos/raw/main/assets/brand/cosmos-logo.png)](https://github.com/NVIDIA/cosmos/blob/main/assets/brand/cosmos-logo.png)

# NVIDIA Cosmos

[Permalink: NVIDIA Cosmos](https://github.com/nvidia/cosmos#nvidia-cosmos)

### World Foundation Models for Physical AI

[Permalink: World Foundation Models for Physical AI](https://github.com/nvidia/cosmos#world-foundation-models-for-physical-ai)

**One model family that sees, reasons, simulates, and acts.**

[![Models](https://camo.githubusercontent.com/0f5772b1ed407a470ee15f6603faa8fac238e61933a3e6ecf3b5dc1a62c81317/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d436f736d6f73253230332532306d6f64656c732d6666643231653f6c6f676f3d68756767696e6766616365266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d353535)](https://huggingface.co/collections/nvidia/cosmos3)[![Paper](https://camo.githubusercontent.com/2f68774063c917c7cb146a6e030cc9ce270ef02cb487c31e4c2d9d52ff284427/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d546563686e6963616c2532305265706f72742d3736623930303f6c6f676f3d6172786976266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d353535)](https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf)[![Website](https://github.com/NVIDIA/cosmos/raw/main/assets/brand/badge-website.svg)](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)[![Discussions](https://camo.githubusercontent.com/910de443c3327876bc010dac2423198eecaa883e123dc005e30c0206cce3f832/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d44697363757373696f6e732d3138313731373f6c6f676f3d676974687562266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d353535)](https://github.com/NVIDIA/cosmos/discussions)

[**Try it in your browser**](https://build.nvidia.com/nvidia/cosmos3-nano-reasoner) · [**Quickstart**](https://github.com/nvidia/cosmos#generate-your-first-video) · [**Find your path**](https://github.com/nvidia/cosmos#find-your-path) · [**Model Family**](https://github.com/nvidia/cosmos#models)

|     |     |     |
| --- | --- | --- |
| [![Physics-aware generation: Newton's cradle](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/physics_newton_cradle.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/physics_newton_cradle.gif)[![Physics-aware generation: Newton's cradle](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/physics_newton_cradle.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/physics_newton_cradle.gif)[Open Physics-aware generation: Newton's cradle in new window](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/physics_newton_cradle.gif)[**Physics-aware generation**](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/generator/audiovisual/run_with_vllm_omni.ipynb)<br>A Newton's cradle in motion: momentum transfer rendered with physical fidelity | [![World-scenario transfer: control layout to photoreal driving video](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/transfer_worldscenario.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/transfer_worldscenario.gif)[![World-scenario transfer: control layout to photoreal driving video](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/transfer_worldscenario.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/transfer_worldscenario.gif)[Open World-scenario transfer: control layout to photoreal driving video in new window](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/transfer_worldscenario.gif)[**Transfer**](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/generator/transfer/run_video_transfer_with_vllm_omni.ipynb)<br>World-scenario control layout → photoreal driving video | [![Robot policy executing a manipulation task](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/policy_screwdriver.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/policy_screwdriver.gif)[![Robot policy executing a manipulation task](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/policy_screwdriver.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/policy_screwdriver.gif)[Open Robot policy executing a manipulation task in new window](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/policy_screwdriver.gif)[**Action policy**](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/generator/action/run_policy_with_vllm_omni.ipynb)<br>Policy run: "put the screwdriver and the glove in the purple container" |
| [![Driving simulation for autonomous vehicles](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/driving_sim_falling_rocks.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/driving_sim_falling_rocks.gif)[![Driving simulation for autonomous vehicles](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/driving_sim_falling_rocks.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/driving_sim_falling_rocks.gif)[Open Driving simulation for autonomous vehicles in new window](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/driving_sim_falling_rocks.gif)[**Simulation**](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/generator/audiovisual/run_with_vllm_omni.ipynb)<br>Generate synthetic data and create simulation for autonomous driving | [![Forward dynamics egocentric rollout](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/fd_egocentric_repair_poses.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/fd_egocentric_repair_poses.gif)[![Forward dynamics egocentric rollout](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/fd_egocentric_repair_poses.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/fd_egocentric_repair_poses.gif)[Open Forward dynamics egocentric rollout in new window](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/fd_egocentric_repair_poses.gif)[**Action-conditioned World Model**](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/generator/action/run_fd_with_vllm_omni.ipynb)<br>Forward dynamics: egocentric rollout from input camera + hand pose | [![World Reasoner: dashcam hazard anticipation](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/reasoner_driving_hazard.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/reasoner_driving_hazard.gif)[![World Reasoner: dashcam hazard anticipation](https://github.com/NVIDIA/cosmos/raw/main/assets/demos/reasoner_driving_hazard.gif)](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/reasoner_driving_hazard.gif)[Open World Reasoner: dashcam hazard anticipation in new window](https://github.com/NVIDIA/cosmos/blob/main/assets/demos/reasoner_driving_hazard.gif)[**World reasoning**](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/reasoner/run_with_vllm.ipynb)<br>Reason in complex real-world scenarios: a rolling ball means a child or pet may follow |

* * *

## What's new

[Permalink: What's new](https://github.com/nvidia/cosmos#whats-new)

- **\[Jul 2026\]** [Cosmos3-Edge](https://huggingface.co/nvidia/Cosmos3-Edge) released — the 4B tier for on-device, real-time deployment (Jetson AGX Orin / Thor / RTX Pro 6000).
- **\[May 2026\]** Cosmos 3 released: [HF collection](https://huggingface.co/collections/nvidia/cosmos3) · [Technical Report](https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf).

## What is Cosmos?

[Permalink: What is Cosmos?](https://github.com/nvidia/cosmos#what-is-cosmos)

NVIDIA Cosmos is an open platform for building physical AI applications — robots, autonomous vehicles, and smart infrastructure — providing better data, better environment, better starting point, and better tooling for physical AI developers. **Cosmos 3**, the current model family, is a suite of omnimodal world models built on a unified Mixture-of-Transformers architecture ( [technical report](https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf)).

One model, two surfaces:

|  | Inputs | Outputs | Use it for |
| --- | --- | --- | --- |
| **Reasoner** | text, vision | text | world understanding, grounding, task planning, embodied reasoning |
| **Generator** | text, vision, sound, action | vision, sound, action | world simulation, future prediction, synthetic data, policy learning |

This repository is the home of the models: everything for exploring, running, and evaluating Cosmos. For model training (SFT, LoRA, RL, distillation etc.), go to [Cosmos Framework](https://github.com/NVIDIA/cosmos-framework). Use [Cosmos Curator](https://github.com/NVIDIA/cosmos-curator) for data curation, and [Cosmos Evaluator](https://github.com/NVIDIA/cosmos-evaluator) for model output evaluation.

## Find your path

[Permalink: Find your path](https://github.com/nvidia/cosmos#find-your-path)

| I want to… | Go to | Time |
| :-- | :-- | :-- |
| **See it work** — zero install | [Video generation](https://build.nvidia.com/nvidia/cosmos3-nano), [visual reasoning](https://build.nvidia.com/nvidia/cosmos3-nano-reasoner) | 1 min |
| **Generate my first video** | [Quickstart ↓](https://github.com/nvidia/cosmos#generate-your-first-video) | 10 min |
| **Reason over images & video** | [Reasoner notebook](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/reasoner/run_with_vllm.ipynb) | 10 min |
| **Serve an OpenAI-compatible API** | [Serving setup guide](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md) — vLLM, vLLM-Omni, or NIM | 30 min |
| **Post-train on my own data** — SFT, distillation, RL | [Cosmos Framework](https://github.com/NVIDIA/cosmos-framework), then [evaluate here](https://github.com/NVIDIA/cosmos/blob/main/evaluation) | hours |
| **Explore runnable notebooks** | [Cookbooks](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md) | browse |
| **Evaluate a model** | [Evaluation suites](https://github.com/NVIDIA/cosmos/blob/main/evaluation) — PAIBench, Physics-IQ, VLMEvalKit | hours |
| **Check latency & throughput** | [Benchmarks](https://github.com/NVIDIA/cosmos/blob/main/inference_benchmarks.md) | browse |

## Generate your first video

[Permalink: Generate your first video](https://github.com/nvidia/cosmos#generate-your-first-video)

Before running the code, request access to [nvidia/Cosmos-1.0-Guardrail](https://huggingface.co/nvidia/Cosmos-1.0-Guardrail) and accept its access conditions. Once access is granted, log in below with a Hugging Face read token from the same account. Logging in alone does not grant access.

```
uv venv --python 3.13 --seed --managed-python && source .venv/bin/activate
uv pip install --torch-backend=auto \
  "diffusers @ git+https://github.com/huggingface/diffusers.git" \
  accelerate av cosmos_guardrail huggingface_hub imageio imageio-ffmpeg \
  torch torchvision transformers
uvx hf@latest auth login   # Authenticate for the gated Guardrail repository
```

```
import torch
from diffusers import Cosmos3OmniPipeline
from diffusers.utils import export_to_video

pipe = Cosmos3OmniPipeline.from_pretrained(
    "nvidia/Cosmos3-Nano", torch_dtype=torch.bfloat16, device_map="cuda"
)
video = pipe(prompt="A mobile robot navigates a warehouse aisle and stops at a shelf.").video
export_to_video(video, "first_video.mp4", fps=24)
```

First run downloads the 16B checkpoint; diffusion steps are compute-heavy, so long step times are normal. Full options, image/sound modes, and every other backend: [audiovisual cookbooks](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/generator/audiovisual) · setup issues: [environment setup guide](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md).

## Models

[Permalink: Models](https://github.com/nvidia/cosmos#models)

**Cosmos 3 ships as three base models** — every deployment tier, one omnimodal architecture:

| Base model | Size | Runs on | Best for |
| --- | --- | --- | --- |
| [Cosmos3-Super](https://huggingface.co/nvidia/Cosmos3-Super) | 64B | H200 / B200 / GB200 | Highest quality; synthetic data generation; teacher for distillation |
| [Cosmos3-Nano](https://huggingface.co/nvidia/Cosmos3-Nano) | 16B | RTX Pro 6000 / H100 / B200 | Balanced speed and quality; strong base model to post-train |
| [Cosmos3-Edge](https://huggingface.co/nvidia/Cosmos3-Edge) | 4B | Jetson AGX Orin / Thor / RTX Pro 6000 | Edge deployment; real-time robot policy and visual reasoning |

**Example checkpoints** in the [cosmos3-examples](https://huggingface.co/collections/nvidia/cosmos3-examples) collection are post-trained variants of the base models. They demonstrate what [post-training with Cosmos Framework](https://github.com/NVIDIA/cosmos-framework) can specialize Cosmos for — they're capability demos, not part of the product line:

| Example checkpoint | Base | Demonstrates |
| --- | --- | --- |
| [Cosmos3-Super-Text2Image](https://huggingface.co/nvidia/Cosmos3-Super-Text2Image) | Super | Elite quality text-to-image |
| [Cosmos3-Super-Text2Image-4Step](https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step) | Super | Elite quality text-to-image, 17-25x faster |
| [Cosmos3-Super-Image2Video](https://huggingface.co/nvidia/Cosmos3-Super-Image2Video) | Super | Elite quality image-to-video |
| [Cosmos3-Super-Image2Video-4Step](https://huggingface.co/nvidia/Cosmos3-Super-Image2Video-4Step) | Super | Elite quality image-to-video, 17-25x faster |
| [Cosmos3-Nano-Policy-DROID](https://huggingface.co/nvidia/Cosmos3-Nano-Policy-DROID) | Nano | Open SOTA DROID robot policy, runs on RTX Pro 6000 |
| [Cosmos3-Edge-Policy-DROID](https://huggingface.co/nvidia/Cosmos3-Edge-Policy-DROID) | Edge | DROID robot policy at edge-deployable scale |

Full I/O specs, generation settings, and supported action embodiments: [model reference](https://github.com/NVIDIA/cosmos/blob/main/docs/reference/models.md).

## Repository map

[Permalink: Repository map](https://github.com/nvidia/cosmos#repository-map)

```
cosmos/
├── cookbooks/          # runnable notebooks for every capability (start here to explore)
│   └── cosmos3/        # generator (audiovisual · action · transfer) · reasoner + prompt guide
├── evaluation/         # quality benchmark suites: PAIBench, Physics-IQ, RBench, UniGenBench, VLMEvalKit
├── docs/
│   └── reference/      # lookup: model reference
├── assets/             # brand + demo media
└── README.md           # you are here
```

Training, optimization, and deployment tooling lives in [Cosmos Framework](https://github.com/NVIDIA/cosmos-framework).

## Platform

[Permalink: Platform](https://github.com/nvidia/cosmos#platform)

| Project | Purpose |
| --- | --- |
| **Cosmos** | This repo |
| [Cosmos Framework](https://github.com/NVIDIA/cosmos-framework) | Train, optimize, and deploy physical AI models — SFT · LoRA · distillation · RL post-training, for Cosmos and beyond |
| [Cosmos Curator](https://github.com/NVIDIA/cosmos-curator) | Distributed data curation: processing, annotation, filtering, dedup |
| [Cosmos Evaluator](https://github.com/NVIDIA/cosmos-evaluator) | Automated evaluation system for world generation & reasoning outputs |

Cosmos 3 runs on Diffusers, Transformers, vLLM, vLLM-Omni, SGLang, TensorRT-LLM, and NIM — pick a backend in the [environment setup guide](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md).

## Community & contributing

[Permalink: Community & contributing](https://github.com/nvidia/cosmos#community--contributing)

Questions and ideas → [Discussions](https://github.com/NVIDIA/cosmos/discussions). Bugs → [Issues](https://github.com/NVIDIA/cosmos/issues). Code → [CONTRIBUTING.md](https://github.com/NVIDIA/cosmos/blob/main/CONTRIBUTING.md).

## Limitations & safety

[Permalink: Limitations & safety](https://github.com/nvidia/cosmos#limitations--safety)

Cosmos 3 can produce artifacts in long, high-resolution, or physically complex outputs (temporal inconsistency, object morphing, implausible dynamics). Safety-critical applications need additional validation and system-level safety analysis. Generation ships with [guardrails](https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md) on by default.

## Citation & license

[Permalink: Citation & license](https://github.com/nvidia/cosmos#citation--license)

```
@techreport{nvidia2026cosmos3,
  title  = {Cosmos 3: Omnimodal World Models for physical AI},
  author = {{NVIDIA Cosmos Team}},
  year   = {2026},
  url    = {https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf}
}
```

Source code and models are released under [OpenMDW-1.1](https://openmdw.ai/license/1-1/). Custom licensing: [cosmos-license@nvidia.com](mailto:cosmos-license@nvidia.com). This project may download third-party open source software; review those licenses before use.

## About

NVIDIA Cosmos is an open platform of world models, datasets, and tools that enables developers to build Physical AI for robots, autonomous vehicles, smart infrastructure, and more.

[www.nvidia.com/en-us/ai/cosmos/](https://www.nvidia.com/en-us/ai/cosmos/)

### Resources

[Readme](https://github.com/nvidia/cosmos#readme-ov-file)

[License](https://github.com/nvidia/cosmos#License-1-ov-file)

### Contributing

[Contributing](https://github.com/nvidia/cosmos#contributing-ov-file)

### Security policy

[Security policy](https://github.com/nvidia/cosmos#security-ov-file)

[Activity](https://github.com/NVIDIA/cosmos/activity)

[Custom properties](https://github.com/NVIDIA/cosmos/custom-properties)

### Stars

**12.0k** stars

### Watchers

**94** watching

### Forks

[**898** forks](https://github.com/NVIDIA/cosmos/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FNVIDIA%2Fcosmos&report=NVIDIA+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

You can’t perform that action at this time.