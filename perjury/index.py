"""SceneIndex: the per-segment records T0 pushes down over (cache/i24_index.json; fixture twin cache/fixture_i24_index.json).

Shape (docs/BUILD-CONTRACT.md "Index file"): {"version","source","camera_id","scenes":{"1":{label,duration,cameras}},"segments":[Segment]}.
A missing file loads as an empty index so the app still boots (T0 then has nothing to say).
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Optional

from perjury.types import Segment


class SceneIndex:
    def __init__(self, data: Optional[dict] = None):
        data = data or {}
        self.version = data.get("version", 1)
        self.source = data.get("source", "missing")
        self.camera_id = data.get("camera_id", "i24_cam-1")
        self.scene_meta: dict[int, dict] = {int(k): v for k, v in (data.get("scenes") or {}).items()}
        self._segs: list[Segment] = [Segment(**s) for s in data.get("segments", [])]
        self._by_scene: dict[int, list[Segment]] = defaultdict(list)
        self._by_source: dict[str, Segment] = {}
        for s in sorted(self._segs, key=lambda s: (s.scene, s.camera, s.seg)):
            self._by_scene[s.scene].append(s)
            self._by_source[s.source] = s

    @classmethod
    def load(cls, path: Path | str) -> "SceneIndex":
        p = Path(path)
        return cls(json.loads(p.read_text())) if p.exists() else cls()

    def __len__(self) -> int:
        return len(self._segs)

    def scenes(self) -> list[int]:
        return sorted(set(self.scene_meta) | set(self._by_scene))

    def meta(self, scene: int) -> dict:
        return dict(self.scene_meta.get(scene, {}))

    def segments(self, scene: int, camera: Optional[str] = None) -> list[Segment]:
        segs = self._by_scene.get(scene, [])
        return [s for s in segs if s.camera == camera] if camera else list(segs)

    def segment(self, source: str) -> Optional[Segment]:
        return self._by_source.get(source)

    def cameras(self, scene: int) -> list[str]:
        cams = self.scene_meta.get(scene, {}).get("cameras")
        return list(cams) if cams else sorted({s.camera for s in self._by_scene.get(scene, [])})

    def scene_parent(self, scene: int, camera: str) -> Optional[str]:
        segs = self.segments(scene, camera)
        return segs[0].original_video if segs else None

    def captions(self, scene: int) -> list[dict]:
        """Every caption in the scene as T1 snippets: {id, cam, seg, text, source}."""
        return [{"id": f"s{i + 1}", "cam": s.camera, "seg": s.seg, "text": s.caption, "source": s.source}
                for i, s in enumerate(self._by_scene.get(scene, [])) if s.caption]

    def locations(self, scene: int) -> set[str]:
        return {(s.location or "").lower() for s in self._by_scene.get(scene, []) if s.location}

    def camera_ids(self, scene: int) -> set[str]:
        return {s.camera_id for s in self._by_scene.get(scene, [])} or {self.camera_id}
