"""Verdict rows: VastDB table perjury_verdicts when writable ([A], PERJURY_VASTDB_VERDICTS=1 + vastdb SDK), else
cache/verdicts.jsonl. append_verdict() never raises: a storage problem must not break a verdict.
"""
from __future__ import annotations

import asyncio
import json
from datetime import datetime
from typing import Any

from perjury.config import CACHE, Settings, settings

TABLE = "perjury_verdicts"
JSONL = CACHE / "verdicts.jsonl"
_vastdb_ok: bool | None = None   # None = untried; False after the first failure (stay on JSONL)


def verdict_row(v: Any) -> dict:
    d = v.model_dump(mode="json") if hasattr(v, "model_dump") else dict(v)
    return {"run_id": str(d.get("run_id", "")), "ts": datetime.now().astimezone().isoformat(timespec="seconds"),
            "text": str(d.get("text", "")), "scene": int(d.get("scene") or 0), "verdict": str(d.get("verdict", "")),
            "explanation": str(d.get("explanation", "")), "mode": str(d.get("mode", "")),
            "parser": str(d.get("parser", "")), "elapsed_ms": int(d.get("elapsed_ms") or 0),
            "gpu_s": float(d.get("gpu_s") or 0.0), "calls": int(d.get("calls") or 0),
            "atoms_json": json.dumps(d.get("atoms") or []), "atom_verdicts_json": json.dumps(d.get("atom_verdicts") or [])}


def _write_vastdb(row: dict, s: Settings) -> None:
    import pyarrow as pa  # noqa: WPS433  (VM only: requirements-vm.txt)
    import vastdb  # noqa: WPS433
    schema = pa.schema([(k, pa.int64() if isinstance(v, int) else pa.float64() if isinstance(v, float) else pa.utf8())
                        for k, v in row.items()])
    ep = s.vdb_endpoint if "://" in s.vdb_endpoint else f"http://{s.vdb_endpoint}"
    session = vastdb.connect(endpoint=ep, access=s.s3_access, secret=s.s3_secret, ssl_verify=False)
    with session.transaction() as tx:
        sch = tx.bucket(s.vdb_bucket).schema(s.vdb_schema)
        table = sch.table(TABLE, fail_if_missing=False) or sch.create_table(TABLE, schema)
        table.insert(pa.record_batch([[row[k]] for k in schema.names], schema=schema))


def append_verdict(v: Any, s: Settings | None = None) -> str:
    """Returns where the row went: "vastdb" | "jsonl" | "none"."""
    global _vastdb_ok
    s = s or settings()
    row = verdict_row(v)
    if s.mode == "live" and s.env.get("PERJURY_VASTDB_VERDICTS") == "1" and _vastdb_ok is not False:
        try:
            _write_vastdb(row, s)
            _vastdb_ok = True
            return "vastdb"
        except Exception as e:
            _vastdb_ok = False
            print(f"[perjury] {TABLE} not writable ({type(e).__name__}); using {JSONL.name}")
    try:
        JSONL.parent.mkdir(parents=True, exist_ok=True)
        with JSONL.open("a") as f:
            f.write(json.dumps(row) + "\n")
        return "jsonl"
    except OSError:
        return "none"


async def append_verdict_async(v: Any, s: Settings | None = None) -> str:
    return await asyncio.to_thread(append_verdict, v, s)
