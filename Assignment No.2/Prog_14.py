#Problem No.14

def minimum(Tuple):
    min = Tuple[0]
    i = 1
    while i < len(Tuple):
        if Tuple[i] < min:
            min = Tuple[i]
        i += 1
    return min
