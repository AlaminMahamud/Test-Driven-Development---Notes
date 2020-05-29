class Dollar:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        """Gets amount"""
        return self._amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def __eq__(self, other):
        return self.amount == other.amount
