# Група з полями назва, студенти(list).
# Перевизначити  методи __init__, __str__, __repr__
# Визнасити метод add_student, print_students, is_contain(Людина)


class Group:

    def __init__(self, group_name, students_list=None):
        self.group_name = group_name
        self.students_list = students_list

    def __str__(self):
        return f"group: {self.group_name} students: {self.students_list}"

    def __repr__(self):
        return f"{self.group_name}"

    def add_student(self, student):
        if self.students_list is None:
            self.students_list = []
        self.students_list.append(student)

    def print_students(self):
        print(f"There are {self.students_list} in a group {self.group_name}")

    def is_contain(self, student):
        return student in self.students_list
