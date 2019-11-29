from src.model.GameState import GameState as Game
from ui.ConsoleCommands import get_all_commands, Command
import typing


class ConsoleUI:
    game: Game
    commands: typing.Dict[str, Command]
    commandsExecuted: typing.List[Command]

    def __init__(self):
        self.game = Game()
        self.commands = get_all_commands()
        self.commandsExecuted = []

    def start(self):
        print("Starting game:\n")
        while True:
            command = input("Please enter a command, for help type \'h\': ").lower().strip()
            if command == "e":
                break
            elif command == "u":
                if len(self.commandsExecuted) > 0:
                    self.commandsExecuted.pop().undo()
            elif command in self.commands:
                to_execute = self.commands[command]
                to_execute.execute(self.game)
                self.commandsExecuted.append(to_execute)
            else:
                print("Invalid command.\n")


main = ConsoleUI()
main.start()
