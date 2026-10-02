# Deploying PERJURY to /app

The team pod serves the same FastAPI app as the VM, at `http://video-lab-team-<N>.cosmos.vastdata.com/app`. This follows the starter `deploy-app-no-registry` skill: public `python:3.12-slim` image, code from ConfigMaps, credentials from a Secret, and Ingress path `/app` on the team host. Nothing is built or pushed.

## Run it (on the event VM)

```bash
deploy/deploy.sh fixture     # 10:00 skeleton: offline fakes, proves the deploy path (FIXTURE banner on screen)
deploy/deploy.sh             # live: real endpoints; needs cache/i24_index.json + cache/scene_probes.json
deploy/deploy.sh --dry-run   # manifests + ConfigMap size table only; writes deploy/out/ (gitignored)
```

Run it from the event VM. Only 2 people per team can use a VM, so one of those two deploys; nothing runs on a laptop.

- The script reads `/config/<team>.config`, which may be team-prefixed and must be the only `*.config` there.
- `KUBECONFIG` falls back to `/config/kubeconfig`, then to `/config/<team>-k8s.yaml` (files or symlinks).
- The namespace is `$USERNAME` and the host comes from `$INGRESS_URL`. Override them with `NS=` / `APP_NAME=` if needed.
- `WANDB_*` and the other keys are also taken from your shell environment when the config file lacks them.

## What it creates

| Object | Contents |
|---|---|
| `perjury-code-N` ConfigMaps | `perjury/*.py`, `perjury/*.yaml`, `app/*.py`, `app/static/*`, `requirements.txt`, and `deploy/pod_main.py` shipped as `main.py`. Keys are flattened (`perjury__pipeline.py`). |
| `perjury-cache-N` ConfigMaps | `cache/*.json`, `cache/*.npy`, `cache/replays/*.jsonl`. `fixture_*` files ship only in fixture mode. |
| `perjury-secrets` Secret | `VSS_URL/USERNAME/PASSWORD` (from `INGRESS_URL/USERNAME/PASSWORD`), `GPU_BEARER_TOKEN` (optional: the GPU endpoints need no auth token), model URLs and ids (`CANARY_1B_MODEL`, `COSMOS3_REASON_MODEL`, `COSMOS_EMBED1_MODEL` when set), `WANDB_*`, S3/VastDB keys, plus any `PERJURY_*` tuning variables set in your shell. Only the key names are printed. |
| Deployment `perjury` | One projected volume maps every ConfigMap key back to its repo path under `/seed`. At start the container copies `/seed/*` into a writable `/code` (emptyDir), runs `pip install -r requirements.txt` (1–3 min), then `python main.py` on `:8080`. A startup probe allows 6 min; readiness and liveness probes hit `/health`. |
| Service + Ingress | `/app(/|$)(.*)` → `/$2` on the team host. Proxy buffering is off for the SSE verdict stream, and the body limit is 16 MB for recorded testimony. |

Why it differs from the skill's single `--from-file` ConfigMap:
- `--from-file=<dir>` doesn't recurse, and one ConfigMap holds about 1 MiB. `build_manifests.py` bin-packs the files under 1,000,000 bytes per ConfigMap and fails loudly if a single file is too big.
- ConfigMaps are applied with `--server-side`. A client-side `kubectl apply` stores a `last-applied-configuration` annotation, which caps a ConfigMap at 256 KiB.
- `/code` is a writable copy, so `cache/runs/` (replay recordings), tiles and the Cosmos disk cache work in the pod. That state is lost on restart. Ship hero recordings through `cache/replays/` (see below).

## Update loop

| Change | Action |
|---|---|
| Code, UI, or any `cache/*.json` | `deploy/deploy.sh`. The pod template carries a hash of every shipped file, so changed content rolls the pod automatically (`Recreate`, ~2 min with pip). |
| Credentials | `deploy/deploy.sh`. The Secret is rebuilt every run. Then `kubectl -n $NS rollout restart deploy/perjury`, because a Secret change alone doesn't roll the pod. |
| Hero replays for the pod | Copy the chosen VM recordings: `cp cache/runs/<ts>_<slug>.jsonl cache/replays/`, then redeploy. They show up with a ★ in the Replay menu. |
| Logs | `kubectl -n $NS logs deploy/perjury --tail=100 -f` |
| Health | `curl -s http://$HOST/app/health`. Check that `mode`, `pod`, `index_segments`, `probes` and `pipeline` are true. |

## Checks after a deploy

```bash
curl -sS -o /dev/null -w "%{http_code}\n" http://$HOST/app/        # 200
curl -sS http://$HOST/app/health                                    # {"ok":true,"mode":"live","pod":"perjury-…",…}
curl -sS http://$HOST/app/api/scene/2 | head -c 300                 # scene meta + cameras
curl -sN -X POST http://$HOST/app/api/testify -H 'content-type: application/json' \
     -d '{"text":"Three pedestrians are crossing the highway in the snow.","scene":2}' | head -40   # SSE
```

The K8s ribbon chip lights only when the page was served by the pod (`/health` reports a pod name). From VM localhost it stays grey.

## Pitfalls

| Symptom | Fix |
|---|---|
| `/app` shows the VSS UI or a blank page | Open `/app/` with the trailing slash (the page also redirects itself). Check the rewrite annotation and that the path is `/app(/|$)(.*)`. |
| Pod stuck at `pip install` | The pod has no PyPI egress (gate G0). Serve live from the VM (`python -m app.main`, http://localhost:8080) and let /app serve fixture + replay only. |
| SSE arrives all at once | Ingress buffering. Check the `proxy-buffering: "off"` annotation. |
| `metadata.annotations: Too long` | Something applied a ConfigMap client-side. Use the script, which applies server-side. |
| `index not built yet` in the UI | Live mode needs `cache/i24_index.json` (from `perjury/index_i24.py`). Redeploy after building it. |
