for n in range(2, 11):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n , 'is a prime number')
        