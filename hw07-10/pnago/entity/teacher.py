"""
Створити сутність Викладач яка наслідує класс людина,
додати поля кафедра, посада.
Перевизначити  методи __init__, __str__, __repr__, __eq__
"""
from pnago.entity.human import Human


class Teacher(Human):
    def __init__(self, name, age, sex, chair, position):
        super().__init__(name, age, sex)
        self.chair = chair
        self.position = position

    def __str__(self):
        return f'Teacher name: {self.name}, Age: {self.name}, Sex: {self.sex} Chair: {self.chair}, Teacher Position: ' \
               f'{self.position}.'

    def __repr__(self):
        return f"{self.chair}, {self.position}"

    def __eq__(self, other):
        return self.name == other.name
