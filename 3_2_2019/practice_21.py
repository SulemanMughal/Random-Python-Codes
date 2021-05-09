def user_remove(listA, n):
    for i in range(len(listA)):
        if listA[i] == n:
            continue
        listA[i] = listA[i]

    return listA
