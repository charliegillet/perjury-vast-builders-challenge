# PERJURY: judge Q&A card (print it; one fold)

Numbers in `{braces}` come from `cache/bench_report.json` (`python -m bench.fill_numbers`). Unfilled means unmeasured:
**don't say it.**

---

**1 · Hassan: "VSS 3.3 search already confirms and rejects clips, and alert verification uses a VLM. What's new?"**
- VSS checks a clip against a query or alert someone configured. PERJURY checks *free-form testimony*, from a person
  or an agent: atom by atom, on every camera in the scene, cheapest instrument first, with a decline category.
- Our own error rates are measured on a held-out bench, including how much a leading prompt inflates agreement
  ({k}/{syco_n} leading vs {j}/{syco_n} neutral).
- We'd add VSS's verifier as one more juror and audit it the same way.

**2 · Adam: "Where does this sit in a VSS workflow, and who uses it?"**
- After `agent/ask` or `synthesize`, before a human acts: a `verify(claim, scope)` tool a NemoClaw/VSS agent can call.
- Output: a cited, timestamped verdict with exhibits. That's "traceability from evidence to decision" applied to the
  agent's own sentences.
- Users: whoever signs off on a narrative about footage (fleet safety, claims, traffic ops), and the teams building
  the agents that write those narratives.

**3 · Ram: "What did you actually do with VAST beyond reading?"**
- VastDB pushdown settles cheap atoms across every segment of the scene, past `top_k`, before any GPU call.
- Visual vectors drive the prosecutor (Embed1 picks the most claim-like moments).
- Exhibits go back in through `videos/upload`, so DataEngine indexes the verdict as searchable video. Verdict rows
  go to a VastDB table where allowed.
- The rules forbid custom DataEngine functions. Checking captions at ingest is the first one we'd write.

**4 · Brian: "How do you audit and improve it?"**
- Every verdict records the transcript, atoms, juror inputs (image hashes), probe version, model, latency and
  GPU-seconds, in Weave and in the verdict table.
- 👍/👎 is Weave feedback, and it joins the bench as a new labeled claim.
- Probe versions compete on the Weave leaderboard against the frozen test split.

**5 · Anushrav: "A system that answers 'can't tell' to everything never makes a mistake: the robot that hovers."**
- That's why support ({S}/{T}) and false accusation ({Y}/{T}) sit next to decline ({Z}/{U}). A hovering PERJURY
  scores 0 support.
- Hard-verdict types were *earned* on the dev bench (catch ≥ 80%, false accusation ≤ 10%, n ≥ 5). The rest render
  "demoted by bench".
- The jury-size curve shows whether more cameras help. If they don't, the jurors' errors are correlated, and we show that too.
- Cost: records settle {p}% of atoms with zero GPU, and T2 calls at most 6 jurors. GPU cost scales with claims, not
  footage hours.

**6 · Arnav: "Is this just a wrapper around a VLM?"**
- The VLM never sees the claim and never decides the verdict.
- The LLM splits the sentence, code validates every span, a router picks instruments, and Canary, Nemotron, Cosmos
  and YOLO play separate roles, plus Embed1 retrieval. The verdict is pure, unit-tested code.
- Built in a day in Cursor. The repo ships a `perjury-verify` skill so another agent can call it.

---

**Never say:** a TAM we didn't measure · "court evidence" / "forensics" · anything about a person's identity ·
any number not in `bench_report.json` · funding figures for guardrail companies.
**Facts we may cite:** Forbes: Axon Draft One helped write 600,000 police reports, and public records show errors
(the "on the stand" quote is from King County prosecutor Daniel Clark, not an officer) · TwelveLabs $100M Series B,
July 2026 · guardrail tools Patronus AI / Galileo / Cleanlab **[verify before stage]**.
**If a verdict is wrong live:** "That's a false accusation, and it goes into the bench." Press 👎 on screen.
