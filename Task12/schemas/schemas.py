from pydantic import BaseModel

# Category
class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True

# Tasks
class TaskCreate(BaseModel):
    title: str
    completed: bool = False
    category_id: int | None = None

class TaskUpdate(BaseModel):
    title: str
    completed: bool
    category_id: int | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    created_at: str
    category_id: int | None = None
    class Config:
        from_attributes = True

