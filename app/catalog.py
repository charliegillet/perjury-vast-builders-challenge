"""Live VAST catalog with immutable allowlisted playback/evidence snapshots."""
from __future__ import annotations
import asyncio,copy,hashlib,time,uuid,re
from collections import Counter,OrderedDict
from dataclasses import dataclass
from perjury.vss import rows,normalize
from perjury.yolo import persistence,peak_counts,parse_counts

LABELS={'san_francisco':'San Francisco','indoor':'Indoor','warehouse3':'Warehouse 3','neighborhood':'Neighborhood','toronto':'Toronto','nashville':'Nashville'}

def opaque(source):return hashlib.sha256(source.encode()).hexdigest()[:24]
def order(row):return (row.get('upload_timestamp') or '',int(row.get('chunk_index') or 0),row.get('filename') or '')
def camera_key(row):
    # I-24 metadata identifies the upload stream; explicit source names identify
    # its three physical views. Retain both rather than merging them as one view.
    m=re.search(r'(?:^|_)p([1-3])c([1-6])(?:_|\.)',row.get('filename') or '')
    return f"{row['camera_id']}:p{m[1]}c{m[2]}" if row['camera_id'].startswith('i24') and m else row['camera_id']

@dataclass(frozen=True)
class Snapshot:
    id: str
    location: str
    created: float
    records: tuple
    index_data: dict
    def public(self):
        cameras={}
        for r in self.records:
            camera=camera_key(r);entry=cameras.setdefault(camera,{'key':camera,'label':camera,'clips':[]})
            timeline=r.get('timeline') or []
            classes=sorted({c.strip() for s in timeline for c in (s.get('object_classes') or '').split(',') if c.strip()})
            counts={}
            for segment in timeline:
                for k,v in parse_counts(segment.get('object_counts')).items():counts[k]=max(counts.get(k,0),v)
            entry['clips'].append({'source_id':opaque(r['original_video']),'label':r.get('filename') or camera,'upload_timestamp':r.get('upload_timestamp'),'duration':r.get('chunk_duration_sec'),'chunk_index':r.get('chunk_index'),'location':r['location'],'caption':' '.join(s.get('reasoning_content') or '' for s in timeline)[:4000],'object_classes':classes,'object_counts':counts,'evidence_scope':'indexed caption and peak counts in this clip'})
        return {'id':self.id,'scope_id':self.id,'location':self.location,'label':('All locations' if self.location=='all' else LABELS.get(self.location,self.location.title())),'segments_count':len(self.index_data['segments']),'cameras':list(cameras.values()),'analyzable':True,'analysis_scope':'All catalog chunks for selected camera; select camera explicitly','created_at':self.created,'coverage':self.index_data['coverage']}
    def source(self,camera,clip=0):
        clips=[r for r in self.records if camera_key(r)==camera]
        if clip<0 or clip>=len(clips):raise KeyError('Unknown camera clip')
        return clips[clip]['original_video']
    def source_id(self,sid):
        for r in self.records:
            if opaque(r['original_video'])==sid:return r['original_video']
            for s in r.get('timeline') or []:
                if s.get('source') and opaque(s['source'])==sid:return s['source']
        raise KeyError('Source outside selected scope')

