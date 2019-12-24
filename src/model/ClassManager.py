from model import DefaultClass
from model.DefaultClassBuilder import DefaultClassBuilder


# If a class with the name exists then return it, otherwise return a new default class
# TODO: Implement
def get_default_class(class_name: str) -> DefaultClass:
    return DefaultClassBuilder(class_name).get_default_class()
