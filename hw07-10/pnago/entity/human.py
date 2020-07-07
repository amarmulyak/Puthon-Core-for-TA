"""
Людина з полями імя, вік, стать.
Перевизначити  методи __init__, __str__, __repr__, __eq__
"""


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Sex: {self.sex}."

    def __repr__(self):
        return f"{self.name}, {self.age}"

    def __eq__(self, other):
        return self.sex == other.sex or self.name == other.name

