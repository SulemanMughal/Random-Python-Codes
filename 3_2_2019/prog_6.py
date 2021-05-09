#Write a program which accepts a sequence of comma-separated numbers from
#console and generate a list and a tuple which contains every number.

string = input("Enter numbers : ")

A = string.split(",")
B = tuple(A)

print(A)
print(B)

