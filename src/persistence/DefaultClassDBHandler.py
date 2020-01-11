from pathlib import Path
import pickle


cwd = Path.cwd().parent
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

    def insert(self, default_class):
        print("Inserting %s\n" % default_class.class_name)
        self.__class_list.append(default_class)

    def get_all_database_objects(self):
        return self.__class_list

    def save(self):
        with open(db_file_path, 'wb') as file:
            pickle.dump(self.__class_list, file, protocol=pickle.HIGHEST_PROTOCOL)
