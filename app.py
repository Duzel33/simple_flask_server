from flask import Flask, jsonify

# We create a Flask application by initializing the `app` object.
app = Flask(__name__)

# Sample student data
students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

# We define a route `/students/old_students` that returns students older than 20
@app.route('/students/old_students', methods=['GET'])
def get_old_students():
    old_students = []
    for student in students:
        if student["age"] > 20:
            old_students.append(student)
    return jsonify(old_students)

# We define a route `/students/young_students` that returns students younger than 21
@app.route('/students/young_students', methods=['GET'])
def young_students():
    young_students = []
    for student in students:
        if student["age"] < 21:
            young_students.append(student)
    return jsonify(young_students)

# We define a route `/students/advance_students` that returns students younger than 21 with A's
@app.route('/students/advance_students', methods=['GET'])
def advance_students():
    advance_students = []
    for student in students:
        if student["age"] < 21 and student["grade"] == "A":
            advance_students.append(student)
    return jsonify(advance_students)

# We define a route `/students/student_names` that returns first and last names
@app.route('/students/student_names', methods=['GET'])
def student_names():
    student_names = []
    for student in students:
        first_name = student["first_name"]
        last_name = student["last_name"]
        student_names.append(f"first_name: {first_name} , last_name: {last_name}")
    return jsonify(student_names)

# We define a route `/students/student_ages` that returns full names and ages
@app.route('/students/student_ages', methods=['GET'])
def student_ages():
    student_ages = []
    for student in students:
        first_name = student["first_name"]
        last_name = student["last_name"]
        age = student["age"]
        student_ages.append(f"student_name: {first_name} {last_name}, age: {age}")
    return jsonify(student_ages)

# We define a route `/students` that returns all student information
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)