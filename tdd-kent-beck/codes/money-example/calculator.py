from money import Money
from exchange_rate import ExchangeRate
from decimal import Decimal


class Calculator:
    @staticmethod
    def add_money(money1, money2):
        er = ExchangeRate()
        amount = money1.amount * Decimal(er.get_rate(money1.currency)) + \
                 money2.amount * Decimal(er.get_rate(money2.currency))
        return Money(int(amount), currency="USD")

    @staticmethod
    def times(money, num):
        return Money(money.amount * num, money.currency)
