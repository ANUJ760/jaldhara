from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..db.session import get_db
from ..schemas.impact import ImpactResponse
from ..impact.village_impact import compute_impact
from ..auth.keycloak import require_role, RoleEnum

router = APIRouter()

@router.get("/{job_id}", response_model=ImpactResponse)
async def get_impact(job_id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.DDMA_OFFICER))):
    impacts = compute_impact(job_id)
    return ImpactResponse(job_id=job_id, villages=impacts)

@router.get("/{job_id}/evacuation")
async def get_evacuation_priority(job_id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.DDMA_OFFICER))):
    impacts = compute_impact(job_id)
    # Sort by priority descending
    sorted_impacts = sorted(impacts, key=lambda x: x["evacuation_priority"], reverse=True)
    return {"evacuation_list": sorted_impacts}
