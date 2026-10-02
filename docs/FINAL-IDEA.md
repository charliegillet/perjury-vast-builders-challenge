# FINAL IDEA — UNWATCHED

> **🔁 SUPERSEDED (2026-10-01 night) by [FINAL-IDEA-v2.md](FINAL-IDEA-v2.md): ASSAY.** Round-2 corpus research showed UNWATCHED's learned-normal story only holds on Pack D (one baseline day, possibly sparse). UNWATCHED survives as the pivot NIGHTSHIFT + VOID.

> **🚨 READ FIRST — official starter kit found (2026-10-01 night): [OFFICIAL-STARTER-KIT.md](OFFICIAL-STARTER-KIT.md) supersedes §5 architecture and §9 checklist.** Teams build on a pre-deployed stack from a browser VM (workshop.thecosmoslabs.com) and must **not** deploy DataEngine functions — our scorer/verifier/digest run as one app service on the VastDB index. Model is **Cosmos3-Reason** (call directly, bearer `GPU_BEARER_TOKEN`). Corpus = dashcam/highway/neighborhood/SF streets/**warehouse (synthetic)**/**indoor** — use Packs C+F+D. New video upload works via `upload-video` (indexing takes tens of seconds–minutes).
>
> **⚠️ Corrections from deep research (2026-10-02) — read before pitching.** Full detail in [DEEP-RESEARCH.md](DEEP-RESEARCH.md).
> 1. **Do NOT say "no shipped product does this" or "first."** Avigilon (Motorola) has shipped rule-free, learned-per-scene "Unusual Activity Detection" since 2018; Lumana/Coram claim per-camera learned normal; Google Home and Svid send unprompted daily digests; a Qdrant + Twelve Labs open-source VSS demo (Mar 2026) does embedding-distance outliers → VLM. What's defensible is the **combination**: per-camera learned normal + Cosmos-Reason2 verify of every outlier + measured suppression counter + push digest over stored archives, all inside VAST DataEngine.
> 2. **New stage line:** "Cameras that learn what's normal aren't new — Avigilon shipped it in 2018. They never took off because for every real event they flagged a hundred harmless ones. UNWATCHED adds the missing step: Cosmos-Reason2 checks every outlier against what that camera normally sees, nobody gets paged until it passes, and we count and measure everything we chose not to show you."
> 3. **Cosmos already runs on every segment** in the starter blueprint (ingest captions each 5 s segment). "Cosmos only sees 3%" applies only to our *verify* call — say "only ~3% of segments get the expensive reasoning/verify pass."
> 4. **Segments are 5 s** (not 10 s). Upload 5 s live-cam chunks. Embeddings are 256-d; skip all-zero vectors when building the centroid.
> 5. **No Kafka/DB-row triggers in DataEngine** — triggers are `Element` (S3 object events) and `Schedule` (Quartz cron). Fan the scorer out from the embedder output; use DataEngine conditional routing (or a poller) to reach the verifier. Digest: schedule every minute, post once at 15:31 PT (cron timezone undocumented); laptop cron as backup.
> 6. ~~Try NVIDIA's `Cosmos-Embed1-448p-anomaly-detection` embedder~~ — **not available on the event stack** (only 256-d Cosmos-Embed1). Still credit VSS's temporal dedup openly. — and credit VSS's "temporal dedup" step openly.
> 7. **Market:** video surveillance ≈ **$27B (Omdia, 2025)**, $60–80B+ on broad definitions — not "$50B+". IPVM: **<1%** of recorded footage is watched live. NVIDIA: **2B+ cameras**. Price **$8/camera/month** is supported by comps.
> 8. **Use the venue's Cosmos NIM** (hosted build.nvidia.com Reason2 has been returning 404). VSS 3.2.1+ defaults to Cosmos Reason 3 Nano — confirm which model the event serves at 10:00.
> 10. **Verifier model accuracy is the #1 risk.** On VANTAGE-Bench (NVIDIA + Clemson, Sep 2026), Cosmos-Reason2-8B accepted ~42% of events that never happened (specificity 57.6); Cosmos3-Super/Nano score higher. Prefer Cosmos 3 if the venue serves it, use **class-specific** verify prompts, and **measure specificity on our ~60 labeled clips in Weave before claiming "doesn't cry wolf."** Gemini is an outage-only fallback (`src/verifier_backends.py`); see [GEMINI-FALLBACK.md](GEMINI-FALLBACK.md).
> 9. **Privacy framing:** private operational spaces (stockrooms, server cages, after-hours docks), no face ID, no "suspicious person" language.


