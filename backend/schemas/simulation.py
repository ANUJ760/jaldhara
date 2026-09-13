from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class SimulationRequest(BaseModel):
    aoi_id: int
    dam_id: int
    engine: str # SPH, DELFT3D, BOTH
    breach_params: Dict[str, Any]

class JobResponse(BaseModel):
    id: int
    aoi_id: int
    dam_id: int
    engine: str
    status: str
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_msg: Optional[str] = None
    
    class Config:
        from_attributes = True

class DivergenceResponse(BaseModel):
    rmse: float
    bias: float
    f_score: float
    divergence_raster_url: str
