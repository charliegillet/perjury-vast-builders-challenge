"""Media: 2x2 grid geometry + burned-in panel numbers, ffmpeg keyframes / crops on a tiny generated mp4 (bundled
imageio-ffmpeg binary), SigV4 presign (AWS documented test vector), and base64/secret redaction on the ribbon."""
from __future__ import annotations

import asyncio
import io
import json
import os
import subprocess
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlsplit

import pytest
from PIL import Image

os.environ.setdefault("PERJURY_WEAVE", "0")

from perjury.clients import ribbon  # noqa: E402
from perjury.config import Settings  # noqa: E402
from perjury.events import EventBus  # noqa: E402
from perjury.media import Media, draw_boxes, ffmpeg_exe, grid2x2, presign_s3, stills_to_mp4, to_jpeg  # noqa: E402
from perjury.obs import redact  # noqa: E402
from perjury.yolo import mp4_dims  # noqa: E402


def solid(color, size=(1920, 1080)) -> bytes:
    return to_jpeg(Image.new("RGB", size, color))


def test_grid2x2_dims_and_panel_numbers():
    jpg = grid2x2([solid((90, 90, 90))] * 4, labels=["t=6s", "t=21s", "t=36s", "t=51s"])
    im = Image.open(io.BytesIO(jpg)).convert("L")
    assert im.size == (1920, 1080)
    for x0, y0 in ((0, 0), (960, 0), (0, 540), (960, 540)):
        badge = im.crop((x0 + 14, y0 + 14, x0 + 94, y0 + 104))
        lo, hi = badge.getextrema()
        assert lo < 30 and hi > 220                    # black badge with a white digit burned in
        assert 70 < im.getpixel((x0 + 480, y0 + 270)) < 110   # frame content in the panel centre


def test_grid2x2_digits_differ_and_missing_panels_ok():
    im = Image.open(io.BytesIO(grid2x2([solid((90, 90, 90))]))).convert("L")
    badges = [im.crop((x0 + 14, y0 + 14, x0 + 94, y0 + 104)).tobytes()
              for x0, y0 in ((0, 0), (960, 0), (0, 540), (960, 540))]
    assert len(set(badges)) == 4                       # "1".."4" are distinct glyphs
    assert im.getpixel((1440, 810)) < 30               # absent panel stays dark


def test_draw_boxes_keeps_size():
    out = Image.open(io.BytesIO(draw_boxes(solid((0, 0, 0), (640, 360)),
                                           [{"xyxy1000": [100, 100, 500, 500], "label": "juror p1c1"}], "Exhibit A")))
    assert out.size == (640, 360) and out.getpixel((64, 36))[0] > 200   # box corner painted


@pytest.fixture(scope="module")
def tiny_mp4(tmp_path_factory):
    p = tmp_path_factory.mktemp("media") / "tiny.mp4"
    subprocess.run([ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-f", "lavfi", "-i",
                    "testsrc=duration=2:size=640x360:rate=10", "-pix_fmt", "yuv420p", "-c:v", "libx264", "-y", str(p)],
                   check=True, timeout=60)
    return str(p)


def test_keyframes_on_tiny_mp4(tiny_mp4):
    m = Media(Settings({"PERJURY_MODE": "live"}))
    frames = asyncio.run(m.keyframes(tiny_mp4, [0.2, 1.5], width=320))
    assert len(frames) == 2 and frames[0] != frames[1]
    assert all(Image.open(io.BytesIO(f)).size == (320, 180) for f in frames)
    grid = Image.open(io.BytesIO(m.grid2x2(frames * 2)))
    assert grid.size == (1920, 1080)


def test_crop_clip_and_reel_are_mp4(tiny_mp4):
    m = Media(Settings({"PERJURY_MODE": "live"}))
    clip = asyncio.run(m.crop_clip(tiny_mp4, 0.5, (100, 50, 300, 150), dur=0.5))
    assert clip[4:8] == b"ftyp"
    w, h = mp4_dims(clip)
    assert max(w, h) == 640 and w > h                  # longer side scaled to 640 for YOLO
    reel = asyncio.run(stills_to_mp4([solid((200, 0, 0), (640, 360)), solid((0, 200, 0), (640, 360))],
                                     seconds_each=0.5, width=320))
    assert reel[4:8] == b"ftyp" and mp4_dims(reel)[0] == 320


def test_keyframe_failure_raises(tmp_path):
    from perjury.media import MediaError
    m = Media(Settings({"PERJURY_MODE": "live"}))
    with pytest.raises(MediaError):
        asyncio.run(m.keyframes(str(tmp_path / "missing.mp4"), [0.0]))


def test_sigv4_aws_test_vector():
    # docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html (example presigned URL)
    url = presign_s3("https://s3.amazonaws.com", "examplebucket", "test.txt", "AKIAIOSFODNN7EXAMPLE",
                     "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY", expires=86400,
                     now=datetime(2013, 5, 24, tzinfo=timezone.utc), virtual_host=True)
    assert url.startswith("https://examplebucket.s3.amazonaws.com/test.txt?")
    assert parse_qs(urlsplit(url).query)["X-Amz-Signature"] == [
        "aeeed9bbccd4d02ee5c0109b86d86835f995330da4c265957d157751f604d404"]


def test_presign_path_style_structure():
    s = Settings({"PERJURY_MODE": "live", "S3_ENDPOINT": "http://172.27.0.1:9000", "ACCESS_KEY": "AK",
                  "SECRET_KEY": "SK"})
    url = Media(s).presign("s3://vss-chunks-segments/i24/scene1_p1c1/seg 000.mp4", expires=600)
    u = urlsplit(url)
    q = parse_qs(u.query)
    assert u.netloc == "172.27.0.1:9000" and u.path == "/vss-chunks-segments/i24/scene1_p1c1/seg%20000.mp4"
    assert q["X-Amz-Expires"] == ["600"] and q["X-Amz-SignedHeaders"] == ["host"]
    assert q["X-Amz-Credential"][0].startswith("AK/") and "SK" not in url and len(q["X-Amz-Signature"][0]) == 64


def test_redaction_of_base64_and_secrets_on_ribbon():
    b64 = "data:image/jpeg;base64," + "A" * 5000
    r = redact({"image_url": {"url": b64}, "Authorization": "Bearer tok", "file": b"\x00" * 99})
    assert len(r["image_url"]["url"]) < 100 and r["Authorization"] == "<redacted>" and r["file"] == "<99 bytes>"
    bus = EventBus("t")
    with ribbon(bus, "cosmos3", gpu=True, request={"messages": [{"url": b64}], "token": "s3cr3t-value"}) as call:
        call.response = {"echo": b64}
    dumped = json.dumps(bus.events)
    assert "A" * 200 not in dumped and "s3cr3t-value" not in dumped
    assert bus.fired["cosmos3"]["n"] == 1


def test_ribbon_reports_error():
    bus = EventBus("t")
    with pytest.raises(RuntimeError):
        with ribbon(bus, "yolo"):
            raise RuntimeError("boom")
    assert [e["data"]["state"] for e in bus.events] == ["firing", "error"] and "yolo" not in bus.fired
