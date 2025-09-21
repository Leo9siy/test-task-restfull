from typing import Dict, List
from schemas import Task, TaskCreate, TaskUpdate


class MemoryStore:
    def __init__(self):
        self._data: Dict[int, Task] = {}
        self._next_id = 1


    def list(self) -> List[Task]:
        return list(self._data.values())


    def create(self, payload: TaskCreate) -> Task:
        tid = self._next_id
        self._next_id += 1
        task = Task(id=tid, title=payload.title, is_done=False)
        self._data[tid] = task

        return task


    def update(self, task_id: int, payload: TaskUpdate) -> Task:
        if task_id not in self._data:
            raise KeyError("Task not found")
        current = self._data[task_id]
        updated = current.model_copy(update={
        **({"title": payload.title} if payload.title is not None else {}),
        **({"is_done": payload.is_done} if payload.is_done is not None else {}),
        })
        self._data[task_id] = updated

        return updated


    def delete(self, task_id: int) -> None:
        if task_id not in self._data:
           raise KeyError("Task not found")
        del self._data[task_id]


store = MemoryStore()
