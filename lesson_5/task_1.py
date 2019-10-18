#!/usr/bin/python
# -*- coding: UTF-8
"""
1)
Создать декоратор, который будет запускать функцию в отдельном потоке.
Декоратор должен принимать следующие аргументы: название потока, является ли поток демоном.
"""
from threading import Thread


def decorator(name, daemon):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Started Thread {name}, {args[0]}")
            func_thread = Thread(target=func, args=[*args], kwargs=kwargs, name=name, daemon=daemon)
            func_thread.start()
            print(f'Thread is {func_thread.is_alive()}')

            return func_thread

        return wrapper

    return actual_decorator

# @decorator('Dima', True)
# def say_hello(name):
#     print(f"Hello, {name}")
#
#
# say_hello('Ale')
