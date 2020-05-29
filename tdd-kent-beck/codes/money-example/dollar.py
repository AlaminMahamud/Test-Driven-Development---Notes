from money import Money


class Dollar(Money):

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

