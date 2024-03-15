def list_students_by_gpa(students, courses):
    sorted_students = sorted(students.items(), key=lambda x: calculate_gpa(x[1], courses), reverse=True)
    for student_id, student_info in sorted_students:
        print(f"{student_id}: {student_info['name']} - GPA: {calculate_gpa(student_info, courses)}")

def show_student_marks(students, courses):
    student_id = input("Enter student ID: ")
    if student_id in students:
        print(f"Student: {students[student_id]['name']}")
        print("Marks:")
        for course_id, marks in students[student_id].get('marks', {}).items():
            print(f"{courses[course_id]['name']}: {marks}")
    else:
        print("Student not found.")

def calculate_gpa(student, courses):
    total_credits = 0
    weighted_sum = 0
    for course_id, marks in student.get('marks', {}).items():
        if course_id in courses:
            credit = 1  # Assuming each course has 1 credit
            total_credits += credit
            weighted_sum += marks * credit
    if total_credits == 0:
        return 0
    return weighted_sum / total_credits