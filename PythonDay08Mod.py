# MarkS - Python Challenge Day 08Main - Re-usability

def meet_ratings(rating_dict: dict, rating_minimum: int) -> list:
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
