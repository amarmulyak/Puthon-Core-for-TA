import copy
from entity.lesson import Lesson
from entity.human import Teacher
from entity.group import Group


class Schedule:

    week_days = {
            "mon": 1,
            "tue": 2,
            "wed": 3,
            "thu": 4,
            "fri": 5
        }

    week_days_r = {
        1: "mon",
        2: "tue",
        3: "wed",
        4: "thu",
        5: "fri"
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
                    week_schedule[i][j] = week_schedule[i][j].subj
        for row in week_schedule:
            print(row)

    def add_lesson_to_schedule(self, lesson, day, order):
        if day not in self.week_days.keys():
            print(f"Correct day should be in: {self.week_days.keys()}")
            raise Exception("Incorrect day")
        if not isinstance(lesson, Lesson):
            raise Exception("'lesson' is not instance of 'Lesson'")
        if order > 6 or order < 1:
            raise Exception("Correct order is from 1-6")
        self.week_schedule[order - 1][self.week_days[day] - 1] = lesson

    def delete_lesson_from_schedule(self, day, order):
        if day not in self.week_days.keys():
            print(f"Correct day should be in: {self.week_days.keys()}")
            raise Exception("Incorrect day")
        if order > 6 or order < 1:
            raise Exception("Correct value is from 1-6")
        self.week_schedule[order - 1][self.week_days[day] - 1] = None

    def print_schedule_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise Exception("'teacher' is not instance of 'Teacher'")
        teacher_schedule = copy.deepcopy(self.week_schedule)
        for j in range(5):
            for i in range(6):
                if teacher_schedule[i][j] \
                        and teacher_schedule[i][j].teacher == teacher:
                    print(f"day:{self.week_days_r[j+1]}, order:{i+1}, "
                          f"subject:{teacher_schedule[i][j].subj}, "
                          f"room:{teacher_schedule[i][j].room}")

    def print_schedule_group(self, group):
        if not isinstance(group, Group):
            raise Exception("'group' is not instance of 'Group'")
        group_schedule = copy.deepcopy(self.week_schedule)
        for j in range(5):
            for i in range(6):
                if group_schedule[i][j] and group_schedule[i][j].group == group:
                    print(f"day:{self.week_days_r[j+1]}, order:{i+1}, "
                          f"subject:{group_schedule[i][j].subj}, "
                          f"room:{group_schedule[i][j].room}")
