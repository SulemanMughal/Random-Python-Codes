#Problem No.24

num = int(input("Enter a Number: "))
sum = 0
i = 0
while num != 0:
    sum += (num%2) * 10**i 
    num = num//2
    i += 1

print("Binary Equivalent : ", sum)
