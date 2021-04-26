# MarkS - Python Challenge Day 04 - Composition

BASIC_SUPERPOWERS: dict = {"Flight": 51, "Speed": 90, "Height": 30}
WALLET: dict = {"USD": 170, "GBP": 50, "EUR": 30, "YEN": 50}



def power_hits(powers, power_rating):
    power_list: list = []
    for power, rating in powers.items():
        if rating > power_rating:
            power_list.append(power)
    return (power_list)

print(power_hits(BASIC_SUPERPOWERS, 10))