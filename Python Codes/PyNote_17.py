def is_pangram(phrase):
    string = "abcdefghijklmnopqrstuvwxyz"
    string = list(string)
    for a in phrase:
        if a ==" ":
            pass
        elif a in string:
            i = string.index(a)
            string.pop(i)

    if len(string) == 0:
        return True
    return False
