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
    c = House()
    c.put(1, 2, 2)
    assert c.score2() == 0
    c.put(5, 1, 2)
    assert c.score2() == 6
    c.put(5, 3, 2)
    assert c.score2() == 16

def test_score3():
    c = House()
    c.put(1, 3, 3)
    assert c.score3() == 6
    c.put(1, 2, 3)
    assert c.score3() == 9
    print(c)

def test_score4():
    c = House()
    c.put(4, 5, 1)
    assert c.score4() == 1
    c.put(3, 4, 2 )
    assert c.score4() == 2
    c.put(2, 5, 3)
    assert c.score4() == 3
    print(c)

def test_score5():
    c = House()
    c.put(5, 3, 5)
    assert c.score5() == 6
    c.put(3, 4, 5)
    assert c.score5() == 10
    c.put(4, 5, 5)
    assert c.score5() == 15
    print(c)
def test_score6():
    c = House()
    c.put(1, 1, 6)
    print(c.score6())

def test_save():
    pass

def test_load():
    pass