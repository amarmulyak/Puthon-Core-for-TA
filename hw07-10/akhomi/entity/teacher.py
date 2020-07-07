# Створити сутність Викладач яка наслідує класс людина, додати поля кафедра, посада. Перевизначити методи init, str, repr, eq
# створити класс Заняття: назва група викладач аудиторія
# Створити клас Розклад. Визначити методи метод для додавання заняття у розклад, приймає три паметри заняття, день тижня(пн..пт),
# номер пари(1..6) у випадку невірних даних генерує відповідну ерору
# Визначити метод для друку розкладу викладача, приймає
# параметер типу викладач. У випадку якщо параметер не являється обєктом викладача генерується помилка Визначити метод для
# друку розкладу групи, приймає параметер типу група. У випадку якщо параметер не являється обєктом групи генерується помилка
# додати у класи Людина, Група, Викладач, Заняття обробітники винятків у необхідні методи
# визначити в модулі run.py можливість роботи з програмую через термінал

from entity.human import Human
from entity.group import StudentGroup
import copy

class Teacher(Human):
    def __init__(self, name, age, sex, department, position):
        Human.__init__(self, name, age, sex)
        self.department = department
        self.position = position
    def __str__(self):
        # Human.__str__(self)
        return f"Name: {self.name}, Department: {self.department}, Position:{self.position} "
    def __repr__(self):
        return f"Name: {self.name}, Position: {self.position}"
    def __eq__(self, other):
        return self.name == other.name and self.position == other.position and self.department == other.department

class Lesson:
    def __init__(self, subject, group, teacher, classroom):
        self.subject = subject
        self.group = group
        self.teacher = teacher
        self.classroom = classroom
    def __repr__(self):
        return f"Lesson: {self.subject}, Group: {self.group}, Teacher: {self.teacher}, Classroom: {self.classroom}"

class Schedule:
    def __init__(self):
        self.week_schedule = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append("-")
            self.week_schedule.append(row)


    def schedule_presentation(self):
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        k = ""
        for day in week:
            k += '{:^10}'.format(day)
        print(k)
        for row in self.week_schedule:
            s = ""
            for i in row:
                if isinstance(i, Lesson):
                    s += '{:^10}'.format(i.subject)
                else:
                    s += '{:^10}'.format(i)
            print(s)

    def add_lesson(self, subject, day, pair):
        # self.subject = subject
        # self.day = day
        # self.pair = pair
        dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4}
        try:
            self.week_schedule[pair - 1].pop(dict[day])
            self.week_schedule[pair - 1].insert(dict[day], subject)
        except (KeyError, IndexError):
            print("Please enter correct day or/and pair")



    def del_lesson(self, subject, day, pair):
        self.subject = subject
        self.day = day
        self.pair = pair
        dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4}
        try:
            self.week_schedule[pair - 1].pop(dict[day])
            self.week_schedule[pair - 1].append('x')
        except (KeyError, IndexError):
            print("Please enter correct day or/and pair")
        print(self.week_schedule)

    def group_sch(self, group):
        if isinstance(group, StudentGroup):
            group_sch = copy.deepcopy(self.week_schedule)
            gr_sc = []
            for lesson in group_sch:
                for i in lesson:
                    if isinstance(i, Lesson):
                        if i.group == group.group_name:
                            gr_sc.append(i)
            print(f"Group {group.group_name}:  schedule", gr_sc)
        else:
            raise Exception

    def teacher_sch(self, teacher):
        if isinstance(teacher, Teacher):
            teach_sch = copy.deepcopy(self.week_schedule)
            tech_sc = []
            for lesson in teach_sch:
                for i in lesson:
                    if isinstance(i, Lesson):
                        if i.teacher == teacher.name:
                            tech_sc.append(i)
            print(f"Teacher {teacher.name} has schedule", tech_sc)
        else:
            raise Exception


# schedule = Schedule()
# teacher1 = Teacher('Jack', 25, 'male', 'Biology', 'PhD')
# teacher2 = Teacher('John', 40, 'male', 'Philosophy', 'PhD')
# group_name = "Group-12"
# students = ['Iryna', 'Olesia', 'Mykola', 'Ostap', 'Ruslan']
# group = StudentGroup(group_name, students)
# Biology = Lesson('Biology', group.group_name, teacher1.name, 321)
# Philosophy = Lesson('Philosophy', group.group_name, teacher2.name, 333)
#
# # schedule.schedule_presentation()
# schedule.add_lesson(Biology, 'Monday', 1)
# schedule.add_lesson(Philosophy, 'Wednesday', 4)
# # schedule.schedule_presentation()
# # schedule.add_lesson('Math', 'Friday', 5)
# # schedule.del_lesson('Biology', 'Monday', 1)
# # schedule.teacher_sch('Khomiak')
# schedule.teacher_sch(teacher1)
# schedule.schedule_presentation()
# schedule.group_sch(group)

# print(teacher.__eq__())

# print(lesson)

#     def add_lesson(self, lesson, day, order):
#         self.lesson = lesson
#         self.day = day
#         self.order = order
#         self.week_schedule[self.order - 1][self.day - 1] = self.lesson
#         return self.week_schedule
