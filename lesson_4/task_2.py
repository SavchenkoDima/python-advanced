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
import shelve

"""
Admin
Admin1234!

Dima
Dima1234!
"""






class Registration:
    COUNT_USER = 0
    """class registration in social network"""

    def password_check(self):
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
        length_error = len(self.password) < 8
        # searching for digits
        digit_error = re.search(r"\d", self.password) is None
        # searching for uppercase
        uppercase_error = re.search(r"[A-Z]", self.password) is None
        # searching for lowercase
        lowercase_error = re.search(r"[a-z]", self.password) is None
        # searching for symbols
        symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', self.password) is None
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

    def check_user(self):
        with shelve.open(db_file) as db:
            if self.name in db.keys():
                return True
        return False

    def registration_new_user(self):
        self.COUNT_USER += 1

        if self.check_user():
            print(f'This {self.name} already exists')
            return False
        else:
            user_name = True

        if self.password_check():
            user_pass = True
        else:
            print(f'password {self.password} is bed')
            return False

        if user_name is True and user_pass is True:
            with shelve.open(db_file) as db:
                db[self.name] = self
            return True

    def del_user(self):
        with shelve.open(db_file) as db:
            del db[self.name]
            return f'user {self.name} deleted'


class Authorization:

    def login_user(self):
        with shelve.open(db_file) as db:
            user = db.get(self.name, None)
            if user == None:
                print(f'Такого {self.name} пользователя нет.')
                return False
            elif user.name == self.name:
                if user.password == self.password:
                    user.login = 1
                    print(f'Добро пожаловать {user.name} в сеть')
                    return True
                else:
                    print('Вы ошиблись паролем')
                    return False
        print(f'Такого {self.name} пользователя нет.')
        return False

    def logout_user(self):
        self.login = 0

    def check_user_is_login(self):
        if self.login == 1:
            return True
        else:
            return False


class User(Registration, Authorization):
    """user class"""
    def __init__(self, name, password, admin=0, login=0, post_list=None):
        if post_list is None:
            post_list = []
        self._name = name
        self._password = password
        self._admin = admin
        self._login = login
        self._date_registration = datetime.datetime.now().strftime('%Y%m%d')
        self._post_list = post_list

    def get_date_registration(self):
        return self._date_registration

    def set_post(self, text):
        post_dict.update({datetime.datetime.now().strftime('%Y%m%d'): text})
        self._post_list.append(post_dict)
        print(self._post_list)
        with shelve.open(db_file) as db:
            db[self.name] = self
        post_dict.clear()
        return True

    def get_posts(self):
        with shelve.open(db_file) as db:
            self._post_list = db.get(self.name)
            return self._post_list

    def get_list_posts(self):
        with shelve.open(db_file) as db:
            user = db.get(self.name)
            for post in user._post_list:
                print(post)

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

    def save_user(self):
        with shelve.open(db_file) as db:
            db[self.name] = self

    def load_user(self):
        with shelve.open(db_file) as db:
            return db.get(self.name)

    def update_user(self):
        with shelve.open(db_file) as db:
            db[self.name] = self

    def print_list_user(self):
        with shelve.open(db_file) as db:
            for user in db.items():
                print(f'У Вас есть ползователь {user[1].name} датой регистрации {user[1].get_date_registration()}')



db_file = 'DB'
user_list = []
post_dict = {}

while True:
    print('')
    print('вы попали в программку социальная сеть')
    print('Вы хотите ввойти в сеть или зарегистрироваться?')
    print('')
    answer = input('Введите свой ответ в формате "Y" - войти  или "N" зарегистрироваться:').upper()

    while answer not in ('Y', 'N'):
        print('Вы ввели неверное значение!')
        answer = input('Введите свой ответ в формате "Y" или "N":').upper()

    if answer == 'Y':
        print('Введите свой логин и пароль')
        in_login = input('name =')
        in_pass = input('pass = ')
        in_admin = input('admin (0,1)= ')

        user_log = User(in_login, in_pass, admin=int(in_admin))
        if user_log.login_user() == False:
            continue

        print('')
        print('Admin', user_log.is_admin())
        print('')
        print('Admin = ', user_log.get_admin())
        print('')
        if user_log.is_admin() == True:
            print('Все пользователи')
            user_log.print_list_user()

        answer = input('хотите разместить новую статью "Y" или "N":').upper()
        while answer not in ('Y', 'N'):
            print('Вы ввели неверное значение!')
            answer = input('Введите свой ответ в формате "Y" или "N":').upper()

        if answer == 'Y':
            text = input('введите ваш текст')
            user_log.set_post(text)
            user_log.save_user()

        else:
            answer = input('хотите выйти "Y" или "N":').upper()
            while answer not in ('Y', 'N'):
                print('Вы ввели неверное значение!')
                answer = input('Введите свой ответ в формате "Y" или "N":').upper()

            if answer == 'Y':
                user_log.logout_user()
                print('Пока')


    else:
        print('Тогда вы хотите пройти регистрацию')
        new_user_name = input('name =')
        new_user_pass = input('pass = ')
        new_user = User(new_user_name, new_user_pass)
        if new_user.registration_new_user():
            print("спасибо за регистрацию")
