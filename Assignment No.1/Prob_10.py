#Problem No.10

year = int(input("Enter the Year: "))

if (year%100 != 0 or year%400 == 0) and (year%4 ==0):
    print("Leap Year")
else:
    print("Not Leap Year")
