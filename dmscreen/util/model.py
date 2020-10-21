from peewee import *

db = SqliteDatabase('people.db')
db.connect()


class BaseModel(Model):

    class Meta:
        database = db
