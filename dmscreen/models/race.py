from peewee import *


class RaceModel(Model):
    name = CharField()
    speed = IntegerField()


class Race:
    def __init__(self):
        self.name = ""
        self.speed = 0
        self.languages = []
        self.ability_score_modifiers = []
