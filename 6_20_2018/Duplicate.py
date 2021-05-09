def Duplicate(A):
    B = [A[0], ]
    i = 1
    while i < len(A):
        if A[i] in B:
            i += 1
        else:
            B.append(A[i])
            i += 1

    return B

            
            
