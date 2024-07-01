from house import House

def test_init():
    pass

def test_repr():
    pass

def test_score():
    pass

def test_score1():
    c = House()
    assert c.score1() == 0
    c.put(1, 1, 1)
    c.put(1, 2, 2)
    c.put(1, 3, 3)
    c.put(1, 5, 5)
    assert c.score1() == 6

    a = House()
    assert a.score1() == 0
    a.put(1, 1, 2)
    a.put(1, 2, 2)
    a.put(1, 3, 2)
    a.put(1, 5, 2)
    assert a.score1() == 4
    assert type(a.score1()) == int

def test_score2():
    pass

def test_score3():
    c = House()
    c.put(1, 3, 3)
    assert c.score3() == 6
    c.put(1, 2, 3)
    assert c.score3() == 9
    print(c)

def test_score4():
    pass

def test_score5():
    pass
def test_score6():
    pass

def test_save():
    pass

def test_load():
    pass
