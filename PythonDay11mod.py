# MarkS - Python Challenge Day 11mod - Object-oriented programming
from typing import Dict


class Wallet:

    def __init__(self, name: str, balances: Dict[str, int]):
        self.name = name
        self.balances = balances

    def spend_money(self, currency: str, amount: int) -> int:
        new_balance = self.balances.get(currency, 0) - amount
        if new_balance >= 0:
            self.balances[currency] = new_balance
        return self.balances[currency]

    def deposit_money(self, currency: str, amount: int) -> int:
        self.balances[currency] = self.balances.get(currency, 0) + amount
        return self.balances[currency]

    def transfer_money(self, creditor: object, currency: str, amount: int) -> int:
        new_balance = self.balances.get(currency, 0) - amount
        if new_balance >= 0:
            self.balances[currency] = new_balance
            creditor.deposit_money(currency, amount)
        return self.balances[currency]

    def display_balances(self):
        print(self.balances)


mark_wallet = Wallet("Marks International Wallet", {"USD": 0, "GBP": 0, "EUR": 0, "YEN": 0})
peter_wallet = Wallet("Peter Wallet", {"USD": 0, "GBP": 0, "EUR": 0, "YEN": 0})
mark_wallet.deposit_money("GBP", 375)
mark_wallet.spend_money("GBP", 100)
mark_wallet.transfer_money(peter_wallet, "GBP", 50)
mark_wallet.display_balances()
peter_wallet.display_balances()
