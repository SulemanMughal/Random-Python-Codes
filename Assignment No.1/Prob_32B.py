#Problem No.32B

row = int(input("Enter the size of the triangle: "))

i = row
while i >= 0:
    j = i
    while j > 0 :
        print("*", end = '')
        j -= 1
    i -= 1
    print()

