"""Meaningful round-isolation, provenance, persistence and HTTP workflow checks."""
import copy
import io
import json
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import Application, ROOT, handler_for
from engine import InvalidScenario, RoundStore, validate_scenario
from vss import VSS, UpstreamError, normalize, rows

FIXTURES = json.loads((ROOT / "fixtures.json").read_text())


def live_scenario():
    s = copy.deepcopy(FIXTURES[0])
    s.update(id="live-test", provenance="human-reviewed-vss", reviewed=True, original_video="s3://chunks/drive.mp4")
    for key in ("before", "after"):
        s[key].update(source=f"s3://segments/{key}.mp4", original_video=s["original_video"])
    return s


class EngineTests(unittest.TestCase):
    def setUp(self):
        self.store = RoundStore(FIXTURES)

    def test_fixture_integrity(self):
        self.assertEqual(len({s["id"] for s in FIXTURES}), len(FIXTURES))
        for s in FIXTURES:
            validate_scenario(s)

    def test_no_future_in_public_observation(self):
        observation = self.store.start("curbside")
        for key in ("answer", "outcome", "explanation", "after", "evidence"):
            self.assertNotIn(key, observation["scenario"])
        self.assertEqual(observation["scenario"]["clip"]["end"], 5)

    def test_immutable_and_idempotent_answer(self):
        token = self.store.start("curbside")["round_id"]
        first = self.store.answer(token, "b", 90)
        self.assertTrue(first["correct"])
        self.assertEqual(first["brier"], .01)
        self.assertEqual(first, self.store.answer(token, "b", 90))
        with self.assertRaises(ValueError):
            self.store.answer(token, "a", 90)
        first["evidence"][0]["text"] = "modified client copy"
        self.assertNotEqual(first, self.store.answer(token, "b", 90))

    def test_wrong_answer_and_bad_confidence(self):
        token = self.store.start("curbside")["round_id"]
        with self.assertRaises(ValueError):
            self.store.answer(token, "b", True)
        with self.assertRaises(ValueError):
            self.store.answer(token, "missing", 90)
        result = self.store.answer(token, "a", 90)
        self.assertFalse(result["correct"])
        self.assertEqual(result["brier"], .81)

    def test_future_stream_is_locked(self):
        store = RoundStore([live_scenario()])
        token = store.start("live-test")["round_id"]
        with self.assertRaises(PermissionError):
            store.media(token, "after")
        self.assertEqual(store.media(token, "before"), "s3://segments/before.mp4")
        store.answer(token, "b", 70)
        self.assertEqual(store.media(token, "after"), "s3://segments/after.mp4")

    def test_rounds_do_not_share_reveal_state(self):
        store = RoundStore([live_scenario()])
        one = store.start("live-test")["round_id"]
        two = store.start("live-test")["round_id"]
        store.answer(one, "b", 70)
        with self.assertRaises(PermissionError):
            store.media(two, "after")

    def test_concurrent_commit_accepts_only_one_choice(self):
        token = self.store.start("curbside")["round_id"]
        def answer(option):
            try:
                return self.store.answer(token, option, 70)["selected"]
            except ValueError:
                return None
        with ThreadPoolExecutor(2) as pool:
            responses = list(pool.map(answer, ["a", "b"]))
        self.assertEqual(sum(value is not None for value in responses), 1)

    def test_expired_round_is_inaccessible(self):
        now = [0]
        store = RoundStore(FIXTURES, clock=lambda: now[0])
        token = store.start("curbside")["round_id"]
        now[0] = 7201
        with self.assertRaises(KeyError):
            store.answer(token, "b", 70)

    def test_validation_rejects_bad_windows_and_unreviewed_clips(self):
        for mutate in (
            lambda s: s["before"].update(end=float("nan")),
            lambda s: s["after"].update(start=4),
            lambda s: s.update(reviewed=False),
            lambda s: s["after"].update(original_video="different-parent"),
            lambda s: s["after"].update(start=6),
            lambda s: s["evidence"][0].update(at=100),
        ):
            s = live_scenario()
            mutate(s)
            with self.assertRaises(InvalidScenario):
                validate_scenario(s)


class MockStream(io.BytesIO):
    status = 200
    headers = {"Content-Type": "video/mp4", "Content-Length": "10", "Accept-Ranges": "bytes"}


class MockVSS:
    """Deterministic fake, never represented as a live endpoint test."""
    configured = True
    env = {}

    def search(self, query):
        return self.segments("s3://chunks/drive.mp4")

    def segments(self, parent):
        s = live_scenario()
        return [{**s[key], "caption": "Example caption", "camera_id": "mock-camera", "location": "mock-location"} for key in ("before", "after")]

    def request(self, *args, **kwargs):
        return MockStream(b"test-bytes")


