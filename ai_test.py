from ai import AI
from house import House


def test_choose_dice():
    c = AI()
    assert c.choose_dice([1, 3, 2]) in [1,3,2]

def test_choose_action():
    c = AI()
    a = House()
    c.choose_action(a, [2, 6])
    assert type(c.choose_action(a, [2, 6])) == tuple
    assert c.choose_action(a, [2, 6])[0] in [1, 2, 3, 4, 5]
    assert c.choose_action(a, [2, 6])[1] in [1, 2, 3, 4, 5, 6]
    assert c.choose_action(a, [2, 6])[2] in [1, 2, 3, 4, 5, 6]