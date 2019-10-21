#!/usr/bin/python
# -*- coding: UTF-8
"""
 Написать свой контекстный менеджер для работы с файлами.
"""


class ContextManagerFile:
    def __init__(self, file_name, act):
        self._file_name = file_name
        self._act = act

    def __enter__(self):
        self.file = open(file=self._file_name, mode=self._act)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with ContextManagerFile('test.txt', 'w') as file:
    file.write('test')

with ContextManagerFile('test.txt', 'r') as file:
    print(file.readlines())
