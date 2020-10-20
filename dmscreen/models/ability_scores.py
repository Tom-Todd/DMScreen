from enum import Enum
from dmscreen.util.util import calculate_modifier

class ScoreType(Enum):
    STRENGTH = 0,
    DEXTERITY = 1,
    CONSTITUTION = 2,
    INTELLIGENCE = 3,
    WISDOM = 4,
    CHARISMA = 5,

class AbilityScores:
    def __init__(self):
        self.scores = [AbilityScore() for i in range(6)]


class AbilityScore:
    def __init__(self):
        self._score = 0
        self._modifier = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
        self._modifier = calculate_modifier(score)

    @property
    def modifier(self):
        return self._modifier
