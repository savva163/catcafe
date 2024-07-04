from random import randint
from random import choice
from house import House

items = [1, 2, 3, 4, 5, 6]
class AI():
    def choose_dice(self, dice_list: list=None):
        """выбирает произвоьный кубик из трех или двух в зависимости от хода, i_player = True если игрок выбирает кубик первым"""
        return choice(dice_list)

    def choose_action(self, house: House, dices=[int, int]):
        tow_n = [1, 2, 3, 4, 5]
        while tow_n != []:
            tower = choice(tow_n)
            if house._get(tower, dices[0]) == "":
                return tower, dices[0], dices[1]
            elif house._get(tower, dices[1]) == "":
                return tower, dices[1], dices[0]
            else:
                tow_n.remove(tower)
        return None

