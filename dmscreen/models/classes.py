# pylint: disable=too-many-instance-attributes
# number of attributes is reasonable in this case
from peewee import *


class Class(Model):
    class_id = IntegerField()
    name = CharField()
    spell_casting_ability = IntegerField()


class ClassSet(Model):
    set_id = IntegerField()
    class_id = IntegerField()
