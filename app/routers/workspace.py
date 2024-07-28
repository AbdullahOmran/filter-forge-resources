from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.api.v1.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=schemas.Workspace)
def create_workspace(workspace: schemas.WorkspaceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_workspace(db=db, workspace=workspace, user_id=current_user.id)

@router.get("/", response_model=List[schemas.Workspace])
def read_workspaces(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_workspaces_by_user(db=db, user_id=current_user.id)

@router.delete("/{workspace_id}", response_model=schemas.Workspace)
def delete_workspace(workspace_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    workspace = crud.get_workspace(db=db, workspace_id=workspace_id)
    if workspace is None or workspace.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Workspace not found")
    crud.delete_workspace(db=db, workspace_id=workspace_id)
    return workspace

