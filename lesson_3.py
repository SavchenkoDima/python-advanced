"""
1)
Создать декоратор с аргументами.
Который будет вызывать функцию, определенное кол-во раз,
будет выводить кол-во времени затраченного на выполнение данной функции и её название.
"""
import time


def decorator(num_of_repeats):
    def actual_decorator(funk):
        start_time_all = time.perf_counter()
        def wrapper(*args, **kwargs):
            results = []
            time_results = {}
            for i in range(num_of_repeats):
                start_time_step = time.perf_counter()
                result = funk(*args, **kwargs)
                results.append(result)
                name_funk = f'Name funk = {funk.__name__}'
                time_step = (time.perf_counter() - start_time_step)
                time_results.update({f'step {i}': time_step})
            time_all = time.perf_counter() - start_time_all
            return name_funk, f'time all = {time_all}', time_results, results

        return wrapper

    return actual_decorator


@decorator(30)
def hello(name):
    return f'hello,{name}'


print(hello('Hi'))

"""
2)
Создать класс структуры данных Стек, Очередь. 
Создать класс комплексного числа и реализовать для него арифметические операции.
"""


class Stack:
    """ description """

    def __init__(self):
        """ description """
        self.items = []

    def is_empty(self):
        """ description """
        return self.items == []

    def push(self, item):
        """ description """
        self.items.append(item)

    def pop(self):
        """ description """
        return self.items.pop()

    def peek(self):
        """ description """
        return self.items[len(self.items) - 1]

    def size(self):
        """ description """
        return len(self.items)


class Queue:
    """ description """

    def __init__(self):
        """ description """
        self.items = []

    def is_empty(self):
        """ description """
        return self.items == []

    def enqueue(self, item):
        """ description """
        self.items.insert(0, item)

    def dequeue(self):
        """ description """
        return self.items.pop()

    def size(self):
        """ description """
        return len(self.items)


class Complex:
    """ description """

    def __init__(self, real_parts, imaginary_parts):
        """ description """
        self._real_parts = real_parts
        self._imaginary_parts = imaginary_parts

    def set_imaginary_parts(self, value):
        """ description """
        self._imaginary_parts = value

    def get_imaginary_parts(self):
        """ description """
        return self._imaginary_parts

    def set_real_parts(self, value):
        """ description """
        self._real_parts = value

    def get_real_parts(self):
        """ description """
        return self._real_parts

    def print_complex(self, real_parts, imaginary_parts):
        """ description """
        sign = '+' if imaginary_parts >= 0 else ''
        return '({}{}{}j)'.format(round(real_parts), sign, round(imaginary_parts))

    def __str__(self):
        """ description """
        sign = '+' if self.get_imaginary_parts() >= 0 else ''
        return '{}{}{}j'.format(self.get_real_parts(), sign, self.get_imaginary_parts())

    def __add__(self, other):
        """ description """
        return self.print_complex(self.get_real_parts() + other.get_real_parts(),
                                  self.get_imaginary_parts() + other.get_imaginary_parts())

    def __sub__(self, other):
        """ description """
        return self.print_complex(self.get_real_parts() - other.get_real_parts(),
                                  self.get_imaginary_parts() - other.get_imaginary_parts())

    def __mul__(self, other):
        """ description """
        return self.print_complex(self.get_real_parts() * other.get_real_parts() +
                                  ((self.get_imaginary_parts() * other.get_imaginary_parts()) * -1),
                                  self.get_real_parts() * other.get_imaginary_parts() +
                                  self.get_imaginary_parts() * other.get_real_parts()
                                  )

    def __truediv__(self, other):
        """ description """
        second_part = (other.get_real_parts() ** 2 + other.get_imaginary_parts() ** 2)

        return self.print_complex((self.get_real_parts() * other.get_real_parts() +
                                   ((self.get_imaginary_parts() * (other.get_imaginary_parts()) * -1) * -1))
                                  / second_part,
                                  (self.get_real_parts() * (other.get_imaginary_parts() * -1) +
                                   self.get_imaginary_parts() * other.get_real_parts())
                                  / second_part)


w = 13
e = 1
x = -7
d = 6

a = Complex(w, e)
b = Complex(x, d)

c = a * b
print('MY = ', c)

r = complex(w, e)
t = complex(x, d)

print('True = ', r * t)
