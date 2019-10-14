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
