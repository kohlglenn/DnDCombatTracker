from abc import ABC, abstractmethod


class Actor(ABC):
    @abstractmethod
    def get_stat_block(self):
        pass
