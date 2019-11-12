"""
 Создать базу данных студентов (ФИО, группа, оценки, куратор студента, факультет).
 Написать CRUD ко всем полям.
 Описать методы для вывода отличников по каждому факультету.
 Вывести всех студентов определенного куратора.
"""

from mongoengine import *

connect('students_db')


class Student_grades(Document):
    subject = StringField(unique=True)
    grade = IntField(default=None)


class Students(Document):
    first_name = StringField(max_length=255, required=True)
    last_name = StringField(max_length=255, required=True)
    group = StringField(max_length=255, required=True)
    student_curator = StringField(max_length=255)
    faculty = StringField(max_length=255)
    student_id = IntField(required=True)
    grades = ListField(ReferenceField(StringField))
