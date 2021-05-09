def multipleSix(string):
    listA = []
    for i in range(len(string)):
        for j in range(len(string)-1):
            if int(string[i])  % 6 == 0:
                if string[i] not in listA:
                    listA.append(string[i])
            if (i+j)<len(string):   
                word = string[i] + string[i+j]
            if int(word) %6 == 0:
                if word not in listA:
                    listA.append(word)
    print(listA)
    print("Number of Subsequences divisble by 6 : " , len(listA)) 
    return len(listA)
    

multipleSix('1234566')
