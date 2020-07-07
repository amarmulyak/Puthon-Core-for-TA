"""створити модуль run.py в ньому створити екземпляри Людей, та екземпляр однієї групи додати людей до групи"""

from entity.human import Human
from entity.human import Lecturer
from entity.group import Group
from entity.lesson import Lesson
from entity.schedule import Schedule

human_1 = Human('Luci', 22, 'female')
human_2 = Human('Alex', 20, 'male')
human_3 = Human('Leo', 18, 'male')

group = Group('Main Group ', [human_1, human_2])
group.add_student(human_3)

print(group)
print('\t')

print(group.is_contain(human_1))
print('\t')

lecturer_1 = Lecturer('Dr. Williams', 40, 'male', 'Mathematics', 'PhD')
lecturer_2 = Lecturer('McGonagle', 50, 'female', 'Literature', 'Professor')
lecturer_3 = Lecturer('Starling', 55, 'female', 'Biology', 'PhD')

mathematics = Lesson(group, subject_name='Mathematics', lecturer=lecturer_1, classroom='100')
literature = Lesson(group, subject_name='Literature', lecturer=lecturer_2, classroom='101')
biology = Lesson(group, subject_name='Biology', lecturer=lecturer_3, classroom='102')

print(literature)
print('\t')

week = Schedule()

week.add_lesson(mathematics, "Monday", 5)
week.add_lesson(biology, "Friday", 4)
week.add_lesson(biology, "Friday", 1)
# week.add_lesson(biology, "Tuesday", 1)
# week.add_lesson(mathematics, "Monday", 3)
# week.add_lesson(literature, "Friday", 3)
# week.add_lesson(biology, "Tuesday", 2)
# week.add_lesson(biology, "Monday", 1)

print(week.__repr__())

print('\t')

week.print_lecturer_schedule(lecturer_1)

print('\t')

week.print_group_schedule(group)
