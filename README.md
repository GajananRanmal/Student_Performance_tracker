
# 🎓 Student Performance SQL Tracker

<p align="center">
  <img src="https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge&logo=mysql">
  <img src="https://img.shields.io/badge/Python-Data%20Analysis-yellow?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Project-Mini%20Project-green?style=for-the-badge">
</p>

<p align="center">
📊 A data-driven system to analyze and visualize student academic performance using SQL & Python
</p>

---

## 🔍 Project Overview
**Student Performance SQL Tracker** is a mini project that demonstrates how **MySQL and Python** can be combined to store, analyze, and visualize academic data efficiently.

The system helps identify:
- Subject-wise performance trends  
- Pass vs Fail statistics  
- Top-performing students  

---

## 🎯 Objectives
- Design a structured MySQL database  
- Generate realistic student datasets using Python  
- Analyze academic data using SQL queries  
- Visualize results using charts  
- Understand database-driven analytics  

---

## 🛠️ Tech Stack
| Technology | Purpose |
|----------|---------|
| MySQL | Database creation & querying |
| Python | Data generation & visualization |
| Pandas | Data processing |
| Matplotlib | Graph plotting |
| Windows OS | Development environment |

---

## 📂 Project Structure
```
Student_Performance_SQL_Tracker/
│
├── Source_Code/
│   ├── data_generator.py
│   ├── visualization.py
│
├── SQL_Files/
│   ├── database.sql
│   ├── analysis_queries.sql
│
├── Dataset/
│   ├── student_data.csv
│
├── Report/
│   └── Student_Performance_SQL_Tracker_Report.pdf
│
└── README.md
```

---

## 🧩 Database Schema
**Table Name:** `students`

| Column | Data Type | Description |
|------|-----------|-------------|
| student_id | INT (Primary Key) | Unique student identifier |
| name | VARCHAR(50) | Student name |
| subject | VARCHAR(30) | Subject name |
| marks | INT | Marks obtained |
| result | VARCHAR(10) | Pass / Fail status |

---

## ⚙️ Workflow
1. Create MySQL database and table  
2. Generate 4000+ student records using Python  
3. Insert records automatically into database  
4. Execute SQL queries for performance analysis  
5. Visualize data using Python graphs  

---

## 📊 Analysis Performed
- Subject-wise average marks  
- Pass vs Fail distribution  
- Top-performing students  
- Overall performance trends  

---

## 🚀 How to Run the Project
```bash
pip install pandas matplotlib mysql-connector-python
```

```bash
python data_generator.py
python visualization.py
```

Ensure MySQL server is running and credentials are correctly configured.

---

## 📌 Results & Insights
- Mathematics showed comparatively lower average marks  
- Majority of students passed  
- SQL handled large datasets efficiently  
- Graphs improved data interpretation  

---

## 🔮 Future Scope
- Web-based dashboard  
- Automated grading system  
- Machine learning-based performance prediction  
- Real-time data entry and analytics  

---

## 👨‍💻 Author
**Gajanan Govind Ranmal**  
ENTC Engineering Student  
Interested in Data Analytics, SQL, Python & IoT  

---

## ⭐ Support
If you like this project:
- ⭐ Star the repository  
- 🍴 Fork it  
- 📢 Share it  
