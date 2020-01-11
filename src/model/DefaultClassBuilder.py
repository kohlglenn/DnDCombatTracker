from model.DefaultClass import DefaultClass
from model.Ability import Ability, create_special_ability
from model.StatBlock import StatBlock, get_ability_mod
from model.Size import Size
import typing
from typing import Dict, List


# TODO: Documentation and finish fleshing out
class DefaultClassBuilder:
    def __init__(self, name):
        self.default_class = DefaultClass(name, Size.MEDIUM, "Generic", "", "any alignment",
                                          10, 10, "", "30 ft.", StatBlock(),
                                          "", "", "", "", "Common", 1, [],
                                          [], [], {})

    def set_stat_block(self, strength: int = 10, dexterity: int = 10, constitution: int = 10,
                       intelligence: int = 10, wisdom: int = 10, charisma: int = 10):
        self.default_class.stat_block.strength = strength
        self.default_class.stat_block.dexterity = dexterity
        self.default_class.stat_block.constitution = constitution
        self.default_class.stat_block.intelligence = intelligence
        self.default_class.stat_block.wisdom = wisdom
        self.default_class.stat_block.charisma = charisma

    def set_actions(self, actions: List[Ability]):
        self.default_class.actions = actions

    def add_action(self, action: Ability):
        self.default_class.actions.append(action)

    def set_armor_class(self, armor_class: int):
        self.default_class.armor_class = armor_class

    def set_hit_points(self, hp: int):
        self.default_class.max_hit_points = hp

    def get_default_class(self):
        return self.default_class


# TODO: Finish mapping dnd 5e api monster to a default class
def parse_to_default_class(cd: Dict) -> DefaultClass:
    class_name = cd["name"]
    size = Size(__get_if_exists(cd, "size", "MEDIUM").upper())
    type = __get_if_exists(cd, "type", "None")
    subtype: str = __get_if_exists(cd, "subtype", "None")
    alignment: str = __get_if_exists(cd, "alignment", "None")
    armor_class: int = __get_if_exists(cd, "armor_class", 10)
    max_hit_points: int = __get_if_exists(cd, "hit_points", 0)
    hit_dice: str = __get_if_exists(cd, "hit_dice", "None")
    speed: str = parse_str_from_dict(__get_if_exists(cd, "speed", "None"))
    stat_block: StatBlock = __get_stat_block(cd)
    damage_vulnerabilities: str = ", ".join(__get_if_exists(cd, "damage_vulnerabilities", []))
    damage_resistances: str = ", ".join(__get_if_exists(cd, "damage_resistances", []))
    damage_immunities: str = ", ".join(__get_if_exists(cd, "damage_immunities", []))
    condition_immunities: str = __get_condition_immunities(cd)
    senses: str = parse_str_from_dict(__get_if_exists(cd, "senses", {}))
    languages: str = __get_if_exists(cd, "languages", "No languages")
    challenge_rating: int = __get_if_exists(cd, "challenge_rating", 0)
    special_abilities: List[Ability] = __get_special_abilities(cd)
    actions: List[Ability] = __get_actions(cd)
    legendary_actions = __get_legendary_actions(cd)
    save_throws = parse_saving_throws_from_dict(stat_block, __get_if_exists(cd, "proficiencies", []))
    return DefaultClass(class_name, size, type, subtype, alignment, armor_class, max_hit_points, hit_dice, speed,
                        stat_block, damage_vulnerabilities, damage_resistances, damage_immunities, condition_immunities, senses,
                        languages, challenge_rating, special_abilities, actions, legendary_actions, save_throws)


def __get_legendary_actions(cd):
    try:
        return[Ability(__get_if_exists(x, "attack_bonus", None), x["desc"], x["name"],
                       __get_if_exists(x, "damage_bonus", None), __get_if_exists(x, "damage_dice", None))
               for x in cd["legendary_actions"]]
    except KeyError:
        return []


def __get_actions(cd):
    try:
        return [Ability(__get_if_exists(x, "attack_bonus", None), x["desc"], x["name"],
                        __get_if_exists(x, "damage_bonus", None), __get_if_exists(x, "damage_dice", None))
                for x in cd["actions"]]
    except KeyError:
        return []


def __get_special_abilities(cd):
    try:
        return [create_special_ability(x["name"], x["desc"]) for x in cd["special_abilities"]]
    except KeyError:
        return []


def parse_str_from_dict(my_dict: Dict) -> str:
    return " ".join([(key + " " + str(value)) for (key, value) in my_dict.items()])


def parse_saving_throws_from_dict(stat_block: StatBlock, proficiencies: List[Dict]) -> Dict[str, int]:
    save_throws = {"Str": 0, "Dex": 0, "Con": 0, "Int": 0, "Wis": 0, "Cha": 0}
    stat_block_mapping = {"Str": "strength", "Dex": "dexterity", "Con": "constitution",
                          "Int": "intelligence", "Wis": "wisdom", "Cha": "charisma"}
    stat_block_dict = vars(stat_block)
    # iterates over keys, if there is a proficiency matching the key then there is the corresponding value
    # otherwise need to get value from stat_block and convert to an ability modifier
    for (key, _) in save_throws.items():
        for prof in proficiencies:
            name = prof["name"]
            if key.upper() in name:
                save_throws[key] = prof["value"]
            else:
                save_throws[key] = get_ability_mod(stat_block_dict[stat_block_mapping[key]])
    return save_throws


def __get_if_exists(my_dict, key, default_value):
    try:
        return my_dict[key]
    except KeyError:
        return default_value


def __get_stat_block(cd):
    stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    stat_values = [__get_if_exists(cd, stat, 10) for stat in stats]
    return StatBlock(*stat_values)


def __get_condition_immunities(cd):
    try:
        return ", ".join([condition["name"] for condition in cd["condition_immunities"]])
    except KeyError:
        return []
