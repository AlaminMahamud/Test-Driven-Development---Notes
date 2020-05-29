from dollar import Dollar


def test_dollar_multiplication():
    dollar = Dollar(5)
    assert dollar.times(2) == Dollar(10)
    assert dollar.times(3) == Dollar(15)


def test_dollar_equality():
    dollar1 = Dollar(5)
    dollar2 = Dollar(5)
    assert dollar1 == dollar2

    dollar1 = Dollar(10)
    dollar2 = Dollar(11)
    assert dollar1 != dollar2


test_dollar_multiplication()
test_dollar_equality()
