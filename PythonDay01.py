# MarkS - Python Challenge Day 01 - Abstraction

CALENDAR_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
character_name = "Jimmy The Snowman"
year_of_birth = 1945
month_of_birth = 4
day_of_birth = 1
date_of_birth = (year_of_birth, month_of_birth, day_of_birth)

character_sex = "Male"
character_alive = True

print("Character's Name:", character_name)
print("Character Born:", day_of_birth, CALENDAR_MONTHS[month_of_birth], year_of_birth)

if character_alive:
    print("Character Is Alive")
else:
    print("Character Is Dead")
