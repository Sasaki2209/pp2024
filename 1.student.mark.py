# Practical work 1

# Initialize empty dictionaries to store student and course information
students = {}
courses = {}

# Input
def input_students():
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student Dob (DD-MM-YYYY): ")
        students[student_id] = {'name': student_name, 'dob': student_dob}

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses[course_id] = {'name': course_name}

def input_marks():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    marks = float(input("Enter student marks for this course: "))
    if student_id in students and course_id in courses:
        if 'marks' not in students[student_id]:
            students[student_id]['marks'] = {}
        students[student_id]['marks'][course_id] = marks
    else:
        print("Student or course not found.")

# Listing
def list_courses():
    print("Courses:")
    for course_id, course_info in courses.items():
        print(f"{course_id}: {course_info['name']}")

def list_students():
    print("Students:")
    for student_id, student_info in students.items():
        print(f"{student_id}: {student_info['name']}")

def show_student_marks():
    student_id = input("Enter student ID: ")
    if student_id in students:
        print(f"Student: {students[student_id]['name']}")
        print("Marks:")
        for course_id, marks in students[student_id].get('marks', {}).items():
            print(f"{courses[course_id]['name']}: {marks}")
    else:
        print("Student not found.")

# Main
while True:
    print("\nStudent Mark Management System")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input student marks")
    print("4. List courses")
    print("5. List students")
    print("6. Show student marks")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        input_students()
    elif choice == '2':
        input_courses()
    elif choice == '3':
        input_marks()
    elif choice == '4':
        list_courses()
    elif choice == '5':
        list_students()
    elif choice == '6':
        show_student_marks()
    elif choice == '0':
        break
    else:
        print("Invalid choice")
