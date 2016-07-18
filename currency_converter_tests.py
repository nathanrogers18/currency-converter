from nose.tools import raises

from currency_converter import Currency, DifferentCurrencyCodeError

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
def test_currency_code_error():
    usd_currency = Currency('USD', 5)
    eur_currency = Currency('EUR', 5)
    usd_currency + eur_currency


def test_string_currency():
    pass

"""
Must be created with an amount and a currency code.
TESTED - Must equal another Currency object with the same amount and currency code.
TESTED - Must NOT equal another Currency object with different amount or currency code.
TESTED - Must be able to be added to another Currency object with the same currency code.
TESTED - Must be able to be subtracted by another Currency object with the same currency code.
Must raise a DifferentCurrencyCodeError when you try to add or subtract two Currency objects with different currency codes.
TESTED - Must be able to be multiplied by an int or float and return a Currency object.
Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and figure out the correct currency code. It can also take two arguments, one being the amount and the other being the currency code.
"""