class Catalog:
    def __init__(self,ttl=60):
        self.ttl=ttl;self.updated=0;self.records=[];self.task=None;self.scopes=OrderedDict();self.scope_tasks={};self.detection_cache={}
    async def refresh(self,vss):
        if self.records and time.time()-self.updated<self.ttl:return
        if self.task is None or self.task.done():self.task=asyncio.create_task(self._fetch(vss))
        await asyncio.shield(self.task)
    async def _fetch(self,vss):
        found={};offset=0
        while offset<10000:
            response=await vss.explore(limit=48,offset=offset);page=rows(response)
            for r in page:
                if r.get('original_video') and r.get('camera_id') and r.get('location'):
                    found[r['original_video']]=copy.deepcopy(r)
            offset+=len(page)
            if not page or len(page)<48 or offset>=int(response.get('total') or 10000):break
        self.records=sorted(found.values(),key=order,reverse=True);self.updated=time.time()
    async def summary(self,vss):
        await self.refresh(vss);counts=Counter(r['location'] for r in self.records)
        locations=[{'key':'all','label':'All locations','count':len(self.records),'latest_upload':max((r.get('upload_timestamp') or '' for r in self.records),default=None)}]
        for key in sorted(counts):
            locations.append({'key':key,'label':LABELS.get(key,key.replace('_',' ').title()),'count':counts[key],'latest_upload':max(r.get('upload_timestamp') or '' for r in self.records if r['location']==key)})
        return {'locations':locations,'total':len(self.records),'updated_at':self.updated}
    async def scope(self,vss,location):
        await self.refresh(vss)
        selected=[r for r in self.records if location=='all' or r['location']==location]
        if not selected:raise KeyError('Location not in live VAST catalog')
        latest_days={}
        for r in selected:
            latest_days[r['location']]=max(latest_days.get(r['location'],''),(r.get('upload_timestamp') or '')[:10])
        selected=[r for r in selected if (r.get('upload_timestamp') or '')[:10]==latest_days[r['location']]]
        key=(self.updated,location)
        task=self.scope_tasks.get(key)
        if task is not None and task.done():
            try:
                previous=task.result()
                if time.time()-previous.created>1200 or previous.id not in self.scopes:task=None
            except (Exception, asyncio.CancelledError):task=None
        if task is None:
            task=asyncio.create_task(self._scope(vss,location,selected));self.scope_tasks={k:t for k,t in self.scope_tasks.items() if k[0]==self.updated};self.scope_tasks[key]=task
        return copy.deepcopy(await asyncio.shield(task))
    async def _scope(self,vss,location,selected):
        cameras=list(dict.fromkeys(camera_key(r) for r in selected))
        segments=[]
        for parent in selected:
            for i,row in enumerate(parent.get('timeline') or []):
                n=normalize(row,parent['original_video'])
                if not n.get('source') or n['start'] is None or n['end'] is None:continue
                classes=row.get('object_classes') or []
                if isinstance(classes,str):classes=[c.strip() for c in classes.split(',') if c.strip()]
                segments.append({'source':n['source'],'original_video':parent['original_video'],'scene':1,'camera':camera_key(parent),'camera_id':parent['camera_id'],'location':parent['location'],'seg':len(segments),'start':n['start'],'end':n['end'],'caption':n['caption'],'object_classes':classes,'object_counts':parse_counts(row.get('object_counts')),'persist':{}})
        index={'version':1,'source':'live','camera_id':'catalog','scenes':{'1':{'label':LABELS.get(location,location),'duration':max((r.get('chunk_duration_sec') or 0 for r in selected),default=0),'cameras':cameras}},'coverage':{'selected_location':location,'catalog_chunks':len(selected),'analysis_chunks':len(selected),'window':'all category chunks; per-run analysis restricted to one camera','detection_evidence':'loaded on verification'},'segments':segments}
        snap=Snapshot(uuid.uuid4().hex,location,time.time(),tuple(copy.deepcopy(selected)),index)
        self.scopes[snap.id]=snap
        while len(self.scopes)>12:self.scopes.popitem(last=False)
        return snap
    def get(self,sid):
        snap=self.scopes.get(sid)
        if snap is None or time.time()-snap.created>1200:raise KeyError('Scope expired; reload catalog')
        return copy.deepcopy(snap)

CATALOG=Catalog()

async def build_context(base,snapshot,camera=None):
    """All selected-camera chunks; unrelated sites never form a joint jury."""
    from perjury.index import SceneIndex
    from perjury.pipeline import Context
    data=copy.deepcopy(snapshot.index_data)
    cameras=data['scenes']['1']['cameras']
    if not camera:raise ValueError('Select an assessment camera explicitly')
    if camera not in cameras:raise ValueError('Camera outside selected scope')
    data['segments']=[s for s in data['segments'] if s['camera']==camera]
    if not data['segments']:raise ValueError('No indexed segments are available for this camera')
    data['scenes']['1']['cameras']=[camera];data['coverage']['analysis_camera']=camera
    data['coverage']['catalog_scope']=True
    locations={s['location'] for s in data['segments']}
    if len(locations)!=1:raise ValueError('Assessment camera must resolve to one location')
    data['coverage']['selected_location']=next(iter(locations))
    data['camera_id']=data['segments'][0]['camera_id']
    scoped_settings=copy.copy(base.settings)
    scoped_settings.camera_id=data['camera_id']
    errors=[]
    enriched=set()
    sem=asyncio.Semaphore(6)
    async def enrich(s):
        cached=CATALOG.detection_cache.get(s['source'])
        if cached and time.time()-cached[0]<300:side=cached[1]
        else:
            try:
                async with sem:side=await base.clients.vss.detections(s['source'])
            except Exception:
                errors.append(s['source']);return
            if side is not None:CATALOG.detection_cache[s['source']]=(time.time(),side)
        if not isinstance(side,dict) or not side.get('frames'):
            errors.append(s['source']);return
        s['persist']=persistence(side);s['object_counts']=peak_counts(side)
        s['video_shape']=side.get('video_shape')
        enriched.add(s['source'])
    try:
        await asyncio.wait_for(asyncio.gather(*(enrich(s) for s in data['segments'])),timeout=12)
    except asyncio.TimeoutError:
        errors.extend(s['source'] for s in data['segments'] if s['source'] not in enriched)
    data['coverage']['detection_errors']=len(set(errors))
    data['coverage']['detection_evidence']='complete' if not errors else 'partial; no absence proof'
    if len(CATALOG.detection_cache)>4000:CATALOG.detection_cache.clear()
    return Context(settings=scoped_settings,clients=base.clients,index=SceneIndex(data),probes={},router=base.router)
