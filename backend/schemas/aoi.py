from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AOIBase(BaseModel):
    name: str
    bbox_wkt: str # e.g., POLYGON((...))

class AOICreate(AOIBase):
    pass

class AOIResponse(AOIBase):
    id: int
    conditioned: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
