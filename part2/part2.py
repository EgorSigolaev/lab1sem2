import datetime

import ApiHelper
import FormatHelper
from datetime import timedelta, date
import GraphHelper

crypto_signs = ["BTC", "ETH"]
currency_signs = ["UAH", "USD"]
date_variants = ["Последние 7 дней", "Последний месяц", "Последний год"]


def greetings():
    print("Привет! Это крипто бот, который готов помочь найти нужный курс криптовалюты.")


def input_id(input_text, variants) -> str:
    request_text = ""
    for index, sign in enumerate(variants):
        request_text += f"[{index}] {sign}\n"
    print(request_text)
    return input(input_text)


def get_variant_id(input_text, variants) -> int:
    while True:
        try:
            id = int(input_id(input_text, variants))
            if id < 0 or id >= len(variants):
                raise ValueError()
        except ValueError:
            print("Извините, не понял, что вы ввели. Попробуйте ещё раз!")
        else:
            return id


def main():
    try:
        greetings()
        crypto = crypto_signs[get_variant_id("Введите номер крипты: ", crypto_signs)]
        currency_sign = currency_signs[get_variant_id("Введите номер валюты: ", currency_signs)]
        date_variant_id = get_variant_id("Введите вариант выборки: ", date_variants)
        today = datetime.date.today()
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
        print("Ошибка загрузки данных. Проверьте ваше интернет соединение!")
    except Exception:
        print("Произошла непредвиденная ошибка!")


main()
