# Група з полями назва, студенти(list).
# Перевизначити  методи __init__, __str__, __repr__
# Визнасити метод add_student, print_students, is_contain(Людина)
# додати у класи Людина, Група, Викладач, Заняття  обробітники винятків у необхідні методи
# визначити в модулі run.py можливість роботи з програмую через термінал


class Group:

    def __init__(self, group_name, students_list):
        self.group_name = group_name
        self.students_list = students_list

    def __str__(self):
        return f"group: {self.group_name} students: {self.students_list}"

    def __repr__(self):
        return f"{self.group_name}, {self.students_list}"

    def add_student(self, student_name):
        try:
            self.students_list.append(student_name)
        except BaseException as e:
            print(f"There is a wrong student name - {e}")

    def print_students(self):
        print(f"There are {self.students_list} in a group {self.group_name}")

    def is_contain(self, student):
        return student in self.students_list
