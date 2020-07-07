"""створити класс Заняття: назва група викладач аудиторія"""


class Lesson:
    def __init__(self, group, subject_name, lecturer, classroom):
        self.group = group
        self.subject_name = subject_name
        self.lecturer = lecturer
        self.classroom = classroom

    def __repr__(self):
        return f"Group: {self.group.group}\n" \
               f"Subject: {self.subject_name} \n" \
               f"Lecturer: {self.lecturer}\n" \
               f"Classroom: {self.classroom}"
