# MarkS - Python Challenge Day 11mod - Object-oriented programming
from typing import Dict


class Wallet:

    name: str
    balances: Dict[str, int]


def spend_money(self, currency: str, amount: int) -> int:
    self.balances[currency] = self.balances[currency].get(currency, 0) - amount
    return self.balances[currency]


def display_balances(self):
    print(self.balances)


mark_wallet = Wallet()
mark_wallet.name = "Marks International Wallet"
mark_wallet.balances = {"GBP": 100, "EUR": 80}

new_gbp_balance = mark_wallet.spend_money("GBP", 50)
