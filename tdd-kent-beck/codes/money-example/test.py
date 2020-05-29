from dollar import Dollar


def test_multiply_dollars():
    dollar = Dollar(5)
    product = dollar.times(2)
    assert product.amount == 10
    product = dollar.times(3)
    assert product.amount == 15


def test_equality():
    dollar1 = Dollar(5)
    dollar2 = Dollar(5)
    assert dollar1 == dollar2

    dollar1 = Dollar(10)
    dollar2 = Dollar(11)
    assert dollar1 != dollar2


test_multiply_dollars()
test_equality()
