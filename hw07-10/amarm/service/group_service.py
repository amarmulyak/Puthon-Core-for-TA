from entity.group import Group


def create_group():
    name = input("Enter Group Name: ")
    group = Group(name, [])
    print(f"Group {group.group_name} is created successfully")
    return group

