import enum
from pydantic import BaseModel
from typing import List

class RoleEnum(str, enum.Enum):
    ANALYST = "analyst"
    DDMA_OFFICER = "ddma_officer"

class UserToken(BaseModel):
    username: str
    roles: List[RoleEnum]
