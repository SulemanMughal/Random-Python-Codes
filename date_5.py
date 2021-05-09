from datetime import datetime

#Current date and time
now = datetime.now()

print("Current date and  time : ", now)

#Indicates the local date and time
print(now.strftime("%c"))

#Yet unknown...
print(now.strftime("%C"))

#local date
print(now.strftime("%x"))

#local time
print(now.strftime("%X"))

#Formatting Time...

print(now.strftime("%I:%M:%S %p"))

print(now.strftime("%H:%M:%S"))
