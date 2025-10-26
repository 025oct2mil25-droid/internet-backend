from pydantic import BaseModel, EmailStr
from typing import Optional

# Usuario
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

# Token
class Token(BaseModel):
    access_token: str
    token_type: str

# Item
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True
