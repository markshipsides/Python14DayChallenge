# MarkS - Python Challenge Day 02 - Logic

CALENDAR_MONTHS: tuple = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
BASIC_SUPERPOWERS: tuple = ("Flight", "Speed")

character_name: str = "Jimmy The Snowman"
character_sex: str = "Male"
year_of_birth: int = 1945
month_of_birth: int = 4
day_of_birth: int = 1
character_alive: bool = True

extended_superpowers: list = list(BASIC_SUPERPOWERS)
new_superpower: str

print("Character's Name:", character_name)
print("Character Born:", day_of_birth, CALENDAR_MONTHS[month_of_birth], year_of_birth)

new_superpower = input("Please add a Superpower: ")

if new_superpower in extended_superpowers:
    print("Sorry " + new_superpower + " already exists")
else:
    extended_superpowers.append(new_superpower)
    print("Thank you, " + new_superpower + " added")

print("Full list of Superpowers ", extended_superpowers[::-1])
