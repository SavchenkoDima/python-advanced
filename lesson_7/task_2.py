#!/usr/bin/python
# -*- coding: UTF-8

"""
2) Создать базу данных студентов. У студента есть факультет, группа, оценки, номер студенческого билета.
Написать программу, с двумя ролями: Администратор, Пользователь.
Администратор может добавлять, изменять существующих студентов.
Пользователь может получать список отличников, список всех студентов, искать студентов по номеру студенческого,
получать полную информацию о конкретном студенте (включая оценки, факультет)
"""

import sqlite3


class ContextManagerDB:
    def __init__(self, db_name):
        self._db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self._db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


class Students:

    def __init__(self, name, department, group, grades, id_student_number):
        self._id_student_number = id_student_number
        self._grades = grades
        self._group = group
        self._department = department
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value
    name = property(get_name, set_name)

    def get_department(self):
        return self._department

    def set_department(self, value):
        self._department = value
    department = property(get_department, set_department)

    def get_grades(self):
        return self._grades

    def set_grades(self, value):
        self._grades = value
    grades = property(get_grades, set_grades)

    def get_group(self):
        return self._group

    def set_group(self, value):
        self._group = value
    group = property(get_group, set_group)

    def get_id_student_number(self):
        return self._id_student_number

    def set_id_student_number(self, value):
        self._id_student_number = value
    id_student_number = property(get_id_student_number, set_id_student_number)


class User(Students):

    def __init__(self, name, id_role):
        self._name = name
        self._id_role = id_role

    def get_id_role(self):
        return self._id_role

    def set_id_role(self, value):
        self._id_role = value
    id_role = property(get_id_role, set_id_role)


print('привет вы попали в базу студентов университета имени ПУПКИНА')
print('')
date_base = 'task_2_DB.db'



while True:
    print('')
    print('вы попали в Базу Данных института')
    print('')

    print('Введите свой логин и пароль')
    in_login = input('name =')
    in_pass = input('pass = ')

    with ContextManagerDB(date_base) as connection:
        sql = " SELECT password, users.name, id_role, name_role " \
              " FROM users " \
              " INNER JOIN role " \
              " ON role.id = users.id_role " \
              " WHERE users.name = '%s' " % in_login
        results = connection.execute(sql)
        results = results.fetchone()
        print(results)
    if results:
        if results[0] == in_pass:
            print(f'добро пожаловать {in_login}')
            if results[3] == 'admin':
                print('Вы хотите изменить пользователя или добавить? ')
                answer = input('хотите разместить новую статью "AD" или "CH":').upper()
                while answer not in ('AD', 'CH'):
                     print('Вы ввели неверное значение!')
                     answer = input('Введите свой ответ в формате "AD" или "CH":').upper()

                if answer == 'AD':
                    new_user_name = input('Укажите имя ')
                    new_user_department = input('факультет')
                    new_user_group = input('группа')
                    new_user_ID_student_number = input('номер студентческого')

                    conn = sqlite3.connect(date_base)
                    cursor = conn.cursor()
                    sql = """INSERT INTO students (name, department, group, ID_student_number) VALUES(?, ?, ?, ?)"""
                    cursor.execute(sql, [new_user_name,
                                         new_user_department,
                                         new_user_group,
                                         new_user_ID_student_number])
                    conn.commit()
                    conn.close()
                else:
                    ch_user_name = input('Введите имя студента которого хотите изменить')
                    conn = sqlite3.connect(date_base)
                    cursor = conn.cursor()
                    sql = """ SELECT * 
                          FROM  students 
                          WHERE students.name = '%s' """ % ch_user_name
                    results = cursor.execute(sql).fetchone()
                    print(results, '/', results[1])
                    if results:
                        new_name = input(f'Укажите новое имя для {results[1]} на ')
                        new_department = input(f'заменить факультет {results[2]} на')
                        new_group = input(f'заменить группу {results[3]} на ')
                        new_ID = input(f'заменить номер {results[4]} на ')

                        connect = sqlite3.connect(date_base)
                        cursor = connect.cursor()
                        sql = f""" UPDATE students 
                        SET name = '{str(new_name)}', s_group = '{str(new_group)}',
                        ID_student_number = {new_ID},
                        department = '{str(new_department)}' 
                        WHERE name = '{results[1]}'"""
                        cursor.execute(sql)
                        connect.commit()
                        connect.close()

                    conn.commit()
                    conn.close()







                    #new_user_add = input('может ли пользователь добавлять пользователей установите "1" - да,"0" - нет')
                    #new_user_cheng = input('может ли пользователь изменять пользователей установите "1" - да,"0" - нет')
                    #new_user_view = input('может ли пользователь просматривать пользователей '
                     #                     'установите "1" - да,"0" - нет')



        else:
            print(f'не верный пароль')
            continue
    else:
        print('Нет такого пользователя')







    #
    # user_log = User(in_login, in_pass, admin=int(in_admin))
    # if user_log.login_user() == False:
    #     continue
    #
    # print('')
    # print('Admin', user_log.is_admin())
    # print('')
    # print('Admin = ', user_log.get_admin())
    # print('')
    # if user_log.is_admin() == True:
    #     print('Все пользователи')
    #     user_log.print_list_user()
    #
    # answer = input('хотите разместить новую статью "Y" или "N":').upper()
    # while answer not in ('Y', 'N'):
    #     print('Вы ввели неверное значение!')
    #     answer = input('Введите свой ответ в формате "Y" или "N":').upper()
    #
    # if answer == 'Y':
    #     text = input('введите ваш текст')
    #     user_log.set_post(text)
    #     user_log.save_user()
    #
    # else:
    #     answer = input('хотите выйти "Y" или "N":').upper()
    #     while answer not in ('Y', 'N'):
    #         print('Вы ввели неверное значение!')
    #         answer = input('Введите свой ответ в формате "Y" или "N":').upper()
    #
    #     if answer == 'Y':
    #         user_log.logout_user()
    #         print('Пока')
    #
    #
    #
    #
