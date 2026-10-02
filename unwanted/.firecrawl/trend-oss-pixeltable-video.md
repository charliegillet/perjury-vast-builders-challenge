Intermediate · 30 min

# Video Intelligence Pipeline: Extract, Enrich, and Search Video at Scale

Build an end-to-end video analysis system with Pixeltable. Ingest video, extract frames, run multimodal AI models, generate embeddings, and enable semantic search, all as computed columns on a table.

[Quick Start](https://docs.pixeltable.com/overview/quick-start) [View on GitHub](https://github.com/pixeltable/pixeltable) [Documentation](https://docs.pixeltable.com/)

## The Challenge

Video analysis pipelines are notoriously fragmented. You need separate tools for frame extraction, object detection, transcription, embedding generation, and indexing, each with its own storage format, execution model, and failure modes. Adding a new model or changing extraction parameters means rewriting glue code.

## The Solution

Pixeltable treats video as a native data type. Define your entire pipeline, from ingestion through AI inference to embedding indexes, as computed columns on a table. Frame extraction, model inference, and indexing happen automatically and incrementally. Add a new video and everything updates.

## Implementation Guide

Step-by-step walkthrough with code examples

Step 1 of 5

01Ingest Videos02Extract Frames03Run AI Models04Build Embedding Indexes05Semantic Search

### Ingest Videos

Create a table with native Video columns and insert your media.

python

```python
1import pixeltable as pxt
2

3# Create a table with native video support
4videos = pxt.create_table('app.videos', {
5    'video': pxt.Video,
6    'title': pxt.String,
7    'category': pxt.String,
8})
9

10# Insert videos: local paths, URLs, or cloud storage
11videos.insert([\
12    {'video': 's3://bucket/marketing_demo.mp4',\
13     'title': 'Product Demo Q1', 'category': 'marketing'},\
14    {'video': '/data/training_session.mp4',\
15     'title': 'Onboarding Module 3', 'category': 'training'},\
16])
```

Pixeltable handles video storage and metadata together. No separate blob store or file registry needed.

PreviousUse arrow keys to navigateNext

### Key Benefits

85% less pipeline code vs custom video processing stacks

Incremental processing: only new videos trigger computation

Native multimodal types (Video, Image, Audio) with automatic format handling

Embedding indexes stay in sync without manual rebuilds

Full data lineage: trace any result back to its source frame and model version

### Real Applications

Content moderation and safety filtering at scale

Training video search and knowledge management

Marketing content tagging and optimization

Surveillance and security video analytics

Media asset management and discovery

### Prerequisites

Basic Python programming

Familiarity with AI/ML concepts

Python 3.9+

OpenAI API key (for Whisper transcription)

Google AI API key (for Gemini multimodal)

ffmpeg installed for video processing

### Performance

Pipeline Code Reduction

vs custom video processing stack

85%

Incremental Processing

Per new video added to pipeline

< 1 min

### Learn More

[AI Automation Workflow: The Pipeline Is the Table\\
\\
What “AI automation workflow” means when the work is multimodal](https://www.pixeltable.com/blog/ai-automation-workflow) [Object Detection in Videos with YOLOX\\
\\
Frame-level object detection pipeline walkthrough](https://www.pixeltable.com/blog/object-detection-videos-yolox) [Video Similarity Search\\
\\
Building cross-modal video search with embeddings](https://docs.pixeltable.com/use-cases/video-similarity-search) [Pixeltable Documentation\\
\\
Full API reference and guides](https://docs.pixeltable.com/)

### Related Guides

- [Production RAG: From Documents to Answers in One System](https://www.pixeltable.com/use-cases/production-rag-implementation)
Modality: Document

Computed column: Chunk view plus an embedding index
[Docs](https://docs.pixeltable.com/howto/cookbooks/text/doc-chunk-for-rag)
- [Computer Vision Pipeline: Object Detection, Classification, and Search](https://www.pixeltable.com/use-cases/computer-vision-pipeline-optimization)
Modality: Image

Computed column: Detection computed column on an Image or frame column
[Docs](https://docs.pixeltable.com/platform/type-system)
- [AI Agents & MCP: Give Your Agents Persistent Multimodal Memory](https://www.pixeltable.com/use-cases/ai-agents-mcp)
Modality: Agent state

Computed column: Tool results stored as computed columns on the row
[Docs](https://docs.pixeltable.com/overview/quick-start)

## Ready to get started?

Install Pixeltable and start building in minutes. One pip install, no infrastructure to manage.

[View on GitHub](https://github.com/pixeltable/pixeltable) [Quick Start Guide](https://docs.pixeltable.com/overview/quick-start) [Starter Kit](https://github.com/pixeltable/pixeltable-starter-kit)