import math


class StatBlock:
    def __init__(self, strength: int = 10, dexterity: int = 10, constitution: int = 10,
                 intelligence: int = 10, wisdom: int = 10, charisma: int = 10):
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitution: int = constitution
        self.intelligence: int = intelligence
        self.wisdom: int = wisdom
        self.charisma: int = charisma


def get_ability_mod(ability_score):
    return math.floor((ability_score - 10) / 2)