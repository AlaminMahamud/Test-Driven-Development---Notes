from dollar import Dollar
from franc import Franc
from money import Money


def test_multiplication():
    money = Money(20)
    assert money.times(2) == Money(40)
    assert not money.times(2) == Dollar(40)
    assert not money.times(2) == Franc(40)

    # test_franc_multiplication
    franc = Franc(5)
    assert franc.times(2) == Franc(10)
    assert franc.times(3) == Franc(15)

    # test_dollar_multiplication
    dollar = Dollar(5)
    assert dollar.times(2) == Dollar(10)
    assert dollar.times(3) == Dollar(15)


def test_equals():
    assert Franc(5) == Franc(5)
    assert Dollar(5) == Dollar(5)
    assert not Franc(6) == Franc(69)
    assert not Dollar(50) == Dollar(55)
    assert not Franc(5) == Dollar(5)


test_equals()
test_multiplication()
