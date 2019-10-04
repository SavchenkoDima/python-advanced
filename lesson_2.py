"""
1)
Создать класс автомобиля.
Описать общие аттрибуты.
Создать классы легкового автомобиля и грузового.
Описать в основном классе базовые аттрибуты для автомобилей.
Будет плюсом если в классах наследниках переопределите методы базового класса.
"""


class Car:
    """  It is class about cars """
    NUMBER_OF_WHEELS = 4
    TYPE_FUEL = 'GAS'
    NUMBER_OF_DOORS = 4

    def __init__(self, color, engine_type, fuel):
        """ description """
        self._color = color
        self._engine = engine_type
        self._fuel = fuel

    def broke_down_car(self):
        """ description """
        return 'Car is broke down!'

    def drive(self):
        """ description """
        return "Car is drive!"

    def set_fuel(self, value):
        """ description """
        self._fuel += value

    def get_fuel(self):
        """ description """
        return self._fuel

    def set_engine(self, value):
        self._engine = value
        """ description """

    def get_engine(self):
        """ description """
        return self._engine

    def set_color(self, value):
        """ description """
        self._color = value

    def get_color(self):
        """ description """
        return self._color


class Truck(Car):
    """ it is class about truck """
    def __init__(self, carrying, color, engine_type, fuel):
        """ description """
        super().__init__(color, engine_type, fuel)
        self._carrying = carrying

    def set_carrying(self, value):
        """ description """
        self._carrying += value

    def get_carrying(self):
        """ description """
        return self._carrying

    def set_fuel(self, value):
        """ description """
        self._fuel += value*2


class SmallCar(Car):
    """ it is class about small car """
    def __init__(self, number_of_seats, color, engine_type, fuel):
        """ description """
        super().__init__(color, engine_type, fuel)
        self._number_of_seats = number_of_seats

    def set_number_of_seats(self, value):
        """ description """
        self._number_of_seats += value

    def get_number_of_seats(self):
        """ description """
        return self._number_of_seats

    def drive(self):
        """ description """
        return 'Car is driving very fast'


"""
2)
Создать класс магазина. 
Конструктор должен инициализировать значения: «Название магазина» и «Количество проданных товаров». 
Реализовать методы объекта, которые будут увеличивать кол-во проданных товаров, 
и реализовать вывод значения переменной класса, которая будет хранить общее количество товаров проданных 
всеми магазинами.
"""


class Shop:
    SOLD_ALL = 0
    """ description """
    def __init__(self, shop_name, quantity_goods_sold):
        """ description """
        self._shop_name = shop_name
        self._quantity_goods_sold = quantity_goods_sold

    def set_goods_sold(self, value):
        """ description """
        self._quantity_goods_sold += value
        Shop.SOLD_ALL += self._quantity_goods_sold

    def get_goods_sold(self):
        """ description """
        return self._quantity_goods_sold

    def get_sold_all(self):
        return Shop.SOLD_ALL


# shop1 = Shop('asd', 0)
# shop1.set_goods_sold(12)
#
# shop2 = Shop('dsa', 0)
# shop2.set_goods_sold(5)
#
# print(shop1.SOLD_ALL)
# print(Shop.SOLD_ALL)

"""
3)
Создать класс точки, 
реализовать конструктор который инициализирует 3 координаты (x, y, z). 
Реалзиовать методы для получения и изменения каждой из координат. 
Перегрузить для этого класса методы сложения, вычитания, деления умножения. 
Перегрузить один любой унарный метод.
Ожидаемый результат: умножаю точку с координатами 1,2,3
на другую точку с такими же координатами, получаю результат 1, 4, 9.  
"""


class Point(object):
    """ description """
    def __init__(self, coordinate_x, coordinate_y, coordinate_z):
        """ description """
        self._coordinate_x = coordinate_x
        self._coordinate_y = coordinate_y
        self._coordinate_z = coordinate_z

    def set_coordinate_x(self, value):
        """ description """
        self._coordinate_x = value

    def set_coordinate_y(self, value):
        """ description """
        self._coordinate_y = value

    def set_coordinate_z(self, value):
        """ description """
        self._coordinate_z = value

    def get_coordinate_x(self):
        """ description """
        return self._coordinate_x

    def get_coordinate_y(self):
        """ description """
        return self._coordinate_y

    def get_coordinate_z(self):
        """ description """
        return self._coordinate_z

    def __add__(self, other):
        """ description """
        return Point(self._coordinate_x + other._coordinate_x,
                     self._coordinate_y + other._coordinate_y,
                     self._coordinate_z + other._coordinate_z)

    def __sub__(self, other):
        """ description """
        return Point(self._coordinate_x - other._coordinate_x,
                     self._coordinate_y - other._coordinate_y,
                     self._coordinate_z - other._coordinate_z)

    def __mul__(self, other):
        """ description """
        return Point(self._coordinate_x * other._coordinate_x,
                     self._coordinate_y * other._coordinate_y,
                     self._coordinate_z * other._coordinate_z)

    def __truediv__(self, other):
        """ description """
        return Point(self._coordinate_x / other._coordinate_x,
                     self._coordinate_y / other._coordinate_y,
                     self._coordinate_z / other._coordinate_z)

    def __neg__(self):
        """ description """
        return Point(-self._coordinate_x, -self._coordinate_y, -self._coordinate_z)

    def __invert__(self):
        """ description """
        return Point(~self._coordinate_x, ~self._coordinate_y, ~self._coordinate_z)

    def __repr__(self):
        """ description """
        return 'Point x = {}, y = {}, z = {}'.format(self._coordinate_x, self._coordinate_y, self._coordinate_z)

    def __str__(self):
        """ description """
        return 'x = {}, y = {}, z = {}'.format(self._coordinate_x, self._coordinate_y, self._coordinate_z)


point1 = Point(1, 2, 3)
point2 = Point(1, 2, 3)
s = point1 * point2

print(s)
print(point1.__mul__(point2))
