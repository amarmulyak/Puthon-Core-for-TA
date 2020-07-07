"""
створити модуль run.py в ньому створити екземпляри Людей, та екземпляр однієї групи
додати людей до групи
"""
import sys
sys.path.append('/Users/pnahorny/Documents/Python/PythonCore/hw07-10/')

from pnago.entity.human import Human
from pnago.entity.group import Group
from pnago.entity.teacher import Teacher
from pnago.entity.subject import Subject
from pnago.entity.schedule import Schedule

human_01 = Human("Marshal", 30, "male")
human_02 = Human("Lily", 29, "female")
human_03 = Human("Vasia", 15, "male")

group_01 = Group("My_group", [human_01.name, human_02.name])
group_02 = Group("Second_group", human_03)

teacher_01 = Teacher("Liubomyr", 28, "male", "CS", "lecturer")
teacher_02 = Teacher("Alexa", 34, "female", "CS", "lecturer")

subject_01 = Subject("Python", group_01.group_title, teacher_01.name, 102)
subject_02 = Subject("C#", group_01.group_title, teacher_02.name, 103)

schedule = Schedule()

schedule.add_subject_to_schedule("Mon", 1, subject_01.subject_title, subject_01.teacher, subject_01.room)
schedule.add_subject_to_schedule("Tue", 2, subject_01.subject_title, subject_02.teacher, 104)
schedule.add_subject_to_schedule("Tue", 3, subject_01.subject_title, subject_01.teacher, 105)

# schedule.print_schedule_for_teacher(teacher_01)
print()
schedule.print_schedule_for_group(group_01)
print()
schedule.print_schedule_for_group(group_02)
