from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.dependencies import get_current_active_user
from app.database import get_db
from app.models.user import User
from app.models.zeros_poles import ZerosPoles
from app.models.workspace import Workspace

router = APIRouter()


@router.post("/{workspace_id}/zeros_poles", response_model=schemas.ZerosPoles)
def create_zeros_poles(workspace_id: int, zeros_poles: schemas.ZerosPolesCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    workspace = crud.get_workspace(db=db, workspace_id=workspace_id)
    if workspace is None or workspace.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Workspace not found")
    return crud.create_zeros_poles(db=db, zeros_poles=zeros_poles, workspace_id=workspace_id)

@router.get("/{workspace_id}/zeros_poles", response_model=List[schemas.ZerosPoles])
def read_zeros_poles(workspace_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    workspace = crud.get_workspace(db=db, workspace_id=workspace_id)
    if workspace is None or workspace.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Workspace not found")
    return crud.get_zeros_poles(db=db, workspace_id=workspace_id)

@router.delete("/zeros_poles/{zeros_poles_id}", response_model=schemas.ZerosPoles)
def delete_zeros_poles(zeros_poles_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    zeros_poles = db.query(ZerosPoles).join(Workspace).filter(ZerosPoles.id == zeros_poles_id, Workspace.user_id == current_user.id).first()
    if zeros_poles is None:
        raise HTTPException(status_code=404, detail="Zeros or Poles not found")
    crud.delete_zeros_poles(db=db, zeros_poles_id=zeros_poles_id)
    return zeros_poles
