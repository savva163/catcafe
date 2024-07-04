from gamestate import Gamestate
from player import Player

def test_rolled_dice():
    players = [Player('Bob'), Player('Rick')]
    game = Gamestate(players, 0)
    game.rolled_dice()
    assert game.rolled_dices != game.dices
    game.rolled_dices.remove(game.rolled_dices[0])
    assert game.rolled_dices != game.dices

def test_choose_dice():
    players = [Player('Bob'), Player('Rick')]
    game = Gamestate(players, 0)
    game.rolled_dice()
    game.choose_dice_stage()
    for player in game.players:
        assert player.choosen_dice in [1, 2, 3, 4, 5, 6]

def test_choose_action():
    players = [Player('Bob'), Player('Rick')]
    game = Gamestate(players, 0)
    game.rolled_dice()
    game.choose_dice_stage()
    game.choose_action_stage()
    for player in game.players:
        print(player.tower_lst)

def test_run():
    players = [Player('Bob'), Player('Rick')]
    game = Gamestate(players, 0)
    game.run()