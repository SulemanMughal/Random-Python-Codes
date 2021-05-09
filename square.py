def square(n):
    return n*n



numbers= list(range(11))

for item in map(square, numbers):
    print(item)
    

print(list(map(square, numbers)))


def check_even(n):
    return n%2 == 0

print(list(filter(check_even, numbers)))