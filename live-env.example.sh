# Live settings used on the team-41 VM. Copy to live-env.sh (gitignored), fill in the endpoints, then:
#   . ./live-env.sh && ./run.sh live
# Endpoints: /config/<team>.config, or the GPU host in .cursor/skills/gpu/README.md; never commit real values (BUILD_DAY rules).
export PERJURY_MODE=live
export PERJURY_TEAM_CONFIG=/config/<team>.config
export COSMOS3_REASON_URL=http://<host:port>
export YOLO_URL=http://<host:port>
export COSMOS_EMBED1_URL=http://<host:port>
export CANARY_1B_URL=http://<host:port>
export IMAGEIO_FFMPEG_EXE=/usr/bin/ffmpeg
# Optional overrides. Unset, Cosmos asks the server (/v1/models -> nvidia/cosmos3-nano-reasoner) and the atomizer
# uses Nemotron 3.5 Lightning with thinking off (Qwen/Qwen3-30B-A3B-Instruct-2507 also works).
# export COSMOS3_REASON_MODEL=nvidia/cosmos3-nano-reasoner
# export PERJURY_ATOMIZER_MODEL=Qwen/Qwen3-30B-A3B-Instruct-2507
export COSMOS_EMBED1_MODEL=nvidia/cosmos-embed1
