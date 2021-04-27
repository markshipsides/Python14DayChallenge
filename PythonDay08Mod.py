# MarkS - Python Challenge Day 08Mod - Re-usability
from typing import List

BASIC_SUPERPOWERS: dict = {"Flight": 51, "Speed": 90, "Strength": 50, "Sight": 30}
MY_WALLET: dict = {"USD": 170, "GBP": 50, "EUR": 30, "YEN": 50}
ratings = List[str]


def meet_ratings(rating_dict: dict, rating_minimum: int) -> ratings:
    rating_list: list = []
    for rating_name, rating_value in rating_dict.items():
        if rating_value >= rating_minimum:
            rating_list.append(rating_name)
    return rating_list


def amount_spent(wallet: dict, currency: str, currency_spent: int) -> int:
    currency_available: int = wallet.get(currency, 0)
    if currency_available > currency_spent:
        currency_available = currency_spent
    return currency_available
