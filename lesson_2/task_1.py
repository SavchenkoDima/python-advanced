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
