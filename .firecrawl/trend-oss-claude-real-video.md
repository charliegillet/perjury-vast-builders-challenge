[Skip to content](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) to refresh your session.Dismiss alert

{{ message }}

[HUANGCHIHHUNGLeo](https://github.com/HUANGCHIHHUNGLeo)/ **[claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video)** Public

- [Notifications](https://github.com/login?return_to=%2FHUANGCHIHHUNGLeo%2Fclaude-real-video) You must be signed in to change notification settings
- [Fork\\
195](https://github.com/login?return_to=%2FHUANGCHIHHUNGLeo%2Fclaude-real-video)
- [Star\\
2.2k](https://github.com/login?return_to=%2FHUANGCHIHHUNGLeo%2Fclaude-real-video)


master

[**2** Branches](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/branches) [**31** Tags](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tags)

[Go to Branches page](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/branches)[Go to Tags page](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tags)

Go to file

Code

Open more actions menu

## Latest commit

![HUANGCHIHHUNGLeo](https://avatars.githubusercontent.com/u/207666334?v=4&size=40)![claude](https://avatars.githubusercontent.com/u/81847?v=4&size=40)

[HUANGCHIHHUNGLeo](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commits?author=HUANGCHIHHUNGLeo)

and

[claude](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commits?author=claude)

[README: add 100-second demo (Can Claude watch a video?)](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/08309bbf4f7d5afe203755519ea0db17a9107466)

Open commit detailssuccess

12 hours agoOct 1, 2026

[08309bb](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/08309bbf4f7d5afe203755519ea0db17a9107466) · 12 hours agoOct 1, 2026

## History

[125 Commits](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commits/master/)

Open commit details

[View commit history for this file.](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commits/master/) 125 Commits

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| [.claude-plugin](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/.claude-plugin ".claude-plugin") | [.claude-plugin](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/.claude-plugin ".claude-plugin") | [0.7.16: batch-hardening from a 2,181-video field report + marketplace…](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/14570fcff652fd294398d364e3cfd5e2a7894dbb "0.7.16: batch-hardening from a 2,181-video field report + marketplace distribution  - dedup action channel: small-in-frame fast action survives (1/10 -> 10/10   action frames in synthetic repro); 32x32 strong-cell criterion alongside   the global % channel and the settled channel - decode all ffprobe/ffmpeg output with errors=replace (Latin-1 metadata   crashed runs) - --max-frames default scales with duration: clamp(150, s*1.5, 600) - --min-frame-interval alias for --fps-floor, honest seconds-per-frame help - Claude Code plugin marketplace structure (.claude-plugin/marketplace.json) - README: measured numbers (mode table + dedup before/after), marketplace   install instructions  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | 3 months agoJul 21, 2026 |
| [.github](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/.github ".github") | [.github](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/.github ".github") | [ci: publish to official MCP Registry via GitHub OIDC (manual dispatch…](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/cd47c472b9d27f204bb1c0e609b86601c117a628 "ci: publish to official MCP Registry via GitHub OIDC (manual dispatch + on release)") | 2 months agoAug 3, 2026 |
| [benchmark](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/benchmark "benchmark") | [benchmark](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/benchmark "benchmark") | [0.7.4: dedup gains a settled-local pass — small-area changes (ink str…](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/76d6f77bd10e7fda92a381167349081de9de29bf "0.7.4: dedup gains a settled-local pass — small-area changes (ink strokes, caption swaps, UI updates) are no longer invisible  Found by our own benchmark (included in benchmark/): the single downscaled- signature comparison measured thin handwriting strokes as a 0.0% change, so writing animations collapsed to blank+final frames and caption cards were dropped. The fix adds a second detection pass that looks for locally-settled new content at higher resolution, with shift-tolerant masking (film grain and sensor jitter do not trigger), a same-cell hard-contrast check, and a cooldown.  - benchmark/: reproducible methodology, per-video results, before/after tables - package metadata version fixed (reported 0.4.0 from a stale editable install) - --max-frames 0 no longer divides by zero - streaming signatures: memory stays flat on multi-hour videos  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | 3 months agoJul 10, 2026 |
| [capafy-staging/.claude/skills/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/capafy-staging/.claude/skills/claude-real-video "This path skips through empty directories") | [capafy-staging/.claude/skills/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/capafy-staging/.claude/skills/claude-real-video "This path skips through empty directories") | [skill: document --from/--to and --frame-width for the published Capaf…](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/48e1b7ce330c96e8f3239e19ac0c876d0f37f1f5 "skill: document --from/--to and --frame-width for the published Capafy skill  The skill file is what the buyer's agent reads, so it has to teach the two new flags and when they are worth using — a window for long recordings, a wider frame when the meaning is small on-screen text.") | 2 months agoAug 22, 2026 |
| [docs](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/docs "docs") | [docs](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/docs "docs") | [docs: add 60s real demo video block to README top](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/3fc1872dba1ba85ee534a3faa812231cef501e97 "docs: add 60s real demo video block to README top  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | 3 months agoJul 19, 2026 |
| [marketing](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/marketing "marketing") | [marketing](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/marketing "marketing") | [0.10.5: Apple Silicon GPU transcription via \[mlx\] extra (](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/e9bbf21779127549ae5448518f1eed97524698e7 "0.10.5: Apple Silicon GPU transcription via [mlx] extra (#28)  Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com> Claude-Session: https://claude.ai/code/session_01HqTvL9RNiU5ryN9ZhDZyAx") [#28](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/pull/28) [)](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/e9bbf21779127549ae5448518f1eed97524698e7 "0.10.5: Apple Silicon GPU transcription via [mlx] extra (#28)  Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com> Claude-Session: https://claude.ai/code/session_01HqTvL9RNiU5ryN9ZhDZyAx") | 3 weeks agoSep 11, 2026 |
| [personal-skill-backup](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/personal-skill-backup "personal-skill-backup") | [personal-skill-backup](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/personal-skill-backup "personal-skill-backup") | [0.10.1: window fixes — input-side -t (](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/827a596b4bf59dd2a31557403cbcd08e13a91292 "0.10.1: window fixes — input-side -t (#19/#21), caption clipping (#20/#23), anchor rebase (#20/#24), loud Pillow failure (#22)  Thanks @Jassu225 for the reports, the regression tests and three ready PRs. Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>") [#19](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/issues/19) [/](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/827a596b4bf59dd2a31557403cbcd08e13a91292 "0.10.1: window fixes — input-side -t (#19/#21), caption clipping (#20/#23), anchor rebase (#20/#24), loud Pillow failure (#22)  Thanks @Jassu225 for the reports, the regression tests and three ready PRs. Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>") [#21](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/pull/21) [), caption clipping (](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/827a596b4bf59dd2a31557403cbcd08e13a91292 "0.10.1: window fixes — input-side -t (#19/#21), caption clipping (#20/#23), anchor rebase (#20/#24), loud Pillow failure (#22)  Thanks @Jassu225 for the reports, the regression tests and three ready PRs. Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>") [#20](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/issues/20) [/](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/827a596b4bf59dd2a31557403cbcd08e13a91292 "0.10.1: window fixes — input-side -t (#19/#21), caption clipping (#20/#23), anchor rebase (#20/#24), loud Pillow failure (#22)  Thanks @Jassu225 for the reports, the regression tests and three ready PRs. Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>") [#…](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/pull/23) | 2 months agoAug 27, 2026 |
| [plugins/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/plugins/claude-real-video "This path skips through empty directories") | [plugins/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/plugins/claude-real-video "This path skips through empty directories") | [0.7.16: batch-hardening from a 2,181-video field report + marketplace…](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/14570fcff652fd294398d364e3cfd5e2a7894dbb "0.7.16: batch-hardening from a 2,181-video field report + marketplace distribution  - dedup action channel: small-in-frame fast action survives (1/10 -> 10/10   action frames in synthetic repro); 32x32 strong-cell criterion alongside   the global % channel and the settled channel - decode all ffprobe/ffmpeg output with errors=replace (Latin-1 metadata   crashed runs) - --max-frames default scales with duration: clamp(150, s*1.5, 600) - --min-frame-interval alias for --fps-floor, honest seconds-per-frame help - Claude Code plugin marketplace structure (.claude-plugin/marketplace.json) - README: measured numbers (mode table + dedup before/after), marketplace   install instructions  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | 3 months agoJul 21, 2026 |
| [skills](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/skills "skills") | [skills](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/skills "skills") | [Lite fused timeline: frames woven into the transcript on one clock](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/c2ba02367caf17ba9251c30bdc9586b3a19dd1cf "Lite fused timeline: frames woven into the transcript on one clock  New --- timeline --- MANIFEST section (timeline_lite.py): transcript segments become spans, silences >1.5s become frame-only spans, every kept frame is placed inside its span (nearest-span fallback so none are lost). Whisper phantom segments past the runtime are clamped. Emitted only when timestamped segments exist.") | 3 months agoJul 17, 2026 |
| [src/claude\_real\_video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/src/claude_real_video "This path skips through empty directories") | [src/claude\_real\_video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/src/claude_real_video "This path skips through empty directories") | [fix: a caption 429 no longer fails the whole download](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/67b06a0a070f4d778692952f4e48d34b22e077b1 "fix: a caption 429 no longer fails the whole download  crv asks the platform for its own captions before downloading, since they beat Whisper on speed and accuracy when they arrive. But platforms rate-limit caption endpoints far harder than media, and a 429 there aborted the entire run: the subtitle flags rode along on each cookie retry, so all three attempts failed identically and Whisper -- the documented fallback -- never received a file. The user saw a bare \"Download failed\", which points at the video rather than at the captions.  Both download paths now retry once without the caption request and rebind the base command so later attempts stop asking for captions too. A genuine error such as \"Video unavailable\" still fails on the first attempt, unmasked.  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>") | last weekSep 25, 2026 |
| [tests](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/tests "tests") | [tests](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/tree/master/tests "tests") | [fix: a caption 429 no longer fails the whole download](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/67b06a0a070f4d778692952f4e48d34b22e077b1 "fix: a caption 429 no longer fails the whole download  crv asks the platform for its own captions before downloading, since they beat Whisper on speed and accuracy when they arrive. But platforms rate-limit caption endpoints far harder than media, and a 429 there aborted the entire run: the subtitle flags rode along on each cookie retry, so all three attempts failed identically and Whisper -- the documented fallback -- never received a file. The user saw a bare \"Download failed\", which points at the video rather than at the captions.  Both download paths now retry once without the caption request and rebind the base command so later attempts stop asking for captions too. A genuine error such as \"Video unavailable\" still fails on the first attempt, unmasked.  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>") | last weekSep 25, 2026 |
| [.gitignore](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/.gitignore ".gitignore") | [.gitignore](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/.gitignore ".gitignore") | [mlx-whisper: review fixes](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/2a671645153548197f9b25f5d70f57cd89139c87 "mlx-whisper: review fixes  Review of the pre-gate found three ways it could be wrong rather than merely absent, plus a floor it did not declare.  SpeechTimestampsMap.get_original_time only grew is_end in faster-whisper 1.2.0, so on 1.1.x — which the extra's >=1.1.0 allowed — the restore raised TypeError outside any try. The [mlx] extra now asks for >=1.2.0, the gate checks the installed version and raises ImportError naming the real cause, and the whole restore is inside a try that returns GATE_ERROR.  The gate's one failure verdict conflated two very different events. Silero/ONNX throwing now yields VAD_FAILED -> GATE_ERROR, so a broken gate sends the file down the chain to a backend that gates itself instead of quietly transcribing it unguarded. Only a failed *decode* is VAD_UNREADABLE, which still lets mlx try: the wav is one ffmpeg just wrote, so an undecodable one is about to fail on every backend and refusing would cost a transcript without buying any safety.  Restored timestamps are now held to 0 <= start < end <= duration. Whisper's times can overshoot the window it was reading, and past a chunk seam that overshoot lands in the wrong place; out-of-order times get corrected, a segment restored entirely past the end is dropped, and losing every segment that way is GATE_ERROR rather than a terminal \"no speech\". Rounding happens once, at the 3dp transcript.json uses, on top of SpeechTimestampsMap's own 2dp step — the same two steps the faster-whisper path already takes, so both backends report alike.  Tests: timestamps restored across three chunks separated by long silences (including across a seam and clamped at the end), the bounds check on its own, a thrown VAD proving GATE_ERROR with mlx never called, and the whole chain showing faster-whisper still runs after mlx returns GATE_ERROR. The speech sample is now a committed fixture instead of a `say` call at test time.  Still: silence/tone/pink-noise -> no_signal in <1.1s, TED 21min in 61.3s with byte-identical output and no segment outside the audio.  Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com> Claude-Session: https://claude.ai/code/session_01HqTvL9RNiU5ryN9ZhDZyAx") | 3 weeks agoSep 11, 2026 |
| [.mcp.json](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/.mcp.json ".mcp.json") | [.mcp.json](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/.mcp.json ".mcp.json") | [Add .mcp.json (project MCP config; enables directory auto-detection)](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/51ba89573749ffa126d97ad58085f5b666ea3c22 "Add .mcp.json (project MCP config; enables directory auto-detection)") | 2 months agoAug 3, 2026 |
| [ATTRIBUTIONS.md](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/ATTRIBUTIONS.md "ATTRIBUTIONS.md") | [ATTRIBUTIONS.md](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/ATTRIBUTIONS.md "ATTRIBUTIONS.md") | [0.7.9: --speakers — local speaker diarization labels for the transcript](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/182885a572ab7eb4f7b115ea8e5ef2d2ea554fbb "0.7.9: --speakers — local speaker diarization labels for the transcript  - new optional extra [speakers]: sherpa-onnx pipeline (pyannote segmentation-3.0   onnx + 3D-Speaker ERes2Net embeddings), 45 MB models auto-download, no account   or token required - transcript.txt lines gain [SPEAKER_XX] prefixes; transcript.json segments gain   a speaker field; MANIFEST notes detected speaker count - speakers relabeled to first-appearance order; overlap-wins alignment against   whisper segments with nearest-turn fallback - fail-fast with install hint when the extra is missing; zero impact when unused - cluster threshold calibrated to 0.9 (upstream example default oversplits) - ATTRIBUTIONS.md added (engine and model licenses, all commercial-friendly)  Community-requested by u/clerveu.  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | 3 months agoJul 16, 2026 |
| [CHANGELOG.md](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/CHANGELOG.md "CHANGELOG.md") | [CHANGELOG.md](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/CHANGELOG.md "CHANGELOG.md") | [0.10.7: a caption 429 no longer fails the whole download (](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/0b4149d5c68fe3a5d6b01d6601c322378e703a89 "0.10.7: a caption 429 no longer fails the whole download (#29 by @Kikobazz123)") [#29](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/pull/29) [by](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/0b4149d5c68fe3a5d6b01d6601c322378e703a89 "0.10.7: a caption 429 no longer fails the whole download (#29 by @Kikobazz123)") [@Kik…](https://github.com/Kikobazz123) | last weekSep 26, 2026 |
| [CONTRIBUTING.md](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/CONTRIBUTING.md "CONTRIBUTING.md") | [CONTRIBUTING.md](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/CONTRIBUTING.md "CONTRIBUTING.md") | [docs: add CONTRIBUTING, SECURITY, and issue templates](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/a4495d7cefbb3f53ccdcfa834374c540a4afc4f7 "docs: add CONTRIBUTING, SECURITY, and issue templates  Best-effort response time (one-person project), security reports via email, supported versions = latest minor.  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | 3 months agoJul 10, 2026 |
| [LICENSE](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/LICENSE "LICENSE") | [LICENSE](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/LICENSE "LICENSE") | [claude-real-video v0.1.0: let any LLM actually watch a video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/449ee8c0a6cbdf09e1468947d7bf6615912c01f4 "claude-real-video v0.1.0: let any LLM actually watch a video  URL (yt-dlp) or local file -> scene-change frame extraction + density floor + average-hash dedup + optional Whisper transcript -> a manifest an LLM can read. Beats fixed-quota extractors: URL ingestion, scene-aware sampling, dedup (static slide collapses to 1 frame). pip-installable CLI (crv) + Python API.  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>") | 4 months agoJun 29, 2026 |
| [README.md](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/README.md "README.md") | [README.md](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/README.md "README.md") | [README: add 100-second demo (Can Claude watch a video?)](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/08309bbf4f7d5afe203755519ea0db17a9107466 "README: add 100-second demo (Can Claude watch a video?)  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>") | 12 hours agoOct 1, 2026 |
| [SECURITY.md](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/SECURITY.md "SECURITY.md") | [SECURITY.md](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/SECURITY.md "SECURITY.md") | [docs: add CONTRIBUTING, SECURITY, and issue templates](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/a4495d7cefbb3f53ccdcfa834374c540a4afc4f7 "docs: add CONTRIBUTING, SECURITY, and issue templates  Best-effort response time (one-person project), security reports via email, supported versions = latest minor.  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | 3 months agoJul 10, 2026 |
| [install-skill.sh](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/install-skill.sh "install-skill.sh") | [install-skill.sh](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/install-skill.sh "install-skill.sh") | [fix: arithmetic increment safe with set -e](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/3def733e89f2465a3aedc0c6f96de15f48632cbb "fix: arithmetic increment safe with set -e") | 3 months agoJul 7, 2026 |
| [pyproject.toml](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/pyproject.toml "pyproject.toml") | [pyproject.toml](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/pyproject.toml "pyproject.toml") | [0.10.7: a caption 429 no longer fails the whole download (](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/0b4149d5c68fe3a5d6b01d6601c322378e703a89 "0.10.7: a caption 429 no longer fails the whole download (#29 by @Kikobazz123)") [#29](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/pull/29) [by](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/0b4149d5c68fe3a5d6b01d6601c322378e703a89 "0.10.7: a caption 429 no longer fails the whole download (#29 by @Kikobazz123)") [@Kik…](https://github.com/Kikobazz123) | last weekSep 26, 2026 |
| [server.json](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/server.json "server.json") | [server.json](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/server.json "server.json") | [0.10.5: Apple Silicon GPU transcription via \[mlx\] extra (](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/e9bbf21779127549ae5448518f1eed97524698e7 "0.10.5: Apple Silicon GPU transcription via [mlx] extra (#28)  Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com> Claude-Session: https://claude.ai/code/session_01HqTvL9RNiU5ryN9ZhDZyAx") [#28](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/pull/28) [)](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/commit/e9bbf21779127549ae5448518f1eed97524698e7 "0.10.5: Apple Silicon GPU transcription via [mlx] extra (#28)  Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com> Claude-Session: https://claude.ai/code/session_01HqTvL9RNiU5ryN9ZhDZyAx") | 3 weeks agoSep 11, 2026 |
| View all files |

## Repository files navigation

# claude-real-video

[Permalink: claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#claude-real-video)

[![PyPI](https://camo.githubusercontent.com/acc5aad7726b5732f81f156c8a616098f30d28bacf9878aa972ebcc0d548b318/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f636c617564652d7265616c2d766964656f)](https://pypi.org/project/claude-real-video/)[![Python 3.10+](https://camo.githubusercontent.com/e801a66299d2c15286fe0fee660d9ffa666c1c5576e5e1536acc07b49ce8ac8f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31302532422d626c7565)](https://pypi.org/project/claude-real-video/)[![License: MIT](https://camo.githubusercontent.com/f8df3091bbe1149f398a5369b2c39e896766f9f6efba3477c63e9b4aa940ef14/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d677265656e)](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/blob/master/LICENSE)[![HN front page](https://camo.githubusercontent.com/e0113aa86047235def7d6cc711696da0bcad608786ab52bfb42fe2856db6d88c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4861636b65722532304e6577732d66726f6e74253230706167652d6f72616e6765)](https://news.ycombinator.com/item?id=48766005)

[![Can Claude watch a video? Same question to ChatGPT, Gemini and Claude](https://camo.githubusercontent.com/f5e82e9f2f49ea19c4071669c231b619ac7c9a2bbf0fefb30fa3444b3d3a23f6/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f51527568316f427954334d2f687164656661756c742e6a7067)](https://youtu.be/QRuh1oByT3M)

**▶ [100-second demo](https://youtu.be/QRuh1oByT3M):** ChatGPT and Gemini can watch video, Claude can't. Here's what Claude answers once crv turns the video into frames plus a timestamped transcript.

[![LLM Real Video — Give Your LLM Eyes (60-second film)](https://camo.githubusercontent.com/752401357e79b196e6ee4796e37ee07a0dc8afccbc678dcd05a195d24ec1b653/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f7377365f38452d353777342f6d617872657364656661756c742e6a7067)](https://youtu.be/sw6_8E-57w4)

**▶ [The 60-second pixel film — sound on](https://youtu.be/sw6_8E-57w4)** ( [mp4 on GitHub](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/releases/download/v0.7.16/crv-999-film-60s.mp4)) · an AI agent searches "how can an LLM truly understand video?", finds a key, and unlocks vision.

[![crv 60s demo](https://raw.githubusercontent.com/HUANGCHIHHUNGLeo/claude-real-video/master/docs/crv-demo-poster.jpg)](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/releases/download/v0.7.15/crv-demo-60s.mp4)

60-second real demo — real install, real run, real viewer.

**Let Claude — or any LLM — actually watch a video.**

```
pip install "claude-real-video[whisper]"
npx skills add HUANGCHIHHUNGLeo/claude-real-video   # one command, installs the skill into Claude Code, Cursor, Codex, Copilot, Gemini CLI & 50+ agent hosts
```

Claude Code plugin marketplace (enable auto-update in /plugin → Marketplaces if you want it):

```
/plugin marketplace add HUANGCHIHHUNGLeo/claude-real-video
/plugin install claude-real-video@claude-real-video
```

Then paste a video link into your agent and ask about it. (CLI-only use? `crv "<url>"` works with just the pip install.)

> **Naming:** crv is the short name for claude-real-video (the PyPI package). The paid add-on, **crv Pro**, is sold on Capafy under the listing name "llm-real-video Pro".

![demo](https://raw.githubusercontent.com/HUANGCHIHHUNGLeo/claude-real-video/master/docs/demo.gif)![demo](https://raw.githubusercontent.com/HUANGCHIHHUNGLeo/claude-real-video/master/docs/demo.gif)[Open demo in new window](https://raw.githubusercontent.com/HUANGCHIHHUNGLeo/claude-real-video/master/docs/demo.gif)

> ▶ **New: the 40-second film** — [_my AI agent learned to watch videos (and stopped working)_](https://youtu.be/xFqPtcju_xo)

> Same 58-second clip: fixed 1 fps sampling = **58 frames**. crv keeps the **26 that actually differ** — and `--grid` packs them into **3 contact sheets**. Fewer tokens, nothing missed.

> **This free version lets your AI _see_ the video.** [crv Pro](https://leoaido.com/crv-pro/) lets it _understand_ it — how it was shot (cut rhythm, camera moves) plus a timestamped timeline of what frames can't show: gestures, expressions, voice pitch shifts, emotion, sound events. One-time price $29 — [get it on Capafy](https://capafy.ai/agent/llm-real-video-pro-let-any-llm-watch-videos/5451082151) or [buy with card via Lemon Squeezy](https://leoaido.lemonsqueezy.com/checkout/buy/ff552000-adc0-49f1-8eec-5e8ada1905a1).

> **On Codex CLI?** [Real Video for Codex](https://capafy.ai/agent/real-video-for-codex/3594524971) is a self-contained build for it. You ask Codex about a video, it runs one command, then reads a `SUMMARY.md` with chapters, a timecoded transcript and **the text that was on screen**, which this free edition leaves out. So it can quote the config block on the slide at 12:40, not only what the speaker said about it, and it answers you in `hh:mm:ss`. Download, frames, transcription and text recognition all run on your machine, and the tool itself needs no API key and no account. Ships with the Codex skill and a `crv-easy doctor` self-check. Python 3.10 to 3.14, macOS or Windows 11 native. One-time $9.90: [get it on Capafy](https://capafy.ai/agent/real-video-for-codex/3594524971) or [buy with card via Lemon Squeezy](https://leoaido.lemonsqueezy.com/buy/cbbead56-5838-43fd-a00c-62b53b0de13e?checkout%5Bcustom%5D%5Bref%5D=github-readme).

Most AI tools don't really _see_ a video. Paste a YouTube link into ChatGPT and it
reads the **transcript**, not the picture. Claude won't take a video file at all.
Even Gemini, which _can_ read video natively, has to send it up to Google and
samples frames at a **fixed interval** (1 fps by default), so fast cuts slip past.

`claude-real-video` does it differently, and **the processing runs locally**: point it at a URL or a
file, and it pulls the frames that _actually matter_ (every scene change, not a
fixed quota), throws away the near-duplicates, transcribes the audio, and hands
you a clean folder any LLM can read. All the processing happens on your own machine — what gets sent anywhere is only the frames/text _you_ choose to paste into an LLM afterwards.

```
crv "https://www.youtube.com/watch?v=..."
# → crv-out/frames/*.jpg  +  frames.json (per-frame timestamps)  +  transcript.txt/.json  +  MANIFEST.txt
```

Then drop the frames + `MANIFEST.txt` into Claude / ChatGPT / Gemini and ask away.

**No terminal needed** — run `crv-web` and a local page opens (Traditional Chinese / Simplified Chinese / English): paste a YouTube or Reels link or a file path, click Analyze, open the result viewer. Video analysis and output generation run on your machine — the source video never gets uploaded. (If you then paste the extracted frames or transcript into a cloud LLM, that data goes to that provider.)

Want to eyeball what the model will see first? Add `--viewer` — it writes a local `viewer.html` (video + keyframe grid + transcript) you can double-click open. No network, no extra installs.

**Only part of a video matters** (a 10-minute screen share inside a 90-minute call): `--from 28:00 --to 43:00`. ffmpeg seeks instead of decoding the whole file, Whisper only hears the window, and the frame budget is spent inside it — but every timestamp crv reports is still a source timecode you can quote to a colleague.

**The meaning is small text** (a terminal, a spreadsheet, an IDE): `--frame-width 1600`. Frame _selection_ is the hard part and crv already does it; at 640px on a 1920-wide screen recording the right moment gets found and then the detail that made it worth finding is thrown away.

**Slow-changing content** (animation tutorials, gradual morphs, slow pans): add `--adaptive` — frames are picked against their rolling neighbourhood instead of a fixed threshold, so a 2-3s squash-and-stretch that never spikes any single frame still gets captured.

**Text-heavy content** (lecture slides, screen recordings, talking-head explainers): add `--text-anchors` — extra frames are forced at subtitle-cue timestamps, so each spoken segment gets a matching visual even when the scene barely changes. Needs a sidecar `.srt`/`.vtt` or an embedded subtitle track — captions burned into the pixels can't be detected. At most one forced frame per second; scene detection is untouched.

**Multi-speaker content** (interviews, podcasts, meetings): add `--speakers` — every transcript line gets a speaker label (`[SPEAKER_00]`, `[SPEAKER_01]`, …) so the model can follow who said what. Runs a local diarization model (45 MB, downloads once, no account or token needed). Install with `pip install "claude-real-video[speakers]"`.

Not doing LLM work? It also works as a **general-purpose video keyframe extractor** —
scene-change detection + dedup, no ML models to download.

**Using Claude Code — or any coding agent?** One command installs the skill
(works with Claude Code, Cursor, Codex, Copilot, Gemini CLI and other
[agentskills.io](https://agentskills.io/)-compatible hosts):

```
pip install "claude-real-video[whisper]"
npx skills add HUANGCHIHHUNGLeo/claude-real-video
```

Then just paste a video link into your agent and ask about it.

Manual install (clone + copy)

```
git clone https://github.com/HUANGCHIHHUNGLeo/claude-real-video.git
mkdir -p ~/.claude/skills && cp -r claude-real-video/skills/claude-real-video ~/.claude/skills/
```

**Tell it _why_ you're watching, and keep what it finds:**

```
crv "https://youtu.be/..." --why "find the pricing strategy" --kb ~/notes
```

`--why` makes the analysis focus on what you care about instead of a generic summary;
`--kb` saves the result as a dated note in your own notes folder, so it doesn't die in `crv-out`.

**New in 0.10.x** — analyse only the part that matters:

```
crv long-meeting.mp4 --from 28:00 --to 43:00
```

`--from` / `--to` cut a window out of a long video: ffmpeg seeks instead of decoding
the whole file, the transcript and frame budget follow the window, and every reported
timestamp is still a source timecode you can quote back to the original.

* * *

## Measured numbers

[Permalink: Measured numbers](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#measured-numbers)

Real run on a 3-minute 640x360 video (benchmark/jfk-rice.mp4), Mac mini M4, local CPU, frames + dedup only (`--no-transcribe`). Image tokens estimated with Anthropic's `(width x height) / 750` — 307 tokens/frame at 640x360.

| Mode | Frames kept | Wall time | Est. image tokens |
| --- | --- | --- | --- |
| default (scene-change + 1s floor) | 170 (from 180 extracted) | 23.5 s | ~52k |
| `--max-frames 80` | 80 | 23.4 s | ~25k |
| `--adaptive` (catches slow morphs) | 270 | 36.8 s | ~83k |

**Dedup v0.7.16 — small-subject fast action no longer disappears.** A percentage comparator is structurally blind to a subject that covers <1% of the frame (it can never change 8% of the pixels). Found in a user's 2,181-video batch run; fixed with a third "action channel". Synthetic repro — static 1280x720 shot, a 40x90 px subject (0.4% of frame) moves fast only in the last 10 of 65 frames:

|  | Frames kept | Action frames survived |
| --- | --- | --- |
| v0.7.15 | 2 | 1 / 10 |
| v0.7.16 | 11 | **10 / 10** — full trajectory |

## Why not just sample frames?

[Permalink: Why not just sample frames?](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#why-not-just-sample-frames)

Most "let an LLM watch a video" scripts (and Gemini's own pipeline) grab frames
at a **fixed interval** — e.g. one per second. That over-samples a static
screencast and under-samples a fast-cut reel. `claude-real-video` is smarter:

|  | fixed-interval sampling | **claude-real-video** |
| --- | --- | --- |
| Frame selection | every N seconds | **scene-change detection** \+ density floor |
| Repeated shots (A-B-A cuts) | sent again every time | **sliding-window dedup** sends each shot once |
| Static slide (10 min) | ~600 near-identical frames | **collapses to 1** (dedup) |
| Fast-cut reel | misses frames between samples | catches each visual change |
| Audio | often ignored | Whisper transcript w/ language detect |
| Where the processing happens | often in someone's cloud | **on your machine** (you choose what to share with an LLM afterwards) |
| Input | usually local file only | **URL (yt-dlp) or local file** |

You feed the model _fewer, more meaningful_ frames — cheaper context, better
understanding.

* * *

## Install

[Permalink: Install](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#install)

```
pip install "claude-real-video[whisper]"   # recommended: frames + dedup + audio transcription
pip install claude-real-video              # core only (frames + dedup)
```

pip extras never install themselves — without `[whisper]` there is **no speech-to-text**
(videos that ship their own subtitles still get a transcript).

### System requirement: ffmpeg

[Permalink: System requirement: ffmpeg](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#system-requirement-ffmpeg)

`ffmpeg` / `ffprobe` are used for frame extraction and audio, and aren't
pip-installable. Install them once:

| OS | command |
| --- | --- |
| **macOS** | `brew install ffmpeg` |
| **Linux** | `sudo apt install ffmpeg` (or your distro's package manager) |
| **Windows** | `winget install Gyan.FFmpeg` — or `choco install ffmpeg` — or [download a build](https://www.gyan.dev/ffmpeg/builds/) and add its `bin\` folder to your `PATH` |

Verify it's on your `PATH`:

```
ffmpeg -version
```

Transcription uses the `whisper` CLI (installed by the `[whisper]` extra, or
`pip install openai-whisper`). Whisper also relies on ffmpeg.

**Faster + hallucination-proof transcripts (recommended):** install the `[fast]`
extra and crv automatically switches to
[faster-whisper](https://github.com/SYSTRAN/faster-whisper) — same models, same
output files, several times faster, and gated by Silero VAD (voice-activity
detection): music-only or silent audio yields an honest "no speech" note instead
of whisper's classic invented caption. No new flags to learn:

```
pip install 'claude-real-video[fast]'
```

If both are installed, faster-whisper wins; if it ever fails, crv falls back
to the `whisper` CLI on its own.

**Apple Silicon (M1–M4): GPU transcription.** Install the `[mlx]` extra and crv
runs Whisper on the Mac's GPU through
[mlx-whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper) —
a 21-minute talk that takes ~6 minutes on faster-whisper finishes in about a
minute on an M4, with the same transcript. The Silero VAD gate still runs
first, so music or silence never turns into invented captions; if the gate or
mlx cannot run, crv drops back to faster-whisper, then the CLI. Contributed by
[@blazejp83](https://github.com/blazejp83) (#28).

```
pip install 'claude-real-video[mlx]'
```

Works on **macOS, Windows, and Linux** — Python 3.10+.

* * *

## Usage

[Permalink: Usage](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#usage)

```
# A YouTube / Instagram / TikTok / ... link
crv "https://www.instagram.com/reel/XXXX/"

# A local file, English transcript, output to ./out
crv lecture.mp4 -o out --lang en

# Frames only, no transcription
crv clip.mp4 --no-transcribe

# A login-gated video (your own / authorised use): pass a Netscape cookie file
crv "https://..." --cookies cookies.txt
```

`python -m claude_real_video ...` works as an alias for `crv` too.

### Options

[Permalink: Options](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#options)

| flag | default | meaning |
| --- | --- | --- |
| `-o, --out` | `crv-out` | output directory |
| `--overwrite` | off | replace a previous analysis living in the output directory (without this, a non-empty output dir is refused to avoid mixing videos) |
| `--scene` | `0.30` | scene-change sensitivity (lower = more frames) |
| `--fps-floor` | `1.0` | at least one frame every N seconds |
| `--from` / `--to` | whole file | analyse only part of a video (`90`, `1:30`, `0:01:30.5`). Reported timestamps stay **source** timecodes — a window shifts the analysis, not the clock — and the frame budget plus the transcript follow the window instead of the whole file |
| `--frame-width` | `640` | width of extracted frames, aspect kept. Raise it when the meaning _is_ small text (terminals, spreadsheets, dense dashboards); larger frames multiply output size and model cost |
| `--max-frames` | auto: `clamp(150, window×1.5, 600)` | hard cap on total frames (explicit value always wins) |
| `--adaptive` | off | adaptive scene detection: catches slow morphs (2-3s squash/stretch, gradual pans) a fixed threshold misses, by comparing each frame against its rolling neighbourhood |
| `--text-anchors` | off | force extra frames at subtitle-cue timestamps (sidecar `.srt`/`.vtt` or embedded track) — for videos where meaning changes faster than pixels; at most one forced frame per second |
| `--speakers` | off | label every transcript line with the speaker (`[SPEAKER_00]` …) via local diarization — needs `pip install "claude-real-video[speakers]"`, 45 MB model downloads once |
| `--lang` | `auto` | Whisper language (`en`, `zh`, `auto`, ...) |
| `--whisper-model` | `base` | Whisper model for transcription (`tiny`/`base`/`small`/`medium`/`large`/`turbo` — base is fast; **want sharper transcripts? `--whisper-model turbo` is one flag away**: a pruned large-v3 — much faster than `large` with a minor quality trade-off, one-time 1.6GB download, ~6GB memory) |
| `--dedup-threshold` | `8` | % of pixels that must change for a frame to count as new; higher = fewer frames (the settled-local detector's gate scales with it too) |
| `--dedup-window` | `4` | compare against the last N kept frames — a shot the model already saw doesn't come back after a cutaway (`1` = consecutive-only) |
| `--report` | off | keep dropped frames in `./dropped` \+ write `report.html` visualising every keep/drop decision |
| `--no-transcribe` | off | skip audio |
| `--keep-audio` | off | also save the **full soundtrack** (`audio.m4a`) so audio models can _hear_ it |
| `--viewer` | off | also write `viewer.html` — browse the video, keyframes and transcript in one local page (double-click to open) |
| `--grid` | off | also tile the kept frames into 3x3 contact sheets (`./grids`) — consecutive frames side by side help the model follow motion and progression |
| `--why` | – | why you're watching, e.g. `--why "find the pricing strategy"` — written into `MANIFEST.txt` so the model analyses with that lens instead of a generic summary |
| `--kb` | – | also save the analysis as a dated markdown note into this folder (your Obsidian vault, notes dir, ...) — so it joins your knowledge base instead of dying in `crv-out` |
| `--cookies` | – | Netscape cookie file for login-gated sources |
| `--cookies-from-browser` | – | read login cookies straight from your own browser — `chrome`, `safari`, `firefox` or `edge` (your own account only) |

* * *

### What `--grid` output looks like

[Permalink: What --grid output looks like](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#what---grid-output-looks-like)

One contact sheet = nine consecutive keyframes, in order, filenames on each cell — the model reads a sequence, not scattered stills:

![contact sheet example](https://raw.githubusercontent.com/HUANGCHIHHUNGLeo/claude-real-video/master/docs/grid_example.jpg)

## Memory — ask across everything you've watched

[Permalink: Memory — ask across everything you've watched](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#memory--ask-across-everything-youve-watched)

Every analysis is indexed locally (transcript lines + on-screen text, with timestamps),
so a question can span your whole library instead of one output folder:

```
crv-ask "pricing strategy"   # → which video, which second, the exact line
crv-ask 定價                  # CJK works — trigram FTS with a substring fallback
crv-ask --list               # everything you've watched, newest first
crv-ask --stats              # where the index lives, how big it is
crv-ask --prune 200          # keep the newest 200 videos, reclaim the space
```

Re-running the same source with the same options doesn't re-process — crv says
"already watched" and points at the existing analysis (0.04s vs several seconds
measured). Different options, or `--overwrite`, re-analyse as usual.

Everything stays local: one SQLite file at `~/.crv/memory.db` (override with
`CRV_MEMORY_DB`), user-only permissions, no embeddings, no network. The first time
anything is indexed, crv prints one line saying so. Don't want it at all?
`CRV_NO_MEMORY=1`.

## MCP server (Claude Desktop / Cursor / any MCP client)

[Permalink: MCP server (Claude Desktop / Cursor / any MCP client)](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#mcp-server-claude-desktop--cursor--any-mcp-client)

crv also ships as an MCP server, so MCP clients can ask for a video to be
watched directly — same local pipeline, zero cloud. Five tools: `watch_video`,
`get_frames`, `search_memory` (ask across every watched video), `list_watched`
(check before re-watching), and `get_transcript` (words only — no frames, so a
long talk doesn't cost image tokens).

```
pip install 'claude-real-video[mcp]'
```

Claude Code:

```
claude mcp add crv -- crv-mcp
```

Claude Desktop — add to `claude_desktop_config.json`:

```
{ "mcpServers": { "crv": { "command": "crv-mcp" } } }
```

Tools: `watch_video(source, max_frames, language, transcribe)` returns the
timestamped transcript plus the first batch of keyframes as images;
`get_frames(source, start_index, count)` pages through the rest. Analyses are
cached under `~/.cache/crv-mcp`, so follow-up questions about the same video
are instant.

mcp-name: io.github.HUANGCHIHHUNGLeo/claude-real-video

Verified end-to-end on Claude Code (the model described a test video's frames
correctly through the tool). Claude Desktop and Cursor speak the same MCP
stdio protocol — config above; open an issue if anything misbehaves.

## Use it from Python

[Permalink: Use it from Python](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#use-it-from-python)

```
from claude_real_video import process

r = process("https://youtu.be/...", "out", lang="en")
print(r.frame_count, r.transcript_path)
```

* * *

## How it works

[Permalink: How it works](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#how-it-works)

1. **Fetch** — `yt-dlp` for URLs (optional cookies), or copy a local file.
2. **Extract** — one chronological `ffmpeg select` pass grabs every scene change
_plus_ a density floor (at least one frame every `--fps-floor` seconds), so
fast cuts and slow screencasts are both covered.
3. **Dedup** — three channels against a **sliding window** of the last
`--dedup-window` kept frames, so an A-B-A cutaway doesn't re-send a shot the
model has already seen. A _global_ channel measures real pixel difference
(downscaled RGB, not a perceptual hash — hashes go blind on flat colours and
equal-luma hue changes); `--dedup-threshold` is the % of it that must change.
A _settled-local_ channel (v0.7.4) catches what the global one can't see:
thin pen strokes, caption/text-card swaps and small UI updates that average
out to ~0% globally. It looks, on a finer signature, for a region that
differs strongly from every recent kept frame (with 1px shift tolerance, so
film grain and frame jitter don't trigger) _and_ is no longer changing — a
settled new state, not motion mid-flight — with a cooldown so continuous
motion that pauses every second (a waving flag, drifting smoke) can't keep
re-firing. The final frame is evaluated even if still in motion (so a video's closing state is never lost), but it must clear both contrast gates like any other frame. `--report` writes `report.html` showing every keep/drop decision
with its diff % (settled-local keeps are labelled), for tuning.
4. **Text** — if the video **already has subtitles** (a sidecar `.srt`/`.vtt` next to a
local file, or an embedded subtitle track), those are used as the transcript —
faster and more accurate than re-transcribing. Only when there are no subtitles
does it fall back to **Whisper** on the audio (skipped cleanly if there's no audio).
5. **Audio** _(optional, `--keep-audio`)_ — save the **full original soundtrack**
(`audio.m4a`: music + speech + effects, copied losslessly when possible). The
transcript only has the _words_; the audio file lets a model that can listen
(Gemini, GPT-4o, …) actually _hear_ the music and tone.
6. **Timestamps** — every kept frame's source-video time survives the whole
pipeline (extraction → dedup → `--max-frames` thinning → renaming) and is
written to `frames.json` (`file` / `timestamp_sec` / `timestamp` /
`selection_reason`). Cite visual evidence as `frame_012 @ 00:03:41`, align
frames with `transcript.json` segments, or feed the map to a video-RAG
pipeline. In `viewer.html`, click any keyframe → "play video from here".
7. **Manifest** — `MANIFEST.txt` summarises everything for the model.

So the model can **see** (key frames), **read** (transcript) and — with `--keep-audio` —
**hear** (full soundtrack) the video. The transcript is plain text any model can read;
the tool **doesn't burn subtitles into the video** — burning is a presentation choice,
not something needed to make a video AI-readable.

* * *

## Notes

[Permalink: Notes](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#notes)

- Only download content you have the right to. The `--cookies` option is for
your own, authorised access — don't ship credentials in a repo.
- Use one output folder per video. Re-running into a folder that already holds
an analysis is refused (so two videos never mix); pass `--overwrite` to replace it.

## crv Pro — understand _how_ a video was shot

[Permalink: crv Pro — understand how a video was shot](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#crv-pro--understand-how-a-video-was-shot)

The free tool gives your AI keyframes and a transcript — enough to know **what** a video is about. **crv Pro adds everything else: how it's shot, how it's cut, how it's spoken, what it feels like.** All computed on your machine, written as plain text any LLM can read.

- **Camera & pacing (`--motion`)** — every shot auto-labelled: static, pan, tilt, zoom, handheld. Full shot table: per-shot duration, cuts per minute, pacing across open/middle/close. High-motion shots get 0.2s-apart burst frames.
- **Sound & emotion (`--senses`)** — voice emotion, tone curves and audio events (laughter, SFX, ambience) timestamped segment by segment. Vocals and music auto-separated: emotion reads the clean voice, music gets its own BPM + energy track. No-dialogue footage (MVs, film) falls back to reading mood from color and light.
- **Interactive viewer (`--viewer`)** — one self-contained web page per analysis: the video, a clickable event timeline that jumps to the second, a transcript that highlights along with playback. EN / 繁中 / 简中.
- **Two reports, one flag (`--ai-report`)** — with your own API key: one report on how it's shot, one on what it says.
- **Breakdown report (`--breakdown`)** — hook analysis, pacing curve, camera language, and a rubric your own LLM completes into a full teardown.
- **Memory across your library (`crv-pro-ask`)** — search everything Pro has watched by what the camera and the voice did: `--camera zoom` (every zoom you've ever watched), `--track emotion --label angry`, `--rhythm` (cuts/min ranked). The free `crv-ask` searches words; these search measurements the free edition never takes.

One-time price **$29**:

- **Buy on Capafy** (instant download, license key included): [https://capafy.ai/agent/llm-real-video-pro-let-any-llm-watch-videos/5451082151](https://capafy.ai/agent/llm-real-video-pro-let-any-llm-watch-videos/5451082151)
- **Buy with credit card** (Lemon Squeezy checkout, instant download): [https://leoaido.lemonsqueezy.com/checkout/buy/ff552000-adc0-49f1-8eec-5e8ada1905a1](https://leoaido.lemonsqueezy.com/checkout/buy/ff552000-adc0-49f1-8eec-5e8ada1905a1)
- Product page & demo: [https://leoaido.com/crv-pro/](https://leoaido.com/crv-pro/)

* * *

**Following the build?** I'm documenting the road from open-source tool to first paying customer, in public — [@LeoAidoAI on X](https://x.com/LeoAidoAI).

## FAQ

[Permalink: FAQ](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#faq)

### What is the best tool to let an LLM watch or analyze a video?

[Permalink: What is the best tool to let an LLM watch or analyze a video?](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#what-is-the-best-tool-to-let-an-llm-watch-or-analyze-a-video)

It depends on what "watch" means for you. If you just want one answer about one clip and don't mind uploading it, a hosted multimodal model (e.g. Gemini) is the shortest path. If you want **any** LLM — Claude, GPT, Gemini or a local model — to analyze video **reproducibly and locally**, you want a preprocessing pipeline: scene-aware keyframes + a timestamped transcript, handed to the model as evidence it can cite. That pipeline is exactly what `claude-real-video` does, in one command, with nothing leaving your machine. Uniform frame sampling (1 fps) either misses cuts or floods the context window; scene-aware extraction keeps the frames that carry information.

### How can I make Claude understand a video?

[Permalink: How can I make Claude understand a video?](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#how-can-i-make-claude-understand-a-video)

Claude cannot ingest video files directly. The working approach:

```
pip install "claude-real-video[fast]"
npx skills add HUANGCHIHHUNGLeo/claude-real-video   # or install via the Claude Code plugin marketplace
```

Then in Claude Code: `Analyze this video: /path/to/video.mp4`. The skill extracts scene-aware keyframes, a timestamped transcript (`transcript.json`), a frame→timestamp map (`frames.json`) and a `MANIFEST.txt` that tells the model how to read the folder — so Claude can cite `frame_012 @ 00:03:41` instead of guessing.

### What is claude-real-video?

[Permalink: What is claude-real-video?](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#what-is-claude-real-video)

An MIT-licensed Python CLI (`crv`) that turns a video into what an LLM can actually read: scene-aware keyframes (with real source timestamps that survive dedup and renaming), sliding-window deduplication so small-subject motion isn't thrown away, and local Whisper transcription with optional speaker labels. Works with YouTube URLs or local files, runs 100% locally. It exists because subtitles alone are not watching — models that only read the transcript hallucinate everything visual.

## Who makes this

[Permalink: Who makes this](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#who-makes-this)

Built by Leo Huang — a one-person company running on AI.
I post what actually breaks and what works while building tools like this:
[https://x.com/LeoAidoAI](https://x.com/LeoAidoAI)

## License

[Permalink: License](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#license)

MIT

## About

Let Claude (or any LLM) actually watch a video — scene-aware, deduplicated frames + transcript, from a URL or local file. Runs locally, MIT.

[leoaido.com/crv-pro/](https://leoaido.com/crv-pro/)

### Topics

[claude](https://github.com/topics/claude) [claude-code](https://github.com/topics/claude-code) [cli](https://github.com/topics/cli) [codex](https://github.com/topics/codex) [codex-cli](https://github.com/topics/codex-cli) [ffmpeg](https://github.com/topics/ffmpeg) [keyframe-extraction](https://github.com/topics/keyframe-extraction) [llm](https://github.com/topics/llm) [multimodal](https://github.com/topics/multimodal) [ocr](https://github.com/topics/ocr) [openai-codex](https://github.com/topics/openai-codex) [python](https://github.com/topics/python) [scene-detection](https://github.com/topics/scene-detection) [transcription](https://github.com/topics/transcription) [video-analysis](https://github.com/topics/video-analysis) [whisper](https://github.com/topics/whisper)

### Resources

[Readme](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#readme-ov-file)

[MIT license](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#MIT-1-ov-file)

### Contributing

[Contributing](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#contributing-ov-file)

### Security policy

[Security policy](https://github.com/HUANGCHIHHUNGLeo/claude-real-video#security-ov-file)

[Activity](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/activity)

### Stars

**2.2k** stars

### Watchers

**4** watching

### Forks

[**195** forks](https://github.com/HUANGCHIHHUNGLeo/claude-real-video/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FHUANGCHIHHUNGLeo%2Fclaude-real-video&report=HUANGCHIHHUNGLeo+%28user%29)

## Releases

## Packages

## Contributors

## Languages

You can’t perform that action at this time.