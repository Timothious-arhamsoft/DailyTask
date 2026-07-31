# Task1: Added and run the Task 10 main.py
# Command: uvicorn Task11.main:app --reload
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
import sqlite3
from datetime import datetime
from pathlib import Path

# Creating the database
# Task 2: Replaced Dictionary with SQLite
BASE_DIR = Path(__file__).resolve().parent
db = BASE_DIR / "tasks.db"

def make_connection():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = make_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()




app = FastAPI()
init_db()

@app.get("/")
async def home():
    return {"message": "Hello FastAPI!"}



class Task(BaseModel):
    title: str
    completed : bool = False


# Task 3: Change Every Endpoint
#-----------------------------------------
# 1: Get all tasks
@app.get("/tasks")
async def get_tasks():

    conn = make_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        title,
        completed,
        created_at
    FROM tasks
    """)

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "id": row["id"],
            "title": row["title"],
            "completed": bool(row["completed"]),
            "created_at": row["created_at"]
        }
        for row in rows
    ]

# 2: Task according to id
@app.get("/tasks/{task_id}")
async def get_task(task_id:int):

    conn = make_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT
            id,
            title,
            completed,
            created_at
        FROM tasks
        WHERE id=?
        """,
        (task_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "id": row["id"],
        "title": row["title"],
        "completed": bool(row["completed"]),
        "created_at": row["created_at"]
    }


# 3: Createing task
@app.post("/tasks", status_code=201)
async def post_task(task: Task):

    conn = make_connection()
    cursor = conn.cursor()
    created_at = datetime.now().isoformat()
    cursor.execute(
        """
        INSERT INTO tasks(
            title,
            completed,
            created_at
        )
        VALUES(?,?,?)
        """,
        (
            task.title,
            task.completed,
            created_at
        )
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {
        "id": new_id,
        "title": task.title,
        "completed": task.completed,
        "created_at": created_at
    }

# 4: UPdate task
@app.put("/tasks/{task_id}")
async def put_task(task_id:int, task:Task):

    conn = make_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE tasks
        SET title=?,
            completed=?
        WHERE id=?
        """,
        (
            task.title,
            task.completed,
            task_id
        )
    )
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    conn.close()
    return {
        "id": task_id,
        "title": task.title,
        "completed": task.completed
    }

# 5: Delete task
@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id:int):

    conn = make_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    conn.close()
    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )
#-----------------------------------------

