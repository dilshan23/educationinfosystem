import psycopg2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to fetch student data with classroom and term marks from the PostgreSQL database
def get_student_data():
    connection = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='chess004'
    )
    cursor = connection.cursor()
    cursor.execute('''
        SELECT s.name, c.room_number, t.subject, t.marks, t.year
        FROM TermMark t
        INNER JOIN Student s ON t.student_id = s.student_id
        INNER JOIN ClassRoom c ON t.classroom_id = c.classroom_id
        WHERE t.term = 'Term 1' AND s.student_id = 1
    ''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    print(data)
    return data

# Function to generate the PDF report
def generate_pdf_report(data):
    pdf_filename = 'student_report.pdf'
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Set up the PDF content
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, "Student Report")
    c.drawString(100, 770, "Name | Classroom | Subject | Marks | Year")
    c.drawString(100, 750, "-" * 60)

    # Iterate through the data and add it to the PDF
    y = 730
    for student_info in data:
        student_info_str = " | ".join(str(info) for info in student_info)
        c.drawString(100, y, student_info_str)
        y -= 20

    c.save()
    print(f"PDF report generated: {pdf_filename}")

if __name__ == "__main__":
    student_data = get_student_data()
    generate_pdf_report(student_data)
