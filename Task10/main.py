from fastapi import FastAPI, HTTPException, Response, status, APIRouter

# Task 1: fastapi uvicorn
app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello FastAPI!"}

# Command: uvicorn Task10.main:app --reload


# Task2: Designing the Task resource
from pathlib import Path
import json


def task2():
    base = Path(__file__).parent
    json_file = base / "task2.json"

    with json_file.open() as file:
        tasks = json.load(file)


    print(f"{'Operation':<15} {'Method':<10} {'URL':<20} {'Success status'}")
    print("-" * 70)
    for task in tasks:
        print(
            f"{task['operation']:<15}"
            f"{task['method']:<10}"
            f"{task['url']:<20}"
            f"{task['success_status']}"
        )

# Task 3: Implement 5 Endpoints
from pydantic import BaseModel
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

'''
Tested the Api using Swagger

url: http://127.0.0.1:8000/docs

'''

# Task 4: Annotated 
'''
*   Trying 127.0.0.1:8000...
* Connected to 127.0.0.1 (127.0.0.1) port 8000 (#0)

> GET /tasks HTTP/1.1          <-- Request Line
> Host: 127.0.0.1:8000         <-- Request Header
> User-Agent: curl/7.81.0      <-- Request Header
> Accept: */*                  <-- Request Header
>                              
                               <-- (No Request Body because this is a GET request)

* Mark bundle as not supporting multiuse

< HTTP/1.1 200 OK              <-- Status Line
< date: Thu, 30 Jul 2026 ...   <-- Response Header
< server: uvicorn              <-- Response Header
< content-length: 2            <-- Response Header
< content-type: application/json <-- Response Header
<
[]                             <-- Response Body

* Connection #0 to host 127.0.0.1 left intact

'''
# Task 5: Api Versioning
task_router = APIRouter(prefix="/api/v1/tasks", tags=["Tasks"])

# if v2 needed to rename a field without breaking existing v1 clients, what would you actually do?
'''
I would keep /api/v1/tasks unchanged for existing clients and create a separate /api/v2/tasks 
endpoint with the renamed field so both versions can run during migration.

'''


class TaskV1(BaseModel):
    name: str
    completed : bool = False

@task_router.post("", status_code=201)
async def create_task_v2(task: TaskV1):
    new_task_id =  max(tasks_v1.keys(), default=0) + 1

    tasks_v1[new_task_id] = {
        "id": new_task_id,
        **task.model_dump()
    }

    return tasks_v1[new_task_id]

app.include_router(task_router)


# Task 6: syncio lesson concrete
import asyncio
@app.get("/slow")
async def slow_endpoint():
    await asyncio.sleep(2)

    return {
        "message": "Finished after 2 seconds"
    }

def main():
    task2()

if __name__ == "__main__":
    main()