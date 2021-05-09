#Problem no.5

def rangeOwn(start, stop, step):
    myList = []
    while start < stop:
        myList.append(start)
        start += step
    return myList
