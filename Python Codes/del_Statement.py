a = [1, 2, 3, 4]

print(a)

del a[0]

print(a)

del a[len(a)-1]

print(a)

a = a+a

print(a)

a = a*3

print(a)

del a[2:6]

print(a)

del a[:]

print(a)

a = [1, 2, 3]*2
print(a)

del a
#print(a)
