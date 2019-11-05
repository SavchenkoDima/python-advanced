# a = tuple([1, 2])
#
# print(type(type(a)))
# print(type(int))
#
# my_class = type(
#     'classExample',
#     (),
#     {
#         'attr_1': 100,
#         'attr_2': 200,
#         'get_attr_1': lambda self: self.attr_1,
#         'get_attr_2': lambda self: self.attr_2,
#     }
# )
#
# obj = my_class()
# print(obj.get_attr_2())
#
# print(type(obj))
#
#
# class MyMetaClass(type):
#
#     def __new__(mcs, name, base, attrs):
#         print(name, base, attrs)
#
#         if 'CLASSFIELD1' in attrs:
#             raise Exception('Error')
#
#         if attrs.get("CLASS_FIELD_1", 0) < 100:
#             attrs["CLASS_FIELD_1"] = 1000
#
#         if attrs.get('verywell'):
#             attrs['verywell'] = 'my_value'
#         return super().__new__(mcs, name, base, attrs)
#
#
# class OurClass(metaclass=MyMetaClass):
#     CLASS_FIELD_1 = 1
#     CLASS_FIELD_2 = 2
#
#     def __init__(self, value):
#         self._value = value
#
# print(OurClass.CLASS_FIELD_1)
#
#
# from abc import ABC, abstractmethod
#
#
#
#
# class Vehicle(ABC):
#
#     @abstractmethod
#     def move(self):
#         print("moving")
#
#
# class Car(Vehicle):
#
#     def __init__(self, model):
#         self._model = model
#
#     def move(self):
#         super().move()
#
#
# car = Car('BMW')
# car.move()
#
#
# class Vehicle:
#
#     def move(self):
#         raise NotImplementedError
#
#
# class Car(Vehicle):
#
#     def __init__(self, model):
#         self._model = model
#
#     def move(self):
#         print('123')
#
#
#
# car = Car('BMW')
# car.move()
#
#
#
# class Vehicle(ABC):
#
#     @abstractmethod
#     def move(self):
#         print("moving")
#
#     def get_fuel(self):
#         return self._fuel
#
#
# class Car(Vehicle):
#
#     def __init__(self, model, fuel=0):
#         self._model = model
#         self._fuel = fuel
#
#     def move(self):
#         super().move()
#
#
# car = Car('BMW')
# car.move()
# car.get_fuel()


class PropertyEaxsample:

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

    def set_x(self, value):
        self._x = value

    def get_x(self):
        return self._x

    x = property(get_x, set_x)



obj = PropertyEaxsample

obj.x = 99

print(obj.x)


class DecoratorsExample:
    NUM = 0

    def __init__(self):
        self._value = 100

    @classmethod
    def increacse_num(cls, num):
        cls.NUM += num

    @classmethod
    def get_num(cls):
        return cls.NUM

    @classmethod
    def create_one_more(cls):
        return cls()

    @staticmethod
    def my_funk():
        print("HHH")
#
# DecoratorsExample.increacse_num(100)
# print(DecoratorsExample.get_num())
# DecoratorsExample.my_funk()
#
#
# class Singletone(type):
#     isinstance = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls.isinstance:
#             cls.isinstance[cls] = super().__call__(*args, **kwargs)
#         else:
#             raise Exception('Alert')
#
# class MyClass(metaclass=Singletone):
#
#     def __init__(self):
#         self._x = 100
#
# a = MyClass()
# b = MyClass()
#
# a = '1'
#
#a.alf


# class Exm:
#     """
#     :except
#     """
#
#     def __init__(self, arg1, arg2):
#         self._arg1 = arg1
#         self._arg2 = arg2
#
#     def __call__(self, *args, **kwargs):
#         """
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         print(self.__doc__)
#
#
# obj = Exm(1, 2)
# obj()
#
#
# class Dec:
#     def __init__(self, f):
#         self._f = f
#
#     def __call__(self, *args, **kwargs):
#         print('1')
#         self._f()
#         print("end")
#
#
# @Dec
# def fu():
#     print('HH')


list_var = [i for i in range(100) if not i % 2]
#print(list_var)

dic_var = dict(key1='1', key2='2', key3='3')

new_dic = {key: value for key, value in dic_var.items() if value == '3'}
