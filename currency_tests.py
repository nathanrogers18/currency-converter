from nose.tools import raises
from currency import Currency, DifferentCurrencyCodeError, CURRENCY_CONVERSIONS
from currency_converter import CurrencyConverter, UnknownCurrencyCodeError
from currency_trader import CurrencyTrader, EpicCurrencyTrader
from currency_scraper import CurrencyScraper

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

### CurrencyScraper Tests

def test_currency_scraper():
    scraped_rates = CurrencyScraper('2008-01-24').currency_conversions
    expected_rates = {
        "AED": 3.6725,
        "ALL": 82.814029,
        "AMD": 303.001575,
        "ANG": 1.785,
        "AOA": 74.832052,
        "ARS": 3.152147,
        "AUD": 1.139338,
        "AWG": 1.79025,
        "BBD": 2,
        "BDT": 68.400592,
        "BGN": 1.333844,
        "BHD": 0.3759,
        "BIF": 1078.796256,
        "BMD": 1,
        "BND": 1.485052,
        "BOB": 7.575415,
        "BRL": 1.790533,
        "BSD": 1,
        "BTN": 39.453633,
        "BWP": 6.147085,
        "BYR": 2153.981007,
        "BZD": 1.9849,
        "CAD": 1.010445,
        "CDF": 539.782947,
        "CHF": 1.087969,
        "CLP": 471.09077,
        "CNY": 7.22617,
        "COP": 1985.871756,
        "CRC": 496.739256,
        "CVE": 75.197436,
        "CZK": 17.670446,
        "DJF": 177.721,
        "DKK": 5.068412,
        "DOP": 33.514438,
        "DZD": 66.85224,
        "EEK": 10.620542,
        "EGP": 5.545601,
        "ETB": 9.040353,
        "EUR": 0.678728,
        "FJD": 1.55687,
        "FKP": 0.507922,
        "GBP": 0.507648,
        "GEL": 1.594729,
        "GIP": 0.509343,
        "GMD": 24.821099,
        "GNF": 4264.1642,
        "GTQ": 7.73131,
        "GYD": 202.730131,
        "HKD": 7.808065,
        "HNL": 18.905,
        "HRK": 4.95089,
        "HTG": 37.441233,
        "HUF": 175.273302,
        "IDR": 9390.86448,
        "IEP": 0.667495,
        "ILS": 3.694286,
        "INR": 39.39768,
        "IQD": 1212.940608,
        "IRR": 9281.438508,
        "ISK": 65.893746,
        "JMD": 70.012542,
        "JOD": 0.70885,
        "JPY": 106.692058,
        "KES": 70.78502,
        "KGS": 35.951522,
        "KHR": 3942.969384,
        "KMF": 335.516606,
        "KPW": 142.44491,
        "KRW": 949.329601,
        "KWD": 0.27292,
        "KZT": 120.187829,
        "LAK": 9239.341713,
        "LBP": 1506.819828,
        "LKR": 107.862304,
        "LRD": 61.752658,
        "LSL": 7.068605,
        "LTL": 2.354771,
        "LVL": 0.477598,
        "LYD": 1.226049,
        "MAD": 7.739222,
        "MDL": 11.299046,
        "MGA": 1775.881001,
        "MKD": 41.849826,
        "MMK": 6.51,
        "MNT": 1171.050927,
        "MOP": 8.026713,
        "MRO": 245.030337,
        "MUR": 28.851125,
        "MVR": 12.7975,
        "MWK": 138.302973,
        "MXN": 10.901137,
        "MYR": 3.269578,
        "NAD": 7.039298,
        "NGN": 122.922761,
        "NIO": 18.337133,
        "NOK": 5.461264,
        "NPR": 66.623839,
        "NZD": 1.29419,
        "OMR": 0.384497,
        "PAB": 1,
        "PEN": 3.004574,
        "PGK": 2.735151,
        "PHP": 41.117434,
        "PKR": 62.428466,
        "PLN": 2.466412,
        "PYG": 4927.414918,
        "QAR": 3.64,
        "RON": 2.560881,
        "RUB": 24.468645,
        "RWF": 544.455672,
        "SAR": 3.74985,
        "SBD": 7.213634,
        "SCR": 7.996452,
        "SEK": 6.443289,
        "SGD": 1.428298,
        "SHP": 0.507922,
        "SKK": 22.757134,
        "SLL": 2954.923648,
        "SOS": 1354.930673,
        "STD": 14067.127787,
        "SVC": 8.75061,
        "SYP": 51.050108,
        "SZL": 7.066184,
        "THB": 31.20498,
        "TJS": 3.470008,
        "TND": 1.217224,
        "TOP": 1.940904,
        "TRY": 1.192114,
        "TTD": 6.2505,
        "TWD": 32.33907,
        "TZS": 1161.004754,
        "UAH": 5.064015,
        "UGX": 1702.752677,
        "USD": 1,
        "UYU": 27.059923,
        "UZS": 1294.694128,
        "VEF": 2.1473,
        "VND": 15970.038807,
        "VUV": 94.450001,
        "WST": 2.583618,
        "XAF": 476.727629,
        "XCD": 2.667507,
        "XDR": 0.633666,
        "XOF": 447.052624,
        "XPF": 81.691434,
        "YER": 198.42514,
        "ZAR": 7.02172,
        "ZMK": 3741.504911,
        "ZWD": 29996.973112
    }
    assert scraped_rates == expected_rates

"""
Poll the currency conversion rates from an API or scrape them from a website on the internet using either the built-in urllib module.
Use these semi-real time rates in conjunction with your CurrencyTrader to attempt real-world statistical arbitrage.
"""
