# створити модуль run.py в ньому створити екземпляри Людей, та екземпляр однієї групи
# додати людей до групи

from entity.human import Human
from entity.group import Group
from entity.schedule import Schedule
from entity.lessons import Lesson

human_1 = Human("Tina", 25, "female")
human_2 = Human('Tomas', 27, 'male')
human_3 = Human("Ema", 15, "female")
human_4 = Human('Roy', 17, 'male')

group_1 = Group("Group 1", [human_1, human_2])
group_1.add_student(human_3)
group_1.add_student(human_4)

# create lessons
math = Lesson(name="Math", group=group_1, lecturer=human_1, classroom=5)
language = Lesson(name="Language", group=group_1, lecturer=human_2, classroom=3)

# add lessons to schedule
schedule = Schedule()
schedule.add_lesson_to_schedule(lecture_name=math, day="Mon", lecture_num=4)
schedule.add_lesson_to_schedule(lecture_name=math, day="Thu", lecture_num=1)
schedule.add_lesson_to_schedule(lecture_name=language, day="Fri", lecture_num=1)

# get lectures and group schedules
schedule.get_lecturer_schedule(lecture=math)
schedule.get_group_schedule(lecture=math)
