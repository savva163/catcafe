from ai import AI
from dice import Dice
from house import House
from human import Human

DICES = [Dice(), Dice(), Dice()]

class Player:
    def __init__(self, name: str, house: House = None, is_human: bool = False):
        self.name = name
        self.tower_lst = house
        if is_human:
            self.actor = Human()
        else:
            self.actor = AI()

    def __repr__(self):
        return f'{self.name}: {self.tower_lst}'

    def choose_dice(self, dices):
        return self.actor.choose_dice(dices)

    def choose_action(self):
        return self.actor.choose_action(self.tower_lst, DICES)

    def to_dict(self):
        return {
            "name": self.name,
            "house": self.tower_lst.house,
            "is_human": isinstance(self.actor, Human)
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], House(data["house"]), data["is_human"])

    def save(self):
        return self.to_dict()

    @classmethod
    def load(cls, data: dict):
        return cls.from_dict(data)

if __name__ == '__main__':
    print(type(DICES[0]))



