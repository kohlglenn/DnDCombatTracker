from enum import unique, Enum


@unique
class Proficiencies(Enum):
    MEDICINE = "MEDICINE"
    DEX_SAVE = "DEXTERITY_SAVE"
    SIMPLE_WEAPON = "SIMPLE_WEAPON"