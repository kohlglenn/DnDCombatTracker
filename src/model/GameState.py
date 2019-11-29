from src.model.PlayerCharacter import PlayerCharacter
from src.model.DefaultClass import DefaultClass
from src.model.Npc import Npc
import typing
from typing import Optional


class GameState:
    players: typing.List[PlayerCharacter]
    npcs: typing.List[Npc]

    def __init__(self):
        self.players = []
        self.npcs = []

    def add_player(self, pc: PlayerCharacter):
        self.players.append(pc)

    def add_player_by_name(self, pc: str):
        self.players.append(PlayerCharacter(pc))

    def add_npc(self, npc: Npc):
        self.npcs.append(npc)

    def roll_npc_initiative(self):
        for npc in self.npcs:
            npc.roll_initiative()

    def list_players(self) -> typing.List[str]:
        return [(lambda x: x.name)(x) for x in self.players]

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

    def remove_player_by_name(self, pc: str) -> Optional[PlayerCharacter]:
        players_list = self.list_players()
        if pc in players_list:
            index = players_list.index(pc)
            return self.players.pop(index)

    def remove_player(self, pc: PlayerCharacter) -> Optional[PlayerCharacter]:
        if pc in self.list_players():
            self.players.remove(pc)
            return pc
