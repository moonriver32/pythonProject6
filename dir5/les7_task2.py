from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, arg):
        self.arg = arg

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):

    @property
    def expenses(self):
        return self.arg / 6.5 + 0.5


class Suit(Clothes):

    @property
    def expenses(self):
        return (2 * self.arg + 0.3)


fabric = Coat(2)
fabric1 = Suit(1)

print(fabric.expenses)
print(fabric1.expenses)
