from fastapi import Depends, FastAPI
from .routers import user, auth, workspace, zeros_poles
from app import models
from app.database import engine

# create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/api/v1", tags=["users"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(workspace.router, prefix="/api/v1/workspace", tags=["workspaces"])
app.include_router(zeros_poles.router,prefix="/api/v1/workspace", tags=["zeros and poles"])

@app.get("/")
async def root():
    return {"message": "Hey there!"}