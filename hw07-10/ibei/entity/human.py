'''створити пекедж Сутність, в ньому створити модулі з відповідними класами:

Людина з полями імя, вік, стать. Перевизначити методи init, str, repr, eq

Група з полями назва, студенти(list). Перевизначити методи init, str, repr

Визначити метод add_student, print_students, is_contain(Людина)

створити модуль run.py в ньому створити екземпляри Людей, та екземпляр однієї групи додати людей до групи'''


class Human:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Sex: {self.sex}"

    def __repr__(self):
        return f"Name: {self.name}"

    def __eq__(self, other):
        self.other = other
        return {self.age} == {self.other}

