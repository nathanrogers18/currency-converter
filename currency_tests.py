from nose.tools import raises
from currency import Currency, DifferentCurrencyCodeError, CURRENCY_CONVERSIONS
from currency_converter import CurrencyConverter, UnknownCurrencyCodeError
from currency_trader import CurrencyTrader, EpicCurrencyTrader

### Currency Tests

def test_create_create_currency_with_code_and_amount():
    one_dollar = Currency('USD', 1)
    assert one_dollar.code == 'USD'
    assert one_dollar.value == 1

def test_add_two_currencies():
    #Arrange
    one_dollars = Currency('USD', 1)
    two_dollars = Currency('USD', 2)
    #Act
    result = one_dollars + two_dollars
    #Assertt
    assert result.value == 3
    assert result.code == 'USD'

def test_subtract_two_currencies():
    #Arrange
    five_dollars = Currency('USD', 5)
    two_dollars = Currency('USD', 2)
    #Act
    result = five_dollars - two_dollars
    #Assertt
    assert result.value == 3
    assert result.code == 'USD'

def test_equal_currencies():
    five_dollars = Currency('USD', 5)
    fiver = Currency('USD', 5.00)
    assert five_dollars == fiver

def test_not_equal_currencies_value():
    five_dollars = Currency('USD', 5)
    six_dollars = Currency('USD', 6)
    assert five_dollars != six_dollars

def test_not_equal_currencies_code():
    five_dollars = Currency('USD', 5)
    fiver = Currency('EUR', 5.00)
    assert five_dollars != fiver

def test_mult_currency_int():
    five_dollars = Currency('USD', 5)
    expected_outcome = Currency('USD', 25)
    assert five_dollars * 5 == expected_outcome

def test_mult_currency_float():
    five_dollars = Currency('USD', 5)
    expected_outcome = Currency('USD', 2.5)
    assert five_dollars * 0.5 == expected_outcome

@raises(DifferentCurrencyCodeError)
def test_currency_code_error_add():
    usd_currency = Currency('USD', 5)
    eur_currency = Currency('EUR', 5)
    usd_currency + eur_currency

@raises(DifferentCurrencyCodeError)
def test_currency_code_error_sub():
    usd_currency = Currency('USD', 5)
    eur_currency = Currency('EUR', 5)
    usd_currency - eur_currency


def test_string_currency_USD():
    string_currency = Currency('$1.20')
    standard_currency = Currency('USD', 1.20)
    assert string_currency == standard_currency

def test_string_currency_JPY():
    string_currency = Currency('¥  1.20')
    standard_currency = Currency('JPY', 1.20)
    assert string_currency == standard_currency

def test_string_currency_EUR():
    string_currency = Currency('€ 1.20 ')
    standard_currency = Currency('EUR', 1.20)
    assert string_currency == standard_currency


"""
TESTED - Must be created with an amount and a currency code.
TESTED - Must equal another Currency object with the same amount and currency code.
TESTED - Must NOT equal another Currency object with different amount or currency code.
TESTED - Must be able to be added to another Currency object with the same currency code.
TESTED - Must be able to be subtracted by another Currency object with the same currency code.
TESTED - Must raise a DifferentCurrencyCodeError when you try to add or subtract two Currency objects with different currency codes.
TESTED - Must be able to be multiplied by an int or float and return a Currency object.
TESTED - Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and figure out the correct currency code. It can also take two arguments, one being the amount and the other being the currency code.
"""

### CurrencyConverter Tests

def test_create_converter_with_dictionary():
    converter = CurrencyConverter({'USD': 1.0, 'EUR': 0.74})
    assert converter.currency_conversions == {'USD': 1.0, 'EUR': 0.74}

def test_convert_to_same_currency():
    converter = CurrencyConverter({'USD': 1.0, 'EUR': 0.74})
    assert converter.convert(Currency('USD', 1), 'USD') == Currency('USD', 1)

def test_convert_to_different_currency_small_dict():
    converter = CurrencyConverter({'USD': 1.0, 'EUR': 0.74})
    assert converter.convert(Currency('USD', 1), 'EUR') == Currency('EUR', 0.74)

