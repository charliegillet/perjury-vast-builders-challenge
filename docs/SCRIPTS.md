# PERJURY scripts (FINAL-IDEA-v3 §14a, §14c, tightened)

`{X}` numbers come from `cache/bench_report.json` (`python -m bench.fill_numbers`). The live receipt numbers are read
off the screen. **If a number isn't measured, cut the line.**

## Table-side (3:00) · laptop Chrome on `/app` with the mic flag; VM `localhost:8080` as backup

| t | Beat | Say / do |
|---|---|---|
| 0:00–0:15 | Hook | "Say anything about this footage. We'll tell you if it's true, and when we can't. Want to testify?" Hand over the mic and the claim card. |
| 0:15–0:45 | **Warm-up, Scene 2** | Judge reads *"Three pedestrians are crossing the highway in the snow."* All 16 tiles go red; snow turns green; **FALSE**. "That was VastDB and YOLO records. Zero live GPU-seconds." |
| 0:45–1:30 | **Hero** | *"A pickup is towing a trailer."* Embed1 picks the 6 most trailer-like moments, the tiles pulse, 0 jurors say yes, no caption mentions one: **FALSE**. Click **Scene 1**, same sentence: jurors say yes, each with a cyan box and a YOLO zoom ✓: **TRUE**. Open the exhibit. "Same sentence, opposite verdict. The jurors never hear the claim." |
| 1:30–1:55 | **Judge's own claim** | Any sentence. If it's temporal or about identity, it comes back UNPROVEN with the reason. "We'd rather say 'can't tell' than guess." |
| 1:55–2:20 | **A/B and numbers** | "The stock VSS agent, on the same sentence, said: '…'" (read it off the panel). "On {N} held-out claims, PERJURY caught {X}/{L} lies, wrongly accused {Y}/{T} truths, and declined {Z}/{U} untestable ones. Stock caught {A}/{A_n}." |
| 2:20–2:45 | **Witness stand + sycophancy** | "We also put VSS's own summary on the stand: {c} contradicted, {u} unverifiable. When we *leak* the claim into the prompt, Cosmos agrees with the lie {k}/{syco_n} times; with neutral probes, {j}/{syco_n}. That's why jurors never hear testimony." |
| 2:45–3:00 | **Receipt** | Read the receipt off the screen: "N of 13 services fired, calls, seconds, GPU-seconds. Every step is in Weave. Thumbs up or down, and it goes into the eval." |

**Fallbacks:** mic dead → recorded file upload, then typed. GPU host saturated → REPLAY (banner stays on; say "this is
the 15:35 run"). If the judge's claim gets a wrong verdict: "That's a false accusation, and it goes into the bench." Press 👎.
**If G3 failed**, the hero is the snow flip: *"The road is covered in snow"* → S1 FALSE vs S2 TRUE. The trailer stays
in the bench as a measured failure.

## Submission video (2:00) · freeze 15:30 · record 15:35–16:05 · upload by 16:15 · submit by 16:20

| t | Shot | On screen |
|---|---|---|
| 0:00–0:08 | **Cold open** | A judge's voice: "A pickup is towing a trailer." 16 tiles pulse; **FALSE** stamps at 0:08. |
| 0:08–0:20 | Title | PERJURY · "Every claim about the footage takes the stand." · built on VAST, NVIDIA, W&B and CoreWeave |
| 0:20–0:50 | Flip + exhibit | Scene 1, same sentence → **TRUE**; exhibit drawer with the Cosmos box and the YOLO zoom; fast cut of the pedestrians warm-up. |
| 0:50–1:10 | How it works | Tier diagram (records → captions → jury), then the ribbon lighting chip by chip, receipt "N of 13 fired". |
| 1:10–1:30 | Bench | Test numbers with CIs, the jury-size curve, the sycophancy bars, the stock A/B row (Weave leaderboard screenshot). |
| 1:30–1:45 | Witness + decline | A VSS summary with pills on every sentence; UNPROVEN on "braked hard". |
| 1:45–2:00 | Close | Repo URL, `/app` QR code, team, **"Measured, not claimed."** |

**Recording rules:**
- The live segment is the 15:35 run, and an on-screen caption says so.
- Bench numbers come from the 14:00 test run only (rendered slides, never typed).
- QuickTime on the laptop (VM screen-recorder as backup). Upload unlisted to YouTube or Drive; check the link in incognito.
- The FIXTURE or REPLAY banner is never cropped out.
