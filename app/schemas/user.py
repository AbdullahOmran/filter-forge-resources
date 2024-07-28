from pydantic import BaseModel, EmailStr
from typing import Union



class UserBase(BaseModel):
    username: str
    email: Union[EmailStr, None] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool

    class Config:
        # orm_mode = True  <deprecated>
        from_attributes = True