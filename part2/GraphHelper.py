import matplotlib.pyplot as plt
from ApiHelper import CryptoCurrency


def draw_graph(dates, crypto_sign, currency_sign, crypto_currencies: [CryptoCurrency]):
    plt.plot(dates, [currency.price for currency in crypto_currencies])
    plt.title(f"{crypto_sign} цена")
    plt.xlabel("Дата")
    plt.ylabel(currency_sign)
    plt.show()
