import ApiHelper
import FormatHelper
from datetime import timedelta
import GraphHelper

crypto_signs = ["BTC", "ETH"]
currency_signs = ["UAH", "USD"]
date_variants = ["Последние 7 дней", "Последний месяц", "Последний год"]


def greetings():
    print("Привет! Это крипто бот, который готов помочь найти нужный курс криптовалюты.")


def input_crypto_id() -> str:
    request_text = ""
    for index, sign in enumerate(crypto_signs):
        request_text += f"[{index}] {sign}\n"
    print(request_text)
    return input("Введите номер крипты: ")


def input_currency_id() -> str:
    request_text = ""
    for index, sign in enumerate(currency_signs):
        request_text += f"[{index}] {sign}\n"
    print(request_text)
    return input("Введите номер валюты: ")


def input_date_variant_id() -> str:
    request_text = ""
    for index, sign in enumerate(date_variants):
        request_text += f"[{index}] {sign}\n"
    print(request_text)
    return input("Введите вариант выборки: ")


def get_crypto_id() -> int:
    while True:
        try:
            crypto_id = int(input_crypto_id())
            if crypto_id < 0 or crypto_id >= len(crypto_signs):
                raise ValueError()
        except ValueError:
            print("Извините, не понял, что вы ввели. Попробуйте ещё раз!")
        else:
            return crypto_id


def get_currency_id() -> int:
    while True:
        try:
            currency_id = int(input_currency_id())
            if currency_id < 0 or currency_id >= len(currency_signs):
                raise ValueError()
        except ValueError:
            print("Извините, не понял, что вы ввели. Попробуйте ещё раз!")
        else:
            return currency_id


def get_date_variant_id() -> int:
    while True:
        try:
            date_variant_id = int(input_date_variant_id())
            if date_variant_id < 0 or date_variant_id >= len(date_variants):
                raise ValueError()
        except ValueError:
            print("Извините, не понял, что вы ввели. Попробуйте ещё раз!")
        else:
            return date_variant_id


def main():
    try:
        greetings()
        crypto = crypto_signs[get_crypto_id()]
        currency_sign = currency_signs[get_currency_id()]
        date_variant_id = get_date_variant_id()
        today = date.today()
        today_year = today.year
        today_month = today.month
        today_day = today.day
        if date_variant_id == 0:
            dates = [
                today - timedelta(days=6),
                today - timedelta(days=5),
                today - timedelta(days=4),
                today - timedelta(days=3),
                today - timedelta(days=2),
                today - timedelta(days=1),
                today
            ]
        elif date_variant_id == 1:
            dates = [
                today - timedelta(days=30),
                today - timedelta(days=24),
                today - timedelta(days=18),
                today - timedelta(days=12),
                today - timedelta(days=6),
                today
            ]
        else:
            dates = [
                today - timedelta(days=180),
                today - timedelta(days=150),
                today - timedelta(days=120),
                today - timedelta(days=90),
                today - timedelta(days=60),
                today - timedelta(days=30),
                today
            ]
        crypto_currencies = []
        for date in dates:
            crypto_currencies.append(ApiHelper.get_crypto_currency(crypto.lower(), currency_sign=currency_sign.lower(),
                                                                   date_formatted=FormatHelper.format_date_for_api(
                                                                       date)))
        GraphHelper.draw_graph(dates=[FormatHelper.format_date_for_ui(date) for date in dates], crypto_sign=crypto,
                               currency_sign=currency_sign,
                               crypto_currencies=crypto_currencies)
    except ConnectionError:
        print("Failed to load data. Check your internet connection!")
