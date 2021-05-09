def findSequence(listA):
    i = 0
    j = 0
    for  i in range(len(listA)):
        if listA[i] == 1:
            if  (i+1) < len(listA) and listA[i+1] == 2:
                if (i+2) < len(listA) and listA[i+2] == 3:
                    return True

    return False

listA = [1, 1, 2,  1, 2, 3]
print(findSequence(listA))
