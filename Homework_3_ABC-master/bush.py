from plants import Plants
from enum import Enum


class Monthes(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class Bush(Plants):
    def __init__(self, name, monthes):
        super().__init__(name)
        self.monthes = Monthes(monthes)

    def Print(self):
        print("It is bush: name =  ", self.name, ", month of flowering = ", self.monthes.name,
              ". Quotient = ", super().quotient())
        pass

    def Write(self, ostream):
        ostream.write("Bush: name = {}  month of flowering = {}. Quotient = {}".format(
            self.name, self.monthes.name, str(super().quotient())))
        pass
