"""Represents presenter that interacts between views and model"""
from typing import Dict
from ui.views.CreateNpcView import CreateNpcView
from model.GameModel import GameModel

class GamePresenter:
    def __init__(self):
        self.npc_classes = ["Goblin", "Bugbear", "Lich"]
        self.game = GameModel()

    def get_npc_classes(self):
        return self.npc_classes

    def add_npcs_from_view(self, npc_dict: Dict, view: CreateNpcView):
        print("Not implemented.")
