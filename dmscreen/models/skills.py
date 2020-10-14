

class Skills:
    def __init__(self):
        self.acrobatics = Skill()
        self.animal_handling = Skill()
        self.arcana = Skill()
        self.athletics = Skill()
        self.deception = Skill()
        self.history = Skill()
        self.insight = Skill()
        self.intimidation = Skill()
        self.investigation = Skill()
        self.medicine = Skill()
        self.nature = Skill()
        self.perception = Skill()
        self.performance = Skill()
        self.persuasion = Skill()
        self.religion = Skill()
        self.sleight_of_hand = Skill()
        self.stealth = Skill()
        self.survival = Skill()


class Skill:
    def __init__(self):
        self._proficient = False
        self._modifier = 0

    @property
    def proficient(self):
        return self._proficient

    @proficient.setter
    def proficient(self, proficient):
        self._proficient = proficient

    @property
    def modifier(self):
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        self._modifier = modifier
