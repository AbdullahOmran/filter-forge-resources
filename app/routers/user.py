from fastapi import APIRouter, Depends
from typing import Annotated, Union
from app.dependencies import get_current_active_user
from app import schemas



router = APIRouter()


@router.get("/users/me", response_model=schemas.User)
async def read_users_me(
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
):
    return current_user
