from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime

from ..db.session import get_db
from ..db.models import Job, StatusEnum, EngineEnum
from ..schemas.simulation import SimulationRequest, JobResponse, DivergenceResponse
from ..auth.keycloak import require_role, RoleEnum

router = APIRouter()

@router.post("/run", response_model=JobResponse)
async def run_simulation(req: SimulationRequest, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    new_job = Job(
        aoi_id=req.aoi_id,
        dam_id=req.dam_id,
        engine=EngineEnum(req.engine),
        status=StatusEnum.PENDING,
        breach_params=req.breach_params,
        started_at=datetime.utcnow()
    )
    db.add(new_job)
    await db.commit()
    await db.refresh(new_job)
    
    # Trigger Celery task here depending on engine
    
    return new_job

@router.get("/{job_id}", response_model=JobResponse)
async def get_job(job_id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.get("/{job_id}/results")
async def get_job_results(job_id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    # Mock result fetching
    return {"message": "Job results here", "url": "minio_url_to_results"}

@router.get("/compare/{job_id_sph}/{job_id_delft}", response_model=DivergenceResponse)
async def compare_simulations(job_id_sph: int, job_id_delft: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    # Return mock divergence
    return DivergenceResponse(
        rmse=1.2,
        bias=0.1,
        f_score=0.85,
        divergence_raster_url="minio_url_to_raster"
    )
