# Live settings used on the team-41 VM. Copy to live-env.sh (gitignored), fill in the endpoints, then:
#   . ./live-env.sh && ./run.sh live
# Endpoints come from /config/<team>.config; never commit real values (BUILD_DAY rules).
export PERJURY_MODE=live
export PERJURY_TEAM_CONFIG=/config/<team>.config
export COSMOS3_REASON_URL=http://<host:port>
export YOLO_URL=http://<host:port>
export COSMOS_EMBED1_URL=http://<host:port>
export CANARY_1B_URL=http://<host:port>
export IMAGEIO_FFMPEG_EXE=/usr/bin/ffmpeg
export COSMOS3_REASON_MODEL=nvidia/cosmos3-nano-reasoner
export COSMOS_EMBED1_MODEL=nvidia/cosmos-embed1
export PERJURY_ATOMIZER_MODEL=Qwen/Qwen3-30B-A3B-Instruct-2507
