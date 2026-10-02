"""Client layer: fixture fakes (deterministic, demo-shaped), model-output parsing, sidecar persistence, and the live
clients' request shapes against an httpx MockTransport (no network)."""
from __future__ import annotations

import asyncio
import json
import os

import httpx
import pytest

os.environ.setdefault("PERJURY_WEAVE", "0")

from perjury import fakes  # noqa: E402
from perjury.clients import HttpBase, ServiceError, build_clients, parse_model_json, strip_think  # noqa: E402
from perjury.config import Settings  # noqa: E402
from perjury.events import EventBus  # noqa: E402
from perjury.probes import PROBES, lead_prompt  # noqa: E402
from perjury.yolo import mp4_dims, peak_counts, persistence, zoom_from_response  # noqa: E402

FIX = {"PERJURY_MODE": "fixture", "PERJURY_FIXTURE_LATENCY": "0", "PERJURY_WEAVE": "0"}
TOW_TIMES = [0.6, 1.8, 3.0, 4.2]


def run(coro):
    return asyncio.run(coro)


@pytest.fixture(scope="module")
def c():
    return build_clients(Settings(FIX))


def segs(scene: int) -> list[dict]:
    return [x for x in fakes.load_index()["segments"] if x["scene"] == scene]


async def tow_probe(c, source: str):
    grid = c.media.grid2x2(await c.media.keyframes(source, TOW_TIMES))
    return await c.cosmos.probe(grid, PROBES["P-TOW"].prompt, PROBES["P-TOW"].version)


def yes_panels(parsed: dict) -> list[int]:
    return [p["panel"] for p in parsed["panels"] if p["towing"]]


# ---- fakes ----
def test_build_clients_fixture_is_fakes(c):
    assert c.mode == "fixture"
    assert isinstance(c.cosmos, fakes.FakeCosmos) and isinstance(c.media, fakes.FakeMedia)


def test_fake_ptow_yes_on_scene1_towing_truth_panels(c):
    truth = fakes.load_truth()["towing"]
    src = next(k for k in truth if "scene1_" in k)
    r = run(tow_probe(c, src))
    assert r.error is None and not r.cached
    assert yes_panels(r.parsed) == truth[src]["panels"]
    assert r.parsed["panels"][truth[src]["panels"][0] - 1]["towing"][0]["towing_vehicle"] == "pickup"


def test_fake_ptow_no_on_scene2_and_rate_is_low(c):
    s2 = segs(2)
    clean = next(x["source"] for x in s2 if fakes.false_yes_panel(x["source"]) is None)
    assert yes_panels(run(tow_probe(c, clean)).parsed) == []

    async def all_s2():
        return [await tow_probe(c, x["source"]) for x in s2]
    res = run(all_s2())
    yes = sum(bool(yes_panels(r.parsed)) for r in res)
    assert 0 < yes / len(s2) < 0.12          # ~5% hallucination per juror, never on most of Scene 2


def test_fakes_deterministic(c):
    src = segs(1)[3]["source"]
    a, b = run(tow_probe(c, src)), run(tow_probe(c, src))
    assert a.parsed == b.parsed and a.image_sha == b.image_sha
    assert run(c.media.keyframes(src, [1.0])) == run(c.media.keyframes(src, [1.0]))


def test_fake_pcond_and_pcount(c):
    src = segs(2)[0]["original_video"]
    grid = c.media.grid2x2(run(c.media.keyframes(src, [6.0, 21.0, 36.0, 51.0])))
    cond = run(c.cosmos.probe(grid, PROBES["P-COND"].prompt, PROBES["P-COND"].version)).parsed
    assert cond["road"] in ("C", "D") and cond["light"] == "A"
    cnt = run(c.cosmos.probe(grid, PROBES["P-COUNT"].prompt, PROBES["P-COUNT"].version)).parsed
    assert [p["people_on_foot"] for p in cnt["panels"]] == [0, 0, 0, 0]


def test_fake_plead_sycophancy_rate(c):
    async def go():
        out = []
        for x in segs(2)[::4]:
            grid = c.media.grid2x2(await c.media.keyframes(x["source"], TOW_TIMES))
            r = await c.cosmos.probe(grid, lead_prompt("A pickup is towing a trailer"), PROBES["P-LEAD"].version)
            out.append(r.parsed["witness_correct"])
        return out
    v = run(go())
    assert 0.4 <= sum(v) / len(v) <= 0.8      # agrees with the lie ~60% regardless of pixels


