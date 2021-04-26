# MarkS - Python Challenge Day 04 - Composition

BASIC_SUPERPOWERS: dict = {"Flight": 51, "Speed": 90, "Strength": 50, "Sight": 30}
MY_WALLET: dict = {"USD": 170, "GBP": 50, "EUR": 30, "YEN": 50}


def meet_ratings(rating_dict, rating_minimum):
    rating_name: str
    rating_value: int
    rating_list: list = []
    for rating_name, rating_value in rating_dict.items():
        if rating_value >= rating_minimum:
            rating_list.append(rating_name)
    return rating_list


def amount_spent(wallet, currency, currency_spent):
    currency_available: int
    currency_spent: int
    currency_available = wallet.get(currency, 0)
    if currency_available > currency_spent:
        currency_available = currency_spent
    return currency_available


minimum_rating = int(input("Please Enter Minimum rating value: "))
print(meet_ratings(BASIC_SUPERPOWERS, minimum_rating))

chosen_currency = input("Please Select a currency: ")
currency_amount = int(input("Please choose an amount to spend: "))
print(amount_spent(MY_WALLET, chosen_currency, currency_amount))
