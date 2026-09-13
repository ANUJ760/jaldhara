from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..db.session import get_db
from ..db.models import DamMetadata
from ..schemas.breach import BreachComputeRequest, BreachParamsResponse, BreachValidateRequest, BreachValidateResponse
from ..breach.froehlich import compute_froehlich
from ..auth.keycloak import require_role, RoleEnum

router = APIRouter()

@router.post("/compute", response_model=BreachParamsResponse)
async def compute_breach(req: BreachComputeRequest, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    result = await db.execute(select(DamMetadata).where(DamMetadata.id == req.dam_id))
    dam = result.scalar_one_or_none()
    if not dam:
        raise HTTPException(status_code=404, detail="Dam not found")
        
    params = compute_froehlich(dam.height_m, dam.reservoir_volume_mcm, req.failure_mode)
    return params

@router.post("/validate", response_model=BreachValidateResponse)
async def validate_breach(req: BreachValidateRequest, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    # Perform basic sanity checks
    warnings = []
    is_valid = True
    
    if req.breach_width_m <= 0:
        is_valid = False
        warnings.append("Breach width must be positive.")
    if req.formation_time_hrs <= 0:
        is_valid = False
        warnings.append("Formation time must be positive.")
    
    return BreachValidateResponse(is_valid=is_valid, warnings=warnings)
