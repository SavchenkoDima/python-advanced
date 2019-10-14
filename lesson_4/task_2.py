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
print(user_list)
post_dict = {}


class SocialNetwork:
    """class about social network"""
    pass

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
        for user in user_list:
            if user.name == self.name:
                return True
        return False

    def registration_new_user(self):
        self.COUNT_USER += 1

        if self.check_user():
            print(f'This {self.name} already exists')
        else:
            user_name = True

        if self.password_check():
            user_pass = True
        else:
            print(f'password {self.password} is bed')

        if user_name is True and user_pass is True:
            user_list.append(self)
        else:



    def del_user(self, name):
        for user in user_list:
            if user.name == name:
                del user.name
                return f'user {user.name} deleted'
        return f'I cant find user {name}'


class Login:

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



class User(Registration, Login):
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


a = 0
while a < 2:
    new_u_name = input('name =')
    new_u_nik = input('nik = ')
    new_u_pass = input('pass = ')
    new_user1 = User(new_u_name, new_u_pass, new_u_nik)
    new_user1.registration_new_user()
    a += 1

for user in user_list:
    print(user.name)
    print(user.password)
    print(user.nickname)





# a = 0
# while a < 1:
#     new_u_name = input('name =')
#     new_u_nik = input('nik = ')
#     new_u_pass = input('pass = ')
#
#     new_u = Registration()
#     new_u.registration_new_user(new_u_name, new_u_pass, new_u_nik)
#
#     a += 1
#
# for user in user_list:
#     print(user)
#     print(user.name)
#     print(user.login)
#     print(user.nickname)