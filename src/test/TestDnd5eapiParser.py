import unittest
from model.GameModel import GameModel
from model.Npc import Npc
from persistence.GameModelIO import save_game_model, load_game_model
from pickle import PickleError
from parsers.Dnd5eapiParser import get_all_monsters
import asyncio
from model.DefaultClass import DefaultClass
from model.DefaultClassBuilder import DefaultClassBuilder


class TestDnd5eapiParser(unittest.TestCase):

    def test_for_adult_green_dragon(self):
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(get_all_monsters())
        values = loop.run_until_complete(future)
        test_val = __create_adult_green_dragon()
        if test_val not in values:
            self.fail("There was an error parsing")


# Creates an Adult Green Dragon as per the spec provided on http://www.dnd5eapi.co/api/monsters/adult-green-dragon/
# retrieved Jan 11, 2020
# TODO: Finish implementation
def __create_adult_green_dragon() -> DefaultClass:
    agd = DefaultClassBuilder("Adult Green Dragon")
    return agd.get_default_class()
