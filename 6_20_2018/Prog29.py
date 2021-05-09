read = open('Hello.txt', 'r')

for line in read:
    print(line, end = '')

read.close()

print('File closed: ', read.closed)
