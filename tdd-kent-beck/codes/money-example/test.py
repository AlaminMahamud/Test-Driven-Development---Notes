from dollar import Dollar
from franc import Franc


def test_dollar_multiplication():
    dollar = Dollar(5)
    assert dollar.times(2) == Dollar(10)
    assert dollar.times(3) == Dollar(15)


def test_franc_multiplication():
    franc = Franc(5)
    assert franc.times(2) == Franc(10)
    assert franc.times(3) == Franc(15)


def test_equals():
    assert Franc(5) == Franc(5)
    assert Dollar(5) == Dollar(5)

    assert not Franc(6) == Franc(69)
    assert not Dollar(50) == Dollar(55)


test_franc_multiplication()
test_dollar_multiplication()

test_equals()
