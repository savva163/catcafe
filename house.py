from copy import copy
SCORES = [[6, 4], [9, 5], [7, 3], [8, 4], [3, 2]]
ITEMS = ["_домик_", "клубок_", "бабочка", "_миска_", "подушка", "_мышка_"]
MOUSE = [2, 6, 12, 20]
BOT = (2, 0)
TOP = (-2, 0)
RBOT = (1, 1)
LBOT = (1, -1)
RTOP = (-1, 1)
LTOP = (-1, -1)
CONNECTIONS = [BOT, TOP, RBOT, LBOT, RTOP, LTOP]
class House():
    def __init__(self, house=None):
        if house == None:
            self.house = [["NAN", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["NAN", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "NAN", "NAN", ""],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", ""],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", ""],
                          ["NAN", "", "NAN", "", "NAN"]]
        else:
            self.house = house

    def item(self, i, g):
        if type(self.house[i][g]) == int:
            return (ITEMS[self.house[i][g] - 1])
        else:
            return "_______"

    def __repr__(self):
        return f"""  
                                     7/3
                         9/5          |           8/4
           6/4           |         6_{self.item(1, 2)}_      |
            |         6_{self.item(0, 1)}_      |         6_{self.item(0, 3)}_
         5_{self.item(3, 0)}_      |         5_{self.item(3, 2)}_      |
            |         5_{self.item(2, 1)}_      |         5_{self.item(2, 3)}_
            |            |         4_{self.item(5, 2)}_      |           3/2
            |         4_{self.item(4, 1)}_      |         4_{self.item(4, 3)}_      |
         3_{self.item(7, 0)}_      |            |            |         3_{self.item(7, 4)}_
            |         3_{self.item(6, 1)}_      |         3_{self.item(6, 3)}_      |
         2_{self.item(9, 0)}_      |         2_{self.item(9, 2)}_      |         2_{self.item(9, 4)}_
            |         2_{self.item(8, 1)}_      |         2_{self.item(8, 3)}_      |
         1_{self.item(11, 0)}_      |         1_{self.item(11, 2)}_      |         1_{self.item(11, 4)}_
            |         1_{self.item(10, 1)}_      |         1_{self.item(10, 3)}_      |
            |            |            |            |            |
            =            =            =            =            =
        """

    def score(self):
        s = 0
        s += self.score_home_1()
        s += self.score_ball_2()
        s += self.score_butterfly_3()
        s += self.score_bowl_4()
        s += self.score_pillow_5()
        s += self.score_mouse_6()
        return s

    def score_home_1(self):
        s = 0
        for i in range(5):
            w = []
            for g in range(len(self.house)):
                w.append(self.house[g][i])
            if "" in w:
                s += 0
            elif 1 in w:
                s += SCORES[i][0]
            else:
                s += SCORES[i][1]
        return s


    def score_ball_2(self):
        total_balls = 0
        total_isolated_balls = 0
        num_rows = len(self.house)
        num_cols = len(self.house[0])

        for row in range(num_rows):
            for col in range(num_cols):
                if self.house[row][col] == 2:
                    total_balls += 1
                    isolated = True
                    for drow, dcol in CONNECTIONS:
                        adj_row = row + drow
                        adj_col = col + dcol
                        if 0 <= adj_row < num_rows and 0 <= adj_col < num_cols:
                            if self.house[adj_row][adj_col] == 2:
                                isolated = False
                                break
                    if isolated:
                        total_isolated_balls += 1

        return total_balls * total_isolated_balls


    def score_butterfly_3(self):
        s = 0
        for row in self.house:
            count_butterflies = row.count(3)
            s += count_butterflies * 3

        return s

    def score_bowl_4(self):
        s = 0
        for row in range(len(self.house)):
            for col in range(len(self.house[row])):
                if self.house[row][col] == 4:
                    items = set()
                    for connection in CONNECTIONS:
                        drow = connection[0]
                        dcol = connection[1]
                        if self._position(row + drow, col + dcol):
                            if self.house[row + drow][col + dcol] not in ["", "NAN"]:
                                items.add(self.house[row + drow][col + dcol])
                    s += len(set(items))
        return s

    def score_pillow_5(self):
        s = 0
        for i in range(len(self.house)):
            for item_index, item in enumerate(self.house[i]):
                if item == 5:
                    s += (12 - i) // 2 if item_index % 2 == 0 else (13 - i) // 2
        return s

    def score_mouse_6(self):
        s = 0
        for row in range(len(self.house)):
            for col in range(len(self.house[row])):
                if self.house[row][col] != 6:
                    continue
                mice = self.find_mice_complex(row, col, [(row, col)])
                s += (20 / len(mice)) if len(mice) > 4 else 1 + len(mice)
        return round(s)

    def put(self, number_tower, number_floor, number_item):
        if number_tower % 2 == 1:
            row_index = 12 - 2 * number_floor
        else:
            row_index = 13 - 2 * number_floor

        if self.house[row_index][number_tower - 1] != "NAN":
            if self.house[row_index][number_tower - 1] in [1, 2, 3, 4, 5, 6]:
                print('Это место уже занято!')
            else:
                self.house[row_index][number_tower - 1] = number_item
        else:
            print(f'Такого места нет!')

    def _position(self, x, y):
        if 0 <= x <= 11 and 0 <= y <= 4:
            return True
        else:
            return False

    def find_mice_complex(self, row, col, mice):
        for drow, dcol in CONNECTIONS:
            next_row, next_col = row + drow, col + dcol
            if self._position(next_row, next_col) and self.house[next_row][next_col] == 6 and (
            next_row, next_col) not in mice:
                mice.append((next_row, next_col))
                self.find_mice_complex(next_row, next_col, mice)
        return mice

    def save(self):
        return self.house

    @classmethod
    def load(cls, data: list):
        return cls(data)











