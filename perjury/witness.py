"""Witness stand (§6, §8): VSS videos/synthesize on N scene parents; every summary sentence is put on trial through the
same atomizer -> router -> quorum path (perjury.pipeline, imported lazily) -> cache/witness.json.

    python -m perjury.witness [--parents 9] [--per-scene 3]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
import uuid
from datetime import datetime
from pathlib import Path

from perjury.config import CACHE, settings
from perjury.events import EventBus

_TS = re.compile(r"^\s*(?:[-*•]\s*)?(?:\[?\d{1,2}:\d{2}(?::\d{2})?\s*(?:[-–—]\s*\d{1,2}:\d{2}(?::\d{2})?)?\]?\s*[:\-–—]?\s*)?")


def split_sentences(answer: str, min_words: int = 3) -> list[str]:
    """Markdown summary -> claim sentences (headings, bullets, timestamps and emphasis stripped)."""
    out = []
    for line in (answer or "").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or set(line) <= set("-=*_|"):
            continue
        line = _TS.sub("", line).replace("**", "").replace("__", "").strip()
        for sent in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])", line):
            sent = sent.strip().strip("*").strip()
            if len(sent.split()) >= min_words:
                out.append(sent)
    return out


def pick_parents(index: dict, n: int, per_scene: int) -> list[dict]:
    """Up to per_scene cameras per scene (spread across poles), n parents total."""
    out = []
    for sc, meta in sorted(index["scenes"].items(), key=lambda kv: int(kv[0])):
        cams = meta["cameras"]
        step = max(1, len(cams) // per_scene)
        for cam in cams[::step][:per_scene]:
            seg = next((s for s in index["segments"] if s["scene"] == int(sc) and s["camera"] == cam), None)
            if seg:
                out.append({"scene": int(sc), "camera": cam, "original_video": seg["original_video"]})
    return out[:n]


async def _verify(sentence: str, scene: int, ctx) -> dict:
    from perjury import pipeline
    bus = EventBus(f"witness-{uuid.uuid4().hex[:8]}")
    v = await pipeline.testify(sentence, scene, ctx, bus, transcript_source="typed")
    d = v.model_dump(mode="json") if hasattr(v, "model_dump") else dict(v)
    return {"text": sentence, "verdict": d.get("verdict"), "explanation": d.get("explanation"),
            "run_id": d.get("run_id"), "atoms": d.get("atoms"), "atom_verdicts": d.get("atom_verdicts"),
            "parser": d.get("parser")}


async def run(n: int = 9, per_scene: int = 3, out: Path | None = None, ctx=None) -> dict:
    """ctx: an existing pipeline Context (the app passes its own); built from settings() when None."""
    from perjury import pipeline
    ctx = ctx or pipeline.load_context(settings())
    s = ctx.settings
    clients = ctx.clients
    index = json.loads(s.index_path.read_text())
    parents = pick_parents(index, n, per_scene)
    result = {"version": 1, "mode": "live" if s.mode == "live" else "fixture",
              "ran_at": datetime.now().astimezone().isoformat(timespec="seconds"), "parents": []}
    for p in parents:
        rec = {**p, "who": "videos/synthesize", "question": "Summarize what happens in this video"}
        try:
            syn = await clients.vss.synthesize(p["original_video"], rec["question"], 20)
            rec["answer"] = (syn or {}).get("answer") or (syn or {}).get("llm_synthesis") or ""
        except Exception as e:
            rec["error"] = f"synthesize: {type(e).__name__}: {str(e)[:160]}"
            result["parents"].append(rec)
            print(f"[witness] {p['original_video']}: {rec['error']}", file=sys.stderr)
            continue
        rec["sentences"] = []
        for sent in split_sentences(rec["answer"]):
            try:
                rec["sentences"].append(await _verify(sent, p["scene"], ctx))
            except Exception as e:
                rec["sentences"].append({"text": sent, "verdict": None, "error": f"{type(e).__name__}: {str(e)[:160]}"})
        result["parents"].append(rec)
    sents = [x for p in result["parents"] for x in p.get("sentences", [])]
    result["summary"] = {"parents": len(result["parents"]), "sentences": len(sents),
                         **{k: sum(x.get("verdict") == k for x in sents) for k in ("TRUE", "FALSE", "UNPROVEN")},
                         "errors": sum(1 for x in sents if x.get("error"))}
    out = out or CACHE / "witness.json"
    out.write_text(json.dumps(result, indent=1))
    print(f"witness: {result['summary']} -> {out}")
    return result


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description="VSS summaries on the witness stand")
    ap.add_argument("--parents", type=int, default=9)
    ap.add_argument("--per-scene", type=int, default=3)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args(argv)
    asyncio.run(run(a.parents, a.per_scene, a.out))


if __name__ == "__main__":
    main()
