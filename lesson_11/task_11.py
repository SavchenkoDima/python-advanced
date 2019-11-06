import telebot
import lesson_11.config
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from mongoengine import *

connect('telbotdb')


class Category(Document):
    name_category = StringField(max_length=64)


class User(Document):
    name_product = StringField(max_length=64)
    quantity = IntField(default=0)
    price = FloatField(default=0.00)
    product_for_sale = BooleanField(default=False)
    category = ReferenceField(Category)


bot = telebot.TeleBot(lesson_11.config.token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hey. I am a bot consultant. I want to know your data.')
    bot.send_message(message.chat.id, 'Enter your Name')
    bot.register_next_step_handler(message, last_name)


def last_name(message):
    bot.send_message(message.chat.id, 'Enter your last name')
    bot.register_next_step_handler(message, email_address)


def email_address(message):
    bot.send_message(message.chat.id, 'Enter your email address')
    bot.register_next_step_handler(message, phone_number)


def phone_number(message):
    bot.send_message(message.chat.id, 'Enter your phone number')
    bot.register_next_step_handler(message, address)


def address(message):
    bot.send_message(message.chat.id, 'Enter your address')
    bot.register_next_step_handler(message, wishes)


def wishes(message):
    bot.send_message(message.chat.id, 'Show wishes')


# @bot.message_handler(func=lambda message: message.text == 'hi')
# def hello(message):
#     bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_e(call):
    print(call)
    bot.send_message(call.message.chat.id, f'I am massage from {call.data}')


bot.polling(none_stop=False)
