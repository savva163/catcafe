from random import randint
class Dice():
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]
        self.side = self.roll()
    def __repr__(self):
        return str(self.side)
    def roll(self):
        return self.sides[randint(0, 5)]
c1 = Dice()
c2 = Dice()
c3 = Dice()
print(c1, c1.roll())
