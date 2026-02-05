CREATE DATABASE student_performance;
USE student_performance;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    subject VARCHAR(30),
    marks INT,
    result VARCHAR(10)
);
