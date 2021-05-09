def user_remove(listA, n):
    listB = []
    j = 0
    if n in listA:
        for i in range(len(listA)):
            if listA[i] == n:
                for j in range(j+1, len(listA)-1):
                    listB.append(listA[j+1])
                break
            else:
                listB.append(listA[i])

    print(listB)
    
