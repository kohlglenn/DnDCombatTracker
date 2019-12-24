"""Represents presenter that interacts between views and model"""
from typing import Dict, TYPE_CHECKING, Union
from model.GameModel import GameModel
from ui.views.IView import IView
import model.ClassManager as Cm
from model.Npc import Npc
from model.PlayerCharacter import PlayerCharacter
from model.Ability import Ability
from model.StatBlock import StatBlock, get_ability_mod
from model.AbstractActor import AbstractActor


class GamePresenter:
    def __init__(self):
        # TODO: Hook up to some kind of database
        self.npc_classes = ["Goblin", "Bugbear", "Lich"]
        self.player_classes = ["Paladin", "Rogue"]
        self.game = GameModel()

    def get_npc_classes(self):
        return self.npc_classes

    def add_npcs_from_view(self, npc_dict: Dict):
        for (_, npc) in npc_dict.items():
            name = npc["name"]
            npc_class_name = npc["class"]
            npc_class = Cm.get_default_class(npc_class_name)
            self.game.add_npc(Npc(name, npc_class))

    def get_player_classes(self):
        return self.player_classes

    def add_players_from_view(self, player_dict: Dict):
        for (_, player) in player_dict.items():
            name = player["name"]
            player_class_name = player["class"]
            player_class = Cm.get_default_class(player_class_name)
            self.game.add_player(PlayerCharacter(name, player_class))

    # Returns list of names in order of *players, *npcs
    def get_actor_list(self):
        players = self.game.players
        npcs = self.game.npcs
        player_names = [x.character_name + " " + x.name for x in players]
        npc_names = [x.name for x in npcs]
        return [*player_names, *npc_names]

    # Returns list of initiative in same order as get_actor_list
    def get_initiative_list(self):
        players = self.game.players
        npcs = self.game.npcs
        player_init = [x.initiative for x in players]
        npc_init = [x.initiative for x in npcs]
        return [*player_init, *npc_init]

    def get_stat_block_with_mods(self, actor_name: str):
        actor: AbstractActor = self.game.get_actor(actor_name)
        stats = actor.get_stat_block_values()
        stat_block_str = [stat_block_to_str_with_mod(stat) for stat in stats]
        return stat_block_str

    def get_actor_special_abilities(self, actor_name: str):
        actor: AbstractActor = self.game.get_actor(actor_name)
        abilities = actor.get_special_abilities()
        return [str(a) for a in abilities]

    def get_actor_actions(self, actor_name: str):
        actor: AbstractActor = self.game.get_actor(actor_name)
        actions = actor.get_actions()
        return [str(a) for a in actions]

    def get_actor_legendary_actions(self, actor_name: str):
        actor: AbstractActor = self.game.get_actor(actor_name)
        actions = actor.get_legendary_actions()
        return [str(a) for a in actions]

    def get_actor_class_name(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        name = actor.get_class_name()
        return name

    def get_actor_type_subtype(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        type = actor.get_type()
        subtype = actor.get_subtype()
        return str(type) + " " + str(subtype)

    def get_actor_alignment(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        type = actor.get_type()
        subtype = actor.get_subtype()
        return str(type) + " " + str(subtype)

    def get_actor_armor_class(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        ac = actor.get_armor_class()
        return str(ac)

    def get_actor_hp(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        hp = actor.get_hp()
        return str(hp)

    def get_actor_speed(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        speed = actor.get_speed()
        return speed

    def get_actor_save_throws(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        # Return in a dict with format {Str: 6, Wis: -2, ...}
        save_throws = actor.get_save_throws()
        ret_val = []
        for (stat, mod) in save_throws.items():
            mod_str = str(mod) if mod < 0 else "+" + str(mod)
            ret_val.append(stat + " " + mod_str)
        return ", ".join(ret_val)

    def get_actor_immunities(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        immunities = actor.get_immunities()
        return immunities

    def get_actor_resistances(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        resistances = actor.get_resistances()
        return resistances

    def get_actor_vulnerabilities(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        vulnerabilities = actor.get_vulnerabilities()
        return vulnerabilities

    def get_actor_senses(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        senses = actor.get_senses()
        return senses

    def get_actor_languages(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        languages = actor.get_languages()
        return languages

    def get_actor_size(self, actor_name):
        actor: AbstractActor = self.game.get_actor(actor_name)
        size = actor.get_size()
        return str(size)

    def update_actor_hp(self, actor_name, hp):
        actor: AbstractActor = self.game.get_actor(actor_name)
        new_hp = actor.get_hp() + hp
        actor.set_hp(new_hp)

    def set_actor_hp(self, actor_name, hp):
        actor: AbstractActor = self.game.get_actor(actor_name)
        actor.set_hp(hp)


def stat_block_to_str_with_mod(stat: str):
    mod = get_ability_mod(stat)
    mod_str = str(mod) if mod < 0 else "+" + str(mod)
    return str(stat) + "(" + mod_str + ")"
