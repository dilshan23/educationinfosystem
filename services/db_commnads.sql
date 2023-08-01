-- Create Student Table
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    address TEXT,
    email VARCHAR(100),
    whatsapp VARCHAR(100),
);

INSERT INTO Students (name, date_of_birth, address, email, whatsapp)
VALUES
    ('John Doe', '1995-08-15', '123 Main St, City', 'john.doe@example.com', '+1234567890'),
    ('Jane Smith', '1998-04-20', '456 Elm St, Town', 'jane.smith@example.com', '+9876543210'),
    ('Michael Johnson', '1999-12-10', '789 Oak St, Village', 'michael.johnson@example.com', '+1112223334'),
    ('Emily Brown', '1997-07-25', '101 Maple St, County', 'emily.brown@example.com', '+4445556667'),
    ('William Lee', '2000-02-05', '222 Pine St, Suburb', 'william.lee@example.com', '+8889990001');




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



--   ADD year to classroom table


-- To update the "ClassRoom" table to include the "year" column and add the corresponding data, you need to use the ALTER TABLE statement to add the new column and then use UPDATE statements to populate the "year" values for each classroom.

-- Let's first modify the "ClassRoom" table:

-- sql
-- Copy code
-- -- Step 1: Add the "year" column to the ClassRoom table
ALTER TABLE ClassRoom
ADD COLUMN year INTEGER;
-- Now, you can insert the data into the "ClassRoom" table along with the "year" information:

-- sql
-- Copy code
-- -- Step 2: Insert data into the ClassRoom table with subject, teacher, and year assignments
INSERT INTO ClassRoom (room_number, grade_level, subject_id, teacher_id, year)
VALUES
    ('101', 'Grade 1', 1, 1, 2023), -- Classroom 101 with subject Math taught by teacher Alice in 2023
    ('202', 'Grade 2', 2, 2, 2023), -- Classroom 202 with subject English taught by teacher Bob in 2023
    ('303', 'Grade 3', 3, 2, 2023); -- Classroom 303 with subject Science taught by teacher Bob in 2023
-- In this updated "ClassRoom" table, the "year" column is now added, and the data is inserted into the table with the specified year (2023 in this case) for each classroom along with the subject and teacher assignments.

-- Now, each row in the "ClassRoom" table will have a "year" value, which represents the academic year in which the subject is taught by the teacher in that classroom. The "year" information allows you to differentiate the subject-teacher-classroom assignments for different years.



postgres=# SELECT
    s.subject_name AS subject,
    t.first_name || ' ' || t.last_name AS teacher_name
FROM
    ClassRoom c
INNER JOIN
    Subject s ON c.subject_id = s.subject_id
INNER JOIN
    Teacher t ON c.teacher_id = t.teacher_id
WHERE
    c.room_number = '101'
    -- Assuming year is stored in the year column of ClassRoom table
    AND c.year = 2023;
 subject | teacher_name  
---------+---------------
 English | Alice Johnson
(1 row)

