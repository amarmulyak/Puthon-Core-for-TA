# створити модуль run.py в ньому створити екземпляри Людей, та екземпляр однієї групи додати людей до групи
from services.human_service import create_human
from services.group_service import create_group, add_student_to_group
from services.teacher_service import create_teacher
from services.lesson_service import create_lesson
from entity.teacher import Lesson, Schedule
from services.schedule_service import add_lesson_to_scedule

command_str = """
1. Create Human
2. Create Group
3. Add Human to Group
4. Print Groups
5. Create Teacher
6. Create Lesson
7. Add lesson
8. Show schedule
0 exit
"""
groups = []
teachers = []
schedule = Schedule()

if __name__ == "__main__":
    while True:
        print(command_str)
        try:
            command = int(input("Enter command: "))
        except:
            print("Incorrect command")
            continue
        if command == 0:
            break
        if command == 1:
            create_human()
        elif command == 2:
            group = create_group()
            groups.append(group)
        elif command == 3:
            print(groups)
            try:
                group_index = int(input("Enter Group index: "))
            except:
                print("Should be int")
            group = groups[group_index]
            add_student_to_group(group)
        elif command == 4:
            print(groups)
        elif command == 5:
            teacher = create_teacher()
            teachers.append(teacher)
        elif command == 6:
            lesson = create_lesson()
            print(lesson)
        elif command == 7:
            add_lesson_to_scedule(schedule)
        elif command == 8:
            schedule.schedule_presentation()








# from entity.human import Human
# from entity.group import StudentGroup
# from  entity.teacher import Teacher, Lesson
#
#
# human1 = Human('Oleh', 25, 'male')
# human2 = Human('Andrii', 'lol', 'male')
# human3 = Human('Natalia', 30, 'female')
# human4 = Human('Denys', 21, 'male')
#
# # try:
# #     print(human2)
# # except (ValueError, NameError):
# #     print("Incorrect data")
#
# # group_name = "Group12"
# students1 = [human1, human2]
# students2 = [human3, human4]
# group1 = StudentGroup('Group-12', students1)
# group2 = StudentGroup('Group-14', students2)
#
# students.extend([human1.name, human2.name, human3.name, human4.name])
# print(group)
#
# teacher1 = Teacher("Jack", 28, 'male', 'Biology', 'PhD')
# teacher2 = Teacher("Nick", 40, "male", "Math", "PhD")
# # print(teacher.__eq__())
# #
# math = Lesson('Biology', group1, teacher1, 321)
# philosophy = ('Philisophy', group2, teacher2, 333)
# # print(lesson)


# try:
#      Human.name= str(Human.name)
# except ValueError as e:
#     print(e)

# def HumanErr(name, age, sex):
#     try:
#         name = str(name)
#         age = int(age)
#         sex = sex
#     except ValueError:
#         print('Incorrect age')
#     if sex != 'male' and sex != 'female':
#         print ('Incorrect sex')
#
# h = HumanErr(name='Jack', age='25', sex='kgjg')
# print(h)
