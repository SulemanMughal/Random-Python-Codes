def user_remove(listA, n):
    listB = []
    j = 0
    if n in listA:
        for i in range(len(listA)):
            if listA[i] == n:
                j = i
                break
            else:
                listB.append(listA[i])

        if j+1 < len(listA):
            for i in range(j+1, len(listA)-1):
                listB.append(listA[j])

        return listB
    else:
        return -1
