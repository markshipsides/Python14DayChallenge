# MarkS - Python Challenge Day 03 - Flow control

CALENDAR_MONTHS: tuple = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
BASIC_SUPERPOWERS: dict = {"Flight": 51, "Speed": 90}
SUPERPOWER_UPPER_LIMIT = 80
SUPERPOWER_LOWER_LIMIT = 50


character_name: str = "Jimmy The Snowman"
character_sex: str = "Male"
year_of_birth: int = 1945
month_of_birth: int = 4
day_of_birth: int = 1
character_alive: bool = True

extended_superpowers = BASIC_SUPERPOWERS
new_superpower: str
new_superpower_rating: int

print("Character's Name:", character_name)
print("Character Born:", day_of_birth, CALENDAR_MONTHS[month_of_birth], year_of_birth)
print("Basic superpowers are: ", BASIC_SUPERPOWERS)

new_superpower = input("Please add a Superpower: ")
new_superpower_rating = int(input("Please add a rating (0-100) for " + new_superpower + ": "))
extended_superpowers[new_superpower] = new_superpower_rating

print("Full list of Superpowers ", extended_superpowers)

superpower_test = input("Please enter Superpower to test rating: ")
superpower_test_value = extended_superpowers[superpower_test]

if superpower_test_value > SUPERPOWER_UPPER_LIMIT:
    print("SUPER COOL")
elif superpower_test_value > SUPERPOWER_LOWER_LIMIT:
    print("COOL")