> **The archive that watches itself and doesn't cry wolf.**
> Every camera-hour that lands in VAST gets scored against what that camera *normally* sees. Cosmos-Reason2 checks only the outliers. You get pinged only when a clip is worth your time, plus a morning digest you never asked for: "8 hours of footage last night, 3 things you should see, 41 seconds total."

Merge of NIGHT WATCH (push, not pull: the archive triages itself) with FOREMAN (Cosmos verify step, visible suppression counter). The name comes straight from the event theme: *"most of it stays in storage, unwatched and underused."*

---

## 1. Judge-panel simulation (C = creativity, T = technical implementation, I = real-world impact)

### UNWATCHED (merged, with the demo fix below) — **25.2 / 30, demo 9**
| Judge | C | T | I | One line |
|---|---|---|---|---|
| Hassan Moustafa (NVIDIA TME, Multimodal) | 9 | 8 | 8 | Uses Cosmos-Embed1 vectors to model "normal", not to search, and puts Reason2's grounding and CoT on screen as the reason for each decision. I haven't seen that before. |
| Adam Ryason (NVIDIA Product) | 8 | 8 | 9 | It sits next to alert-verification instead of copying it: it finds the events nobody wrote a rule for. I could picture it as a VSS workflow. |
| Ram Bansal (VAST Sr Dev Advocate) | 9 | 9 | 8 | They wrote their own DataEngine functions into our pipeline, and the live camera is just another bucket prefix. That's the right way to use the platform. |
| Brian Verkley (VAST Dir. AI Data Platform) | 9 | 8 | 9 | "Unwatched data becomes an asset that pages you" is the AI OS story. VastDB holds the baseline, the verdicts, and the audit trail. |
| Anushrav Vatsa (CoreWeave SA, Physical AI) | 8 | 8 | 9 | Only 3% of segments reach the GPU. The cost per camera-hour works at 10k cameras. |
| W&B SA (Vera A. / Junaid Butt) | 8 | 9 | 8 | They measured suppression precision and recall with a Weave eval and fed Slack thumbs up/down back as Weave feedback. That's a real eval loop, not just logging. |

### T-MINUS (formerly BLACKBOX) — **22.7 / 30, demo 8**
| Judge | C | T | I | One line |
|---|---|---|---|---|
| Hassan | 7 | 7 | 7 | Solid, but the video reasoning mostly re-captions footage. |
| Adam | 7 | 7 | 7 | It only runs after an alert already fired, so it's reactive. |
| Ram | 9 | 8 | 7 | Snapshots for time travel is a rarely used VastDB feature. Big flex if the granularity holds up. |
| Brian | 9 | 8 | 8 | "What did the system know at T-4 min" is a real enterprise audit question. |
| Anushrav | 7 | 7 | 7 | Useful to ops teams, less exciting as physical AI. |
| W&B | 7 | 8 | 7 | The Weave-traced postmortem is good. The eval story is weaker. |

### FOREMAN standalone — **20.3 / 30, demo 9**
| Judge | C | T | I | One line |
|---|---|---|---|---|
| Hassan | 5 | 8 | 7 | "That's our alert-verification NIM with a hardhat on it." |
| Adam | 4 | 8 | 8 | "We ship this. What's new?" |
| Ram | 5 | 7 | 7 | Uses the blueprint pipeline as-is, nothing custom in DataEngine. |
| Brian | 5 | 7 | 7 | PPE is already productized. |
| Anushrav | 6 | 8 | 8 | The live demo is nice, but it's the fourth PPE demo today. |
| W&B | 6 | 7 | 7 | Standard Weave tracing. |

### Other merge considered: FOREMAN + BLACKBOX ("verified alert, then postmortem") — ~22
Rejected. It inherits FOREMAN's prior-art problem and BLACKBOX's snapshot risk, and it still reacts to a rule someone already wrote. The one piece worth keeping from BLACKBOX goes into UNWATCHED as a stretch goal: each dismissal records the VastDB snapshot ID of the baseline it was judged against, so you can audit why something was suppressed.

