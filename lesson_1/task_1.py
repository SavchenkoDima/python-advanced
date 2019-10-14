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
