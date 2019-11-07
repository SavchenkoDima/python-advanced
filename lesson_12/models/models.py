from mongoengine import *

connect('web_shop_bot')


class Texts(Document):
    title = StringField(unique=True)
    body = StringField(max_length=4096)


class Properties(DynamicEmbeddedDocument):
    weight = FloatField(min_value=0)
    pass


class Category(Document):
    title = StringField(max_length=255, required=True)
    description = StringField(max_length=512)
    subcategory = ListField(ReferenceField('self'))
    is_main_category = BooleanField(default=False)

    @property
    def is_parent(self):
        return bool(self.subcategory)

    def is_main(self):
        return self.is_main_category

    @property
    def get_product(self, **kwargs):
        return Product.objects(category=self, **kwargs)

    def add_subcategory(self, obj):
        self.subcategory.append(obj)


class Product(Document):
    title = StringField(max_length=255)
    description = StringField(max_length=1024)
    price = IntField(min_value=0)
    new_prise = IntField(min_value=0)
    is_discount = BooleanField(default=False)
    properties = EmbeddedDocumentField(Properties)
    category = ReferenceField(Category)

    @property
    def get_price(self):
        if self.is_discount:
            return str(self.new_prise/100)
        return str(self.price/100)

    @classmethod
    def get_discount_products(cls, **kwargs):
        return cls.objects(is_discount=True)
