def maximum(x,y):
    if x > y:
        return x
    return y

def maximum3(x, y,z):
    return maximum(x, maximum(y,z))
