from fastapi import Depends, FastAPI
from .routers import user, auth


app = FastAPI()

app.include_router(user.router, prefix="/api/v1", tags=["users"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Hey there!"}