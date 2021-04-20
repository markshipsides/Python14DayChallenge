# MarkS - Python Challenge Day 02 - Logic

CALENDAR_MONTHS: tuple = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
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
print("Hello")
if character_alive:
    print("Character Is Alive")
else:
    print("Character Is Dead")
