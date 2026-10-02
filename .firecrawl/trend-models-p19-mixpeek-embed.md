[Skip to content](https://github.com/mixpeek/video-embedding-benchmark#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/mixpeek/video-embedding-benchmark) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/mixpeek/video-embedding-benchmark) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/mixpeek/video-embedding-benchmark) to refresh your session.Dismiss alert

{{ message }}

[mixpeek](https://github.com/mixpeek)/ **[video-embedding-benchmark](https://github.com/mixpeek/video-embedding-benchmark)** Public

- [Notifications](https://github.com/login?return_to=%2Fmixpeek%2Fvideo-embedding-benchmark) You must be signed in to change notification settings
- [Fork\\
1](https://github.com/login?return_to=%2Fmixpeek%2Fvideo-embedding-benchmark)
- [Star\\
5](https://github.com/login?return_to=%2Fmixpeek%2Fvideo-embedding-benchmark)


main

[**1** Branch](https://github.com/mixpeek/video-embedding-benchmark/branches) [**0** Tags](https://github.com/mixpeek/video-embedding-benchmark/tags)

[Go to Branches page](https://github.com/mixpeek/video-embedding-benchmark/branches)[Go to Tags page](https://github.com/mixpeek/video-embedding-benchmark/tags)

Go to file

Code

Open more actions menu

## Latest commit

![esteininger](https://avatars.githubusercontent.com/u/15973166?v=4&size=40)![claude](https://avatars.githubusercontent.com/u/81847?v=4&size=40)

[esteininger](https://github.com/mixpeek/video-embedding-benchmark/commits?author=esteininger)

and

[claude](https://github.com/mixpeek/video-embedding-benchmark/commits?author=claude)

[Add Gemini embedding generations; correct the "Gemini Embedding 2" la…](https://github.com/mixpeek/video-embedding-benchmark/commit/2faa379ea5cfe78702a4ffcf0a29afd50db5967a)

Open commit details

2 months agoAug 14, 2026

[2faa379](https://github.com/mixpeek/video-embedding-benchmark/commit/2faa379ea5cfe78702a4ffcf0a29afd50db5967a) · 2 months agoAug 14, 2026

## History

[2 Commits](https://github.com/mixpeek/video-embedding-benchmark/commits/main/)

Open commit details

[View commit history for this file.](https://github.com/mixpeek/video-embedding-benchmark/commits/main/) 2 Commits

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| [configs](https://github.com/mixpeek/video-embedding-benchmark/tree/main/configs "configs") | [configs](https://github.com/mixpeek/video-embedding-benchmark/tree/main/configs "configs") | [Initial release: video embedding benchmark with 6 models, dataset, an…](https://github.com/mixpeek/video-embedding-benchmark/commit/5fca6028e9ca7ae1d55bf7cc486b84a4d3a51f12 "Initial release: video embedding benchmark with 6 models, dataset, and results  20 CC0 videos (Pexels), 60 graded-relevance queries, standard IR metrics (NDCG, MRR, Recall, mAP). Models: Gemini Embedding 2, Twelve Labs Marengo 2.7, Mixedbread Wholembed v3, X-CLIP Base, SigLIP 2 SO400M, InternVideo2-Stage2 6B.  Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>") | 7 months agoMar 12, 2026 |
| [data](https://github.com/mixpeek/video-embedding-benchmark/tree/main/data "data") | [data](https://github.com/mixpeek/video-embedding-benchmark/tree/main/data "data") | [Initial release: video embedding benchmark with 6 models, dataset, an…](https://github.com/mixpeek/video-embedding-benchmark/commit/5fca6028e9ca7ae1d55bf7cc486b84a4d3a51f12 "Initial release: video embedding benchmark with 6 models, dataset, and results  20 CC0 videos (Pexels), 60 graded-relevance queries, standard IR metrics (NDCG, MRR, Recall, mAP). Models: Gemini Embedding 2, Twelve Labs Marengo 2.7, Mixedbread Wholembed v3, X-CLIP Base, SigLIP 2 SO400M, InternVideo2-Stage2 6B.  Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>") | 7 months agoMar 12, 2026 |
| [flash\_attn](https://github.com/mixpeek/video-embedding-benchmark/tree/main/flash_attn "flash_attn") | [flash\_attn](https://github.com/mixpeek/video-embedding-benchmark/tree/main/flash_attn "flash_attn") | [Initial release: video embedding benchmark with 6 models, dataset, an…](https://github.com/mixpeek/video-embedding-benchmark/commit/5fca6028e9ca7ae1d55bf7cc486b84a4d3a51f12 "Initial release: video embedding benchmark with 6 models, dataset, and results  20 CC0 videos (Pexels), 60 graded-relevance queries, standard IR metrics (NDCG, MRR, Recall, mAP). Models: Gemini Embedding 2, Twelve Labs Marengo 2.7, Mixedbread Wholembed v3, X-CLIP Base, SigLIP 2 SO400M, InternVideo2-Stage2 6B.  Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>") | 7 months agoMar 12, 2026 |
| [models](https://github.com/mixpeek/video-embedding-benchmark/tree/main/models "models") | [models](https://github.com/mixpeek/video-embedding-benchmark/tree/main/models "models") | [Add Gemini embedding generations; correct the "Gemini Embedding 2" la…](https://github.com/mixpeek/video-embedding-benchmark/commit/2faa379ea5cfe78702a4ffcf0a29afd50db5967a "Add Gemini embedding generations; correct the \"Gemini Embedding 2\" label (MAR-106)  Extends the harness to the video-capable Gemini embedding generations and re-runs on the committed 20-video, 60-query dataset with the existing metrics.  The three ids the key exposes reduce to one scoreable video row: - gemini-embedding-2 scored fresh (NDCG@5 0.671, NDCG@10 0.764, MRR 0.896,   20/20 videos, 0 errors). - gemini-embedding-2-preview returns byte-identical embeddings (cosine 1.0), so   it is kept as results/audit/ evidence rather than a duplicate row. - gemini-embedding-001 is text-only and returns 400 on a video file, so it is   excluded from the video table with the measured error recorded.  The initial-release \"Gemini Embedding 2\" row actually ran the -preview alias; load_model now pins the canonical gemini-embedding-2 id. Details and coverage in results/GEMINI-GENERATIONS.md.  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>") | 2 months agoAug 14, 2026 |
| [results](https://github.com/mixpeek/video-embedding-benchmark/tree/main/results "results") | [results](https://github.com/mixpeek/video-embedding-benchmark/tree/main/results "results") | [Add Gemini embedding generations; correct the "Gemini Embedding 2" la…](https://github.com/mixpeek/video-embedding-benchmark/commit/2faa379ea5cfe78702a4ffcf0a29afd50db5967a "Add Gemini embedding generations; correct the \"Gemini Embedding 2\" label (MAR-106)  Extends the harness to the video-capable Gemini embedding generations and re-runs on the committed 20-video, 60-query dataset with the existing metrics.  The three ids the key exposes reduce to one scoreable video row: - gemini-embedding-2 scored fresh (NDCG@5 0.671, NDCG@10 0.764, MRR 0.896,   20/20 videos, 0 errors). - gemini-embedding-2-preview returns byte-identical embeddings (cosine 1.0), so   it is kept as results/audit/ evidence rather than a duplicate row. - gemini-embedding-001 is text-only and returns 400 on a video file, so it is   excluded from the video table with the measured error recorded.  The initial-release \"Gemini Embedding 2\" row actually ran the -preview alias; load_model now pins the canonical gemini-embedding-2 id. Details and coverage in results/GEMINI-GENERATIONS.md.  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>") | 2 months agoAug 14, 2026 |
| [.gitignore](https://github.com/mixpeek/video-embedding-benchmark/blob/main/.gitignore ".gitignore") | [.gitignore](https://github.com/mixpeek/video-embedding-benchmark/blob/main/.gitignore ".gitignore") | [Initial release: video embedding benchmark with 6 models, dataset, an…](https://github.com/mixpeek/video-embedding-benchmark/commit/5fca6028e9ca7ae1d55bf7cc486b84a4d3a51f12 "Initial release: video embedding benchmark with 6 models, dataset, and results  20 CC0 videos (Pexels), 60 graded-relevance queries, standard IR metrics (NDCG, MRR, Recall, mAP). Models: Gemini Embedding 2, Twelve Labs Marengo 2.7, Mixedbread Wholembed v3, X-CLIP Base, SigLIP 2 SO400M, InternVideo2-Stage2 6B.  Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>") | 7 months agoMar 12, 2026 |
| [README.md](https://github.com/mixpeek/video-embedding-benchmark/blob/main/README.md "README.md") | [README.md](https://github.com/mixpeek/video-embedding-benchmark/blob/main/README.md "README.md") | [Add Gemini embedding generations; correct the "Gemini Embedding 2" la…](https://github.com/mixpeek/video-embedding-benchmark/commit/2faa379ea5cfe78702a4ffcf0a29afd50db5967a "Add Gemini embedding generations; correct the \"Gemini Embedding 2\" label (MAR-106)  Extends the harness to the video-capable Gemini embedding generations and re-runs on the committed 20-video, 60-query dataset with the existing metrics.  The three ids the key exposes reduce to one scoreable video row: - gemini-embedding-2 scored fresh (NDCG@5 0.671, NDCG@10 0.764, MRR 0.896,   20/20 videos, 0 errors). - gemini-embedding-2-preview returns byte-identical embeddings (cosine 1.0), so   it is kept as results/audit/ evidence rather than a duplicate row. - gemini-embedding-001 is text-only and returns 400 on a video file, so it is   excluded from the video table with the measured error recorded.  The initial-release \"Gemini Embedding 2\" row actually ran the -preview alias; load_model now pins the canonical gemini-embedding-2 id. Details and coverage in results/GEMINI-GENERATIONS.md.  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>") | 2 months agoAug 14, 2026 |
| [benchmark.py](https://github.com/mixpeek/video-embedding-benchmark/blob/main/benchmark.py "benchmark.py") | [benchmark.py](https://github.com/mixpeek/video-embedding-benchmark/blob/main/benchmark.py "benchmark.py") | [Add Gemini embedding generations; correct the "Gemini Embedding 2" la…](https://github.com/mixpeek/video-embedding-benchmark/commit/2faa379ea5cfe78702a4ffcf0a29afd50db5967a "Add Gemini embedding generations; correct the \"Gemini Embedding 2\" label (MAR-106)  Extends the harness to the video-capable Gemini embedding generations and re-runs on the committed 20-video, 60-query dataset with the existing metrics.  The three ids the key exposes reduce to one scoreable video row: - gemini-embedding-2 scored fresh (NDCG@5 0.671, NDCG@10 0.764, MRR 0.896,   20/20 videos, 0 errors). - gemini-embedding-2-preview returns byte-identical embeddings (cosine 1.0), so   it is kept as results/audit/ evidence rather than a duplicate row. - gemini-embedding-001 is text-only and returns 400 on a video file, so it is   excluded from the video table with the measured error recorded.  The initial-release \"Gemini Embedding 2\" row actually ran the -preview alias; load_model now pins the canonical gemini-embedding-2 id. Details and coverage in results/GEMINI-GENERATIONS.md.  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>") | 2 months agoAug 14, 2026 |
| [download\_dataset.py](https://github.com/mixpeek/video-embedding-benchmark/blob/main/download_dataset.py "download_dataset.py") | [download\_dataset.py](https://github.com/mixpeek/video-embedding-benchmark/blob/main/download_dataset.py "download_dataset.py") | [Initial release: video embedding benchmark with 6 models, dataset, an…](https://github.com/mixpeek/video-embedding-benchmark/commit/5fca6028e9ca7ae1d55bf7cc486b84a4d3a51f12 "Initial release: video embedding benchmark with 6 models, dataset, and results  20 CC0 videos (Pexels), 60 graded-relevance queries, standard IR metrics (NDCG, MRR, Recall, mAP). Models: Gemini Embedding 2, Twelve Labs Marengo 2.7, Mixedbread Wholembed v3, X-CLIP Base, SigLIP 2 SO400M, InternVideo2-Stage2 6B.  Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>") | 7 months agoMar 12, 2026 |
| [generate\_hero.py](https://github.com/mixpeek/video-embedding-benchmark/blob/main/generate_hero.py "generate_hero.py") | [generate\_hero.py](https://github.com/mixpeek/video-embedding-benchmark/blob/main/generate_hero.py "generate_hero.py") | [Initial release: video embedding benchmark with 6 models, dataset, an…](https://github.com/mixpeek/video-embedding-benchmark/commit/5fca6028e9ca7ae1d55bf7cc486b84a4d3a51f12 "Initial release: video embedding benchmark with 6 models, dataset, and results  20 CC0 videos (Pexels), 60 graded-relevance queries, standard IR metrics (NDCG, MRR, Recall, mAP). Models: Gemini Embedding 2, Twelve Labs Marengo 2.7, Mixedbread Wholembed v3, X-CLIP Base, SigLIP 2 SO400M, InternVideo2-Stage2 6B.  Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>") | 7 months agoMar 12, 2026 |
| [hero.png](https://github.com/mixpeek/video-embedding-benchmark/blob/main/hero.png "hero.png") | [hero.png](https://github.com/mixpeek/video-embedding-benchmark/blob/main/hero.png "hero.png") | [Initial release: video embedding benchmark with 6 models, dataset, an…](https://github.com/mixpeek/video-embedding-benchmark/commit/5fca6028e9ca7ae1d55bf7cc486b84a4d3a51f12 "Initial release: video embedding benchmark with 6 models, dataset, and results  20 CC0 videos (Pexels), 60 graded-relevance queries, standard IR metrics (NDCG, MRR, Recall, mAP). Models: Gemini Embedding 2, Twelve Labs Marengo 2.7, Mixedbread Wholembed v3, X-CLIP Base, SigLIP 2 SO400M, InternVideo2-Stage2 6B.  Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>") | 7 months agoMar 12, 2026 |
| [report.py](https://github.com/mixpeek/video-embedding-benchmark/blob/main/report.py "report.py") | [report.py](https://github.com/mixpeek/video-embedding-benchmark/blob/main/report.py "report.py") | [Add Gemini embedding generations; correct the "Gemini Embedding 2" la…](https://github.com/mixpeek/video-embedding-benchmark/commit/2faa379ea5cfe78702a4ffcf0a29afd50db5967a "Add Gemini embedding generations; correct the \"Gemini Embedding 2\" label (MAR-106)  Extends the harness to the video-capable Gemini embedding generations and re-runs on the committed 20-video, 60-query dataset with the existing metrics.  The three ids the key exposes reduce to one scoreable video row: - gemini-embedding-2 scored fresh (NDCG@5 0.671, NDCG@10 0.764, MRR 0.896,   20/20 videos, 0 errors). - gemini-embedding-2-preview returns byte-identical embeddings (cosine 1.0), so   it is kept as results/audit/ evidence rather than a duplicate row. - gemini-embedding-001 is text-only and returns 400 on a video file, so it is   excluded from the video table with the measured error recorded.  The initial-release \"Gemini Embedding 2\" row actually ran the -preview alias; load_model now pins the canonical gemini-embedding-2 id. Details and coverage in results/GEMINI-GENERATIONS.md.  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>") | 2 months agoAug 14, 2026 |
| [requirements.txt](https://github.com/mixpeek/video-embedding-benchmark/blob/main/requirements.txt "requirements.txt") | [requirements.txt](https://github.com/mixpeek/video-embedding-benchmark/blob/main/requirements.txt "requirements.txt") | [Initial release: video embedding benchmark with 6 models, dataset, an…](https://github.com/mixpeek/video-embedding-benchmark/commit/5fca6028e9ca7ae1d55bf7cc486b84a4d3a51f12 "Initial release: video embedding benchmark with 6 models, dataset, and results  20 CC0 videos (Pexels), 60 graded-relevance queries, standard IR metrics (NDCG, MRR, Recall, mAP). Models: Gemini Embedding 2, Twelve Labs Marengo 2.7, Mixedbread Wholembed v3, X-CLIP Base, SigLIP 2 SO400M, InternVideo2-Stage2 6B.  Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>") | 7 months agoMar 12, 2026 |
| View all files |

## Repository files navigation

# Video Embedding Model Benchmark: Retrieval Quality for Information Retrieval

[Permalink: Video Embedding Model Benchmark: Retrieval Quality for Information Retrieval](https://github.com/mixpeek/video-embedding-benchmark#video-embedding-model-benchmark-retrieval-quality-for-information-retrieval)

A head-to-head comparison of multimodal embedding models for text-to-video retrieval, tested on a standardized dataset with reproducible IR metrics.

## Results (6 of 7 models — Nova pending)

[Permalink: Results (6 of 7 models — Nova pending)](https://github.com/mixpeek/video-embedding-benchmark#results-6-of-7-models--nova-pending)

| Model | Dims | NDCG@5 | NDCG@10 | R@1 | R@5 | MRR | mAP@10 | Latency (ms) | Vec Size |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Gemini Embedding 2** | 3072 | 0.671 | **0.764** | 0.200 | 0.679 | 0.896 | 0.702 | 2094 | 12,288 B |
| **Twelve Labs Marengo 2.7**\* | 1024 | **0.721** | 0.760 | **0.250** | **0.743** | **1.000** | **0.737** | 18148 | 4,096 B |
| **Mixedbread Wholembed v3**\*\* | ColBERT | 0.644 | 0.757 | 0.216 | 0.649 | 0.932 | 0.688 | 500 | N/A |
| X-CLIP Base (temporal) | 512 | 0.327 | 0.470 | 0.067 | 0.367 | 0.520 | 0.338 | 192 | 2,048 B |
| SigLIP 2 SO400M (frame-avg) | 1152 | 0.202 | 0.325 | 0.075 | 0.237 | 0.466 | 0.204 | 636 | 4,608 B |
| InternVideo2-Stage2 6B | 768 | 0.186 | 0.302 | 0.046 | 0.237 | 0.405 | 0.170 | 24817 | 3,072 B |

\\* _Marengo results based on 34/60 queries (56%) due to Twelve Labs free-tier daily rate limit (50 req/day). Full results pending re-run._
\\*\\* _Mixedbread results based on 37/60 queries (62%) due to rate limiting. Uses Stores API (ColBERT-style late interaction) — no single embedding vector._

_Gemini row re-run August 2026. The key exposes three Gemini embedding ids, but on video they reduce to this one row: `gemini-embedding-2-preview` returns byte-identical embeddings to `gemini-embedding-2` (cosine 1.0), and `gemini-embedding-001` is text-only and cannot embed video. Evidence and coverage in [results/GEMINI-GENERATIONS.md](https://github.com/mixpeek/video-embedding-benchmark/blob/main/results/GEMINI-GENERATIONS.md)._

**Key takeaways:**

- The top 3 are all API models — Gemini, Marengo, and Mixedbread cluster tightly at NDCG@10 0.757–0.764
- Marengo's perfect MRR means the correct video was _always_ ranked #1 across all 34 evaluated queries — remarkable for a video-specialist model
- Mixedbread Wholembed v3 is a strong third at NDCG@10=0.757 with perfect MRR on hard negatives (1.000) — its ColBERT-style late interaction works well for video
- All three API models are 2x+ better than the best open-source option (X-CLIP at 0.470 NDCG@10)
- X-CLIP is the best open-source model despite being the smallest (512d) — temporal cross-frame attention matters more than model size
- InternVideo2 6B underperforms despite being 12x larger than X-CLIP — its Stage2 checkpoint is optimized for multimodal pretraining, not zero-shot retrieval
- Frame-averaging (SigLIP) is a poor proxy for video understanding — temporal structure matters
- Latency varies wildly: X-CLIP at 192ms (local GPU) vs Marengo at 18s (API processing). Mixedbread query latency is 500ms but requires upfront video upload
- Mixedbread's Stores-based approach is architecturally different — you upload videos once and search via API, no embedding vectors to manage

**Pending:** Amazon Nova Multimodal (need Bedrock model access). Marengo re-run for remaining 26 queries after rate limit reset.

## Models Under Test

[Permalink: Models Under Test](https://github.com/mixpeek/video-embedding-benchmark#models-under-test)

| # | Model | Provider | Dims | Video Native | Type | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **Gemini Embedding 2** | Google | 768–3072 (Matryoshka) | Yes | API | Done |
| 2 | **Twelve Labs Marengo 2.7** | Twelve Labs | 1024 | Yes | API | Partial (34/60 queries) |
| 3 | **Mixedbread Wholembed v3** | Mixedbread | ColBERT (late interaction) | Yes | API (Stores) | Partial (37/60 queries) |
| 4 | **X-CLIP Base** | Microsoft | 512 | Yes (cross-frame attn) | Open-source | Done |
| 5 | **Amazon Nova Multimodal** | Amazon (Bedrock) | 256–3072 (Matryoshka) | Yes | API | Pending (need Bedrock) |
| 6 | **SigLIP 2 SO400M** | Google (open) | 1152 | No (frame-avg baseline) | Open-source | Done |
| 7 | **InternVideo2-Stage2 6B** | OpenGVLab | 768 | Yes (temporal ViT) | Open-source | Done |

### Why These Models

[Permalink: Why These Models](https://github.com/mixpeek/video-embedding-benchmark#why-these-models)

- **Gemini Embedding 2**: Launched March 2026. First model to unify text, image, video, audio, and documents in one embedding space. The new standard.
- **Twelve Labs Marengo 3.0**: Purpose-built for video. Claims 78.5% composite vs. Nova's 61.8%. Handles 4K and 4-hour videos. The specialist.
- **Mixedbread Wholembed v3**: ColBERT-style late-interaction retrieval. Uses Stores API — upload videos, search with text. No single embedding vector; retrieval is done server-side.
- **X-CLIP Base**: Microsoft's video-text contrastive model. Extends CLIP with cross-frame temporal attention. Best open-source model with true temporal understanding.
- **Amazon Nova**: AWS's five-modality model on Bedrock. The enterprise default.
- **SigLIP 2 SO400M**: SOTA open-source image-text encoder. No video understanding — mean-pools 8 frames. Included as a baseline to quantify the cost of ignoring temporal structure.
- **InternVideo2-Stage2 6B**: OpenGVLab's video foundation model. Contrastive video-text pretraining with temporal ViT backbone + BERT-large text encoder. The largest open-source model in this benchmark.

## Dataset

[Permalink: Dataset](https://github.com/mixpeek/video-embedding-benchmark#dataset)

20 CC0 videos from Pexels (640x360, 24fps, ≤10s, H.264), normalized with ffmpeg:

| Category | Videos | Content |
| --- | --- | --- |
| Sports | 4 | Basketball, soccer, swimming, running |
| Cooking | 4 | Chopping, stirring, pouring, plating |
| Nature | 4 | Waterfall, ocean, forest, birds |
| Urban | 4 | Traffic, pedestrians, construction, skyline |
| Technology | 4 | Typing, soldering, 3D printing, robotics |

60 text queries with **graded relevance** (following BEIR/MTEB conventions):

- **relevance=2**: Exact match (query describes this specific video)
- **relevance=1**: Partial match (query describes the category)
- **relevance=0**: Irrelevant (implicit)

Three query types per video:

1. **Exact** — "A person chopping vegetables with a knife on a cutting board"
2. **Partial** — "Someone preparing food in a kitchen"
3. **Hard negative** — semantically adjacent but wrong domain (e.g., "A technician carefully assembling small electronic parts by hand" for a cooking video)

### Downloading

[Permalink: Downloading](https://github.com/mixpeek/video-embedding-benchmark#downloading)

```
python download_dataset.py  # No API key needed — uses direct Pexels CDN links
```

## Metrics

[Permalink: Metrics](https://github.com/mixpeek/video-embedding-benchmark#metrics)

Following standard IR evaluation (BEIR, MTEB):

- **NDCG@K** — Normalized Discounted Cumulative Gain with graded relevance (primary metric)
- **Recall@K** — Fraction of relevant docs retrieved in top K
- **MRR** — Mean Reciprocal Rank of first relevant result
- **mAP@10** — Mean Average Precision at 10
- **Latency** — Embedding time per video (median, p95)
- **Storage** — Bytes per embedding vector (float32)

## Running the Benchmark

[Permalink: Running the Benchmark](https://github.com/mixpeek/video-embedding-benchmark#running-the-benchmark)

### Prerequisites

[Permalink: Prerequisites](https://github.com/mixpeek/video-embedding-benchmark#prerequisites)

```
pip install -r requirements.txt
```

### API Keys (only for API models)

[Permalink: API Keys (only for API models)](https://github.com/mixpeek/video-embedding-benchmark#api-keys-only-for-api-models)

```
export GEMINI_API_KEY="..."            # Gemini Embedding 2
export TWELVE_LABS_API_KEY="..."       # Marengo 3.0
export AWS_ACCESS_KEY_ID="..."         # Nova (Bedrock)
export AWS_SECRET_ACCESS_KEY="..."
export AWS_DEFAULT_REGION="us-east-1"
export MIXEDBREAD_API_KEY="..."        # Wholembed v3
```

X-CLIP and SigLIP 2 run locally (MPS/CUDA/CPU).

### Run

[Permalink: Run](https://github.com/mixpeek/video-embedding-benchmark#run)

```
# Download dataset (no API key needed)
python download_dataset.py

# Run individual models
python benchmark.py --model gemini
python benchmark.py --model marengo
python benchmark.py --model xclip
python benchmark.py --model nova
python benchmark.py --model siglip
python benchmark.py --model mixedbread

# Run all
python benchmark.py --all

# Generate comparison report
python report.py
```

Results are written to `results/` as JSON + `results/COMPARISON.md`.

## Detailed Results by Query Type

[Permalink: Detailed Results by Query Type](https://github.com/mixpeek/video-embedding-benchmark#detailed-results-by-query-type)

### Exact Match (text describes a specific video)

[Permalink: Exact Match (text describes a specific video)](https://github.com/mixpeek/video-embedding-benchmark#exact-match-text-describes-a-specific-video)

| Model | NDCG@1 | NDCG@5 | R@1 | R@5 | MRR |
| --- | --- | --- | --- | --- | --- |
| Marengo 2.7\* | 0.556 | 0.662 | 0.250 | 0.667 | 1.000 |
| Gemini Embedding 2 | 0.600 | 0.652 | 0.200 | 0.600 | 0.887 |
| Mixedbread Wholembed v3\*\* | 0.564 | 0.630 | 0.231 | 0.615 | 0.962 |
| X-CLIP Base | 0.267 | 0.378 | 0.100 | 0.400 | 0.606 |
| SigLIP 2 (frame-avg) | 0.133 | 0.160 | 0.075 | 0.212 | 0.435 |
| InternVideo2 6B | 0.050 | 0.176 | 0.037 | 0.263 | 0.396 |

### Hard Negative (adjacent domain — model should NOT be confused)

[Permalink: Hard Negative (adjacent domain — model should NOT be confused)](https://github.com/mixpeek/video-embedding-benchmark#hard-negative-adjacent-domain--model-should-not-be-confused)

| Model | NDCG@1 | NDCG@5 | R@5 | MRR |
| --- | --- | --- | --- | --- |
| Marengo 2.7\* | 1.000 | 0.846 | 0.841 | 1.000 |
| Mixedbread Wholembed v3\*\* | 1.000 | 0.802 | 0.750 | 1.000 |
| Gemini Embedding 2 | 0.800 | 0.790 | 0.800 | 0.900 |
| X-CLIP Base | 0.200 | 0.322 | 0.350 | 0.467 |
| SigLIP 2 (frame-avg) | 0.400 | 0.236 | 0.200 | 0.556 |
| InternVideo2 6B | 0.200 | 0.220 | 0.250 | 0.423 |

Marengo and Mixedbread both achieve perfect NDCG@1 and MRR on hard negatives — never fooled by adjacent-domain queries. Gemini is close behind at 0.900 MRR.

\\* _Marengo: partial results — 34/60 queries evaluated._
\\*\\* _Mixedbread: partial results — 37/60 queries evaluated. Uses Stores-based retrieval (ColBERT-style)._

## Cost Comparison

[Permalink: Cost Comparison](https://github.com/mixpeek/video-embedding-benchmark#cost-comparison)

| Model | Pricing Model | Est. Cost / 1000 Videos |
| --- | --- | --- |
| Gemini Embedding 2 | Free tier (1K/day), then per-token | ~$0 (free tier) |
| Marengo 3.0 | $0.033/min | ~$5–15 |
| Mixedbread Wholembed v3 | Free tier, then per-token | ~$0 (free tier) |
| X-CLIP Base | Self-hosted | GPU/CPU cost only |
| Nova Multimodal | Bedrock per-token | ~$2–8 |
| SigLIP 2 | Self-hosted | GPU/CPU cost only |

## Methodology Notes

[Permalink: Methodology Notes](https://github.com/mixpeek/video-embedding-benchmark#methodology-notes)

- All embeddings L2-normalized to unit vectors; retrieval uses cosine similarity
- Random seed fixed at 42 for reproducibility
- Videos normalized to uniform specs (640x360, 24fps, 10s max, H.264) to control for input variation
- SigLIP 2 samples 8 frames uniformly and mean-pools frame embeddings
- X-CLIP samples 8 frames with cross-frame temporal attention
- Gemini processes the full video natively via file upload
- Marengo processes the full video natively via file upload (purpose-built video model)
- InternVideo2 samples 4 frames with temporal ViT backbone + BERT-large text encoder (6B params, CPU inference)
- Mixedbread uses Stores API (ColBERT-style late interaction) — videos uploaded once, retrieval via search endpoint. No single embedding vector; ranking done server-side
- Graded relevance (NDCG) is the primary metric because binary relevance (R@K) doesn't capture partial matches

## License

[Permalink: License](https://github.com/mixpeek/video-embedding-benchmark#license)

Benchmark code: MIT. Videos: CC0 (Pexels). Model weights subject to their respective licenses.

## About

Head-to-head benchmark of multimodal embedding models for text-to-video retrieval. 6 models, 20 CC0 videos, 60 queries, reproducible IR metrics (NDCG, MRR, Recall).

### Resources

[Readme](https://github.com/mixpeek/video-embedding-benchmark#readme-ov-file)

[Activity](https://github.com/mixpeek/video-embedding-benchmark/activity)

[Custom properties](https://github.com/mixpeek/video-embedding-benchmark/custom-properties)

### Stars

**5** stars

### Watchers

**0** watching

### Forks

[**1** fork](https://github.com/mixpeek/video-embedding-benchmark/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fmixpeek%2Fvideo-embedding-benchmark&report=mixpeek+%28user%29)

## Releases

## Packages

## Contributors

## Languages

You can’t perform that action at this time.