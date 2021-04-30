# MarkS - Python Challenge Day 11main - Object-oriented programming
from PythonDay11mod import *

mark_wallet = Wallet("Marks International Wallet", {"USD": 0, "GBP": 0, "EUR": 0, "YEN": 0})
peter_wallet = Wallet("Peter Wallet", {"USD": 0, "GBP": 0, "EUR": 0, "YEN": 0})
mark_wallet.deposit_money("GBP", 375)
mark_wallet.spend_money("GBP", 100)
mark_wallet.transfer_money(peter_wallet, "GBP", 50)
mark_wallet.display_balances()
peter_wallet.display_balances()