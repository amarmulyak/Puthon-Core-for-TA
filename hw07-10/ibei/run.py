'''створити пекодж Сутність, в ньому створити модулі з відповідними класами:

Людина з полями імя, вік, стать. Перевизначити методи init, str, repr, eq

Група з полями назва, студенти(list). Перевизначити методи init, str, repr Визнасити метод add_student, print_students, is_contain(Людина)

створити модуль run.py в ньому створити екземпляри Людей, та екземпляр однієї групи додати людей до групи'''


from entity.human import Human
from entity.group import Group

human1 = Human('Zhanna', 15, 'male')
human2 = Human('Oleg', 12, 'male')
human3 = Human('Illia', 22, 'male')

group_name = "Group1"
students = ['Anna', 'Petro', 'Ian', 'Martin', 'Mykola']
group = Group(group_name, students)
students.extend([human1.name, human2.name, human3.name])
print(group)

