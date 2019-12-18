from abc import ABC, abstractmethod


class IView(ABC):
    @abstractmethod
    def update(self, **kwargs):
        pass
