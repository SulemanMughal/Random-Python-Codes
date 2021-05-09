#Problem No. 7

number = int(input("Enter a five digit number: "))

sum  = 0
remainder = 0
while number != 0:
    remainder = number % 10
    sum = sum + remainder
    number = number//10

print("Sum of digits is ", sum)
