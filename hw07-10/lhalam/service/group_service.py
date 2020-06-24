from entity.group import Group
from service.human_service import create_human

def create_group():
    name = input("group name: ")
    group = Group(name)
    return group

def add_student_to_group(group:Group):
    student = create_human()
    group.add_student(student)