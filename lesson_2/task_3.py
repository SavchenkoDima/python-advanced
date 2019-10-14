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