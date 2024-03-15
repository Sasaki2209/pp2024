from input import input_students, input_courses, input_marks
from output import list_students_by_gpa, show_student_marks

students = {}
courses = {}

while True:
    print("\nStudent Mark Management System")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input student marks")
    print("4. List courses")
    print("5. List students by GPA")
    print("6. Show student marks")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        students = input_students()
    elif choice == '2':
        courses = input_courses()
    elif choice == '3':
        input_marks(students, courses)
    elif choice == '4':
        for course_id, course_info in courses.items():
            print(f"{course_id}: {course_info['name']}")
    elif choice == '5':
        list_students_by_gpa(students, courses)
    elif choice == '6':
        show_student_marks(students, courses)
    elif choice == '0':
        break
    else:
        print("Invalid choice")