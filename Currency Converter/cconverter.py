# print("Meet a conicoin!")
# n = int(input(""))
# print(f"I have {n} conicoins.")
# amount = 100 * n
# print(f"{n} conicoins cost {amount} dollars.")
# print("I am rich! Yippee!")
# conicoins = float(input())
# currency = ['RUB', 'ARS', 'HNL', 'AUD', 'MAD']
# exchange =
# for c, e in zip(currency, exchange):
#     result = round(conicoins * e, 2)
#     print(f"I will get {result} {c} from the sale of {conicoins} conicoins.")
# exchange = float(input("Please, enter the exchange rate:"))
# result = round((conicoins * exchange), 2)
# print("The total amount of dollars:", result)

import json
import requests
import sys

class Forex:
    filecurrency = {}
    currency_have = input()

    def __init__(self):
        self.maine()

    def maine(self):
        while self.currency_have != "":
            currency_exchange = input()
            if currency_exchange == "":
                sys.exit(0)
            amount = float(input())
            if currency_exchange != "":
                self.foreign_exchange(currency_exchange, amount)
                continue
            else:
                sys.exit(0)

        # return currency_exchange, amount

    def check_currency(self, currency_exchange, r):
        if self.currency_have == 'usd':
            self.filecurrency['eur'] = r['eur']['rate']
        elif self.currency_have == 'eur':
            self.filecurrency['usd'] = r['usd']['rate']
        else:
            self.filecurrency['eur'] = r['eur']['rate']
            self.filecurrency['usd'] = r['usd']['rate']
        if currency_exchange in self.filecurrency:
            print("Oh! It is in the cache!")
            r[currency_exchange]['rate']
        else:
            print("Sorry, but it is not in the cache!")
            self.filecurrency[currency_exchange] = r[currency_exchange]['rate']

        return self.filecurrency[currency_exchange]

    def foreign_exchange(self, currency_exchange, amount):

        response = requests.get(f'http://www.floatrates.com/daily/{self.currency_have.lower()}.json')
        r = response.json()

        print("Checking the cache...")
        exchange = self.check_currency(currency_exchange, r)

        print(f"You received {round(exchange * amount, 2)} {currency_exchange.upper()}.")


Forex()
