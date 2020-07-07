"""Група з полями назва, студенти(list). Перевизначити методи init, str, repr Визнасити метод add_student, print_students,
 is_contain(Людина)"""


class Group:
    def __init__(self, group, students_list):
        self.group = group
        # exception
        if not isinstance(students_list, list):
            raise Exception("'Students' is not a students list")
        self.students_list = students_list

    def __str__(self):
        return f"Group: {self.group}\n" \
               f"Students: {self.students_list}"

    def __repr__(self):
        return f"{self.group}, {self.students_list}"

    def add_student(self, student_name):
        self.students_list.append(student_name)

    def print_student(self):
        print(f"There are {self.students_list} in a group {self.group}")

    def is_contain(self, student_name):
        return student_name in self.students_list
