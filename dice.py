import json
from random import choice

SIDES = [1, 2, 3, 4, 5, 6]
class Dice:
    def init(self):
        self.current_side = choice(SIDES)
    def __repr__(self):
        return str(self.current_side)
    def roll(self):
        self.current_side = choice(SIDES)
    def save(self):
        with open('data1.json', 'w') as file:
            json.dump({"current_side": self.current_side}, file)
            return {"current_side": self.current_side}
    @staticmethod
    def load():
        with open('data1.json', 'r') as file:
            data = json.load(file)
        return data["current_side"]


