# Command: uvicorn Task11.main:app --reload
from fastapi import FastAPI, HTTPException, Response, status, APIRouter
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello FastAPI!"}



class Task(BaseModel):
    title: str
    completed : bool = False
tasks = {}
tasks_v1 = {}

#-----------------------------------------
# 1: Get all tasks
@app.get("/tasks")
async def get_tasks():
    return list(tasks.values())

# 2: Task according to id
@app.get("/tasks/{task_id}")
async def get_task(task_id:int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

# 3: Createing task
@app.post("/tasks", status_code=201)
async def post_task(task: Task):
    new_task_id = max(tasks.keys(), default=0) + 1
    tasks[new_task_id] = {
    "id": new_task_id,
    **task.model_dump()
    }
    return {"id": new_task_id, **task.model_dump()}

# 4: UPdate task
@app.put("/tasks/{task_id}")
async def put_task(task_id:int, task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = {
    "id": task_id,
    **task.model_dump()
    }
    return tasks[task_id]

# 5: Delete task
@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id:int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
#-----------------------------------------

# Task 5: Api Versioning
task_router = APIRouter(prefix="/api/v1/tasks", tags=["Tasks"])

class TaskV1(BaseModel):
    name: str
    completed : bool = False

@task_router.post("", status_code=201)
async def create_task_v1(task: TaskV1):
    new_task_id =  max(tasks_v1.keys(), default=0) + 1

    tasks_v1[new_task_id] = {
        "id": new_task_id,
        **task.model_dump()
    }

    return tasks_v1[new_task_id]

app.include_router(task_router)


def main():
    pass

if __name__ == "__main__":
    main()