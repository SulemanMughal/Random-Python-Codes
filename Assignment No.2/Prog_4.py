#Problem No.4

def octalEqual(num):
    remainder  = 0
    sum =0
    i = 0
    while num > 0 :
        remainder = num % 8
        sum += (remainder * (10**i))
        i += 1
        num //= 8

    print(sum)
