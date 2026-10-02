"""App routes (BUILD-CONTRACT "App"): health, scene, SSE testify in fixture mode, replay, transcribe, relative URLs."""
from __future__ import annotations

import io
import json
import re
import struct
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

STATIC = Path(__file__).resolve().parent.parent / "app" / "static"


@pytest.fixture()
def client(monkeypatch, tmp_path):
    monkeypatch.setenv("PERJURY_MODE", "fixture")
    monkeypatch.setenv("PERJURY_FIXTURE_LATENCY", "0")
    monkeypatch.setenv("PERJURY_WARM_TILES", "0")
    monkeypatch.setenv("PERJURY_WEAVE", "0")
    monkeypatch.setenv("PERJURY_RUNS_DIR", str(tmp_path / "runs"))
    monkeypatch.delenv("WANDB_API_KEY", raising=False)
    from perjury.config import settings
    settings.cache_clear()
    import app.main as main
    monkeypatch.setattr(main, "CACHE", tmp_path)   # feedback.jsonl, bench/witness lookups stay in tmp
    with TestClient(main.app) as c:
        yield c
    settings.cache_clear()


def sse_events(body: str) -> list[tuple[str, dict]]:
    out = []
    for frame in body.split("\n\n"):
        name = next((l[7:] for l in frame.splitlines() if l.startswith("event: ")), None)
        data = next((l[6:] for l in frame.splitlines() if l.startswith("data: ")), None)
        if name and data:
            out.append((name, json.loads(data)))
    return out


def wav_bytes(seconds: float = 0.2, rate: int = 16000) -> bytes:
    n = int(seconds * rate)
    buf = io.BytesIO()
    buf.write(b"RIFF" + struct.pack("<I", 36 + n * 2) + b"WAVE")
    buf.write(b"fmt " + struct.pack("<IHHIIHH", 16, 1, 1, rate, rate * 2, 2, 16))
    buf.write(b"data" + struct.pack("<I", n * 2) + b"\x00\x00" * n)
    return buf.getvalue()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    h = r.json()
    assert h["ok"] is True and h["mode"] == "fixture"
    assert h["index_segments"] > 0
    for k in ("pod", "probes"):
        assert k in h


def test_index_page_served(client):
    r = client.get("/")
    assert r.status_code == 200 and "PERJURY" in r.text
    assert client.get("/static/app.js").status_code == 200
    assert client.get("/static/wav.js").status_code == 200


def test_scene_2(client):
    r = client.get("/api/scene/2")
    assert r.status_code == 200
    d = r.json()
    assert d["scene"] == 2 and d["label"]
    assert len(d["cameras"]) >= 14
    assert len(d["slots"]) == 18
    assert set(d["t0"]["cameras"]) == set(d["cameras"])
    assert client.get("/api/scene/4").status_code == 422


def test_tile_validation(client):
    assert client.get("/api/tile", params={"scene": 2, "camera": "p9c9"}).status_code == 422
    r = client.get("/api/tile", params={"scene": 2, "camera": "p1c1"})
    assert r.status_code == 200 and r.headers["content-type"] == "image/jpeg"


def test_testify_validation(client):
    assert client.post("/api/testify", json={"text": "x", "scene": 4}).status_code == 422
    assert client.post("/api/testify", json={"text": "x" * 501, "scene": 2}).status_code == 422
    assert client.post("/api/testify", json={"text": "   ", "scene": 2}).status_code == 422


def test_testify_streams_to_done_and_records(client, tmp_path):
    pytest.importorskip("perjury.pipeline")
    pytest.importorskip("perjury.fakes")
    with client.stream("POST", "/api/testify",
                       json={"text": "Three pedestrians are crossing the highway in the snow.", "scene": 2}) as r:
        assert r.status_code == 200
        assert r.headers["content-type"].startswith("text/event-stream")
        body = "".join(r.iter_text())
    evs = sse_events(body)
    names = [n for n, _ in evs]
    assert names[0] == "run" and names[-1] == "done"
    assert "error" not in names, [d for n, d in evs if n == "error"]
    for needed in ("transcript", "atoms", "atom_verdict", "verdict", "receipt"):
        assert needed in names
    verdict = next(d for n, d in evs if n == "verdict")
    assert verdict["verdict"] == "FALSE"
    run_id = evs[0][1]["run_id"]
    assert (tmp_path / "runs" / f"{run_id}.jsonl").exists()

    # exhibit for a juror of the contradicted atom, resolved from the run registry
    av = next(d["atom_verdict"] for n, d in evs if n == "atom_verdict" and d["atom_verdict"]["votes"])
    cam = av["votes"][0]["camera"]
    ex = client.get("/api/exhibit", params={"run_id": run_id, "atom_id": av["atom_id"], "camera": cam})
    assert ex.status_code == 200 and ex.json()["camera"] == cam
    jpg = client.get("/api/exhibit.jpg", params={"run_id": run_id, "atom_id": av["atom_id"], "camera": cam})
    assert jpg.status_code == 200 and jpg.content[:2] == b"\xff\xd8"

    fb = client.post("/api/feedback", json={"run_id": run_id, "thumbs": "down", "note": "test"})
    assert fb.status_code == 200 and fb.json()["ok"]
    row = json.loads((tmp_path / "feedback.jsonl").read_text().splitlines()[-1])
    assert row["run_id"] == run_id and row["verdict"] == "FALSE"


