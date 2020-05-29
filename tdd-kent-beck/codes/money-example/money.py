class Money:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def __eq__(self, other):
        print(f"__eq__ called --> self:{self!r} \n other:{other!r}")
        return (self.amount == other.amount) and \
               (self.__class__.__name__ == other.__class__.__name__)



