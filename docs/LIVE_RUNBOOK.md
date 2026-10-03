# Live Team 41 operation

The deployed application uses real workshop data and services. Do not use fixture mode for the deliverable.

Connect with `ssh vast`, then `cd /home/yahyasalhinai/perjury-live`.
Run `source ./live-env.sh` before any live indexing, probe, or deployment command.
Credentials stay in `/config/team-41.config`; never commit or print them.

## Rebuild and deploy

```bash
source ./live-env.sh
.venv/bin/python -m perjury.index_i24 --sidecars
.venv/bin/python -m perjury.prerun_scene_probes
bash deploy/deploy.sh --dry-run
bash deploy/deploy.sh
```

Use system FFmpeg via `IMAGEIO_FFMPEG_EXE=/usr/bin/ffmpeg`.
The verified Cosmos model is `nvidia/cosmos3-nano-reasoner`.
The verified W&B parser model is `Qwen/Qwen3-30B-A3B-Instruct-2507`.
Canary requires `en-US` and works without a guessed model ID.

## Verify

```bash
export KUBECONFIG=/config/team-41-k8s.yaml
kubectl -n team-41 get pods,svc,ingress -l app=perjury
curl -fsS https://team-41-vss.thecosmoslabs.com/app/health
```

Inspect logs only after removing authentication tokens and signed query strings.
Test a typed claim, voice transcription, evidence image and video playback, stock VSS comparison, replay, and feedback.

## Available footage

Read-only database and S3 inspection found 180 I-24 segments from scene 1 and three cameras, over 300 seconds. All 180 detection sidecars were retrieved. Six real Cosmos condition/count probes were generated from distributed times across the archive.

Scenes 2 and 3 and the additional expected cameras are absent from Team 41 storage. Full coverage requires the organizers to restore that footage. Do not fabricate it or reduce quorum thresholds to hide the gap. Scene-wide assertions can legitimately remain UNPROVEN because eight valid camera votes are required.

## Development verification

On the Mac, use `.venv312/bin/python -m pytest -q`.
Test fixtures are isolated from the deployed live runtime.
Coordinate file ownership and deployment with other agents before editing shared files.


## VAST video playback and source scope

The camera wall uses native HTML video elements backed by `/api/camera-stream` and the authenticated VSS `videos/stream` endpoint. Range requests are proxied server-side; VSS credentials are not sent to the browser. Playback is recorded, indexed workshop footage, not an independently verified current RTSP/HLS camera feed. Claims use the indexed scene evidence and cached/current model assessments; the displayed playback position does not redefine claim scope. The execution trace updates during each real inference run.

The team VSS Explore page exposes indexed MP4 chunks and file uploads. No current live camera feed was confirmed in the inspected workshop UI. Live-capture backend sessions are separate from archived scene evidence and reject stale frames; they are not exposed as a VAST live camera source.

Service readiness was verified through actual S3 reads, VastDB evidence rows, VSS exploration, YOLO base64 clip inference, uncached Cosmos reasoning, embedding inference, Canary audio transcription, W&B structured inference and a Weave trace. YOLO remote signed-URL fetching can fail; use the tested base64 video input path.

## All-footage location chooser: verified API inventory

On 2026-10-02, authenticated Explore returned **414 distinct indexed parent chunks** across five pages (`limit=100`, offsets 0, 100, 200, 300, 400). This is archive availability, not 414 independent cameras or a current live feed.

| Location label | Parent chunks | Metadata camera IDs |
|---|---:|---|
| `toronto` | 180 | `pie_cam-3` |
| `san_francisco` | 92 | `sf_streets_cam-1` through `sf_streets_cam-4` |
| `neighborhood` | 52 | `neighborhood_cam-1` |
| `indoor` | 30 | `smartspace_cam-1` |
| `nashville` | 30 | `i24_cam-1`; filenames identify p1c1–p1c3 viewpoints |
| `warehouse3` | 30 | `sdg_warehouse_cam-2`; filename view/run metadata requires separate verification |

