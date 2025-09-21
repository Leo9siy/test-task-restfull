from typing import List

from fastapi import FastAPI, HTTPException

from schemas import Task, TaskUpdate, TaskCreate
from storage import store

app = FastAPI()


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return store.list()


@app.post(
    "/tasks",
    response_model=Task,
    status_code=201
)
async def create_task(create_task: TaskCreate):
    return store.create(create_task)


@app.put(
    "/tasks/{task_id}",
    response_model=Task,
    status_code=201
)
async def update_task(payload: TaskUpdate):
    try:
        return store.update(payload)
    except KeyError:
        raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
async def delete_task(payload: Task):
    try:
        store.delete(payload)
        return {"message": "Task deleted"}
    except KeyError:
        raise HTTPException(status_code=404, detail="Task not found")

