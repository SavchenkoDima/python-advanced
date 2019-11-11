import config
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from models.models import Category, Product, Texts, Users
import keyboards
from models import models
from keyboards import ReplyKB

bot = telebot.TeleBot(config.TOKEN)
hideBoard = ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard

# @bot.message_handler(func=lambda message: message.text)
# def test(message):
#     print(message)

@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    user_dict = {
        'first_name': message.chat.first_name,
        'username': message.chat.username,
        'last_name': message.chat.last_name,
        'user_id': message.chat.id,
    }
    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    #print('Users.objects.get(user_id=message.chat.id)', Users.objects.get(user_id=message.chat.id))
    try:
        if Users.objects.get(user_id=message.chat.id):
            user = Users.objects.get(user_id=message.chat.id)
            bot.send_message(message.chat.id, text=f'Hi again {user.username}', reply_markup=keyboard)
        else:
            Users(**user_dict).save()
            bot.send_message(message.chat.id, text=f'Hello new buyer {message.chat.username}', reply_markup=keyboard)
    except Exception:
        Users(**user_dict).save()
        bot.send_message(message.chat.id, text=f'Hello new buyer {message.chat.username}', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['products'])
def show_categoryies(message):
    category_queryset = models.Category.is_main()
    kb = keyboards.InlineKB(
        iterable=category_queryset,
        lookup_fields='id',
        named_arg='category',
    )
    bot.send_message(message.chat.id, message.text, reply_markup=kb.generate_kb())


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'category')
def show_product_or_sub_category(call):
    obj_id = call.data.split('_')[1]
    print(obj_id)
    category = models.Category.objects(id=obj_id).get()
    if category.is_parent:
        kb = keyboards.InlineKB(
            iterable=category.subcategory,
            lookup_fields='id',
            named_arg='category',
        )
        bot.edit_message_text(text=category.title, chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=kb.generate_kb()
                              )
    else:
        products = Product.objects(category=obj_id)
        for product in products:
            photo = product.photo_product.read()
            keyboard = InlineKeyboardMarkup(row_width=2)
            buttons = [InlineKeyboardButton(f'{i}',
                                            callback_data=f'{key}_{product.id}')
                       for key, i in keyboards.product_kb.items()]
            keyboard.add(*buttons)
            bot.send_photo(chat_id=call.message.chat.id, photo=photo,
                           caption=f'<b>{product.title}</b>  Цена: <i> {product.price} 💵 </i> '
                                   f' <code> {product.description} </code>',
                           reply_markup=keyboard,
                           parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'add to basket')
def test(call):
    obj_id = call.data.split('_')[1]
    print('obj_id', obj_id)
    product = Product.objects.get(id=obj_id)
    print(product.title)
    print(call.message.chat.id)
    user = Users.objects.get(user_id=call.message.chat.id)
    print(user.username)
    user.add_product(product)
    user.save()
    # basket_kb = {
    #     'news': 'Последние новости',
    #     'products': 'Продукты',
    #     'sales': 'Продукты со скидкой',
    #     'about': 'информация о магазине',
    #     'basket': f'в корзине {user.count_product()} товара'
    # }
    # keyboard = ReplyKB().generate_kb(*basket_kb.values())
    # bot.send_message(call.message.chat.id, '👍' ,reply_markup=keyboard)
    # print(call.data)


@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['news'])
def inline(message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    text_obj = Texts.objects()
    buttons = [InlineKeyboardButton(f'{text.title}:{text.body}',
                                    callback_data=str(text.title)) for text in text_obj]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, message.text, reply_markup=keyboard)
    # ##
    # category_obj_db = Product.objects.get(id='5dc5c79087cf8fe5055b3b30')
    # photo = category_obj_db.photo_product.read()
    # bot.send_photo(message.chat.id, photo=photo)


if __name__ == '__main__':
    bot.polling(none_stop=True)
