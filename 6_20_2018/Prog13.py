readFile = open('NEWS.txt', 'r')

for line in readFile:
    print(line)

readFile.close()
