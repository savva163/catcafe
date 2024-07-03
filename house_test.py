from house import (House)

def test_position():
    c = House()
    assert c._position(12, 3) == False
    assert c._position(2, -1) == False
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
    assert c.house[7][2] == "NAN"
    c.put(3, 2, 2)
    assert c.house[9][2] == 2


def test_score():
    c = House()
    c.put(1, 1, 1)
    c.put(1, 2, 2)
    c.put(1, 5, 5)
def test_score_home1():
    a = House()
    assert a.score_home1() == 0
    a.put(1, 1, 2)
    assert a.score_home1() == 0
    a.put(1, 2, 2)
    a.put(1, 3, 2)
    a.put(1, 5, 2)
    assert a.score_home1() == 4

def test_score_ball_2():
    c = House()
    assert c.score_ball_2() == 0
    c.put(5, 1, 2)
    assert c.score_ball_2() == 3
    c.put(5, 3, 2)
    assert c.score_ball_2() == 8

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
    assert c.score_bowl_4() == 1
    c.put(3, 4, 2 )
    assert c.score_bowl_4() == 2
    c.put(2, 5, 3)
    assert c.score_bowl_4() == 4
    c.put(3, 6, 6)
    print(c)

def test_score_pillow_5():
    c = House()
    c.put(4, 5, 5)
    assert c.score_pillow_5() == 15
    c.put(3, 6, 5)
    assert c.score_pillow_5() == 21
    c.put(1, 2, 5)
    assert c.score_pillow_5() == 23
    c.put(1, 3, 5)
    assert c.score_pillow_5() == 26
    c.put(1, 5, 5)
    assert c.score_5() == 31
    print(c)
def test_score_6():
    c = House()
    c.put(5, 1, 6)
    assert c.score_mouse_6() == 22
    c.put(5, 2, 6)
    assert c.score_mouse_6() == 22
    c.put(2, 4, 6)
    assert c.score_mouse_6() == 26
    c.put(2, 5, 6)
    assert c.score_mouse_6() == 32
    print(c)

def test_save():
    pass

def test_load():
    c = House()
    c.put(3, 4, 1)
    print(c)
    c.save()
    a = House()
    print(a)
    a.load(c.save())
    print(a)
