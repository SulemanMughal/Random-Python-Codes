def bubbleSort(listA):
    for num in range(len(listA)-1,0,-1):
        for i in range(num):
            if listA[i]>listA[i+1]:
                temp = listA[i]
                listA[i] = listA[i+1]
                listA[i+1] = temp
    #list is sorted in Ascending order.....
    print(listA[len(listA)-3], listA[0])
    return (listA[len(listA)-3], listA[0])


listA = [54,26,93,17,77,31,44,55,20]
bubbleSort(listA)
print(listA)
