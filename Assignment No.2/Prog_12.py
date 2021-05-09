#Problem No.12

import random
import statistics
def mean(listA):
    i = 0
    sum = 0
    while i < len(myList):
        sum += myList[i]
        i += 1
    print("Mean: ", sum/(len(myList)))


myList =[]
i = 1
while i <= 10:
    myList.append(random.randint(0, 10))
    i += 1
print(myList)
mean(myList)
myList.sort()
print(myList)
print("Median : ", (myList[i//2]+ myList[(i//2)-1])/2)
print("Mode : ", statistics.mode(myList))


