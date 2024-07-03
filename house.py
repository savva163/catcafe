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
            self.house = [["NAN", "", "NAN", "", "NAN"],
                          ["NAN", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["NAN", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "NAN", "NAN", ""],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", ""],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", ""]]
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
    s = sum([self.score_home_1(), self.score_ball_2(), self.score_butterfly_3(),
             self.score_bowl_4(), self.score_pillow_5(), self.score_mouse_6()])
    return s

    def score_home_1(self):
    s = 0
    for i in range(5):
        w = [self.house[g][i] for g in range(len(self.house))]
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

    for row in range(len(self.house)):
        for col in range(len(self.house[row])):
            if self.house[row][col] == 2:
                is_isolated = True
                for connection in CONNECTIONS:
                    drow, dcol = connection
                    if self._position(row + drow, col + dcol) and self.house[row + drow][col + dcol] == 2:
                        is_isolated = False
                        break
                total_balls += 1
                if is_isolated:
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
                if self.house[row][col] != 4:
                    continue
                items = set()
                for connection in CONNECTIONS:
                    drow = connection[0]
                    dcol = connection[1]
                    if self._position(row + drow, col + dcol):
                        items.add(self.house[row + drow][col + dcol])
                items.remove("")
                s += len(items)
        return s

    def score_5(self):
        pass

    def score_6(self):
        pass

    def put(self, number_tower, number_floor, number_item):
    target_floor = 12 if number_tower % 2 == 0 else 13
    if self.house[target_floor - 2 * number_floor][number_tower - 1] != "NAN":
        self.house[target_floor - 2 * number_floor][number_tower - 1] = number_item
    else:
        print(f'Такого места нет!')

    def save(self):
        pass

    def load(self):
        pass










