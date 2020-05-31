class ExchangeRate:

    _DEFAULT_CURRENCY = 'USD'
    _RATES = {
        'USD': 1,
        'CHF': 0.5
    }

    def get_rate(self, currency):
        return self._RATES[currency]
