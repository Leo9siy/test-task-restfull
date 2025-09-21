from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Tast-Restfull",
    description="Tast-Restfull",
    version="1.0",
)

tasks: list[str] = []


@app.get("/tasks/")
async def get_tasks():
    return {"tasks": tasks}


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks[task_id]


@app.put("/tasks/{task_id}")
async def put_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    pass


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks.pop(task_id)
    return {"message": "Task deleted"}







