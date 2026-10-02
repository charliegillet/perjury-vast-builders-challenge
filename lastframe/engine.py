"""Video decision rounds. Outcomes stay on the server until an answer is committed."""
from __future__ import annotations

import copy
import math
import secrets
import threading
import time


class InvalidScenario(ValueError):
    pass


def validate_scenario(raw: dict) -> dict:
    if not isinstance(raw, dict):
        raise InvalidScenario("A scenario must be an object.")
    s = copy.deepcopy(raw)
    for key in ("id", "title", "pack", "skill", "question", "context", "outcome", "explanation"):
        if not isinstance(s.get(key), str) or not s[key].strip() or len(s[key]) > 4000:
            raise InvalidScenario(f"{key} must be non-empty text (maximum 4000 characters).")
    if s.get("provenance") not in ("storyboard", "human-reviewed-vss"):
        raise InvalidScenario("Provenance must identify storyboard or human-reviewed-vss evidence.")
    options = s.get("options", [])
    if not isinstance(options, list) or not 2 <= len(options) <= 4:
        raise InvalidScenario("Provide two to four answer options.")
    ids = []
    for option in options:
        if not isinstance(option, dict) or not isinstance(option.get("id"), str) or not isinstance(option.get("text"), str) or not option["text"].strip():
            raise InvalidScenario("Each option needs an id and text.")
        ids.append(option["id"])
    if len(set(ids)) != len(ids) or s.get("answer") not in ids:
        raise InvalidScenario("Option IDs must be unique, and the answer must match one.")
    for key in ("before", "after"):
        clip = s.get(key)
        if not isinstance(clip, dict):
            raise InvalidScenario(f"{key} clip is required.")
        start, end = clip.get("start"), clip.get("end")
        if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in (start, end)) or start < 0 or end <= start:
            raise InvalidScenario("Clip times must be finite, non-negative, and increasing.")
    if s["before"]["end"] > s["after"]["start"]:
        raise InvalidScenario("The observation and continuation must not overlap.")
    evidence = s.get("evidence")
    if not isinstance(evidence, list) or not evidence or len(evidence) > 10:
        raise InvalidScenario("Provide one to ten evidence observations.")
    for item in evidence:
        if not isinstance(item, dict) or not isinstance(item.get("text"), str) or not item["text"].strip():
            raise InvalidScenario("Evidence needs an observation.")
        at = item.get("at")
        if isinstance(at, bool) or not isinstance(at, (int, float)) or not math.isfinite(at) or not s["before"]["start"] <= at <= s["after"]["end"]:
            raise InvalidScenario("Evidence timestamps must be inside the clip window.")
    if s["provenance"] == "human-reviewed-vss":
        if not s.get("reviewed"):
            raise InvalidScenario("Watch both clips and confirm the answer before publishing.")
        for key in ("before", "after"):
            if not isinstance(s[key].get("source"), str) or not s[key]["source"].startswith("s3://"):
                raise InvalidScenario("Live clips need a VSS S3 source.")
        if not s.get("original_video") or s["before"].get("original_video") != s["original_video"] or s["after"].get("original_video") != s["original_video"]:
            raise InvalidScenario("Both clips must belong to the same parent video.")
        if abs(s["after"]["start"] - s["before"]["end"]) > 0.1:
            raise InvalidScenario("Select adjacent clips with no gap at the decision point.")
    return s


def card(s: dict) -> dict:
    return {k: s.get(k) for k in ("id", "title", "pack", "skill", "difficulty", "provenance")}


class RoundStore:
    def __init__(self, scenarios, clock=time.monotonic):
        self.scenarios = {s["id"]: validate_scenario(s) for s in scenarios}
        self.rounds = {}
        self.lock = threading.RLock()
        self.clock = clock

    def start(self, scenario_id):
        with self.lock:
            now = self.clock()
            self.rounds = {k: v for k, v in self.rounds.items() if now - v["created"] < 7200}
            if len(self.rounds) >= 5000:
                raise ValueError("Too many active rounds. Try again later.")
            s = self.scenarios[scenario_id]
            token = secrets.token_urlsafe(24)
            self.rounds[token] = {"scenario": copy.deepcopy(s), "created": now, "result": None}
            observation = {**card(s), **{k: s[k] for k in ("question", "context", "options")}}
            observation["clip"] = {"start": s["before"]["start"], "end": s["before"]["end"], "scene": s["before"].get("scene")}
            observation["clip"]["url"] = f"/api/media/{token}/before" if s["provenance"] == "human-reviewed-vss" else None
            return {"round_id": token, "scenario": observation}

    def get(self, token):
        r = self.rounds[token]
        if self.clock() - r["created"] >= 7200:
            del self.rounds[token]
            raise KeyError(token)
        return r

    def answer(self, token, option_id, confidence):
        with self.lock:
            r = self.get(token)
            s = r["scenario"]
            if option_id not in [o["id"] for o in s["options"]]:
                raise ValueError("Choose an available answer.")
            if isinstance(confidence, bool) or confidence not in (50, 70, 90):
                raise ValueError("Confidence must be 50, 70 or 90.")
            if r["result"]:
                if r["result"]["selected"] != option_id or r["result"]["confidence"] != confidence:
                    raise ValueError("This answer is already committed. Start a new round to try again.")
                return copy.deepcopy(r["result"])
            correct = option_id == s["answer"]
            result = {"selected": option_id, "answer": s["answer"], "correct": correct, "confidence": confidence,
                      "brier": round((confidence / 100 - int(correct)) ** 2, 4),
                      "outcome": s["outcome"], "explanation": s["explanation"], "evidence": s["evidence"],
                      "provenance": s["provenance"], "scenario_id": s["id"], "skill": s["skill"],
                      "clip": {"start": s["after"]["start"], "end": s["after"]["end"], "scene": s["after"].get("scene"),
                               "url": f"/api/media/{token}/after" if s["provenance"] == "human-reviewed-vss" else None}}
            r["result"] = result
            return copy.deepcopy(result)

    def media(self, token, phase):
        with self.lock:
            r = self.get(token)
            if phase not in ("before", "after") or (phase == "after" and not r["result"]):
                raise PermissionError("Commit an answer to unlock the continuation.")
            s = r["scenario"]
            if s["provenance"] != "human-reviewed-vss":
                raise ValueError("Storyboard rounds have no video stream.")
            return s[phase]["source"]
