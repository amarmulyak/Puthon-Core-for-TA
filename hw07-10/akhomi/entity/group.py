# створити пекодж Сутність, в ньому створити модулі з відповідними класами:
# Людина з полями імя, вік, стать. Перевизначити методи init, str, repr, eq
# Група з полями назва, студенти(list). Перевизначити методи init, str, repr
# Визнасити метод add_student, print_students, is_contain(Людина)
# створити модуль run.py в ньому створити екземпляри Людей, та екземпляр однієї групи додати людей до групи
from entity.human import Human

class StudentGroup:
    """
    Student group
    """

    def __init__(self, group_name, students = None):
        self.group_name = group_name
        # if not isinstance(students, list):
        #     raise Exception
        self.students = students

    def __str__(self):
        return f"Group name :{self.group_name}, Students of {self.group_name} group: {self.students}"

    def __repr__(self):
        return f"Group name : {self.group_name}"

    def add_student(self, student):
        if self.students is None:
            self.students = []
        self.students.append(student)
        return f"New student is added {self.students}"

    def print_students(self):
        if isinstance(students, Human):
            if not isinstance(students):
                raise Exception
        return (f"Students of {self.group_name}: {self.students}")

    def is_contain(self, student):
        return student in self.students


# group_name = "Group12"
# students = ['Iryna', 'Olesia', 'Mykola', 'Ostap', 'Ruslan']
# group = StudentGroup(group_name, students)
# print(group)
# print(group.__str__())
# print(group.__repr__())
# print(group.add_student('Lucka'))
# print(group.print_students())
# print(group.is_contain('Ostap'))
