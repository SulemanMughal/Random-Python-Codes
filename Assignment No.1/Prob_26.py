#Problem No.26

x = int(input("Enter The Ending Index: "))
for i in range(1, x):
    if i%2 == 0 and i%3 == 0:
        print(i)
