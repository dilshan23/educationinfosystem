postgres=# INSERT INTO student (id,name, age, marks, grade) VALUES
    (0001,'John Doe', 20, 85, 'B'),
    (0002,'Jane Smith', 22, 92, 'A'),
    (0003,'Michael Johnson', 19, 78, 'C'),
    (0004,'Emily Brown', 21, 95, 'A'),
    (0005,'William Lee', 23, 70, 'C');



postgres=# -- Create the Subject table
CREATE TABLE Subject (
    subject_id SERIAL PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL
);
CREATE TABLE
postgres=# -- Insert data into the Subject table
INSERT INTO Subject (subject_name)
VALUES
    ('English'),
    ('Math'),
    ('Science'),
    ('History'),
    ('Art');
INSERT 0 5
postgres=# CREATE TABLE Teacher (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    subject_taught VARCHAR(100)
);
CREATE TABLE
postgres=# -- Modify the ClassRoom table
CREATE TABLE ClassRoom (
    classroom_id SERIAL PRIMARY KEY,   
    room_number VARCHAR(20) NOT NULL,
    grade_level VARCHAR(10) NOT NULL,
    subject_id INTEGER REFERENCES Subject(subject_id),
    teacher_id INTEGER REFERENCES Teacher(teacher_id)
);
CREATE TABLE
postgres=# CREATE TABLE TermMark (
    mark_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES Student(student_id),
    classroom_id INTEGER REFERENCES ClassRoom(classroom_id),
    term VARCHAR(20),
    subject VARCHAR(100),
    marks INTEGER
);
CREATE TABLE
postgres=# INSERT INTO ClassRoom (room_number, grade_level)
VALUES
    ('101', 'Grade 1'),
    ('202', 'Grade 2');
INSERT 0 2
postgres=# INSERT INTO TermMark (student_id, classroom_id, term, subject, marks) 
VALUES
    (1, 1, 'Term 1', 'Math', 90),
    (1, 1, 'Term 1', 'English', 85),
    (1, 2, 'Term 2', 'Math', 92),
    (2, 1, 'Term 1', 'Math', 88),
    (2, 2, 'Term 1', 'Science', 78);
INSERT 0 5
postgres=# INSERT INTO Teacher (first_name, last_name, email, subject_taught)
VALUES
    ('Alice', 'Johnson', 'alice.johnson@example.com', 'Math'),
    ('Bob', 'Anderson', 'bob.anderson@example.com', 'English');
INSERT 0 2
postgres=# INSERT INTO ClassRoom (room_number, grade_level, teacher_id)
VALUES
    ('101', 'Grade 1', 1),  -- Classroom with teacher Alice Johnson (teacher_id = 1)
    ('202', 'Grade 2', 2),  -- Classroom with teacher Bob Anderson (teacher_id = 2)
    ('303', 'Grade 3', NULL); -- Classroom without a teacher (teacher_id = NULL)
INSERT 0 3
postgres=# -- Query the ClassRoom table with teacher information
SELECT c.classroom_id, c.room_number, c.grade_level, t.first_name || ' ' || t.last_name AS teacher_name
FROM ClassRoom c
LEFT JOIN Teacher t ON c.teacher_id = t.teacher_id;
 classroom_id | room_number | grade_level | teacher_name  
--------------+-------------+-------------+---------------
            1 | 101         | Grade 1     | 
            2 | 202         | Grade 2     | 
            3 | 101         | Grade 1     | Alice Johnson
            4 | 202         | Grade 2     | Bob Anderson
            5 | 303         | Grade 3     | 
(5 rows)

-- ---------------------------

SELECT t.subject, t.marks , t.year
FROM TermMark t
INNER JOIN Student s ON t.student_id = s.student_id
WHERE t.term = 'Term 1' AND s.student_id = 1;


 subject | marks 
---------+-------
 Math    |    90
 English |    85
(2 rows)




-- ----------------
postgres=# ALTER TABLE TermMark
ADD COLUMN year INTEGER;
ALTER TABLE
postgres=# UPDATE TermMark
SET year = 2023
WHERE student_id = 1 AND term = 'Term 1';
UPDATE 2


postgres=# SELECT s.name ,t.subject, t.marks , t.year
FROM TermMark t
INNER JOIN Student s ON t.student_id = s.student_id
WHERE t.term = 'Term 1' AND s.student_id = 1;
 subject | marks | year 
---------+-------+------
 Math    |    90 | 2023
 English |    85 | 2023



-- ----

SELECT s.name, c.room_number, t.subject, t.marks, t.year
FROM TermMark t
INNER JOIN Student s ON t.student_id = s.student_id
INNER JOIN ClassRoom c ON t.classroom_id = c.classroom_id
WHERE t.term = 'Term 1' AND s.student_id = 1;


   name   | room_number | subject | marks | year 
----------+-------------+---------+-------+------
 John Doe | 101         | Math    |    90 | 2023
 John Doe | 101         | English |    85 | 2023




-- Modify class room table

-- Insert data into the ClassRoom table with subject and teacher assignments
INSERT INTO ClassRoom (room_number, grade_level, subject_id, teacher_id)
VALUES
    ('101', 'Grade 1', 1, 1), -- Classroom 101 with subject Math taught by teacher Alice
    ('202', 'Grade 2', 2, 2), -- Classroom 202 with subject English taught by teacher Bob
    ('303', 'Grade 3', 3, 2); -- Classroom 303 with subject Science taught by teacher Bob


postgres=# SELECT
    c.room_number AS classroom,
    c.grade_level AS grade,
    s.subject_name AS subject,
    t.first_name || ' ' || t.last_name AS teacher_name
FROM
    ClassRoom c
INNER JOIN
    Subject s ON c.subject_id = s.subject_id
INNER JOIN
    Teacher t ON c.teacher_id = t.teacher_id;
 classroom |  grade  | subject | teacher_name  
-----------+---------+---------+---------------
 101       | Grade 1 | English | Alice Johnson
 202       | Grade 2 | Math    | Bob Anderson
 303       | Grade 3 | Science | Bob Anderson
(3 rows)




