import config
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from models.models import Category, Product, Texts
import keyboards
from models import models
from keyboards import ReplyKB

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # greetings_str = models.Texts(title='Greetings').get().boody
    greetings_str = 'Hy'
    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    bot.send_message(message.chat.id, greetings_str, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Продукты')
def inline(message):
    keyboard = InlineKeyboardMarkup(row_width=3)
    categorys_obj = Category.objects()
    for i in categorys_obj:

        if not i.is_parent:
            print(i.title)
    #buttons = [InlineKeyboardButton(f'{category.title}', callback_data=str(category.title)) for category in categorys_obj]
    #keyboard.add(*buttons)
    #bot.send_message(message.chat.id, message.text, reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
