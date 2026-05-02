from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pendente"
    priority: Optional[str] = "media"
    completed: Optional[bool] = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    completed: Optional[bool] = None

class TaskResponse(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class AIGenerateRequest(BaseModel):
    title: str

class AIGenerateResponse(BaseModel):
    description: str
    priority: str
    subtasks: List[str]