#Problem No. 32A

row = int(input("Enter the size of the triangle: "))

i = 0
j = 0
while i <= row:
    while j < i :
        print("*", end = '')
        j += 1
    i += 1
    j = 0
    print()

