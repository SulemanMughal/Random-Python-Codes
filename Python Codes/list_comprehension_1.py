matrix = [[1, 2], [3, 4], [5, 6]]

print(matrix)

A = []
for i in matrix:
    for j in i:
      A.append(j)

print(A)

print([[row[i] for row in matrix] for i in range(2)])
