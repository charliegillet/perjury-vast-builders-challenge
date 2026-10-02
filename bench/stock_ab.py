"""Stock A/B (FINAL-IDEA-v3 §6, §8): the same bench claims through VSS `agent/search-and-answer` with the exact prompt.

    python -m bench.stock_ab [--split dev|test|all] [--concurrency 4]       # -> cache/stock_ab.json
    python -m bench.stock_ab --g2                                           # G2 gate: 10 planted lies -> cache/g2_stock.json

The first token of each answer is classified by regex: TRUE | FALSE | CANNOT TELL; everything else is UNCLASSIFIED
and must be checked by hand by two people. Put the agreed labels in bench/stock_hand_labels.yaml
(`<claim id>: TRUE|FALSE|CANNOT TELL`); they override the regex for those rows.
The stock agent can't scope by scene: the §6 body filters camera_id only, and we keep it that way on purpose.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional

import yaml

from bench.common import load_claims, now_iso
from perjury.config import CACHE, ROOT

HAND_LABELS = ROOT / "bench" / "stock_hand_labels.yaml"
TO_VERDICT = {"TRUE": "TRUE", "FALSE": "FALSE", "CANNOT TELL": "UNPROVEN"}


def classify(answer: Optional[str]) -> str:
    from perjury.probes import classify_stock   # one regex for the app's stock panel and the bench
    return classify_stock(answer)


def prompt_template() -> str:
    from perjury.probes import STOCK_AB_TEMPLATE
    return STOCK_AB_TEMPLATE


def load_hand_labels(path: Path = HAND_LABELS) -> dict[str, str]:
    if not path.exists():
        return {}
    d = yaml.safe_load(path.read_text()) or {}
    return {str(k): str(v).upper() for k, v in d.items()}


async def ask_all(rows: list[dict], camera_id: str, concurrency: int) -> list[dict]:
    from perjury.clients import build_clients
    from perjury.config import Settings
    vss = build_clients(Settings()).vss
    sem = asyncio.Semaphore(max(1, concurrency))
    hand = load_hand_labels()

    async def one(r: dict) -> dict:
        async with sem:
            t0 = time.monotonic()
            out = {k: r[k] for k in ("id", "split", "kind", "scene", "text", "expected_claim")}
            try:
                d = await vss.search_and_answer(r["text"], camera_id)
                answer = d.get("answer") if isinstance(d, dict) else str(d)
                out.update(answer=answer, hits=(d or {}).get("hits"), query=(d or {}).get("query"),
                           latency_ms=(d or {}).get("latency_ms") or int((time.monotonic() - t0) * 1000), error=None)
            except Exception as e:
                out.update(answer=None, hits=None, query=None, latency_ms=int((time.monotonic() - t0) * 1000),
                           error=f"{type(e).__name__}: {e}"[:300])
            out["classification"] = classify(out["answer"]) if out["answer"] is not None else "ERROR"
            out["hand_label"] = hand.get(r["id"])
            label = out["hand_label"] or out["classification"]
            out["verdict"] = TO_VERDICT.get(label)   # None = UNCLASSIFIED/ERROR: excluded until hand-checked
            print(f"  {r['id']} S{r['scene']} {r['kind']:<12} {out['classification']:<13} "
                  f"{(out['answer'] or out['error'] or '')[:80]!r}", flush=True)
            return out
    return list(await asyncio.gather(*(one(r) for r in rows)))


def g2_rows(n: int = 10) -> list[dict]:
    """The first n planted lies (dev first, then test). The stock agent isn't tuned, so this doesn't leak test."""
    return [r for r in load_claims() if r["kind"] == "lie"][:n]


def g2_decision(results: list[dict]) -> dict:
    n = len(results)
    false = sum(1 for r in results if r.get("verdict") == "FALSE")
    unclassified = sum(1 for r in results if r.get("verdict") is None)
    line = ("stock rejects >= 8/10 => pitch 'evidence audit' (same verdict + atoms, exhibits, decline, measured rates)"
            if false >= 8 else "stock rejects < 8/10 => keep the pitch line 'the stock agent believes the lie'")
    return {"n": n, "false": false, "unclassified": unclassified, "pitch": line}


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Stock VSS search-and-answer A/B")
    ap.add_argument("--split", choices=("dev", "test", "all"), default="all")
    ap.add_argument("--g2", action="store_true", help="G2 gate: 10 planted lies, count FALSE")
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--offline", action="store_true", help="fixture fakes (labelled FIXTURE)")
    a = ap.parse_args(argv)
    if a.offline:
        os.environ["PERJURY_MODE"] = "fixture"
        os.environ["PERJURY_WEAVE"] = "0"
    from perjury.config import Settings
    s = Settings()

    rows = g2_rows() if a.g2 else load_claims(split=None if a.split == "all" else a.split)
    print(f"[stock] {'G2' if a.g2 else a.split} · {len(rows)} claims · camera_id={s.camera_id} · mode={s.mode}")
    results = asyncio.run(ask_all(rows, s.camera_id, a.concurrency))
    doc = {"version": 1, "generated_at": now_iso(), "mode": s.mode, "camera_id": s.camera_id,
           "prompt_template": prompt_template(), "results": results}
    if a.g2:
        doc["g2"] = g2_decision(results)
        out = CACHE / "g2_stock.json"
        out.write_text(json.dumps(doc, indent=1))
        g = doc["g2"]
        print(f"[G2] stock answered FALSE on {g['false']}/{g['n']} planted lies "
              f"({g['unclassified']} unclassified: hand-check them)" + (" · FIXTURE" if s.mode != "live" else ""))
        print(f"[G2] {g['pitch']}" + ("" if s.mode == "live" else "  [FIXTURE: not a gate result]"))
        return 0
    g2 = CACHE / "g2_stock.json"
    if g2.exists():
        g2doc = json.loads(g2.read_text())
        if g2doc.get("mode") == s.mode:   # never attach a fixture G2 to a live A/B (or vice versa)
            doc["g2"] = g2doc.get("g2")
    out = CACHE / "stock_ab.json"
    out.write_text(json.dumps(doc, indent=1))
    unc = [r["id"] for r in results if r["verdict"] is None]
    print(f"[stock] wrote {out}" + (f" · hand-check {len(unc)}: {', '.join(unc)}" if unc else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
