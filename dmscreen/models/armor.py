from enum import Enum


class ArmorClass(Enum):
    LIGHT = 0
    MEDIUM = 1
    HEAVY = 2


class Armor:
    def __init__(self):
        self.ac = 0
        self.use_dex_mod = False
        self.dex_mod_capped = False
        self.dex_mod_max = 2
        self.armor_class = ArmorClass.LIGHT
