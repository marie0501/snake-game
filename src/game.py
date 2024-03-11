from abc import ABC, abstractmethod

class Game(ABC):

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def game_over(self):
        pass

    @abstractmethod
    def update(self):
        pass