Use `GET /api/v1/videos/explore` with `scope=all|mine|public`, `location=<label>`, `date=YYYY-MM-DD`, `limit=1..100`, and `offset>=0`. The response uses **`chunks`**, plus `total`, `locations` (`label`, `chunk_count`), `uploads_by_day`, selected filters and table availability. Pages sort descending by upload timestamp; ties have no guaranteed ordering. All 414 cards had camera ID, location, capture type and upload timestamp when checked. A card contains its parent source, preview source, inline segment timeline/captions, stream metadata and counts. Do not expose playback authentication query strings.

All indexed uploads are dated **2026-10-01**; an upload-date filter for 2026-10-02 returned zero. Filename prefixes can reflect upload/chunk generation times, and a neighborhood filename embeds an older 2026-09-02 date. These are not proof of recording time. Display “latest indexed upload” separately from any confirmed capture time.

Cold parallel pagination took approximately 540–766 ms per page; warmed location-filter requests took about 25–28 ms. `GET /api/v1/tools/segments?original_video=<parent>` returned canonical camera/location metadata and local segment times. Tested Nashville, SF and warehouse detection sidecars each contained 150 frames. Those samples establish availability, not completeness for every archive segment.

The deployed API ignored `indexed=partial`: it returned the same 414 chunks and no `indexed` echo. Although the checked-out organizer source documents the parameter, do not advertise it as working until the deployed endpoint is verified to support it. All/mine/public each returned 414 accessible cards for the team account.

### Claim scope and independent evidence

For the general location chooser, analyze a selected parent chunk or an explicitly selected segment window. Tie the answer to that exact source and interval. Captions and YOLO sidecars are previous model outputs and should be labeled as such; an uncached visual analysis is a separate current inference.

Do not feed arbitrary location-wide chunks into the existing multi-camera jury. Consecutive chunks, frames, duplicate uploads and several views from different runs are correlated observations, not independent jurors. Different SF camera IDs do not by themselves establish synchronized capture. Warehouse ceiling/eye filenames do not establish matched time or run. The I-24 path currently has three identified viewpoints, so its existing eight-camera quorum remains unsatisfied for scene-wide claims. Preserve these safeguards; use bounded single-clip observations with clear uncertainty rather than invented multi-camera confidence.

The I-24 VSS indexing fallback now recognizes the deployed `chunks` response and filters actual segment metadata by the requested camera ID. It does not pull unrelated locations into a scene when parent metadata is missing.

### Catalog selector and clip-boundary recovery
The app now exposes All locations plus the six locations returned by the real VSS catalog. A selection fetches every catalog page, keeps the newest upload day for each selected location, and presents newest-first recorded MP4 playlists. Up to three players load video bytes at once. The assessment camera explicitly scopes the existing claim pipeline to that camera's indexed archive, independently of the current playback position. Unrelated locations and sequential chunks are never counted as independent jurors. Catalog scopes cannot reuse archived scene probes or baseline calibrated scene/jury verdicts; location verdicts use the actual upload metadata.

Detection sidecars are fetched with six concurrent requests, cached for five minutes, and bounded by a 12-second preparation budget. Missing or timed-out sidecars are reported as partial coverage. Metadata and existing indexed captions remain available; this is not an exhaustive fresh visual analysis of every frame. The catalog cache lasts 60 seconds; Refresh footage retrieves a new snapshot. Scope IDs are held in the running app process for up to 20 minutes, so refresh an open page after an app rollout or an expired selection.

The player explicitly reloads each MP4 at a clip boundary, ignores expected play cancellation, retries source failures twice, and clears a stale warning when actual video loads or plays. Persistent errors expose a functioning Retry video button. The proxy preserves byte ranges, returns video/mp4, and renews an expired VSS playback token once. No still-image or fake-video fallback is used.
