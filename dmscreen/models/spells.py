from peewee import *
from dmscreen.util.model import BaseModel


class SpellModel(Model):
    spell_id = IntegerField()


class SpellSetModel(BaseModel):
    spell_set_id = IntegerField()
    spell_id = IntegerField()


class SpellsList:
    def __init__(self):
        w, h = 5, 5
        self.spells = [[0 for x in range(w)] for y in range(h)]
