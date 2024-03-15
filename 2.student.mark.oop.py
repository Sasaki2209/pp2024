#Pracical work 2

#Class
class MarkManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def input(self):
        pass

    def list(self):
        pass

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student Dob (DD-MM-YYYY): ")
            self.students[student_id] = {'name': student_name, 'dob': student_dob}

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            self.courses[course_id] = {'name': course_name}

    def input_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        marks = float(input("Enter student marks for this course: "))
        if student_id in self.students and course_id in self.courses:
            if 'marks' not in self.students[student_id]:
                self.students[student_id]['marks'] = {}
            self.students[student_id]['marks'][course_id] = marks
        else:
            print("Student or course not found.")

    def list_courses(self):
        print("Courses:")
        for course_id, course_info in self.courses.items():
            print(f"{course_id}: {course_info['name']}")

    def list_students(self):
        print("Students:")
        for student_id, student_info in self.students.items():
            print(f"{student_id}: {student_info['name']}")

    def show_student_marks(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            print(f"Student: {self.students[student_id]['name']}")
            print("Marks:")
            for course_id, marks in self.students[student_id].get('marks', {}).items():
                print(f"{self.courses[course_id]['name']}: {marks}")
        else:
            print("Student not found.")

# Main
system = MarkManagementSystem()
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
        system.input_students()
    elif choice == '2':
        system.input_courses()
    elif choice == '3':
        system.input_marks()
    elif choice == '4':
        system.list_courses()
    elif choice == '5':
        system.list_students()
    elif choice == '6':
        system.show_student_marks()
    elif choice == '0':
        break
    else:
        print("Invalid choice")