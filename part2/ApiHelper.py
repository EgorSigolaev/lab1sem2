import requests


class CryptoCurrency:

    def __init__(self, date, price):
        self.date = date
        self.price = price


def get_crypto_currency(crypto, currency_sign, date_formatted) -> CryptoCurrency:
    response_json = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{date_formatted}/currencies/{crypto}/{currency_sign}.json").json()
    return CryptoCurrency(date=response_json["date"], price=response_json[currency_sign])
