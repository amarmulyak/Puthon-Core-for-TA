"""
Створити клас Розклад.
Визначити методи:
    метод для додавання заняття у розклад, приймає три паметри заняття, день тижня(пн..пт), номер пари(1..6)
                                        у випадку невірних даних генерує відповідну ерору
    Визначити метод для друку розкладу викладача, приймає параметер типу викладач. У випадку якщо параметер не являється
                                        обєктом викладача генерується помилка
    Визначити метод для друку розкладу групи, приймає параметер типу група.
                                        У випадку якщо параметер не являється обєктом групи генерується помилка.
"""


class Schedule:
    def __init__(self):
        self.schedule = []

    def __str__(self):
        return f"Schedule: {self.schedule}"

    def add_subject_to_schedule(self, day, sequence, subject, teacher, room):
        try:
            assert isinstance(day, str) and isinstance(sequence, int) and isinstance(subject, str) and \
                   isinstance(teacher, str) and isinstance(room, int)
        except AssertionError:
            print(f"You've entered a wrong format.")
        self.schedule.append([day, sequence, subject, teacher, room])

    def print_schedule_for_teacher(self, teacher):
        try:
            print(f"Schedule for {teacher.name}:")
            print('|{:^10s}|{:^6s}|{:^12s}|{:^7s}|'.format('DAY', '#', 'SUBJECT', 'ROOM'))
            print("_" * 40)

            for lesson in self.schedule:
                if teacher.name in lesson:
                    print('|{:^10s}|{:^6d}|{:^12s}|{:^7d}|'.format(lesson[0], lesson[1], lesson[2], lesson[4]))
        except AttributeError:
            print("You should provide a valid attribute")

    def print_schedule_for_group(self, group):
        try:
            print(f"Schedule for {group.group_title}")
            print('|{:^10s}|{:^7s}|{:^12s}|{:^18s}|{:^7s}|'.format('DAY', '#', 'SUBJECT', 'TEACHER', 'ROOM'))
            print("_" * 60)

            for lesson in self.schedule:
                print('|{:^10s}|{:^7d}|{:^12s}|{:^18s}|{:^7d}|'.format(lesson[0], lesson[1], lesson[2], lesson[3], \
                                                                       lesson[4]))
        except AttributeError:
            print("You should provide a valid attribute")
