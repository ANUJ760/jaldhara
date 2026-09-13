from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from geoalchemy2.elements import WKTElement

from ..db.session import get_db
from ..db.models import DamMetadata
from ..schemas.dam import DamCreate, DamResponse
from ..auth.keycloak import require_role, RoleEnum

router = APIRouter()

@router.post("", response_model=DamResponse)
async def create_dam(dam_in: DamCreate, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    point_wkt = f"POINT({dam_in.lon} {dam_in.lat})"
    new_dam = DamMetadata(
        aoi_id=dam_in.aoi_id,
        name=dam_in.name,
        location=WKTElement(point_wkt, srid=4326),
        height_m=dam_in.height_m,
        reservoir_volume_mcm=dam_in.reservoir_volume_mcm,
        dam_type=dam_in.dam_type,
        spillway_capacity=dam_in.spillway_capacity,
        year_built=dam_in.year_built,
        source=dam_in.source
    )
    db.add(new_dam)
    await db.commit()
    await db.refresh(new_dam)
    return new_dam

@router.get("/{id}", response_model=DamResponse)
async def get_dam(id: int, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    result = await db.execute(select(DamMetadata).where(DamMetadata.id == id))
    dam = result.scalar_one_or_none()
    if not dam:
        raise HTTPException(status_code=404, detail="Dam not found")
    # Add coordinates extract here if needed
    return dam

@router.put("/{id}", response_model=DamResponse)
async def update_dam(id: int, dam_in: DamCreate, db: AsyncSession = Depends(get_db), user=Depends(require_role(RoleEnum.ANALYST))):
    result = await db.execute(select(DamMetadata).where(DamMetadata.id == id))
    dam = result.scalar_one_or_none()
    if not dam:
        raise HTTPException(status_code=404, detail="Dam not found")
    
    point_wkt = f"POINT({dam_in.lon} {dam_in.lat})"
    dam.aoi_id = dam_in.aoi_id
    dam.name = dam_in.name
    dam.location = WKTElement(point_wkt, srid=4326)
    dam.height_m = dam_in.height_m
    dam.reservoir_volume_mcm = dam_in.reservoir_volume_mcm
    dam.dam_type = dam_in.dam_type
    dam.spillway_capacity = dam_in.spillway_capacity
    dam.year_built = dam_in.year_built
    dam.source = dam_in.source
    
    await db.commit()
    await db.refresh(dam)
    return dam
