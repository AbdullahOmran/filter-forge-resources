from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship


class ZerosPoles(Base):
    __tablename__ = "zeros_poles"
    id = Column(Integer, primary_key=True, index=True)
    x = Column(Float)
    y = Column(Float)
    has_conj = Column(Boolean, default=False)
    is_zero = Column(Boolean, default=True)
    workspace_id = Column(Integer, ForeignKey("workspaces.id"))

    workspace = relationship("Workspace", back_populates="zeros_poles")
