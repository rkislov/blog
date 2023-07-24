from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional

class UserCreate(BaseModel):
    email : EmailStr
    password : str = Field(..., min_length=6)



class ShowUser(BaseModel):
    id: UUID
    firstname: Optional[str] = None
    lastname: Optional[str] = None 
    email: str
    is_active: bool

    class Config():
        orm_mode = True