"""
home work 27.09.2019
"""
"""
1)
Создать список из N элементов (от 0 до n с шагом 1). 
В этом списке вывести все четные значения.
"""
list_n_elements = []
n = 100
for i in range(0, n):
    if i % 2 == 0:
        list_n_elements.append(i)
print(list_n_elements)


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


"""
3)
Напишите программу, которая выводит на экран числа от 1 до 100. 
При этом вместо чисел, кратных трем, программа должна выводить слово Fizz,
а вместо чисел, кратных пяти — слово Buzz. 
Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz.
"""

for i in range(1, 100):
    if i % 3 == 0:
        print('Fizz')
    if i % 5 == 0:
        print('Buzz')
    if i % 15 == 0:
        print('FizzBuzz')


'''
4) 
Реализовать функцию bank, которая приннимает следующие аргументы: сумма депозита, кол-во лет, и процент. 
Результатом выполнения должна быть сумма по истечению депозита
'''


def bank(deposit_amount, number_of_years, percent):
    ''' it is bank def '''
    for year in range(1, number_of_years):
        deposit_amount = (deposit_amount*percent/100)+deposit_amount
    return deposit_amount
