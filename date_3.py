from datetime import date

wd = date.weekday(date.today())


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print("Today's Day Number :", wd, end="")
print(" which is a " + days[wd])
