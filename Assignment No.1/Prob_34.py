#Problem No.34

row  = int(input("Enter the size of the diamond: "))

i = 0
n = 1
while i <= (row):
    j = 1
    if i <= (row/2):
        while j <= (2 * i - 1):
            print("*", end = '')
            j += 1
    else:
        while j <= (row-i)*2-1:
           print("*", end = '')
           j += 1
    print()
    i += 1
    
