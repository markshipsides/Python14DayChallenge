# MarkS - Python Challenge Day 09 - Exceptions
from PythonDay08Mod import *

while True:
    try:
        minimum_rating = int(input("Please Enter Minimum rating value between 0-100: "))
        break
    except ValueError:
        print("Not an integer")

print(meet_ratings(BASIC_SUPERPOWERS, minimum_rating))
chosen_currency = input("Please Select a currency: ")
currency_amount = int(input("Please choose an amount to spend: "))
print(amount_spent(MY_WALLET, chosen_currency, currency_amount))
