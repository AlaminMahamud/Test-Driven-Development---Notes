class Money:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def __eq__(self, other):
        return (self.amount == other.amount) and \
               (self.__class__.__name__ == other.__class__.__name__)

    @classmethod
    def get_instance_of_called_class(cls, amount):
        return cls(amount)

    def times(self, multiplier):
        return self.get_instance_of_called_class(self.amount * multiplier)
