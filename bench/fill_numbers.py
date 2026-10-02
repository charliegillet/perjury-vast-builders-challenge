"""Fill the pitch's {X} placeholders in docs/slides/*.md from cache/bench_report.json["numbers"].

    python -m bench.fill_numbers [--report cache/bench_report.json] [--out docs/slides/rendered] [--allow-fixture]

"If the repo didn't measure a number, it doesn't go on screen":
- Refuses a report built from fixture/offline runs (exit 2) unless --allow-fixture. With that flag, every filled number
  is stamped "[FIXTURE]".
- A placeholder whose number is missing or null stays visible as {X}. The script lists it and exits 1.
Templates are never modified; rendered copies go to --out. A placeholder is `{Name}` with an identifier inside
(letters, digits, _), so JSON braces in the slides are left alone.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional

from perjury.config import CACHE, ROOT

PLACEHOLDER = re.compile(r"\{([A-Za-z][A-Za-z0-9_]*)\}")
SLIDES = ROOT / "docs" / "slides"


class FixtureRefused(SystemExit):
    pass


def render(text: str, numbers: dict, *, fixture: bool) -> tuple[str, set[str]]:
    missing: set[str] = set()

    def sub(m: re.Match) -> str:
        key = m.group(1)
        v = numbers.get(key)
        if v is None:
            missing.add(key)
            return m.group(0)
        s = f"{v:g}" if isinstance(v, float) else str(v)
        return f"{s} [FIXTURE]" if fixture else s
    return PLACEHOLDER.sub(sub, text), missing


def fill(report: dict, src: Path, out: Path, *, allow_fixture: bool) -> dict[str, set[str]]:
    fixture = bool(report.get("fixture")) or report.get("mode") not in ("live", "empty")
    if fixture and not allow_fixture:
        raise FixtureRefused("REFUSED: bench_report.json was built from FIXTURE/offline runs. These are not pitch "
                             "numbers. Re-run the bench live, or pass --allow-fixture to preview (every number is "
                             "stamped [FIXTURE]).")
    numbers = report.get("numbers") or {}
    out.mkdir(parents=True, exist_ok=True)
    missing: dict[str, set[str]] = {}
    for p in sorted(x for x in src.glob("*.md") if x.name.lower() != "readme.md"):
        text, miss = render(p.read_text(), numbers, fixture=fixture)
        if fixture:
            text = "> **FIXTURE PREVIEW: not measured on the live stack. Do not present.**\n\n" + text
        (out / p.name).write_text(text)
        if miss:
            missing[p.name] = miss
    return missing


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Render slide placeholders from measured bench numbers")
    ap.add_argument("--report", default=str(CACHE / "bench_report.json"))
    ap.add_argument("--src", default=str(SLIDES))
    ap.add_argument("--out", default=str(SLIDES / "rendered"))
    ap.add_argument("--allow-fixture", action="store_true")
    a = ap.parse_args(argv)
    rp = Path(a.report)
    if not rp.exists():
        print(f"[fill] no {rp}: run `python -m bench.report` first", file=sys.stderr)
        return 2
    report = json.loads(rp.read_text())
    try:
        missing = fill(report, Path(a.src), Path(a.out), allow_fixture=a.allow_fixture)
    except FixtureRefused as e:
        print(str(e), file=sys.stderr)
        return 2
    print(f"[fill] rendered {a.src}/*.md -> {a.out} (report {report.get('generated_at')}, mode {report.get('mode')})")
    if missing:
        for name, keys in missing.items():
            print(f"  UNMEASURED in {name}: {', '.join(sorted(keys))}  (left as {{X}}; not on screen until measured)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
