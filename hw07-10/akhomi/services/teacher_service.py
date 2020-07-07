from entity.teacher import Teacher
from entity.exception import TeacherException

def create_teacher():
    created = True
    while created:
        try:
            name = input("Please enter Teacher name: ")
            age = int(input("Please enter age: "))
            sex = input("Please enter sex: ")
            department = input("Please enter department: ")
            position = input("Please enter position: ")

            teacher = Teacher(name, age, sex, department, position)
            created = False
        except TeacherException as err:
            print(err)
        except ValueError as err:
            print("Age should be integer")
    return teacher