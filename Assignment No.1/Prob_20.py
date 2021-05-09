#Problem No. 20

import math
print("Enter your marks in the following subject")

subA = float(input("Enter the marks in subject A: "))
subB = float(input("Enter the marks in subject B: "))

if subA >= 55 and subB >= 45:
    print("Passed")
elif (subA >= 45 and subA < 55) and subB >= 55:
    print("Passed")
elif subB <= 45 and subA >= 65 :
    print("Reappear")
else:
    print("Failed")
