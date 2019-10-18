#!/usr/bin/python
# -*- coding: UTF-8

"""
2)
Создать функцию, которая будет скачивать файл из интернета по ссылке, повесить на неё созданный декоратор.
Создать список из 10 ссылок, по которым будет происходить скачивание.
Создать список потоков, отдельный поток, на каждую из ссылок.
Каждый поток должен сигнализировать, о том, что, он начал работу и по какой ссылке он работает,
так же должен сообщать когда скачивание закончится.
"""
import requests
from task_1 import decorator
from threading import Thread

# url = 'http://www.vashsad.ua/i/gallery/wallpapers/30/475_356/J2HOD4jX.jpg'
# r = requests.get(url, allow_redirects=True)
# open('google.ico', 'wb').write(r.content)

list_url = ['http://www.vashsad.ua/i/gallery/wallpapers/30/475_356/J2HOD4jX.jpg',
            'http://www.vashsad.ua/i//gallery/wallpapers/475_356/eRGfach6.jpg',
            'http://www.vashsad.ua/i//gallery/wallpapers/475_356/96OWDccB.jpg',
            'http://www.vashsad.ua/i//gallery/wallpapers/475_356/qb237CTD.jpg',
            'http://www.vashsad.ua/i//gallery/wallpapers/475_356/pn1t142L.jpg',
            'http://www.vashsad.ua/i//gallery/wallpapers/475_356/448eE2U8.jpg',
            'http://www.vashsad.ua/i//gallery/wallpapers/475_356/vdqy1FCw.jpg',
            'http://www.vashsad.ua/i//gallery/wallpapers/475_356/56Yvuu5K.jpg',
            'http://www.vashsad.ua/i/gallery/wallpapers/12/475_356/XTndBDFB.jpg',
            'http://www.vashsad.ua/i/gallery/wallpapers/12/475_356/q1TV5mci.jpg',
            ]


@decorator('d', False)
def downloaded_file(url):
    """
    :param url:
    :return True:
    """
    file = requests.get(url, allow_redirects=True)
    open(f'{url[-12:]}', 'wb').write(file.content)
    return print(f'Downloaded_file {url[-12:]} the end')


for url in list_url:
    downloaded_file(url)
