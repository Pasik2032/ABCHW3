from plants import Plants


class Tree(Plants):
    def __init__(self,  name, age):
        super().__init__(name)
        self.age = age

    def Print(self):
        print("It is tree: name =  ", self.name, ", age = ", self.age, ". Quotient = ", super().quotient())
        pass

    def Write(self, ostream):
        ostream.write("It is tree: name = {}  age = {}, Quotient = {}".format(self.name, self.age, str(super().quotient())))
        pass
