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

class EpicCurrencyTrader:
    def __init__(self, currency, converters):
        self.currency = currency
        self.converters = converters

    def best_investments(self):
        best_investments = []
        for i in range(len(self.converters) - 1):
            conversions1 = self.converters[i].currency_conversions
            conversions2 = self.converters[i + 1].currency_conversions
            performance = {}
            for code in conversions1.keys():
                performance[code] = conversions2[code] / conversions1[code]
            best_investments.append(max(performance, key=performance.get))
        return best_investments
