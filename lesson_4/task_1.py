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
import operator


class Person(ABC):
    """ description """

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
        return int(today) - int(self.date_of_birth)

    @abstractmethod
    def about(self):
        return 'My surname is {} and, I am {} years'.format(self._surname, self.how_many_years())


class Enrollee(Person):
    """ description """

    def __init__(self, surname, date_of_birth, faculty):
        super().__init__(surname, date_of_birth)
        self._faculty = faculty

    def about(self):
        return 'My surname is {} and, I am {} years. I am enrollee {}'. \
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


class Student(Person):
    """ description """
    def __init__(self, surname, date_of_birth, faculty, course):
        super().__init__(surname, date_of_birth)
        self._faculty = faculty
        self._course = course

    def about(self):
        return 'My surname is {} and, I am {} years. I am enrollee {}.I am studied on {} course '. \
            format(self._surname, self.how_many_years(), self._faculty, self._course)

    def how_many_years(self):
        return super().how_many_years()

    def get_course(self):
        return self._course

    def set_course(self, value):
        self._course = value

    def del_course(self):
        del self._course

    course = property(get_course, set_course, del_course)

    def get_faculty(self):
        return self._faculty

    def set_faculty(self, value):
        self._faculty = value

    def del_faculty(self):
        del self._faculty

    faculty = property(get_faculty, set_faculty, del_faculty)


class Teacher(Person):
    """ description """

    def __init__(self, surname, date_of_birth, faculty, position, experience):
        super().__init__(surname, date_of_birth)
        self._faculty = faculty
        self._position = position
        self._experience = experience

    def about(self):
        return 'My surname is {} and, I am {} years. I work in positions {}. my experience {} years'. \
            format(self._surname, self.how_many_years(), self._position, self._experience)

    def how_many_years(self):
        return super().how_many_years()

    def get_faculty(self):
        return self._faculty

    def set_faculty(self, value):
        self._faculty = value

    def del_faculty(self):
        del self._faculty

    faculty = property(get_faculty, set_faculty, del_faculty)

    def get_position(self):
        return self._position

    def set_position(self, value):
        self._position = value

    def del_position(self):
        del self._position

    position = property(get_position, set_position, del_position)

    def get_experience(self):
        return self._experience

    def set_experience(self, value):
        self._experience = value

    def del_experience(self):
        del self._experience

    experience = property(get_experience, set_experience, del_experience)


enrollee1 = Enrollee('Abramson', 2010, 'C#')
enrollee2 = Enrollee('Babcock', 2001, 'C')
enrollee3 = Enrollee('Calhoun', 2002, 'C++')
enrollee4 = Enrollee('Daniels', 2003, 'java')
enrollee5 = Enrollee('Eddington', 2004, 'C#')

student1 = Student('Faber', 2010, 'C++', 1)
student2 = Student('Galbraith', 2005, 'C#', 2)
student3 = Student('Haig', 2006, 'java', 3)
student4 = Student('Keat', 2008, 'python', 4)
student5 = Student('Laird', 1990, 'C', 5)


teacher1 = Teacher('MacAdam', 1983, 'python', 'Teacher', 5)
teacher2 = Teacher('Nash', 1983, 'C#', 'Teacher', 10)
teacher3 = Teacher('Page', 1983, 'java', 'Head Teacher', 20)
teacher4 = Teacher('Raleigh', 1983, 'C++', 'Head Teacher', 30)
teacher5 = Teacher('Salisburry', 1983, 'C', 'Head Teacher', 35)

list_person = [enrollee1, enrollee2, enrollee3, enrollee4, enrollee5,
               student1, student2, student3, student4, student5,
               teacher1, teacher2, teacher3, teacher4, teacher5]
list_years = []
for p in list_person:
    list_years.append(p.how_many_years())

print('вы попали в программку об студентах и преподователях института')
print('Вы хотите получить полный список ?')

all_list = input('Введите свой ответ в формате "Y" или "N":').upper()

while all_list not in ('Y', 'N'):
    print('Вы ввели неверное значение!')
    all_list = input('Введите свой ответ в формате "Y" или "N":').upper()

if all_list == 'Y':
    print('Вы хотите получить отсортированный список ?')
    all_list = input('Введите свой ответ в формате "Y" или "N":').upper()
    while all_list not in ('Y', 'N'):
        print('Вы ввели неверное значение!')
        all_list = input('Введите свой ответ в формате "Y" или "N":').upper()

    if all_list == 'Y':
        sort_list_person = sorted(list_person, reverse=True, key=operator.attrgetter('date_of_birth'))
        for person in sort_list_person:
            print(person.about())
    else:
        for person in list_person:
            print(person.about())
else:
    print('Тогда сортируем по вашему желанию')
    first_year = input('Введите возраст в формате "{}" От:'.format(min(list_years)))
    while not first_year.isdigit():
        print('Вы ввели неверное значение!')
        first_year = input('Введите возраст в формате "{}" От:'.format(min(list_years)))

    last_year = input('Введите возраст в формате "{}" До:'.format(max(list_years)))
    while not last_year.isdigit():
        print('Вы ввели неверное значение!')
        last_year = input('Введите возраст в формате "{}" До:'.format(max(list_years)))

    sort_list_person = sorted(list_person, reverse=True, key=operator.attrgetter('date_of_birth'))
    for person in sort_list_person:
        if int(first_year) < person.how_many_years() < int(last_year):
            print(person.about())
