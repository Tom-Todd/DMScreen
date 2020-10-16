from dmscreen.util.util import calculate_modifier


class AbilityScores:
    def __init__(self):
        self.strength = AbilityScore()
        self.dexterity = AbilityScore()
        self.constitution = AbilityScore()
        self.intelligence = AbilityScore()
        self.wisdom = AbilityScore()
        self.charisma = AbilityScore()


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
