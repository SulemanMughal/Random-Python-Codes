read = open('textfile.txt', 'r+')

print(read.readline())

print(read.readline())

read.close()

print('File closed: ', read.closed)

