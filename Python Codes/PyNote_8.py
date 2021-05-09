def reverse_String(string):
    reverseString = ""
    for i in range(len(string), 0, -1):
        reverseString += string[i-1]

    return reverseString


def is_palindrome(string):
    if string == reverse_String(string):
        return "True"
    return "False"
