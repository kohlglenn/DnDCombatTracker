from . import DiceRoller as Dice
import typing
from enum import Enum, unique
import math

@unique
class Size(Enum):
    TINY = "TINY"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    HUGE = "HUGE"
    GARGANTUAN = "GARGANTUAN"


# TODO: Finish enum
@unique
class Proficiencies(Enum):
    MEDICINE = "MEDICINE"
    DEX_SAVE = "DEXTERITY_SAVE"
    SIMPLE_WEAPON = "SIMPLE_WEAPON"


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


class Ability:
    attack_bonus: int
    desc: str
    name: str
    damage_bonus: int # can be NULL
    damage_dice: str # can be NULL


# Represents a class
class DefaultClass:
    def __init__(self, name: str, size: Size, type: str, subtype: str, alignment: str,
                 armor_class: int, hit_points: int, hit_dice: str, speed: str, stat_block: StatBlock,
                 damage_vulnerabilities: str, damage_resistances: str, condition_immunities: str,
                 senses: str, languages: str, challenge_rating: int, special_abilities: typing.List[Ability],
                 actions: typing.List[Ability], legendary_actions: typing.List[Ability]):
        self.name: str  = name
        self.size: Size = size
        self.type: str = type
        self.subtype: str = subtype
        self.alignment: str = alignment
        self.armor_class: int = armor_class
        self.hit_points: int = hit_points
        self.hit_dice: str = hit_dice
        self.speed: str = speed
        self.stat_block: StatBlock = stat_block
        self.damage_vulnerabilities: str = damage_vulnerabilities
        self.damage_resistances: str = damage_resistances
        self.condition_immunities: str = condition_immunities
        self.senses: str = senses
        self.languages: str = languages
        self.challenge_rating: int = challenge_rating
        self.special_abilities: typing.List[Ability] = special_abilities
        self.actions: List[Ability] = actions
        self.legendary_actions: typing.List[Ability] = legendary_actions


    def roll_initiative(self):
        return get_ability_mod(self.stat_block.dexterity). + Dice.roll_dice(20)

    def is_dead(self) -> bool:
        return self.hit_points <= 0


