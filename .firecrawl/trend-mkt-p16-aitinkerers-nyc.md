cookie\_policy.sh

$cat /etc/cookies.conf

We use cookies to understand how people use this site.

Analytics cookies help us improve your experience.

They are off by default. Nothing tracks you until you say so.

$select cookie\_preferences

\[1\] Accept All\[2\] Necessary Only

[cat privacy\_policy.md](https://nyc.aitinkerers.org/privacy-policy) Esc to dismiss

Browse the showcase

## Projects

Explore what the teams built and watch their demos.

21 projects5 videos

Video

### [Anomaly Congestion in NYC](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_1uMztk9jtjw)

This app solves situational awareness at city scale.

New York has thousands of public traffic cameras, but no one watches them continuously. The agent turns that passive feed into an active anomaly detector: it learns what each block normally looks like, then flags the cameras that suddenly deviate — congestion spikes, empty streets that should be busy, unusual pedestrian or vehicle patterns — and explains why in plain English.

Who would use it:

NYC DOT / traffic operations centers — spot incidents before 311 calls come in
Emergency dispatch — validate and triage field reports against live camera evidence
Urban planners / civic data teams — see patterns across boroughs and time windows
Journalists and researchers — monitor public infrastructure conditions in real time
Hackathon judges — it demos a concrete, public-interest AI application on real city data

AI TinkerersClaudeGoogle CloudLovableeleven labs

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/img-8137-jpeg-Dudi.jpg)Frank Yu](https://nyc.aitinkerers.org/connect/client/client_WtLwJY2akAI)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_1uMztk9jtjw) [Watch video](https://www.youtube.com/watch?v=rOrXtsc6LdM)

Video

### [Ari](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_S5JVBOOCmGE)

automatic alert system for accidents

Google CloudRoboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1727733701268-1787788800-beta-j4tfavut8mcfxzl-JKOu.jpg)Ari Fomalont](https://nyc.aitinkerers.org/connect/client/client_c1pebrsiERE)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_S5JVBOOCmGE) [Watch video](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/live)

### [Blockwatch](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_HySG-YZZK58)

Block Watch turns New York City's public traffic cameras into a narrated, real-time vision agent.

The city already broadcasts 968 traffic cameras through the DOT's Traffic Management Center — free, public, no API key. Block Watch polls one every couple of seconds, runs the frame through Roboflow hosted inference, and shows what's on that block right now: cars, pedestrians, bicycles, buses. Our demo sits on Broadway at 45th Street, and a runtime picker switches to any of the ~374 cameras online in Manhattan without a redeploy.

Counts alone aren't insight. A Gemini agent reads a rolling history of those counts every 60 seconds and writes a plain-English summary of how the block is changing — the difference between a camera and an observer.

Flask behind gunicorn, three concurrent loops sharing an in-memory store. That choice keeps it fast with no database, but pins the service to one instance so every request sees the same frame — a tradeoff documented in the README, not buried.

Deployed on Google Cloud Run (us-east1). Source: https://github.com/pillaiarjun/Blockwatch

It was built with Cloud Run, Gemini 2.0 Flash, Roboflow, the NYC DOT camera API, Flask, and gunicorn.

Claude CodeGoogle CloudRoboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/img-1679-jpeg-O5gS.jpg)Arjun Pillai](https://nyc.aitinkerers.org/connect/client/client_Cl9692UFlN0) [![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1780881503166-1787184000-beta-fdrcj1ynisruzkr-qP35.png)Soham Banerjee](https://nyc.aitinkerers.org/connect/client/client_SCXIx22byqc)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_HySG-YZZK58)

### [Channel 966](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_C3ZnGIGpsD4)

A machine is directing live television from 966 live video feeds of New York City. It has a premise, it holds the shot while the premise is true, and it cuts instantly when the premise breaks. We have three premises to work from: water, noir, empty.

Using Google Cloud and Roboflow to assemble and serve the feeds.

https://vision-701951209607.us-east1.run.app/channel

AI TinkerersGoogle CloudRoboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1778973707068-1785974400-beta-e68wngqwes-kv4b-Djyi.png)Ida Benedetto](https://nyc.aitinkerers.org/connect/client/client_jOJf-iRpUW8) [![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1676502038192-1770854400-beta-3zkupuloyv3aeko-UeNv.jpg)Jeff Nickerson](https://nyc.aitinkerers.org/connect/client/client_HVoc6PCzl0c)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_C3ZnGIGpsD4)

Video

### [CurbWatch](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_rqiMo3mvW-g)

CurbWatch is an agentic vision system that transforms NYC's public traffic-camera network into an accountability tool for blocked bike and bus lanes — deployed as a single container on Google Cloud Run.

How the NYC data becomes an intelligent vision agent, in three steps:

Pick a camera. All 963 online NYC DOT cameras render as points on a dark map, overlaid with 29,682 bike-lane segments from NYC Open Data, so you can see which cameras actually watch a protected lane. Search by street, filter by borough, or just ask the agent in plain language.
Trace the lane and watch. Four clicks define the lane polygon. CurbWatch then polls a live frame every 3 seconds and runs detection through Roboflow's hosted inference API. A single detection is not evidence, so our tracker matches vehicles across frames by IoU: a vehicle passing through is ignored, while one whose footprint stays in the lane for ≥3 consecutive frames is flagged as blocking, with a live dwell clock. Click any vehicle to target-lock it and follow that specific object across frames.
Get a grounded verdict. The report call sends the actual camera frame to Gemini alongside the detection timeline. Gemini cross-checks the detector's labels against the image, corrects mislabels, and states honestly when the detector is wrong — then writes the verdict in the user's language. A human approves, edits, or discards it before anything is filed, and the approved result downloads as an evidence bundle.
Working demo on real feeds: every number and frame in the demo is live from webcams.nyctmc.org. Verified in production at demo time: 963 cameras listed, 0.5–1.3 s per analyzed frame, 1.2 s per grounded report, agent replies correct in English, Spanish, Hindi and Nepali. A zero-cost replay mode (12 committed frames with cached detections) is built in as a fallback if a camera goes dark on stage.

Usefulness in numbers: ~90 seconds and ≈ $0.03 to verify one complaint with evidence; ≈ $29 to sweep all 963 cameras once. The output artifact — camera coordinates, keyframe, dwell timeline, human decision, and full JSONL agent trace in one timestamped file — does not exist in the 311 process today.

Technical execution: Node 22 + TypeScript + Hono in one container; src/core/ is dependency-free and unit-tested (48 tests); vanilla JS frontend with no build step; server-side credit guard caps inference spend and returns 429 gracefully; Gemini runs on the cheapest Flash-Lite tier and is called once per report, not once per frame.

Data craft and responsibility: all sources are public and cited (NYC DOT camera API, NYC Open Data bike routes). Detection runs on the same bytes shown to the user, so overlays can never drift from the evidence. Every LLM call, tool call, verdict, and human decision is appended to a JSONL trace that is viewable and downloadable in-app — the agent is auditable, not trusted. And by design CurbWatch detects vehicle classes only — no license plates, no faces, no identity: the enforcement question is "is the lane blocked and for how long," which a class and a clock answer. Nothing persists beyond an in-memory session.

682 segmentsAI TinkerersCanvas 2D for zone tracingCloud Build + Artifact Registry — source-to-container build pipeline.Cloud Run — the entire app is one scale-to-zero container deployed from source via ./deploy.sh (the script also auto-grants the Cloud Build role fresh projects lack). Hosts the API

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1787000219317-1788393600-beta-dqrcd1r5-tgjo-w-KXOq.png)Roshan Sharma](https://aitinkerers.org/connect/client/client_huTYOQnXkSw)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_rqiMo3mvW-g) [Watch video](https://www.loom.com/share/f36ade9fe48e433b9d6058a52d8b905a)

### [Flood Rat](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_CCDBUcrFQyE)

Hyperlocal flood watch for New York City. It reads the city's street-level water sensors, pairs them to traffic cameras, and has a rat write down what the instruments report. It pairs a city wide water sensor system called FloodNet with NYC DOT cameras. It pairs the cameras that are within 100 meters of the sensors to get a combined metric. There is an alert system where a user can monitor sensors and have them report when chosen metrics are met. There is a rat narrator that writes alerts as the water rises. And neighborhood rat stats on the back of each sensor card. Also, city wide tide gauges and sewer outflow locations to keep users aware of the water systems in NYC.

AI TinkerersGoogle CloudRoboflowneon database

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1760044894739-1770249600-beta-dcq6p4ecd-w4cba-td2Q.jpg)Joaquin Perez](https://nyc.aitinkerers.org/connect/client/client_UVPtA763nCg)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_CCDBUcrFQyE)

### [FridgeSight](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_pQkde8j5D44)

FridgeSight NYC is a vision agent for NYC community fridges: upload a photo, get inventory JSON, and see the map pin and restock queue update in real time. FastAPI on Google Cloud Run sanitizes images (EXIF strip, face blur), calls Gemini for capacity and categories, and joins live 311 rodent feeds so organizers know what to restock and what to audit. Built with Next.js, Leaflet, Pydantic, OpenCV, and Dockerized Cloud Run — turning open data and one phone photo into network-wide mutual-aid intelligence.

Google CloudRoboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/profile-amz-algorithm-aws4-hmac-sha256-amz-cr-LydV.jpg)Jian Jin Chen](https://nyc.aitinkerers.org/connect/client/client_dPx22m5N0S0)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_pQkde8j5D44)

### [HA\_CK](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_VcKs7OcitWo)

Traffic can feed to car counter + time series. Parallel camera feeds to car counts using Agents (or attempt at it). Somewhat works. Vibe-coded in Google AI Studio.

Google Cloud

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1765375354077-1776297600-beta-dxte4lalgixerpe-6pYG.jpg)Hafiz Ahsan](https://nyc.aitinkerers.org/connect/client/client_aFfQE3AM56s)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_VcKs7OcitWo)

### [Naina](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_dU4zPTKAD2E)

Naina
NYC gets ~3 million 311 complaints a year, and many of them resolve on their own. The double-parked car drives off. The debris gets swept. An inspector still gets sent.

Naina is the one-stop AI agent you need. Naina checks whether a complaint is still true by looking. It takes a complaint, finds a traffic camera that can see the location, pulls the current live frame, and asks Gemini:

Blocked Driveway, 158 E 126 St -> blocking any driveways issue raised -> Naina checks: "No vehicles blocking any driveways or curb cuts."

Naina also shows a live map sweeping all 373 Manhattan cameras every 4 minutes, counting people and vehicles, with a Play button that replays the timeline.

Cloud Run runs the agent UI, 311 pipeline, and Gemini 3.5 Flash via Vertex AI + ADC, so the container authenticates as itself with no API key anywhere. YOLOv8 runs at the edge on a GPU and ships only counts, keeping the image tens of MB instead of gigabytes.

FastAPI · Gemini 3.5 Flash · YOLOv8m · Leaflet · NYC Open Data

Google Cloud

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1725839111557-1774483200-beta-4dunessk3k3s9cq-_AGY.jpg)Swapnil Gautam](https://nyc.aitinkerers.org/connect/client/client_RwX0X5o3KTU)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_dU4zPTKAD2E)

### [NYC Haven](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_dywzRFI_Bi4)

I created a WebApp that detects pedestrians, cars, buses, and trucks in real-time. The algorithm converts these detections into a 0-100 crowd density score, automatically identifying chaotic hotspots versus quiet side streets. Instead of running heavy PyTorch TensorFlow GPU models on my own server, I send live camera frames to Roboflow’s Hosted Inference API.
By using Google Cloud Run, it hosts the FastAPI container in a serverless, auto-scaling environment, giving Haven a sub-second global response times and secure API key management with zero idle infrastructure overhead with zero idle server cost.
Haven has the possibility to make the lives of 800,000 New Yorkers that suffer from spacial anxiety and claustrophobia easier under duress.

AI TinkerersGoogle CloudRoboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1721261026466-1787788800-beta-ulzhubjg3w3hrvz-T6qO.jpg)Yousif Nazhat](https://nyc.aitinkerers.org/connect/client/client_Nnwo9it5k98)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_dywzRFI_Bi4)

### [NYC Nightlife Pulse](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_z_DrgvUNgFo)

NYC Nightlife Pulse reads pedestrian density live off NYC DOT traffic cameras and flags which blocks are unusually busy for themselves right now. Live on Cloud Run: a sampler pulls a fresh 352×240 frame from each watchlisted camera every 60 seconds, runs COCO person detection via Roboflow, and scores each block against its own trailing median — medians and MAD-based z, not means, because at ~25px per person one bad frame swings everything. Ranking by raw headcount just maps Times Square forever; the relative framing is what makes it useful. The 12-camera watchlist came from sweeping all 579 online Manhattan and Brooklyn cameras. It refuses to lie: failed fetches append nothing, thin baselines read too quiet to score. Python/FastAPI/httpx/Pillow, Docker, Cloud Run with --min-instances 1 --no-cpu-throttling — load-bearing, since scale-to-zero erases the baseline. Only (timestamp, count) is stored; no crops, no identity.

AI TinkerersGoogle CloudRoboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/5008952-BfMj.jpg)Octavio Munguia](https://nyc.aitinkerers.org/connect/client/client_jKcOJ2xHI6c)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_z_DrgvUNgFo)

### [NYC Street Risk Analysis](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_tIvFVPre4pM)

NYC Street Risk is an interactive map that combines historical NYC collision records with live traffic-camera observations and computer vision. It identifies current vehicle, pedestrian, and cyclist activity, evaluates spatial proximity indicators, and produces an explainable street-risk score for each camera location. The score supports awareness and decision-making without predicting individual crashes or dangerous behavior.

AI TinkerersDOT APIGoogle CloudRoboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1766763936960-1787184000-beta-gqnkrpwlvnmrn1d-iTk2.jpg)Matthew Levy](https://nyc.aitinkerers.org/connect/client/client_1Ks84WlkZig)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_tIvFVPre4pM)

### [ParkPulse NYC](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_p8OREiiFjEg)

\*\*ParkPulse turns NYC's existing traffic-camera network into a curb-parking
sensor — without installing a single new device.\*\*

Tell it where you're going. It watches the NYC DOT cameras around that
destination, checks the city's own sign and meter records to see where you're
actually \*allowed\* to park at this minute, and shows you — on the map — which
stretches of curb are legal right now, backed by live camera evidence you can
click into.

\*\*Working demo on real feeds.\*\* Live on Cloud Run against 968 NYC DOT cameras
(964 online). Every frame carries the city's own timestamp burned into the
pixels; we crop it out and show it beside our reading. A frozen camera keeps
returning HTTP 200 with a stale JPEG, so we hash the banner pixels — if the
city's clock stops advancing, we mark the feed dead. No HTTP status can tell
you that.

\*\*NYC relevance.\*\* NYC DOT cameras, 73,194 \*current\* DOT parking-sign orders
(nfid-uabd), 3,884 active meters (693u-uax6), NYC Planning Labs GeoSearch for
addresses. Click a curb: "Mott Street (E side) — 2 HR metered, allowed now,
Meter 1243110." At 20:04 Friday, 226 of 228 nearby spots are legal; on Monday
08:30, sixteen flip to restricted as rush-hour No Standing kicks in.

\*\*Usefulness.\*\* An empty curb isn't a legal curb. ParkPulse separates "there is
space" from "you may park here," and only the city's own record can answer the
second. Restricted blockfaces are filtered out of ranking entirely.

\*\*Technical execution.\*\* The feeds are 352×240 with no higher-res variant — we
measured this, and it drove every design decision. Consequently:
\- We never state a gap in feet. There is no honest path from 352px to curb
length, so we report how contested a curb is, not that a space exists.
\- \*\*Parked vs. moving separation.\*\* Counting every detection as curb occupancy
measures \*traffic\*, not parking — a busy street reads "full" from
through-traffic. Detections are IoU-matched across frames; only vehicles
holding still ~a minute count as parked.
\- \*\*The curb band is learned, not drawn.\*\* No hand-drawn ROIs: it accumulates
where parked cars come to rest and infers the parking strip. Adding a camera
is adding an ID to a list, and it re-learns when a camera pans.
\- \*\*Automated quality gate.\*\* Laplacian focus, exposure clipping, and clock
advance. Roughly 3 in 12 nearby cameras are unusable (defocused lens, sun
glare) — a hand-picked list can't notice one degrading mid-demo.
\- \*\*Detector-quality filters.\*\* Gemini returned bridge railings as "car" at
5×89px; we filter on shape and de-duplicate.
\- Two clocks kept apart: UTC for durations, NYC local for rules. Evaluating
"No standing 7–10 AM" against UTC tells drivers a restriction ended five
hours early.

\*\*Google Cloud Run.\*\* Single container — FastAPI serves the API \*and\* the built
React bundle. One service, one URL, no CORS. Deployed with
\`--min-instances=1 --no-cpu-throttling\`, which is mandatory: Cloud Run freezes
background work between requests, and our poller is a background asyncio task,
so without those flags the ring buffer never fills. Gemini 2.5 Flash runs on
Vertex AI via \*\*Application Default Credentials\*\* — the hackathon project's
policy disallows API keys, and ADC is better anyway: on Cloud Run the service
account supplies credentials, so no secret ever enters the container or repo.

\*\*Stack:\*\* FastAPI · Gemini 2.5 Flash (Vertex AI) · React + Vite + MapLibre GL ·
OpenFreeMap tiles · Photon (OSM) + NYC GeoSearch · Pillow/NumPy/pyproj ·
Cloud Build → Cloud Run.

\*\*Honest limitation:\*\* it rained all evening. Gemini detects moving vehicles
fine but almost no parked ones — dark cars on a wet dark curb at 352×240. The
system reports "Watching…" rather than inventing a reading, which is by design
(honesty rules in docs/PLAN.md §8, enforced by tests). The legality layer is
fully live and independent of weather.

\*\*Live:\*\* https://parkpulse-1026949542335.us-central1.run.app
\*\*Repo:\*\* https://github.com/rogersentongo/parkpulse-nyc

693u-uax6 (meters). NYC Planning Labs GeoSearch.Application DefaultCloud BuildCredentials. NYC DOT traffic cameras (webcams.nyctmc.org). NYC Open Data:Google Cloud

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/roger-sentongo-profile-picture-jpg-LyJd.jpg)Roger Sentongo](https://nyc.aitinkerers.org/connect/client/client_1dzQVxAUzfw)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_p8OREiiFjEg)

### [Shedwatch](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_-tCR42tIct8)

Shedwatch: the camera-verified sidewalk shed auditor

NYC has about 8,300 permitted sidewalk sheds, and 16,299 buildings whose shed permit has lapsed since 2024. Some sheds quietly stand for years after their permits die. Our top case has been up since 2018 with a permit dead for 856 days. The city inspects by foot. We audit by camera.

Shedwatch cross-references DOB NOW permit records against live NYC DOT traffic cameras to find sheds standing with no active permit on record, then assembles evidence-backed 311/DOB complaints that a human approves with one click.

How it works (live, on real feeds): We joined all 107k sidewalk shed permits from NYC Open Data against 968 DOT camera locations, then filtered hard: permit lapsed, job never signed off, no renewal pending, no active neighbor permit. That leaves 90 camera-watchable suspects. One click photographs all 90 corners live. Gemini votes 3 times per frame (majority rules, bounding box drawn), and an adversarial "AI skeptic" pass then tries to refute each detection: could it be a permanent colonnade, an awning, a construction fence? Seven live record checks per case (open complaints, unsafe-facade status, active work permits on site) auto-classify every detection as FILE READY, COMPLAINT ALREADY OPEN, LEGALLY EXCUSED, NEEDS RECHECK, or AI-REJECTED. Every card links its proof: the raw DOB permit chain, the building profile, Street View, and a fresh frame seconds old. A human approves every filing. Nothing is reported without review.

Tech: Google Cloud Run (FastAPI service and UI, deployed via Cloud Build), Gemini structured-output vision (detection votes, bounding boxes, scene-quality gating, skeptic pass), NYC DOT public camera feeds, live NYC Open Data queries (DOB NOW permits, complaints, violations, FISP facades), vanilla JS frontend.

Impact: Turns 968 dumb traffic cameras into a self-skeptical civic inspector for one of NYC's most hated quirks: eternal scaffolding. The same pattern (records, live vision, human approval) extends to blocked bike lanes, bus lanes, and curb ramp accessibility.

Live demo: https://shedwatch-187000325658.us-east1.run.app

AI TinkerersArtifact RegistryCloud BuildCloud RunDOB NOW

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1708786644113-1785974400-beta-hqipgjlic5-dgzx-KV1a.jpg)Aryan Arora](https://nyc.aitinkerers.org/connect/client/client_Ap8brJJ_TBQ) [![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1779841543451-1786579200-beta-nndv-baiwiqm37--V4T2.jpg)Siddharth Saha](https://nyc.aitinkerers.org/connect/client/client_gaV3pMTELAc) [![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1749471103061-1785974400-beta-pfaauue5atwznri-5ROW.jpg)Buland Choudhary](https://nyc.aitinkerers.org/connect/client/client_CvEYGtty9Nk) [![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1763580903206-1785974400-beta-2wilgim9ovm-pbi-B2Ba.jpg)Kevin Shah](https://nyc.aitinkerers.org/connect/client/client_P1VTMywzHOY)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_-tCR42tIct8)

### [Sidestreets](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_u_WZ8s9LbW0)

Google Maps predicts how fast traffic should move from aggregated phone speeds. Sidestreet looks at NYC's own traffic cameras and reports how full the streets actually are... then reroutes you around the mess.

Enter any two NYC addresses. Sidestreet draws two routes: Google's recommendation, and its own. Every candidate is a real Google Routes API route with live traffic (legal turns, correct one-ways) so we never invent a path. What we add is ground truth: 963 live NYC DOT camera feeds, run through Roboflow COCO object detection, counting vehicles per frame and grading each block free / moderate / jammed. We re-rank Google's own candidates by that evidence, and generate side-street alternatives by offsetting perpendicular to the main route. The result is a plain-English answer: "Google routes via 5th Ave; four cameras on it are jammed; take Madison instead, 2.4 minutes faster on Google's own estimate" and you can click any camera to see the live frame that decision was made on.

AI TinkerersGoogle CloudRoboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/441766503-1091982482104458-684767441021303783-7Oa-.jpg)Dev Devnani](https://nyc.aitinkerers.org/connect/client/client_hHbxEoYdWGk)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_u_WZ8s9LbW0)

### [Vibecheck NYC](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_6ogn0tbn0lc)

New York has 900+ public DOT traffic cameras streaming every corner of the city, but no human can watch them all. vibecheck.nyc turns that raw feed into a living crowd-sense: a live density map of Manhattan and an agent you can ask anything — "How busy is Washington Square Park?" "Is the Flatiron rooftop scene worth it?" — and get an answer grounded in what the cameras actually see, right now.

Working demo, real feeds. Everything on screen is live: 968 NYC DOT cameras (85 hero corners sampled every 60 seconds), NWS weather from Central Park, and the city's official CECM permitted-events feed. No mocks, no canned data — reload and the numbers change.

How it works. Cloud Scheduler crons drive a Cloud Run collector that archives frames to Cloud Storage — our source of truth. Roboflow hosted inference (COCO) counts people and vehicles per frame. A Cloud Run agent service wraps Gemini 2.5 Flash (via Vertex AI) with custom tools: it picks cameras near any place you name, counts crowds live, compares against a 4-day same-hour baseline built from our own archive, folds in weather and active permits, and answers in plain language with honest confidence ("solid read" vs "rough read"). Answers stream with narrated progress over SSE. A third Cloud Run service serves the React dashboard: a blue-to-red heat cloud over Manhattan, per-area chips, and hourly trend charts of today versus typical.

NYC quirks we tackled. Cameras are 352×240 and re-aim without warning — we validated sightlines corner by corner and treat person counts as a relative index, stated honestly. Night exposure locks to headlights — the agent knows which corners stay readable after dark. Parks have no cameras inside — so the agent reads the perimeter and infers the inside, the way a New Yorker would.

Why it's useful. One glance answers the question every New Yorker asks daily: where is the energy right now — and is it worth the trip? The same rails generalize to street-fair staffing, event egress monitoring, and city operations.

Stack: Google Cloud Run (3 services: collector, agent, web) · Cloud Scheduler · Cloud Storage · Vertex AI (Gemini 2.5 Flash, function calling) · Roboflow hosted inference · Flask · React + Vite · Express · Google Maps JS · NYC DOT cameras · NYC Open Data (CECM events) · National Weather Service.

AI TinkerersGoogle CloudNYC DOT cameras · NYC Open Data (CECM events) · National Weather Service.Roboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/e77f192959f6b19996b855d9477e3d33-IqK7.jpg)Ayush Sharma](https://nyc.aitinkerers.org/connect/client/client_TB5LBDc6t8I) [![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1755509530521-1785974400-beta-f4xrluttk3hn4i3-x4B_.png)Deepankar Jaisia](https://nyc.aitinkerers.org/connect/client/client_Ob02t3VTPVM)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_6ogn0tbn0lc)

### [Weeknight Warriors](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_9vW6Gu1xt_o)

Red Light Racer:

“I live my life a quarter mile at a time” - Mayor Zohran Mamdani, probably
Turn live New York streets into illegal street races and bet on the winner.
Takes live NYC traffic video data and creates a game where you guess who will win the “street race” and cross the finish line first.
Involves several computer vision algorithms to identify which cameras make for possible games (including our local Houston and Broadway just outside)!.
Another algorithm finds out when cars have accumulated at a red light, and another algorithm tracks car through the race!

Code: https://github.com/nyc-vision-hack-2026/red-light-racer

Google CloudRoboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1763136064173-1770854400-beta-8xohojh17locbom-dYu6.png)Saurav Das](https://nyc.aitinkerers.org/connect/client/client_jRokqTblIls) [![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1767546414841-1786579200-beta-63ic3craqdbznld-Di9Y.jpg)Manikandan Jeyarajan](https://nyc.aitinkerers.org/connect/client/client_KXgLg31q6CQ)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_9vW6Gu1xt_o)

### [Which street should I try?](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_2ePK5Cq8lQ4)

My uncle circles Sheepshead Bay for twenty minutes every night — not because there's nowhere to park, but because NYC parking signs are unreadable. There are 6,288 of them in his neighborhood. This reads all of them: you give it an address and when you'll arrive, and it tells you which block, which side of the street, how far you're walking, and when you'd have to move the car. Built on 1,224 block faces from DOT's sign inventory, the alternate-side-parking calendar, six months of 311 complaints, and four live NYC DOT traffic cameras read by Gemini. Running on Cloud Run.

AI TinkerersClaudeGoogle Cloud

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1751838392057-1787184000-beta-cmna7mzzn9mhcaw-rgdg.jpg)Nicholas Faciano](https://nyc.aitinkerers.org/connect/client/client_reflv97dYaA)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_2ePK5Cq8lQ4)

Video

### [Will McCann](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_lXmHGa_2TRU)

AI Tinkerers Hackathon Google Cloud Run - traffic cam demo

Google CloudGoogle Vertex AIRoboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1666035704671-1787184000-beta-ypmcaczuk0cp-nx-0qcM.jpg)William McCann](https://nyc.aitinkerers.org/connect/client/client_lRlAKawt1BI)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_lXmHGa_2TRU) [Watch video](https://www.youtube.com/watch?v=ttZ7rB1P5mg)

Video

### [XWalk Keyboards](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_OapxeVXw7rg)

This project reimagines crosswalks as piano keyboards with two studies, Realtime and Orchestration. The Realtime study uses a 511NY video feed focused on an intersection on NYC's Westside Highway. As pedestrians cross and step on the crosswalk stripes, the browser plays the corresponding piano note, as if pedestrians are walking on a giant piano.

The Orchestration study lays out a 3 X 4 grid of 511NY Manhattan traffic cams at intersections with crosswalks and staggers their updates at 5s apart. Meanwhile, an agent receives the full grid including pedestrian detections and decides how to "score" the scene by looking at the corresponding notes and making decisions about tone, pacing and audio effects. The overall effect is an audiovisual streetscape where crosswalk keyboard mappings are the main driver of the soundtrack.

Both the NextJS web client and ADK based orchestration agent are deployed to Cloud Run. We're using Roboflow workflows for both the Realtime and Orchestration studies to detect pedestrians.

AI TinkerersCodexFigma Design agentGoogle CloudRoboflow

Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/1516304214622-1785974400-beta-afdsfni3rjqa9yt-kZ1E.jpg)Vince Allen](https://nyc.aitinkerers.org/connect/client/client_VjE6uama0do)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_OapxeVXw7rg) [Watch video](https://www.youtube.com/watch?v=VEdwzpfaP-I)

### [🚌 Bus Reality Check](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_S5dM-RxDOcw)

\# Bus Reality Check — a vision agent that catches MTA Bus Time lying

MTA's own app trusts its GPS feed blindly. Yesterday it told us that a QM15 bus was "arriving now" for seven straight minutes — the icon frozen at one stop while the app cycled 5 min → 0 min → arriving → departed. No bus ever came. We were stranded and late. This happens across the city every day: stale GPS pings, ghost buses, and deadheading buses that blow past stops.

\*\*Bus Reality Check\*\* verifies MTA's real-time claims against physical ground truth using two signals no rider-facing app combines:

\- \*\*Signal A — feed staleness:\*\* We read \`RecordedAtTime\` from MTA's SIRI feed — the timestamp of a bus's last real GPS ping. When a bus claims to be approaching but its GPS hasn't moved in over 90 seconds, we flag it \*\*LOW confidence\*\* and tell you to bail to a backup — the exact failure that stranded our rider, now detectable.
\- \*\*Signal B — camera ground truth:\*\* We bind your stop to the specific bus approaching it, auto-select the nearest NYC DOT traffic camera to where the feed claims the bus is (from all 968 city cameras), and run a Roboflow vision model on the live frame. If the feed is stale \*\*and\*\* the camera sees no bus, that's a confirmed phantom.

The agent fuses both into one verdict — \*\*CONFIRMED · HIGH · OK · LOW\*\* — shows your stop with the upstream stops being verified and the live bus position, and logs a verification trail with saved camera-frame proof ("verified at stop 5, then 4, then 3…") as the bus is confirmed at each stop.

\*\*Working demo on real feeds:\*\* It runs live on real MTA SIRI data and live DOT camera imagery right now, deployed on Google Cloud Run at https://bus-reality-check-k3es2z5enq-uc.a.run.app. A replay mode reproduces the real QM15 incident so the "caught it" moment demos reliably.

\*\*NYC relevance & impact:\*\* This is a universal NYC pain that Google Maps and MTA's own app fail at — they say "no bus" and stop. We beat them by adding an orthogonal, camera-based reality check the official feed fundamentally lacks, making an unreliable system legible so riders decide before they're stranded. It's privacy-clean by design: we detect buses and asphalt, never people.

\## Technologies used

\- \*\*Google Cloud Run\*\* — serverless deployment of the agent (Dockerfile → live URL), pinned to a single warm instance so the verification trail stays coherent.
\- \*\*MTA Bus Time SIRI API\*\* (VehicleMonitoring + OneBusAway stops-for-route) — real-time bus positions, \`RecordedAtTime\`, occupancy, and ordered official stop names per direction.
\- \*\*NYC DOT traffic cameras\*\* (webcams.nyctmc.org) — 968 live camera feeds; nearest-camera lookup via haversine against live stop coordinates.
\- \*\*Roboflow\*\* (hosted COCO inference) — bus/vehicle detection on live 352×240 camera frames.
\- \*\*FastAPI + Uvicorn\*\* (Python) — async backend fusing the two signals; \*\*httpx\*\* for concurrent feed/camera calls; \*\*python-dateutil\*\* for staleness math.
\- \*\*Vanilla JS + HTML/CSS\*\* single-page dashboard — directional stop timeline, live verdict, camera feed, and proof-backed verification log.
\- \*\*JSONL + on-disk proof capture\*\* with an auto-prune cap so the ephemeral filesystem stays bounded.

AI TinkerersAntigravityClaudeGoogle CloudRoboflow

Team

[![](https://www.gravatar.com/avatar/2f5800413028959e0b833d1a29fd4b8a?s=200&d=mp)Engred Vanegas](https://nyc.aitinkerers.org/connect/client/client_xxSk7VarhTE) [![](https://www.gravatar.com/avatar/b10c80f11c6e3e9f87ab2c37ee7aaeb2?s=200&d=mp)Anastasiya Chabotska](https://nyc.aitinkerers.org/connect/client/client_k30sxJ6aIgM)

[Project details](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_S5dM-RxDOcw)

## Project video

[Open video in a new tab](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/showcase#)

### Comments

Commenting on selected text

CancelComment

×

Loading resume data...