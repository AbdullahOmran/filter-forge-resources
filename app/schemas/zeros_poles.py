from pydantic import BaseModel
from typing import List, Optional

class ZerosPolesBase(BaseModel):
    x: float
    y: float
    has_conj: bool
    is_zero: bool

class ZerosPolesCreate(ZerosPolesBase):
    pass

class ZerosPoles(ZerosPolesBase):
    id: int
    workspace_id: int

    class Config:
        orm_mode = True