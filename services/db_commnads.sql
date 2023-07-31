postgres=# CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER,
    marks FLOAT,
    grade CHAR(1)
);




postgres=# INSERT INTO student (name, age, marks, grade) VALUES
    ('John Doe', 20, 85, 'B'),
    ('Jane Smith', 22, 92, 'A'),
    ('Michael Johnson', 19, 78, 'C'),
    ('Emily Brown', 21, 95, 'A'),
    ('William Lee', 23, 70, 'C');