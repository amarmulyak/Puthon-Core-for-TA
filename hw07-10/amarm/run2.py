from service.group_service import (create_group,
                                   )
from service.human_service import (create_human,
                                   create_teacher)
from entity.lesson import Lesson
from entity.schedule import Schedule


main_menu = f"1: Create Group \n" \
            f"2: Add student to group \n" \
            f"3: Print students in group \n" \
            f"4: Create Teacher \n" \
            f"5: Print Teachers \n" \
            f"6: Create lesson \n" \
            f"7: Print lessons \n" \
            f"8: Add lesson to week schedule \n" \
            f"9: Print Group schedule \n" \
            f"10: Print Teacher's schedule \n" \
            f"11: Delete lesson from schedule \n" \
            f"0: Quit \n" \
            f"Make your choice: "

lesson = ""
new_teacher = ""
teachers_dict = {}
lessons_dict = {}


def list_of_teachers():
    print("List of existed teachers:")
    for t in teachers_dict.values():
        print(t)


def list_of_lessons():
    print("List of existed lessons:")
    message = ""
    for les in lessons_dict.values():
        print(les)


if __name__ == "__main__":
    week_schedule = Schedule()
    new_group = ""
    while True:
        choice = input(main_menu)
        if choice == "1":
            if new_group:
                print("Group is created already")
            else:
                new_group = create_group()

        elif choice == "2":
            if new_group:
                new_human = create_human()
                new_group.add_student(new_human)
            else:
                print("Create a group first")
                continue

        elif choice == "3":
            if new_group:
                new_group.print_students()
            else:
                print("Create a group first")
                continue

        elif choice == "4":
            while True:
                new_teacher = create_teacher()
                teachers_dict[new_teacher.name] = new_teacher
                break

        elif choice == "5":
            list_of_teachers()

        elif choice == "6":
            if new_teacher:
                while True:
                    teacher = teachers_dict.get(input("Provide Teacher's name: "))
                    if teacher is None:
                        print("Teacher does not exist")
                        list_of_teachers()
                        continue
                    room = input("Enter room: ")
                    if not room.isdigit():
                        print("Room should contain numbers only")
                        continue
                    subj = input("Enter subject: ")
                    if not subj.isalpha():
                        print("Subject should contain letters only")
                        continue
                    break
                lesson = Lesson(new_group, teacher, room, subj)
                lessons_dict[lesson.subj] = lesson
                print(f"Lesson {lesson.subj} is created successfully")
            else:
                print("Create teacher first")

        elif choice == "7":
            list_of_lessons()

        elif choice == "8":
            if lesson:
                while True:
                    try:
                        lesson = lessons_dict.get(input("Enter lesson's name: "))
                        if lesson is None:
                            print("Lesson doesn't exist")
                            list_of_lessons()
                            continue
                        day = input("Enter day of the week: ")
                        order = int(input("Enter lesson's order: "))
                        week_schedule.add_lesson_to_schedule(lesson, day, order)
                        break
                    except Exception as err:
                        print(err)
                print("Lesson added to schedule successfully")
            else:
                print("Create lesson first")

        elif choice == "9":
            if new_group:
                print("Schedule of the Group:")
                week_schedule.print_schedule_group(new_group)
            else:
                print("Group is not created")

        elif choice == "10":
            if new_teacher:
                teacher = teachers_dict.get(input("Enter teacher's name: "))
                if teacher is None:
                    print("Teacher does not exist")
                    list_of_teachers()
                else:
                    week_schedule.print_schedule_teacher(teacher)
            else:
                print("Teacher is not created")

        elif choice == "11":
            while True:
                try:
                    day = input("Enter day of the week: ")
                    order = int(input("Enter lesson's order: "))
                    week_schedule.delete_lesson_from_schedule(day, order)
                    print("Lesson is deleted successfully")
                    break
                except Exception as err:
                    print(err)

        elif choice == "0":
            break

        else:
            print("Wrong choice!")