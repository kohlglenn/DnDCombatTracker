from abc import ABC, abstractmethod
from model.DefaultClass import DefaultClass
from model.DefaultClassBuilder import DefaultClassBuilder
from . import DiceRoller as Dice
from .StatBlock import StatBlock, get_ability_mod
import typing
from typing import List, Dict
from .Ability import Ability
# TODO: add implementation for all of the methods in GamePresenter.
#  Maybe consider decoupling by IActor -> AbstractActor -> [PC, Npc] ?


class AbstractActor(ABC):
    DEFAULT_CLASS: DefaultClass = DefaultClassBuilder("playerDefault").default_class
    STRENGTH = 1
    DEXTERITY = 2

    def __init__(self, name: str, default_class: DefaultClass = DEFAULT_CLASS):
        self.default_class = default_class
        self.initiative = None
        self.name = name
        self.current_hp = self.default_class.max_hit_points

    def set_initiative(self, initiative: int):
        self.initiative = initiative

    def roll_initiative(self):
        self.initiative = get_ability_mod(self.get_stat_block().dexterity) + Dice.roll_dice(20)

    def get_stat_block(self) -> StatBlock:
        return self.default_class.stat_block

    def get_stat_block_values(self) -> List[int]:
        return self.default_class.stat_block.get_stat_block_values()

    def get_special_abilities(self) -> List[Ability]:
        return self.default_class.special_abilities

    def get_actions(self):
        return self.default_class.actions

    def get_legendary_actions(self):
        return self.default_class.legendary_actions

    def get_class_name(self):
        return self.default_class.class_name

    def get_type(self):
        return self.default_class.type

    def get_subtype(self):
        return self.default_class.subtype

    def get_armor_class(self):
        return self.default_class.armor_class

    def get_hp(self):
        return self.current_hp

    def get_speed(self):
        return self.default_class.speed

    def get_save_throws(self) -> Dict[str, int]:
        return self.default_class.save_throws

    def get_immunities(self):
        return self.default_class.condition_immunities

    def get_resistances(self):
        return self.default_class.damage_resistances

    def get_vulnerabilities(self):
        return self.default_class.damage_vulnerabilities

    def get_senses(self):
        return self.default_class.senses

    def get_languages(self):
        return self.default_class.languages

    def get_size(self):
        return self.default_class.size

    def set_hp(self, hp: int):
        self.current_hp = hp

