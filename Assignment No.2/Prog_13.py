#Problem No.13

def duplicate(ListA):
    i = 0
    while i < len(ListA):
        j = i+1
        while j < (len(ListA)):
            if ListA[i] == ListA[j]:
                ListA.pop(j)
                j -= 1
            j += 1
        i += 1

    return ListA
