from fastapi import Depends, FastAPI
from .routers import user, auth
from app import models
from app.database import engine

# create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/api/v1", tags=["users"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Hey there!"}