from franc import Franc


def test_franc_multiplication():
    franc = Franc(5)
    assert franc.times(2) == Franc(10)
    assert franc.times(3) == Franc(15)


def test_franc_equals():
    franc1 = Franc(5)
    franc2 = Franc(5)
    assert franc1 == franc2

    franc1 = Franc(6)
    franc2 = Franc(65)
    assert not franc1 == franc2


test_franc_multiplication()
test_franc_equals()
