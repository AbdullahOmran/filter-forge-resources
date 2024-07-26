from fastapi import APIRouter, Depends
from typing import Annotated, Union
from app.dependencies import get_current_active_user



router = APIRouter()


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user
