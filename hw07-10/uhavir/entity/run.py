# створити модуль run.py в ньому створити екземпляри Людей, та екземпляр однієї групи
# додати людей до групи

from entity.human import Human
from entity.group import Group

human_1 = Human("Name1", 25, "female")
human_2 = Human('Name2', 27, 'male')

group = Group("Group 1", ["Student A", "Student B"])
group.add_student(human_1)
group.add_student(human_2)

