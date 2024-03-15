import math
'''
def input_students():
    num_students = int(input("Enter the number of students: "))
    students = {}
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student Dob (DD-MM-YYYY): ")
        students[student_id] = {'name': student_name, 'dob': student_dob}
    return students
'''
def input_students():
    num_students = int(input("Enter the number of students: "))
    students = {}
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student Dob (DD-MM-YYYY): ")
        students[student_id] = {'name': student_name, 'dob': student_dob}

    with open('students.txt', 'w') as file:
        for student_id, student_info in students.items():
            file.write(f"{student_id}: {student_info['name']} - DOB: {student_info['dob']}\n")

    return students
'''
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = {}
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses[course_id] = {'name': course_name}
    return courses
'''
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = {}
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses[course_id] = {'name': course_name}

    with open('courses.txt', 'w') as file:
        for course_id, course_info in courses.items():
            file.write(f"{course_id}: {course_info['name']}\n")

    return courses
'''
def input_marks(students, courses):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    marks = float(input("Enter student marks for this course: "))
    marks = math.floor(marks * 10) / 10  # Round down to 1 decimal place
    if student_id in students and course_id in courses:
        if 'marks' not in students[student_id]:
            students[student_id]['marks'] = {}
        students[student_id]['marks'][course_id] = marks
    else:
        print("Student or course not found.")
'''
def input_marks(students, courses):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    marks = float(input("Enter student marks for this course: "))
    marks = math.floor(marks * 10) / 10  # Round down to 1 decimal place
    if student_id in students and course_id in courses:
        if 'marks' not in students[student_id]:
            students[student_id]['marks'] = {}
        students[student_id]['marks'][course_id] = marks

        with open('marks.txt', 'a') as file:
            file.write(f"{student_id}: {students[student_id]['name']} - {course_id}: {marks}\n")
    else:
        print("Student or course not found.")