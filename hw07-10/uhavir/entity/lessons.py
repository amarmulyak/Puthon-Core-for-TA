# створити класс Заняття:
# назва
# група
# викладач
# аудиторія


class Lesson:

    def __init__(self, name, group, lecturer, classroom):
        self.name = name
        self.group = group
        self.lecturer = lecturer
        self.classroom = classroom

    def __str__(self):
        return f"lesson_name: {self.name} group name: {self.group} lecturer: {self.lecturer} classroom: {self.classroom}"

    def __eq__(self, other):
        return self.name == other.name and self.group == other.group and self.lecturer == other.lecturer and self.classroom == other.clasroom
