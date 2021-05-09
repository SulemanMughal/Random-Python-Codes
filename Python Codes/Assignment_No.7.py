def lone_sum(x, y, z):
    if x != y and x != z and y != z:
        return x+y+z
    elif x== y and y!=z:
        return z
    elif x == z and x != y:
        return y
    elif y == z and x != y:
        return x
    else:
        return 0

print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))
