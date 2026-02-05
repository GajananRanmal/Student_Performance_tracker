-- View all records
SELECT * FROM students;

-- Subject-wise average marks
SELECT subject, AVG(marks) AS average_marks
FROM students
GROUP BY subject;

-- Pass vs Fail count
SELECT result, COUNT(*) AS total
FROM students
GROUP BY result;

-- Top 10 students
SELECT name, AVG(marks) AS avg_marks
FROM students
GROUP BY name
ORDER BY avg_marks DESC
LIMIT 10;
