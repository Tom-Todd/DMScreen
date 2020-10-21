from enum import Enum
from peewee import *


class ArmorClass(Enum):
    LIGHT = 0
    MEDIUM = 1
    HEAVY = 2


class ArmorModel(Model):
    armor_id = IntegerField()
    ac = IntegerField()
    use_dex_mod = BooleanField()
    dex_mod_max = IntegerField()
    armor_class = IntegerField()


class Armor(Model):
    pass
