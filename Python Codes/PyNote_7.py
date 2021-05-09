def reverse_String(string):
    reverseString = ""
    for i in range(len(string), 0, -1):
        reverseString += string[i-1]

    return reverseString
