"""Independent truck inventory routes; no global evidence context is changed."""
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field

router = APIRouter()

class InventoryIn(BaseModel):
    scope_id: str = Field(min_length=32, max_length=32)
    camera: str = Field(min_length=1, max_length=96)

@router.post('/api/trucks/inventory')
async def inventory(body: InventoryIn):
    from app.main import _ensure_ctx
    from app.catalog import CATALOG, build_context
    from perjury.trucks import start_inventory
    base=await _ensure_ctx()
    if base is None or base.settings.mode != 'live':
        raise HTTPException(503,'Real video services are unavailable')
    try:
        snapshot=CATALOG.get(body.scope_id)
        context=await build_context(base,snapshot,body.camera)
        job=start_inventory(context)
        return job.public()
    except KeyError as error:
        raise HTTPException(409,'Footage selection expired; refresh footage') from error
    except ValueError as error:
        raise HTTPException(422,str(error)) from error

@router.get('/api/trucks/inventory/{inventory_id}')
async def inventory_status(inventory_id: str):
    from perjury.trucks import INVENTORIES
    job=INVENTORIES.get(inventory_id)
    if job is None:
        raise HTTPException(404,'Inventory unavailable; start a new scan')
    return job.public()

@router.get('/api/trucks/evidence/{inventory_id}/{track_id}')
async def evidence(inventory_id: str,track_id: str,panel: int=0):
    from app.main import _ensure_ctx
    from perjury.trucks import INVENTORIES
    from perjury.media import draw_boxes
    from fastapi.responses import Response
    job=INVENTORIES.get(inventory_id)
    track=next((t for t in job.tracks if t['id']==track_id),None) if job else None
    if track is None:
        raise HTTPException(404,'Truck track not present in this inventory')
    rows=(track.get('classification') or {}).get('evidence') or []
    if panel<0 or panel>=len(rows):
        raise HTTPException(404,'No verified frame for this track')
    ctx=await _ensure_ctx()
    row=rows[panel]
    try:
        frame=(await ctx.clients.media.keyframes(track['source'],[row['time']],width=1920))[0]
        frame=draw_boxes(frame,[{'xyxy1000':row['bbox_2d'],'label':f"{track_id} @ {row['time']:.2f}s"}])
        return Response(frame,media_type='image/jpeg',headers={'Cache-Control':'private, max-age=300'})
    except Exception as error:
        raise HTTPException(502,'Actual evidence frame unavailable') from error
