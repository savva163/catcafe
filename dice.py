import json
from random import randint
class Dice():
    SIDES = [1, 2, 3, 4, 5, 6]
    def __init__(self, side=None):
        if side != None and 1 <= side <= 6:
            self.current_side = side
        else:
            self.roll()

    def __repr__(self):
        return str(self.current_side)

    def roll(self):
        self.current_side = self.SIDES[randint(0, 5)]

    def save(self):
        return repr(self)

    @classmethod
    def load(cls, value: str):
        return cls(value)




