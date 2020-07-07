'''створити пекодж Сутність, в ньому створити модулі з відповідними класами:

Людина з полями імя, вік, стать. Перевизначити методи init, str, repr, eq

Група з полями назва, студенти(list). Перевизначити методи init, str, repr Визнасити метод add_student, print_students, is_contain(Людина)

створити модуль run.py в ньому створити екземпляри Людей, та екземпляр однієї групи додати людей до групи'''


class Group:

    def __init__(self, group_name, students):
        self.group_name = group_name
        self.students = students

    def __str__(self):
        return f"Group name :{self.group_name}, Students: {self.group_name} group: {self.students}"

    def __repr__(self):
        return f"Group name : {self.group_name}"

    def add_student(self, student):
        self.students.append(student)
        return f"New student: {self.students}"

    def print_students(self):
        return (f"Students: {self.group_name}: {self.students}")

    def is_contain(self, student):
        return student in self.students

