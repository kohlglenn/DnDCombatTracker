import unittest
from model.GameModel import GameModel
from model.Npc import Npc
from persistence.GameModelIO import save_game_model, load_game_model
from pickle import PickleError


class TestGameModelIO(unittest.TestCase):

    def setUp(self) -> None:
        self.game = GameModel()
        self.game.add_player_by_name("Kohl")
        self.game.add_npc(Npc("npc"))

    def test_save(self):
        try:
            save_game_model(self.game)
        except PickleError:
            self.fail("Save failed.")

    def test_save_and_load(self):
        try:
            save_game_model(self.game)
            other_game = load_game_model()
            self.assertEqual(self.game.list_players(), other_game.list_players())
        except PickleError:
            self.fail("Load failed.")


if __name__ == '__main__':
    unittest.main()
