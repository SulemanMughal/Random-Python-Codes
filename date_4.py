from datetime import datetime

#Get current date and time

now = datetime.now()

print("Current Date and Time ", now)

#Date Formatting...........
print(now.strftime("%Y"))
print(now.strftime("%y"))


#Change the complete format of the date......
print(now.strftime("%a, %d %B, %y"))


print(now.strftime("%A,  %d %B, %Y"))

print(now.strftime("%a, %d %b, %Y"))

print(now.strftime("%a, %d %B, %y"))

print(now.strftime("%a, %d %b, %y"))
