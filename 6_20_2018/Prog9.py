a = [1 , 2, 1, 3, 4, 5, 9, 3, 4, 2, 7, 6, 8]

print(a)

def counting(a):
        
    i = 0
    while (i < len(a)):
        j = i+1
        while (j < len(a)):
            if a[j] == a[i]:
                print(a[j])
            j += 1
        i += 1

