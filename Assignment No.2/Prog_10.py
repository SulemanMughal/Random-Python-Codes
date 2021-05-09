#Problem No.10

def perfect():
    i = 1
    print("Perfect Numbers: ")
    while i <= 1000:
        sum = 0
        j = 1
        while j < i:
            if (i % j == 0):
                sum += j
            j += 1
        if (sum == i):
            print(i)
        i += 1
        
        
