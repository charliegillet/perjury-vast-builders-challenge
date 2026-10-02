# Stage deck shells (§14b order, 3:00 total)

These are templates. `{X}` placeholders are filled **only** from `cache/bench_report.json["numbers"]` by:

    python -m bench.report && python -m bench.fill_numbers        # -> docs/slides/rendered/

- `fill_numbers` refuses fixture/offline reports (preview with `--allow-fixture`, which stamps every number `[FIXTURE]`).
- Any placeholder it can't fill stays visible as `{X}` and makes the command exit 1. **An unfilled number doesn't go
  on screen**: cut the line instead of typing a number.
- Headline numbers come from the **test** split (run once at 14:00). Dev numbers (`dev_*`) are for the grey row only.
- `[verify before stage]` marks the plan's `[A]` assumptions. Confirm or cut them before 15:15.
- Edit wording here, never in `rendered/`.

| # | File | Section | Time |
|---|---|---|---|
| 1 | `01-problem.md` | Problem | 0:00–0:25 |
| 2 | `02-solution.md` | Solution | 0:25–0:45 |
| 3 | `03-market.md` | Market | 0:45–1:00 |
| 4 | `04-validation.md` | Validation | 1:00–1:20 |
| 5 | `05-demo.md` | Demo | 1:20–2:20 |
| 6 | `06-business-model.md` | Business model | 2:20–2:35 |
| 7 | `07-future.md` | Future | 2:35–2:50 |
| 8 | `08-team.md` | Team | 2:50–3:00 |

Placeholder keys (see the `numbers()` docstring in `bench/report.py`): `N` test claims · `X`/`L` lies caught / lies ·
`Y`/`T` truths falsely accused / truths · `S` truths supported · `Z`/`U` unverifiable correctly declined / unverifiable ·
`*_ci` Wilson 95% CI strings · `A`/`A_n` stock agent lies caught / lies · `j`/`k`/`syco_n` sycophancy neutral / leading
yes counts out of n · `c`/`u` witness-stand sentences contradicted / unverifiable · `p` % of atoms settled by records alone ·
`hero_s1_yes`/`hero_s1_k` · `receipt_calls`/`receipt_s`/`receipt_gpu_s` (dev hero run) · `g2_false`/`g2_n`.
