x = int(input('Enter an integer : '))
ans = 0

while ans**3 < abs(x):
    ans = ans+1
    if ans**3 != abs(x):
        print(x, ' is not a perfect cube')
    else:
        if x < 0:
            print('Cube Root of  ' ,x , ' is ', ans)
    
