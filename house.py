SCORES = [[6, 4], [9, 5], [7, 3], [8, 4], [3, 2]]
ITEMS = ["домик", "клубок", "бабочка", "миска", "подушка", "мышка"]
MOUSE = [2, 6, 12, 20]

class House:
    def __init__(self):
        self.house = [["NAN", "", "", "", "NAN", ""],
                      ["", "", "", "", "NAN", ""],
                      ["NAN", "", "", "", "NAN", ""],
                      ["", "", "NAN", "", "", ""],
                      ["", "", "", "", "", ""],
                      ["", "", "", "", "", ""],
                      ["", "", "", "", "", ""]]

    def item(self, i, g):
        item = ITEMS[self.house[i][g] - 1] if isinstance(self.house[i][g], int) else "_______"
        return item

    def __repr__(self):
        return f"""  
                             7/3
                 9/5          |           8/4
   6/4           |         6_{self.item(0, 2)}_      |
    |         6_{self.item(0, 1)}_      |         6_{self.item(0, 3)}_
 5_{self.item(1, 0)}_      |         5_{self.item(1, 2)}_      |
    |         5_{self.item(1, 1)}_      |         5_{self.item(1, 3)}_
    |            |         4_{self.item(2, 2)}_      |           3/2
    |         4_{self.item(2, 1)}_      |         4_{self.item(2, 3)}_      |
 3_{self.item(3, 0)}_      |            |            |         3_{self.item(3, 4)}_
    |         3_{self.item(3, 1)}_      |         3_{self.item(3, 3)}_      |
 2_{self.item(4, 0)}_      |         2_{self.item(4, 2)}_      |         2_{self.item(4, 4)}_
    |         2_{self.item(4, 1)}_      |         2_{self.item(4, 3)}_      |
 1_{self.item(5, 0)}_      |         1_{self.item(5, 2)}_      |         1_{self.item(5, 4)}_
    |         1_{self.item(5, 1)}_      |         1_{self.item(5, 3)}_      |
    |            |            |            |            |
    =            =            =            =            ="""

    def score(self):
        s = sum([self.score_1(), self.score_2(), self.score_3(),
                 self.score_4(), self.score_5(), self.score_6()])
        return s

    def score_1(self):
        s = 0
        for i in range(5):
            w = [self.house[g][i] for g in range(len(self.house) - 1)]
            if "" in w:
                s += 0
            elif 1 in w:
                s += SCORES[i][0]
            else:
                s += SCORES[i][1]
        return s

    def score_2(self):
        pass

    def score_3(self):
        s = 0
        for g in self.house:
            s += 3 * g.count(3)
        return s

    def score_4(self):
        pass

    def score_5(self):
        pass

    def score_6(self):
        pass

    def put(self, number_tower, number_floor, number_item):
        self.house[6 - number_floor][number_tower - 1] = number_item

    def save(self):
        pass

    def load(self):
        pass









