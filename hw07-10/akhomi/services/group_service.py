from entity.group import StudentGroup
from services.human_service import create_human

def create_group():
    name = input("Group name: ")
    group = StudentGroup(name)
    return group

def add_student_to_group(group:StudentGroup):
    student = create_human()
    group.add_student(student)

