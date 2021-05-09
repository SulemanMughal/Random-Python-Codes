def LCM(x, y):
    lcm = 1
    for i in range(2, max(x, y)):
        if x%i ==0 and y%i ==0:
            lcm = i
            print(lcm)

    return ((x*y)/lcm)

        
print(LCM(35,13))
