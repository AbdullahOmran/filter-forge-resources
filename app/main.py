from fastapi import Depends, FastAPI

from .internal import admin
from .routers import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hey there!"}