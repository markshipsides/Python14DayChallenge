# MarkS - Python Challenge Day 09 - Exceptions
from PythonDay08Mod import *

while True:
    try:
        minimum_rating = int(input("Please Enter Minimum rating value between 0-100: "))
        break
    except ValueError as err:
        # error_message = str(err)
        # print(error_message)
        print("Not an integer")
print(meet_ratings(BASIC_SUPERPOWERS, minimum_rating))

chosen_currency, currency_amount = input("Please Enter a Currency and Amount to spend: ").split()
currency_amount = int(currency_amount)
print(amount_spent(MY_WALLET, chosen_currency, currency_amount))
