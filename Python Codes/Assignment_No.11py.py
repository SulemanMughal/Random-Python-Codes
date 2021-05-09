def AlphabetSoup(string):
    result = ''
    for i in range(len(string)):
        for j in range(len(string)):
            if string[i]<string[j]:
                result += string[i]

    print(result)


AlphabetSoup('hello')
