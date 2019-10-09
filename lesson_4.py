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
from abc import ABC, abstractmethod
import datetime


class Person(ABC):
    """di"""
    def __init__(self, surname, date_of_birth):
        self._surname = surname
        self._date_of_birth = date_of_birth

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @surname.deleter
    def surname(self):
        del self._surname

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value

    @date_of_birth.deleter
    def date_of_birth(self):
        del self._date_of_birth

    @abstractmethod
    def how_many_years(self):
        today = datetime.datetime.now().strftime('%Y')
        return  int(today) - int(self.date_of_birth)

    @abstractmethod
    def about(self):
        return 'My surname is {} and, I am {} years'.format(self._surname, self.how_many_years())


class Enrollee(Person):

    def __init__(self, surname, date_of_birth, faculty):
        super().__init__(surname, date_of_birth)
        self._faculty = faculty

    def about(self):
        return 'My surname is {} and, I am {} years. I am enrollee {}'.\
            format(self._surname, self.how_many_years(), self._faculty)

    def how_many_years(self):
       return super().how_many_years()

    def get_faculty(self):
        return self._faculty

    def set_faculty(self, value):
        self._faculty = value

    def del_faculty(self):
        del self._faculty

    faculty = property(get_faculty, set_faculty, del_faculty)


class Student(Person, Enrollee):
    def __init__(self, surname, date_of_birth, faculty, course):
        super().__init__(surname, date_of_birth)
        self._faculty = faculty
        self._course = course

    def about(self):
        return 'My surname is {} and, I am {} years. I am enrollee {}.I am studied on {} course '. \
            format(self._surname, self.how_many_years, self._faculty, self._course)

    def how_many_years(self):
        return super().how_many_years()

    def get_course(self):
        return self._course

    def set_course(self, value):
        self._course = value

    def del_course(self):
        del self._course

    course = property(get_course, set_course, del_course)


class Teacher(Person, Enrollee, Student):

    def __init__(self, surname, date_of_birth, faculty, position,  experience):
        super().__init__(surname, date_of_birth)
        self._faculty = faculty
        self._position = position
        self._experience = experience




Enrollee1 = Enrollee('Savchenko', '1983', 'python')

print(Enrollee1.about)





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
