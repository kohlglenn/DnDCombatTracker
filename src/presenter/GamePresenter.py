"""Represents presenter that interacts between views and model"""
from typing import Dict, TYPE_CHECKING, Union
from model.GameModel import GameModel
from ui.views.IView import IView
import model.ClassManager as Cm
from model.Npc import Npc
from model.PlayerCharacter import PlayerCharacter
from model.Ability import Ability
from model.StatBlock import StatBlock, get_ability_mod


# TODO: Clean up import statements
# TODO: Implement stubs
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
        player_names = [x.character_name + " " + x.player_name for x in players]
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
        actor: Actor = self.game.get_actor(actor_name)
        stats = actor.get_stat_block()
        stat_block_str = [stat_block_to_str_with_mod(stat) for stat in stats]
        return " ".join(stat_block_str)

    def get_actor_special_abilities(self, actor: str):
        return []

    def get_actor_actions(self, actor: str):
        return ["An action +5 to hit"]

    def get_actor_legendary_actions(self, actor: str):
        return []

    def get_actor_class_name(self, actor):
        return ""

    def get_actor_type_subtype(self, actor):
        return ""

    def get_actor_alignment(self, actor):
        return ""

    def get_actor_armor_class(self, actor):
        return ""

    def get_actor_hp(self, actor):
        return ""

    def get_actor_speed(self, actor):
        return ""

    def get_actor_save_throws(self, actor):
        return []

    def get_actor_immunities(self, actor):
        return []

    def get_actor_resistances(self, actor):
        return []

    def get_actor_senses(self, actor):
        return []

    def get_actor_languages(self, actor):
        return []

    def get_actor_size(self, actor):
        return ""

    def update_actor_hp(self, actor, hp):
        pass


def stat_block_to_str_with_mod(stat: str):
    mod = get_ability_mod(stat)
    mod_str = str(mod) if mod < 0 else "+" + str(mod)
    return str(stat) + "(" + mod_str + ")"
