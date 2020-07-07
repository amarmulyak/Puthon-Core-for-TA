"""
створити класс Заняття:
назва
група
викладач
аудиторія
"""


class Subject:
    def __init__(self, subject_title, group_name, teacher, room):
        self.subject_title = subject_title
        self.group_name = group_name
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f'Subject title: {self.subject_title}, Group Name: {self.group_name}, Teacher: {self.teacher}, Room: {self.room}'

    def __repr__(self):
        return f"{self.subject_title}, {self.group_namename}, {self.teacher}, {self.room}"

    def __eq__(self, other):
        return self.subject_title == other.subject_title and self.teacher == other.teacher and self.group_name == other.group_name
