#Problem No. 31:

row = int(input("Enter the number of rows: "))

print("********")

while row != 0:
    if (row%2 == 0):
        print("********")
    else:
        print(" ********")
    row -= 1
