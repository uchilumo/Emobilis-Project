from peewee import *
from os import path
ROOT = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(ROOT,"users.db"))

class User(Model):
    names = CharField()
    email = CharField (unique=True)
    password = CharField()

    class Meta:
        database = db


class Person (Model):
    owner = ForeignKeyField(User, related_name="persons")
    names = CharField()
    weight = DecimalField()
    age = IntegerField()

    class Meta:
        database = db


User.create_table(fail_silently=True)
Person.create_table(fail_silently=True)

