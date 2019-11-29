from model.DefaultClass import DefaultClass, Size, StatBlock, Ability
import typing


# TODO: Documentation and finish fleshing out
class DefaultClassBuilder:
    def __init__(self, name):
        self.default_class = DefaultClass(name, Size.MEDIUM, "Generic", "", "any alignment",
                                          10, 10, "", "30 ft.", StatBlock(),
                                          "", "", "", "", "Common", 1, [],
                                          [], [])

    def set_stat_block(self, strength: int = 10, dexterity: int = 10, constitution: int = 10,
                       intelligence: int = 10, wisdom: int = 10, charisma: int = 10):
        self.default_class.stat_block.strength = strength
        self.default_class.stat_block.dexterity = dexterity
        self.default_class.stat_block.constitution = constitution
        self.default_class.stat_block.intelligence = intelligence
        self.default_class.stat_block.wisdom = wisdom
        self.default_class.stat_block.charisma = charisma

    def set_actions(self, actions: typing.List[Ability]):
        self.default_class.actions = actions

    def add_action(self, action: Ability):
        self.default_class.actions.append(action)

    def set_armor_class(self, armor_class: int):
        self.default_class.armor_class = armor_class

    def set_hit_points(self, hp: int):
        self.default_class.hit_points = hp
