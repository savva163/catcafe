from house import House

def test_position():
    c = House()
    assert c._position(2, 3) == True
    assert c._position(12, 3) == False
    assert c._position(2, -1) == False
    assert c._position(12, 12323) == False
    assert c._position(-1, -3) == False


def test_init():
    c = House()
    assert c.house == [["NAN", "NAN", "", "NAN", "NAN"],
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

def test_repr():
    c = House()
    print(c)
    c.put(3, 3, 1)
    print(c)
    c.put(3, 2, 2)
    print(c)

def test_put():
    c = House()
    c.put(3, 3, 1)
    assert c.house[6][2] == "NAN"
    c.put(3, 2, 2)
    assert c.house[8][2] == 2
    c.put(2, 6, 5)
    assert c.house[1][1] == 5
    print(c)

def test_get():
    c = House()
    c.put(3, 3, 1)
    assert c._get(3, 3) == "NAN"
    c.put(3, 2, 2)
    assert c._get(3, 2) == 2
    c.put(2, 6, 5)
    assert c._get(2, 6) == 5
    print(c)

def test_score():
    c = House()
    c.put(1, 1, 1)
    c.put(1, 2, 2)
    c.put(1, 3, 3)
    c.put(1, 5, 5)
    c.put(2, 2, 4)
    c.put(2, 1, 6)
    c.put(3, 1, 6)
    c.put(4, 2, 6)
    c.put(3, 2, 4)
    c.put(2, 3, 2)
    c.put(2, 5, 5)
    c.put(2, 4, 3)
    c.put(2, 6, 2)
    c.put(5, 1, 1)
    c.put(5, 3, 5)
    c.put(4, 3, 6)
    c.put(4, 4, 6)
    print(c)
    assert c.score() == 60
def test_score_home_1():
    a = House()
    assert a.score_home_1() == 0
    a.put(1, 1, 2)
    assert a.score_home_1() == 0
    a.put(1, 2, 2)
    a.put(1, 3, 2)
    a.put(1, 5, 2)
    assert a.score_home_1() == 4

def test_score_ball_2():
    c = House()
    c.put(1, 2, 2)
    assert c.score_ball_2() == 0
    c.put(5, 1, 2)
    assert c.score_ball_2() == 3
    c.put(5, 3, 2)
    assert c.score_ball_2() == 8
    print(c)

def test_score_butterfly_3():
    c = House()
    c.put(1, 2, 3)
    assert c.score_butterfly_3() == 9
    c.put(1, 5, 3)
    assert c.score_butterfly_3() == 12
    c.put(2, 1, 3)
    assert c.score_butterfly_3() == 15
    print(c)

def test_score_bowl_4():
    c = House()
    c.put(3, 4, 2)
    assert c.score_bowl_4() == 2
    c.put(2, 5, 3)
    assert c.score_bowl_4() == 3
    c.put(2, 6, 5)
    assert c.score_bowl_4() == 4
    c.put(3, 6, 6)
    assert c.score_bowl_4() == 5
    print(c)

def test_score_bowl():
    c = House()
    c.put(4, 5, 4)
    assert c.score_bowl() == 3
    c.put(4, 6, 4)
    assert c.score_bowl() == 5
    c.put(3, 6, 4)
    assert c.score_bowl() == 7
    print(c)

def test_score_pillow_5():
    c = House()
    c.put(3, 6, 5)
    assert c.score_pillow_5() == 21
    c.put(1, 2, 5)
    assert c.score_pillow_5() == 23
    c.put(1, 3, 5)
    assert c.score_pillow_5() == 26
    c.put(1, 5, 5)
    assert c.score_pillow_5() == 31
    print(c)
def test_score_6():
    c = House()
    c.put(3, 1, 6)
    assert c.score_mouse_6() == 14
    c.put(4, 1, 6)
    assert c.score_mouse_6() == 22
    c.put(5, 1, 6)
    assert c.score_mouse_6() == 22
    c.put(5, 2, 6)
    assert c.score_mouse_6() == 22
    print(c)

def test_save():
    c = House()
    assert c.save() == c.house

def test_load():
    c = House()
    c.put(3,2,1)
    c = c.load(c.house)
    assert c.house == [["NAN", "NAN", "", "NAN", "NAN"],
                      ["NAN", "", "NAN", "", "NAN"],
                      ["", "NAN", "", "NAN", "NAN"],
                      ["NAN", "", "NAN", "", "NAN"],
                      ["NAN", "NAN", "", "NAN", "NAN"],
                      ["NAN", "", "NAN", "", "NAN"],
                      ["", "NAN", "NAN", "NAN", ""],
                      ["NAN", "", "NAN", "", "NAN"],
                      ["", "NAN", 1, "NAN", ""],
                      ["NAN", "", "NAN", "", "NAN"],
                      ["", "NAN", "", "NAN", ""],
                      ["NAN", "", "NAN", "", "NAN"]]
