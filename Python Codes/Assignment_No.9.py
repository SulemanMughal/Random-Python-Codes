def multipleSix(string):
    num = int(string)
    listA = []
    for i in range(num+1):
        if i % 6 == 0:
            listA.append(i)

    print(listA)

multipleSix(1234566)
