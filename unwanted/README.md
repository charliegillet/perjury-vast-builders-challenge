# unwanted/

Files moved out of the working tree on **2026-10-02** because they aren't needed to build, demo or submit **ASSAY** ([docs/FINAL-IDEA-v2.md](../docs/FINAL-IDEA-v2.md)) or its pivot NIGHTSHIFT. Nothing was deleted. Each file keeps its original path under this folder, so `docs/sources/x.md` is now `unwanted/docs/sources/x.md`, and git history follows it (`git log --follow`).

**How it was decided:** four analysis teams each classified a slice of the repo against a shared rubric (KEEP if ASSAY, the pivot, or event logistics needs it, or if it's the primary source for a claim we'll make; MOVE if it's superseded, duplicate, junk, or bulk material with nothing we use). A reviewer then checked every moved file still cited by a kept doc. It found 14 false-positive matches, 41 safe moves and 1 rescue, which was put back.

**[MANIFEST.tsv](MANIFEST.tsv)** lists every moved file with its reason. To restore one: `git mv unwanted/<path> <path>`.

**What's here (632 files):**

| Area | Files |
|---|---|
| `.firecrawl` | 367 |
| `docs/sources` | 215 |
| `.firecrawl/starter-repos` | 44 |
| `docs` | 4 |
| `(root)` | 2 |

**Main categories:**
- **Superseded idea:** UNWATCHED (`docs/FINAL-IDEA.md`, `docs/DEEP-RESEARCH.md`, `docs/research.md`), the round-1 ideation files, and UNWATCHED-only competitor and surveillance-market captures (`dr-comp-*`, `dr-judge-mkt-*`).
- **Gemini deep-dives:** Gemini is an outage-only fallback in ASSAY, so only three core Gemini docs stay in `docs/sources/`.
- **Duplicates:** older copies of the official starter repo (relaxedtomato) and pages captured twice.
- **Junk captures:** empty or error files, 404s, sign-in walls and cookie pages.
- **Raw search-result JSONs** whose useful content is already captured or summarized.
- **Very large, low-value pages:** for example nemoclaw.md and the full Cosmos community index.

**Second pass (same day):** a "can it help make the project?" review restored 85 files to their original paths. See [docs/REUSE-FROM-UNWANTED.md](../docs/REUSE-FROM-UNWANTED.md).

`lastframe/` and `docs/LAST-FRAME.md` were deliberately left alone.
