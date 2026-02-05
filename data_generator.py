import mysql.connector
import random

TOTAL_STUDENTS = 1000
SUBJECTS = ["Maths", "Physics", "Chemistry", "English"]

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1603",
    database="student_performance"
)

cursor = connection.cursor()

for i in range(1, TOTAL_STUDENTS + 1):
    student_name = f"Student_{i}"

    for subject in SUBJECTS:
        marks = random.randint(20, 100)
        result = "Pass" if marks >= 35 else "Fail"

        cursor.execute(
            "INSERT INTO students (name, subject, marks, result) VALUES (%s, %s, %s, %s)",
            (student_name, subject, marks, result)
        )

connection.commit()
cursor.close()
connection.close()

print("✅ 4000 records inserted successfully")
