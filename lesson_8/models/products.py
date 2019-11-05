from mongoengine import *

connect('product')


class Category(Document):
    name_category = StringField(max_length=64)

class Product(Document):
    name_product = StringField(max_length=64)
    quantity = IntField(default=0)
    price = FloatField(default=0.00)
    product_for_sale = BooleanField(default=False)
    category = ReferenceField(Category)

