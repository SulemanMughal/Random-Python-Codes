#Problem No.32C

row = int(input("Enter the size of the triangle: "))

i = row
line = 0
while i > 0:
    j = i
    line += 1
    row = line
    while (row > 1):
        print(" ", end = '')
        row -= 1
    while (j > 0):
        print("*", end = '')
        j -= 1
    print("")
    i -= 1
    
    
