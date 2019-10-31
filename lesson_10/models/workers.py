from mongoengine import *

connect('workers')


class Location(EmbeddedDocument):
    CITY_CHOICES = (
        ('Kiev', 'Kiev'),
        ('lviv', 'Lviv')
    )
    city = StringField(choices=CITY_CHOICES)
    street = StringField(max_length=256)


class Person(Document):
    fist_name = StringField(max_length=64)
    surname = StringField(max_length=64)
    age = IntField()
    experiens = IntField()
    location = EmbeddedDocumentField(Location)
