"""Truck observations from real YOLO sidecars and multi-frame Cosmos colour crops.

IDs are local to a five-second source, never cross-camera/global vehicle identities.
A partial scan can establish existence; it cannot establish absence or hard braking.
"""
from __future__ import annotations

import asyncio
import hashlib
import io
import json
import re
import time
from collections import Counter, OrderedDict
from dataclasses import dataclass, field
from typing import Any

from PIL import Image

from perjury.media import grid2x2, to_jpeg
from perjury.clients import ribbon
from perjury.types import Atom, AtomType, AtomVerdict, Juror, Vote

COLORS = {"white", "black", "gray", "red", "blue", "green", "yellow", "brown", "orange"}
COLOR_PROMPT = '''Inspect the numbered panels independently. Each panel is a crop around one YOLO-detected vehicle at a different time. Do not infer an action, identity, speed, or braking. Describe the predominant visible exterior colour of the central vehicle, excluding the road/background/shadows. White roofs do not establish the colour of a cab or whole truck: if only roof/trailer is visible, glare dominates, several vehicles overlap, or the vehicle is too small, set clarity to uncertain and colour to unknown. Return JSON only: {"panels":[{"panel":1,"vehicle":"truck|car|bus|unknown","colour":"white|black|gray|red|blue|green|yellow|brown|orange|unknown","clarity":"clear|uncertain"}]}. Include only numbered panels that actually contain a vehicle. Never guess.'''


def split_coloured_truck(text: str, atoms: list[Atom]) -> list[Atom]:
    """Keep a simple coloured truck subject separate from its action, using exact spans."""
    matches = list(re.finditer(r"\b(white|black|gr[ae]y|red|blue|green|yellow|brown|orange)\s+(truck)\b", text, re.I))
    if len(matches) != 1 or len(re.findall(r"\btrucks?\b", text, re.I)) != 1:
        return atoms
    if re.search(r"\b(no|not|never|without|neither|isn't|wasn't|aren't|weren't)\b", text, re.I) or any(a.type == AtomType.count for a in atoms):
        return atoms
    from perjury.atomize import rules_parse
    parsed = rules_parse(text)
    subject = next((a for a in parsed if a.type == AtomType.coco_presence and a.cls == "truck"), None)
    if subject is None:
        return atoms
    match = matches[0]
    subject.span = match.group(2)
    colour = next((a for a in parsed if a.type == AtomType.attribute and a.span.lower() == match.group(1).lower()), None)
    if colour is None:
        colour = Atom(id=f"a{len(parsed)+1}", span=match.group(1), type=AtomType.attribute)
        parsed.append(colour)
    colour.cls = "truck"
    colour.value = match.group(1).lower().replace("grey", "gray")
    colour.depends_on = subject.id
    return parsed


def iou(a, b) -> float:
    intersection = max(0, min(a[2], b[2])-max(a[0], b[0])) * max(0, min(a[3], b[3])-max(a[1], b[1]))
    union = (a[2]-a[0])*(a[3]-a[1])+(b[2]-b[0])*(b[3]-b[1])-intersection
    return intersection/union if union > 0 else 0.0


def tracks_from_sidecar(source: str, camera: str, sidecar: dict) -> list[dict]:
    """Conservative adjacent-frame IoU association; ambiguous matches start a new track."""
    shape = sidecar.get("video_shape") or []
    if len(shape) < 2 or not shape[0] or not shape[1]:
        return []
    height, width = int(shape[0]), int(shape[1])
    tracks = []
    fps = float(sidecar.get("fps") or 30)
    gap = min(0.5, max(0.1, 3/max(fps, 1)))
    for frame in sorted(sidecar.get("frames") or [], key=lambda f: float(f.get("time_sec", -1))):
        try:
            timestamp = float(frame["time_sec"])
        except (KeyError, TypeError, ValueError):
            continue
        used = set()
        for detection in frame.get("detections") or []:
            try:
                confidence = float(detection.get("confidence", detection.get("conf", 0)))
                box = list(map(float, detection.get("bbox") or detection.get("xyxy") or []))
            except (TypeError, ValueError):
                continue
            if detection.get("label") != "truck" or confidence < 0.60 or len(box) != 4:
                continue
            if max(box) <= 1.5:
                box = [box[0]*width, box[1]*height, box[2]*width, box[3]*height]
            if not (0 <= box[0] < box[2] <= width and 0 <= box[1] < box[3] <= height):
                continue
            candidates = sorted([(iou(box, t['samples'][-1]['bbox']), j) for j,t in enumerate(tracks)
                if j not in used and 0 < timestamp-t['samples'][-1]['time'] <= gap], reverse=True)
            unambiguous = candidates and candidates[0][0] >= 0.25 and (len(candidates) < 2 or candidates[0][0]-candidates[1][0] >= 0.1)
            if unambiguous:
                index = candidates[0][1]
                track = tracks[index]
            else:
                index = len(tracks)
                track = {'id': hashlib.sha256(source.encode()).hexdigest()[:12]+f'-t{index+1}', 'source':source,
                         'camera':camera, 'shape':[height,width], 'samples':[]}
                tracks.append(track)
            track['samples'].append({'time':timestamp, 'bbox':box, 'confidence':confidence})
            used.add(index)
    # Three actual frames: a single noisy detection cannot establish a truck.
    return [t for t in tracks if len(t['samples']) >= 3 and t['samples'][-1]['time'] > t['samples'][0]['time']]


