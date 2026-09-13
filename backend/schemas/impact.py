from pydantic import BaseModel
from typing import List

class VillageImpact(BaseModel):
    village_name: str
    lat: float
    lon: float
    arrival_time_hrs: float
    max_depth_m: float
    max_velocity_ms: float
    population: int
    evacuation_priority: float

class ImpactResponse(BaseModel):
    job_id: int
    villages: List[VillageImpact]
