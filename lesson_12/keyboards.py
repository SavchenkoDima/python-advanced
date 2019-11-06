from telebot.types import ReplyKeyboardMarkup, KeyboardButton

beginning_kb = {
    'news': 'Последние новости',
    'products': 'Продукты',
    'sales': 'Продукты со скидкой',
    'about': 'информация о магазине',
}


class ReplyKB(ReplyKeyboardMarkup):
    def __init__(self, resize_keyboard=True, one_time_keyboard=True, row_width=3):
        super().__init__(resize_keyboard=resize_keyboard,
                         one_time_keyboard=one_time_keyboard,
                         row_width=row_width)

    def generate_kb(self, *args):
        """

        :param args: button names
        :return:
        """
        buttons = [KeyboardButton(x) for x in args]
        self.add(*buttons)
        return self
