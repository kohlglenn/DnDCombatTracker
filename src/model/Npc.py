from model.DefaultClass import DefaultClass
from model.DefaultClassBuilder import DefaultClassBuilder
from .Actor import Actor


class Npc(Actor):
    DEFAULT_CLASS: DefaultClass = DefaultClassBuilder("default_name").default_class

    def __init__(self,  name: str, default_class: DefaultClass = DEFAULT_CLASS):
        self.default_class = default_class
        self.name = name
        self.initiative = None

    def set_initiative(self, initiative: int):
        self.initiative = initiative

    def roll_initiative(self):
        self.initiative = self.default_class.roll_initiative()

    def get_stat_block(self):
        return self.default_class.stat_block
