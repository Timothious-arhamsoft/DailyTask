import sqlite3

conn = sqlite3.connect("tasks.db")

cursor = conn.cursor()

title = input("Enter title: ")

query = "SELECT * FROM tasks WHERE title=?"
"""
The vulnerable query concatenated user input directly into SQL, 
allowing the input to modify the query structure. The parameterized 
query uses placeholders (?) so SQLite separates SQL code from user data, 
preventing the input from being executed as SQL.
"""
print(query)

cursor.execute(query, (title,))

print(cursor.fetchall())

conn.close()

