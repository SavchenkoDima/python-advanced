import config
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from models.models import Category, Product, Texts
import keyboards
from models import models
from keyboards import ReplyKB

bot = telebot.TeleBot(config.TOKEN)
hideBoard = ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard

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
    buttons = [InlineKeyboardButton(f'{category.title}' if category.is_main() else '',
                                    callback_data=str(category.title)) for category in categorys_obj]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, message.text, reply_markup=keyboard)

# https://toster.ru/q/600287
# https://www.programcreek.com/python/example/93150/telegram.InlineKeyboardButton
@bot.callback_query_handler(func=lambda call: True)
def callback_e(call):
    bot.delete_message(chat_id=call.from_user.id, message_id=(call.message.message_id))

    keyboard = InlineKeyboardMarkup(row_width=3)
    categorys_obj = Category.objects.get(title=call.data)
    buttons = [InlineKeyboardButton(f'{category.title}',
                                    callback_data=str(category.title)) for category in categorys_obj.subcategory]
    keyboard.add(*buttons)
    bot.send_message(call.from_user.id, call.data, reply_markup=keyboard)

   # bot.send_message(call.message.chat.id, f'I am massage from {call.data}//{call.from_user.id, (call.message.message_id)}')


if __name__ == '__main__':
    bot.polling(none_stop=True)
