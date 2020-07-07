# створити пекодж Сутність, в ньому створити модулі з відповідними класами:
# Людина з полями імя, вік, стать. Перевизначити методи init, str, repr, eq
# Група з полями назва, студенти(list). Перевизначити методи init, str, repr Визнасити метод add_student, print_students, is_contain(Людина)
# створити модуль run.py в ньому створити екземпляри Людей, та екземпляр однієї групи додати людей до групи
from entity.exception import HumanException
class Human:
    """
    Human characteristics
    """
    def __init__(self, name, age, sex):
        if not isinstance(name, str):
            raise HumanException("Name is not string")
        if not name.isalpha():
            raise HumanException("Name contain numbers or characters")
        self.name = name
        # if not isinstance(age, int):
        #     raise HumanException("Age contain symbols")
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Sex: {self.sex}"
    def __repr__(self):
        return f"Name: {self.name}"
    def __eq__(self, other):
        self.other = other
        return {self.age} == {self.other}
    # def HumanErr(self, name, age, sex):
    #     try:
    #         self.name = str(name)
    #         self.age = int(age)
    #         self.sex = sex
    #     except ValueError:
    #         print('Incorrect age')
    #     if self.sex != 'male' or 'female':
    #         print('Incorrect sex')


# human = Human('Jack', 25, 'male')
# print(human)
# print(human.__str__())
# print(human.__repr__())
# print(human.__eq__(25))
# print("Name: ", human.name)
# print("Age: ", human.age)
# print("Sex: ", human.sex)




