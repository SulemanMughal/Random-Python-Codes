#Problem No.29

row = int(input("Enter the number of rows: "))
k = 0
l = 0
if row <= 10 :    
    for i in range(0, row):
        for k in range(0, row-i):
            print("\t", end = '')
        for j in range(0, i+1):
            l += 1
            print(l, "\t\t", end = '')
        print("\n")


        
