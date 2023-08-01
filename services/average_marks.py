import psycopg2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import os

# Function to fetch student data with classroom, term, and marks from the PostgreSQL database
def get_student_data():
    connection = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password=''
    )
    cursor = connection.cursor()
    cursor.execute('''
        SELECT s.name, c.room_number, t.term, t.subject, t.marks, t.year
        FROM TermMark t
        INNER JOIN Student s ON t.student_id = s.student_id
        INNER JOIN ClassRoom c ON t.classroom_id = c.classroom_id
        WHERE t.term = 'Term 1' AND s.student_id = 1
    ''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# Function to calculate the average marks for all subjects
def calculate_average_marks(data):
    total_marks = 0
    num_subjects = len(data)
    for student_info in data:
        total_marks += student_info[4]  # Index 4 corresponds to the marks in the student_info tuple
    return total_marks / num_subjects

# Function to generate the PDF report
def generate_pdf_report(data):
    pdf_filename = 'student_report.pdf'
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Set up the PDF content
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, "Student Report")
    c.drawString(100, 770, "Name | Classroom | Term | Subject | Marks | Year")
    c.drawString(100, 750, "-" * 80)

    # Iterate through the data and add it to the PDF
    y = 730
    total_marks = 0
    for student_info in data:
        student_info_str = " | ".join(str(info) for info in student_info)
        c.drawString(100, y, student_info_str)
        y -= 20
        total_marks += student_info[4]  # Index 4 corresponds to the marks in the student_info tuple

    # Calculate average marks
    num_subjects = len(data)
    average_marks = total_marks / num_subjects

    # Add the average marks at the bottom of the PDF
    c.drawString(100, y - 40, f"Average Marks for all Subjects: {average_marks:.2f}")

    c.save()
    print(f"PDF report generated: {pdf_filename}")

if __name__ == "__main__":
    student_data = get_student_data()
    generate_pdf_report(student_data)
