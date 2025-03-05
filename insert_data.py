import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Sample student records to insert
students = [
    ("S101", "pass123", 85, 90, 78),
    ("S102", "secure456", 75, 88, 92),
    ("S103", "hello789", 95, 87, 80),
    ("S104", "mypassword", 70, 60, 65),
    ("S105", "testpass", 88, 76, 91)
]

# Insert records into the database
cursor.executemany("INSERT INTO students (student_id, password, subject1, subject2, subject3) VALUES (?, ?, ?, ?, ?)", students)

# Commit changes and close connection
conn.commit()
conn.close()


