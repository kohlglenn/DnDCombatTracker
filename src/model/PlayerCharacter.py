from model.DefaultClass import DefaultClass
from model.DefaultClassBuilder import DefaultClassBuilder


class PlayerCharacter:
    DEFAULT_CLASS: DefaultClass = DefaultClassBuilder("playerDefault").default_class

    def __init__(self, player_name: str, character_name: str = "", default_class: DefaultClass = DEFAULT_CLASS):
        self.default_class = default_class
        if character_name:
            self.character_name = character_name
        else:
            self.character_name = player_name
        self.player_name = player_name
        self.initiative = None

    def set_initiative(self, initiative: int):
        self.initiative = initiative
