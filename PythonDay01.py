# Mark Shipsides - Python Challenge Day 01 - Abstraction

CalendarMonths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
CharacterName = "Jimmy The Snowman"
YearOfBirth = 1945
MonthOfBirth = 4
DayOfBirth = 1
DateOfBirth = (YearOfBirth,MonthOfBirth,DayOfBirth)

CharacterSex = "Male"
CharacterAlive = True

print("Character's Name:", CharacterName)
print("Character Born:", DayOfBirth, CalendarMonths[MonthOfBirth], YearOfBirth)

if CharacterAlive:
    print("Character Is Alive")
else:
    print("Character Is Dead")
