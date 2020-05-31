from money import Money


def test_multiplication():
    money = Money(5, "CHF")
    assert money.times(2) == Money(10, "CHF")
    assert money.times(3) == Money(15, "CHF")


def test_equals():
    assert Money(5, "CHF") == Money(5, "CHF")
    assert not Money(6, "CHF") == Money(69, "CHF")
    assert not Money(5, "CHF") == Money(5, "USD")


def test_currency():
    assert "USD" == Money(1, "USD").currency
    assert "CHF" == Money(1, "CHF").currency


def test_to_string():
    assert str(Money(1, 'USD')) == '1 USD'


def test_addition():
    # same currency addition
    assert "10 USD" == str(Money(9, "USD") + Money(1, "USD"))

    # different currency addition
    assert "10 USD" == str(Money(9, "USD") + Money(1, "CHF"))


test_equals()
test_multiplication()

test_currency()
test_to_string()

test_addition()
