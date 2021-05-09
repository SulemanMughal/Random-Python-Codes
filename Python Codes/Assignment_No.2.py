def findVowels(string):
    i = 0
    listC = []
    for i in range(len(string)):
        if string[i] == 'a' or  string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
            listC.append(string[i])
    return listC

def addVowels(listA, listB):
    #listA and listB treated as strings
    #find vowels from both strings
    vowelA = findVowels(listA)
    vowelB = findVowels(listB)
    i = 0
    j = 0
    vowelC = []

    print(vowelA)
    print(vowelB)
    for i in range(min(len(vowelA), len(vowelA))):
        vowelC.append( vowelA[i] + vowelB[i]  )  
        j +=1

    print(i)
    if len(vowelA) > len(vowelB):
        for j in range(len(vowelA)-i-1):
            vowelC.append(vowelA[j+i+1])
    else:
        for j in range(len(vowelB)-i-1):
            vowelC.append(vowelB[j+i+1])

            
    print(vowelC)
    return vowelC
