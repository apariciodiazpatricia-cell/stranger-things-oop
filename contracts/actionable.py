from abc import ABC, abstractmethod


class Actionable(ABC):
    @abstractmethod
    def act(self):
        pass
    