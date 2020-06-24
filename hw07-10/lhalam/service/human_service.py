from entity.human import Human, HumanException


def create_human():
    created = True
    while created:
        try:
            name = input("enter name")
            age = int(input("enter age"))
            sex = input("enter sex")

            human = Human(name, age, sex)
            created = False
        except HumanException as err:
            print(err)
        except ValueError as err:
            print("Age must by Int")
    return human