class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.app = Application(cls.temp.name, MockVSS())
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), handler_for(cls.app))
        cls.base = "http://127.0.0.1:" + str(cls.server.server_port)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()
        cls.temp.cleanup()

    def request(self, path, body=None, headers=None):
        data = None if body is None else json.dumps(body).encode()
        req = urllib.request.Request(self.base + path, data=data, headers={"Content-Type": "application/json", **(headers or {})})
        try:
            response = urllib.request.urlopen(req, timeout=3)
        except urllib.error.HTTPError as exc:
            response = exc
        with response:
            raw = response.read()
            return response.status, json.loads(raw) if "application/json" in response.headers.get("Content-Type", "") else raw

    def test_catalog_and_static_do_not_expose_answer_keys(self):
        status, catalog = self.request("/api/scenarios")
        self.assertEqual(status, 200)
        self.assertTrue(all("answer" not in card and "evidence" not in card for card in catalog))
        self.assertEqual(self.request("/fixtures.json")[0], 404)
        self.assertEqual(self.request("/../fixtures.json")[0], 404)
        self.assertEqual(self.request("/")[0], 200)

    def test_cross_origin_commit_is_rejected(self):
        self.assertEqual(self.request("/api/rounds", {"scenario_id": "curbside"}, {"Origin": "https://untrusted.example"})[0], 403)

    def test_round_http_lifecycle(self):
        status, observation = self.request("/api/rounds", {"scenario_id": "curbside"})
        self.assertEqual(status, 201)
        token = observation["round_id"]
        status, result = self.request(f"/api/rounds/{token}/answer", {"option_id": "b", "confidence": 70})
        self.assertEqual(status, 200)
        self.assertTrue(result["correct"])
        self.assertEqual(self.request(f"/api/rounds/{token}/answer", {"option_id": "a", "confidence": 70})[0], 400)

    def test_studio_publish_stream_and_reload(self):
        self.assertEqual(self.request("/api/studio/search", {"query": "person at curb"})[0], 200)
        self.assertEqual(self.request("/api/studio/segments", {"original_video": "s3://chunks/drive.mp4"})[0], 200)
        s = live_scenario()
        self.assertEqual(self.request("/api/studio/publish", s)[0], 201)
        self.assertIn(s["id"], Application(self.temp.name, MockVSS()).store.scenarios)
        _, observation = self.request("/api/rounds", {"scenario_id": s["id"]})
        token = observation["round_id"]
        self.assertEqual(self.request(f"/api/media/{token}/after")[0], 403)
        self.assertEqual(self.request(f"/api/media/{token}/before"), (200, b"test-bytes"))
        self.request(f"/api/rounds/{token}/answer", {"option_id": "b", "confidence": 70})
        self.assertEqual(self.request(f"/api/media/{token}/after"), (200, b"test-bytes"))


class AdapterTests(unittest.TestCase):
    def test_documented_response_wrappers_and_timing_aliases(self):
        row = {"source": "s3://segments/clip.mp4", "start_time_sec": "5", "end_time_sec": "10", "reasoning_content": "visible observation"}
        self.assertEqual(normalize(row, "s3://parent")["start"], 5)
        self.assertIsNone(normalize({"start": float("inf")})["start"])
        self.assertEqual(rows({"segments": [row]}), [row])
        with self.assertRaises(UpstreamError):
            rows({"unexpected": [row]})

    def test_draft_setup_never_receives_continuation_caption(self):
        adapter = VSS({"WANDB_API_KEY": "test-not-real", "LASTFRAME_WANDB_MODEL": "test-model"})
        before = {"caption": "BEFORE_ONLY", "start": 0}
        after = {"caption": "SECRET_FUTURE", "start": 5}
        setup = {"options": [{"id": "a", "text": "wait"}, {"id": "b", "text": "cross"}]}
        with patch.object(adapter, "completion", side_effect=[setup, {"answer": "b"}]) as completion:
            adapter.draft(before, after)
        self.assertNotIn("SECRET_FUTURE", completion.call_args_list[0].args[2])
        self.assertIn("SECRET_FUTURE", completion.call_args_list[1].args[2])

    def test_ambiguous_draft_is_not_published(self):
        adapter = VSS({"WANDB_API_KEY": "test-not-real", "LASTFRAME_WANDB_MODEL": "test-model"})
        with patch.object(adapter, "completion", side_effect=[{"options": []}, {"answer": None}]):
            with self.assertRaises(UpstreamError):
                adapter.draft({"caption": "waiting"}, {"caption": "unclear", "start": 5})


if __name__ == "__main__":
    unittest.main()
