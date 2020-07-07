from entity.human import Human, HumanException

def create_human():
    created = True
    while created:
        try:
            name = input("Please enter name: ")
            age = int(input("Please enter age: "))
            sex = input("Please enter sex: ")

            human = Human(name, age, sex)
            created = False
        except HumanException as err:
            print(err)
        except ValueError as err:
            print("Age should be integer")
    return human



