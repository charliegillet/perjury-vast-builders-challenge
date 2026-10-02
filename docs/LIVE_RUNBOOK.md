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
