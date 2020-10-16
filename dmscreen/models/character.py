from enum import Enum
from dmscreen.models.ability_scores import AbilityScores
from dmscreen.models.skills import Skills
from dmscreen.models.classes import Class


class Alignment(Enum):
    LAWFUL_GOOD = 0
    NEUTRAL_GOOD = 1
    CHAOTIC_GOOD = 2
    LAWFUL_NEUTRAL = 3
    NEUTRAL = 4
    CHAOTIC_NEUTRAL = 5
    LAWFUL_EVIL = 6
    NEUTRAL_EVIL = 7
    CHAOTIC_EVIL = 8


class Character:
    def __init__(self):
        self._name = ""
        self.classes = [Class]
        self.level = 1
        self.xp = 0
        self.ac = 0
        self.speed = 0
        self.ability_score = AbilityScores()
        self.skills = Skills()
        self.hit_points = 0
        self.hit_points_max = 0
        self.proficiency_bonus = 0
        self.passive_wisdom = 0
        self.is_player_character = False
        self.alignment = Alignment.NEUTRAL

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
