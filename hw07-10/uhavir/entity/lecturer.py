# Створити сутність Викладач яка наслідує класс людина,
# додати поля кафедра, посада.
# Перевизначити  методи __init__, __str__, __repr__, __eq__
from entity.human import Human


class Lecturer(Human):
    def __init__(self, name, age, sex, department, position):
        super(Human, self).__init__(name=name, age=age, sex=sex)
        self.department = department
        self.position = position

    def __str__(self):
        return f"department: {self.department} position: {self.position}"

    def __repr__(self):
        return f"{self.department}, {self.position}"

    def __eq__(self, other):
        return self.department == other.department and self.position == other.position
