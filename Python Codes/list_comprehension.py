print([x for x in range(6) if x %2 != 0])

print([y for y in range(1, 10) if y %2 == 0])

print([x for x in range(10, 26) if x %2 != 0])

print([x**3 for x in range(10)])

vec  = [-3, 0, 1, 2]

print([x**2 for x in vec])

print([x for x in vec if x>=0])

print([abs(x) for x in vec])

print([(x, x**2) for x in vec])

vec = [[1], [2], [3]]

print([num for elem in vec for num in elem if num%2 != 0])
