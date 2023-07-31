postgres=# CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER,
    marks FLOAT,
    grade CHAR(1)
);




INSERT INTO student (id, name, age, marks, grade) VALUES
    (10001, 'John Doe', 20, 85, 'B'),
    (10002, 'Jane Smith', 22, 92, 'A'),
    (10003, 'Michael Johnson', 19, 78, 'C'),
    (10004, 'Emily Brown', 21, 95, 'A'),
    (10005, 'William Lee', 23, 70, 'C');
