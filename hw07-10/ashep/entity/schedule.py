"""Створити клас Розклад. Визначити методи
 метод для додавання заняття у розклад, приймає три паметри
 заняття,
 день тижня(пн..пт),
 номер пари(1..6) у випадку невірних даних генерує відповідну ерору"""
import copy
from entity.human import Lecturer
from entity.group import Group


class Schedule:
    weekdays = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5}
    lessons_order = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday'
    }

    def __init__(self):
        self.week_schedule = []
        for i in range(6):
            row = []
            for j in range(5):
                row.append(None)
            self.week_schedule.append(row)

    def __repr__(self):
        week_schedule = copy.deepcopy(self.week_schedule)
        for i in range(6):
            for j in range(5):
                if week_schedule[i][j] is not None:
                    week_schedule[i][j] = week_schedule[i][j].subject_name
        for row in week_schedule:
            print(row)

    def add_lesson(self, subject_name, weekday, lesson_order):
        # exception

        self.week_schedule[lesson_order - 1][self.weekdays[weekday] - 1] = subject_name
        return self

    def delete_lesson(self, weekday, lesson_order):
        self.week_schedule[lesson_order - 1][self.weekdays[weekday] - 1] = None

    def print_lecturer_schedule(self, lecturer):
        # exception
        if not isinstance(lecturer, Lecturer):
            raise Exception("'lecturer' is not instance of 'Lecturer'")
        lecturer_schedule = copy.deepcopy(self.week_schedule)
        for j in range(5):
            for i in range(6):
                if lecturer_schedule[i][j]:
                    if lecturer_schedule[i][j].lecturer == lecturer:
                        print(f'LECTURER SCHEDULE \n'
                              f'Weekday: {self.lessons_order[j + 1]} \n'
                              f'Lesson order: {i + 1} \n'
                              f'Subject: {lecturer_schedule[i][j].subject_name} \n'
                              f'Classroom: {lecturer_schedule[i][j].classroom}')

    def print_group_schedule(self, group):
        # exception
        if not isinstance(group, Group):
            raise Exception("group is not instance of Group")
        group_schedule = copy.deepcopy(self.week_schedule)
        for j in range(5):
            for i in range(6):
                if group_schedule[i][j] and group_schedule[i][j].group.group == group.group:
                    print(
                        f"Weekday: {self.lessons_order[j + 1]}, "
                        f"Lesson order: {i + 1},"
                        f"Subject: {group_schedule[i][j].subject_name},"
                        f"Classroom: {group_schedule[i][j].classroom}")
