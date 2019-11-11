from mongoengine import *

connect('web_shop_bot')


class Texts(Document):
    title = StringField(unique=True)
    body = StringField(max_length=4096)
    photo_product = ImageField()


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


    @property
    def get_product(self, **kwargs):
        return Product.objects(category=self, **kwargs)

    def add_subcategory(self, obj):
        self.subcategory.append(obj)

    @classmethod
    def is_main(cls):
        return cls.objects(is_main_category=True)


class Product(Document):
    title = StringField(max_length=255)
    description = StringField(max_length=1024)
    price = IntField(min_value=0)
    new_prise = IntField(min_value=0)
    is_discount = BooleanField(default=False)
    properties = EmbeddedDocumentField(Properties)
    category = ReferenceField(Category)
    photo_product = ImageField()

    @property
    def get_price(self):
        if self.is_discount:
            return str(self.new_prise/100)
        return str(self.price/100)

    @classmethod
    def get_discount_products(cls, **kwargs):
        return cls.objects(is_discount=True)


class Users(Document):
    first_name = StringField(max_length=255, required=True)
    username = StringField(max_length=255, required=True)
    last_name = StringField(max_length=255, required=True)
    user_id = IntField(required=True)
    basket = ListField(ReferenceField(Product))

    def add_product(self, obj):
        """
        :type obj: object
        """
        self.basket.append(obj)

    def count_product(self):
        return len(self.basket)
