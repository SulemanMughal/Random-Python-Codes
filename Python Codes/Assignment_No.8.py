def compressedString(string):
    i = 0
    j = 0
    count =0
    resultString= ''
    for i in range(len(string)):
        if string[i] in string:
            count += 1

    print(count)

compressedString('ABCABCBC')
