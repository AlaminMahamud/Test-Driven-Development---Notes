from money import Money
from exchange_rate import ExchangeRate
from calculator import Calculator


def test_multiplication():
    calc = Calculator()
    money = Money(5, "CHF")
    assert calc.times(money, 2) == Money(10, "CHF")
    assert calc.times(money, 3) == Money(15, "CHF")


def test_equals():
    assert Money(5, "CHF") == Money(5, "CHF")
    assert not Money(6, "CHF") == Money(69, "CHF")
    assert not Money(5, "CHF") == Money(5, "USD")


def test_currency():
    assert "USD" == Money(1, "USD").currency
    assert "CHF" == Money(1, "CHF").currency


def test_to_string():
    assert str(Money(1, 'USD')) == '1.00 USD'


def test_addition():
    calc = Calculator()

    # same currency addition
    money1 = Money(9, "USD")
    money2 = Money(1, "USD")
    assert "10.00 USD" == str(calc.add_money(money1, money2))

    # different currency addition
    money1 = Money(9, "USD")
    money2 = Money(2, "CHF")
    assert "10.00 USD" == str(calc.add_money(money1, money2))


def test_exchange_rate():
    er = ExchangeRate()

    # 1 USD should be equal to 1 from the ExchangeRate
    assert er.get_rate("USD") == 1
    assert not er.get_rate("USD") != 1

    # 2 CHF should be equal to 1 USD
    assert er.get_rate("CHF") * 2 == 1


test_equals()
test_multiplication()

test_currency()
test_to_string()

test_addition()
test_exchange_rate()
