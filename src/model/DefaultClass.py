from . import DiceRoller as Dice
import typing
from typing import Dict, List
from .Ability import Ability
from .Size import Size
from .StatBlock import StatBlock, get_ability_mod
import math


# Represents a DnD monster stat block/class
class DefaultClass:
    def __init__(self, class_name: str, size: Size, type: str, subtype: str, alignment: str,
                 armor_class: int, max_hit_points: int, hit_dice: str, speed: str, stat_block: StatBlock,
                 damage_vulnerabilities: str, damage_resistances: str, damage_immunities: str,
                 condition_immunities: str, senses: str, languages: str, challenge_rating: int,
                 special_abilities: List[Ability], actions: List[Ability], legendary_actions: List[Ability],
                 save_throws: Dict[str, int]):
        self.class_name: str = class_name
        self.size: Size = size
        self.type: str = type
        self.subtype: str = subtype
        self.alignment: str = alignment
        self.armor_class: int = armor_class
        self.max_hit_points: int = max_hit_points
        self.hit_dice: str = hit_dice
        self.speed: str = speed
        self.stat_block: StatBlock = stat_block
        self.damage_vulnerabilities: str = damage_vulnerabilities
        self.damage_resistances: str = damage_resistances
        self.damage_immunities: str = damage_immunities
        self.condition_immunities: str = condition_immunities
        self.senses: str = senses
        self.languages: str = languages
        self.challenge_rating: int = challenge_rating
        self.special_abilities: typing.List[Ability] = special_abilities
        self.actions: typing.List[Ability] = actions
        self.legendary_actions: typing.List[Ability] = legendary_actions
        self.save_throws = save_throws  # e.g. {"dexterity_save": 8}

    def roll_initiative(self):
        return get_ability_mod(self.stat_block.dexterity) + Dice.roll_dice(20)

    def is_dead(self) -> bool:
        return self.max_hit_points <= 0

    # Accurately maps CR 0-30 to proficiency bonus +2-+9
    def get_proficiency_mod(self) -> int:
        if 1 < self.challenge_rating <= 30:
            return 2 + math.floor((self.challenge_rating - 1) / 4)
        else:
            return 2 if self.challenge_rating < 1 else 9
