from currency import Currency
from currency_converter import CurrencyConverter

class CurrencyTrader:
    def __init__(self, currency, converter1, converter2):
        self.currency = currency
        self.converter1 = converter1
        self.converter2 = converter2

    def best_investment(self):
        performance = {}
        for code in self.converter1.currency_conversions.keys():
            performance[code] = self.converter2.currency_conversions[code] / self.converter1.currency_conversions[code]
        return max(performance, key=performance.get)
