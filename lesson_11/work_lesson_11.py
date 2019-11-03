import telebot
import lesson_11.config
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(lesson_11.config.token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'MASSAGE')
    keyboard = ReplyKeyboardMarkup(
        one_time_keyboard=True,
        resize_keyboard=True
    )
    list_of_buttons = [KeyboardButton(text=f'Botton-{k}') for k in range(6)]
    keyboard.add(*list_of_buttons)
    bot.send_message(message.chat.id, 'TEXT', reply_markup=keyboard)



@bot.message_handler(commands='inline')
def inline(message):
    keyboard = InlineKeyboardMarkup(row_width=4)
    buttons = [InlineKeyboardButton(f'inline-{k}', callback_data=str(k)) for k in range(12)]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, 'inline', reply_markup=keyboard)




# @bot.message_handler(func=lambda message: message.text == 'hi')
# def hello(message):
#     bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

@bot.callback_query_handler(func=lambda call: True )
def callback_e(call):
    print(call)
    bot.send_message(call.message.chat.id, f'I am massage from {call.data}')



bot.polling(none_stop=False)