def colour_result(parsed: Any, panels: int) -> tuple[str | None, list[dict]]:
    rows = (parsed or {}).get('panels', []) if isinstance(parsed, dict) else []
    seen = set()
    clear = []
    for row in rows if isinstance(rows, list) else []:
        if not isinstance(row, dict):
            continue
        panel = row.get('panel')
        if isinstance(panel, str) and panel.isdigit(): panel = int(panel)
        colour = row.get('colour')
        if isinstance(panel, bool) or not isinstance(panel, int) or panel not in range(1, panels+1) or panel in seen:
            continue
        seen.add(panel)
        if row.get('vehicle') == 'truck' and row.get('clarity') == 'clear' and colour in COLORS:
            clear.append(row)
    votes = Counter(r['colour'] for r in clear)
    if votes:
        color, count = votes.most_common(1)[0]
        if count >= 2 and len(votes) == 1:
            return color, clear
    return None, clear


async def classify_track(ctx, track: dict, bus=None) -> dict:
    samples = track['samples']
    # Use a spread of real frames, not repeated copies of one frame.
    indices = sorted(set([len(samples)//10, len(samples)//2, min(len(samples)-1, len(samples)*9//10)]))
    selected = [samples[i] for i in indices]
    with ribbon(bus, 's3', request={'source':track['source'],'times':[s['time'] for s in selected],'op':'truck crop evidence'}) as call:
        frames = await asyncio.gather(*(ctx.clients.media.keyframe(track['source'], s['time'], width=1920) for s in selected), return_exceptions=True)
        call.note = 'Timestamped truck frames'
        call.response = {'decoded_frames':sum(isinstance(f,bytes) for f in frames)}
    crops = []
    evidence = []
    for sample, frame in zip(selected, frames):
        if isinstance(frame, Exception):
            continue
        image = Image.open(io.BytesIO(frame)).convert('RGB')
        height, width = track['shape']
        bbox = sample['bbox']
        rect = [bbox[0]*image.width/width,bbox[1]*image.height/height,bbox[2]*image.width/width,bbox[3]*image.height/height]
        if rect[2]-rect[0] < 24 or rect[3]-rect[1] < 24:
            continue
        crops.append(to_jpeg(image.crop(tuple(map(int,rect)))))
        evidence.append({'time':sample['time'], 'bbox_2d':[round(v/(width if i%2==0 else height)*1000) for i,v in enumerate(bbox)], 'confidence':sample['confidence']})
    if len(crops) < 2:
        return {'state':'uncertain','colour':None,'evidence':evidence,'reason':'Fewer than two clear, sufficiently large crops.'}
    grid = grid2x2(crops)
    response = await ctx.clients.cosmos.probe(grid, COLOR_PROMPT, 'P-TRUCK-COLOUR-v1', timeout_s=15, bus=bus)
    parsed = response.parsed
    # The shared model parser keeps the first dict from a top-level JSON list.
    # Recover the full list strictly from the actual response rather than losing panels.
    if isinstance(parsed, dict) and 'panels' not in parsed and response.raw_text:
        raw = response.raw_text
        start = raw.find('[')
        if start >= 0:
            try:
                recovered, _ = json.JSONDecoder().raw_decode(raw[start:])
                if isinstance(recovered, list): parsed = {'panels': recovered}
            except ValueError: pass
    colour, panels = colour_result(parsed, len(crops))
    return {'state':'classified' if colour else 'uncertain', 'colour':colour, 'evidence':evidence,
            'panels':panels, 'reason':response.error or ('Colour agrees across clear frames.' if colour else 'Colour could not be established consistently.'),
            'cached':response.cached,'cached_at':response.cached_at, 'image_sha':response.image_sha}


@dataclass
class Inventory:
    key: str
    sources: tuple
    created: float = field(default_factory=time.time)
    state: str = 'scanning'
    scanned: int = 0
    classified: int = 0
    failed_sources: int = 0
    tracks: list = field(default_factory=list)
    task: Any = None

    def public(self):
        items=[]
        for track in self.tracks:
            result=track.get('classification') or {}
            items.append({'id':track['id'],'camera':track['camera'],'source':track['source'],
                'first_seen':track['samples'][0]['time'],'last_seen':track['samples'][-1]['time'],
                'detections':len(track['samples']), **result})
        return {'id':self.key,'state':self.state,'sources_total':len(self.sources),'sources_scanned':self.scanned,
                'failed_sources':self.failed_sources,'tracks_detected':len(self.tracks),'tracks_processed':self.classified,
                'tracks':items,'scope':'Truck tracks within each indexed segment; identities are not joined across segments or cameras.',
                'absence_proven':False, 'braking_supported':False}


INVENTORIES: OrderedDict[str,Inventory] = OrderedDict()


def inventory_key(ctx, scene: int) -> str:
    return hashlib.sha256(('P-TRUCK-COLOUR-v1\n'+ctx.settings.cosmos_model+'\n'+'\n'.join(sorted(s.camera+'|'+s.source for s in ctx.index.segments(scene)))).encode()).hexdigest()[:32]


async def _fill(ctx, scene: int, job: Inventory):
    # Cache sidecars from catalog preparation when available, otherwise read real VSS.
    from app.catalog import CATALOG
    source_semaphore = asyncio.Semaphore(6)
    color_semaphore = asyncio.Semaphore(2)
    async def source_scan(segment):
        async with source_semaphore:
            cached = CATALOG.detection_cache.get(segment.source)
            try:
                side = cached[1] if cached and time.time()-cached[0] < 300 else await ctx.clients.vss.detections(segment.source)
                if not isinstance(side, dict) or not side.get('frames'):
                    job.failed_sources += 1
                    return
                tracks = tracks_from_sidecar(segment.source, segment.camera, side)
                job.tracks.extend(tracks)
            except Exception:
                job.failed_sources += 1
            finally:
                job.scanned += 1
    async def color_scan(track):
        async with color_semaphore:
            try:
                track['classification'] = await classify_track(ctx,track)
            except Exception as error:
                track['classification'] = {'state':'error','colour':None,'reason':type(error).__name__,'evidence':[]}
            job.classified += 1
    try:
        await asyncio.gather(*(source_scan(s) for s in ctx.index.segments(scene)))
        job.state = 'classifying'
        await asyncio.gather(*(color_scan(t) for t in job.tracks))
        job.state = 'complete' if job.failed_sources == 0 and all(t.get('classification',{}).get('state') != 'error' for t in job.tracks) else 'partial'
    except asyncio.CancelledError:
        job.state = 'partial'
        raise
    except Exception:
        job.state = 'error'


def start_inventory(ctx, scene=1) -> Inventory:
    key=inventory_key(ctx,scene)
    old=INVENTORIES.get(key)
    if old and time.time()-old.created < 1800:
        return old
    active=sum(bool(j.task and not j.task.done()) for j in INVENTORIES.values())
    if active >= 2:
        raise ValueError('Two truck inventories are already processing; let them finish first.')
    job=Inventory(key,tuple(s.source for s in ctx.index.segments(scene)))
    INVENTORIES[key]=job
    job.task=asyncio.create_task(_fill(ctx,scene,job))
    while len(INVENTORIES)>8:
        removable=next((k for k,j in INVENTORIES.items() if not j.task or j.task.done()),None)
        if removable is None:break
        INVENTORIES.pop(removable)
    return job


async def evaluate_truck(atom,ctx,scene,bus) -> AtomVerdict | None:
    supported_type = (atom.type == AtomType.coco_presence and atom.cls == 'truck' and not atom.negated) or (atom.type == AtomType.attribute and atom.cls == 'truck' and atom.value in COLORS)
    if not supported_type or ctx.settings.mode != 'live':
        return None
    failures=[]
    key=inventory_key(ctx,scene)
    job=INVENTORIES.get(key)
    deadline=time.monotonic()+14
    chosen=None
    if job:
        while time.monotonic()<deadline:
            chosen=next((t for t in job.tracks if t.get('classification',{}).get('colour') == atom.value),None) if atom.type==AtomType.attribute else next(iter(job.tracks),None)
            if chosen or job.state in ('complete','partial','error'):break
            await asyncio.sleep(0.2)
    else:
        # Bounded synchronous evidence for this claim; a separate inventory can scan all sources.
        sem=asyncio.Semaphore(6)
        async def scan(segment):
            from app.catalog import CATALOG
            cached=CATALOG.detection_cache.get(segment.source)
            async with sem:
                side=cached[1] if cached and time.time()-cached[0]<300 else await ctx.clients.vss.detections(segment.source)
            return tracks_from_sidecar(segment.source,segment.camera,side or {})
        tasks=[asyncio.create_task(scan(s)) for s in ctx.index.segments(scene)]
        tracks=[]
        failures=[]
        try:
            for done in asyncio.as_completed(tasks,timeout=6):
                try:tracks.extend(await done)
                except Exception as error:
                    failures.append(type(error).__name__)
                    continue
        except asyncio.TimeoutError:pass
        finally:
            for task in tasks:
                if not task.done():task.cancel()
            await asyncio.gather(*tasks,return_exceptions=True)
        segments = ctx.index.segments(scene)
        source_rank = {s.source:i for i,s in enumerate(segments)}
        captions = {s.source:s.caption.lower() for s in segments}
        # Captions only rank candidates. Pixel classification must establish colour.
        def candidate_rank(track):
            caption=captions.get(track['source'],'')
            hinted=atom.type==AtomType.attribute and bool(re.search(rf"\b{re.escape(atom.value or '')}\b.{0,35}\btruck\b",caption))
            area=max((s['bbox'][2]-s['bbox'][0])*(s['bbox'][3]-s['bbox'][1]) for s in track['samples'])
            return (not hinted,source_rank.get(track['source'],999999),-area)
        tracks.sort(key=candidate_rank)
        if atom.type==AtomType.coco_presence:
            chosen=next(iter(tracks),None)
        else:
            color_sem=asyncio.Semaphore(2)
            async def inspect(track):
                async with color_sem:
                    result=await classify_track(ctx,track,bus)
                    track['classification']=result
                    return track
            candidates=[asyncio.create_task(inspect(t)) for t in tracks[:6]]
            try:
                for done in asyncio.as_completed(candidates,timeout=max(0.01,deadline-time.monotonic())):
                    try: track=await done
                    except Exception: continue
                    if track['classification'].get('colour')==atom.value:
                        chosen=track;break
            except asyncio.TimeoutError:pass
            finally:
                for task in candidates:
                    if not task.done():task.cancel()
                await asyncio.gather(*candidates,return_exceptions=True)
    if chosen:
        result=chosen.get('classification') or {}
        evidence=result.get('evidence') or [{'time':s['time'],'bbox_2d':[round(v/(chosen['shape'][1] if i%2==0 else chosen['shape'][0])*1000) for i,v in enumerate(s['bbox'])]} for s in [chosen['samples'][0],chosen['samples'][len(chosen['samples'])//2],chosen['samples'][-1]]]
        juror=Juror(camera=chosen['camera'],source=chosen['source'],times=[e['time'] for e in evidence])
        vote=Vote(camera=chosen['camera'],vote='yes',tier='JURY' if atom.type==AtomType.attribute else 'RECORDS',probe='P-TRUCK-COLOUR-v1' if atom.type==AtomType.attribute else 'YOLO-TRACK-v1',yes_panels=list(range(1,len(evidence)+1)),grounded=evidence[0]['bbox_2d'],juror=juror,raw={'track_id':chosen['id'],'colour':result.get('colour'),'evidence':evidence},cached=result.get('cached',False),cached_at=result.get('cached_at'))
        bus.emit('juror',{'atom_id':atom.id,'vote':vote,'badge':'COSMOS' if atom.type==AtomType.attribute else 'YOLO'})
        return AtomVerdict(atom_id=atom.id,verdict='SUPPORTED',reason=f"A {atom.value+' ' if atom.type==AtomType.attribute else ''}truck is observed in timestamped frames of this selected footage. Hard braking is not established.",reason_code='truck_colour_observation' if atom.type==AtomType.attribute else 'truck_track_observation',tiers=[vote.tier],votes=[vote],stats={'track_id':chosen['id'],'evidence':evidence,'scope':'Existence within selected footage, not current playback or exhaustive absence.'})
    return AtomVerdict(atom_id=atom.id,verdict='UNVERIFIABLE',reason='No sufficiently clear matching truck evidence was established within this assessment. This does not prove absence; scan the truck inventory for broader coverage.',reason_code='truck_evidence_incomplete',stats={'absence_proven':False,'detection_errors':dict(Counter(failures))})
