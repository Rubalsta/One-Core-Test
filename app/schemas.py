from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class User(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id_usuario: Optional[int] = None
    rol: Optional[str] = None
