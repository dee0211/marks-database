from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE,
            password TEXT,
            subject1 INTEGER,
            subject2 INTEGER,
            subject3 INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # Initialize the database on startup

def get_marks(student_id, password):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT subject1, subject2, subject3 FROM students WHERE student_id = ? AND password = ?", (student_id, password))
    student = cursor.fetchone()
    conn.close()
    
    if student:
        return {"Subject 1": student[0], "Subject 2": student[1], "Subject 3": student[2]}
    return None

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        student_id = request.form['student_id']
        password = request.form['password']
        marks = get_marks(student_id, password)
        if marks:
            return render_template('marks.html', marks=marks)
        else:
            return "Invalid Student ID or Password. Please try again."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
