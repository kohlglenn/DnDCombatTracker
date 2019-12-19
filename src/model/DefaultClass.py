from . import DiceRoller as Dice
import typing
from .Ability import Ability
from .Size import Size
from .StatBlock import StatBlock, get_ability_mod


# Represents a DnD monster stat block/class
class DefaultClass:
    def __init__(self, name: str, size: Size, type: str, subtype: str, alignment: str,
                 armor_class: int, hit_points: int, hit_dice: str, speed: str, stat_block: StatBlock,
                 damage_vulnerabilities: str, damage_resistances: str, condition_immunities: str,
                 senses: str, languages: str, challenge_rating: int, special_abilities: typing.List[Ability],
                 actions: typing.List[Ability], legendary_actions: typing.List[Ability]):
        self.name: str = name
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
        self.actions: typing.List[Ability] = actions
        self.legendary_actions: typing.List[Ability] = legendary_actions

    def roll_initiative(self):
        return get_ability_mod(self.stat_block.dexterity) + Dice.roll_dice(20)

    def is_dead(self) -> bool:
        return self.hit_points <= 0
