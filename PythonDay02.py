# MarkS - Python Challenge Day 02 - Logic

CALENDAR_MONTHS: tuple = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
new_superpower: str
character_name: str = "Jimmy The Snowman"
character_sex: str = "Male"
year_of_birth: int = 1945
month_of_birth: int = 4
day_of_birth: int = 1
character_alive: bool = True
BASIC_SUPERPOWERS: tuple = ("Flight", "Speed")
extended_superpowers: list = list(BASIC_SUPERPOWERS)

print("Character's Name:", character_name)
print("Character Born:", day_of_birth, CALENDAR_MONTHS[month_of_birth], year_of_birth)
print(BASIC_SUPERPOWERS[:])
new_superpower = input("Please add a Superpower: ")

if new_superpower in extended_superpowers:
    print("Sorry " + new_superpower + " already exists")
else:
    extended_superpowers.append(new_superpower)

print("Full list of superpowers", extended_superpowers[::-1])