def test_fake_untagged_image_abstains(c):
    from perjury.media import grid2x2
    r = run(c.cosmos.probe(grid2x2([]), PROBES["P-TOW"].prompt, "P-TOW v1"))
    assert r.parsed is None and "untagged" in r.error


def test_fake_ground_and_zoom_ok_on_truth(c):
    from perjury.cosmos import xyxy1000_to_pixels
    truth = fakes.load_truth()["towing"]
    src = next(k for k in truth if "scene1_" in k)
    t = TOW_TIMES[truth[src]["panels"][0] - 1]
    frame = run(c.media.keyframes(src, [t]))[0]
    box = run(c.cosmos.probe(frame, PROBES["P-GROUND"].prompt, PROBES["P-GROUND"].version)).parsed["bbox_2d"]
    assert len(box) == 4 and box[2] > box[0] and box[3] > box[1]
    crop = run(c.media.crop_clip(src, t, xyxy1000_to_pixels(box, 3840, 2160)))
    z = run(c.yolo.zoom_check(crop, None))
    assert z.ok and z.label in ("car", "truck") and z.frames_ok >= 2


def test_fake_zoom_fails_on_clean_scene2_and_half_of_false_yes(c):
    clean = next(x["source"] for x in segs(2) if fakes.false_yes_panel(x["source"]) is None)
    crop = run(c.media.crop_clip(clean, 1.8, (100, 100, 400, 300)))
    assert not run(c.yolo.zoom_check(crop, None)).ok
    fy = [x["source"] for x in fakes.load_index()["segments"] if fakes.false_yes_panel(x["source"])]
    passed = sum(fakes.zoom_passes(s) for s in fy)
    assert 0 < passed < len(fy)


def test_fake_embed_ranks_towing_truth_first(c):
    from perjury.embed import cosine
    q = run(c.embed.embed_text("a pickup towing a trailer"))
    vis = c.embed.visual_vectors()
    assert len(q) == 256 and len(vis) == 690
    s1 = [x["source"] for x in segs(1)]
    top = sorted(s1, key=lambda s: -cosine(q, vis[s]))[:6]
    assert all(fakes.tow_truth(s) for s in top)
    assert run(c.embed.embed_text("x")) == run(c.embed.embed_text("x"))


def test_fake_llm_atomizer_raises_and_t1_is_contradiction_first(c):
    from perjury.probes import ATOMIZER_SYSTEM, T1_SYSTEM, atomizer_user, t1_user
    with pytest.raises(ServiceError):
        run(c.llm.complete_json(ATOMIZER_SYSTEM, atomizer_user("A pickup is towing a trailer"), purpose="atomize"))
    snips = [{"id": "s1", "cam": "p1c1", "seg": 0, "text": "Dry highway in daylight with free-flowing traffic."},
             {"id": "s2", "cam": "p1c2", "seg": 1, "text": "Snow and slush beside the roadway; cars proceed slowly."},
             {"id": "s3", "cam": "p1c3", "seg": 2, "text": "Overhead view of a busy interstate."}]
    out = run(c.llm.complete_json(T1_SYSTEM, t1_user("snow on the road", snips), purpose="t1"))
    labels = {x["id"]: x for x in out["labels"]}
    assert [labels[k]["label"] for k in ("s1", "s2", "s3")] == ["CONTRADICTS", "SUPPORTS", "SILENT"]
    for k in ("s1", "s2"):
        text = next(s["text"] for s in snips if s["id"] == k)
        assert labels[k]["quote"] in text and len(labels[k]["quote"].split()) <= 12


