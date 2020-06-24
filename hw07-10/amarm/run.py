from entity.human import Human
from entity.human import Teacher
from entity.group import Group
from entity.lesson import Lesson
from entity.schedule import Schedule

# Create Human objects
bob = Human("Bob", 32, "male")
jess = Human("Jess", 28, "female")
john = Human("John", 30, "male")
dan = Human("Dan", 22, "male")
lisa = Human("Lisa", 25, "female")

# Create  Group
group1 = Group("Group #1", [bob, jess])

# Add student to the Group
group1.add_student(john)

# Print all members of the Group
print(group1)

# Verify if student exist in the group
print(group1.is_contain(jess))

print("="*20)

# Create Teacher object
teacher1 = Teacher("Brown", 54, "male", "Cathedra #1", "dean")
teacher2 = Teacher("Black", 5, "male", "Cathedra #2", "teacher")

# Create Lesson
math = Lesson(group1, teacher1, room="215", subj="Mathematics")
history = Lesson(group1, teacher1, room="210", subj="History")
chemistry = Lesson(group1, teacher2, room="222", subj="Chemistry")

# Print Lesson
print(math)

# Create default week Schedule with no subjects
week1 = Schedule()

# Add lesson to schedule (e.g. math - subject, "mon" - Monday
# 3 - lesson's order
week1.add_lesson_to_schedule(math, "mon", 5)
week1.add_lesson_to_schedule(history, "mon", 4)
week1.add_lesson_to_schedule(math, "tue", 2)
week1.add_lesson_to_schedule(history, "fri", 5)
week1.add_lesson_to_schedule(chemistry, "tue", 1)

# Print week schedule
# print(week1.__repr__())

# Delete lesson
# week1.delete_lesson_from_schedule("mon", 3)
# print(week1.__repr__())

print("=" * 50)

print(week1.__repr__())

week1.print_schedule_teacher(teacher1)
print("-"*50)
week1.print_schedule_group(group1)



# Math = Subjects("Mathematic")

# math_repr = Lesson()
# print(math_repr)

