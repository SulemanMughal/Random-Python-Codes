def AlphabetSoup(string):
    listA = []
    for i in range(len(string)):
        listA.append(string[i])


    for i in range(len(string)):
        for j in range(len(string)):
            if listA[i] < listA[j]:
                temp = listA[i]
                listA[i] = listA[j]
                listA[j] = temp

    print(listA)
    
    result = ""
    i = 0
    for i in range(len(string)):
        result += listA[i]

    print(result)
    return result


AlphabetSoup('hello')
