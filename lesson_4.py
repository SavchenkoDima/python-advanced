"""
1)
Создайте класс ПЕРСОНА с абстрактными методами, позволяющими вывести на экран информацию о персоне,
а также определить ее возраст (в текущем году).
Создайте дочерние классы:
АБИТУРИЕНТ (фамилия, дата рождения, факультет),
СТУДЕНТ (фамилия, дата рождения, факультет, курс),
ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
со своими методами вывода информации на экран и определения возраста.
Создайте список из n персон, выведите полную информацию из базы на экран, а также организуйте поиск персон,
чей возраст попадает в заданный диапазон.
"""
# from abc import ABC, abstractmethod
# import datetime
# import operator
#
#
# class Person(ABC):
#     """ description """
#
#     def __init__(self, surname, date_of_birth):
#         self._surname = surname
#         self._date_of_birth = date_of_birth
#
#     @property
#     def surname(self):
#         return self._surname
#
#     @surname.setter
#     def surname(self, value):
#         self._surname = value
#
#     @surname.deleter
#     def surname(self):
#         del self._surname
#
#     @property
#     def date_of_birth(self):
#         return self._date_of_birth
#
#     @date_of_birth.setter
#     def date_of_birth(self, value):
#         self._date_of_birth = value
#
#     @date_of_birth.deleter
#     def date_of_birth(self):
#         del self._date_of_birth
#
#     @abstractmethod
#     def how_many_years(self):
#         today = datetime.datetime.now().strftime('%Y')
#         return int(today) - int(self.date_of_birth)
#
#     @abstractmethod
#     def about(self):
#         return 'My surname is {} and, I am {} years'.format(self._surname, self.how_many_years())
#
#
# class Enrollee(Person):
#     """ description """
#
#     def __init__(self, surname, date_of_birth, faculty):
#         super().__init__(surname, date_of_birth)
#         self._faculty = faculty
#
#     def about(self):
#         return 'My surname is {} and, I am {} years. I am enrollee {}'. \
#             format(self._surname, self.how_many_years(), self._faculty)
#
#     def how_many_years(self):
#         return super().how_many_years()
#
#     def get_faculty(self):
#         return self._faculty
#
#     def set_faculty(self, value):
#         self._faculty = value
#
#     def del_faculty(self):
#         del self._faculty
#
#     faculty = property(get_faculty, set_faculty, del_faculty)
#
#
# class Student(Person):
#     """ description """
#     def __init__(self, surname, date_of_birth, faculty, course):
#         super().__init__(surname, date_of_birth)
#         self._faculty = faculty
#         self._course = course
#
#     def about(self):
#         return 'My surname is {} and, I am {} years. I am enrollee {}.I am studied on {} course '. \
#             format(self._surname, self.how_many_years(), self._faculty, self._course)
#
#     def how_many_years(self):
#         return super().how_many_years()
#
#     def get_course(self):
#         return self._course
#
#     def set_course(self, value):
#         self._course = value
#
#     def del_course(self):
#         del self._course
#
#     course = property(get_course, set_course, del_course)
#
#     def get_faculty(self):
#         return self._faculty
#
#     def set_faculty(self, value):
#         self._faculty = value
#
#     def del_faculty(self):
#         del self._faculty
#
#     faculty = property(get_faculty, set_faculty, del_faculty)
#
#
# class Teacher(Person):
#     """ description """
#
#     def __init__(self, surname, date_of_birth, faculty, position, experience):
#         super().__init__(surname, date_of_birth)
#         self._faculty = faculty
#         self._position = position
#         self._experience = experience
#
#     def about(self):
#         return 'My surname is {} and, I am {} years. I work in positions {}. my experience {} years'. \
#             format(self._surname, self.how_many_years(), self._position, self._experience)
#
#     def how_many_years(self):
#         return super().how_many_years()
#
#     def get_faculty(self):
#         return self._faculty
#
#     def set_faculty(self, value):
#         self._faculty = value
#
#     def del_faculty(self):
#         del self._faculty
#
#     faculty = property(get_faculty, set_faculty, del_faculty)
#
#     def get_position(self):
#         return self._position
#
#     def set_position(self, value):
#         self._position = value
#
#     def del_position(self):
#         del self._position
#
#     position = property(get_position, set_position, del_position)
#
#     def get_experience(self):
#         return self._experience
#
#     def set_experience(self, value):
#         self._experience = value
#
#     def del_experience(self):
#         del self._experience
#
#     experience = property(get_experience, set_experience, del_experience)
#
#
# enrollee1 = Enrollee('Abramson', 2010, 'C#')
# enrollee2 = Enrollee('Babcock', 2001, 'C')
# enrollee3 = Enrollee('Calhoun', 2002, 'C++')
# enrollee4 = Enrollee('Daniels', 2003, 'java')
# enrollee5 = Enrollee('Eddington', 2004, 'C#')
#
# student1 = Student('Faber', 2010, 'C++', 1)
# student2 = Student('Galbraith', 2005, 'C#', 2)
# student3 = Student('Haig', 2006, 'java', 3)
# student4 = Student('Keat', 2008, 'python', 4)
# student5 = Student('Laird', 1990, 'C', 5)
#
#
# teacher1 = Teacher('MacAdam', 1983, 'python', 'Teacher', 5)
# teacher2 = Teacher('Nash', 1983, 'C#', 'Teacher', 10)
# teacher3 = Teacher('Page', 1983, 'java', 'Head Teacher', 20)
# teacher4 = Teacher('Raleigh', 1983, 'C++', 'Head Teacher', 30)
# teacher5 = Teacher('Salisburry', 1983, 'C', 'Head Teacher', 35)
#
# list_person = [enrollee1, enrollee2, enrollee3, enrollee4, enrollee5,
#                student1, student2, student3, student4, student5,
#                teacher1, teacher2, teacher3, teacher4, teacher5]
# list_years = []
# for p in list_person:
#     list_years.append(p.how_many_years())
#
# print('вы попали в программку об студентах и преподователях института')
# print('Вы хотите получить полный список ?')
#
# all_list = input('Введите свой ответ в формате "Y" или "N":').upper()
#
# while all_list not in ('Y', 'N'):
#     print('Вы ввели неверное значение!')
#     all_list = input('Введите свой ответ в формате "Y" или "N":').upper()
#
# if all_list == 'Y':
#     print('Вы хотите получить отсортированный список ?')
#     all_list = input('Введите свой ответ в формате "Y" или "N":').upper()
#     while all_list not in ('Y', 'N'):
#         print('Вы ввели неверное значение!')
#         all_list = input('Введите свой ответ в формате "Y" или "N":').upper()
#
#     if all_list == 'Y':
#         sort_list_person = sorted(list_person, reverse=True, key=operator.attrgetter('date_of_birth'))
#         for person in sort_list_person:
#             print(person.about())
#     else:
#         for person in list_person:
#             print(person.about())
# else:
#     print('Тогда сортируем по вашему желанию')
#     first_year = input('Введите возраст в формате "{}" От:'.format(min(list_years)))
#     while not first_year.isdigit():
#         print('Вы ввели неверное значение!')
#         first_year = input('Введите возраст в формате "{}" От:'.format(min(list_years)))
#
#     last_year = input('Введите возраст в формате "{}" До:'.format(max(list_years)))
#     while not last_year.isdigit():
#         print('Вы ввели неверное значение!')
#         last_year = input('Введите возраст в формате "{}" До:'.format(max(list_years)))
#
#     sort_list_person = sorted(list_person, reverse=True, key=operator.attrgetter('date_of_birth'))
#     for person in sort_list_person:
#         if int(first_year) < person.how_many_years() < int(last_year):
#             print(person.about())

