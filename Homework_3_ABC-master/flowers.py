# ----------------------------------------------
from plants import Plants
from enum import Enum


class Type(Enum):
    homemade = 1
    garden = 2
    wild = 3


class Flowers(Plants):
    def __init__(self, name, typeof):
        super().__init__(name)
        self.typeof = Type(typeof)

    def Print(self):
        print("It is flowers: name =  ", self.name, ", type of = ", self.typeof.name,
              ". Quotient = ", super().quotient())
        pass

    def Write(self, ostream):
        ostream.write("Flowesr: name = {}  type of = {}. Quotient = {}".format(
            self.name, self.typeof.name, super().quotient()))
        pass
