readFile  = open('Hello.txt', 'r')

for line in readFile:
    print(line)


print("File Name: ", readFile.name)

readFile.close()
