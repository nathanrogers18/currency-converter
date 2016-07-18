from currency import Currency


class CurrencyConverter:
    def __init__(self, currency_conversions):
        self.currency_conversions = currency_conversions

    def convert(self, currency, code):
        if currency.code in self.currency_conversions and code in self.currency_conversions:
            ratio = self.currency_conversions[code] / self.currency_conversions[currency.code]
            return Currency(code, currency.value * ratio)
        else:
            raise UnknownCurrencyCodeError

class UnknownCurrencyCodeError(Exception):
    pass
