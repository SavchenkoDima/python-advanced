#!/usr/bin/python
# -*- coding: UTF-8
"""
1)
Написать контекстный менеджер для работы с SQLite DB.
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


with ContextManagerDB('test.db') as conn:
    conn = conn.execute(' select * from user ')

    print(conn.fetchall())
