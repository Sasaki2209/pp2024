import math

class MarkManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def calculate_gpa(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            total_credits = 0
            weighted_sum = 0
            for course_id, marks in student.get('marks', {}).items():
                if course_id in self.courses:
                    credit = 1  # I prefer that each course have 1 credit
                    total_credits += credit
                    weighted_sum += marks * credit
            if total_credits == 0:
                return 0
            return weighted_sum / total_credits
        else:
            return 0