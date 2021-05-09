#Problem No.32D

row  = int(input("Enter the size of the triangle: "))

i = 0
while i != row:
    space = 0
    while space != (row - i ):
        print(" ", end = '')
        space += 1
    j = 0
    while j <= i:
        print(" *", end = '')
        j += 1
    print("")
    i += 1

    
