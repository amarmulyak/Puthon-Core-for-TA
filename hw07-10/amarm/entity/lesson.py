class Lesson:
    def __init__(self, group, teacher, room, subj):
        self.group = group
        self.teacher = teacher
        self.room = room
        self.subj = subj

    def __repr__(self):
        return f"Subject:{self.subj} Group:{self.group.group_name} " \
               f"Teacher:{self.teacher.name} Room:{self.room}"