### Verdict: **COMMIT to UNWATCHED.**
Two teammates really believe in it (the Ideator ranked it #1, and it's the Devil's Advocate's top surviving pick). Its individual pieces exist (Avigilon learned-normal since 2018, consumer digests, a Qdrant/Twelve Labs VSS demo — see corrections above), but the combination with a verify gate and measured suppression is unclaimed. It matches the theme word for word. Its one weakness was a demo score of 7, fixed below. We are not settling for FOREMAN, the safe option everyone else will build.

---

## 2. The demo fix (7 → 9)
The payoff is proven twice, and neither proof needs a person to click anything:
1. **Autonomy proof (pre-seeded but real):** an "overnight" archive of 4 sample cameras ingested during the build. The digest job fires on a schedule at **15:31**, while we're building (it must land before the 16:30 submission deadline so it appears in the demo video), so the Slack timestamp itself shows nobody asked for it.
2. **Live proof:** the room webcam is **camera #5, uploaded to the same bucket and processed by the same pipeline.** It has watched one quiet corner (a stool holding a prop "DGX Spark" box) all afternoon, so its baseline says what that corner looks like. Live on stage, a **decoy** and a **real event** trigger the same cheap YOLO signal (a person in frame). Cosmos dismisses the decoy and escalates the real one. The push notification arrives while the presenter's hands are in the air.

The contrast is the point. A cheap gate fires twice and only one of those matters. The counter goes up for the dismissal, and the phone buzzes for the real event.

---

## 3. Problem and buyer
- **Buyer:** the security or loss-prevention operations manager at a multi-site operator (3PL warehouses, self-storage, car dealerships, school districts) with 50–500 cameras on NVRs or VMS and 30-day retention. **Nobody reviews overnight footage.** It gets deleted unwatched, or someone scrubs through it at 2x speed after a loss is discovered.
- **Pain:** rule-based analytics (line crossing, PPE, loitering) only catch what someone thought to configure, and they spam false alarms, so operators mute them. The footage that matters is the stuff nobody wrote a rule for.
- **Market / comparables:** video surveillance is ~$27B (Omdia 2025; $60–80B+ on broad definitions), and <1% of recorded footage is watched live (IPVM). Comparables are Verkada and Rhombus (cloud VMS) and Ambient.ai (AI alert triage, venture-backed). All of them are rule- or signature-first. UNWATCHED learns "normal" for each camera, needs no rules, and works on the archive as well as live feeds.
- **Business model:** add-on priced per camera per month (~$8). The price holds because only ~3% of segments get the extra Cosmos verify pass. Go-to-market: through VMS/NVR integrators and a VAST AI OS marketplace listing.

## 4. Why this is past the baseline
| | vss-blueprint (starter kit) | NVIDIA `vss-alert-verification` | **UNWATCHED** |
|---|---|---|---|
| Trigger | A human types a search | A detector rule fires (e.g. "person in zone") | **Nobody. Each segment is scored against a learned, per-camera normal** |
| Direction | Pull | Push, but only for rules someone configured | **Push for things no rule covers** |
| Scope | Query time | Live stream | **Live and the entire historical archive** |
| Output | Clip cards and a summary | An enriched alert | **Silence by default, a verified push, a daily digest, and a clickable receipt for every dismissal** |
| Learns | No | No | **Yes: Slack feedback updates the baseline and becomes a Weave eval label** |

One-liner for judges: *"Alert-verification checks the alerts you already wrote rules for. We find what nobody wrote a rule for, in footage nobody watches."*

---

## 5. Architecture

```
[laptop webcam] ffmpeg 5s mp4 → boto3 PUT s3://vss-chunks/cam-05-live/…   (just another camera)
[sample footage x4 cams] ─────────→ s3://vss-chunks/cam-0{1..4}/…            (the "overnight" archive)
        │
REUSED blueprint DataEngine chain:
video-segmenter → video-detector (YOLO11 counts+bbox) → video-reasoner (Reason2 caption)
→ video-embedder (Cosmos-Embed1 visual+text vec) → vastdb-writer (segments table)
        │  (trigger: segment row / embedding sidecar written)
NEW:  nw-scorer ──(candidate)──► Kafka topic nw.candidates ──► nw-verifier (Cosmos-Reason2 CoT + 2D grounding)
        │                                                        │
        │ writes nw_scores                         writes nw_verdicts, Weave trace
        │                                                        ├─ dismiss → suppression counter
        ▼                                                        └─ escalate sev≥4 → nw-pusher → Slack (thumbnail w/ bbox)
nw-baseline-updater (every 15 min; Ibis pushdown over segments ⨝ nw_verdicts)
nw-digest (scheduled; W&B Inference) → Slack digest
Slack 👍/👎 → nw_feedback + Weave feedback on the verifier call → excluded from/added to baseline
Dashboard: heartbeat waveform of score, per-stage chip strip, streamed <think>, counter
```

**Reused from vss-blueprint:** segmenter, detector (YOLO11 class counts give the class-z signal), reasoner (captions feed the baseline summary), embedder (Cosmos-Embed1 visual vector gives the distance signal), vastdb-writer, and `POST /api/v1/agent/ask` (stretch: "ask about this event" in the Slack thread).

**New DataEngine functions:**
| Function | Trigger | Job |
|---|---|---|
| `nw-scorer` | segments row / embedder sidecar (fallback: 2s poller on `scored=false`) | `dist = 1 − cos(visual_vec, centroid[cam, bucket])`; `class_z` from YOLO counts; candidate if dist > cam p99, or class_z > 3, or 1% random audit. The first 200 segments per camera are learn-only |
| `nw-verifier` | Kafka `nw.candidates` (VAST Event Broker) | Reason2 verify prompt, then JSON verdict. Writes `nw_verdicts` and a Weave trace |
| `nw-pusher` | verdict with severity ≥ 4 | Slack Block Kit with a bbox-burned keyframe and the reason, plus 👍/👎 buttons |
| `nw-baseline-updater` | schedule, 15 min | Recompute centroid and percentiles per camera/bucket, excluding escalated segments. Regenerate `summary_text` |
| `nw-digest` | schedule (06:00 in the product; 15:31 on demo day) | W&B Inference LLM writes the Slack digest |

**VastDB tables:**
- `nw_baseline(camera_id, bucket, centroid list<float>, p50, p95, p99, class_mean map, class_std map, n, summary_text, updated_at)`
- `nw_scores(segment_id, camera_id, ts, embed_dist, class_z, score, is_candidate, is_audit)`
- `nw_verdicts(segment_id, verdict, category, severity, reason, bbox list<int>, think_text, model, latency_ms, weave_call_id, baseline_snapshot)`
- `nw_feedback(segment_id, label, user, ts)`
- `nw_digests(digest_id, window_start, window_end, n_segments, n_candidates, n_dismissed, n_escalated, body_md, posted_at)`

Buckets: archive cameras use hour-of-day buckets. The live camera uses a single bucket.

**Cosmos-Reason2 verify prompt (8B; 2B as fallback):**
```
You are a night-shift video verifier for camera {camera_id} ({camera_context}).
A statistical baseline flagged this 5-second clip as unusual compared with what this camera normally shows.
What is normal here: {baseline.summary_text}
Why it was flagged: embed_dist={dist} (p99={p99}); class deltas={class_deltas}.
Decide whether a human should be interrupted. Think step by step inside <think></think>, then output ONLY JSON:
{"verdict":"escalate|dismiss","category":"theft|intrusion|safety|equipment_change|benign_activity|lighting|camera_fault",
 "severity":1-5,"reason":"<=20 words, plain English","evidence_bbox":[x1,y1,x2,y2],"evidence_t":<seconds>}
Escalate only if a person interacts with, removes, or damages property, or someone is at risk. Passing through is not an event.
```
**Baseline summary prompt (W&B Inference, Nemotron 3.5 Lightning):** "Given these 50 captions from camera {id} during {bucket}, describe in 3 sentences what is routine here: who or what appears, how often, what never changes. No speculation."

**Digest prompt (W&B Inference, Nemotron 3 Ultra; fallback Nemotron 3.5 Lightning).** Nemotron here keeps NVIDIA's model on W&B's inference service, which touches two sponsors at once. "Input: JSON of escalations and window stats. Write a Slack digest: headline stat line, at most 5 items ranked by severity, each one line plus a `segment_id` link, total watch time. Footer: segments scanned / flagged / dismissed. Never mention an event that isn't in the input."

**Weave:**
- `@weave.op` on scorer, verifier, and digest. Each Slack alert links to its Weave call.
- **Weave Evaluation:** 60 hand-labeled candidate clips. Scorers: verdict accuracy, escalation precision and recall, JSON validity, latency. Compare Reason2 8B vs 2B and prompt v1 vs v2 in one leaderboard.
- **Weave feedback:** Slack 👍/👎 is attached to the verifier call, which gives a live label stream.

---

## 6. Sponsor features to show off, by judge
- **VAST (Ram, Brian):** custom functions inserted into the DataEngine trigger chain; VAST Event Broker Kafka topic between scorer and verifier; VastDB as the *state* store for the baseline (Ibis pushdown with per-camera percentile queries); `vastde traces` / `logs` shown for the live event; *stretch:* `baseline_snapshot` ID on every verdict (snapshot time travel: "why was this dismissed at 03:12?").
- **NVIDIA (Hassan, Adam):** Cosmos-Embed1 used as a **distribution model** (the uncommon use: anomaly detection, not search); Reason2 **2D grounding** bbox burned into the push; Reason2 `<think>` shown as the reason for each dismissal; YOLO11 as the cheap gate (the pattern Team Jarvis used at the Cookoff); Nemotron for the digest.
- **CoreWeave (Anushrav):** a live GPU-cost meter on the dashboard: "Cosmos invoked on 3.1% of segments, $/camera-hour = X." That explains how it scales.
- **W&B (Vera / Junaid):** Weave Evaluation leaderboard (model × prompt), Weave feedback from Slack, W&B Inference for both LLM roles.

---

## 7. Three-minute demo script
Screen layout: left = dashboard (heartbeat waveform, stage chips, counter, streamed `<think>`); right = Slack. A phone on the table has Slack notifications on.

| Time | Beat |
|---|---|
| 0:00–0:20 | **Problem.** "Last night, a warehouse like this recorded 8 hours on 4 cameras. Who watched it? Nobody. In 30 days it's deleted." Name the buyer. |
| 0:20–0:50 | **Autonomy proof.** Open Slack. A digest **posted at 15:31, while we were heads-down building**: "8h 04m across 4 cameras → 3 things worth 41 seconds." Click #1: bbox keyframe plus a one-line Cosmos reason. Point at the footer: "212 flagged by the baseline, **197 dismissed by Cosmos**. You never saw them." Click one dismissal to show its receipt. |
| 0:50–1:10 | **Same pipeline.** "This room is camera #5. Same bucket, same DataEngine functions." Run a VastDB query live: `cam-05-live` rows keep arriving. The waveform is flat. "It's watched this corner since noon, so it knows what normal looks like here." |
| 1:10–1:45 | **Decoy.** A teammate walks through the frame, glances around, and leaves. Waveform spikes, "candidate" chip lights, `<think>` streams: *"person passes through, no interaction with objects… dismiss."* **Counter 197 → 198. Slack stays silent.** "It noticed. It checked. It stayed quiet." |
| 1:45–2:15 | **Real event (the gasp beat).** Presenter: "I'm not touching anything," and raises both hands. A teammate walks in, **picks up the DGX Spark box, and walks out.** Same spike, but `<think>`: *"person removes boxed equipment and exits; object no longer present → escalate, severity 4."* **The phone buzzes.** Slack push shows the keyframe with Cosmos's bbox around the box: "Equipment removed from table, 14:02:31." Presenter: "That's the prize. We'd like it back." |
| 2:15–2:35 | **Under the hood.** One architecture frame, then click from the Slack alert to its Weave trace. Show the eval leaderboard: escalation precision/recall on 60 labeled clips, 8B vs 2B. GPU meter: "Cosmos ran on 3% of segments." |
| 2:35–2:50 | **Contrast.** "NVIDIA's alert-verification checks the alerts you already wrote rules for. We find what nobody wrote a rule for, in footage nobody watches." |
| 2:50–3:00 | **Business and close.** "Per camera per month, sold through integrators, on the VAST AI OS. Your archive can't watch itself today. Ours does." |

Rehearse the decoy and real event 3× on-site. The two must be the same person, same path, same entry point, so the only difference is the interaction with the box.

---

## 8. Build plan (10:00–16:30 — submission deadline is 4:30 PM PT; demos 5:00)

> Updated 2026-10-02 from the official portal (docs/EVENT-DETAILS.md): submission = **public GitHub repo + shareable demo video** due **16:30**. Coding freeze 15:30.
Roles: **Nihal** = agent/backend lead (scorer, verifier, prompts). **P2** = VAST infra and ingest (DataEngine, VastDB, live cam). **P3** = Slack and dashboard. **P4** = footage, labels, Weave eval, pitch. With 3 people, P3 also takes P4's work.

| Hour | Nihal | P2 | P3 | P4 |
|---|---|---|---|---|
| 10:00–11:00 | Verification checklist (§9). Cosmos latency test, verify-prompt v1 on 3 clips | Blueprint up, test deploy of a hello-world `vastde` function + trigger | Slack app, webhook, Block Kit with image | Pick 4 "overnight" cams from sample footage, splice in 6–8 anomalies |
| 11:00–12:00 | `nw-scorer` offline in a notebook over existing segment vectors; pick signals | `cam-uploader` (ffmpeg → S3) → rows appear; create `nw_*` tables | Dashboard skeleton: waveform, chips, counter | Label 60 candidate clips (escalate/dismiss) |
| 12:00–13:00 | Deploy `nw-scorer` as a function (or poller fallback); Kafka topic | **Start archive ingest by 12:00 at the latest** (throughput cap); aim the live cam at the corner so its baseline starts | Stream `<think>` into the dashboard | Weave eval harness |
| 13:00–14:00 | `nw-verifier` + Weave ops; JSON repair/retry | `nw-baseline-updater` + summary_text job | `nw-pusher` bbox-burn keyframe (PIL) | Run eval: 8B vs 2B, prompt v1 vs v2 |
| 14:00–15:00 | **End-to-end live: walk-by → dismiss, box grab → push** | `nw-digest` on W&B Inference; schedule for 15:31 | Slack 👍/👎 → `nw_feedback` + Weave feedback | GPU-cost meter numbers; draft slides |
| 15:00–15:30 | Tune thresholds on the live corner (30-min timebox); watch the 15:31 digest fire | `vastde traces` view ready | Polish UI; dismissal receipt clickable | Rehearse 1 and 2 |
| 15:30–16:10 | **Code freeze 15:30.** Record the demo video (two proofs, 2–3 min), upload, get shareable link | Make repo public; scrub `.env`/keys; README with tools used | Screenshot for submission | Write "what we built + tools" text; team names + emails |
| 16:10–16:30 | **Submit on tokensand.com/vastsf/submit by 16:20** (10-min buffer) | Stability and quota watch | Final UI | Confirm it shows in the project gallery |
| 16:30–17:00 | Rehearse live demo + Q&A drill | Reset live cam corner | Reset Slack channel for live run | Q&A drill |

---

## 9. First 60 minutes: on-site verification checklist
- [ ] Blueprint version provisioned. Is `/api/v1/agent/ask` up? Does the `segments` table schema include the **visual embedding column** (name, dimension)?
- [ ] Can a custom `vastde` function be created and triggered by **the same bucket/table events** the blueprint uses? Get the exact flags from `vastde doc`.
- [ ] Is there a DataEngine **schedule/cron trigger**? (If not, run the updater and digest as laptop cron jobs.)
- [ ] Does the embedder depend on the reasoner caption? (It decides live latency and whether the archive can skip captioning.)
- [ ] Pipeline throughput: time for 1 min of video from upload to row. Multiply out to size the "overnight" archive we can finish by 15:00.
- [ ] Cosmos-Reason2 endpoint: 8B vs 2B available, p50 latency for a 5s clip (`SELECT avg(processing_time)` on segments), RPM quota (40 RPM on the free tier; is it shared by the whole venue?). Does 2D grounding return usable coordinates?
- [ ] Kafka / Event Broker topic create, produce, and consume from a function.
- [ ] Venue Wi-Fi: webcam PUT to S3 sustained; is outbound Slack allowed? (Tether a phone as backup.)
- [ ] W&B Inference key, model IDs for Nemotron 3 Ultra / 3.5 Lightning; Weave project logging works.
- [ ] (Backup-only) VastDB snapshot: create, list, and read a table *as of* a snapshot, at table or bucket granularity.

---

## 10. Fallbacks per risk
| Risk | Fallback |
|---|---|
| Embedding baseline is noisy | Per-camera percentile rank rather than an absolute threshold, combined with YOLO class-count z-score. Tune for at most 45 min, then freeze. The 1% random audit keeps an eye on recall. |
| Custom function can't hook the trigger chain | `nw-scorer` runs as a 2s poller over VastDB `WHERE scored = false`. Pitch it honestly as the same logic that will run as a DataEngine function. |
| No Kafka topic | Scorer calls the verifier directly and writes to an `nw_queue` table. |
| Cosmos is slow or rate-limited | Switch to 2B, sample 4 frames instead of the full clip, verify only on keyframes. The streamed `<think>` covers the wait. On stage, only the live cam goes to Cosmos. |
| Cosmos escalates the walk-by | Add walk-by examples to the baseline summary and tighten the "passing through is not an event" line. As a last resort, change the decoy to a box moved and then put back. |
| Live cam or Wi-Fi dies on stage | Phone hotspot. If still dead, feed a clip recorded that afternoon into the **same upload path** and say so out loud. Then play the backup video. |
| Slack blocked | Discord webhook, plus an on-dashboard toast with a sound. |
| Archive ingest too slow | Shrink the archive to 4 cams × 30 min and relabel the digest honestly ("2 hours"). The ratio pitch still holds. |
| W&B Inference down | The digest uses a template filled from `nw_digests` stats. The verifier doesn't depend on W&B. |

---

## 11. Judge Q&A armor
1. **"Isn't this NVIDIA's alert-verification?"** That service verifies alerts from a detector rule you configured. We have no rules. The trigger is distance from a normal learned for each camera, applied to the archive as well as live feeds. The verify step is shared plumbing, and we'd happily call their microservice for it in production.
2. **"How does the baseline cold-start, and how does it drift?"** The first ~200 segments per camera bucket are learn-only. The updater recomputes every 15 minutes and excludes escalated segments, so an incident can't become normal. A 👎 from a human moves a segment into the baseline, and that's the only way a flagged pattern gets whitelisted.
3. **"What about misses, where the real event looks normal?"** A 1% random audit sends segments to Cosmos regardless of score, and the Weave eval reports recall next to precision. We're explicit that this ranks attention. It doesn't replace life-safety detectors.
4. **"Does this scale to 10,000 cameras?"** Scoring is one cosine against a cached centroid, CPU only, in a DataEngine function that scales horizontally. Cosmos only sees about 3% of segments, and the meter shows the cost per camera-hour. VastDB handles parallel selects across CNodes when the updater recomputes baselines.
5. **"Why VAST instead of S3 + Postgres + pgvector?"** Video, vectors, baseline state, verdicts, and triggers all live in one system. There's no ETL between object storage, the database, and the queue, and a function fires as soon as a segment lands. Snapshots give an auditable "what did the model consider normal at 03:12" (stretch).
6. **"Who buys this, and how do you reach them?"** The LP/security ops manager at a multi-site operator. They buy per camera per month through VMS integrators who already sell AI add-ons. The wedge is the morning digest: it shows value on day one with no rules to configure.

---

## 12. Backup pitch — **T-MINUS** (renamed from BLACKBOX; a "BlackBox" already won a DataHub agent hackathon)
> *"Every physical incident gets an SRE-grade postmortem: what the cameras saw, what the system knew, and when it knew it."*

An alert arrives on Kafka. T-MINUS fuses the alert stream with video segments and uses **VastDB snapshots** to replay "what the system knew at T-4 min." A W&B Inference model writes a Weave-traced postmortem (timeline, contributing factors, detection gap, action items). It fits Nihal's SRE background: incident timelines and blameless postmortems applied to the physical world. About 70% of the code is shared with UNWATCHED (ingest, verifier, Weave, Slack, VastDB tables). The demo beat: scrub a tape-rewind slider to the T-4min snapshot and watch the postmortem stream in.

**Pivot trigger (hard, 11:15):** pivot if, after the 45-min tuning timebox, the scorer's top-20 outliers on the seeded archive contain fewer than 10 of the planted anomalies **and** the percentile + class-z fallback also misses. The pivot also requires that the checklist confirmed **table-level snapshot time travel** works. If snapshots are bucket-level only, stay on UNWATCHED and cut the archive to a 30-min curated set instead.
