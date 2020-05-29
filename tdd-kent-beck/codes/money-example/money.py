class Money():
    def __init__(self, amount, currency):
        self._amount = amount
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

    @classmethod
    def get_instance_of_called_class(cls, amount, currency):
        return cls(amount, currency)

    def times(self, multiplier):
        return self.get_instance_of_called_class(self.amount * multiplier, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"