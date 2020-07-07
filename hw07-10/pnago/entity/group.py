"""
Група з полями назва, студенти(list).
Перевизначити  методи __init__, __str__, __repr__
Визнасити метод add_student, print_students, is_contain(Людина)
"""


class Group:
    def __init__(self, group_title, students):
        self.group_title = group_title
        self.students = students

    def __str__(self):
        return f"Group title: {self.group_title}. Students in group: {self.students}."

    def __repr__(self):
        return f"{self.group_title}, {self.students}"

    def add_student(self, student_name):
        self.students.append(student_name)

    def print_students_list(self):
        print(f"Students list: {self.students}")

    def is_contain(self, student_name):
        return student_name in self.students
