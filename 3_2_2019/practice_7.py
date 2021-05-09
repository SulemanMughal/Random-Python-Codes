name = "Suleman Shahid Mehmood Mughal"

print(name)


#Simple Program...
A = []

for letter in name:
    A.append(letter)


print(A)




#List Comprehensions ...


A = [letter for letter in name]

print(A)


A = [x for x in range(11)]

print(A)


A = [x**2 for x in range(11)]

print(A)


A = [x for x in range(101) if x%2==0]

print(A)

A = [x for x in range(101) if x%2!=0]

print(A)


