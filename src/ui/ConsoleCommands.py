from abc import ABC, abstractmethod
from model.GameState import GameState
from model.PlayerCharacter import PlayerCharacter


def get_all_commands():
    return {"h": ConsoleHelp(), "p": ConsoleAddPlayer()}


class Command(ABC):
    @abstractmethod
    def execute(self, game: GameState):
        pass

    @abstractmethod
    def undo(self):
        pass


class ConsoleHelp(Command):
    def execute(self, game: GameState):
        print("To add a player type p")
        print("To exit type e")
        print("To undo type u")

    def undo(self):
        pass


class ConsoleAddPlayer(Command):
    lastAdded: PlayerCharacter
    game: GameState

    def execute(self, game: GameState):
        name = input("Type a player name: ")
        player = PlayerCharacter(name)
        game.add_player(player)
        self.lastAdded = player
        self.game = game

    def undo(self):
        self.game.remove_player(self.lastAdded)


class ConsoleAddNpc(Command):
    lastAdded: Npc
    game: GameState

    def execute(self, game):
        npc = input("Type a player name: ")
        self.lastAdded = Npc(npc)
        self.game = game
        self.game.add_npc(self.lastAdded)

    def undo(self):
        self.game.remove_mook(self.lastAdded)