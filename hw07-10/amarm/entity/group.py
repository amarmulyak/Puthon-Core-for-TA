from entity.human import Human


class Group:

    def __init__(self, group_name, students):
        self.group_name = group_name
        if not isinstance(students, list):
            raise Exception("'students' is not a list")
        self.students = students

    def __str__(self):
        return f"Group name: {self.group_name}, students: {self.students}"

    def __repr__(self):
        return {self.group_name: self.students}

    def __eq__(self, other):
        return self.group_name == other.group_name \
               and self.students == other.students

    def add_student(self, student):
        if not isinstance(student, Human):
            raise Exception("'student' is not instance of 'Human'")
        return self.students.append(student)

    def print_students(self):
        print(f"Print Students: {self.students}")

    def is_contain(self, student):
        return student in self.students
