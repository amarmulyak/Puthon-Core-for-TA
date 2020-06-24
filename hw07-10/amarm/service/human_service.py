from entity.human import Human, Teacher


def create_human():
    human_creation = True
    while human_creation:
        try:
            name = input("Enter Student's name: ")
            age = int(input("Enter age: "))
            sex = input("sex: ")
            human = Human(name, age, sex)
            human_creation = False
            print(f"Student {human.name} is added to the group")
            # break
        except ValueError:
            print("Age should be number")
        except Exception as err:
            print(err)
    return human


def create_teacher():
    teacher_crearion = True
    while teacher_crearion:
        try:
            name = input("Enter Teacher's name: ")
            age = int(input("Enter age: "))
            sex = input("Enter sex: ")
            cathedra = input("Enter cathedra: ")
            position = input("Enter position: ")
            teacher = Teacher(name, age, sex, cathedra, position)
            teacher_crearion = False
            print(f"Teacher {teacher.name} is created successfully")
        except ValueError:
            print("Age should be number")
        except Exception as err:
            print(err)
    return teacher
