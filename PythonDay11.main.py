# MarkS - Python Challenge Day 11main - Object-oriented programming
from PythonDay11mod import *

mark_wallet = Wallet()
mark_wallet.name = "Marks International Wallet"
mark_wallet.balances = {"GBP": 100, "EUR": 80}
new_gbp_balance = mark_wallet.spend_money("GBP",50)
