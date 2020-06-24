from service.human_service import create_human
from service.group_service import create_group, add_student_to_group

command_str = """
1) create Human
2) create Group
3) add human to group
4) print groups
0 exit
"""
groups = []

if __name__ == "__main__":
    while True:
        print(command_str)
        try:

            command = int(input("enter comand: "))
        except:
            print("wrong command")
            continue
        if command == 0:
            break
        if command == 1:
            create_human()
        elif command == 2:
            group = create_group()
            print(groups)
            print(group)

            groups.append(group)
            print(groups)
        elif command == 3:
            print(groups)
            try:
                group_index = int(input("enter group index: "))
            except:
                print("bida")
            group = groups[group_index]
            add_student_to_group(group)
        elif command == 4:
            print(groups)
