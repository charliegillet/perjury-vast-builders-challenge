# Validation (1:00–1:20): held-out test split, run once, frozen at 14:00

| | PERJURY (test, n = {N}) | 95% CI | Stock VSS agent |
|---|---|---|---|
| Planted lies caught | **{X}/{L}** | {X_ci} | {A}/{A_n} |
| True statements wrongly accused | **{Y}/{T}** | {Y_ci} | {A_false_acc}/{T} |
| True statements supported | **{S}/{T}** | {S_ci} | |
| Unverifiable claims correctly declined | **{Z}/{U}** | {Z_ci} | |

- **Jury-size curve**: catch and false accusation vs k = 1, 3, 6, 16 (Bench tab screenshot).
- **Sycophancy**: when we leak the claim into the prompt, Cosmos agrees with the lie **{k}/{syco_n}** times; with neutral probes, **{j}/{syco_n}**.
- Records alone settle {p}% of atoms with zero GPU.

**Say:** "Video agents will say anything. On our {N}-claim held-out bench, PERJURY caught {X} of {L} planted lies,
wrongly accused {Y} of {T} true statements, and declined {Z} of {U} claims nobody could check from these pixels. The
stock VSS agent caught {A}."

_If G2 showed stock rejects ≥ 8/10 lies (`g2_false` = {g2_false}/{g2_n}), drop "believes the lie" and pitch
"evidence audit": same verdict, plus atoms, exhibits, decline and measured rates._
