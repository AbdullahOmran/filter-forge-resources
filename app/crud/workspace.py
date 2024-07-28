from sqlalchemy.orm import Session
from app.models.workspace import Workspace
from app.schemas.workspace import WorkspaceCreate

def get_workspace(db: Session, workspace_id: int):
    return db.query(Workspace).filter(Workspace.id == workspace_id).first()

def get_workspaces_by_user(db: Session, user_id: int):
    return db.query(Workspace).filter(Workspace.user_id == user_id).all()

def create_workspace(db: Session, workspace: WorkspaceCreate, user_id: int):
    db_workspace = Workspace(**workspace.dict(), user_id=user_id)
    db.add(db_workspace)
    db.commit()
    db.refresh(db_workspace)
    return db_workspace

def delete_workspace(db: Session, workspace_id: int):
    db_workspace = db.query(Workspace).filter(Workspace.id == workspace_id).first()
    db.delete(db_workspace)
    db.commit()
    