def test_fake_canary_vss_and_ribbon(c):
    bus = EventBus("t")
    out = run(c.canary.transcribe(b"RIFF....WAVE X-Fixture-Transcript: It is snowing\n", bus=bus))
    assert out["text"] == "It is snowing" and out["model_id"]
    assert run(c.canary.transcribe(b"RIFF"))["text"] == fakes.FakeCanary.DEFAULT
    states = [e["data"]["state"] for e in bus.events if e["event"] == "service"]
    assert states == ["firing", "done"] and bus.events[-1]["data"]["note"] == "FIXTURE"
    sa = run(c.vss.search_and_answer("A pickup is towing a trailer", "i24_cam-1"))
    assert sa["classification"] in ("TRUE", "FALSE", "CANNOT TELL") and "TRUE, FALSE or CANNOT TELL" in sa["query"]
    parent = segs(2)[0]["original_video"]
    syn = run(c.vss.synthesize(parent))
    assert syn["answer"].startswith("## Overview") and syn["segment_count"] == len([x for x in segs(2)
                                                                                     if x["original_video"] == parent])
    sc = run(c.vss.detections(segs(1)[0]["source"]))
    assert sc["video_shape"][:2] == [2160, 3840] and sc["frames"]
    assert run(c.vss.upload(b"mp4", "x.mp4", {"tags": ["a"]}))["success"]


def test_fake_latency_respected():
    c = build_clients(Settings({**FIX, "PERJURY_FIXTURE_LATENCY": "0.01"}))
    src = segs(1)[0]["source"]
    grid = c.media.grid2x2(run(c.media.keyframes(src, TOW_TIMES)))
    r = run(c.cosmos.probe(grid, PROBES["P-TOW"].prompt, "P-TOW v1"))
    assert 2500 <= r.latency_ms <= 6000


# ---- parsing ----
def test_parse_model_json_think_fence_and_repair():
    assert parse_model_json('<think>\npanel 1 has {a trailer}\n</think>\n```json\n{"road":"C","traffic":"B",}\n```') \
        == {"road": "C", "traffic": "B"}
    assert parse_model_json('reasoning here...</think>{"witness_correct": True}') == {"witness_correct": True}
    assert parse_model_json('Sure: {"bbox_2d": null} hope that helps') == {"bbox_2d": None}
    assert strip_think("<think>unfinished") == ""
    with pytest.raises(ValueError):
        parse_model_json("<think>ran out of tokens")
    with pytest.raises(ValueError):
        parse_model_json("[1, 2]")


def test_bbox_helpers():
    from perjury.cosmos import normalize_xyxy, xyxy1000_to_pixels, xyxy_to_box2d
    assert normalize_xyxy([512, 256, 1024, 768], scale=1024) == [500, 250, 1000, 750]
    assert normalize_xyxy([300, 400, 100, 200]) == [100, 200, 300, 400]
    assert normalize_xyxy(None) is None and normalize_xyxy([1, 1, 1, 1]) is None
    assert xyxy1000_to_pixels([250, 500, 500, 1000], 3840, 2160) == (960, 1080, 1920, 2160)
    assert xyxy_to_box2d([100, 200, 300, 400]) == [200, 100, 400, 300]


# ---- YOLO sidecars ----
SIDECAR = {"video_shape": [2160, 3840, 3], "frames": [
    {"time_sec": 0.0, "detections": [{"label": "car", "bbox": [0, 0, 10, 10], "conf": 0.9},
                                     {"label": "car", "bbox": [20, 0, 30, 10], "conf": 0.8}]},
    {"time_sec": 0.1, "detections": [{"label": "person", "bbox": [0, 0, 5, 9], "conf": 0.4},
                                     {"label": "car", "bbox": [0, 0, 10, 10], "conf": 0.9}]},
    {"time_sec": 0.2, "detections": [{"label": "person", "bbox": [0, 0, 5, 9], "conf": 0.4}]},
    {"time_sec": 0.3, "detections": [{"label": "car", "bbox": [0, 0, 10, 10], "conf": 0.9}]},
    {"time_sec": 0.4, "detections": [{"label": "car", "bbox": [0, 0, 10, 10], "conf": 0.9},
                                     {"label": "person", "bbox": [0, 0, 5, 9], "conf": 0.3}]},
]}


def test_sidecar_persistence_and_peaks():
    assert persistence(SIDECAR) == {"car": 2, "person": 2}
    assert persistence({"frames": list(reversed(SIDECAR["frames"]))}) == {"car": 2, "person": 2}  # sorted by time
    assert persistence(SIDECAR, min_conf=0.35) == {"car": 2, "person": 2}
    assert persistence(SIDECAR, min_conf=0.5) == {"car": 2}
    assert peak_counts(SIDECAR) == {"car": 2, "person": 1}
    assert persistence(None) == {} and peak_counts({"object_counts": '{"truck": 3}'}) == {"truck": 3}


