from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from geoalchemy2.elements import WKTElement

from ..db.session import get_db
from ..db.models import AOI
from ..schemas.aoi import AOICreate, AOIResponse
from ..auth.keycloak import require_role, RoleEnum

router = APIRouter()

@router.post("", response_model=AOIResponse)
async def create_aoi(aoi_in: AOICreate, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    new_aoi = AOI(
        name=aoi_in.name,
        bbox=WKTElement(aoi_in.bbox_wkt, srid=4326)
    )
    db.add(new_aoi)
    await db.commit()
    await db.refresh(new_aoi)
    return new_aoi

@router.get("", response_model=list[AOIResponse])
async def list_aois(db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    result = await db.execute(select(AOI))
    return result.scalars().all()

@router.get("/{id}", response_model=AOIResponse)
async def get_aoi(id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    result = await db.execute(select(AOI).where(AOI.id == id))
    aoi = result.scalar_one_or_none()
    if not aoi:
        raise HTTPException(status_code=404, detail="AOI not found")
    return aoi

@router.post("/{id}/condition")
async def condition_aoi(id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    # Trigger Celery task here
    return {"message": "DEM conditioning triggered"}
