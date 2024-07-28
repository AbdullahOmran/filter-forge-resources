from sqlalchemy.orm import Session
from app.models.zeros_poles import ZerosPoles
from app.schemas.workspace import ZerosPolesCreate


def get_zeros_poles(db: Session, workspace_id: int):
    return db.query(ZerosPoles).filter(ZerosPoles.workspace_id == workspace_id).all()

def create_zeros_poles(db: Session, zeros_poles: ZerosPolesCreate, workspace_id: int):
    db_zeros_poles = ZerosPoles(**zeros_poles.dict(), workspace_id=workspace_id)
    db.add(db_zeros_poles)
    db.commit()
    db.refresh(db_zeros_poles)
    return db_zeros_poles

def delete_zeros_poles(db: Session, zeros_poles_id: int):
    db_zeros_poles = db.query(ZerosPoles).filter(ZerosPoles.id == zeros_poles_id).first()
    db.delete(db_zeros_poles)
    db.commit()