def test_zoom_rule_cover_and_frames():
    big = {"label": "truck", "bbox": [0, 0, 400, 400], "conf": 0.7}       # 160000 / (640*480) = 52 %
    small = {"label": "car", "bbox": [0, 0, 100, 100], "conf": 0.9}       # 3 %
    resp = {"video_shape": [480, 640, 3], "frames": [{"detections": [big]}, {"detections": [small]},
                                                     {"detections": [big, small]}]}
    z = zoom_from_response(resp)
    assert z.ok and z.frames_ok == 2 and z.label == "truck" and z.cover == pytest.approx(0.521, abs=0.001)
    assert not zoom_from_response({**resp, "frames": resp["frames"][:2]}).ok
    one = {"video_shape": [480, 640], "frames": [{"detections": [big]}]}
    assert zoom_from_response(one).ok                      # a 1-frame response needs only that frame
    person = {"video_shape": [480, 640], "frames": [{"detections": [{**big, "label": "person"}]}] * 3}
    assert not zoom_from_response(person).ok
    assert zoom_from_response({"frames": []}).error


# ---- live clients against a mock transport ----
LIVE = {"PERJURY_MODE": "live", "PERJURY_WEAVE": "0", "GPU_BEARER_TOKEN": "tok-secret",
        "COSMOS3_REASON_URL": "http://gpu:8001", "YOLO_URL": "http://gpu:8002", "COSMOS_EMBED1_URL": "http://gpu:8003",
        "CANARY_1B_URL": "http://gpu:8004", "WANDB_API_KEY": "wb-secret", "VSS_URL": "http://vss",
        "VSS_USERNAME": "u", "VSS_PASSWORD": "p"}


@pytest.fixture
def mock(monkeypatch):
    calls: list[httpx.Request] = []
    routes: dict = {}

    def handler(req: httpx.Request) -> httpx.Response:
        calls.append(req)
        fn = routes.get((req.method, req.url.path))
        return fn(req) if fn else httpx.Response(404, text="no route")

    monkeypatch.setattr(HttpBase, "http", lambda self: httpx.AsyncClient(transport=httpx.MockTransport(handler)))
    return calls, routes


def test_live_cosmos_body_cache_and_think(mock, tmp_path):
    from perjury.cosmos import Cosmos, ProbeCache
    calls, routes = mock
    routes[("POST", "/v1/chat/completions")] = lambda r: httpx.Response(200, json={"choices": [{"message": {
        "content": '<think>hmm</think>```json\n{"road":"C","traffic":"B","light":"A"}\n```'}}]})
    cos = Cosmos(Settings(LIVE), cache=ProbeCache(tmp_path))
    bus = EventBus("t")
    r1 = run(cos.probe(b"\xff\xd8jpeg", "PROMPT", "P-COND v1", timeout_s=5, bus=bus))
    assert r1.parsed == {"road": "C", "traffic": "B", "light": "A"} and not r1.cached
    body = json.loads(calls[0].content)
    assert body["temperature"] == 0 and body["max_tokens"] == 512 and "chat_template_kwargs" not in body
    img = body["messages"][0]["content"][0]
    assert img["type"] == "image_url" and img["image_url"]["url"].startswith("data:image/jpeg;base64,")
    assert calls[0].headers["authorization"] == "Bearer tok-secret"
    done = [e["data"] for e in bus.events if e["data"].get("state") == "done"][0]
    assert "tok-secret" not in json.dumps(bus.events) and bus.gpu_ms >= 0 and done["note"] == "P-COND v1"
    r2 = run(cos.probe(b"\xff\xd8jpeg", "PROMPT", "P-COND v1", timeout_s=5))
    assert r2.cached and r2.parsed == r1.parsed and len(calls) == 1 and len(r2.cached_at) == 5
    run(cos.probe(b"\xff\xd8jpeg", "PROMPT v2", "P-COND v1", timeout_s=5))   # prompt change => cache miss
    assert len(calls) == 2


