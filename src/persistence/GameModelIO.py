from pathlib import Path
import pickle
from model.GameModel import GameModel

cwd = Path.cwd().parent
data_folder = cwd / "data"
game_model_file_path = data_folder / "game_models.pickle"


# TODO: Be able to save/load multiple game models (to pre-make battles or save a template with PCs and stuff like that)
def save_game_model(game: GameModel):
    try:
        file = open(game_model_file_path, 'wb')
    except FileNotFoundError:
        file = open(game_model_file_path, 'xb')
    pickle.dump(game, file, protocol=pickle.HIGHEST_PROTOCOL)
    file.close()


def load_game_model() -> GameModel:
    with open(game_model_file_path, 'rb') as file:
        game = pickle.load(file)
        file.close()
    return game
