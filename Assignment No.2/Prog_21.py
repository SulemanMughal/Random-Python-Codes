#Problem No.21

def ion2e(string):
    if "ion" in string:
        return  string.replace("ion", "e")
    else:
        return string
