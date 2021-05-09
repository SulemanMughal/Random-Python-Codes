def  nthRoot(x, Root):
    m= 0
    n=0
    for i in range(1, x):
        for j in range(0, (x-i**Root)+1):
            if (pow(i, Root) + j) == x:
                m = i
                n = j
                break
            
    k =m+ (n/(Root * pow(m, Root-1)))
    print("K = " , k)
    print("Original Value = " , pow(x, 1/Root))
    print("Error: " , abs((pow(x, (1/Root)))-k))
    
