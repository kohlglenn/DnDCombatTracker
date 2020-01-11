from model import DefaultClass
from model.DefaultClassBuilder import DefaultClassBuilder
from persistence.DefaultClassDBHandler import DefaultClassDBHandler
from typing import List


class ClassManager:

    def __init__(self):
        self.db = DefaultClassDBHandler()

    # If a class with the name exists then return it, otherwise return a new default class
    def get_default_class(self, class_name: str) -> DefaultClass:
        dc_list = self.db.get_all_default_classes()
        dc = list(filter(lambda x: x.class_name == class_name, dc_list))
        if len(dc) > 0:
            return dc[0]
        else:
            dc = DefaultClassBuilder(class_name).get_default_class()
            self.db.insert_default_class(dc)
            self.db.save()
            return dc

    def get_all_default_class_names(self) -> List[str]:
        return [c.class_name for c in self.db.get_all_default_classes()]
