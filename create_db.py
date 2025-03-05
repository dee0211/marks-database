import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create the 'students' table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        subject1 INTEGER,
        subject2 INTEGER,
        subject3 INTEGER
    )
""")

# Commit changes and close connection
conn.commit()
conn.close()

print("✅ Database and table created successfully!")


