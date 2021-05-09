A =  [1, 2, 3, 4, 45]
print(A)

print(A.index(2))

print(A.count(2))
B = A.copy()

print(B)

print(A)

del B[1]
print(B)
print(A)

print(id(B))
print(id(A))
