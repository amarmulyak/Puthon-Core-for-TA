from entity.teacher import Lesson, Schedule, StudentGroup, Teacher
from services.teacher_service import create_teacher

def create_lesson():
    subject = input("Subject: ")
    group = input("Group: ")
    teacher = input("Teacher: ")
    classroom = int(input("Classroom: "))
    lesson = Lesson(subject, group, teacher, classroom)
    return lesson
