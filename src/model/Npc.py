from model.DefaultClass import DefaultClass
from model.DefaultClassBuilder import DefaultClassBuilder


class Npc:
    DEFAULT_CLASS: DefaultClass = DefaultClassBuilder("default_name")

    def __init__(self,  name: str, default_class: DefaultClass = DEFAULT_CLASS):
        self.default_class = default_class
        self.name = name
        self.initiative = None

    def set_initiative(self, initiative: int):
        self.initiative = initiative

    def roll_initiative(self):
        self.initiative = self.default_class.roll_initiative()
