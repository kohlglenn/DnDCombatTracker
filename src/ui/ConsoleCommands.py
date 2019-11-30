from abc import ABC, abstractmethod
from model.GameModel import GameModel, Character
from model.PlayerCharacter import PlayerCharacter
from model.Npc import Npc


def get_all_commands():
    return {"h": ConsoleHelp(), "p": ConsoleAddPlayer(), "a": ConsoleAddNpc(), "s": StartCombat(),
            "l": ConsoleGetActors(), "c": ConsoleGetCurrentActor(), "n": NextActor(), "sp": ConsoleSetPlayerInitiative()}


class Command(ABC):
    @abstractmethod
    def execute(self, **kwargs):
        pass

    @abstractmethod
    def undo(self):
        pass


class ConsoleHelp(Command):
    def execute(self, game: GameModel):
        print("To exit type e")
        print("To undo type u")
        print("To add a player type p")
        print("To add a npc type a")
        print("To set a players initiative type sp")
        print("To start combat type s")
        print("***AFTER STARTING COMBAT***")
        print("To list npcs and players type l")
        print("To list current actors type c")
        print("To advance 1 turn press n")

    def undo(self):
        pass


class ConsoleAddPlayer(Command):
    lastAdded: PlayerCharacter
    game: GameModel

    def execute(self, game: GameModel):
        name = input("Type a player name: ")
        player = PlayerCharacter(name)
        game.add_player(player)
        self.lastAdded = player
        self.game = game

    def undo(self):
        self.game.remove_player(self.lastAdded)


class ConsoleAddNpc(Command):
    lastAdded: Npc
    game: GameModel

    def execute(self, game):
        npc = input("Type a player name: ")
        self.lastAdded = Npc(npc)
        self.game = game
        self.game.add_npc(self.lastAdded)

    def undo(self):
        try:
            self.game.remove_npc(self.lastAdded)
        except ValueError:
            pass # If value error occurs, npc was already removed


class StartCombat(Command):
    game: GameModel

    def execute(self, game: GameModel):
        self.game = game
        game.start_combat()

    def undo(self):
        pass


class ConsoleGetActors(Command):
    game: GameModel

    def execute(self, game: GameModel):
        self.game = game
        order = game.get_combat_order()
        print("NAME     INIT")
        for char in order:
            print("%s       %d" % (get_name(char), char.initiative))

    def undo(self):
        pass


class ConsoleGetCurrentActor(Command):
    game: GameModel

    def execute(self, game: GameModel):
        self.game = game
        print("Currently up: %s" % (get_name(game.get_current_actor())))
        print("On Deck: %s" % (get_name(game.get_next_actor())))

    def undo(self):
        pass


class NextActor(Command):
    game: GameModel

    def execute(self, game: GameModel):
        self.game = game
        game.next_actor()

    def undo(self):
        pass


class ConsoleSetPlayerInitiative(Command):
    game: GameModel
    player: str
    prev_init: int

    def execute(self, game: GameModel):
        self.game = game
        print("Which player?")
        idx = 1
        player_list = game.list_players()
        self.player = "None"
        for player in player_list:
            print("%d. %s" % (idx, player))
            idx += 1
        selection = input("Type player index: ")
        selection = int(selection) if is_int(selection) else -1
        if 0 < selection <= len(player_list):
            curr_init = input("Type initiative: ")
            curr_init = int(curr_init) if is_int(curr_init) else -1
            if curr_init != -1:
                self.player = player_list[selection-1]
                self.prev_init = game.get_player_initiative(self.player)
                game.set_player_initiative(self.player,curr_init)
            else:
                print("Invalid initiative")
        else:
            print("Invalid index")

    def undo(self):
        if self.player != "None" and self.prev_init != -1:
            self.game.set_player_initiative(self.player,self.prev_init)


# TODO: Move into a couple util classes
def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def get_name(char: Character) -> str:
    if char.__class__ == PlayerCharacter:
        return char.player_name + " " + char.character_name
    else:
        return char.name
