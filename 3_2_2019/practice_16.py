def prime(n, x):
    i = 1
    j = 1
    while j <= n:
        if x[i] == 1:
            j = j+1
        i = i+1

    return i-1