def test_voice_path_counts_canary_only_when_text_unchanged(client):
    pytest.importorskip("perjury.pipeline")
    pytest.importorskip("perjury.fakes")
    assert client.post("/api/transcribe", files={"file": ("x.wav", b"not a wav", "audio/wav")}).status_code == 415
    text = "A pickup is towing a trailer."
    r = client.post("/api/transcribe", files={"file": ("claim.wav", wav_bytes(), "audio/wav")},
                    headers={"X-Fixture-Transcript": text})
    assert r.status_code == 200, r.text
    tr = r.json()
    assert tr["text"] == text and tr["transcript_id"]
    with client.stream("POST", "/api/testify", json={"text": text, "scene": 1, "transcript_source": "canary",
                                                     "transcript_id": tr["transcript_id"]}) as s:
        evs = sse_events("".join(s.iter_text()))
    assert any(n == "service" and d["service"] == "canary" and d["state"] == "done" for n, d in evs)
    # edited text is typed testimony: the Canary chip stays idle (§10 honesty rule)
    with client.stream("POST", "/api/testify", json={"text": text + " Edited.", "scene": 1,
                                                     "transcript_source": "canary",
                                                     "transcript_id": tr["transcript_id"]}) as s:
        evs = sse_events("".join(s.iter_text()))
    assert not any(n == "service" and d["service"] == "canary" for n, d in evs)


def test_replay_reemits_recording(client, tmp_path):
    runs = tmp_path / "runs"
    runs.mkdir(parents=True, exist_ok=True)
    name = "20261002-153500_a-pickup-is-towing-a-trailer_abcd"
    rec = [
        {"event": "run", "t_ms": 0, "data": {"run_id": name, "text": "A pickup is towing a trailer.", "scene": 1,
                                             "mode": "live"}},
        {"event": "verdict", "t_ms": 30, "data": {"verdict": "TRUE", "explanation": "6/6"}},
        {"event": "receipt", "t_ms": 40, "data": {"verdict": "TRUE", "elapsed_ms": 40}},
        {"event": "done", "t_ms": 50, "data": {}},
    ]
    (runs / f"{name}.jsonl").write_text("".join(json.dumps(e) + "\n" for e in rec))
    listing = client.get("/api/replays").json()["replays"]
    item = next(x for x in listing if x["name"] == name)
    assert item["verdict"] == "TRUE" and item["scene"] == 1
    with client.stream("GET", f"/api/replay/{name}", params={"speed": 0}) as r:
        assert r.status_code == 200
        evs = sse_events("".join(r.iter_text()))
    assert [n for n, _ in evs] == ["run", "verdict", "receipt", "done"]
    assert all(d["replay"] is True and d["recorded_at"].startswith("2026-10-02T15:35") for _, d in evs)
    assert [d["_t_ms"] for _, d in evs] == [0, 30, 40, 50]
    assert client.get("/api/replay/nope").status_code == 404
    assert client.get("/api/replay/..%2Fsecrets").status_code in (404, 422)


def test_bench_and_witness_not_run(client):
    assert client.get("/api/bench").json()["status"] == "not_run"
    assert client.get("/api/witness").json()["status"] == "not_run"


def test_ui_uses_relative_urls_only():
    """The Ingress serves the UI at /app/ and strips /app, so a root-relative URL would hit the VSS UI."""
    bad = re.compile(r"""(src|href|action)\s*=\s*["']/(?!/)|fetch\(\s*[`"']/(?!/)|["'`]/api/|EventSource\(\s*[`"']/""")
    for f in ("index.html", "app.js", "wav.js", "style.css"):
        text = (STATIC / f).read_text()
        hits = [m.group(0) for m in bad.finditer(text)]
        assert not hits, f"{f}: root-relative URL(s) {hits}"
    assert "url(/" not in (STATIC / "style.css").read_text()
