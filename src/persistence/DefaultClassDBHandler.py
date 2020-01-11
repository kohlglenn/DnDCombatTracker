from pathlib import Path
import pickle
from typing import List
import os

cwd = Path(os.path.dirname(os.path.realpath(__file__))).parent
data_folder = cwd / "data"
db_file_path = data_folder / "default_class_db.pickle"


# Set up using the singleton pattern found here
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
class DefaultClassDBHandler(object):
    __instance = None

    def __new__(cls):
        if DefaultClassDBHandler.__instance is None:
            DefaultClassDBHandler.__instance = object.__new__(cls)
        with open(db_file_path, 'rb') as file:
            DefaultClassDBHandler.__instance.__class_list = pickle.load(file)
            file.close()
        return DefaultClassDBHandler.__instance

    def insert_default_class(self, default_class):
        if default_class not in self.__class_list:
            self.__class_list.append(default_class)

    # NOTE: Assumes list is not mutated
    def get_all_default_classes(self) -> List:
        return self.__class_list

    def save(self):
        with open(db_file_path, 'wb') as file:
            pickle.dump(self.__class_list, file, protocol=pickle.HIGHEST_PROTOCOL)
