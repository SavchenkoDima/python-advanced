"""
2)
СОздать словарь Страна:Столица.
Создать список стран.
Не все страны со списка должны сходиться с названиями стран со словаря.
С помощою оператора in проверить на вхождение элемента страны в словарь,
и если такой ключ действительно существует вывести столицу.
"""

dict_country = {'Абхазия': 'Сухум',
                'Австралия': 'Канберра',
                'Буркина Фасо': 'Уагадугу',
                'Гамбия': 'Банжул',
                'Ирландия': 'Дублин',
                'Китай': 'Пекин'
                }

list_country = ['Киргизия', 'Ирландия', 'Коморы', 'Китай']

for key in list_country:
    print(dict_country.get(key, "I can't find this country"))