def test_convert_to_different_currency_big_dict():
    converter = CurrencyConverter(CURRENCY_CONVERSIONS)
    assert converter.convert(Currency('BBD', 2), 'GHS') == Currency('GHS', 3.969829297340214)


@raises(UnknownCurrencyCodeError)
def test_convert_from_unknown_currency():
    converter = CurrencyConverter({'USD': 1.0, 'EUR': 0.74})
    converter.convert(Currency('XXX', 1), 'EUR')

@raises(UnknownCurrencyCodeError)
def test_convert_to_unknown_currency():
    converter = CurrencyConverter({'USD': 1.0, 'EUR': 0.74})
    converter.convert(Currency('USD', 1), 'XXX')

"""
TESTED - Must be initialized with a dictionary of currency codes to conversion rates (see link to rates below).
TESTED - At first, just make this work with two currency codes and conversation rates, with one rate being 1.0 and the other being the conversation rate. An example would be this: {'USD': 1.0, 'EUR': 0.74}, which implies that a dollar is worth 0.74 euros.
TESTED - Must be able to take a Currency object and a requested currency code that is the same currency code as the Currency object's and return a Currency object equal to the one passed in. That is, currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD').
TESTED - Must be able to take a Currency object that has one currency code it knows and a requested currency code and return a new Currency object with the right amount in the new currency code.
TESTED - Must be able to be created with a dictionary of three or more currency codes and conversion rates. An example would be this: {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}, which implies that a dollar is worth 0.74 euros and that a dollar is worth 120 yen, but also that a euro is worth 120/0.74 = 162.2 yen.
TESTED - Must be able to convert Currency in any currency code it knows about to Currency in any other currency code it knows about.
TESTED - Must raise an UnknownCurrencyCodeError when you try to convert from or to a currency code it doesn't know about.
"""

### CurrencyTrader Tests

def test_currency_trader():
    currency = Currency('USD', 1)
    converter1 = CurrencyConverter({'USD': 1.0, 'EUR': 0.5, 'JPY': 100})
    converter2 = CurrencyConverter({'USD': 1.0, 'EUR': 2, 'JPY': 25})
    trader = CurrencyTrader(currency, converter1, converter2)
    assert trader.best_investment() == 'EUR'

"""
TESTED - Build a third class named CurrencyTrader. CurrencyTrader must be initialized with two CurrencyConverter objects from two different points in time, plus a starting Currency.
CurrencyTrader must have a method which returns the best currency investment over that span of time.
For instance, if you are starting with $1,000,000, assume that you can convert your dollars to one currency at the first point in time, but that you must then convert it back to dollars at the second point in time. The best bet given two CurrencyConverters may be GBP. If USD -> GBP is 1 to 1 at the first point in time, then 1 to 0.5 at the second point in time, you can double your money.
You do not need to modify Currency or CurrencyConverter to get this to work, but if you see a path that involves modifying them and want to give it a shot, feel free.
"""

### Epic CurrencyTrader Tests

def test_currency_trader_array_of_converters():
    currency = Currency('USD', 1)
    converter1 = CurrencyConverter({'USD': 1.0, 'EUR': 0.5, 'JPY': 100})
    converter2 = CurrencyConverter({'USD': 1.0, 'EUR': 2, 'JPY': 25})
    converter3 = CurrencyConverter({'USD': 1.0, 'EUR': 2, 'JPY': 250})
    converter4 = CurrencyConverter({'USD': 10, 'EUR': 12, 'JPY': 25})
    trader = EpicCurrencyTrader(currency, [converter1, converter2, converter3, converter4])
    assert trader.best_investments() == ['EUR','JPY','USD']


"""
You guessed it. Modify your CurrencyTrader to accept an array of CurrencyConverter objects and a starting Currency.
If the length of the array is greater than 2, you can move your currency more than once,
so long as it ends in the same currency code as it started. Find the best set of currency trades for your money over time.
"""
