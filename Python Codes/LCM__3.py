def LCM_2(x, y):
    lcm = x*y
    for i in range(x, y+1):
        if i%x ==0 and i%y == 0:
            lcm = i;
    return lcm


print(LCM_2(7, 3))
