from dollar import Dollar


def test_multiply_dollars():
    dollar = Dollar(5)
    dollar.times(2)
    assert dollar.amount == 10

test_multiply_dollars()