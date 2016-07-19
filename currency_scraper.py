import requests

class CurrencyScraper:
    """Takes date in the format YYYY-MM-DD"""
    def __init__(self, date):
        self.date = date
        url = "https://openexchangerates.org/api/historical/{}.json?app_id=52d118f151774431acbe8ef5e54d3c40".format(date)
        req = requests.get(url)
        self.currency_conversions = req.json()['rates']
