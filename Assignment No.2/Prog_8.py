#Problem No.8

def square(size, character):
    i = 0
    while i < size:
        j = 0
        while j < size:
            print(character, end = '')
            j += 1
        print()
        i += 1

