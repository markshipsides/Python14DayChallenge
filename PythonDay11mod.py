# MarkS - Python Challenge Day 11mod - Object-oriented programming
# from typing import Dict


class Wallet:

    def __init__(self, name):
        self.name = name
        self.balances: dict = {"USD": 0, "GBP": 0, "EUR": 0, "YEN": 0}

    def spend_money(self, currency: str, amount: int) -> int:
        new_balance = self.balances.get(currency, 0) - amount
        if new_balance >= 0:
            self.balances[currency] = new_balance
        return self.balances[currency]

    def deposit_money(self, currency: str, amount: int) -> int:
        self.balances[currency] = self.balances.get(currency, 0) + amount
        return self.balances[currency]

    def give_money(self, creditor: object, currency: str, amount: int) -> int:
        new_balance = self.balances.get(currency, 0) - amount
        if new_balance >= 0:
            self.balances[currency] = new_balance
            creditor.deposit_money(currency, amount)
        return self.balances[currency]

    def display_balances(self):
        print(self.balances)


mark_wallet = Wallet("Marks International Wallet")
peter_wallet = Wallet("Peter Wallet")
mark_wallet.deposit_money("GBP", 200)
mark_wallet.spend_money("GBP", 100)
mark_wallet.give_money(peter_wallet, "GBP", 100)
mark_wallet.display_balances()
peter_wallet.display_balances()
print(mark_wallet.name)
print(mark_wallet)
