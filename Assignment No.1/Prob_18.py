#Problem No.18

lateDate = int(input("Enter the number of days the memeber is late to return the book : "))

if lateDate > 0 and lateDate <= 5 :
    print("The Fine is 50 paise")
elif lateDate >= 6 and lateDate <= 10:
    print("The Fine is 1 rupee")
if lateDate > 10 and lateDate <= 30:
    print("The fine is 5 rupees")
if lateDate > 30 :
    print("Your membership has been cancelled")
