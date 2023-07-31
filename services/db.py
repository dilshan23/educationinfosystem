import psycopg2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to fetch student data from the PostgreSQL database
def get_student_data():
    connection = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password=''
    )
    cursor = connection.cursor()
    cursor.execute('SELECT id,name, age, marks, grade FROM student')
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
    c.drawString(100, 770, "ID | Name | Age | Marks | Grade")
    c.drawString(100, 750, "-" * 60)

    # Iterate through the data and add it to the PDF
    y = 730
    for student in data:
        
        student_info = f"{student[0]} | {student[1]} | {student[2]} | {student[3]}  | {student[4]}"
        c.drawString(100, y, student_info)
        y -= 20

    c.save()
    print(f"PDF report generated: {pdf_filename}")

if __name__ == "__main__":
    student_data = get_student_data()
    generate_pdf_report(student_data)
