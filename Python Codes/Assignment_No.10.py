def LongestWord(string):
    listA = []
    word = ''

    for i in range(len(string)):
        if string[i] != ' ':
            word += string[i]
        else:
            listA.append(word)
            word = ''

    for j in range(len(string)):
        if string[i] == ' ':
            word = string[i:]
    
    listA.append(word)
    i = 0
    j = 0
    maxWord = ' '
    for i in range(len(listA)):
        if len(listA[i]) > len(maxWord):
            maxWord = listA[i]            

    return maxWord
    
    
LongestWord("university of engineering and technology")
