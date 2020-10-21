# pylint: disable=too-many-instance-attributes
# number of attributes is reasonable in this case
from dmscreen.models.ability_scores import ScoreType


class Class:
    def __init__(self):
        self._id = 0
        self._name = ""
        self.spell_casting_ability = ScoreType.CHARISMA

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id_):
        self._id = id_
