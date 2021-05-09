#Problem No.6

def binary2Decimal(num):

    sum = 0
    remainder = 0
    i = 0
    while num != 0:
        remainder = num %10
        sum += (remainder * (2 ** i))
        num //= 10
        i += 1

    print("Decimal Equilvalent: ", sum)
    
