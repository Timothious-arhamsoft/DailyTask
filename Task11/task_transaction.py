import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
db = BASE_DIR / "tasks.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS task_audit_log(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    action TEXT NOT NULL
)
""")

conn.commit()


try:

    conn.execute("BEGIN")
    cursor.execute(
        """
        UPDATE tasks
        SET completed=1
        WHERE id=?
        """,
        (1,)
    )

    cursor.execute(
        """
        INSERT INTO task_audit_log(
            task_id,
            action
        )
        VALUES(?,?)
        """,
        (
            1,
            "Task marked completed"
        )
    )

    raise Exception("Something failed after two writes")
    conn.commit()


except Exception as e:

    print("Error:", e)
    conn.rollback()


finally:

    conn.close()