def test_live_cosmos_errors_abstain(mock, tmp_path):
    from perjury.cosmos import Cosmos, ProbeCache
    calls, routes = mock
    routes[("POST", "/v1/chat/completions")] = lambda r: httpx.Response(200, json={"choices": [{"message": {
        "content": "<think>never closed"}}]})
    cos = Cosmos(Settings({**LIVE, "PERJURY_COSMOS_NO_THINK": "1"}), cache=ProbeCache(tmp_path))
    r = run(cos.probe(b"x", "P", "P-TOW v1", timeout_s=5))
    assert r.parsed is None and r.error.startswith("invalid_json")
    assert json.loads(calls[0].content)["chat_template_kwargs"] == {"enable_thinking": False}
    routes[("POST", "/v1/chat/completions")] = lambda r: httpx.Response(503, text="busy")
    r = run(cos.probe(b"y", "P", "P-TOW v1", timeout_s=5))
    assert r.parsed is None and "503" in r.error
    assert not list(tmp_path.glob("*.json"))     # failures are never cached


def test_live_llm_retries_429_then_parses(mock):
    from perjury.llm import LLM
    calls, routes = mock
    seq = iter([httpx.Response(429, headers={"retry-after": "0"}),
                httpx.Response(200, json={"choices": [{"message": {"content": '```json\n{"atoms": []}\n```'}}]})])
    routes[("POST", "/chat/completions")] = lambda r: next(seq)
    llm = LLM(Settings({**LIVE, "WANDB_BASE_URL": "http://wb"}))
    assert run(llm.complete_json("sys", "user", purpose="atomize")) == {"atoms": []}
    assert len(calls) == 2 and json.loads(calls[0].content)["response_format"] == {"type": "json_object"}


def test_live_canary_variants(mock):
    from perjury.canary import Canary
    calls, routes = mock

    def tr(req):
        body = req.content.decode(errors="replace")
        if 'name="model"\r\n\r\nnvidia/canary-1b' in body:
            return httpx.Response(422, text="unknown model")
        return httpx.Response(200, json={"text": "A pickup is towing a trailer."})
    routes[("POST", "/v1/audio/transcriptions")] = tr
    can = Canary(Settings(LIVE))
    out = run(can.transcribe(b"RIFFwav"))
    assert out["text"].startswith("A pickup") and out["model_id"] == "(default)" and len(calls) == 2
    run(can.transcribe(b"RIFFwav"))
    assert len(calls) == 3          # the working variant is cached


def test_live_vss_relogin_and_stock_body(mock):
    from perjury.vss import VSSClient
    calls, routes = mock
    tokens = iter(["t1", "t2"])
    routes[("POST", "/api/v1/auth/login")] = lambda r: httpx.Response(200, json={"access_token": next(tokens)})
    routes[("POST", "/api/v1/agent/search-and-answer")] = lambda r: (
        httpx.Response(401) if r.headers["authorization"] == "Bearer t1" else
        httpx.Response(200, json={"answer": "TRUE. Trailers are visible.", "evidence": {"chunks": [{"a": 1}] * 3}}))
    v = VSSClient(Settings(LIVE))
    out = run(v.search_and_answer("A pickup is towing a trailer", "i24_cam-1"))
    assert out["classification"] == "TRUE" and out["hits"] == 3
    body = json.loads(calls[-1].content)
    assert body == {"query": "Is this statement about the footage true: 'A pickup is towing a trailer'? Start your "
                             "answer with TRUE, FALSE or CANNOT TELL, then one sentence.",
                    "metadata_filters": {"camera_id": "i24_cam-1"}, "top_k": 10, "min_similarity": 0.1}
    routes[("GET", "/api/v1/videos/detections")] = lambda r: httpx.Response(404)
    assert run(v.detections("s3://x/y.mp4")) is None


def test_live_yolo_url_then_b64_fallback(mock):
    from perjury.yolo import Yolo
    calls, routes = mock

    def infer(req):
        b = json.loads(req.content)
        if "url" in b:
            return httpx.Response(400, text="cannot fetch url")
        return httpx.Response(200, json={"video_shape": [480, 640, 3], "frames": [
            {"detections": [{"label": "truck", "bbox": [0, 0, 400, 400], "conf": 0.7}]}] * 3})
    routes[("POST", "/v1/infer")] = infer
    z = run(Yolo(Settings(LIVE)).zoom_check(b"mp4bytes", "http://s3/crop.mp4"))
    assert z.ok and len(calls) == 2 and json.loads(calls[1].content)["include_frames"] is True


def test_mp4_dims_none_on_garbage():
    assert mp4_dims(b"not an mp4") is None and mp4_dims(None) is None
