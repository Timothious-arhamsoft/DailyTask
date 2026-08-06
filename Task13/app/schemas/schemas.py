from pydantic import BaseModel, Field, ConfigDict, EmailStr
from datetime import datetime
from typing import Optional

# --User
class UserCreateSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr 
    password: str = Field(min_length=8)

class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str
    role: str

    model_config = ConfigDict(from_attributes=True)

# -- Category
class CategoryCreateSchema(BaseModel):
    name: str = Field(min_length=1, max_length=50)

class CategoryResponseSchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

# -- Note
class NoteCreateSchema(BaseModel):
    title: str = Field(default=None, min_length=1, max_length=200)
    body: Optional[str] = None
    category_id: Optional[int] = None

class NoteResponseSchema(BaseModel):
    id: int
    title: str
    body: Optional[str] = None
    owner_id: int
    category_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class NoteUpdateSchema(BaseModel):
    title: Optional[str] = Field(min_length=1, max_length=200)
    body: Optional[str] = None
    category_id: Optional[int] = None

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

