from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..db.session import get_db
from ..db.models import GEEReading
from ..schemas.monitoring import GEEReadingResponse
from ..auth.keycloak import require_role, RoleEnum
from datetime import datetime

router = APIRouter()

@router.get("/{aoi_id}/latest", response_model=list[GEEReadingResponse])
async def get_latest_monitoring(aoi_id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.DDMA_OFFICER))):
    result = await db.execute(select(GEEReading).where(GEEReading.aoi_id == aoi_id).order_by(GEEReading.timestamp.desc()).limit(1))
    return result.scalars().all()

@router.get("/{aoi_id}/history", response_model=list[GEEReadingResponse])
async def get_history_monitoring(aoi_id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.DDMA_OFFICER))):
    result = await db.execute(select(GEEReading).where(GEEReading.aoi_id == aoi_id).order_by(GEEReading.timestamp.desc()))
    return result.scalars().all()

@router.post("/{aoi_id}/trigger")
async def trigger_monitoring(aoi_id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    # Trigger GEE task
    return {"message": "Monitoring analysis triggered"}
