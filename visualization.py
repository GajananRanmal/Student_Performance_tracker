import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1603",
    database="student_performance"
)

# Query data
query = "SELECT subject, marks, result FROM students"
df = pd.read_sql(query, connection)

connection.close()

# ---- Graph 1: Subject-wise Average Marks ----
subject_avg = df.groupby("subject")["marks"].mean()

plt.figure()
subject_avg.plot(kind="bar")
plt.title("Subject-wise Average Marks")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# ---- Graph 2: Pass vs Fail Count ----
result_count = df["result"].value_counts()

plt.figure()
result_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Fail Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()
