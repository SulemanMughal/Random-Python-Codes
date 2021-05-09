def overlapping(a, b):
    for i in a:
        if i in b:
            return "True"
    return "False"
