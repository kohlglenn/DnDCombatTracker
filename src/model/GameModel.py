from src.model.PlayerCharacter import PlayerCharacter
from src.model.DefaultClass import DefaultClass
from src.model.Npc import Npc
import typing
from typing import Optional, Union, List

Character = Union[PlayerCharacter, Npc]


class GameModel:
    players: typing.List[PlayerCharacter]
    npcs: typing.List[Npc]
    combat_list: typing.List[Character]
    current_turn: int

    def __init__(self):
        self.players = []
        self.npcs = []

    def add_player(self, pc: PlayerCharacter):
        self.players.append(pc)

    def add_player_by_name(self, pc: str):
        self.players.append(PlayerCharacter(pc))

    def add_npc(self, npc: Npc):
        self.npcs.append(npc)

    """Throws ValueError if npc is not found"""
    def remove_npc(self, npc: Npc):
        self.npcs.remove(npc)

    def roll_npc_initiative(self):
        for npc in self.npcs:
            npc.roll_initiative()

    def list_players(self) -> typing.List[str]:
        return [(lambda x: x.player_name)(x) for x in self.players]

    def find_player_index(self, name: str):
        arr = self.list_players()
        if name in arr:
            return arr.index(name)
        else:
            return -1

    def set_player_initiative(self, name: str, init: int):
        idx = self.find_player_index(name)
        if idx != -1:
            self.players[idx].set_initiative(init)

    def get_player_initiative(self, name: str) -> int:
        idx = self.find_player_index(name)
        if idx != -1:
            return self.players[idx].initiative
        return -1

    def remove_player_by_name(self, pc: str) -> Optional[PlayerCharacter]:
        players_list = self.list_players()
        if pc in players_list:
            index = players_list.index(pc)
            return self.players.pop(index)

    def remove_player(self, pc: PlayerCharacter) -> Optional[PlayerCharacter]:
        if pc in self.list_players():
            self.players.remove(pc)
            return pc

    # Must start combat before using combat functions
    # TODO: Exception handling or setting combat flag?
    def start_combat(self):
        self.roll_npc_initiative()
        self.combat_list = [*self.players, *self.npcs]
        self.combat_list.sort(key=lambda char: char.initiative, reverse=True)
        self.current_turn = 0

    def get_combat_order(self):
        return self.combat_list

    def get_current_actor(self):
        return self.combat_list[self.current_turn]

    def get_next_actor(self):
        idx = self.current_turn + 1 if self.current_turn <= len(self.combat_list) - 2 else 0
        return self.combat_list[idx]

    def next_actor(self):
        self.current_turn = self.current_turn + 1 if self.current_turn <= len(self.combat_list) - 2 else 0
