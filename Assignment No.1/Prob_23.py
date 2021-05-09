#Problem No.23

positive = 0
zero = 0
negative = 0
print("Enter -1 to End enter the numbers....")
num = float(input("Enter a Number: "))

while num != -1:
    if num > 0:
        positive += 1
    elif num == 0:
        zero += 1
    else:
        negative += 1
    num = float(input("Enter Number : "))

print("Positive Number : ", positive)
print("Negative Number : ", negative)
print("Zero            : ", zero)
