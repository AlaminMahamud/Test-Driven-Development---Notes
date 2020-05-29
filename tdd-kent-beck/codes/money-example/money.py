class Money:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def __eq__(self, other):
        return self.amount == other.amount
