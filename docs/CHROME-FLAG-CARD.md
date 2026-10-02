# PERJURY · mic over plain HTTP (print me)

Chrome only gives a page the microphone on HTTPS or `localhost`. Our app is at
**`http://video-lab-team-__.cosmos.vastdata.com/app/`** (plain HTTP), so the table-side laptop needs a single flag.
Set it up at G0 (10:00–10:20) and test it then, not at 16:45.

## Steps (about 1 minute)

1. In the Chrome address bar, paste:
   **`chrome://flags/#unsafely-treat-insecure-origin-as-secure`**
2. In the highlighted box, type the origin, with **no path and no trailing slash**:
   **`http://video-lab-team-__.cosmos.vastdata.com`**
3. Set the dropdown to **Enabled**.
4. Click **Relaunch** (bottom right). Chrome reopens your tabs.
5. Open **`http://video-lab-team-__.cosmos.vastdata.com/app/`**. The red button should read **HOLD TO TESTIFY**, not "MIC NEEDS HTTPS".
6. Hold the button (or the **space bar**) and say *"A pickup is towing a trailer."* Then release. Allow the mic when Chrome asks. The transcript shows up "as heard by Canary".

## If it still says "MIC NEEDS HTTPS"

- The origin must match exactly: `http://`, the full host, no `/app`, no trailing `/`.
- The flag only applies after **Relaunch**. Closing the window isn't enough.
- Managed or corporate Chrome profiles can block flags. Use a personal profile or another laptop.
- macOS: System Settings → Privacy & Security → Microphone → Google Chrome must be on.

## Fallbacks, in order (FINAL-IDEA-v3 §10)

| | Where the mic runs | How |
|---|---|---|
| b | VM browser | `http://localhost:8080`. localhost counts as secure, so the mic works with no flag (if the VM desktop passes audio through). |
| c | Laptop localhost | From the repo: `mkdir -p /tmp/pj && cp app/static/index.html /tmp/pj/ && cp -r app/static /tmp/pj/static && cd /tmp/pj && python3 -m http.server 5173`, then open `http://localhost:5173/?api=http://video-lab-team-__.cosmos.vastdata.com/app/`. localhost is secure, so the mic works, and every API call goes to /app (CORS is on). |
| d | **Recorded file** | Record the line in Voice Memos or QuickTime → **⤒ recording** → pick the file. Works over plain HTTP. |
| e | **Typed** | Always available. Type the claim and press Enter. |

Honesty rule: the transcript is shown exactly as Canary heard it. If it's wrong, say it again or type it. Never fix it silently.

---
Team host: `video-lab-team-____.cosmos.vastdata.com` · VM fallback: `http://localhost:8080`
