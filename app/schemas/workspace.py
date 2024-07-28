from pydantic import BaseModel
from typing import List, Optional
from .zeros_poles import ZerosPoles


class WorkspaceBase(BaseModel):
    workspace_name: str

class WorkspaceCreate(WorkspaceBase):
    pass

class Workspace(WorkspaceBase):
    id: int
    user_id: int
    zeros_poles: List[ZerosPoles] = []

    class Config:
        orm_mode = True
