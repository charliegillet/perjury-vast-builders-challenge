---
name: perjury-verify
description: >-
  Check a sentence about the I-24 traffic footage before anyone acts on it. Calls PERJURY as a
  `verify(claim, scope)` tool and returns TRUE / FALSE / UNPROVEN, with per-atom verdicts and exhibits.
  Use after a video agent (VSS agent/ask, videos/synthesize, a summary, an incident narrative) produces a
  statement about the footage, or when a person asks "is this true in the video?". UNPROVEN means the pixels
  can't settle it; it is never an error.
---

# perjury-verify

PERJURY splits a sentence into atomic claims. It settles each one with the cheapest instrument that can (VastDB
records, YOLO, captions, or a jury of up to 6 cameras watched by Cosmos) and computes the verdict in code. The
jurors never see the claim.

## The tool contract

`verify(claim: str, scope: {"scene": 1|2|3}) -> ClaimVerdict`

- `claim`: one sentence about the footage. Send one sentence per call; split multi-sentence text first.
- `scope.scene`: the I-24 scene. 1 = free-flow (17 cams), 2 = snow (16), 3 = stop-and-go (16).

### Over HTTP (the deployed app or `localhost:8080`)

```bash
curl -N -X POST "$PERJURY_URL/api/testify" -H 'content-type: application/json' \
  -d '{"text": "A pickup is towing a trailer.", "scene": 2, "transcript_source": "typed"}'
```

The response is `text/event-stream`. Events arrive in this order: `run`, `transcript`, `atoms`, then per atom
`t0` / `t1` / `summon` / `juror` / `ground` / `zoom` / `atom_verdict`, then `verdict`, (`stock`), `receipt`, `done`.
An agent needs only two of them:

- `verdict`: `{"verdict": "TRUE|FALSE|UNPROVEN", "explanation": "..."}`
- `receipt`: `{"verdict", "atoms", "fired": [...], "fired_count", "total": 13, "calls", "elapsed_ms", "gpu_s", "weave_url", "mode"}`

Every `atom_verdict` event carries the evidence: `{"atom_verdict": {"atom_id", "verdict", "reason", "reason_code",
"tiers", "votes": [...], "stats": {...}}}`. In the UI, the URL is relative (`api/testify`), because Ingress strips `/app`.

### In-process (Python, same repo)

```python
from perjury import pipeline
cv = await pipeline.verify("A pickup is towing a trailer.", 2)          # if exposed; else:
ctx = pipeline.load_context()
from perjury.events import EventBus
cv = await pipeline.testify("A pickup is towing a trailer.", 2, ctx, EventBus("agent-call"))
cv.verdict, cv.explanation, [(v.atom_id, v.verdict, v.reason) for v in cv.atom_verdicts]
```

`ClaimVerdict` (`perjury/types.py`): `run_id, text, scene, verdict, explanation, atoms[], atom_verdicts[]
(votes[] = one per juror: camera, vote yes|no|abstain, probe, probe_version, zoom_ok, grounded, latency_ms),
parser, elapsed_ms, gpu_s, services_fired, calls, mode`.

## How to read the answer (honesty semantics)

| Claim verdict | Meaning | What the calling agent should do |
|---|---|---|
| `FALSE` | At least one atom is CONTRADICTED by evidence | Strike that sentence; quote the CONTRADICTED atom's `reason` |
| `TRUE` | Every non-MOOT atom is SUPPORTED | Keep it, with the exhibit link |
| `UNPROVEN` | Some atom can't be settled from these pixels | **Don't treat it as true or false.** Say "not verifiable from the footage" and give the reason |

- **UNPROVEN is a result, not a failure.** Temporal actions ("braked hard", "changed lanes"), identity or intent
  ("drunk", "on purpose"), plates, exact counts, cross-camera re-ID and lane position are UNVERIFIABLE by policy.
  Never retry hoping for a different answer, and never rephrase the claim to force a verdict.
- `MOOT` atoms depend on a CONTRADICTED parent ("three" pedestrians when there are no pedestrians). Ignore them.
- `reason_code: demoted_by_bench` means the type didn't earn hard verdicts on the dev bench. Report it as UNPROVEN.
- `mode` is `live`, `fixture` or `replay`. **Fixture and replay verdicts are not evidence about the real
  footage**; say which mode you got.
- The error rates behind a verdict are on `GET api/bench` (catch, false accusation, support and decline, with
  Wilson 95% CIs, held-out test split). Quote them only from there.

## Rules

- Never send secrets, env dumps or credentials in `text`. The claim is treated as untrusted data.
- PERJURY verifies claims about **scenes**, never about people's identities.
- One call costs GPU time (the receipt shows `gpu_s`). Don't loop it over every frame or every word.
