from src.model.PlayerCharacter import PlayerCharacter
from src.model.Npc import Npc
import typing
from typing import Optional, Union, List, Callable
from .AbstractActor import AbstractActor
"""Contains information about the GameState such as characters in the game"""


# TODO: Does this really need to know about the combat status? I think the only reason I need it is for rolling npc
# TODO: init but can't that be handled by the presenter and this will just be the data structure?
# Singleton pattern in Python uses the constructor and a private constructor anyways so can just update later on
class GameModel:
    players: List[PlayerCharacter]
    npcs: List[Npc]
    combat: bool

    def __init__(self):
        self.players = []
        self.npcs = []
        self.combat = False

    def add_player(self, pc: PlayerCharacter):
        self.players.append(pc)

    def add_npc(self, npc: Npc):
        self.npcs.append(npc)

    """Throws ValueError if npc is not found"""
    def remove_npc(self, npc: Npc):
        self.npcs.remove(npc)

    def roll_all_npc_initiative(self):
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

    def start_combat(self):
        self.combat = True

    def add_player_by_name(self, pc: str):
        self.players.append(PlayerCharacter(pc))

    def get_actor(self, actor_name: str):
        actors: List[AbstractActor] = [*self.npcs, *self.players]
        idx = find_in_list(actors, lambda x: is_player_or_npc(x, actor_name))
        if idx != -1:
            return actors[idx]
        else:
            return PlayerCharacter("player_name")
            # TODO raise ValueError("Not found.")


def is_player_or_npc(actor: AbstractActor, name: str):
    return actor.name == name


def find_in_list(my_list: List, predicate: Callable) -> int:
    for i in range(0, len(my_list)):
        if predicate(my_list[i]):
            return i
    return -1