"""
2)
Создать подобие социальной сети.
Описать классы, которые должны выполнять соответствующие функции 
(Предлагаю насследовать класс авторизации от класса регистрации). 
Добавить проверку на валидность пароля (содержание символов и цифр), 
проверка на уникальность логина пользователя.
Человек заходит, и имеет возможность зарегистрироваться (ввод логин, пароль, потдверждение пароля), 
далее входит в свою учетную запись.
Добавить возможность выхода из учетной записи, и вход в новый аккаунт. 
Создать класс User, 
котоырй должен разделять роли обычного пользователя и администратора. 
При входе под обычным пользователем мы можем добавить новый пост, с определённым содержимим, 
так же пост должен содержать дату публикации. 
Под учётной записью администратора мы можем увидеть всех пользователей нашей системы, дату их регистрации, и их посты.
"""

import re
import datetime

user_list = []
post_dict = {}


class SocialNetwork:
    """class about social network"""
    pass


class User:
    """user class"""
    def __init__(self, name, password, nickname, admin=0, login=0, post_list=None):
        if post_list is None:
            post_list = []
        self._name = name
        self._password = password
        self._nickname = nickname
        self._admin = admin
        self._login = login
        self._date_registration = datetime.datetime.now().strftime('%Y%m%d')
        self._post_list = post_list

    def set_post(self, text):
        post_dict.update({datetime.datetime.now().strftime('%Y%m%d'): text})
        self._post_list.append(post_dict)
        post_dict.clear()
        return True

    def get_posts(self):
        return self._post_list

    def get_list_posts(self):
        for post in self._post_list:
            print(post.items())

    def get_date_registration(self):
        return self._date_registration

    def set_name(self, value):
        self._name = value

    def get_name(self):
        return self._name

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name)

    def set_password(self, value):
        self._password = value

    def get_password(self):
        return self._password

    def del_password(self):
        del self._password

    password = property(get_password, set_password, del_password)

    def set_nickname(self, value):
        self._nickname = value

    def get_nickname(self):
        return self._nickname

    def del_nickname(self):
        del self._nickname

    nickname = property(get_nickname, set_nickname, del_nickname)

    def set_admin(self, value):
        self._admin = value

    def get_admin(self):
        return self._admin

    admin = property(get_admin, set_admin)

    def is_admin(self):
        if self._admin == 1:
            return True
        else:
            return False

    def set_login(self, value):
        self._login = value

    def get_login(self):
        return self._login

    login = property(get_login, set_login)


