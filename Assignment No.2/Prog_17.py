#Problem No.17

def swap(ListA):
    temp = ListA[:1]
    ListA[:1] = ListA[len(ListA)-1 :]
    ListA[len(ListA)-1:] = temp
    del temp
    return ListA
