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


shop1 = Shop('asd', 0)
shop1.set_goods_sold(12)

shop2 = Shop('dsa', 0)
shop2.set_goods_sold(5)

print(shop1.SOLD_ALL)
print(Shop.SOLD_ALL)
