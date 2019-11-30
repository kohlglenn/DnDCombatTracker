from model.GameModel import GameModel
from src.model.PlayerCharacter import PlayerCharacter
from src.model.DefaultClass import DefaultClass
from src.model.Npc import Npc
import typing
from typing import Optional, Union, List


Character = Union[PlayerCharacter, Npc]


class CombatWrapper:
    game: GameModel
    current_turn: int
    combat_list: List[Character]

    def __init__(self, game: GameModel):
        self.game = game
        self.game.roll_all_npc_initiative()
        self.combat_list = [*self.game.players, *self.game.npcs]
        self.combat_list.sort(key=lambda char: char.initiative, reverse=True)
        self.current_turn = 0

    def get_combat_order(self):
        order = self.combat_list
        idx = self.current_turn
        if idx != 0:
            return [*order[idx:len(order)], *order[0:idx]]
        else:
            return order

    def get_current_actor(self):
        return self.combat_list[self.current_turn]

    def get_next_actor(self):
        idx = self.current_turn + 1 if self.current_turn <= len(self.combat_list) - 2 else 0
        return self.combat_list[idx]

    def next_actor(self):
        self.current_turn = self.current_turn + 1 if self.current_turn <= len(self.combat_list) - 2 else 0
