def reverseNumber(number):
    new=0
    while(number != 0):
        new = (number%10)+new*10
        number //= 10

    print(new)
    
