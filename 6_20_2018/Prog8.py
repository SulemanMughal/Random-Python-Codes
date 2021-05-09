a = [1, 2, 1, 3, 5,5, 10, 6, 6,10]
print(a)

a.sort()
print(a)
for i in a:
    j = a.count(i)
    if (j > 1):
        a.remove(i)

print(a)
