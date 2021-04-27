# MarkS - Python Challenge Day 08Main - Re-usability
from PythonDay08Mod import *

minimum_rating = int(input("Please Enter Minimum rating value: "))
print(meet_ratings(BASIC_SUPERPOWERS, minimum_rating))

chosen_currency = input("Please Select a currency: ")
currency_amount = int(input("Please choose an amount to spend: "))
print(amount_spent(MY_WALLET, chosen_currency, currency_amount))
