from pydantic import BaseModel
from datetime import datetime
from typing import Any, Dict, List

class GEEReadingResponse(BaseModel):
    id: int
    timestamp: datetime
    satellite: str
    ndwi_mean: float
    baseline_ndwi_mean: float
    anomaly_detected: bool
    water_extent_geojson: Dict[str, Any]
    
    class Config:
        from_attributes = True
