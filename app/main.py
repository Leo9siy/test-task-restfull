from typing import List

from fastapi import FastAPI, HTTPException

from app.schemas import Task, TaskCreate

app = FastAPI(
    title="Tast-Restfull",
    description="Tast-Restfull",
    version="1.0",
)


tasks: list[Task] = []


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks[task_id]


@app.put("/tasks/{task_id}", response_model=Task)
async def put_task(task_id: int, payload: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]
    task.title = payload.title if payload.title else task.title
    task.priority = payload.priority if payload.priority else task.priority
    task.is_done = payload.is_done if payload.is_done else task.is_done

    return {"message": "Task updated", "task_id": task_id}


@app.post("/tasks", response_model=Task)
async def post_task(task_schema: TaskCreate):
    id = len(tasks)
    new_task = Task(id=id, **task_schema.dict())
    tasks.append(new_task)

    return {"message": "Task created", "task_id": id}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks.pop(task_id)
    return {"message": "Task deleted"}







