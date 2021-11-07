
class Plants:
    def __init__(self, name):
        self.name = name

    def quotient(self):
        vowels = set("aeyiou")
        count = 0
        for letter in self.name:
            if letter in vowels:
                count += 1
        return float(count) / float(len(self.name))
    pass
