
import sqlite3
import re

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)''')

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def add_student(name, email):
    if not is_valid_email(email):
        print("Invalid email format.")
        return
    try:
        cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("Student added successfully.")
    except sqlite3.IntegrityError:
        print("Duplicate entry. Email already exists.")

def show_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

# Example Usage
add_student("Alice", "alice@example.com")
add_student("Bob", "bob@example.com")
add_student("Alice", "alice@example.com")  # Duplicate
show_students()

conn.close()
