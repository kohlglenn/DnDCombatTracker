from .DefaultClass import DefaultClass
from .DefaultClassBuilder import DefaultClassBuilder
from .Actor import Actor


class PlayerCharacter(Actor):
    DEFAULT_CLASS: DefaultClass = DefaultClassBuilder("playerDefault").default_class

    def __init__(self, player_name: str, character_name: str = "", default_class: DefaultClass = DEFAULT_CLASS):
        self.default_class = default_class
        if character_name:
            self.character_name = character_name
        else:
            self.character_name = player_name
        self.player_name = player_name
        self.initiative = None

    def get_stat_block(self):
        return self.default_class.stat_block

    def set_initiative(self, initiative: int):
        self.initiative = initiative
