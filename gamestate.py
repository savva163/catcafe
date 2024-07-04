import json
from dice import Dice
from player import Player

class GameStage():
    ROLL_DICE = 1
    CHOOSE_DICE = 2
    CHOOSE_ACTION = 3
    NEXT_ROUND = 4
    END_GAME = 5

class Gamestate():
    def __init__(self, players, current_player: int = 0, dices = None):
        self.players = players
        self.current_player_index = current_player
        if dices is None:
            dices = []
            for i in range(len(players)+1):
                dices.append(Dice())
        self.dices = dices

    def run(self):
        stage = GameStage.ROLL_DICE
        while stage != GameStage.END_GAME:
            match stage:
                case GameStage.ROLL_DICE:
                    stage = self.rolled_dice()
                case GameStage.CHOOSE_DICE:
                    stage = self.choose_dice_stage()
                case GameStage.CHOOSE_ACTION:
                    stage = self.choose_action_stage()
                case GameStage.NEXT_ROUND:
                    if self.is_win_condition():
                        stage = GameStage.END_GAME
                    else:
                        self.next_player()
                        stage = GameStage.ROLL_DICE
        return self.win_player()

    def current_player(self):
        return self.players[self.current_player_index]

    def next_player(self):
        n = len(self.players)
        self.current_player_index = (self.current_player_index + 1) % n

    def rolled_dice(self):
        self.rolled_dices = []
        for dice in self.dices:
            dice.roll()
            self.rolled_dices.append(dice.current_side)
        return GameStage.CHOOSE_DICE

    def choose_dice_stage(self):
        for _ in range(len(self.players)):
            self.players[self.current_player_index].choosen_dice = self.players[self.current_player_index].choose_dice(self.rolled_dices)
            self.rolled_dices.remove(self.players[self.current_player_index].choosen_dice)
            self.next_player()
        return GameStage.CHOOSE_ACTION
    def choose_action_stage(self):
        for i in range(len(self.players)):
            dice_list = [self.players[i].choosen_dice, self.rolled_dices[0]]
            action = self.players[i].choose_action(dice_list)
            if action != None:
                self.players[i].tower_lst.put(action[0], action[1], action[2])
        return GameStage.NEXT_ROUND

    def is_win_condition(self):
        for player in self.players:
            full_tower = 0
            for col in range(5):
                w = []
                for row in range(len(player.tower_lst.house)):
                    w.append(player.tower_lst.house[row][col])
                if "" not in w:
                    full_tower += 1
            if full_tower == 3:
                return GameStage.END_GAME
        return False

    def win_player(self):
        lst_player = []
        for player in self.players:
            lst_player.append({
                "pl_cls": player,
                "name": player.name,
                "score": player.tower_lst.score()
            })
        srt_list = sorted(lst_player, key = lambda x: x["score"])
        print(f'Побеждает: {srt_list[-1]["name"]}, с количеством очков: {srt_list[-1]["score"]}')


    def save(self):
        return {
            'players': [p.save() for p in self.players],
            'current_player_index': self.current_player_index,
            'dices': [d.save() for d in self.dices]
        }
    @classmethod
    def load(cls, data):
        data = json.load(data)
        return cls([Player.load(pd) for pd in data['players']],
                   data['current_player_index'],
                   [Dice.load(dd) for dd in data['dices']])





if __name__ == '__main__':
    s = Player('Bob', is_human=True)
    a = Player('Rick')
    c = Gamestate([a, s], 0)
    c.run()
