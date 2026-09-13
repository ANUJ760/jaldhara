from pydantic import BaseModel
from typing import Optional

class DamBase(BaseModel):
    name: str
    aoi_id: int
    lat: float
    lon: float
    height_m: float
    reservoir_volume_mcm: float
    dam_type: str
    spillway_capacity: Optional[float] = None
    year_built: Optional[int] = None
    source: Optional[str] = None

class DamCreate(DamBase):
    pass

class DamResponse(DamBase):
    id: int
    
    class Config:
        from_attributes = True
