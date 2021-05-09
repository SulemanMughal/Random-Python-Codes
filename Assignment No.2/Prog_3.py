#Problem No.3

def armStrong(num):
    i = num
    if (sumOfDigits(i) == num):
        return True
    else:
        return False

def sumOfDigits(num):
    remainder = 0
    sum = 0
    while num !=0:
        remainder = num % 10
        sum += cube(remainder)
        num //= 10
    return sum

def cube(num):
    return (num ** 3)
