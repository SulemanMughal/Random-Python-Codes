#Problem No. 30

num = int(input("Enter the size of the square (in between 1 to 20) :"))
i = 0
j = 0
while i != num:
    while j != num:
        print("*", end='')
        j += 1
    print()
    i += 1
    j = 0

