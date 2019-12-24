from .DefaultClass import DefaultClass
from .DefaultClassBuilder import DefaultClassBuilder
from .AbstractActor import AbstractActor


class PlayerCharacter(AbstractActor):
    DEFAULT_CLASS: DefaultClass = DefaultClassBuilder("playerDefault").default_class

    def __init__(self, player_name: str, character_name: str = "", default_class: DefaultClass = DEFAULT_CLASS):
        AbstractActor.__init__(self, player_name, default_class)
        if character_name:
            self.character_name = character_name
        else:
            self.character_name = self.name
