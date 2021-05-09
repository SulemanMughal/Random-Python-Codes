def LCM(x, y):
    gcd = 1
    for i in range(2, min(x, y)+1):
        if x%i ==0 and y%i ==0:
            gcd = i

    return ((x*y)/gcd)


print(LCM(13,26))
