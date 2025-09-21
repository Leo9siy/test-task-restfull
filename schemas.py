from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    is_done: bool = False


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(..., min_length=1, max_length=100)
    is_done: Optional[bool] = None


class Task(TaskBase):
    id: int
