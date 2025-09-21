from typing import Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str
    priority: str
    is_done: bool


class TaskCreate(BaseModel):
    title: str
    priority: Optional[str] = "Low"
    is_done: Optional[bool] = False

    class Config:
        from_attributes = True
