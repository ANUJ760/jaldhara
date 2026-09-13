import asyncio
from .celery_app import celery_app
from ..db.session import async_session
from ..db.models import Job, StatusEnum
from sqlalchemy.future import select

@celery_app.task
def run_sph_simulation(job_id: int):
    # Mocking task execution
    return {"status": "success", "job_id": job_id, "engine": "SPH"}

@celery_app.task
def run_delft3d_simulation(job_id: int):
    return {"status": "success", "job_id": job_id, "engine": "DELFT3D"}

@celery_app.task
def run_dem_conditioning(aoi_id: int):
    return {"status": "success", "aoi_id": aoi_id}

@celery_app.task
def run_gee_analysis(aoi_id: int):
    return {"status": "success", "aoi_id": aoi_id}

@celery_app.task
def generate_export(job_id: int, format: str):
    return {"status": "success", "job_id": job_id, "format": format}
