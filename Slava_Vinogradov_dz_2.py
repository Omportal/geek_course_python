from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, arg):
        self.arg = arg

    @abstractmethod
    def coast(self):
        pass


class Coat(Clothes):
    @property
    def coast(self):
        return round(self.arg / 6.5 + 0.5)


class Suit(Clothes):
    @property
    def coast(self):
        return round(self.arg * 2 + 0.3)


a = Coat(200)
b = Suit(100)
print(a.coast)
print(b.coast)
print(a.coast + b.coast)
