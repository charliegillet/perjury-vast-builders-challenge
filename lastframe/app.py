#!/usr/bin/env python3
"""LAST FRAME: a dependency-free local app and workshop video adapter."""
from __future__ import annotations

import argparse
import json
import mimetypes
import os
import re
import secrets
import threading
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from engine import InvalidScenario, RoundStore, card, validate_scenario
from vss import UpstreamError, VSS

ROOT = Path(__file__).resolve().parent


class Application:
    def __init__(self, data_dir=None, vss=None):
        self.data_dir = Path(data_dir or os.getenv("LASTFRAME_DATA_DIR", ROOT / "data"))
        scenarios = json.loads((ROOT / "fixtures.json").read_text())
        saved = self.data_dir / "scenarios.json"
        if saved.exists():
            scenarios.extend(json.loads(saved.read_text()))
        self.store = RoundStore(scenarios)
        self.vss = vss or VSS()
        self.candidates = {}
        self.lock = threading.RLock()

    def publish(self, raw):
        s = validate_scenario(raw)
        if s["provenance"] != "human-reviewed-vss":
            raise InvalidScenario("Studio publishing requires reviewed VSS footage.")
        with self.lock, self.store.lock:
            # Resolve only sources returned by this server, not arbitrary S3 paths.
            for phase in ("before", "after"):
                source = s[phase]["source"]
                known = self.candidates.get(source)
                if not known or any(s[phase].get(k) != known.get(k) for k in ("start", "end", "original_video")):
                    raise InvalidScenario("Search and select these clips in the studio first.")
            if s["id"] in self.store.scenarios:
                raise InvalidScenario("This scenario ID already exists.")
            live = [v for v in self.store.scenarios.values() if v["provenance"] == "human-reviewed-vss"] + [s]
            self.data_dir.mkdir(parents=True, exist_ok=True)
            temp = self.data_dir / ("scenarios-" + secrets.token_hex(6) + ".tmp")
            temp.write_text(json.dumps(live, indent=2))
            temp.replace(self.data_dir / "scenarios.json")
            self.store.scenarios[s["id"]] = s
        return card(s)


