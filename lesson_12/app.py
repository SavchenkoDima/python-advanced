import config
import telebot
import keyboards
from models import models
from flask_restful import Api
from keyboards import ReplyKB
from flask import Flask, request, abort
from resousers.resource import CategoryResurse, ProductResurse
from models.models import Category, Product, Texts, Users, Basket, BasketHistory
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove


bot = telebot.TeleBot(config.TOKEN)
app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryResurse, '/Category/', '/Category/<string:id>')
api.add_resource(ProductResurse, '/Product/', '/Product/<string:id>')

# Process webhook calls
@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)

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
    kb = keyboards.InlineKB(key='root', lookup_fields='id', named_arg='category')
    bot.send_message(message.chat.id, message.text, reply_markup=kb.generate_kb())


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'category')
def show_product_or_sub_category(call):
    obj_id = call.data.split('_')[1]
    category = models.Category.objects(id=obj_id).get()
    if category.is_parent:
        kb = keyboards.InlineKB(
            iterable=category.subcategory,
            lookup_fields='id',
            named_arg='category',
        )
        kb.generate_kb()
        kb.add(InlineKeyboardButton(text=f'<<', callback_data=f'back_{category.id}'))
        bot.edit_message_text(text=category.title, chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=kb
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
                           caption=f'<b>{product.title}</b>  Цена: <i> {product.get_price} 💵 </i> '
                                   f' <code> {product.description} </code>',
                           reply_markup=keyboard,
                           parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'back')
def go_back(call):
    obj_id = call.data.split('_')[1]
    category = models.Category.objects(id=obj_id).get()
    if category.is_root:
        kb = keyboards.InlineKB(key='root', lookup_fields='id', named_arg='category')
        kb.generate_kb()
    else:
        kb = keyboards.InlineKB(
            iterable=category.parent.subcategory,
            lookup_fields='id',
            named_arg='category',
        )
        kb.generate_kb()
        kb.add(InlineKeyboardButton(text=f'<<{category.parent.title}', callback_data=f'back_{category.parent.id}'))
    text = 'Категории' if not category.parent else category.parent.title
    bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'add to basket')
def test(call):
    obj_id = call.data.split('_')[1]
    product = Product.objects.get(id=obj_id)
    user = Users.objects.get(user_id=call.message.chat.id)
    try:
        basket = Basket.objects.get(user=user)
        if basket and basket.bought == False:
            basket.add_product(product)
            basket.save()
        else:
            basket = Basket(user=user)
            basket.add_product(product)
            basket.save()
    except:
        basket = Basket(user=user)
        basket.add_product(product)
        basket.save()

@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'show basket')
def show_basket(call):
    user = Users.objects.get(user_id=call.message.chat.id)
    basket = Basket.objects.get(user=user, bought=False)
    if len(basket.basket_list) == 0:
        bot.send_message(call.message.chat.id, 'Карзина пуста Добавте товар.')
    else:
        for product in basket.basket_list:
            photo = product.photo_product.read()
            keyboard = InlineKeyboardMarkup(row_width=2)
            buttons = [InlineKeyboardButton(f'{i}', callback_data=f'{key}_{product.id}')
                       for key, i in keyboards.basket_kb.items()]
            keyboard.add(*buttons)
            bot.send_photo(chat_id=call.message.chat.id, photo=photo,
                           caption=f'<b>{product.title}</b>  Цена: <i> {product.get_price} 💵 </i> '
                                   f' <code> {product.description} </code>',
                           reply_markup=keyboard,
                           parse_mode='HTML')
    if len(basket.basket_list):
        keyboard = InlineKeyboardMarkup(row_width=2)
        buttons = [InlineKeyboardButton(f'{i}', callback_data=f'{key}_{basket.id}')
                   for key, i in keyboards.basket_buy_kb.items()]
        keyboard.add(*buttons)
        bot.send_message(chat_id=call.message.chat.id, text=f'Стоимость всех товаров {basket.total_cost()} грн',
                         reply_markup=keyboard,)

@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'Buy')
def buy_basket(call):
    user = Users.objects.get(user_id=call.message.chat.id)
    basket = Basket.objects.get(id=call.data.split('_')[1])
    basket.basket_closed
    BasketHistory(basket_list=basket).save()
    user.update(basket=basket)
    bot.send_message(chat_id=call.message.chat.id, text=f'Спасибо за покупку')
    print('buy_basket')



@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'clear')
def clear_basket(call):
    user = Users.objects.get(user_id=call.message.chat.id)
    basket = Basket.objects.get(id=call.data.split('_')[1])
    if not basket.bought:
        basket.delete()
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        print('clear_basket')
    else:
        bot.send_message(chat_id=call.message.chat.id, text=f'Эта карзина уже была купленна {basket.bought_date}.')


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'delete')
def delete_product(call):
    user = Users.objects.get(user_id=call.message.chat.id)
    product = Product.objects.get(id=call.data.split('_')[1])
    basket = Basket.objects.get(user=user, bought=False)
    basket.basket_list.remove(product)
    basket.save()
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    # obj_id = call.data.split('_')[1]
    # print('obj_id', obj_id)
    # product = Product.objects.get(id=obj_id)
    # print(product.title)
    # print(call.message.chat.id)
    # user = Users.objects.get(user_id=call.message.chat.id)
    # basket = Basket(user=user)
    # basket.add_product(product)
    # basket.save()
    # print(basket.user.id)

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


if __name__ == '__main__':
    import time
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(config.webhook_url, certificate=open('webhook_cert.pem', 'r'))
    app.run(debug=True)

    # try:
    #     basket = Basket.objects.get(user=user, bought=False)
    #     print(basket.total_cost())
    #     print('len=', len(basket.basket_list))
    #     if len(basket.basket_list) == 0:
    #         bot.send_message(call.message.chat.id, 'Карзина пуста Добавте товар.')
    #         print('1111')
    #     else:
    #         for product in basket.basket_list:
    #
    #             photo = product.photo_product.read()
    #             keyboard = InlineKeyboardMarkup(row_width=2)
    #             buttons = [InlineKeyboardButton(f'{i}', callback_data=f'{key}_{product.id}')
    #                        for key, i in keyboards.basket_kb.items()]
    #             keyboard.add(*buttons)
    #             # bot.send_photo(chat_id=call.message.chat.id, photo=photo,
    #             #                caption=f'<b>{product.title}</b>  Цена: <i> {product.get_price} 💵 </i> '
    #             #                        f' <code> {product.description} </code>',
    #             #                reply_markup=keyboard,
    #             #                parse_mode='HTML')
    #             #bot.send_message(chat_id=call.message.chat.id, text=basket.total_cost())
    # except:
    #     print(Exception)
    #     print('2222')
    #     bot.send_message(call.message.chat.id, 'Карзина пуста Добавте товар.')