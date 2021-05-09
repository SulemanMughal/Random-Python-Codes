A = [1, 2, 3, 4, 5, 6]
print(A)

A[len(A):]= [5, 6, 7, 8]
print(A)
#Error
#A[5:] = 6
A[5] = [5, 6, 7, 8]
print(A)


l = [2]

print(l)

l.append(1)

print(l)


l.insert(0, -1)

print(l)

l.extend([4, 5])

print(l)
