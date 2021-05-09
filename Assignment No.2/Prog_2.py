#Problem No.2

def primeFactor(num):
    i = 2
    while i <= num:
        if num % i == 0:
            if prime(i):
                print(i)
                num //= i
                i = 2
        else:
            i += 1
                    

def prime(num):
    j = 2
    while j < num:
        if num%j == 0:
            break
        j += 1
    if ( j == num):
        return True
    else:
        return False
