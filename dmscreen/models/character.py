# pylint: disable=too-many-instance-attributes
# number of attributes is reasonable in this case
import math
from enum import Enum
from dmscreen.models.ability_scores import AbilityScores
from dmscreen.models.ability_scores import ScoreType
from dmscreen.models.skills import Skills
from dmscreen.models.classes import Class
from dmscreen.models.race import Race
from dmscreen.models.dice import RollType
from dmscreen.models.armor import Armor


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


class HitPoints:
    def __init__(self):
        self.current = 0
        self.max = 0
        self.die = RollType()


class Character:
    def __init__(self):
        self._name = ""
        self.classes = [Class]
        self.race = Race()
        self.level = 1
        self.xp = 0
        self.armor = Armor()
        self.ability_scores = AbilityScores()
        self.skills = Skills()
        self.hit_points = HitPoints()
        self.is_player_character = False
        self.alignment = Alignment.NEUTRAL
        self.languages = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def get_spell_save_dc(self, class_id):
        spell_score = self.ability_scores.scores[self.classes[class_id].spell_casting_ability]
        return 8 + spell_score.modifier + self.proficiency_bonus

    @property
    def proficiency_bonus(self):
        return math.ceil(1 + 0.25 * self.level)

    @property
    def passive_wisdom(self):
        return 10 + self.ability_scores.scores[ScoreType.WISDOM].modifier

    @property
    def speed(self):
        return self.race.speed

    @property
    def ac(self):
        if self.armor.use_dex_mod:
            mod = min(self.ability_scores.scores[ScoreType.DEXTERITY], 2) if \
                self.armor.dex_mod_capped else \
                self.ability_scores.scores[ScoreType.DEXTERITY]
            return self.armor.ac + mod
        return self.armor.ac

    @property
    def know_languages(self):
        """Combine and return languages known by character"""
        return sorted(list(set(self.race.languages) | set(self.languages)))
