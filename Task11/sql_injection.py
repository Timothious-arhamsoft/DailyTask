# Task 3: SQL-injection 

import sqlite3

conn = sqlite3.connect("tasks.db")

cursor = conn.cursor()

title = input("Enter title: ")

query = f"SELECT * FROM tasks WHERE title='{title}'"

print(query)

cursor.execute(query)

print(cursor.fetchall())

conn.close()