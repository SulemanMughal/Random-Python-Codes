def sixmultiplt(string):
    listA = []
    word = ''
    for i in range(len(string)):
        if int(string[i])%6 == 0:
                listA.append(string[i])
        for j in range(i+1, len(string)):
            word = string[i] + string[j]
            if int(word)%6 == 0:
                listA.append(word)
    print(listA)
    print(len(listA))

sixmultiplt('1234566')