def handler_for(app):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            # Avoid logging round capabilities, source URIs or query parameters.
            print(f"[lastframe] {self.command} {urllib.parse.urlparse(self.path).path.split('/')[1:3]} {args[1] if len(args) > 1 else ''}")

        def json_response(self, value, status=200):
            body = json.dumps(value).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def body(self):
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 100_000:
                    raise ValueError("Request must contain at most 100 KB of JSON.")
                data = json.loads(self.rfile.read(length))
                if not isinstance(data, dict):
                    raise ValueError("Request must be a JSON object.")
                return data
            except (json.JSONDecodeError, UnicodeDecodeError) as exc:
                raise ValueError("Invalid JSON request.") from exc

        def do_GET(self):
            self.dispatch("GET")

        def do_POST(self):
            # Local studio is same-origin. Public deployment needs real authentication.
            origin = self.headers.get("Origin")
            if origin and urllib.parse.urlparse(origin).netloc != self.headers.get("Host"):
                return self.json_response({"error": "Cross-origin requests are not allowed."}, 403)
            self.dispatch("POST")

        def dispatch(self, method):
            parsed = urllib.parse.urlparse(self.path)
            path, query = parsed.path, urllib.parse.parse_qs(parsed.query)
            try:
                if method == "GET" and path == "/api/status":
                    return self.json_response({"vss_configured": app.vss.configured,
                                               "drafting_configured": bool(app.vss.env.get("WANDB_API_KEY") and app.vss.env.get("LASTFRAME_WANDB_MODEL")),
                                               "mode": "workshop-configured" if app.vss.configured else "storyboard-demo"})
                if method == "GET" and path == "/api/scenarios":
                    with app.store.lock:
                        return self.json_response([card(s) for s in app.store.scenarios.values()])
                if method == "POST" and path == "/api/rounds":
                    return self.json_response(app.store.start(self.body().get("scenario_id")), 201)
                match = re.fullmatch(r"/api/rounds/([\w-]+)/answer", path)
                if method == "POST" and match:
                    data = self.body()
                    return self.json_response(app.store.answer(match[1], data.get("option_id"), data.get("confidence")))
                match = re.fullmatch(r"/api/media/([\w-]+)/(before|after)", path)
                if method == "GET" and match:
                    return self.stream(app.store.media(match[1], match[2]))
                if method == "POST" and path == "/api/studio/search":
                    text = self.body().get("query")
                    if not isinstance(text, str) or not 3 <= len(text.strip()) <= 500:
                        raise ValueError("Enter a query between 3 and 500 characters.")
                    results = app.vss.search(text)
                    with app.lock:
                        for row in results:
                            if row.get("source"):
                                app.candidates[row["source"]] = row
                    return self.json_response(results)
                if method == "POST" and path == "/api/studio/segments":
                    parent = self.body().get("original_video")
                    with app.lock:
                        if not any(r["original_video"] == parent for r in app.candidates.values()) or not parent:
                            raise ValueError("Select a parent video returned by search.")
                    segments = app.vss.segments(parent)
                    with app.lock:
                        for row in segments:
                            app.candidates[row["source"]] = row
                    return self.json_response(segments)
                if method == "GET" and path == "/api/studio/media":
                    source = query.get("source", [None])[0]
                    with app.lock:
                        if source not in app.candidates:
                            raise ValueError("Select a searched clip first.")
                    return self.stream(source)
                if method == "POST" and path == "/api/studio/draft":
                    data = self.body()
                    with app.lock:
                        before = app.candidates[data.get("before_source")]
                        after = app.candidates[data.get("after_source")]
                    if before["end"] is None or after["start"] is None or before["original_video"] != after["original_video"] or abs(before["end"] - after["start"]) > 0.1:
                        raise ValueError("Choose two adjacent clips from one video.")
                    return self.json_response(app.vss.draft(before, after))
                if method == "POST" and path == "/api/studio/publish":
                    return self.json_response(app.publish(self.body()), 201)
                if path.startswith("/api/"):
                    return self.json_response({"error": "Route not found."}, 404)
                if method != "GET":
                    return self.json_response({"error": "Method not allowed."}, 405)
                return self.static(path)
            except KeyError:
                self.json_response({"error": "Round or selected clip not found. Start again."}, 404)
            except PermissionError as exc:
                self.json_response({"error": str(exc)}, 403)
            except (ValueError, InvalidScenario) as exc:
                self.json_response({"error": str(exc)}, 400)
            except UpstreamError as exc:
                self.json_response({"error": str(exc)}, 502)
            except (BrokenPipeError, ConnectionResetError):
                pass
            except Exception:
                self.json_response({"error": "The request failed. Check the server and retry."}, 500)

        def stream(self, source):
            with app.vss.request("/api/v1/videos/stream", query={"source": source}, stream=True, range_header=self.headers.get("Range")) as response:
                self.send_response(response.status)
                for name in ("Content-Type", "Content-Length", "Content-Range", "Accept-Ranges"):
                    if response.headers.get(name):
                        self.send_header(name, response.headers[name])
                self.send_header("Cache-Control", "private, no-store")
                self.end_headers()
                while chunk := response.read(64 * 1024):
                    self.wfile.write(chunk)

        def static(self, path):
            allowed = {"/": "index.html", "/index.html": "index.html", "/app.js": "app.js", "/style.css": "style.css"}
            if path not in allowed:
                return self.json_response({"error": "File not found."}, 404)
            file = ROOT / "web" / allowed[path]
            body = file.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", mimetypes.guess_type(file.name)[0] + "; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self'; img-src 'self' data:; media-src 'self'; connect-src 'self'; frame-ancestors 'none'")
            self.end_headers()
            self.wfile.write(body)
    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8787)
    args = parser.parse_args()
    app = Application()
    server = ThreadingHTTPServer((args.host, args.port), handler_for(app))
    print(f"LAST FRAME → http://{args.host}:{args.port}")
    print("Workshop configured" if app.vss.configured else "Storyboard demo. No live footage is connected.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()


if __name__ == "__main__":
    main()
