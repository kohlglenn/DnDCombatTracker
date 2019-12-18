"""Represents presenter that interacts between views and model"""
from typing import Dict, TYPE_CHECKING
if TYPE_CHECKING:
    from ui.views.CreateNpcView import CreateNpcView
from model.GameModel import GameModel
from ui.views.IView import IView


class GamePresenter:
    def __init__(self):
        self.npc_classes = ["Goblin", "Bugbear", "Lich"]
        self.player_classes = ["Paladin", "Rogue"]
        self.game = GameModel()

    def get_npc_classes(self):
        return self.npc_classes

    def add_npcs_from_view(self, npc_dict: Dict, view: IView):
        print("Not implemented.")
        # view.update()

    def get_player_classes(self):
        return self.player_classes

    def add_players_from_view(self, npc_dict: Dict, view: IView):
        print("Not implemented.")
        # view.update()

    # Returns list of names in order of *players, *npcs
    def get_actor_list(self):
        """
        players = self.game.players
        npcs = self.game.npcs
        player_names = [x.character_name + " " + x.player_name for x in players]
        npc_names = [x.name for x in npcs]

        return [*player_names, *npc_names]"""
        return ["Kohl", "Goblin"]

    # Returns list of initiative in same order as get_actor_list
    def get_initiative_list(self):
        """players = self.game.players
        npcs = self.game.npcs
        player_init = [x.initiative for x in players]
        npc_init = [x.initiative for x in npcs]

        return [*player_init, *npc_init]"""
        return [10, 20]

    def get_stat_block_with_mods(self, actor: str):
        return ["10 (0)", "10 (0)", "10 (0)", "10 (0)", "10 (0)", "10 (0)"]
