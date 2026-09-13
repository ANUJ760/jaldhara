from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..db.session import get_db
from ..schemas.export import ExportResponse
from ..auth.keycloak import require_role, RoleEnum

router = APIRouter()

@router.post("/shapefile/{job_id}", response_model=ExportResponse)
async def export_shapefile(job_id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    # Trigger export job
    return ExportResponse(download_url="minio_url/shapefile.zip", status="COMPLETED")

@router.post("/kml/{job_id}", response_model=ExportResponse)
async def export_kml(job_id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    return ExportResponse(download_url="minio_url/export.kml", status="COMPLETED")

@router.post("/geotiff/{job_id}", response_model=ExportResponse)
async def export_geotiff(job_id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    return ExportResponse(download_url="minio_url/export.tif", status="COMPLETED")

@router.post("/pdf/{job_id}", response_model=ExportResponse)
async def export_pdf(job_id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    return ExportResponse(download_url="minio_url/report.pdf", status="COMPLETED")

@router.get("/download/{export_id}")
async def download_export(export_id: str, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    # Would redirect or stream file
    return {"message": "Stream file here"}
