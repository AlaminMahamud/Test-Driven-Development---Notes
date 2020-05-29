from dollar import Dollar
from franc import Franc


def test_multiplication():

    # test_franc_multiplication
    franc = Franc(5, "CHF")
    assert franc.times(2) == Franc(10, "CHF")
    assert franc.times(3) == Franc(15, "CHF")

    # test_dollar_multiplication
    dollar = Dollar(5, "USD")
    assert dollar.times(2) == Dollar(10, "USD")
    assert dollar.times(3) == Dollar(15, "USD")


def test_equals():
    assert Franc(5, "CHF") == Franc(5, "CHF")
    assert Dollar(5, "USD") == Dollar(5, "USD")
    assert not Franc(6, "CHF") == Franc(69, "CHF")
    assert not Dollar(50, "USD") == Dollar(55, "USD")
    assert not Franc(5, "CHF") == Dollar(5, "USD")


def test_currency():
    assert "USD" == Dollar(1, "USD").currency
    assert "CHF" == Franc(1, "CHF").currency


def test_to_string():
    assert str(Dollar(1, 'USD')) == '1 USD'


test_equals()
test_multiplication()

test_currency()
test_to_string()