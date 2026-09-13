from pydantic import BaseModel

class BreachComputeRequest(BaseModel):
    dam_id: int
    failure_mode: str # overtopping, piping, instant

class BreachParamsResponse(BaseModel):
    breach_width_m: float
    formation_time_hrs: float
    side_slope: float
    invert_elevation_m: float
    
class BreachValidateRequest(BaseModel):
    dam_id: int
    breach_width_m: float
    formation_time_hrs: float
    side_slope: float

class BreachValidateResponse(BaseModel):
    is_valid: bool
    warnings: list[str]
