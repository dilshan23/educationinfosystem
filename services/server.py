from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Hardcoded username and password (replace with your own)
HARDCODED_USERNAME = 'admin'
HARDCODED_PASSWORD = 'password'

import psycopg2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import os

# Function to fetch student data with classroom, term, and marks from the PostgreSQL database
# def get_student_data():
#     connection = psycopg2.connect(
#         host='localhost',
#         database='postgres',
#         user='postgres',
#         password='chess004'
#     )
#     cursor = connection.cursor()
#     cursor.execute('''
#         SELECT s.name, c.room_number, t.term, t.subject, t.marks, t.year
#         FROM TermMark t
#         INNER JOIN Student s ON t.student_id = s.student_id
#         INNER JOIN ClassRoom c ON t.classroom_id = c.classroom_id
#         WHERE t.term = 'Term 1' AND s.student_id = 1 AND t.year = '2023'
#     ''')
#     data = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return data

def get_student_data(term, student_id, year):
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
        WHERE t.term = %s AND s.student_id = %s AND t.year = %s
    ''', (term, student_id, year))
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

# if __name__ == "__main__":
#     student_data = get_student_data()
#     generate_pdf_report(student_data)


@app.route('/login', methods=['POST'])
def login():
    print(request.get_json())
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    print(username,password)

    if username == HARDCODED_USERNAME and password == HARDCODED_PASSWORD:
        response = {'message': 'Login successful'}
        # Set the 'auth_cookie' cookie in the response
        resp = make_response(jsonify(response), 200)
        #resp.set_cookie('auth_cookie', '3333333')
        resp.set_cookie('auth_cookie', '3333333', secure=False, httponly=True, domain='127.0.0.1')

        return resp
    else:
        response = {'message': 'Invalid credentials'}
        return jsonify(response), 401

@app.route('/generate_report', methods=['POST'])
def generate_report():
    # Get request data from the JSON payload
    data = request.get_json()
    term = data.get('term')
    student_id = data.get('student_id')
    year = data.get('year')

    # Validate if the required parameters are provided
    if not term or not student_id or not year:
        return jsonify({'error': 'Invalid request data'}), 400

    # Get student data using the provided parameters
    student_data = get_student_data(term, student_id, year)

    # Generate the PDF report
    generate_pdf_report(student_data)

    # Read the generated PDF file
    with open('student_report.pdf', 'rb') as f:
        pdf_content = f.read()

    # Delete the PDF file after reading its content
    os.remove('student_report.pdf')

    # Create a response with the PDF content and set appropriate headers
    response = make_response(pdf_content)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=student_report.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)
