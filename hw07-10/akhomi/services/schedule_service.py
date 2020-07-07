from entity.teacher import Schedule
# from entity.exception import TeacherException


def add_lesson_to_scedule(schedule):
    created = True
    while created:
        try:
            subject = input("Please enter subject: ")
            day = input("Please enter day: ")
            pair = int(input("Please enter pair: "))

            schedule.add_lesson(subject, day, pair)
            created = False
        # except TeacherException as err:
        #     print(err)
        except ValueError as err:
            print("Pair should be integer")