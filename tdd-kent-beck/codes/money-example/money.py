from decimal import Decimal


class Money:
    def __init__(self, amount, currency="USD"):
        self._amount = Decimal(amount)
        self._currency = currency

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    def __eq__(self, other):
        return (self.amount == other.amount) and \
               (self.currency == other.currency)

    def __str__(self):
        return f"{round(self.amount, 2)} {self.currency}"
