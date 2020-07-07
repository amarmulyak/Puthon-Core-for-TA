# Створити клас Розклад.
# Визначити методи метод для додавання заняття у розклад, приймає три паметри заняття,
# день тижня(пн..пт), номер пари(1..6)
# у випадку невірних даних генерує відповідну ерору

# Визначити метод для друку розкладу викладача, приймає параметер типу викладач.
# У випадку якщо параметер не являється обєктом викладача генерується помилка

# Визначити метод для друку розкладу групи, приймає параметер типу група.
# У випадку якщо параметер не являється обєктом групи генерується помилка
from entity.lessons import Lesson

DAYS = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5
}


class Schedule:

    def __init__(self):
        self.schedule = []
        for day in range(5):
            lessons = []
            for lesson in range(5):
                lessons.append(None)
            self.schedule.append(lessons)

    def __repr__(self):
        for row in self.schedule:
            print(row)

    def add_lesson_to_schedule(self, lecture_name, day, lecture_num):
        """
        :param lecture_name:
        :param day: week workdays - DAYS
        :param lecture_num: from 1 to 6
        :return:
        """
        try:
            assert isinstance(day, str) and isinstance(lecture_num, int)
            self.schedule[lecture_num - 1][DAYS.get(day) - 1] = lecture_name.name
        except BaseException and TypeError and AssertionError as e:
            print(f"There is a wrong format of {e}")

    def get_lecturer_schedule(self, lecture):
        lecture_schedule = {}
        try:
            for i in range(5):
                if lecture.name in self.schedule[i]:
                    print(lecture.name)
                    lecture_schedule[lecture.classroom] = lecture.name
            print(f"The schedule for {lecture.lecturer.name} = {lecture_schedule}")
        except BaseException as e:
            print(f"The object {e} not in lecture")

    def get_group_schedule(self, lecture):
        group_schedule = {}
        try:
            for i in range(5):
                if lecture.name in self.schedule[i]:
                    group_schedule[lecture.classroom] = lecture.name
            print(f"The schedule for {lecture.group.group_name} = {group_schedule}")
        except BaseException as e:
            print(f"The object {e} not in lecture")