class Registration:
    COUNT_USER = 0
    """class registration in social network"""

    def password_check(self, password):
        """
        Verify the strength of 'password'
        Returns a dict indicating the wrong criteria
        A password is considered strong if:
            8 characters length or more
            1 digit or more
            1 symbol or more
            1 uppercase letter or more
            1 lowercase letter or more
        """
        # calculating the length
        length_error = len(password) < 8
        # searching for digits
        digit_error = re.search(r"\d", password) is None
        # searching for uppercase
        uppercase_error = re.search(r"[A-Z]", password) is None
        # searching for lowercase
        lowercase_error = re.search(r"[a-z]", password) is None
        # searching for symbols
        symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None
        # overall result
        password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)
        # return {
        #     'password_ok': password_ok,
        #     'length_error': length_error,
        #     'digit_error': digit_error,
        #     'uppercase_error': uppercase_error,
        #     'lowercase_error': lowercase_error,
        #     'symbol_error': symbol_error,
        # }
        return password_ok

    def check_user(self, value):
        for user in user_list:
            if user.get_name == value:
                return True
        return False

    def registration_new_user(self, name, password, nickname):
        self.COUNT_USER += 1

        if self.check_user(name):
            print(f'This {name} already exists')
        else:
            user_name = name
            print('name', name)

        if self.password_check(password):
            user_password = password
        else:
            print('password is bed')
        user_nickname = nickname

        user = User(user_name, user_password, user_nickname)

        user_list.append(user)

    def del_user(self, name):
        for user in user_list:
            if user.name == name:
                del user.name
                return f'user {user.name} deleted'
        return f'I cant find user {name}'


class Login(User):

    def login_user(self):
        self.login = 1
        return True

    def logout_user(self):
        self.login = 0

    def check_user_is_login(self, user):
        if user.login == 1:
            return True
        else:
            return False


a = 0
while a < 1:
    new_u_name = input('name =')
    new_u_nik = input('nik = ')
    new_u_pass = input('pass = ')

    new_u = Registration()
    new_u.registration_new_user(new_u_name, new_u_pass, new_u_nik)

    a += 1

for user in user_list:
    print(user)
    print(user.name)
    print(user.login)
    print(user.nickname)
