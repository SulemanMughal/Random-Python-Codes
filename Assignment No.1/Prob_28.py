#Problem No.28

num = int(input("Enter a non-negative number: "))
factorial = 1
while num != 1:
    factorial = factorial * num
    num -= 1
print("Factorial : ", factorial)
